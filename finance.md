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
      <span class="ticker-price ticker-down">3,584.58</span>
      <span class="ticker-change down">▼ -0.50%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000001" aria-label="查看上证指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>上海证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-17 15:35:57（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 深证成指</span>
      <span class="ticker-code">399001.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">10,638.52</span>
      <span class="ticker-change down">▼ -0.49%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399001" aria-label="查看深证成指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>深圳证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-17 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399006" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 创业板指</span>
      <span class="ticker-code">399006.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">2,292.20</span>
      <span class="ticker-change down">▼ -1.20%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399006" aria-label="查看创业板指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>创业板市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-17 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sh000688" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 科创50</span>
      <span class="ticker-code">000688.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">1,221.19</span>
      <span class="ticker-change up">▲ +0.62%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000688" aria-label="查看科创50 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>科创板核心指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-17 15:35:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSTECH" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生科技</span>
      <span class="ticker-code">HSTECH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,766.06</span>
      <span class="ticker-change down">▼ -0.94%</span>
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
      <span class="ticker-price ticker-down">27,197.15</span>
      <span class="ticker-change down">▼ -2.67%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-17 09:23:20（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">6.6655</span>
      <span class="ticker-change up">▲ +0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 17:52:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">$3,866.89 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change up">▲ +10.65 (+0.28%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 17:52:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">¥832.00 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change up">▲ +3.00 (+0.36%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 15:29:59（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生指数</span>
      <span class="ticker-code">HSI</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">23,545.14</span>
      <span class="ticker-change down">▼ -0.88%</span>
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
      <span class="ticker-price ticker-up">$92.75 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change up">▲ +0.31 (+0.33%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 17:52:54（非实时）</div>
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
        <a class="news-item" href="https://www.ithome.com/1/028/430.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，当地时间 16 日，雷诺集团宣布，计划到 2028 年在法国工厂新增 2000 名员工，以满足不断增长的纯电车型需求，同时通过自愿离职计划削减最多 1000 个白领岗位。法国《回声报》率先披露了这一计划。汽油价格大幅上涨带动欧洲纯电汽车销量激增，雷诺旗下纯电车型需求随之上升，汽车行业的生产布局也需要相应调整。此次裁员将涉及雷诺在法国的所有工业业务，包括质量控制和供应链部门，但生产线工人不受影响。雷诺生产业务直接或间接雇用的员工共 17500 人。今年 6 月，雷诺曾宣布重组工程研发部门，以降低成本、缩短研发周期，并缩小与中国新兴竞争对手之间的差距。此次人员调整是继研发部门重组之后的又一项措施。雷诺集团工业总监蒂埃里 · 沙尔韦指出，商用厢式车和雷诺 5 等纯" data-title="扩招裁员两手抓：雷诺将新增 2000 个生产岗，并裁减至多 1000 个白领岗" data-date="11-17 17:28" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:28</span>
          <span class="news-item-title">扩招裁员两手抓：雷诺将新增 2000 个生产岗，并裁减至多 1000 个白领岗</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/420.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，微博今日发布 2026 财年（2026 年 1 月～2026 年 12 月）第三财季（2026 年 7 月～2026 年 9 月）报告：营业总收入：4.1 亿美元（IT之家注：现汇率约合 27.38 亿元人民币），同比下降 7%归母净利润：2,451.5 万美元（现汇率约合 1.64 亿元人民币），同比下降 88.91%经营现金流：1,020 万美元（现汇率约合 6,812.8 万元人民币）基本每股收益：0.1 美元（现汇率约合 0.67 元人民币）稀释每股收益：0.1 美元（现汇率约合 0.67 元人民币） AI 解读微博 2026 年三财季及前三季度业绩整体低于市场机构预期，营收、归母净利润均不及机构此前给出的一致预测。公司业务与本次财报核心亮点微博是中" data-title="微博 2026 财年第三季度归母净利润 2451.5 万美元，同比下降 88.91%" data-date="11-17 17:28" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:28</span>
          <span class="news-item-title">微博 2026 财年第三季度归母净利润 2451.5 万美元，同比下降 88.91%</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/417.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，腾讯音乐今日发布 2026 财年（2026 年 1 月～2026 年 12 月）前三季度（2026 年 1 月～2026 年 9 月）及第三财季（2026 年 7 月～2026 年 9 月）报告：2026 财年前三季度营业总收入：257.69 亿元，同比增长 6.22%毛利润：113.18 亿元，同比增长 6.04%毛利率：43.92%，同比下降 0.07 个百分点归母净利润：67.16 亿元，同比下降 24.14%经营现金流：103.96 亿元，同比增长 32.6%基本每股收益：2.16 元，同比下降 25.26%稀释每股收益：2.14 元，同比下降 24.91%资产负债率：34.14%2026 财年第三财季营业总收入：89.41 亿元，同比增长 5.6%" data-title="腾讯音乐 2026 财年前三季度归母净利润 67.16 亿元，同比下降 24.14%" data-date="11-17 17:02" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:02</span>
          <span class="news-item-title">腾讯音乐 2026 财年前三季度归母净利润 67.16 亿元，同比下降 24.14%</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ck5y1g89jnnxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="台湾试图以企业家身份与科技优势扩大能见度，中国则以原则框架维持主导权。APEC作为平台，或许能让双方同时在场，但仍难以消弭两岸在全球外交参与的既有分歧。" data-title="APEC深圳峰会：赖清德派施振荣出席 台湾参会空间再成焦点" data-date="11-17 16:44" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 16:44</span>
          <span class="news-item-title">APEC深圳峰会：赖清德派施振荣出席 台湾参会空间再成焦点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733525.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网11月17日电 据“今日俄罗斯”(RT)报道，11月17日，俄罗斯总统特别代表、俄罗斯直接投资基金总裁基里尔·德米特里耶夫在社交平台X上发布了自己此次中国之行的首张照片，宣布抵达深圳，参加亚太经合组织(APEC)相关活动。" data-title="俄总统特别代表抵深后发布首张照片：APEC会议致力于合作与繁荣" data-date="11-17 16:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:36</span>
          <span class="news-item-title">俄总统特别代表抵深后发布首张照片：APEC会议致力于合作与繁荣</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733479.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社深圳11月17日电 (记者 尹倩芸)来自亚太经合组织(APEC)21个经济体和英国、法国、德国、瑞士等13个域外经济体的2000余位政商界代表17日在深圳参加2026年APEC工商领导人峰会。" data-title="（深圳APEC）2000余位政商界代表参加APEC工商领导人峰会" data-date="11-17 16:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:13</span>
          <span class="news-item-title">（深圳APEC）2000余位政商界代表参加APEC工商领导人峰会</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c68x0j2r8lkyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="英国首相在伦敦金融城市长晚宴上向与会人士表示，“我们得到的脱欧结果并没有奏效”。" data-title="欧盟峰会前夕 贝安德称英国脱欧“得不偿失”" data-date="11-17 15:52" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 15:52</span>
          <span class="news-item-title">欧盟峰会前夕 贝安德称英国脱欧“得不偿失”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733390.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网11月17日电 据美联社报道，当地时间16日，加拿大总理卡尼表示，如果与美国总统特朗普的贸易谈判未能保住北美一体化汽车产业，加拿大可能转向中国汽车制造商寻求合作。" data-title="加总理卡尼：加拿大或寻求与中国等车企合作" data-date="11-17 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 14:14</span>
          <span class="news-item-title">加总理卡尼：加拿大或寻求与中国等车企合作</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/business/shoe-prices-inflation-tariffs.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="10月份，鞋类价格创下历史新高，原因是各品牌正面临材料成本上涨和关税上调的双重压力。" data-title="Shoe Prices Hit a Record High Amid Inflation and Increased Tariffs" data-date="11-17 13:00" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 13:00</span>
          <span class="news-item-title">Shoe Prices Hit a Record High Amid Inflation and Increased Tariffs</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/us/politics/bessent-lutnick-china.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="这位曾试图缓和关税战的财政部长，正对美国敏感技术的出口采取更强硬的措施。" data-title="Bessent Takes Hawkish Turn in White House Debate on China" data-date="11-17 06:46" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 06:46</span>
          <span class="news-item-title">Bessent Takes Hawkish Turn in White House Debate on China</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1034694/nuclear-energy-constellation-earnings-data-centers-democrats" target="_blank" rel="noopener" data-cat="caijing" data-summary="美国最大的核电站运营商康斯泰利शन能源公司并不认同华尔街的担忧，即民主党将放缓数据中心的发展。在上周的公司第三季度财报电话会议上，首席执行官Joe Dominguez" data-title="Big Nuclear isn’t worried about the Democrats stopping data centers" data-date="11-17 04:29" data-source="The Verge">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:29</span>
          <span class="news-item-title">Big Nuclear isn’t worried about the Democrats stopping data centers</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/" target="_blank" rel="noopener" data-cat="caijing" data-summary="美国联邦调查局表示，这款开源黑客工具曾被用于针对美国一家IT巨头和韩国金融业的网络攻击。" data-title="FBI says Artex AI open source hacking tool used to breach networks in ‘under three hours’" data-date="11-17 01:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 01:36</span>
          <span class="news-item-title">FBI says Artex AI open source hacking tool used to breach networks in ‘under three hours’</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/009.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，综合第一财经、鞭牛士报道，多位消息人士透露，360 副总裁、市场部负责人卜思南因涉嫌职务侵占等案件已在上周一被警方带走调查。截至发稿，360 方面暂未回应。今年 8 月，360 集团宣布，为推进“安全 +AI”战略，对集团市场与传播中心进行组织调整，设立公关部和市场部，任命卜思南为市场部负责人，向周鸿祎汇报。消息人士还透露，除了卜思南涉案外，内部或许还有相关人员被带走调查。IT之家查询获悉，卜思南是 360 集团副总裁、360 集团市场部负责人、360 数字安全集团教育事业部总经理、ISC 品牌主理人。卜思南早期负责集团市场战略、品牌生态建设，后主管产教融合业务，对接数百所院校共建安全产业学院，牵头国家级产教融合共同体；同时主理 ISC.AI 相关生态，推出" data-title="消息人士称 360 市场负责人卜思南涉嫌职务侵占已被警方带走调查" data-date="11-17 01:16" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 01:16</span>
          <span class="news-item-title">消息人士称 360 市场负责人卜思南涉嫌职务侵占已被警方带走调查</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/004.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，华为官方 X 账号分享了副董事长、轮值董事长徐直军发表在美国《时代》杂志的文章《亲历华为创新之路：看见、亲历、引领》（《Inside Huawei&#39;s innovation journey:Seeing it,living it,leading it》）。徐直军在文中以第一人称视角回顾了华为三十多年来的创新历程。据徐直军回忆，余承东（现任华为常务董事、产品投资评审委员会主任、终端 BG 董事长）除了发现欧洲的站点获取成本高得惊人，并提出分布式基站这一方案外，还在与西班牙电信德国公司的一次讨论中提出，把 2G 和 3G 集成到一个基站里。后来，华为与沃达丰合作推出了 SingleRAN 解决方案，把 2G、3G、4G、5G 在物理上集成到同一个基站中。这同样成" data-title="徐直军：分布式基站和 SingleRAN 两个开创性方案，确立了华为在移动通信领域全球领先地位" data-date="11-17 00:23" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 00:23</span>
          <span class="news-item-title">徐直军：分布式基站和 SingleRAN 两个开创性方案，确立了华为在移动通信领域全球领先地位</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1028004/best-gifts-under-100-2026" target="_blank" rel="noopener" data-cat="caijing" data-summary="即使在像我们现在这样的通胀时代，100美元仍然可以买到很多东西……如果您知道去哪里找的话。事实上，这足以买到一件实用且做工精良的东西，但又不会贵到让您感到内疚。" data-title="The Verge’s guide to the best gifts under $100" data-date="11-17 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 00:00</span>
          <span class="news-item-title">The Verge’s guide to the best gifts under $100</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-17 17:49（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
