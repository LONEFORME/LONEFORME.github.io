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
      <span class="ticker-price ticker-down">25,028.98</span>
      <span class="ticker-change down">▼ -5.61%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-21 06:30:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">6.6737</span>
      <span class="ticker-change down">▼ -0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 05:59:59（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">$3,534.64 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change down">▼ -90.37 (-2.49%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 05:55:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">¥756.00 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change down">▼ -8.00 (-1.05%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 02:30:00（非实时）</div>
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
      <span class="ticker-price ticker-up">$92.63 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change up">▲ +0.65 (+0.70%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 06:59:55（非实时）</div>
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
        <a class="news-item" href="https://www.ithome.com/1/030/505.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，当地时间 20 日，据《华尔街日报》报道，亚马逊对纽约市的一项劳工法案《配送保护法》（又称第 518 号提案）发起了反击。该法案将强制企业直接雇佣送货人员，而不是外包给第三方承包商。不仅如此，亚马逊通过弹出窗口警告客户：如果该法案最终成为法律，每笔订单的配送费用或将涨价 5 美元（IT之家注：现汇率约合 33.5 元人民币）。该法案将改变亚马逊配送司机的实际雇主身份。按照目前的配送模式，在身穿亚马逊马甲、驾驶亚马逊货车，甚至受到亚马逊 AI 摄像头的驾驶行为监控的司机背后，实际的雇主往往是亚马逊旗下配送体系中的小型合作企业，或称配送服务合作伙伴（Delivery Service Partners）。根据纽约市这项法案，亚马逊若想继续在纽约市五大行政区运营配送" data-title="亚马逊硬刚纽约拟议《配送保护法》：喊话消费者当心配送费涨价最高 5 美元" data-date="11-21 22:18" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 22:18</span>
          <span class="news-item-title">亚马逊硬刚纽约拟议《配送保护法》：喊话消费者当心配送费涨价最高 5 美元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/504.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，11 月 20 日，广汽夸克电驱非晶-碳纤维电驱第 10 万套正式量产下线。官方表示，这一里程碑标志着广汽成为全球唯一实现非晶合金车用电驱规模化量产的企业。据介绍，广汽动力总成自主研发团队围绕材料、工艺、结构和控制开展全链路攻关，首创非晶合金定子量产工艺，突破碳纤维高速转子关键技术，让非晶-碳纤维电驱从科研成果转化为可批量交付的车规级产品。夸克电驱 2.0 非晶-碳纤维电驱的核心突破，始于定子与转子两端：定子采用厚度 0.025mm 的非晶合金带材，厚度约为常规超薄硅钢片的五分之一；非晶合金磁导率可达普通硅钢片的 20 至 100 倍，单位铁损低至 5.7W/kg，较极薄硅钢降低约 50%。为实现车规级量产，广汽打通复合、冲压、叠装等成套工艺，非晶铁芯叠压层" data-title="全球唯一实现非晶合金车用电驱规模化量产，广汽夸克电驱非晶" data-date="11-21 21:53" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 21:53</span>
          <span class="news-item-title">全球唯一实现非晶合金车用电驱规模化量产，广汽夸克电驱非晶</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735919.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社南宁11月21日电 (张广权 黄令妍)2026年林木业大会21日在广西南宁举行。大会现场签约一批项目，总金额超400亿元人民币，涵盖浆纸原料林、纸品加工等领域。" data-title="2026年林木业大会在南宁举行 现场签约超400亿元" data-date="11-21 21:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 21:51</span>
          <span class="news-item-title">2026年林木业大会在南宁举行 现场签约超400亿元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/479.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，从零开发一套操作系统，即使对经验丰富的工程团队而言也是一项艰巨任务，南非开发者兼企业家德里克 · 佩恩却选择独自承担这项工作。当地时间 20 日，据外媒 TechSpot 报道，佩恩近日公布了面向现代 x86-64 PC 的全新操作系统 ——Impossible OS，其设计借鉴 Windows 11，完全基于开源代码开发。根据项目官方宣言，Impossible OS 的目标是原生运行基于 Win32 API 开发的软件，同时兼容 Linux 二进制程序。佩恩强调，其并非“又一个 Linux 发行版”，而是一套拥有自身底层架构的独立操作系统，包含 Ring 0 内核、UEFI 引导程序和桌面图形界面等核心组件。在兼容性方面，Impossible OS 通过内" data-title="南非开发者宣称独自开发操作系统 Impossible OS：兼容 Win32 和 Linux 二进制程序，两年后见" data-date="11-21 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 21:32</span>
          <span class="news-item-title">南非开发者宣称独自开发操作系统 Impossible OS：兼容 Win32 和 Linux 二进制程序，两年后见</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/478.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，当地时间 19 日，据 BBC 报道，英国开展了一项保密的网络安全行动，保护各大超市、仓库、餐厅、加油站及体育场馆内数万台冰箱和冷冻柜，防止黑客入侵。据IT之家了解，欧洲近期接连发生多轮网络攻击，数百家门店的数吨食品因此变质，损失达数百万英镑。此前，外界认为英国基本避开了此类黑客攻击，原因是英国制冷行业采用了不同类型的设备。实际上，英国制冷行业也存在一个潜在漏洞，业界一直在加紧修补。10 月下旬，安全研究人员发现一处重大漏洞。一旦被黑客发现，这一漏洞可能给英国造成更加严重的损害。此后，研究人员、IT 团队和英国国家网络安全中心（NCSC）日夜不停地向数十家企业发出警告。为降低黑客发现漏洞并利用漏洞造成破坏的风险，BBC 此前一直没有披露这项大规模、保密的行动" data-title="为抵御黑客攻击，英国秘密发起大规模“冰箱保卫战”" data-date="11-21 21:16" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 21:16</span>
          <span class="news-item-title">为抵御黑客攻击，英国秘密发起大规模“冰箱保卫战”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/476.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，据新华社报道，11 月 19 日，全国首条超百公里纯氢长输管道 —— 达尔罕茂明安联合旗至包头市区 195 公里氢气长输管道正式启运。该项目入选国家能源局首批能源领域氢能试点项目，标志着我国规模化、长距离纯氢管道输送实现关键突破，推动绿氢“制 — 储 — 输 — 用”全产业链协同发展。IT之家获悉，这条管道在内蒙古包头率先启运，得益于当地“制氢端有资源、用氢端有场景、地理空间高度集约”的独特条件。包头市委副书记、市长孟庆维介绍，包头风光资源富集，新能源装机占比超过火电，依托华电 20 万千瓦风光制氢项目，绿氢年产能达 7800 吨，生产成本较低；作为老工业基地，化工、冶金、燃气、交通等领域对绿氢需求集中；新能源制氢基地在北部达茂旗，主要用氢场景在南部包头市区" data-title="全国首条超百公里纯氢长输管道在内蒙古启运，核准年输氢量 10 万吨" data-date="11-21 21:03" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 21:03</span>
          <span class="news-item-title">全国首条超百公里纯氢长输管道在内蒙古启运，核准年输氢量 10 万吨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735890.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网杭州11月21日电(林波 孙琳茹)11月20日至22日，首届历史经典产业博览会在浙江杭州举行。博览会以“经典传承 新质兴业”为主题，汇聚丝绸、茶叶、瓷器、中药、酿造、工艺美术等产业，集中展示历史经典产业守正创新、向新发展的丰硕成果。" data-title="首届历史经典产业博览会在杭州举行：有哪些“经典”？" data-date="11-21 20:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 20:45</span>
          <span class="news-item-title">首届历史经典产业博览会在杭州举行：有哪些“经典”？</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1038448/harbinger-ev-startup-240m-series-d-fedex-army-trucks" target="_blank" rel="noopener" data-cat="caijing" data-summary="当传统汽车制造商在电动汽车方面踩下刹车时，一家初创公司却踩下了油门。本月早些时候，电动卡车制造商Harbinger在D轮融资中筹集了2.4亿美元，为一段辉煌的时期画上了圆满的句号，这段时期包括一笔价值3亿美元的订单。" data-title="Harbinger is building the unsexy EVs that keep the economy moving" data-date="11-21 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-21 20:00</span>
          <span class="news-item-title">Harbinger is building the unsexy EVs that keep the economy moving</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/414.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，中国通号今日宣布，中国通号所属低空公司自主研发的 4.9GHz 无蜂窝移动通信基站，正式取得工业和信息化部颁发的电信设备进网许可证，成为国内首款获证的 4.9GHz 无蜂窝移动通信基站。IT之家注：中国铁路通信信号股份有限公司（简称中国通号，CRSC）成立于 2010 年，是国务院国资委监管的中央企业，总部位于北京，主营业务为轨道交通控制系统相关业务。据介绍，移动通信通常采用蜂窝模式，各基站分别划定信号覆盖范围，如同蜂巢般拼接成整张网络。蜂窝网络彼此独立，覆盖范围交界处的信号衰减较快，用户跨小区移动时容易出现切换卡顿，多基站之间资源难以统一调度协同。工业作业、低空飞行、应急救援等场景对网络连续性和稳定性要求高，无蜂窝技术的出现极大满足了信息互联需求。官方表示" data-title="国内首款，中国通号所属低空公司 4.9GHz 无蜂窝基站获证商用" data-date="11-21 16:41" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:41</span>
          <span class="news-item-title">国内首款，中国通号所属低空公司 4.9GHz 无蜂窝基站获证商用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/412.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 21 日消息，据 Techspot 报道，美国罗切斯特大学和康奈尔大学的研究团队开发出一款低成本生物打印机，能够连续堆叠约 100 层含有活细胞的凝胶材料，整套设备成本仅约 450 美元（IT之家注：现汇率约合 3,011 元人民币）。作为参考，商用生物打印机价格通常超过 10 万美元（现汇率约合 66.9 万元人民币）。据介绍，生物打印机在原理上与普通 3D 打印机类似，只不过它挤出的不是熔融塑料，而是含有活细胞的凝胶。不过由于这类凝胶在凝固前容易因自身重量下垂，许多 DIY 生物打印机此前最多只能打印不到 20 层结构。而本次研究团队开发的新型生物打印机以常见的 Creality Ender 3 3D 打印机为基础，将原有打印头替换为注射泵，并使用 3D 打印的 PE" data-title="美国高校团队打造低成本生物打印机，可连续堆叠约 100 层活细胞凝胶材料" data-date="11-21 16:36" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:36</span>
          <span class="news-item-title">美国高校团队打造低成本生物打印机，可连续堆叠约 100 层活细胞凝胶材料</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735704.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网海口11月21日电 (张月和)世界客属第34届恳亲大会客家青年自贸港创新峰会20日在海南海口举行，海内外客家青年企业家、创业者代表等立足海南自贸港封关运作新起点，围绕产业创新、发展赛道、项目合作等话题展开交流。" data-title="客家青年相聚海南 共谋自贸港发展机遇" data-date="11-21 13:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 13:43</span>
          <span class="news-item-title">客家青年相聚海南 共谋自贸港发展机遇</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/us/politics/baaja-permitting-bill-trump.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="总统的影响无处不在，笼罩着旨在加快推进能源项目建设的两党立法，这些立法正在国会推进。" data-title="It’s a Bill on Energy Permits, but Trump’s Pet Projects Are Part of the Debate" data-date="11-21 11:41" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 11:41</span>
          <span class="news-item-title">It’s a Bill on Energy Permits, but Trump’s Pet Projects Are Part of the Debate</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/article/stock-market-correction.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="标普500指数较近期高点已下跌超过10%，越过了表明投资者对股市持悲观态度的门槛。" data-title="What Is a Stock Market Correction?" data-date="11-21 06:48" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 06:48</span>
          <span class="news-item-title">What Is a Stock Market Correction?</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/business/anthropic-ai-stocks-sp500.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="标普500指数收盘时较近期高点下跌超过10%，这标志着投资者情绪的恶化。" data-title="Stocks Skid Into a Correction, as A.I. Worries Intensify" data-date="11-21 06:47" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 06:47</span>
          <span class="news-item-title">Stocks Skid Into a Correction, as A.I. Worries Intensify</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735603.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="11月20日晚，国务院总理李强在北京钓鱼台国宾馆同澳大利亚总理阿尔巴尼斯共同出席第九届中澳工商界首席执行官圆桌会。新华社记者 黄敬文 摄 新华社北京11月20日电(记者伍岳)11月20日晚，国务院总理李强在北京钓鱼台国宾馆同澳大利亚总理阿尔巴尼斯共同出席第九届中澳工商界首席执行官圆桌会。近30位中澳商会和企业负责人出席。" data-title="李强同澳大利亚总理阿尔巴尼斯共同出席第九届中澳工商界首席执行官圆桌会" data-date="11-20 23:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 23:53</span>
          <span class="news-item-title">李强同澳大利亚总理阿尔巴尼斯共同出席第九届中澳工商界首席执行官圆桌会</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-21 23:30（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
