/* ==========================================================================
   DeckKit v2 · 演示文稿控制器
   - 1280×720 固定画布等比缩放（任何屏幕不裁切）
   - 深链：#/3 直达第 3 页
   - O 键目录跳页、F 全屏、Esc 返回列表
   - 内容超框自动兜底缩小，避免投影时被切掉
   - Ctrl+P 直接导出 1280×720 PDF（见 deckkit.css 的 @page 规则）
   ========================================================================== */
(function () {
  'use strict';

  var stage = document.getElementById('deck-stage');
  var canvas = document.querySelector('.deck-canvas');
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var total = slides.length;
  var current = 0;

  var progressBar = document.getElementById('progressBar');
  var currentNum = document.getElementById('currentSlideNum');
  var totalNum = document.getElementById('totalSlidesNum');
  var outline = null;

  if (!stage || !canvas || !total) return;

  /* ---------------- 画布缩放 ---------------- */
  function fitCanvas() {
    var w = window.innerWidth;
    var h = window.innerHeight;
    var hud = parseFloat(
      getComputedStyle(document.documentElement).getPropertyValue('--hud-space')
    ) || 0;
    var scale = Math.min((w - 24) / 1280, (h - hud - 12) / 720);
    if (w <= 720) scale = Math.min(w / 1280, h / 720);
    if (!isFinite(scale) || scale <= 0) scale = 1;
    document.documentElement.style.setProperty('--deck-scale', scale.toFixed(4));
  }

  /* ---------------- 内容超框兜底 ---------------- */
  function autoFitSlides() {
    slides.forEach(function (slide) {
      var body = slide.querySelector('.slide-body');
      if (!body) return;
      body.style.transform = '';
      body.style.transformOrigin = 'center center';
      var over = body.scrollHeight - body.clientHeight;
      if (over > 2) {
        var k = Math.max(0.78, body.clientHeight / body.scrollHeight);
        body.style.transform = 'scale(' + k.toFixed(3) + ')';
        slide.setAttribute('data-dense', '1');
      } else {
        slide.removeAttribute('data-dense');
      }
    });
  }

  /* ---------------- 页码 / 进度 ---------------- */
  function pad(n) { return String(n).padStart(2, '0'); }

  if (totalNum) totalNum.textContent = pad(total);

  function updateSlide(index, skipHash) {
    if (index < 0) index = 0;
    if (index >= total) index = total - 1;
    current = index;

    slides.forEach(function (s, idx) {
      s.classList.remove('active', 'prev');
      s.setAttribute('aria-hidden', idx === current ? 'false' : 'true');
      if (idx === current) s.classList.add('active');
      else if (idx < current) s.classList.add('prev');
    });

    if (progressBar) progressBar.style.width = ((current + 1) / total) * 100 + '%';
    if (currentNum) currentNum.innerHTML = '<b>' + pad(current + 1) + '</b>';

    markOutlineCurrent();
    renderNotes();

    if (!skipHash) {
      try {
        history.replaceState(null, '', '#/' + (current + 1));
      } catch (e) { /* file:// 下可能受限，忽略 */ }
    }
  }

  function next() { updateSlide(current + 1); }
  function prev() { updateSlide(current - 1); }

  function readHash() {
    var m = /^#\/?(\d+)$/.exec(window.location.hash || '');
    if (m) {
      var n = parseInt(m[1], 10) - 1;
      if (n >= 0 && n < total) return n;
    }
    return 0;
  }

  /* ---------------- 目录浮层 ---------------- */
  function buildOutline() {
    outline = document.createElement('div');
    outline.className = 'deck-outline';
    outline.setAttribute('role', 'dialog');
    outline.setAttribute('aria-label', '演示稿目录');

    var titles = slides.map(function (s, i) {
      var el = s.querySelector('.slide-title, .cover-title');
      var text = el ? el.textContent.replace(/\s+/g, ' ').trim() : '第 ' + (i + 1) + ' 页';
      return text || '第 ' + (i + 1) + ' 页';
    });

    var grid = document.createElement('div');
    grid.className = 'outline-grid';

    titles.forEach(function (title, i) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'outline-item';
      btn.dataset.index = String(i);
      btn.innerHTML = '<span class="num">' + pad(i + 1) + '</span>' +
                      '<span class="label">' + escapeHtml(title) + '</span>';
      btn.addEventListener('click', function () {
        updateSlide(i);
        closeOutline();
      });
      grid.appendChild(btn);
    });

    var head = document.createElement('h3');
    head.textContent = '目录 · ' + total + ' 页　（点击跳转，O 键或 Esc 关闭）';

    outline.appendChild(head);
    outline.appendChild(grid);
    document.body.appendChild(outline);
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function openOutline() {
    if (!outline) return;
    markOutlineCurrent();
    outline.classList.add('open');
  }
  function closeOutline() {
    if (outline) outline.classList.remove('open');
  }
  function toggleOutline() {
    if (!outline) return;
    if (outline.classList.contains('open')) closeOutline();
    else openOutline();
  }
  function markOutlineCurrent() {
    if (!outline) return;
    var items = outline.querySelectorAll('.outline-item');
    for (var i = 0; i < items.length; i++) {
      items[i].classList.toggle('is-current', i === current);
    }
  }

  /* ---------------- 讲稿备注（N 键 / ?notes=1） ---------------- */
  var notesPanel = null;

  function buildNotesPanel() {
    var has = slides.some(function (s) { return s.querySelector('.notes'); });
    if (!has) return;
    notesPanel = document.createElement('div');
    notesPanel.id = 'notes-panel';
    notesPanel.innerHTML = '<span class="k">SPEAKER NOTES · N 关闭</span><div class="txt"></div>';
    document.body.appendChild(notesPanel);

    if (/[?&]notes=1/.test(window.location.search)) notesPanel.classList.add('show');
  }

  function renderNotes() {
    if (!notesPanel) return;
    var note = slides[current] && slides[current].querySelector('.notes');
    var txt = notesPanel.querySelector('.txt');
    txt.textContent = note ? note.textContent.replace(/\s+/g, ' ').trim() : '（本页无备注）';
  }

  function toggleNotes() {
    if (!notesPanel) return;
    notesPanel.classList.toggle('show');
  }

  /* ---------------- 全屏 ---------------- */
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      var el = document.documentElement;
      var req = el.requestFullscreen || el.webkitRequestFullscreen;
      if (req) {
        var p = req.call(el);
        if (p && p.catch) p.catch(function () {});
      }
    } else {
      var exit = document.exitFullscreen || document.webkitExitFullscreen;
      if (exit) exit.call(document);
    }
  }

  /* ---------------- 交互绑定 ---------------- */
  var nextBtn = document.getElementById('nextBtn');
  var prevBtn = document.getElementById('prevBtn');
  var fullscreenBtn = document.getElementById('fullscreenBtn');
  var outlineBtn = document.getElementById('outlineBtn');

  if (nextBtn) nextBtn.addEventListener('click', next);
  if (prevBtn) prevBtn.addEventListener('click', prev);
  if (fullscreenBtn) fullscreenBtn.addEventListener('click', toggleFullscreen);
  if (outlineBtn) outlineBtn.addEventListener('click', toggleOutline);

  window.addEventListener('keydown', function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;

    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case ' ':
      case 'PageDown':
        e.preventDefault(); closeOutline(); next(); break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
        e.preventDefault(); closeOutline(); prev(); break;
      case 'f':
      case 'F':
        e.preventDefault(); toggleFullscreen(); break;
      case 'o':
      case 'O':
        e.preventDefault(); toggleOutline(); break;
      case 'n':
      case 'N':
        e.preventDefault(); toggleNotes(); break;
      case 'Home':
        e.preventDefault(); updateSlide(0); break;
      case 'End':
        e.preventDefault(); updateSlide(total - 1); break;
      case 'Escape':
        if (outline && outline.classList.contains('open')) {
          e.preventDefault(); closeOutline();
        } else if (document.fullscreenElement) {
          var exit = document.exitFullscreen || document.webkitExitFullscreen;
          if (exit) exit.call(document);
        } else {
          window.location.href = '/slides/';
        }
        break;
      default: break;
    }
  });

  // 滚轮翻页（笔记本触摸板限流）
  var wheelLock = 0;
  window.addEventListener('wheel', function (e) {
    if (outline && outline.classList.contains('open')) return;
    var now = Date.now();
    if (now < wheelLock) return;
    if (Math.abs(e.deltaY) < 24) return;
    wheelLock = now + 420;
    if (e.deltaY > 0) next(); else prev();
  }, { passive: true });

  // 触控滑动
  var touchStartX = 0;
  var touchStartY = 0;
  window.addEventListener('touchstart', function (e) {
    touchStartX = e.changedTouches[0].clientX;
    touchStartY = e.changedTouches[0].clientY;
  }, { passive: true });
  window.addEventListener('touchend', function (e) {
    if (outline && outline.classList.contains('open')) return;
    var dx = e.changedTouches[0].clientX - touchStartX;
    var dy = e.changedTouches[0].clientY - touchStartY;
    if (Math.abs(dx) < 50 || Math.abs(dx) < Math.abs(dy)) return;
    if (dx < 0) next(); else prev();
  }, { passive: true });

  var rotateDismiss = document.getElementById('rotateDismiss');
  if (rotateDismiss) {
    rotateDismiss.addEventListener('click', function () {
      var hint = rotateDismiss.closest('.rotate-hint');
      if (hint) hint.classList.add('dismissed');
      fitCanvas();
    });
  }

  window.addEventListener('resize', fitCanvas);
  window.addEventListener('orientationchange', function () {
    setTimeout(fitCanvas, 120);
  });

  // 打印前展开全部页面（CSS 已处理，这里确保目录浮层关闭）
  window.addEventListener('beforeprint', closeOutline);

  /* ---------------- 启动 ---------------- */
  fitCanvas();
  buildOutline();
  buildNotesPanel();
  updateSlide(readHash(), true);
  autoFitSlides();

  // 中文字体加载完成后再兜底测一次
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(autoFitSlides);
  }
  window.addEventListener('load', autoFitSlides);
})();
