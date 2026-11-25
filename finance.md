---
layout: default
title: 股票财经
---

<h1>📈 股票与宏观财经看板</h1>
<p class="page-subtitle">全球市场快照 · A 股与港股 K 线 · 宏观财经资讯</p>

{% include market-chart.html %}

<!-- ================= 1. 全球核心指数行情看板 ================= -->
<div class="section-header" style="margin-top: 24px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>🌍 全球核心股指 & 宏观资产快照</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">覆盖 15 项市场指标 · 行情按源时间展示，可能存在延迟</span>
</div>

<!-- QUOTES:BEGIN -->
<div class="finance-ticker-grid">
  <div class="ticker-card" data-tcode="sh000001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 上证指数</span>
      <span class="ticker-code">000001.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,476.47</span>
      <span class="ticker-change down">▼ -2.03%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000001" aria-label="查看上证指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>上海证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:35:57（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 深证成指</span>
      <span class="ticker-code">399001.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">10,086.35</span>
      <span class="ticker-change down">▼ -3.24%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399001" aria-label="查看深证成指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>深圳证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399006" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 创业板指</span>
      <span class="ticker-code">399006.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">2,183.58</span>
      <span class="ticker-change down">▼ -4.19%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399006" aria-label="查看创业板指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>创业板市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sh000688" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 科创50</span>
      <span class="ticker-code">000688.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">1,186.14</span>
      <span class="ticker-change down">▼ -5.12%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000688" aria-label="查看科创50 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>科创板核心指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:35:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSTECH" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生科技</span>
      <span class="ticker-code">HSTECH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,378.26</span>
      <span class="ticker-change down">▼ -2.56%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="hkHSTECH" aria-label="查看恒生科技 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>香港科技股指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="usNDX" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇺🇸 纳斯达克100</span>
      <span class="ticker-code">NDX</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">26,046.90</span>
      <span class="ticker-change down">▼ -0.64%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-26 05:54:01（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">6.6674</span>
      <span class="ticker-change up">▲ +0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 05:54:01（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">$3,581.52 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change up">▲ +25.69 (+0.72%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 05:54:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">¥758.06 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change up">▲ +1.16 (+0.15%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 02:29:55（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生指数</span>
      <span class="ticker-code">HSI</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">21,966.01</span>
      <span class="ticker-change down">▼ -1.14%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="hkHSI" aria-label="查看恒生指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>港股基准大盘</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="usDJI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇺🇸 道琼斯工业指数</span>
      <span class="ticker-code">DJIA</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">46,247.29</span>
      <span class="ticker-change up">▲ +0.65%</span>
    </div>
    <div class="ticker-footer">
      <span>美股蓝筹风向标</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="ukUKX" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇬🇧 富时100</span>
      <span class="ticker-code">FTSE</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">9,284.83</span>
      <span class="ticker-change up">▲ +0.77%</span>
    </div>
    <div class="ticker-footer">
      <span>欧洲市场开盘参照</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🇯🇵 日经225</span>
      <span class="ticker-code">N225</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">44,946.64</span>
      <span class="ticker-change down">▼ -0.90%</span>
    </div>
    <div class="ticker-footer">
      <span>亚太早盘情绪指标</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="usINX" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇺🇸 标普500</span>
      <span class="ticker-code">SPX</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">6,643.70</span>
      <span class="ticker-change up">▲ +0.59%</span>
    </div>
    <div class="ticker-footer">
      <span>美股大盘核心基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="hf_OIL" data-fmt="usd" data-unit="/桶">
    <div class="ticker-header">
      <span class="ticker-name">🛢️ 布伦特原油</span>
      <span class="ticker-code">OIL/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">$90.78 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change up">▲ +2.00 (+2.25%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 05:54:11（非实时）</div>
  </div>
</div>



<style>
.ticker-card[data-live="1"] .ticker-quote-time { color: #00b86b; }
</style>
<script>
(function () {
  var cards = Array.prototype.slice.call(document.querySelectorAll('.ticker-card[data-tcode]'));
  if (!cards.length) return;
  var REFRESH_MS = 60000;
  var API = 'https://qt.gtimg.cn/q=';

  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  function comma(v, d) {
    var s = v.toFixed(d), p = s.split('.');
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return p.join('.');
  }
  function unitSpan(unit) {
    return unit ? ' <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">' + unit + '</span>' : '';
  }

  // 指数格式：1~名称~代码~现价~昨收~今开~...~YYYYMMDDHHMMSS~
  function parseIdx(raw) {
    var f = raw.split('~');
    if (f.length < 6) return null;
    var price = parseFloat(f[3]), prev = parseFloat(f[4]);
    if (!isFinite(price)) return null;
    // Field 30 is the timestamp. Other numeric fields can resemble a date.
    var t = f[30] || '';
    if (!/^20\d{12}$/.test(t) && !/^20\d{2}[-/]\d{2}[-/]\d{2} \d{2}:\d{2}:\d{2}$/.test(t)) t = '';
    if (price <= 0 || !isFinite(prev) || prev <= 0) return null;
    return { price: price, pct: (price - prev) / prev * 100, chg: price - prev, time: t };
  }

  // 外盘现货/期货格式：现价,涨跌幅%,买,卖,最高,最低,HH:MM:SS,昨收,今开,...
  function parseHf(raw) {
    var f = raw.split(',');
    if (f.length < 8) return null;
    var price = parseFloat(f[0]), pct = parseFloat(f[1]), prev = parseFloat(f[7]);
    if (!isFinite(price) || price <= 0) return null;
    return { price: price, pct: isFinite(pct) ? pct : 0, chg: isFinite(prev) ? price - prev : 0, time: f[6] || '' };
  }

  function paint(card, q) {
    var up = q.pct >= 0;
    var fmt = card.getAttribute('data-fmt') || 'idx';
    var unit = card.getAttribute('data-unit') || '';
    var priceHTML, chgText;

    if (fmt === 'fx') {
      priceHTML = q.price.toFixed(4);
      chgText = (q.chg >= 0 ? '+' : '') + Math.round(q.chg * 10000) + ' bp';
    } else if (fmt === 'usd' || fmt === 'cny') {
      priceHTML = (fmt === 'usd' ? '$' : '¥') + comma(q.price, 2) + unitSpan(unit);
      chgText = (q.chg >= 0 ? '+' : '') + q.chg.toFixed(2) + ' (' + (up ? '+' : '') + q.pct.toFixed(2) + '%)';
    } else {
      priceHTML = comma(q.price, 2);
      chgText = (up ? '+' : '') + q.pct.toFixed(2) + '%';
    }

    var pEl = card.querySelector('.ticker-price');
    var cEl = card.querySelector('.ticker-change');
    var tEl = card.querySelector('.ticker-quote-time');
    if (pEl) { pEl.innerHTML = priceHTML; pEl.className = 'ticker-price ' + (up ? 'ticker-up' : 'ticker-down'); }
    if (cEl) { cEl.innerHTML = (up ? '\u25b2 ' : '\u25bc ') + chgText; cEl.className = 'ticker-change ' + (up ? 'up' : 'down'); }
    if (tEl) {
      var hhmmss = '';
      if (/^20\d{12}$/.test(q.time)) {
        hhmmss = q.time.slice(0, 4) + '-' + q.time.slice(4, 6) + '-' + q.time.slice(6, 8) + ' '
               + q.time.slice(8, 10) + ':' + q.time.slice(10, 12) + ':' + q.time.slice(12, 14);
      } else if (q.time) {
        hhmmss = q.time;
      }
      if (hhmmss) {
        // 数据源时间按北京时间换算，超过 3 分钟就说明已收盘或延迟
        var stale = true;
        if (/^20\d{12}$/.test(q.time)) {
          var t = Date.UTC(+q.time.slice(0, 4), +q.time.slice(4, 6) - 1, +q.time.slice(6, 8),
                           +q.time.slice(8, 10) - 8, +q.time.slice(10, 12), +q.time.slice(12, 14)) / 1000;
          stale = (Date.now() / 1000 - t) > 180;
        } else if (/^\d{2}:\d{2}:\d{2}$/.test(q.time)) {
          // 外盘只给 HH:MM:SS，按北京时间拼今天再比较
          var n = new Date(Date.now() + (new Date().getTimezoneOffset() + 480) * 60000);
          var hh = +q.time.slice(0, 2), mi = +q.time.slice(3, 5), se = +q.time.slice(6, 8);
          var t2 = Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate(), hh - 8, mi, se) / 1000;
          stale = Math.abs(Date.now() / 1000 - t2) > 600;
        }
        tEl.textContent = '\ud83d\udd52 行情时间 ' + hhmmss
          + (/^20\d{12}$/.test(q.time) ? (stale ? '（延迟/已收盘）' : '') : '（源时区）');
      } else {
        tEl.textContent = '\ud83d\udd52 已获取行情，源时间未知';
      }
    }
    card.setAttribute('data-live', q.time && !stale ? '1' : '0');
  }

  function apply() {
    cards.forEach(function (c) {
      var code = c.getAttribute('data-tcode');
      var raw = window['v_' + code];
      if (!raw) return;
      var q = code.indexOf('hf_') === 0 ? parseHf(raw) : parseIdx(raw);
      if (q) paint(c, q);
    });
  }

  function refresh() {
    if (document.visibilityState === 'hidden') return;
    var el = document.createElement('script');
    el.charset = 'gbk';
    el.src = API + cards.map(function (c) { return c.getAttribute('data-tcode'); }).join(',')
           + '&_=' + Date.now();
    el.onload = function () { apply(); el.remove(); };
    el.onerror = function () { el.remove(); };
    document.head.appendChild(el);
  }

  refresh();
  setInterval(refresh, REFRESH_MS);
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible') refresh();
  });
})();
</script>

<!-- QUOTES:END -->

<!-- ================= 2. 热门核心赛道与主力资金流向 ================= -->
<div class="section-header" style="margin-top: 32px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>产业主题观察</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">关注领域</span>
</div>

<div class="finance-sector-grid">
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">🤖 人工智能 & 先进算力链</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">CPO 光模块</span>
      <span class="sector-tag-chip">GPU 服务器</span>
      <span class="sector-tag-chip">先进制程封装</span>
      <span class="sector-tag-chip">PCB 算力板</span>
    </div>
  </div>
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">⚡ 新能源出海 & 特高压电网</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">特高压直流</span>
      <span class="sector-tag-chip">固态锂电</span>
      <span class="sector-tag-chip">工商业储能</span>
      <span class="sector-tag-chip">核电核岛</span>
    </div>
  </div>
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">🚗 具身智能 & 智能网联车</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">端到端智驾</span>
      <span class="sector-tag-chip">激光雷达</span>
      <span class="sector-tag-chip">行星滚柱丝杠</span>
      <span class="sector-tag-chip">六维力传感器</span>
    </div>
  </div>
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">🛡️ 高股息红利与底仓资产</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">国有大行</span>
      <span class="sector-tag-chip">水电公用</span>
      <span class="sector-tag-chip">高股息煤炭</span>
      <span class="sector-tag-chip">中字头基建</span>
    </div>
  </div>
</div>


<!-- ================= 3. 每日财经资讯 ================= -->
<div class="section-header" style="margin-top: 36px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>📰 每日宏观财经 & 资本市场资讯聚合</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">宏观经济与资本市场</span>
</div>

<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">💰</span>
      <span class="news-category-title">宏观经济 · 汇率 · 证券 · 产业深度</span>
      <span class="news-category-count">15 条精选资讯</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/business/economy/inflation-pce-interest-rates.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="外界普遍预计美联储将于下月加息。" data-title="Another Hot Inflation Reading Keeps Fed on Track to Raise Rates Again" data-date="11-26 03:13" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 03:13</span>
          <span class="news-item-title">Another Hot Inflation Reading Keeps Fed on Track to Raise Rates Again</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/us/economic-growth-recession-pessimism.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="最新的增长和招聘指标显示经济状况良好。但处境艰难的美国人却感受不到这一点。" data-title="The U.S. Isn’t in a Recession. Try Telling Many Americans That." data-date="11-26 01:51" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 01:51</span>
          <span class="news-item-title">The U.S. Isn’t in a Recession. Try Telling Many Americans That.</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1028004/best-gifts-under-100-2026" target="_blank" rel="noopener" data-cat="caijing" data-summary="即使在像我们现在这样的通胀时代，100美元仍然可以买到很多东西……如果您知道去哪里找的话。事实上，这足以买到一件实用且做工精良的东西，但又不会贵到让您感到内疚。" data-title="The Verge’s guide to the best gifts under $100" data-date="11-26 01:00" data-source="The Verge">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 01:00</span>
          <span class="news-item-title">The Verge’s guide to the best gifts under $100</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/business/corporate-america-democrats.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="经过两年的放松监管，由民主党人领导的国会委员会将再次将目光聚焦于美国的企业界。" data-title="Corporate Oversight Revs Up as Washington Turns Blue Again" data-date="11-26 00:43" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 00:43</span>
          <span class="news-item-title">Corporate Oversight Revs Up as Washington Turns Blue Again</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/533.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，奕境汽车品牌总经理曾清林刚刚发文，分享了 70% 和 90% 两组数据：70% 来自工信部。2026 年以来，搭载辅助驾驶功能的乘用车新车，市场渗透率已经达到 70%。这再次印证，新能源上半场是电动化，现在来到了下半场的智能化。随着充电网络的普及和续航的提升，充电和续航对很多朋友来说已经不再是主要焦虑，真正的考题在智驾。90% 这个数据来自华为智能辅助驾驶后台：买了华为智驾车型的车主，90% 以上每天都在用。这个数据在我身上也可以得到验证。我目前开奕境 X9，每天 90% 的路程都是智驾开的。曾清林表示，有的智能辅助驾驶，让用户雨天不敢用、晚上没法用，极端工况更是害怕用，这样的智驾只会给用户添麻烦。问题往往出在感知硬件上。摄像头在夜晚、雨天、小目标面前存在短" data-title="奕境曾清林：新能源汽车来到智能化下半场，四激光正是面向 L3、一步到位的智驾硬件方案" data-date="11-25 23:59" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 23:59</span>
          <span class="news-item-title">奕境曾清林：新能源汽车来到智能化下半场，四激光正是面向 L3、一步到位的智驾硬件方案</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/business/trump-tariffs-trade.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="最新一轮的升级之际，政府正面临持续的法律障碍，以及即将上任的民主党主导的国会的新一轮审查。" data-title="Trump Administration Unveils New Tariffs for China, EU and More, Citing Unfair Practices" data-date="11-25 23:58" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 23:58</span>
          <span class="news-item-title">Trump Administration Unveils New Tariffs for China, EU and More, Citing Unfair Practices</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/531.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，工信部发布第 414 批《道路机动车辆生产企业及产品公告》新产品公示，北汽 T700 完成申报。本次申报的车型由北京汽车集团越野车有限公司生产，隶属于北京牌，定位为插电式增程混合动力运动型乘用车，车尾分别标注“T700”与“北汽集团”字样。根据外观及动力差异，公示中包含两种版本，整体造型延续方正硬派的方盒子设计语言，配备贯穿式尾灯与银色下护板装饰。IT之家注意到，两种版本的三围尺寸均为长 4973mm、宽 2019mm，轴距同为 3050mm ，额定载客 5 人。基础版本高度为 1930mm，整备质量 2410kg，最高车速 180km/h；高配版本高度略降为 1910mm，整备质量提升至 2700kg，最高车速达到 200km/h，同时可选装牵引专用装置（" data-title="北京汽车 T700 新车申报：1.5T 增程动力、单 / 双电机两种版本" data-date="11-25 23:53" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 23:53</span>
          <span class="news-item-title">北京汽车 T700 新车申报：1.5T 增程动力、单 / 双电机两种版本</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/529.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，工信部发布第 414 批《道路机动车辆生产企业及产品公告》新产品公示，零跑 C19 增程版与纯电版完成申报。本次申报的零跑 C19 车身尺寸为长 5128mm、宽 1972mm、高 1770mm（选装配置时为 1765mm），轴距 3000mm，定位中大型 SUV。车尾右侧标注有“C19”字样，左侧为“零跑”中文标识，中部为“LEAPMOTOR”英文标识，采用贯穿式尾灯设计。▲ 零跑 C19 增程版IT之家注意到，零跑 C19 增程版搭载重庆小康动力型号为 L15T 的 1.5T 四缸增程器，排量 1496ml，发动机额定功率 97kW，最大净功率 95kW，系统最高车速 180km/h。增程版采用前后双电机四驱布局，前电机额定功率 65kW、峰值功率 10" data-title="零跑 C19 新车申报：增程 / 纯电双动力，5.1 米长 5/6/7 座中大型 SUV" data-date="11-25 23:35" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 23:35</span>
          <span class="news-item-title">零跑 C19 新车申报：增程 / 纯电双动力，5.1 米长 5/6/7 座中大型 SUV</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/528.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，工信部发布第 414 批《道路机动车辆生产企业及产品公告》新产品公示，岚图汽车全新中大型 MPV 岚图梦想家 8 完成申报，涵盖纯电动、插电式混合动力共三款车型。IT之家注意到，本次申报的岚图梦想家 8 车尾带有“梦想家 8”标识，整体采用简约方正的 MPV 车身造型，配备贯穿式尾灯组，后包围下方设有红色反光饰条，整体风格偏向家用与商务兼顾的定位。车身尺寸方面，新车长宽高分别为 5260/2008/1780-1805mm，轴距为 3150mm，采用 7 座布局，轮胎规格提供 255/55R19、255/50R20 两种选择。配置上，新车可选装双色车身、前格栅样式、前格栅饰条、不同轮辋，全系配备 ABS、汽车事件数据记录系统（EDR），并可选装直接供电式 ET" data-title="岚图梦想家 8 申报：纯电 / 插混可选，7 座中大型 MPV" data-date="11-25 23:30" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 23:30</span>
          <span class="news-item-title">岚图梦想家 8 申报：纯电 / 插混可选，7 座中大型 MPV</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/527.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，工信部发布第 414 批《道路机动车辆生产企业及产品公告》新产品公示，零跑全新大五座旗舰 SUV DX 完成申报。IT之家注意到，本次申报的零跑 DX 车尾带有 LEAPMOTOR 品牌英文标识与“DX”字样，整体为大五座中大型 SUV 造型，车尾配备贯穿式尾灯组，后包围带有银色防擦护板与红色反光条，整体风格偏稳重旗舰取向。车身尺寸方面，零跑 DX 的长宽高分别为 5151/1999/1775mm（1795mm），轴距为 3110mm，前悬 / 后悬为 950/1091mm，前轮距 1710mm、后轮距 1715mm，接近角 / 离去角均为 18 度，额定载客人数为 5 人，采用承载式车身结构。动力部分，本次申报共包含四款配置版本，其中两款增程版本均搭载极光" data-title="零跑 DX 大五座 SUV 申报：纯电 / 增程可选，轴距 3110mm" data-date="11-25 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 23:28</span>
          <span class="news-item-title">零跑 DX 大五座 SUV 申报：纯电 / 增程可选，轴距 3110mm</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/526.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，工信部发布第 414 批《道路机动车辆生产企业及产品公告》新产品公示，极狐阿尔法 T7 换电版完成申报。本次申报的车型为极狐 (ARCFOX) 阿尔法 T7 换电式纯电动多用途乘用车，由北汽蓝谷麦格纳汽车有限公司生产制造，车辆长宽高分别为 5020mm / 1996mm / 1685mm，轴距为 3040mm，额定载客人数为 5 人，最高车速可达 180km/h。IT之家注意到，动力方面，该车搭载湖南中车时代电驱科技有限公司生产的驱动电机，电机额定功率 73kW，峰值功率 227kW；储能装置为宁德时代供应的磷酸铁锂蓄电池，由宁德时代新能源科技股份有限公司提供单体、宁德时代（江苏）新能源科技有限公司提供总成。值得一提的是，该产品销售时可依据国家相关部门的规定" data-title="极狐阿尔法 T7 换电版申报，搭载 227kW 电机与宁德时代磷酸铁锂电池" data-date="11-25 23:27" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 23:27</span>
          <span class="news-item-title">极狐阿尔法 T7 换电版申报，搭载 227kW 电机与宁德时代磷酸铁锂电池</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737848.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社柏林11月25日电 (记者 马秀秀)德国联邦统计局25日公布的数据显示，经价格、季节和工作日调整后，2026年第三季度德国国内生产总值环比增长0.1%，较此前公布的初值下调0.1个百分点。" data-title="德国下调三季度经济增速至0.1%" data-date="11-25 23:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 23:27</span>
          <span class="news-item-title">德国下调三季度经济增速至0.1%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737822.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社伦敦11月25日电 (记者 欧阳开宇)英国能源监管机构天然气和电力市场办公室25日宣布，受中东地缘冲突持续扰动国际能源供应链、天然气价格走高影响，英国居民能源价格上限将自2027年1月起大幅上调26%，全国约2000万户家庭将面临冬季用能成本显著上涨。" data-title="英国能源限价2027年将大幅上调" data-date="11-25 21:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:55</span>
          <span class="news-item-title">英国能源限价2027年将大幅上调</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737832.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社厦门11月25日电 (吴冠标)厦门市发展和改革委员会主任孙建辉25日表示，厦门将深化两岸服务业融合发展，建强两岸区域性金融服务中心，打造台胞休闲旅游、就医康养、居住就业“第一目的地”。" data-title="厦门推进服务业扩能提质 深化两岸融合发展" data-date="11-25 21:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:53</span>
          <span class="news-item-title">厦门推进服务业扩能提质 深化两岸融合发展</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cm9d7g967l5lo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="新关税将打击美国许多最大的贸易伙伴，包括中国和欧盟。" data-title="美国准备公布对全球贸易伙伴加征新关税的计划" data-date="11-25 20:18" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-25 20:18</span>
          <span class="news-item-title">美国准备公布对全球贸易伙伴加征新关税的计划</span>
        </a>
  </div>
</div>


<div style="text-align: center; margin: 36px 0 20px;">
  <a href="{{ "/news" | relative_url }}" class="card-link" style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 24px; font-size: 14px;">
    <span>📰 返回综合热点新闻专区</span>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
  </a>
</div>

---

<p class="news-updated">🕐 页面生成于 2026-11-26 05:52（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
