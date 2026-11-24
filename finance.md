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
      <span class="ticker-price ticker-up">3,548.37</span>
      <span class="ticker-change up">▲ +0.27%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000001" aria-label="查看上证指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>上海证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-24 15:35:57（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 深证成指</span>
      <span class="ticker-code">399001.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">10,423.60</span>
      <span class="ticker-change down">▼ -0.29%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399001" aria-label="查看深证成指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>深圳证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-24 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399006" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 创业板指</span>
      <span class="ticker-code">399006.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">2,278.99</span>
      <span class="ticker-change down">▼ -0.05%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399006" aria-label="查看创业板指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>创业板市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-24 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sh000688" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 科创50</span>
      <span class="ticker-code">000688.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">1,250.09</span>
      <span class="ticker-change up">▲ +1.81%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000688" aria-label="查看科创50 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>科创板核心指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-24 15:35:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSTECH" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生科技</span>
      <span class="ticker-code">HSTECH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,464.52</span>
      <span class="ticker-change down">▼ -1.24%</span>
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
      <span class="ticker-price ticker-up">26,746.10</span>
      <span class="ticker-change up">▲ +6.86%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-24 09:17:52（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">6.6624</span>
      <span class="ticker-change down">▼ -0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 19:47:53（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">$3,632.88 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change down">▼ -2.35 (-0.06%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 19:47:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">¥777.25 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change down">▼ -2.99 (-0.38%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 15:30:01（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生指数</span>
      <span class="ticker-code">HSI</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">22,205.65</span>
      <span class="ticker-change down">▼ -0.80%</span>
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
      <span class="ticker-price ticker-up">$87.06 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change up">▲ +0.38 (+0.43%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 19:48:07（非实时）</div>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737107.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网11月24日电 据江西省纪委监委消息：江西省金融控股集团有限公司党委委员、副总经理，江西瑞奇期货有限公司董事长吴晓涉嫌严重违纪违法，主动向组织交代问题，目前正接受江西省纪委监委纪律审查和监察调查。" data-title="江西省金融控股集团有限公司副总经理吴晓接受审查调查" data-date="11-24 19:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:40</span>
          <span class="news-item-title">江西省金融控股集团有限公司副总经理吴晓接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737148.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网沈阳11月24日电 (记者 李𬀪)为深化慈善文化“五进”活动，引导企业履行社会责任，推动慈善文化与企业文化深度融合，助力沈阳慈善事业高质量发展，11月24日，由沈阳市民政局主办的“慈善力量·共识共融”慈善文化进企业活动在沈阳国际软件园举行。" data-title="“慈善力量·共识共融”慈善文化进企业活动在沈阳举办" data-date="11-24 19:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:39</span>
          <span class="news-item-title">“慈善力量·共识共融”慈善文化进企业活动在沈阳举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737125.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网漠河11月24日电 题：黑龙江漠河：立足极寒边境禀赋 推动产业联农带农提质增效" data-title="黑龙江漠河：立足极寒边境禀赋 推动产业联农带农提质增效" data-date="11-24 19:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:37</span>
          <span class="news-item-title">黑龙江漠河：立足极寒边境禀赋 推动产业联农带农提质增效</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737128.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网哈尔滨11月24日电(记者 王妮娜)24日，记者获悉，黑龙江首届机器人冰雪运动超级联赛暨2027寒地机器人竞技展演大赛(机器人“冰超”)将于2027年1月9日至11日在哈尔滨市举办。组委会即日起面向国内高等院校、机器人科创企业广发邀约，欢迎各单位组队参赛，在极寒冰雪场景下检验机器人技术成果，共探“冰雪+机器人”融合创新路径。" data-title="黑龙江向全国发出邀约 带着机器人来冰城参加“冰超”赛" data-date="11-24 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:29</span>
          <span class="news-item-title">黑龙江向全国发出邀约 带着机器人来冰城参加“冰超”赛</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/810.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 24 日消息，国产开放世界生存建造游戏《异化之境》将于今天稍晚在 Steam 平台开启抢先体验，目前官方已放出游戏试玩 DEMO。该作由机械狂牛工作室独立开发并发行。IT之家附游戏商品页（https://store.steampowered.com/app/5257810/异化之境/?l=schinese&amp;cc=cn）。根据官方介绍，《异化之境》是一款支持单人与在线合作的开放世界生存与机械建造游戏。玩家将穿过神秘传送门，来到核战后的陌生世界，在肩载机器人伙伴陈小拉的协助下采集资源、建造基地、自由拼装机械载具，并驾驶自己的造物探索自然荒野与战争遗迹，追寻特殊能源背后的秘密。游戏核心玩法特色包括：肩载机器人陈小拉：旅途中的重要伙伴，可协助玩家组装机械、搭建房屋、与其他机器人沟" data-title="国产开放世界生存游戏《异化之境》开启抢先体验，提供试玩 DEMO" data-date="11-24 19:14" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:14</span>
          <span class="news-item-title">国产开放世界生存游戏《异化之境》开启抢先体验，提供试玩 DEMO</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512411.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="2026年11月27日，2027中国AIoT产业年会暨创新私董会将在深圳柏悦酒店举行" data-title="最新议程与嘉宾阵容公布！2027中国AIoT产业年会，11月27日深圳见" data-date="11-24 16:44" data-source="量子位">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-24 16:44</span>
          <span class="news-item-title">最新议程与嘉宾阵容公布！2027中国AIoT产业年会，11月27日深圳见</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512387.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="探讨未来产业布局与结构性新周期下的资产配置机遇。" data-title="叙事时代丨第20届中国投资年会·有限合伙人峰会在沪成功举办" data-date="11-24 16:34" data-source="量子位">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-24 16:34</span>
          <span class="news-item-title">叙事时代丨第20届中国投资年会·有限合伙人峰会在沪成功举办</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/23/megaspeed-the-company-at-the-center-of-the-jensen-huang-scandal-appears-headed-for-a-u-s-blacklist/" target="_blank" rel="noopener" data-cat="caijing" data-summary="除非美国公司获得联邦政府的特别许可，否则Megaspeed（此前由黄馨（Alice Huang）领导）将被禁止与美国公司开展业务。" data-title="Megaspeed, the company at the center of the Jensen Huang scandal, appears headed for a US blacklist" data-date="11-24 05:25" data-source="TechCrunch">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-24 05:25</span>
          <span class="news-item-title">Megaspeed, the company at the center of the Jensen Huang scandal, appears headed for a US blacklist</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/style/amy-nelson-riveter-amazon-fbi-investigation.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="艾米·纳尔逊（Amy Nelson）是“女老板”时代的女性代言人，她发现自己的家人被亚马逊盯上了，而自己也成为了反企业斗士的新角色。" data-title="Amy Nelson Was a Corporate Feminist Darling. Then a Corporation Upended Her Life." data-date="11-24 03:33" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 03:33</span>
          <span class="news-item-title">Amy Nelson Was a Corporate Feminist Darling. Then a Corporation Upended Her Life.</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/stock-up-on-storage-with-4tb-t-force-g50-ssd-at-just-usd0-10-per-gb-entry-level-pcie-4-0-drive-offers-decent-performance-and-lots-of-capacity" target="_blank" rel="noopener" data-cat="caijing" data-summary="Team Group的4TB T-Force G50 Evo有超值优惠，在黑色星期五前将价格降至每GB仅0.10美元。" data-title="Stock up on storage with 4TB T-Force G50 SSD at just $0.10 per GB" data-date="11-24 02:11" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 02:11</span>
          <span class="news-item-title">Stock up on storage with 4TB T-Force G50 SSD at just $0.10 per GB</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/" target="_blank" rel="noopener" data-cat="caijing" data-summary="由Salesforce前联席首席执行官Bret Taylor共同创立的企业客户体验公司Sierra周一表示，该公司已在F轮融资中筹集了17.5亿美元。" data-title="Sierra doubles valuation to $30B within six months as demand for AI in CX takes off" data-date="11-23 22:43" data-source="TechCrunch">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-23 22:43</span>
          <span class="news-item-title">Sierra doubles valuation to $30B within six months as demand for AI in CX takes off</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/217.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 23 日消息，今日英伟达美股开盘跳涨 32%，市值增加超 1 万亿美元（IT之家注：现汇率约合 6.68 万亿元人民币），总市值重新站上 4 万亿美元（现汇率约合 26.73 万亿元人民币）。英伟达当日宣布，即日起恢复黄仁勋总裁兼首席执行官及董事会成员职务。IT之家注意到，英伟达在新闻稿中称，在与黄仁勋进行一系列讨论和会议后，董事会一致投票决定恢复其职务，董事会随后对黄仁勋的坦诚及其领导英伟达的能力表示满意。“我很荣幸能重返英伟达，并在新一轮工业革命伊始领导这家全球最具影响力的科技公司之一，”黄仁勋表示，“我将以最大的谦逊和焕然一新的承诺肩负起这一重任。我要感谢英伟达董事会在此过程中给予的信任与审慎考量。我尤其感谢哈维 · 琼斯（Harvey Jones）作为董事长所展现" data-title="黄仁勋恢复 CEO 职务：英伟达美股开盘大涨 32%，市值增加超 1 万亿美元" data-date="11-23 22:39" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-23 22:39</span>
          <span class="news-item-title">黄仁勋恢复 CEO 职务：英伟达美股开盘大涨 32%，市值增加超 1 万亿美元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-23/10736705.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社北京11月23日电 (记者 张杨彬 刘子衿)国务院台湾事务办公室与中国进出口银行23日在北京签署《“十五五”时期促进两岸融合发展金融合作协议》。" data-title="国务院台办与中国进出口银行签署合作协议" data-date="11-23 22:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 22:22</span>
          <span class="news-item-title">国务院台办与中国进出口银行签署合作协议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-23/10736698.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社北京11月23日电 (记者 张杨彬 刘子衿)“这个额度是我们当初没有料想到的。”重庆新格有色金属有限公司董事长黄耀滨23日在一场签约仪式上谈起今年初的一笔5000万元(人民币，下同)融资。那是这位台商第一次与中国进出口银行“打交道”。" data-title="政策性金融解台企发展之“渴” 台商期待借力拓展海外市场" data-date="11-23 22:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 22:02</span>
          <span class="news-item-title">政策性金融解台企发展之“渴” 台商期待借力拓展海外市场</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-23/10736687.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网杭州11月23日电 (钱晨菲)杭州市新生代企业家联谊会官方微信公众号近日发文显示，宇树科技股份有限公司董事长、创始人兼CEO王兴兴，已担任杭州市新生代企业家联谊会会长。" data-title="王兴兴担任杭州市新生代企业家联谊会会长" data-date="11-23 21:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 21:56</span>
          <span class="news-item-title">王兴兴担任杭州市新生代企业家联谊会会长</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-24 19:43（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
