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
      <span class="news-category-count">11 条精选资讯</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/030/708.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 22 日消息，科技初创公司 Nomadic 本周展示了旗下的 NOMAD 无人机，同时宣布完成 600 万美元（IT之家注：现汇率约合 4,016 万元人民币）种子轮融资。这款四旋翼无人机有一项与其名字相呼应的独特能力：几乎可以一直飞行，无需返回基地。NOMAD 无人机能够停靠在高压输电线上，直接从线路获取电能并为自身充电，随后继续执行下一项任务。此前外界鲜有关于 NOMAD 无人机的消息。Nomadic 表示，公司已经在德国、挪威和美国的实际带电线路上，对这款四旋翼无人机进行了超过 2 万小时的测试。Nomadic 将其概括为：“NOMAD 无人机可以降落在带电的高压输电线上，直接利用线路充电，并沿着电网移动，前往需要进行测量的地点。”从沿电网开展测量这一用途可以看出，" data-title="Nomadic 无人机停高压电线上就能充电，每架可负责监测 25 公里电网线路" data-date="11-22 20:56" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 20:56</span>
          <span class="news-item-title">Nomadic 无人机停高压电线上就能充电，每架可负责监测 25 公里电网线路</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/707.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 22 日消息，据欧洲汽车新闻报道，雷诺集团首席执行官福兰（Francois Provost）直言，当年未能向时任首席执行官卡洛斯 · 戈恩（Carlos Ghosn）指出其在华销量目标不切实际，是自己职业生涯中最大的失误。福兰于 2025 年 7 月出任雷诺首席执行官，他曾在 2016 年和 2017 年负责该车企在华业务运营。戈恩则于 2005 年至 2019 年 1 月期间担任雷诺集团首席执行官。“我们进入中国市场太晚了。实际上，我们相当于挤上了末班车的最后一节车厢 —— 而且还没买票，”福兰表示。这一表态之所以备受关注，是因为雷诺已于 2020 年退出在华合资企业，如今正吸取当年撤退的教训，将中国业务重塑为工程研发与采购基地，而非终端销售市场。福兰表示，雷诺曾在华推" data-title="雷诺集团 CEO 福兰反思职业生涯最大失误：当年未能指出在华销量目标不切实际" data-date="11-22 20:47" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 20:47</span>
          <span class="news-item-title">雷诺集团 CEO 福兰反思职业生涯最大失误：当年未能指出在华销量目标不切实际</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736181.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网云南保山11月22日电 (时文枝)11月20日至22日，2026年云南省建设面向南亚东南亚辐射中心体育交流大赛暨边境幸福村体育嘉年华主题活动在保山市举行。活动以云南边境县市和南亚东南亚国家体育交流为载体，串联文体旅商农产业多元业态，以赛事赋能兴边富民。" data-title="云南连续四年举办边境幸福村体育嘉年华 以赛事赋能兴边富民" data-date="11-22 20:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 20:23</span>
          <span class="news-item-title">云南连续四年举办边境幸福村体育嘉年华 以赛事赋能兴边富民</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736174.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社北京11月22日电 (记者 陈杭)在2026脑机接口大会上，专家学者围绕技术、应用、产业化与治理展开探讨，勾勒出脑机接口从帮助截瘫患者站立行走到“脑联网”的未来图景。" data-title="院士专家北京共论脑机接口未来图景" data-date="11-22 20:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 20:16</span>
          <span class="news-item-title">院士专家北京共论脑机接口未来图景</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736151.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网11月22日电 综合外媒报道，当地时间20日，美国总统特朗普在白宫举行的新闻发布会上表示，日前在中国深圳举行的亚太经合组织领导人非正式会议是一场非常成功的经济会议，美国、中国和俄罗斯三国领导人还举行了首次三方会晤，这是“多年来最具重大意义”的国际会晤之一。" data-title="特朗普点赞中俄美元首会晤气氛“热烈”，是“多年来最具重大意义”的国际会晤之一" data-date="11-22 19:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 19:12</span>
          <span class="news-item-title">特朗普点赞中俄美元首会晤气氛“热烈”，是“多年来最具重大意义”的国际会晤之一</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736119.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网南宁11月22日电(黄令妍)2026森林合作伙伴关系政策对话21日在广西南宁举行。这是该对话活动首次落地中国，与会代表围绕构建可持续林业产业、提升林业产业的资源基础等全球性议题深入研讨。" data-title="2026森林合作伙伴关系政策对话首次落地中国" data-date="11-22 18:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 18:12</span>
          <span class="news-item-title">2026森林合作伙伴关系政策对话首次落地中国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736083.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社奥斯陆11月21日电 (记者 马秀秀)初冬的奥斯陆，寒意已至。位于卡尔约翰大街的NIO House里，人头攒动，好不热闹。在近日举行的中国新能源汽车品牌蔚来进入挪威市场五周年特别活动上，当地官员、用户以及合作伙伴等齐聚一堂，共话这一中国汽车品牌在挪威的发展实践。" data-title="从“走出去”到“扎下根”：中国新能源汽车企业的“欧洲经”" data-date="11-22 16:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 16:42</span>
          <span class="news-item-title">从“走出去”到“扎下根”：中国新能源汽车企业的“欧洲经”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/623.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 22 日消息，制造商 Hidisc 宣布推出一款 Sound Glasses 轻量化蓝牙音频眼镜，该产品搭载蓝牙 6.0 技术、配有开放式扬声器，售价为 3,980 日元（IT之家注：现汇率约合 167.5 元人民币）。与如今功能日益复杂的智能眼镜不同，这款产品没有摄像头、AI 助手等功能，而是专注于提供基础的无线音频体验。其镜腿内置 10mm 扬声器，采用开放式音频设计，支持蓝牙 6.0，但音频编码仅支持标准 SBC 格式。这款眼镜配备触控区，用户可以通过触摸镜腿实现音乐播放、切换曲目和接听电话等操作。产品还具备 IPX5 级防水能力，可以应对日常出汗或意外淋雨等情况。眼镜配备 160mAh 电池，并采用磁吸方式充电，连续播放音乐时间可达 5.5 小时。" data-title="Hidisc Sound Glasses 轻量化蓝牙音频眼镜发布：10mm 扬声器、5.5 小时续航，3980 日元" data-date="11-22 16:39" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:39</span>
          <span class="news-item-title">Hidisc Sound Glasses 轻量化蓝牙音频眼镜发布：10mm 扬声器、5.5 小时续航，3980 日元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/619.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 22 日消息，据韩媒 ETNews 今日报道，业界消息称，三星电子决定明年不推出智能手表 Galaxy Watch 系列新产品。此举打破了自 2018 年推出首款型号以来连续 9 年保持的年度发布惯例，今后的新产品发布周期将调整为两年一更（隔年发布）。此次决定是三星电子移动业务部门近期全力提升盈利能力基调的延续，三星电子在处理器和内存等核心零部件价格飙升的“芯片通胀”浪潮中，正推进全方位的成本削减与产品线优化。多位业界相关人士分析称：“在智能手表市场增长势头放缓的背景下，今年推出的 Galaxy Watch 9 也因成本上升余波导致发售价上涨，市场反响未及预期”，“既然硬件创新已进入成熟期，三星便判断每年推出新产品的方式投入产出比正在下降”。据市场调查机构 Counter" data-title="消息称三星 Galaxy Watch 智能手表改为隔年发布，明年没有新品" data-date="11-22 16:29" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:29</span>
          <span class="news-item-title">消息称三星 Galaxy Watch 智能手表改为隔年发布，明年没有新品</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736035.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="随着气温持续走低，您家里的暖气热起来了吗？作为我国南方首个核能供热示范工程所在地，浙江嘉兴海盐县本周正式开启供暖。而今年，当地“核能供暖版图”持续扩容，服务范围从居民小区、工业企业，进一步延伸至文旅酒店等，让“零碳暖流”覆盖更多场景。" data-title="“零碳暖流”、AI控温 核能供暖是一种什么样的体验" data-date="11-22 13:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 13:41</span>
          <span class="news-item-title">“零碳暖流”、AI控温 核能供暖是一种什么样的体验</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736018.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社广州11月22日电 (记者 王坚)小鹏汇天22日宣布，其研发的全尺寸全倾转电动飞行汽车A868近日进行倾转过渡试飞并取得成功。此举代表着小鹏汇天成为中国第一家完成全尺寸样机倾转过渡飞行的企业，也意味着中国在该技术领域正式跨入全球第一梯队。" data-title="中国首款全尺寸全倾转电动飞行汽车倾转过渡试飞成功" data-date="11-22 13:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 13:23</span>
          <span class="news-item-title">中国首款全尺寸全倾转电动飞行汽车倾转过渡试飞成功</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-22 23:32（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
