import { createChart, CandlestickSeries, HistogramSeries, LineSeries,
  ColorType } from 'lightweight-charts';
import { createIcons, Maximize, RefreshCw } from 'lucide';

const root = document.querySelector('.market-workbench');
if (root) initialize();

function initialize() {
  createIcons({ icons: { Maximize, RefreshCw } });
  const host = root.querySelector('#market-chart');
  const empty = root.querySelector('#market-chart-empty');
  const status = root.querySelector('#market-chart-status');
  const ohlc = root.querySelector('#market-ohlc');
  const symbol = root.querySelector('#market-symbol');
  const periodButtons = [...root.querySelectorAll('[data-period]')];
  const maToggle = root.querySelector('#market-ma');
  const volumeToggle = root.querySelector('#market-volume');
  const periodNames = { hour: '小时 K', day: '日 K', week: '周 K', month: '月 K' };
  const upColor = '#e5484d', downColor = '#16a375';
  let database, activePeriod = 'day', activeBars = [], request = 0;
  const formatPrice = value => value.toLocaleString('zh-CN', { maximumFractionDigits: 3 });
  const formatTime = time => {
    if (typeof time === 'number') {
      return new Intl.DateTimeFormat('zh-CN', {
        timeZone: 'Asia/Shanghai', month: '2-digit', day: '2-digit',
        hour: '2-digit', minute: '2-digit', hourCycle: 'h23',
      }).format(new Date(time * 1000));
    }
    return typeof time === 'string' ? time : `${time.year}-${String(time.month).padStart(2, '0')}-${String(time.day).padStart(2, '0')}`;
  };
  const chart = createChart(host, {
    autoSize: true, height: host.clientHeight,
    layout: { attributionLogo: true, fontFamily: '"Segoe UI", "Microsoft YaHei", sans-serif' },
    localization: { locale: 'zh-CN', timeFormatter: formatTime },
    rightPriceScale: { borderVisible: false, scaleMargins: { top: .12, bottom: .27 } },
    timeScale: { borderVisible: false, rightOffset: 5, minBarSpacing: 2 },
    crosshair: { mode: 0 },
  });
  const candles = chart.addSeries(CandlestickSeries, {
    upColor, downColor, borderVisible: false, wickUpColor: upColor, wickDownColor: downColor,
  });
  const volume = chart.addSeries(HistogramSeries, {
    priceScaleId: 'volume', priceFormat: { type: 'volume' },
    priceLineVisible: false, lastValueVisible: false,
  });
  chart.priceScale('volume').applyOptions({ scaleMargins: { top: .81, bottom: 0 } });
  const ma5 = chart.addSeries(LineSeries, {
    color: '#c78a16', lineWidth: 1, priceLineVisible: false, lastValueVisible: false,
    crosshairMarkerVisible: false,
  });
  const ma20 = chart.addSeries(LineSeries, {
    color: '#3984d7', lineWidth: 1, priceLineVisible: false, lastValueVisible: false,
    crosshairMarkerVisible: false,
  });

  function applyTheme() {
    const css = getComputedStyle(root);
    const light = document.documentElement.dataset.theme === 'light';
    chart.applyOptions({
      layout: {
        background: { type: ColorType.Solid, color: light ? '#ffffff' : '#10151d' },
        textColor: css.getPropertyValue('--color-body').trim(),
      },
      grid: {
        vertLines: { color: light ? '#eef0f3' : '#202630' },
        horzLines: { color: light ? '#eef0f3' : '#202630' },
      },
    });
  }
  applyTheme();
  new MutationObserver(applyTheme).observe(document.documentElement, {
    attributes: true, attributeFilter: ['data-theme'],
  });
  function movingAverage(bars, window) {
    let sum = 0;
    return bars.flatMap((bar, i) => {
      sum += bar.close;
      if (i >= window) sum -= bars[i - window].close;
      return i >= window - 1 ? [{ time: bar.time, value: sum / window }] : [];
    });
  }
  function showOhlc(bar) {
    if (!bar) { ohlc.textContent = '暂无开高低收数据'; return; }
    const change = (bar.close / bar.open - 1) * 100;
    ohlc.replaceChildren();
    const fields = [
      [formatTime(bar.time), 'market-bar-date'], [`开 ${formatPrice(bar.open)}`],
      [`高 ${formatPrice(bar.high)}`], [`低 ${formatPrice(bar.low)}`],
      [`收 ${formatPrice(bar.close)}`, bar.close >= bar.open ? 'market-rise' : 'market-fall'],
      [`${change >= 0 ? '+' : ''}${change.toFixed(2)}%`, bar.close >= bar.open ? 'market-rise' : 'market-fall'],
    ];
    for (const [text, className] of fields) {
      const span = document.createElement('span');
      span.textContent = text;
      if (className) span.className = className;
      ohlc.append(span);
    }
  }
  chart.subscribeCrosshairMove(param => showOhlc(param.seriesData.get(candles) || activeBars.at(-1)));
  function clear(message) {
    activeBars = [];
    for (const series of [candles, volume, ma5, ma20]) series.setData([]);
    empty.textContent = message;
    empty.hidden = false;
    showOhlc();
  }
  function render() {
    const market = database?.markets[symbol.value];
    const volumeName = symbol.value.startsWith('hk') ? '成交额（港元）' : '成交量（手）';
    root.querySelector('#market-volume-label').textContent = volumeName;
    const periods = market?.periods || {};
    for (const button of periodButtons) {
      button.disabled = !periods[button.dataset.period]?.bars?.length;
      button.title = button.disabled ? '该品种暂无此周期的历史数据' : '';
      button.setAttribute('aria-pressed', String(button.dataset.period === activePeriod));
    }
    host.setAttribute('aria-label', `${market?.name || '行情'}${periodNames[activePeriod]}线与${volumeName}`);
    const data = periods[activePeriod];
    if (!data?.bars?.length) {
      clear('当前品种暂无此周期的历史行情，请选择其他周期或稍后刷新。');
      status.textContent = '暂无数据';
      return;
    }
    activeBars = data.bars;
    empty.hidden = true;
    candles.setData(activeBars);
    volume.setData(activeBars.map(bar => ({
      time: bar.time, value: bar.volume,
      color: bar.close >= bar.open ? '#e5484d55' : '#16a37555',
    })));
    ma5.setData(movingAverage(activeBars, 5));
    ma20.setData(movingAverage(activeBars, 20));
    chart.applyOptions({
      timeScale: {
        timeVisible: activePeriod === 'hour', secondsVisible: false,
        tickMarkFormatter: activePeriod === 'hour' ? time => formatTime(time) : undefined,
      },
    });
    chart.timeScale().setVisibleLogicalRange({
      from: Math.max(0, activeBars.length - (activePeriod === 'month' ? 48 : 90)),
      to: activeBars.length + 4,
    });
    showOhlc(activeBars.at(-1));
    const fetched = new Date(data.fetchedAt);
    const fetchedLabel = Number.isNaN(fetched.getTime()) ? '未知' :
      new Intl.DateTimeFormat('zh-CN', { timeZone: 'Asia/Shanghai',
        dateStyle: 'short', timeStyle: 'short' }).format(fetched);
    status.textContent = `${data.source} · ${activeBars.length} 根 · 截至 ${formatTime(activeBars.at(-1).time)} · 快照更新 ${fetchedLabel}`;
    document.querySelectorAll('.ticker-select').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.symbol === symbol.value));
    });
  }
  async function load() {
    const current = ++request;
    root.setAttribute('aria-busy', 'true');
    status.textContent = '正在获取 K 线数据…';
    try {
      const response = await fetch(root.dataset.historyUrl, {
        cache: 'no-cache', signal: AbortSignal.timeout(15000),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const next = await response.json();
      if (next.schemaVersion !== 1 || !next.markets) throw new Error('无效的行情数据');
      if (current !== request) return;
      database = next;
      render();
    } catch {
      if (current !== request) return;
      if (database) {
        render();
        status.textContent += ' · 刷新失败，保留已加载数据';
      } else {
        clear('历史行情暂时无法加载。请点击右上角刷新按钮重试。');
        status.textContent = '行情加载失败';
      }
    } finally {
      if (current === request) root.setAttribute('aria-busy', 'false');
    }
  }
  symbol.addEventListener('change', () => {
    if (!database?.markets[symbol.value]?.periods[activePeriod]) activePeriod = 'day';
    render();
  });
  periodButtons.forEach(button => button.addEventListener('click', () => {
    activePeriod = button.dataset.period;
    render();
  }));
  document.querySelectorAll('.ticker-select').forEach(button => {
    button.addEventListener('click', () => {
      symbol.value = button.dataset.symbol;
      symbol.dispatchEvent(new Event('change'));
      root.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth',
        block: 'start' });
    });
  });
  maToggle.addEventListener('change', () => {
    ma5.applyOptions({ visible: maToggle.checked });
    ma20.applyOptions({ visible: maToggle.checked });
  });
  volumeToggle.addEventListener('change', () => {
    volume.applyOptions({ visible: volumeToggle.checked });
    candles.priceScale().applyOptions({
      scaleMargins: { top: .12, bottom: volumeToggle.checked ? .27 : .08 },
    });
  });
  root.querySelector('#market-reset').addEventListener('click', () => chart.timeScale().fitContent());
  root.querySelector('#market-retry').addEventListener('click', load);
  load();
}
