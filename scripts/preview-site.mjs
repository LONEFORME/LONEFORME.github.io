// Local Liquid/Markdown preview for the Jekyll pages; the drone docs use VitePress.
import http from 'node:http';
import { readFile, readdir, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { Liquid } from 'liquidjs';
import matter from 'gray-matter';
import MarkdownIt from 'markdown-it';

const root = fileURLToPath(new URL('../', import.meta.url));
const markdown = new MarkdownIt({ html: true, linkify: true });
const liquid = new Liquid({ root: [path.join(root, '_includes')] });
const site = matter(`---\n${await readFile(path.join(root, '_config.yml'), 'utf8')}\n---`).data;
site.time = new Date();
site.pages = [];
for (const directory of ['', 'docs']) {
  for (const name of await readdir(path.join(root, directory))) {
    if (!name.endsWith('.md') && !name.endsWith('.html')) continue;
    const parsed = matter(await readFile(path.join(root, directory, name), 'utf8'));
    if (parsed.data.title) site.pages.push({
      ...parsed.data, content: parsed.content,
      url: '/' + path.posix.join(directory, name.replace(/\.(md|html)$/, '')),
    });
  }
}
liquid.registerFilter('relative_url', value => value);
liquid.registerFilter('absolute_url', value => `${site.url}${value}`);
liquid.registerFilter('jsonify', value => JSON.stringify(value ?? null));
liquid.registerFilter('normalize_whitespace', value => String(value || '').replace(/\s+/g, ' ').trim());
const escape = value => String(value || '').replaceAll('&', '&amp;').replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;').replaceAll('"', '&quot;');
liquid.registerTag('seo', {
  render(context) {
    return `<title>${escape(context.get(['page', 'title']))} | ${escape(site.title)}</title>`;
  },
});
liquid.registerTag('include', {
  parse(token) {
    this.filename = token.args.match(/^([\w./-]+)/)?.[1];
    if (!this.filename || this.filename.includes('..')) throw new Error('Invalid include');
    this.values = Object.fromEntries([...token.args.matchAll(/(\w+)=(?:"([^"]*)"|'([^']*)')/g)]
      .map(([, key, double, single]) => [key, double ?? single]));
  },
  async render(context) {
    const text = await readFile(path.join(root, '_includes', this.filename), 'utf8');
    return liquid.parseAndRender(text, { ...context.getAll(), include: this.values });
  },
});
const mime = {
  '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.woff2': 'font/woff2', '.mp4': 'video/mp4', '.glb': 'model/gltf-binary',
  '.xml': 'application/xml',
};

async function render(filename, url) {
  const file = matter(await readFile(filename, 'utf8'));
  const page = { ...file.data, url, path: path.relative(root, filename).replaceAll('\\', '/') };
  const rendered = await liquid.parseAndRender(file.content, { site, page });
  const content = filename.endsWith('.md') ? markdown.render(rendered) : rendered;
  if (!file.data.layout) return content;
  // GitHub Pages' default theme supplies `page`, which inherits our default layout.
  const layoutName = file.data.layout === 'page' ? 'default' : file.data.layout;
  const layout = await readFile(path.join(root, '_layouts', `${layoutName}.html`), 'utf8');
  return liquid.parseAndRender(layout, { site, page, content });
}

async function handler(req, res) {
  try {
    const url = new URL(req.url, 'http://localhost');
    const pathname = decodeURIComponent(url.pathname);
    if (pathname.split('/').some(part => part.startsWith('.') || part === 'node_modules' || part === 'scripts')) {
      res.writeHead(404).end(); return;
    }
    const relative = pathname === '/' ? 'index.html' : pathname.slice(1);
    const base = path.resolve(root, relative);
    if (!base.startsWith(root)) { res.writeHead(403).end(); return; }
    const candidates = path.extname(base) ? [base] : [base + '.md', base + '.html', path.join(base, 'index.md'), path.join(base, 'index.html')];
    let filename;
    for (const candidate of candidates) {
      if (await stat(candidate).then(s => s.isFile()).catch(() => false)) { filename = candidate; break; }
    }
    if (!filename) { res.writeHead(404).end('Not found'); return; }
    if (filename.endsWith('search.json')) {
      const json = await render(filename, pathname);
      JSON.parse(json);
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
      res.end(json);
      return;
    }
    if (/\.(md|html)$/.test(filename)) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
      res.end(await render(filename, pathname));
      return;
    }
    if (!mime[path.extname(filename)]) { res.writeHead(404).end(); return; }
    res.writeHead(200, { 'Content-Type': mime[path.extname(filename)], 'Cache-Control': 'no-store' });
    res.end(await readFile(filename));
  } catch (error) {
    console.error(error);
    if (!res.headersSent) res.writeHead(500);
    res.end('Preview rendering failed; see terminal.');
  }
}
if (process.argv.includes('--check')) {
  for (const route of ['/', '/news', '/finance', '/projects', '/docs', '/videos', '/slides', '/3d-viewer']) {
    const base = route === '/' ? path.join(root, 'index') : path.join(root, route.slice(1));
    const filename = await stat(base + '.md').then(() => base + '.md').catch(() => base + '.html');
    const html = await render(filename, route);
    if (!html.includes('<html') || html.includes('{%')) throw new Error(`Unrendered page: ${route}`);
    console.log(`OK ${route}: ${html.length} characters`);
  }
} else {
  const server = http.createServer(handler);
  const listen = port => {
    server.once('error', error => {
      if (error.code === 'EADDRINUSE') { server.removeAllListeners('error'); listen(port + 1); }
      else throw error;
    });
    server.listen(port, '127.0.0.1', () => console.log(`Site preview: http://127.0.0.1:${server.address().port}`));
  };
  listen(Number(process.env.SITE_PREVIEW_PORT) || 4173);
}
