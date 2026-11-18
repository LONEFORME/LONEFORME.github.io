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
      <span class="ticker-price ticker-down">27,001.78</span>
      <span class="ticker-change down">▼ -0.72%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-18 06:30:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">6.6683</span>
      <span class="ticker-change up">▲ +0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 08:54:12（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">$3,819.20 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change down">▼ -29.97 (-0.78%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 08:54:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">¥829.86 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change down">▼ -2.47 (-0.30%)</span>
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
      <span class="ticker-price ticker-up">$93.55 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change up">▲ +1.11 (+1.20%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 06:59:57（非实时）</div>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/business/southeast-asia-china-ai-chips.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="美国的新限制措施可能危及数十亿美元的投资，并迫使该地区的国家在华盛顿与北京之间寻求日益艰难的平衡。" data-title="Trump’s New A.I. Chip Rules Rattle Southeast Asia" data-date="11-18 05:04" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 05:04</span>
          <span class="news-item-title">Trump’s New A.I. Chip Rules Rattle Southeast Asia</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6n4ex4y9837o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="柯志恩以“知识蓝”的姿态拉拢中间选民，支持度大幅追贴深耕高雄20年的赖瑞隆，选情咬紧。" data-title="台湾高雄市选战：“知识蓝”柯志恩对决“新潮流”赖瑞隆，国民党有可能复制“韩流”吗？" data-date="11-18 00:25" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 00:25</span>
          <span class="news-item-title">台湾高雄市选战：“知识蓝”柯志恩对决“新潮流”赖瑞隆，国民党有可能复制“韩流”吗？</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/564.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 18 日消息，在昨晚的巴黎发布会上，小米 18 Pro 系列手机国际版正式发布，把背屏设计带向海外，售价 1,399 欧元（IT之家注：现汇率约合 10,278 元人民币）起。小米 18 Pro（电池 6000mAh | 骁龙 8E6）12GB+256GB 规格：1,399 欧元（现汇率约合 10,278 元人民币）；12GB+512GB 规格：1,599 欧元（现汇率约合 11,748 元人民币）。小米 18 Pro Max（电池 7050mAh | 骁龙 8EE6）12GB+256GB 规格：1,599 欧元（现汇率约合 11,748 元人民币）；12GB+512GB 规格：1,799 欧元（现汇率约合 13,217 元人民币）；16GB+1TB 规格：2,099 欧" data-title="小米 18 Pro 系列手机国际版正式发布：把背屏带向海外，1399 欧元起" data-date="11-18 00:20" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 00:20</span>
          <span class="news-item-title">小米 18 Pro 系列手机国际版正式发布：把背屏带向海外，1399 欧元起</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/business/1035366/kalshi-stock-trading" target="_blank" rel="noopener" data-cat="caijing" data-summary="据《华尔街日报》和CNBC报道，Kalshi正准备在其平台上提供股票交易服务。据报道，该公司计划利用其收购的经纪商FB Securities推出股票和交易所交易基金，&quot;以" data-title="Kalshi moves into a new kind of gambling: the stock market" data-date="11-17 23:35" data-source="The Verge">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 23:35</span>
          <span class="news-item-title">Kalshi moves into a new kind of gambling: the stock market</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/561.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，据路透社今天（17 日）援引两名知情人士消息称，面对劳动力成本上涨及制造业回流美国带来的成本压力，通用汽车计划到 2028 年，将北美工厂的机器人及其他自动化技术应用规模提高 20%。多名消息人士称，通用汽车同时也在自主研发机器人，并在印第安纳州科科莫工厂进行组装，重点开发用于厂内零部件运输的自主移动机器人。通用汽车去年曾介绍自主研发机器人技术的计划，目前仍同时向外部供应商采购机器人设备。另外两名熟悉通用汽车供应链的人士透露，通用汽车还要求参与新合同竞标的零部件供应商提交自动化方案，并对供应商的自动化水平进行评分，将评分结果作为合同评审的依据之一。通用汽车称，采用自动化技术是为了改善生产安全、提高质量和效率。“随着全球竞争日益激烈，我们会继续运用这些技术，为" data-title="靠机器人缓解成本压力，通用汽车计划到 2028 年将北美工厂自动化规模提升 20%" data-date="11-17 23:12" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 23:12</span>
          <span class="news-item-title">靠机器人缓解成本压力，通用汽车计划到 2028 年将北美工厂自动化规模提升 20%</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/544.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，据路透社报道，索尼在英国赢得了一场索赔近 20 亿英镑（IT之家注：现汇率约合 176.11 亿元人民币）的诉讼。当地时间 17 日，伦敦竞争上诉法庭驳回了全部诉讼请求，认定原告未能证明索尼利用 PlayStation 的垄断地位抬高数字游戏价格，违反竞争法。原告指控，索尼滥用市场支配地位，强制 PlayStation 主机的数字游戏及附加内容只能通过 PlayStation Store 交易，导致数字版游戏比实体版更贵。索尼在庭审中反驳称，公司耗费多年时间、投入数十亿资金打造的一体化游戏平台，在竞争激烈的游戏市场中为消费者带来了益处，任天堂和微软 Xbox 等竞争对手也采用类似的经营模式。该案今年 3 月开庭审理。伦敦竞争上诉法庭作出裁决，认为集体诉讼原告" data-title="索尼赢得英国近 20 亿英镑诉讼：PlayStation 数字游戏定价未被认定违法" data-date="11-17 22:46" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 22:46</span>
          <span class="news-item-title">索尼赢得英国近 20 亿英镑诉讼：PlayStation 数字游戏定价未被认定违法</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/543.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 17 日消息，比亚迪汽车官方刚刚发布视频，分享了集团董事长兼总裁王传福在 2026 年 APEC 工商领导人峰会上的完整版讲话。面对主持人提问：“可持续发展对于比亚迪来说是什么定位？”王传福直言：“只有可持续发展才能实现长期发展，‘我赢你输’的路子走不远。”王传福表示，地球也是一样，只有可持续环境改善的发展，才能真正让人类持续成长、持续进步。因此，我们在发展的同时，也要改善好我们的环境，要减少二氧化碳的排放。据IT之家今日早些时候报道，王传福还在 APEC 2026 表示，可持续发展是一个全球目标，而中国在这方面做得卓有成效。他提到，过去几年，我国政府在这方面做出了很多贡献。中国的新能源汽车发展到今天如此大的规模，占到全球差不多 2/3 的新能源汽车，新能源汽车的供应链也" data-title="比亚迪王传福：只有可持续发展才能实现长期发展，“我赢你输”的路子走不远" data-date="11-17 22:45" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 22:45</span>
          <span class="news-item-title">比亚迪王传福：只有可持续发展才能实现长期发展，“我赢你输”的路子走不远</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733788.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="深圳的土地面积在全国中大城市里面几乎是最小的，但它每平方公里单位电力负荷却又是全国最高的。2026年APEC领导人会议期间，重要会场、交通枢纽等场所实现100%绿电供应，这是如何做到的？超大城市能源保供、低碳实践正画出什么样的图景？" data-title="绿电点亮APEC会场 在深圳看见中国式现代化城市样本" data-date="11-17 22:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 22:28</span>
          <span class="news-item-title">绿电点亮APEC会场 在深圳看见中国式现代化城市样本</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733787.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="亚太经合组织第三十三次领导人非正式会议即将在深圳举行。面对亚太向何处去的时代课题，各方期待中国理念、中国方案再次引领亚太合作航向，汇聚起推动区域发展的强大合力。会场筹备进展如何？本次会议有哪些核心看点？" data-title="APEC与会各经济体领导人将共商亚太发展大计" data-date="11-17 22:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 22:25</span>
          <span class="news-item-title">APEC与会各经济体领导人将共商亚太发展大计</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733772.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网布鲁塞尔11月17日电 (记者 德永健)欧盟17日发布欧洲经济秋季展望报告，表示受商品出口强劲反弹等因素驱动，今年前三季度欧盟经济增长好于预期。" data-title="欧盟称今年前三季度经济增长好于预期" data-date="11-17 21:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 21:46</span>
          <span class="news-item-title">欧盟称今年前三季度经济增长好于预期</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733736.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网雄安11月17日电 (李玉素 韩冰)17日，2026知识产权服务万里行“知识产权服务重点产业高质量发展暨科技成果赋智中小企业深度行”活动在河北雄安新区举行。" data-title="2026知识产权服务万里行雄安站活动举办" data-date="11-17 21:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 21:25</span>
          <span class="news-item-title">2026知识产权服务万里行雄安站活动举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733734.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网丽水11月17日电(傅飞扬 朱慧 吴陈芊芊)连日来，浙江省丽水市庆元县百山祖镇斋郎村迎来高山花椰菜集中采收季。田垄间，绿叶簇拥着洁白紧实的花球，村民们弯腰采摘、分拣装筐，忙碌的身影随处可见。" data-title="（乡村行·看振兴）浙江庆元：花椰菜“长成”大产业 留守老人家门口增收" data-date="11-17 21:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 21:18</span>
          <span class="news-item-title">（乡村行·看振兴）浙江庆元：花椰菜“长成”大产业 留守老人家门口增收</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733700.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社曼谷11月17日电 (王茜 李映民)泰国政府17日批准多项税收优惠措施，帮助受泰柬边境冲突及洪灾影响的民众减轻财产损失带来的经济负担。其中，符合条件的个人纳税人可按实际支出抵扣房屋维修费用，最高10万泰铢(约合2.2万元人民币)，车辆维修费用最高可抵扣3万泰铢。" data-title="泰国推出税收优惠措施帮助受边境局势及洪灾影响的民众" data-date="11-17 20:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 20:17</span>
          <span class="news-item-title">泰国推出税收优惠措施帮助受边境局势及洪灾影响的民众</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/business/trump-xi-meeting-tensions.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="公开表达的友好态度与日益增加的贸易和投资限制形成鲜明对比，凸显出这两个经济体之间日益扩大的裂痕。" data-title="As Trump and Xi Mingle, Their Governments Are Arming Up" data-date="11-17 18:03" data-source="纽约时报">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 18:03</span>
          <span class="news-item-title">As Trump and Xi Mingle, Their Governments Are Arming Up</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ck5y1g89jnnxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="台湾试图以企业家身份与科技优势扩大能见度，中国则以原则框架维持主导权。APEC作为平台，或许能让双方同时在场，但仍难以消弭两岸在全球外交参与的既有分歧。" data-title="APEC深圳峰会：赖清德派施振荣出席 台湾参会空间再成焦点" data-date="11-17 16:44" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 16:44</span>
          <span class="news-item-title">APEC深圳峰会：赖清德派施振荣出席 台湾参会空间再成焦点</span>
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

<p class="news-updated">🕐 页面生成于 2026-11-18 05:08（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
