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
      <span class="ticker-price ticker-down">3,533.79</span>
      <span class="ticker-change down">▼ -1.22%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000001" aria-label="查看上证指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>上海证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-20 15:43:57（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 深证成指</span>
      <span class="ticker-code">399001.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">10,256.39</span>
      <span class="ticker-change down">▼ -3.09%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399001" aria-label="查看深证成指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>深圳证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-20 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399006" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 创业板指</span>
      <span class="ticker-code">399006.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">2,212.13</span>
      <span class="ticker-change down">▼ -3.54%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399006" aria-label="查看创业板指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>创业板市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-20 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sh000688" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 科创50</span>
      <span class="ticker-code">000688.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">1,231.09</span>
      <span class="ticker-change down">▼ -3.12%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000688" aria-label="查看科创50 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>科创板核心指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-20 15:43:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSTECH" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生科技</span>
      <span class="ticker-code">HSTECH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,511.14</span>
      <span class="ticker-change down">▼ -3.78%</span>
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
      <span class="ticker-price ticker-down">26,517.05</span>
      <span class="ticker-change down">▼ -2.21%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-20 09:19:09（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">6.6810</span>
      <span class="ticker-change down">▼ -0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 17:21:18（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">$3,582.96 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change down">▼ -42.05 (-1.16%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 17:21:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">¥764.00 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change down">▼ -38.06 (-4.75%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 15:30:04（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生指数</span>
      <span class="ticker-code">HSI</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">22,410.80</span>
      <span class="ticker-change down">▼ -1.89%</span>
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
      <span class="ticker-price ticker-down">$90.90 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change down">▼ -1.08 (-1.17%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 17:21:30（非实时）</div>
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
        <a class="news-item" href="https://www.ithome.com/1/030/125.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 20 日现场消息，在今天的鸿蒙智行享界 V8 及星芒品牌发布会上，北汽集团党委书记、董事长张建勇宣布，华为与北汽战略共同体再次升级。张建勇表示，此次合作聚焦技术产品、专属团队、品质保障、服务体验四大体系全面升级，战略投入将持续加码，助力享界进入体系作战新阶段。IT之家注意到，鸿蒙智行官方刚刚公布了华为北汽战略共同体再升级的详情信息：技术产品升级：强化鸿蒙智行模式合作，享界持续投入专项资金，持续拓宽产品矩阵，推动技术及产品体验升级。专属团队升级：汇聚华为北汽双方优秀人才与专家力量，持续锻造享界事业部专属团队能力，夯实品牌升级组织底座。品质保障升级：享界专属品质保障体系，全链路升级迭代双质检体系，共筑行业领先的高端新能源汽车品质标杆。服务体验升级：在鸿蒙智行整体渠道战略下，持" data-title="华为北汽战略共同体升级详情公布：强化鸿蒙智行模式合作、享界持续投入专项资金" data-date="11-20 16:57" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 16:57</span>
          <span class="news-item-title">华为北汽战略共同体升级详情公布：强化鸿蒙智行模式合作、享界持续投入专项资金</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735331.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网伊斯坦布尔11月20日电(记者 王高飞 魏园)近日，中国新闻社“新闻会客厅”在《联合国气候变化框架公约》第三十一次缔约方大会(COP31)期间，于伊斯坦布尔举办“中土生态文明与绿色转型对话会”。中土政界、学界、商界代表共话两国生态文明交流与合作。" data-title="土耳其专家阿蒂利：中国将生态保护“义务”变为产业发展“机遇”｜新闻会客厅" data-date="11-20 16:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:56</span>
          <span class="news-item-title">土耳其专家阿蒂利：中国将生态保护“义务”变为产业发展“机遇”｜新闻会客厅</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735306.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="环球时报 丁雅栀 李炫旻" data-title="【环瞰·APEC中国年】APEC会议现场，企业代表热议“互联互通”" data-date="11-20 16:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:33</span>
          <span class="news-item-title">【环瞰·APEC中国年】APEC会议现场，企业代表热议“互联互通”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735042.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网奥斯陆11月20日电 (记者 马秀秀)挪威创新署贸易与投资部门负责人加尔德·马德森(Gard Madsen)19日在接受记者采访时表示，中国新能源汽车产业发展令人印象深刻。随着中国电动汽车制造商逐渐站稳脚跟，其相较于世界其他地区汽车制造商确实正在获得优势。挪威对电动汽车接受程度很高，是中国汽车品牌拓展欧洲市场的良好选择。" data-title="挪威创新署官员：中国电动汽车制造商正获得竞争优势" data-date="11-20 10:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 10:31</span>
          <span class="news-item-title">挪威创新署官员：中国电动汽车制造商正获得竞争优势</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735057.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网11月20日电 11月18日至19日，亚太经合组织(APEC)第三十三次领导人非正式会议在深圳举行。随着亚太各经济体领导人和工商界代表齐聚这座中国改革开放的前沿城市，深圳成为国际媒体关注的焦点。" data-title="外媒眼中的“现代化奇迹”，APEC深圳会议展现中国开放创新窗口" data-date="11-20 09:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 09:44</span>
          <span class="news-item-title">外媒眼中的“现代化奇迹”，APEC深圳会议展现中国开放创新窗口</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/744.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 20 日消息，Counterpoint Research 2026 年第三季度智能手机市场监测报告显示，欧洲智能手机市场出货量同比下滑 18%，创下超过 13 年以来的最低季度总量。报告指出，上游零部件成本大幅攀升推动终端设备售价上涨，各厂商同步缩减促销力度，叠加宏观经济环境疲软持续压制消费者需求，是本季度欧洲市场大幅下滑的核心原因。IT之家从报告获悉，Counterpoint 副总监 Jan Stryjak 表示，尽管本季度欧洲市场有多款重磅新品发布，但整体经营环境依然严峻。三星推出的“护照级尺寸”Galaxy Z Fold8 是西欧有史以来销量最快的折叠屏机型，但该机型的亮眼表现无法抵消 Galaxy A 系列等中低端产品线的疲软；苹果则发布了品牌首款折叠屏产品 iP" data-title="Counterpoint：今年 Q3 欧洲智能手机出货同比下滑 18%，创 13 年来多季度新低" data-date="11-20 01:43" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 01:43</span>
          <span class="news-item-title">Counterpoint：今年 Q3 欧洲智能手机出货同比下滑 18%，创 13 年来多季度新低</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734984.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社深圳11月19日电 亚太经合组织互联互通蓝图19日发布。蓝图强调，互联互通促进本地区商品、服务、资金和人员流动，有助于密切经济联系、推动长期经济增长；以《2040年亚太经合组织布特拉加亚愿景》为指引，朝着建设开放、活力、强韧、和平的亚太共同体迈进，实现亚太人民和子孙后代的共同繁荣。" data-title="（深圳APEC）亚太经合组织互联互通蓝图发布" data-date="11-19 23:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 23:57</span>
          <span class="news-item-title">（深圳APEC）亚太经合组织互联互通蓝图发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734981.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社北京11月19日电 综合消息：亚太经合组织(APEC)第三十三次领导人非正式会议18日至19日在中国深圳举行。多家外媒聚焦深圳科技创新与城市发展，关注会议释放的开放合作信号，认为维护贸易开放、深化区域合作、推动创新发展，仍是亚太经济体的共同关切。" data-title="（深圳APEC）外媒聚焦APEC：开放合作为亚太发展凝聚共识" data-date="11-19 23:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 23:45</span>
          <span class="news-item-title">（深圳APEC）外媒聚焦APEC：开放合作为亚太发展凝聚共识</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734961.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社深圳11月19日电 2026年亚太经合组织领导人深圳展望19日发布。展望重申，亚太经合组织是区域经济合作的首要平台，将遵循自主自愿、非约束性和协商一致的合作原则，致力于将亚太经合组织打造成一个更加现代、高效、务实的理念孵化器。" data-title="（深圳APEC）2026年亚太经合组织领导人深圳展望发布" data-date="11-19 22:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:37</span>
          <span class="news-item-title">（深圳APEC）2026年亚太经合组织领导人深圳展望发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734948.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社深圳11月19日电 (记者 刘文文)11月的深圳，入夜微凉，盐田港灯火如昼，一派繁忙景象。作为全球单体规模最大的集装箱码头之一，这里每周有53条直通亚太经合组织(APEC)成员经济体的航线。中国的新能源汽车、照相机由此出海，马来西亚榴莲、智利车厘子跨海而来。在亚太地区，类似的航程每时每刻都在发生。彼此相连，也意味着休戚与共。" data-title="（深圳APEC）以船为喻，中国向亚太发出“同舟之约”" data-date="11-19 22:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:25</span>
          <span class="news-item-title">（深圳APEC）以船为喻，中国向亚太发出“同舟之约”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-19/10734950.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网海口11月19日电 (贾浪博)琼州海峡智能航运示范工程启动仪式19日在海口举行，标志着琼州海峡智能航运建设迈入实质推进阶段。" data-title="琼州海峡智能航运示范工程在海口启动" data-date="11-19 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:01</span>
          <span class="news-item-title">琼州海峡智能航运示范工程在海口启动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734932.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社首尔11月19日电(金旭 林珺)韩国大法院(最高法院)19日就韩国前总统尹锡悦妻子金建希涉嫌操纵股价、收受贿赂等案件作出终审判决，判处其有期徒刑4年，并处罚金5000万韩元(约合人民币25万元)。这是韩国最高法院首次就金建希相关案件作出裁定。" data-title="韩国前第一夫人金建希首案终审被判有期徒刑4年" data-date="11-19 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 21:54</span>
          <span class="news-item-title">韩国前第一夫人金建希首案终审被判有期徒刑4年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-19/10734943.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中国日报网11月19日电 山河更迭，风雅长存。11月19日，“何以中国·诗词里的千年文脉”网络主题宣传活动于古都西安启幕。纵使时代千帆竞发、科技日新月异，古典诗词始终沉淀着华夏儿女的家国情怀与人生哲思，是镌刻民族风骨的精神根脉。千年长安承唐风诗韵，以全域深耕的文化建设，探寻古典文脉古今赓续的新生之路。" data-title="何以中国｜唐韵润古邑 诗脉续长安" data-date="11-19 21:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 21:47</span>
          <span class="news-item-title">何以中国｜唐韵润古邑 诗脉续长安</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c38x04eppnpdo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="会后发表的中俄美元首和平宣言显示，三国领导人承诺就“减少核风险、防止核扩散”展开对话，并就联合国改革、能源稳定和国际刑事法院管辖权等议题达成四点共识。" data-title="中美俄“三巨头”峰会结束：涉及乌克兰、伊朗议题，发表和平宣言承诺核对话" data-date="11-19 20:22" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-19 20:22</span>
          <span class="news-item-title">中美俄“三巨头”峰会结束：涉及乌克兰、伊朗议题，发表和平宣言承诺核对话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734799.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社首尔11月19日电(记者 金旭)韩国产业通商资源部19日表示，韩国2026年累计出口额初步统计已超过1万亿美元(约合人民币6.7万亿元)，成为继美国、德国和中国之后，全球第四个实现年度出口额突破1万亿美元的国家。" data-title="韩国2026年累计出口额突破1万亿美元大关" data-date="11-19 18:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 18:35</span>
          <span class="news-item-title">韩国2026年累计出口额突破1万亿美元大关</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-20 17:18（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
