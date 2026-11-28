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
      <span class="ticker-price ticker-up">3,606.49</span>
      <span class="ticker-change up">▲ +3.73%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000001" aria-label="查看上证指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>上海证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-27 15:35:57（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 深证成指</span>
      <span class="ticker-code">399001.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">10,814.02</span>
      <span class="ticker-change up">▲ +7.24%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399001" aria-label="查看深证成指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>深圳证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-27 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399006" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 创业板指</span>
      <span class="ticker-code">399006.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">2,443.96</span>
      <span class="ticker-change up">▲ +11.61%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399006" aria-label="查看创业板指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>创业板市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-27 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sh000688" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 科创50</span>
      <span class="ticker-code">000688.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">1,346.25</span>
      <span class="ticker-change up">▲ +15.07%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000688" aria-label="查看科创50 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>科创板核心指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-27 15:35:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSTECH" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生科技</span>
      <span class="ticker-code">HSTECH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">3,641.04</span>
      <span class="ticker-change up">▲ +6.54%</span>
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
      <span class="ticker-price ticker-up">26,726.39</span>
      <span class="ticker-change up">▲ +2.61%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-28 06:00:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">6.6551</span>
      <span class="ticker-change down">▼ -0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 05:59:47（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">$3,654.15 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change up">▲ +87.89 (+2.46%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 03:44:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">¥780.14 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change down">▼ -3.21 (-0.41%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 02:22:53（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生指数</span>
      <span class="ticker-code">HSI</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">22,688.68</span>
      <span class="ticker-change up">▲ +2.08%</span>
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
      <span class="ticker-price ticker-down">$90.70 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change down">▼ -0.97 (-1.06%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 03:59:58（非实时）</div>
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
        <a class="news-item" href="https://www.ithome.com/1/033/931.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 28 日消息，据界面新闻报道，在 2026 广州车展上，岚图汽车 CEO 蒋焘表示，今年国内车市下滑明显，业界对明年全年的预期相对保守。受补贴退坡影响，明年一季度或有部分需求提前释放；海外出口方面，受关税及法规趋严影响，增量空间亦将受限。总体而言，今明两年汽车行业面临的形势依然严峻，类似变化在手机、家电、光伏产业均有先例。在战略调整方面，蒋焘表示，岚图将从此前“以量为主”转向“量与利润双平衡”。未来将通过保持充足现金流、聚焦盈利车型，让企业健康可持续发展。据IT之家此前报道，岚图汽车 2026 年 10 月交付新车 13030 辆；1-10 月累计交付 128,511 辆，同比增长 13%。工信部本月公布《道路机动车辆生产企业及产品》（第 412 批）目录，岚图被列入该批" data-title="岚图汽车 CEO 蒋焘：明年车市依然严峻，战略从“以量为主”转向“量利双衡”" data-date="11-28 17:18" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-28 17:18</span>
          <span class="news-item-title">岚图汽车 CEO 蒋焘：明年车市依然严峻，战略从“以量为主”转向“量利双衡”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-28/10739234.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网曼谷11月28日电(梁峻祥 王茜 李映民)第四届中泰治国理政经验互学互鉴高端对话会27日在曼谷举行。中国外文局副局长于运全，泰国交通部副部长桑佩·汶亚玛尼，泰国国会下议院法院事务、独立机构、检察机关、国有企业、公共机构及基金委员会委员兼顾问阿卡拉德·翁皮塔洛，中国驻泰国大使馆参赞侯佩，亚太智库主任威伦·披差翁帕迪等嘉宾出席并致辞。来自中泰各界代表及青年代表100余人参加活动。" data-title="第四届中泰治国理政经验互学互鉴高端对话会在曼谷举行" data-date="11-28 17:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-28 17:12</span>
          <span class="news-item-title">第四届中泰治国理政经验互学互鉴高端对话会在曼谷举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/929.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 28 日消息，博主 @未来的学习笔记 今日发文透露，尊界 SUV 将归“X”序列。目前鸿蒙智行在轿车 S 系列和 MPV V 系列是有跨界的产品，但是在 SUV 上，就是专属的系列了。尚界 H 和 Z 系列，享界 G 系列、智界 R 系列、尊界应该就是 X 系列了。这样以后也更容易做好产品矩阵的区分。据IT之家此前报道，博主 @电车总裁 在 11 月 23 日发文透露，鸿蒙智行尊界 SUV 将亮相广州车展，不过该车预计是在“小黑屋”展示，仅部分受邀人士可提前参观。今年 9 月，华为常务董事、产品投资评审委员会主任、终端 BG 董事长余承东现身合肥鸿蒙智行门店。在接受门店工作人员提问时，余承东表示，这台新车“快了”，明年年初可能就要陆续上市，大概在 2、3 月份。他透露，尊" data-title="消息称鸿蒙智行尊界 SUV 将归“X”序列，更易做好产品矩阵区分" data-date="11-28 17:10" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-28 17:10</span>
          <span class="news-item-title">消息称鸿蒙智行尊界 SUV 将归“X”序列，更易做好产品矩阵区分</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-28/10739306.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="石榴云/新疆日报记者 曹华" data-title="“绿围脖”更厚 沙产业生金——环塔克拉玛干沙漠绿色阻沙防护带锁边合龙两周年观察" data-date="11-28 17:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-28 17:06</span>
          <span class="news-item-title">“绿围脖”更厚 沙产业生金——环塔克拉玛干沙漠绿色阻沙防护带锁边合龙两周年观察</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-28/10739285.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网南昌11月28日电 (记者 李韵涵)28日，江西省第二届高层次人才创新创业大赛颁奖仪式在南昌举行，本次大赛共评选出一等奖18名、二等奖36名、三等奖90名。" data-title="与产业深度融合 江西省第二届高层次人才创新创业大赛举行" data-date="11-28 16:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-28 16:57</span>
          <span class="news-item-title">与产业深度融合 江西省第二届高层次人才创新创业大赛举行</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ck0jxz70e4z5o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="台湾“九合一”选举与核能政策公投投票结束，全台1.8万余处投票所随即即场点票。BBC中文紧贴开票进展。" data-title="台湾“九合一”选举与核电公投：开票结果实时更新" data-date="11-28 16:31" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-28 16:31</span>
          <span class="news-item-title">台湾“九合一”选举与核电公投：开票结果实时更新</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-28/10739226.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网兰州11月28日电 (记者 丁思)“甘肃酒泉市的‘九音桥’、白银市的‘板凳会议’、静宁县的产业型代表家站、古浪县古浪镇的‘红色引领、履职为民’特色代表工作室等等，这些接地气、聚人气的平台载体为代表履职提供了广阔的舞台，有效激发了代表履职的活力。”甘肃省人大常委会党组书记、副主任胡焯指出，甘肃各级人大把搭平台建载体作为践行全过程人民民主、密切代表与人民群众联系的重要抓手和基础工程，在服务中心大局中展现了人大担当作为，充分彰显了全过程人民民主的生命力、感召力和创造力。" data-title="甘肃人大推进全过程人民民主实践 代表履职接地气惠民生" data-date="11-28 15:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-28 15:38</span>
          <span class="news-item-title">甘肃人大推进全过程人民民主实践 代表履职接地气惠民生</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/live/c60evlqlpx32t/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="台湾1965万选民将票选县市长、地方议员、乡镇村里长等将近1.11万名公职人员，同时公投决定日后能源政策。" data-title="台湾“九合一”选举：投票结束 全台各地投票所随即开票" data-date="11-28 08:00" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-28 08:00</span>
          <span class="news-item-title">台湾“九合一”选举：投票结束 全台各地投票所随即开票</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/27/us/politics/trump-congressional-investigations-contractors.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="即将上任的民主党多数派已开始在其计划的调查中将矛头指向企业和其他外部人士，但总统已威胁称，如果他们未经其许可就配合调查，他将解雇他们。" data-title="In Democrats vs. Trump, the Loser May Be Federal Contractors" data-date="11-27 23:47" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-27 23:47</span>
          <span class="news-item-title">In Democrats vs. Trump, the Loser May Be Federal Contractors</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/770.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 27 日消息，据央视财经报道，11 月 27 日，中国工程院彭先觉院士团队在成都介绍我国原创“Z 箍缩聚变裂变混合堆”供热示范堆工程初步规划。据介绍，Z 箍缩聚变裂变混合堆是我国科学家自主提出的一种将核聚变与核裂变相结合的技术方案。根据规划，工程拟分两个阶段实施，先开展聚变点火和核心工艺验证，再建设面向城市供热、工农业用热等需求的示范堆。IT之家获悉，按照初步规划，2026 年至 2030 年为核心技术攻关验证阶段，相关验证工作将依托由中国工程物理研究院流体物理所承建的“50MA 电磁驱动聚变大科学装置”开展。该装置已获国家发展改革委批复，计划于 2030 年在成都天府新区建成。第二阶段的供热示范堆拟于 2031 年至 2035 年建设，设计聚变功率为 200 兆瓦、热功" data-title="我国自主聚变能源解决方案发布工程初步规划，拟分两个阶段实施" data-date="11-27 22:58" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 22:58</span>
          <span class="news-item-title">我国自主聚变能源解决方案发布工程初步规划，拟分两个阶段实施</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/768.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 27 日消息，广汽集团旗下广汽能源在今日举行的 2026 广州车展上介绍了补能体系建设进展。广汽能源表示，截至 2026 年 11 月，在补能网络建设上，广汽自营充电网络已覆盖 31 个省级行政区、240 个城市，自营充电站达 2563 座、自营充电桩突破 3.3 万根。广汽能源同时透露，公司目标到 2027 年底补能网络覆盖 300 个城市、2030 年构建十万充电终端的生态网。加速在县域、高速沿线及北方高寒地区布局，并推进兆瓦级 10C 超充桩升级。" data-title="广汽能源：目前自营充电站达 2563 座，目标明年底旗下补能网络覆盖 300 个城市" data-date="11-27 22:40" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 22:40</span>
          <span class="news-item-title">广汽能源：目前自营充电站达 2563 座，目标明年底旗下补能网络覆盖 300 个城市</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/767.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 27 日消息，恒大汽车今日在港交所发布公告称，公司于 2026 年 11 月 27 日接获联交所函件，联交所上市委员会已决定根据上市规则第 6.01A (1) 条取消公司上市地位，原因是公司未能于 2026 年 9 月 30 日的复牌截止时间达成所有复牌指引。根据上市规则第 2B 章，恒大汽车有权在除牌决定发出日期起计七个营业日内，将决定提交上市复核委员会复核。若公司决定不申请复核，股份的最后上市日期为 2026 年 12 月 11 日，上市地位将自 2026 年 12 月 14 日上午 9 时起取消。公告称，董事会正征询顾问意见，并考虑是否提出请求，将除牌决定提交上市复核委员会作进一步复核。董事会同时提醒股东及潜在投资者，复核结果并不确定，公司将在适当时候另行公告。恒大" data-title="恒大汽车：香港联交所上市委员会决定取消公司的上市地位，最快 12 月 14 日摘牌" data-date="11-27 22:38" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 22:38</span>
          <span class="news-item-title">恒大汽车：香港联交所上市委员会决定取消公司的上市地位，最快 12 月 14 日摘牌</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/765.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 27 日消息，蔚来创始人、董事长、CEO 李斌在 2026 广州车展上接受每日经济新闻采访时透露，吉利汽车已经在规划和开发相关换电车型。今年是我们运营换电站的第 8 年，基本做好了对外开放的准备。面对换电业务开放合作话题，李斌直言，蔚来现在的换电业务是有限“开放”。“对蔚来来说，建设换电网络并不是加入的企业越多越好，因为我们还是要为用户提供相比其他换电网络更好的体验。”李斌解释称。吉利控股集团董事长李书福曾表示，吉利完全认同换电模式，新能源车电池是会衰减损坏的，但一台车的使用周期不止七八九年，这个矛盾必须找到解决方案，“直接换一块全新电池包，太贵；拆解翻新修复电池，成本同样很高。所以换电，就是解决这个问题。”据IT之家此前报道，9 月 28 日，蔚来与吉利控股集团达成充换" data-title="蔚来李斌：吉利汽车已经在规划和开发相关换电车型" data-date="11-27 22:32" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 22:32</span>
          <span class="news-item-title">蔚来李斌：吉利汽车已经在规划和开发相关换电车型</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/764.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 27 日消息，据新浪科技报道，在 2026 年第三季度业绩会上，美团 CEO 王兴表示，外卖行业在第三季度走到了拐点，主要有三个信号：客单价同比明显回升；低价订单占比环比持续收缩；行业补贴趋于理性，夏季促销季之后这一趋势尤为明显。这些变化都有利于真正具备经营实力的平台。王兴称，我们第三季度的业绩印证了这一点，依托全方位服务与运营能力，我们拿下了夏季旺季需求；用户结构与订单结构进一步改善，用户消费场景更加多元。行业领导地位继续巩固，单位经济模型优势进一步增强，背后是营销效率与运营效率的双重提升。IT之家注意到，美团今日发布 2026 年第三季度业绩报告。三季度，美团实现收入 1156 亿元，同比增长 21.6%；净利润同比由负转正，经调整净利润为 18.5 亿元，去年同期经" data-title="美团 CEO 王兴谈外卖行业拐点：客单价同比明显回升，行业补贴趋于理性" data-date="11-27 22:24" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 22:24</span>
          <span class="news-item-title">美团 CEO 王兴谈外卖行业拐点：客单价同比明显回升，行业补贴趋于理性</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10739076.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社北京11月27日电 (刘梦青)中国人民大学经济学院教授王孝松27日在北京表示，深圳APEC会议的举行对推动亚太共同体建设产生深远影响。" data-title="专家：深圳APEC会议对亚太共同体建设影响深远" data-date="11-27 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 21:54</span>
          <span class="news-item-title">专家：深圳APEC会议对亚太共同体建设影响深远</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-28 17:32（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
