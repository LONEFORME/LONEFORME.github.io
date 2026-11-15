(() => {
  const search = document.getElementById('news-search-input');
  if (!search) return;
  const categories = [...document.querySelectorAll('.news-category')];
  const items = [...document.querySelectorAll('.news-item')];
  const hero = document.querySelector('.news-hero');
  const channels = [...document.querySelectorAll('.channel-btn')];
  const count = document.getElementById('news-search-count');
  const readKey = 'loneforme_read_news';
  let channel = 'all', source = '', unread = false, sort = 'latest', read = [];
  const expanded = new Set();
  const limit = 6;
  try {
    const stored = JSON.parse(localStorage.getItem(readKey) || '[]');
    if (Array.isArray(stored)) read = stored.filter(value => typeof value === 'string');
  } catch {}

  const tools = document.createElement('div');
  tools.className = 'news-filter-tools';
  tools.innerHTML = '<label>信源 <select id="news-source-filter" aria-label="筛选新闻信源"><option value="">全部信源</option></select></label>' +
    '<label>排序 <select id="news-sort" aria-label="新闻排序"><option value="latest">最新优先</option><option value="earliest">最早优先</option></select></label>' +
    '<label class="news-unread-label"><input type="checkbox" id="news-unread"> 仅看未读</label>' +
    '<button type="button" id="news-clear-filters">重置筛选</button>';
  document.querySelector('.news-header-box').append(tools);
  search.setAttribute('aria-label', '搜索新闻');
  search.placeholder = '搜索标题、摘要、人物或信源';
  count.setAttribute('role', 'status');
  count.setAttribute('aria-live', 'polite');
  const sourceSelect = tools.querySelector('#news-source-filter');
  const sourceCounts = new Map();
  items.forEach(item => {
    const name = item.dataset.source || '其他';
    sourceCounts.set(name, (sourceCounts.get(name) || 0) + 1);
  });
  for (const [name, total] of [...sourceCounts].sort((a, b) => b[1] - a[1])) {
    const option = new Option(`${name} (${total})`, name);
    sourceSelect.add(option);
  }
  const empty = document.createElement('div');
  empty.className = 'news-empty-state';
  empty.setAttribute('role', 'status');
  empty.hidden = true;
  empty.textContent = '没有符合条件的新闻，请更换关键词或重置筛选。';
  document.querySelector('.news-grid').after(empty);
  const index = new Map(items.map(item => [item,
    `${item.textContent} ${item.dataset.title || ''} ${item.dataset.summary || ''} ${item.dataset.source || ''}`.toLocaleLowerCase()]));
  const originalOrder = new Map(items.map((item, i) => [item, i]));
  const buttons = new Map();
  categories.forEach(category => {
    category.removeAttribute('data-collapse');
    category.querySelector('.news-expand-btn')?.remove();
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'news-expand-btn';
    button.addEventListener('click', () => {
      if (expanded.has(category)) expanded.delete(category);
      else expanded.add(category);
      render();
    });
    category.append(button);
    buttons.set(category, button);
  });
  function render() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const matched = items.filter(item =>
      (channel === 'all' || channel === 'source' || item.dataset.cat === channel) &&
      (!source || item.dataset.source === source) &&
      (!unread || !read.includes(item.getAttribute('href'))) &&
      terms.every(term => index.get(item).includes(term)));
    const matchedSet = new Set(matched);
    const filtering = terms.length > 0 || source || unread;
    for (const category of categories) {
      const members = items.filter(item => category.contains(item) && matchedSet.has(item));
      members.sort((a, b) => {
        const difference = (a.dataset.date || '').localeCompare(b.dataset.date || '');
        return (sort === 'latest' ? -difference : difference) || originalOrder.get(a) - originalOrder.get(b);
      });
      const button = buttons.get(category);
      items.filter(item => category.contains(item)).forEach(item => {
        item.hidden = true;
        item.style.removeProperty('display');
      });
      members.forEach((item, i) => {
        item.hidden = !filtering && !expanded.has(category) && i >= limit;
        category.insertBefore(item, button);
      });
      category.hidden = members.length === 0;
      category.style.removeProperty('display');
      const badge = category.querySelector('.news-category-count');
      if (badge) badge.textContent = `${members.length} 条`;
      button.hidden = Boolean(filtering || members.length <= limit);
      button.setAttribute('aria-expanded', String(expanded.has(category)));
      button.textContent = expanded.has(category) ? '收起列表' : `展开其余 ${members.length - limit} 条`;
    }
    if (hero) hero.hidden = Boolean(channel !== 'all' || filtering);
    if (count) count.textContent = `${matched.length} 条`;
    empty.hidden = matched.length > 0;
    channels.forEach(button => {
      const current = (button.getAttribute('onclick') || '').match(/'([^']+)'/)?.[1] || 'all';
      button.classList.toggle('active', current === channel);
      button.setAttribute('aria-pressed', String(current === channel));
    });
  }
  window.onNewsSearch = render;
  window.restoreNewsCollapse = render;
  window.filterNewsChannel = next => {
    channel = next;
    render();
    if (next === 'source') sourceSelect.focus();
  };
  sourceSelect.addEventListener('change', () => { source = sourceSelect.value; render(); });
  tools.querySelector('#news-unread').addEventListener('change', event => { unread = event.target.checked; render(); });
  tools.querySelector('#news-sort').addEventListener('change', event => { sort = event.target.value; render(); });
  tools.querySelector('#news-clear-filters').addEventListener('click', () => {
    search.value = '';
    source = '';
    channel = 'all';
    unread = false;
    sort = 'latest';
    sourceSelect.value = '';
    tools.querySelector('#news-unread').checked = false;
    tools.querySelector('#news-sort').value = 'latest';
    render();
  });
  const links = [...document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card')];
  function paintRead() {
    links.forEach(link => link.classList.toggle('news-read-card', read.includes(link.getAttribute('href'))));
  }
  links.forEach(link => link.addEventListener('click', () => {
    const href = link.getAttribute('href');
    if (href && !read.includes(href)) read.push(href);
    read = read.slice(-300);
    try { localStorage.setItem(readKey, JSON.stringify(read)); } catch {}
    paintRead();
    if (unread) render();
  }));
  const total = items.length;
  const metrics = document.querySelectorAll('.news-overview-bar .ov-num');
  if (metrics[0]) metrics[0].textContent = total;
  if (metrics[1]) metrics[1].textContent = sourceCounts.size;
  if (metrics[2]) metrics[2].textContent = new Set(items.map(item => item.dataset.cat)).size;
  const allBadge = channels[0]?.querySelector('.channel-count');
  if (allBadge) allBadge.textContent = total;
  paintRead();
  render();
})();
