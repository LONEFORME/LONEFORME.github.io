---
layout: default
title: 热点新闻
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">每日聚合全球英超足球、前沿科技与国际时政焦点（电脑端悬浮即览深度特稿 · 手机端自适应浏览）</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>2026-10-12 16:10 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar">
    <svg class="news-search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" class="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)">
    <span id="news-search-count" class="news-search-count"></span>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">56</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">13</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">13</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('source', this)">
        <span>🌐 媒体信源</span>
      </button>
    </div>

    <a href="{{ "/archive" | relative_url }}" class="archive-btn-compact" title="翻阅往期历史档案">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>往期归档</span>
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </a>
  </div>
</div>
<div class="news-overview-bar">
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · IT之家×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-12/10712084.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会。" data-title="外交部介绍王毅访问克罗地亚、黑山、保加利亚3国安排和期待" data-date="10-12 16:03" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-12 16:03</span>
      </div>
      <h2 class="hero-featured-title">外交部介绍王毅访问克罗地亚、黑山、保加利亚3国安排和期待</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/948.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 12 日消息，Arena（arena.ai）平台发布 2026 年第 41 周 AI 大模型排行榜，覆盖时间为 2026-10-05 ~ 2026-10-11。本期榜单中，Anthropic 全新 Claude Opus 5.5 Max 首次入榜智能体榜即夺得第一；国产模型 kimi-k3-max 稳居综合榜前 20，qwen3.8-max 等多款国产模型保持稳定排名，整体处于中上游梯队。IT之家注：本榜单基于 Arena（arena.ai）平台匿名盲测投票，通过 ELO（智能体榜为百分比信号）计算排名，反映用户主观偏好而非绝对能力测试；不同分榜相互独立，不宜跨榜比较，分差在误差范围内均视为并列，新模型也需积累一定投票量后才会正式入榜。综合榜本周综合榜头部格局相对稳定，g" data-title="Arena 公布新一轮 AI 大模型周榜：Claude Opus 5.5 Max 首登智能体榜首，国产多模型稳定中上游" data-date="10-12 16:04" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">Arena 公布新一轮 AI 大模型周榜：Claude Opus 5.5 Max 首登智能体榜首，国产多模型稳定中上游</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/937.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 12 日消息，据科技媒体 Windows Latest 今天报道，在微软工作 30 多年的资深员工 Raymond Chen，最近向 Win11 用户提出建议：不要同时使用两个或以上杀毒软件。据报道，Raymond Chen 帮某位同事调查 Windows 11 企业版系统故障时发现，两款杀毒软件发生了冲突，第一款杀软试图隔离某软件所属进程，而第二款杀软也成功隔离了该软件的进程。他对此表示：“在同一台电脑上安装两款反恶意软件，就像同时雇用两家安保公司巡视同一栋大楼。我说这个并不是替 Microsoft Defender 辩护。如果它们彼此不了解对方存在，就会认为对方是入侵者。运气好的话，它们的指令还只是报告可以活动。”他指出，杀毒软件并不像保安一样可以互相认识。你不能指望" data-title="微软 30 年老员工忠告：Win11 不要装两个或以上杀毒软件" data-date="10-12 15:51" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">微软 30 年老员工忠告：Win11 不要装两个或以上杀毒软件</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/938.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，泰坦军团 (TitanArmy) 今日公布了显示器新品 P279 PLUS。其基于 27&quot; 平面 Fast IPS 面板，分辨率 QHD (2560×1440)，原生刷新率 200Hz、超频刷新率 230Hz。P279 PLUS 拥有 350nits 的 SDR 全屏亮度、400nits 的 HDR 峰值亮度，静态对比度 1000:1；响应时间低至 1ms；色深 8bit + FRC，色域 99% sRGB，色偏（平均值）ΔE＜2。其支持硬件级低蓝光；提供 2 个 HDMI 2.0、1 个 DisplayPort 1.4、1 个 3.5mm 音频输出插孔；原装配备 -5°~+20° 俯仰调节支架，兼容 100×100 (mm) VESA 壁挂规范。" data-title="泰坦军团公布 P279 PLUS 显示器：QHD 230Hz Fast IPS，峰值亮度 400nits" data-date="10-12 15:57" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">泰坦军团公布 P279 PLUS 显示器：QHD 230Hz Fast IPS，峰值亮度 400nits</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712084.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会。" data-title="外交部介绍王毅访问克罗地亚、黑山、保加利亚3国安排和期待" data-date="10-12 16:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 16:03</span>
          <span class="news-item-title">外交部介绍王毅访问克罗地亚、黑山、保加利亚3国安排和期待</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712077.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会。" data-title="美国制裁国际刑事法院 中国外交部回应" data-date="10-12 15:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:54</span>
          <span class="news-item-title">美国制裁国际刑事法院 中国外交部回应</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqy0rd16x33lo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="胡塞武装加强了对沙特阿拉伯领土的攻击，尽管实体损害能够迅速修复，但其稳定声誉正遭受重创。" data-title="胡塞武装空袭沙特利雅德机场 中东冲突又一危险时刻" data-date="10-12 15:51" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 15:51</span>
          <span class="news-item-title">胡塞武装空袭沙特利雅德机场 中东冲突又一危险时刻</span>
          <span class="news-value-point">💡 胡塞武装加强了对沙特阿拉伯领土的攻击，尽管实体损害能够迅速修复，但其稳定声誉正遭受重创</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712074.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会。" data-title="尼泊尔最新洪灾是否影响到中国公民？中方回应" data-date="10-12 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:49</span>
          <span class="news-item-title">尼泊尔最新洪灾是否影响到中国公民？中方回应</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712073.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会。" data-title="中方回应对巴拉圭和伯利兹个别政客实施反制：加以惩戒，以儆效尤" data-date="10-12 15:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:46</span>
          <span class="news-item-title">中方回应对巴拉圭和伯利兹个别政客实施反制：加以惩戒，以儆效尤</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712070.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会。" data-title="中方近期是否会发布关于前往印度的旅行警告？外交部回应" data-date="10-12 15:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:45</span>
          <span class="news-item-title">中方近期是否会发布关于前往印度的旅行警告？外交部回应</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712066.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会。" data-title="中方：敦促日本当政者倾听和重视国内正义之声" data-date="10-12 15:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:42</span>
          <span class="news-item-title">中方：敦促日本当政者倾听和重视国内正义之声</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦 李京泽)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712062.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月12日电 (记者 郭超凯)记者从中国公安部获悉，广东湛江、广西防城港、云南昆明、新疆乌鲁木齐等多地12日同步开展罚没走私烟草集中销毁暨“强治理、护民安、促发展”普法宣传活动，共计销毁走私卷烟1.88亿支、电子烟5.5万余支、烟丝2.7吨。" data-title="中国多地公开销毁走私卷烟1.88亿支 烟丝2.7吨" data-date="10-12 15:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:41</span>
          <span class="news-item-title">中国多地公开销毁走私卷烟1.88亿支 烟丝2.7吨</span>
          <span class="news-value-point">💡 中新社北京10月12日电 (记者 郭超凯)记者从中国公安部获悉，广东湛江、广西防城港、云南昆明、新疆乌鲁木齐等多地12日同步开展罚没走私烟草集中…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712064.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会。" data-title="也门胡塞武装打击沙特机场 中方：一贯反对针对平民和民用设施的袭击" data-date="10-12 15:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:41</span>
          <span class="news-item-title">也门胡塞武装打击沙特机场 中方：一贯反对针对平民和民用设施的袭击</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712063.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会。" data-title="外交部：同“台独”势力绑在一起没有任何前途" data-date="10-12 15:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:40</span>
          <span class="news-item-title">外交部：同“台独”势力绑在一起没有任何前途</span>
          <span class="news-value-point">💡 中新网北京10月12日电 (记者 黄钰钦)中国外交部发言人毛宁12日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10712021.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月12日电 据阿尔及利亚通讯社报道，阿尔及利亚国家警察总局当地时间11日发表声明称，阿警方逮捕了61名摩洛哥公民，因其涉嫌策划危害阿国家安全和公共秩序的破坏活动。" data-title="阿尔及利亚逮捕61名摩洛哥公民 称其涉嫌策划破坏活动" data-date="10-12 15:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:13</span>
          <span class="news-item-title">阿尔及利亚逮捕61名摩洛哥公民 称其涉嫌策划破坏活动</span>
          <span class="news-value-point">💡 中新网北京10月12日电 据阿尔及利亚通讯社报道，阿尔及利亚国家警察总局当地时间11日发表声明称，阿警方逮捕了61名摩洛哥公民，因其涉嫌策划危害…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10712038.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月12日电 综合外媒11日报道，美国总统特朗普呼吁更换乌克兰总统泽连斯基，英国国防大臣斯特里廷对此明确表示，英国支持泽连斯基。" data-title="特朗普称乌克兰应该换总统 英大臣：我们支持泽连斯基" data-date="10-12 15:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:10</span>
          <span class="news-item-title">特朗普称乌克兰应该换总统 英大臣：我们支持泽连斯基</span>
          <span class="news-value-point">💡 中新网10月12日电 综合外媒11日报道，美国总统特朗普呼吁更换乌克兰总统泽连斯基，英国国防大臣斯特里廷对此明确表示，英国支持泽连斯基</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10711973.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网深圳10月12日电 (记者 郭超凯)10月11日，由外交学院主办的“落实抚仙会晤共识 夯实持久和平根基”第三次中柬泰二轨对话会在深圳举行。外交学院副院长孙吉胜在参会期间接受中新社记者专访，梳理三次对话会的脉络并解读二轨对话在化解地区争端中的现实作用和意义。" data-title="专访孙吉胜：发挥二轨对话独特作用 为促进柬泰关系缓和积蓄和平力量" data-date="10-12 14:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 14:41</span>
          <span class="news-item-title">专访孙吉胜：发挥二轨对话独特作用 为促进柬泰关系缓和积蓄和平力量</span>
          <span class="news-value-point">💡 中新网深圳10月12日电 (记者 郭超凯)10月11日，由外交学院主办的“落实抚仙会晤共识 夯实持久和平根基”第三次中柬泰二轨对话会在深圳举行</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cm4g1d4p2k2no/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该协议在美国中期选举前几周宣布，共和党和民主党议员都提出了批评。" data-title="特朗普计划从俄罗斯进口柴油 反对声浪趋涨" data-date="10-12 13:38" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 13:38</span>
          <span class="news-item-title">特朗普计划从俄罗斯进口柴油 反对声浪趋涨</span>
          <span class="news-value-point">💡 该协议在美国中期选举前几周宣布，共和党和民主党议员都提出了批评</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10711959.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国新闻周刊记者：曹然" data-title="冈比亚的“疟疾战争”" data-date="10-12 13:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 13:37</span>
          <span class="news-item-title">冈比亚的“疟疾战争”</span>
          <span class="news-value-point">💡 中国新闻周刊记者：曹然</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/948.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 12 日消息，Arena（arena.ai）平台发布 2026 年第 41 周 AI 大模型排行榜，覆盖时间为 2026-10-05 ~ 2026-10-11。本期榜单中，Anthropic 全新 Claude Opus 5.5 Max 首次入榜智能体榜即夺得第一；国产模型 kimi-k3-max 稳居综合榜前 20，qwen3.8-max 等多款国产模型保持稳定排名，整体处于中上游梯队。IT之家注：本榜单基于 Arena（arena.ai）平台匿名盲测投票，通过 ELO（智能体榜为百分比信号）计算排名，反映用户主观偏好而非绝对能力测试；不同分榜相互独立，不宜跨榜比较，分差在误差范围内均视为并列，新模型也需积累一定投票量后才会正式入榜。综合榜本周综合榜头部格局相对稳定，g" data-title="Arena 公布新一轮 AI 大模型周榜：Claude Opus 5.5 Max 首登智能体榜首，国产多模型稳定中上游" data-date="10-12 16:04" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 16:04</span>
          <span class="news-item-title">Arena 公布新一轮 AI 大模型周榜：Claude Opus 5.5 Max 首登智能体榜首，国产多模型稳定中上游</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，Arena（arena.ai）平台发布 2026 年第 41 周 AI 大模型排行榜，覆盖时间为 2026-1…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/942.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 12 日消息，据 @数码闲聊站 今日爆料，某厂阔屏直板机现阶段工程机测试天玑旗舰芯，影像最高测试大底双 2 亿，配备 6.35 英寸阔屏，大概率定位是 Pro。结合该博主的爆料习惯，新机预计为 OPPO 旗下。该博主此前爆料，OPPO 阔直板工程机是标准 16:9，LIPO 极窄四等边设计，目测边框 1mm±，看标准视频会铺满整块屏幕，机身宽度大概是 81mm。IT之家注意到，除了阔屏直板机，还有爆料显示 OPPO 有望推出搭载 2nm 芯片的阔折叠。该机预计采用 7.6 英寸无痕铰链方案，工程机是三星屏，搭载 200Mp 大底主摄 +50Mp 超广角 +50Mp 潜望长焦 +3Mp 多光谱镜头，哈苏全焦段影像，主打轻薄无痕全能。" data-title="消息称阔屏直板工程机测试天玑旗舰芯，预计为 OPPO 旗下" data-date="10-12 16:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 16:01</span>
          <span class="news-item-title">消息称阔屏直板工程机测试天玑旗舰芯，预计为 OPPO 旗下</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，据 @数码闲聊站 今日爆料，某厂阔屏直板机现阶段工程机测试天玑旗舰芯，影像最高测试大底双 2 亿，配备 6.3…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/939.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 12 日现场消息，华为终端创新技术沟通会今日在上海练秋湖启幕。根据安排，活动将持续至明日。今天是活动的第一天，IT之家在现场了解到，首发登场的十大技术是灵珑屏、灵盾防窥屏、昆仑玻璃、华为悦彰、麒麟芯片、XMAGE 华为睿影、玄武架构、天工铰链、星迹定位和静谧通话。预计明天将介绍云晰柔光屏、小艺、方舟引擎、星闪、鸿蒙星河互联、鸿蒙星盾安全、鸿蒙空间计算、TruSense 玄玑感知系统和巨鲸电池等技术。今天活动的十大技术核心信息目前已公布，IT之家附如下：" data-title="2026 华为终端创新技术沟通会首日十大技术品牌亮相，一图读懂" data-date="10-12 15:58" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 15:58</span>
          <span class="news-item-title">2026 华为终端创新技术沟通会首日十大技术品牌亮相，一图读懂</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日现场消息，华为终端创新技术沟通会今日在上海练秋湖启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712068.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网武汉10月12日电 (记者 马芙蓉)华中科技大学同济医学院附属协和医院12日召开新闻发布会宣布，该院联合相关企业研发出中国国内首个“基于高通道矩阵式电刺激的脑机接口精细运动重建系统”，探索帮助运动功能障碍者从手部抓握训练，逐步迈向手指精细操作。" data-title="科研团队研发脑机接口精细运动重建系统" data-date="10-12 15:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:48</span>
          <span class="news-item-title">科研团队研发脑机接口精细运动重建系统</span>
          <span class="news-value-point">💡 中新网武汉10月12日电 (记者 马芙蓉)华中科技大学同济医学院附属协和医院12日召开新闻发布会宣布，该院联合相关企业研发出中国国内首个“基于高…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/nyregion/mamdani-columbus-day-parade-nyc.html" target="_blank" rel="noopener" data-cat="keji" data-summary="市政厅证实，市长不会参加周一在第五大道举行的游行，但很快将举办意大利裔美国人遗产招待会。" data-title="Mamdani to Skip Columbus Day Parade. Some Italian Americans Are Glad." data-date="10-12 07:51" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 07:51</span>
          <span class="news-item-title">马姆达尼（ Mamdani ） ，无需参加哥伦布日游行。一些意大利裔美国人很高兴。</span>
          <span class="news-item-title-en">Mamdani to Skip Columbus Day Parade. Some Italian Americans Are Glad.</span>
          <span class="news-value-point">💡 市政厅证实，市长不会参加周一在第五大道举行的游行，但很快将举办意大利裔美国人遗产招待会</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1009406/silicon-valley-is-falling-in-line-with-trumps-attempt-to-rename-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="当唐纳德·特朗普总统宣布他计划将人工智能重新命名为“超级智能”时，你会原谅对它会流行的怀疑。虽然大多数人坚持使用人工智能，但硅谷的一些人" data-title="Silicon Valley is falling in line with Trump’s attempt to rename AI" data-date="10-12 02:33" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-12 02:33</span>
          <span class="news-item-title">硅谷正在与特朗普重命名AI的尝试保持一致</span>
          <span class="news-item-title-en">Silicon Valley is falling in line with Trump’s attempt to rename AI</span>
          <span class="news-value-point">💡 当唐纳德·特朗普总统宣布他计划将人工智能重新命名为“超级智能”时，你会原谅对它会流行的怀疑</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/can-the-ai-industry-persuade-data-center-opponents-by-getting-rid-of-ndas/" target="_blank" rel="noopener" data-cat="keji" data-summary="在Equity上，我们讨论了数据中心暂停的影响以及人工智能行业是否存在通信问题。" data-title="Can the AI industry persuade data center opponents by getting rid of NDAs?" data-date="10-12 00:52" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-12 00:52</span>
          <span class="news-item-title">人工智能行业能否通过摆脱保密协议来说服数据中心的对手？</span>
          <span class="news-item-title-en">Can the AI industry persuade data center opponents by getting rid of NDAs?</span>
          <span class="news-value-point">💡 在Equity上，我们讨论了数据中心暂停的影响以及人工智能行业是否存在通信问题</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/714.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，苹果将在本周二举行“欢迎回家”活动，主角预计是 HomeView 智能家庭中枢，除此之外还有新款 HomePod mini 和 Apple TV 4K。据彭博社记者马克 · 古尔曼今日透露，新款 Apple TV 4K 将在 10 月 30 日发售，苹果已在这款新品中测试内置麦克风，用户直接说出 Siri 就能进行语音交互。IT之家了解到，现款 Apple TV 4K 仅在 Siri Remote 中带有麦克风，用户必须对着遥控器或 HomePod 说话，才能使用 Siri。同时，苹果还将重新设计 Siri Remote 遥控器，这款配件将内置扬声器，方便用户找出掉在沙发坐垫的遥控器。此外，新款 HomePod mini 预计将配备 S10 芯片，同样也是" data-title="曝苹果新一代 Apple TV 4K 内置麦克风、Siri Remote 遥控器将配扬声器便于查找" data-date="10-11 23:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 23:20</span>
          <span class="news-item-title">曝苹果新一代 Apple TV 4K 内置麦克风、Siri Remote 遥控器将配扬声器便于查找</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，苹果将在本周二举行“欢迎回家”活动，主角预计是 HomeView 智能家庭中枢，除此之外还有新款 HomePo…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/711.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，据博主 @体验more 爆料，荣耀 WIN Pad 平板搭载第五代骁龙 8 至尊版处理器，配备 8.4 英寸 240Hz OLED 平板、主动散热风扇，和 iQOO Pad Pro 都是本月发布。据博主 @数码闲聊站 于 9 月 21 日爆料，荣耀 WIN2 系列 +WIN Pad 小平板确定 10 月发布。据其爆料，荣耀 WIN2 系列顶配搭载骁龙 8EE6（第六代骁龙 8 超级至尊版处理器）+ 主动散热风扇 + 超高刷 OLED ，今年唯一万级大电池的 2nm 新机。小平板搭载骁龙 8E5（第五代骁龙 8 至尊版处理器）+ 主动散热风扇 +8 英寸级别超高刷 OLED，没有 5G 通信版本。此外，该博主 @数码闲聊站 后续再爆料，荣耀 WIN Pad 小" data-title="消息称荣耀 WIN Pad 平板搭载 8.4 英寸 240Hz OLED 屏，本月发布" data-date="10-11 22:55" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:55</span>
          <span class="news-item-title">消息称荣耀 WIN Pad 平板搭载 8.4 英寸 240Hz OLED 屏，本月发布</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，据博主 @体验more 爆料，荣耀 WIN Pad 平板搭载第五代骁龙 8 至尊版处理器，配备 8.4 英寸 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/708.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，粤芯半导体技术股份有限公司今日宣布，公司将于 2026 年 10 月 13 日（下周二）在深圳证券交易所创业板上市。本次发行价格为 12.01 元 / 股，发行后总股本为 28.78 亿股（超额配售选择权行使前）。IT之家了解到，粤芯半导体已在 9 月 28 日公开网上摇号中签结果，中签号码共有 358848 个，每个中签号码可认购 500 股粤芯半导体 A 股股票。本次发行最终战略配售数量为 25632.30 万股，网上最终发行数量为 17942.40 万股，网下最终发行数量为 15379.50 万股。网上投资者放弃认购 468976 股，由广发证券包销，包销金额 563.24 万元。互联网公开资料显示，粤芯半导体成立于 2017 年，总部位于广州市黄埔区" data-title="粤芯半导体 10 月 13 日在创业板上市，发行价为 12.01 元 / 股" data-date="10-11 22:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:27</span>
          <span class="news-item-title">粤芯半导体 10 月 13 日在创业板上市，发行价为 12.01 元 / 股</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，粤芯半导体技术股份有限公司今日宣布，公司将于 2026 年 10 月 13 日（下周二）在深圳证券交易所创业板…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/modder-discovers-that-putting-a-gpu-in-the-wrong-place-can-deliver-a-19-degree-cooler-hotspot-breaking-convention-can-produce-great-results-despite-decades-of-pc-diy-evolution" target="_blank" rel="noopener" data-cat="keji" data-summary="在PC DIY中，它可能仍然值得挑战传统，正如TrashBench所展示的那样，他的GPU热点最高可达19摄氏度。" data-title="Modder discovers that putting a GPU in the &#39;wrong place&#39; can deliver a 19 degree cooler hotspot" data-date="10-11 22:23" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-11 22:23</span>
          <span class="news-item-title">Modder发现，将GPU放在“错误的位置”可以提供19度更冷的热点</span>
          <span class="news-item-title-en">Modder discovers that putting a GPU in the 'wrong place' can deliver a 19 degree cooler hotspot</span>
          <span class="news-value-point">💡 在PC DIY中，它可能仍然值得挑战传统，正如TrashBench所展示的那样，他的GPU热点最高可达19摄氏度</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/these-execs-think-voice-ai-hasnt-reached-its-chatgpt-moment-yet/" target="_blank" rel="noopener" data-cat="keji" data-summary="语音人工智能经常错过上下文层的重要点，并导致整个管道中断" data-title="These execs think voice AI hasn’t reached its ChatGPT moment yet" data-date="10-11 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-11 22:00</span>
          <span class="news-item-title">这些高管认为语音AI尚未达到ChatGPT时刻</span>
          <span class="news-item-title-en">These execs think voice AI hasn’t reached its ChatGPT moment yet</span>
          <span class="news-value-point">💡 语音人工智能经常错过上下文层的重要点，并导致整个管道中断</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress" target="_blank" rel="noopener" data-cat="keji" data-summary="我正在踏上一段迄今为止一直犹豫不决的旅程：实际上是定期使用人工智能。将大多数个人数据提供给云服务对我来说是一个主要障碍，但越来越有可能在本地运行强大的模型，以了解" data-title="Learning to use local AI is exciting, overwhelming, and frustrating" data-date="10-11 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 19:00</span>
          <span class="news-item-title">学习使用本地人工智能是令人兴奋、不知所措和令人沮丧的</span>
          <span class="news-item-title-en">Learning to use local AI is exciting, overwhelming, and frustrating</span>
          <span class="news-value-point">💡 我正在踏上一段迄今为止一直犹豫不决的旅程：实际上是定期使用人工智能</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/937.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 12 日消息，据科技媒体 Windows Latest 今天报道，在微软工作 30 多年的资深员工 Raymond Chen，最近向 Win11 用户提出建议：不要同时使用两个或以上杀毒软件。据报道，Raymond Chen 帮某位同事调查 Windows 11 企业版系统故障时发现，两款杀毒软件发生了冲突，第一款杀软试图隔离某软件所属进程，而第二款杀软也成功隔离了该软件的进程。他对此表示：“在同一台电脑上安装两款反恶意软件，就像同时雇用两家安保公司巡视同一栋大楼。我说这个并不是替 Microsoft Defender 辩护。如果它们彼此不了解对方存在，就会认为对方是入侵者。运气好的话，它们的指令还只是报告可以活动。”他指出，杀毒软件并不像保安一样可以互相认识。你不能指望" data-title="微软 30 年老员工忠告：Win11 不要装两个或以上杀毒软件" data-date="10-12 15:51" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 15:51</span>
          <span class="news-item-title">微软 30 年老员工忠告：Win11 不要装两个或以上杀毒软件</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，据科技媒体 Windows Latest 今天报道，在微软工作 30 多年的资深员工 Raymond Chen…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/12/premier-league-10-talking-points-from-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城对胜利毫不后悔，马刺取得了某种进步，诺尼·马杜埃克迎接了这一时刻。曼城在利物浦获胜的方式既是辩护也是诽谤。那些兴高采烈地挥舞着充气香蕉" data-title="Premier League: 10 talking points from the weekend’s action" data-date="10-12 15:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 15:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 曼城对胜利毫不后悔，马刺取得了某种进步，诺尼·马杜埃克迎接了这一时刻</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/impervious-city-shrug-off-chaos-and-controversy-to-silence-anfield" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="被称为英超联赛冠军清算日的东西变成了周日下午的漫步安菲尔德欢迎曼城进入他们的新现实，一个肮脏的地方，每一次触摸都伴随着“作弊”的呼喊，任何有利的" data-title="Manchester City shrug off chaos and controversy in public shaming at Anfield | Andy Hunter" data-date="10-12 04:02" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 04:02</span>
          <span class="news-item-title">曼城在安菲尔德的公开羞辱中摆脱混乱和争议|安迪·亨特</span>
          <span class="news-item-title-en">Manchester City shrug off chaos and controversy in public shaming at Anfield | Andy Hunter</span>
          <span class="news-value-point">💡 被称为英超联赛冠军清算日的东西变成了周日下午的漫步安菲尔德欢迎曼城进入他们的新现实，一个肮脏的地方，每一次触摸都伴随着“作弊”的呼喊，任何有利的</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/enzo-maresca-manchester-city-liverpool-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“你无法想象我有多开心……我来这里是为了赢得&#39;自从有罪判决以来，曼城在安菲尔德的第一场比赛中以3比0获胜恩佐·马雷斯卡称赞曼城在利物浦“制造自己的噪音”，因为他们忽略了周围的争议和威胁" data-title="‘We make our own noise’: Maresca hails Manchester City after Liverpool triumph" data-date="10-12 03:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 03:43</span>
          <span class="news-item-title">“我们自己制造噪音” ：马雷斯卡在利物浦胜利后称赞曼城</span>
          <span class="news-item-title-en">‘We make our own noise’: Maresca hails Manchester City after Liverpool triumph</span>
          <span class="news-value-point">💡 “你无法想象我有多开心……我来这里是为了赢得'自从有罪判决以来，曼城在安菲尔德的第一场比赛中以3比0获胜恩佐·马雷斯卡称赞曼城在利物浦“制造自己…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck5yn20wej62o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦在安菲尔德的挣扎仍在继续，因为伊拉奥拉仍在等待他在安菲尔德的第一场英超联赛胜利。" data-title="Winless and an &#39;easy touch&#39; - what&#39;s happened to the Anfield fear factor?" data-date="10-12 03:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 03:41</span>
          <span class="news-item-title">无胜利和“轻松触摸” -安菲尔德的恐惧因素发生了什么？</span>
          <span class="news-item-title-en">Winless and an 'easy touch' - what's happened to the Anfield fear factor?</span>
          <span class="news-value-point">💡 利物浦在安菲尔德的挣扎仍在继续，因为伊拉奥拉仍在等待他在安菲尔德的第一场英超联赛胜利</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/premier-league-returns-in-shadow-of-manchester-citys-judgment-day" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从俱乐部被判犯有违反财务规则的罪行以来，足球在比赛的第一个周末感觉次要Cimbri正朝着危险的南方前进，但在罗马，生活仍在继续。小行星肯定是朝这边来的，但人们去上班，吃饭，" data-title="Premier League returns in shadow of Manchester City’s judgment day | Jonathan Wilson" data-date="10-12 03:11" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 03:11</span>
          <span class="news-item-title">英超联赛在曼城审判日的阴影下回归|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Premier League returns in shadow of Manchester City’s judgment day | Jonathan Wilson</span>
          <span class="news-value-point">💡 自从俱乐部被判犯有违反财务规则的罪行以来，足球在比赛的第一个周末感觉次要Cimbri正朝着危险的南方前进，但在罗马，生活仍在继续</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c962y5nd273no?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安迪·伯纳姆（ Andy Burnham ）在曼城被判犯有与违反英超财务规则有关的所有指控后发表的言论遭到了批评。" data-title="Burnham to release details of Man City meetings" data-date="10-12 02:01" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 02:01</span>
          <span class="news-item-title">伯纳姆将公布曼城会议的细节</span>
          <span class="news-item-title-en">Burnham to release details of Man City meetings</span>
          <span class="news-value-point">💡 安迪·伯纳姆（ Andy Burnham ）在曼城被判犯有与违反英超财务规则有关的所有指控后发表的言论遭到了批评</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/11/liverpool-v-manchester-city-premier-league-live-score-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在Ryan Gravenberch的红牌之后，曼城拥抱了一种充满敌意的气氛，并让利物浦不堪重负威尔·昂温（ Will Unwin ）的更新，他是我们安菲尔德队今天比赛的一员。600多名曼城球迷组成的队伍得到了警察的护送，穿过车站" data-title="Liverpool 0-3 Manchester City: Premier League – as it happened" data-date="10-12 01:52" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:52</span>
          <span class="news-item-title">利物浦0-3曼城：英超联赛–实际情况</span>
          <span class="news-item-title-en">Liverpool 0-3 Manchester City: Premier League – as it happened</span>
          <span class="news-value-point">💡 在Ryan Gravenberch的红牌之后，曼城拥抱了一种充满敌意的气氛，并让利物浦不堪重负威尔·昂温（ Will Unwin ）的更新，他是…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/liverpool-manchester-city-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是曼城以前听过的配乐，但在比赛期间从未听过如此持续的魔咒。它来自利物浦的支持，在开球前先在安菲尔德周围响起，然后定期来。它总是" data-title="Cherki cracker caps Manchester City win at Liverpool in face of Anfield taunts" data-date="10-12 01:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:42</span>
          <span class="news-item-title">面对安菲尔德的嘲讽，切尔基·克拉克（ Cherki Cracker ）在利物浦夺冠</span>
          <span class="news-item-title-en">Cherki cracker caps Manchester City win at Liverpool in face of Anfield taunts</span>
          <span class="news-value-point">💡 这是曼城以前听过的配乐，但在比赛期间从未听过如此持续的魔咒</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck87z1jjynyqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和曼城球员在英超比赛后的评分。" data-title="Who &#39;simply has to do better&#39;? Liverpool v Man City player ratings" data-date="10-12 01:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 01:30</span>
          <span class="news-item-title">谁“只需要做得更好” ？利物浦v曼城球员评分</span>
          <span class="news-item-title-en">Who 'simply has to do better'? Liverpool v Man City player ratings</span>
          <span class="news-value-point">💡 利物浦和曼城球员在英超比赛后的评分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-12 01:26" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:26</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/tension-banners-and-inflatable-bananas-manchester-citys-welcome-to-anfield" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="热烈的气氛迎接了前英超联赛冠军的第一场比赛，因为他们被判犯有违反金融公平竞争规则的罪名在安菲尔德的街道上排成一排，为曼城队巴士的到来做准备，" data-title="Tension, ‘cheat’ banners and inflatable bananas: Manchester City’s welcome to Anfield" data-date="10-12 00:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 00:50</span>
          <span class="news-item-title">紧张气氛、“作弊”横幅和充气香蕉：曼城欢迎您来到安菲尔德</span>
          <span class="news-item-title-en">Tension, ‘cheat’ banners and inflatable bananas: Manchester City’s welcome to Anfield</span>
          <span class="news-value-point">💡 热烈的气氛迎接了前英超联赛冠军的第一场比赛，因为他们被判犯有违反金融公平竞争规则的罪名在安菲尔德的街道上排成一排，为曼城队巴士的到来做准备，</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/hull-city-everton-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从回到英超联赛以来，赫尔在MKM体育场与埃弗顿进行了一场有趣的平局，保持了他们不败的主场纪录。布伦南·约翰逊在第34分钟发现了球网，但没有得到埃弗顿的第一个英超联赛进球。" data-title="Mohamed Belloumi grabs point for Hull in seesaw draw with Everton" data-date="10-11 23:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 23:13</span>
          <span class="news-item-title">穆罕默德·贝卢米（ Mohamed Belloumi ）与埃弗顿（ Everton ）在跷跷板平局中</span>
          <span class="news-item-title-en">Mohamed Belloumi grabs point for Hull in seesaw draw with Everton</span>
          <span class="news-value-point">💡 自从回到英超联赛以来，赫尔在MKM体育场与埃弗顿进行了一场有趣的平局，保持了他们不败的主场纪录</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/938.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，泰坦军团 (TitanArmy) 今日公布了显示器新品 P279 PLUS。其基于 27&quot; 平面 Fast IPS 面板，分辨率 QHD (2560×1440)，原生刷新率 200Hz、超频刷新率 230Hz。P279 PLUS 拥有 350nits 的 SDR 全屏亮度、400nits 的 HDR 峰值亮度，静态对比度 1000:1；响应时间低至 1ms；色深 8bit + FRC，色域 99% sRGB，色偏（平均值）ΔE＜2。其支持硬件级低蓝光；提供 2 个 HDMI 2.0、1 个 DisplayPort 1.4、1 个 3.5mm 音频输出插孔；原装配备 -5°~+20° 俯仰调节支架，兼容 100×100 (mm) VESA 壁挂规范。" data-title="泰坦军团公布 P279 PLUS 显示器：QHD 230Hz Fast IPS，峰值亮度 400nits" data-date="10-12 15:57" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 15:57</span>
          <span class="news-item-title">泰坦军团公布 P279 PLUS 显示器：QHD 230Hz Fast IPS，峰值亮度 400nits</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，泰坦军团 (TitanArmy) 今日公布了显示器新品 P279 PLUS</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712076.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国天气网讯 眼下，正有一股冷空气影响我国北方，今天(10月12日)，它将给华北、东北多地带来降雨。不过降雨来去匆匆，明天将逐渐结束，但随着冷空气继续南下与暖湿气流结合，西南地区至长江中下游一带将迎较强降雨过程，局地降雨具有一定极端性。公众外出需带好雨具，谨防强降雨可能引发的滑坡、泥石流等次生灾害。" data-title="冷空气频繁来袭 南北方雨水发展 未来三天江南等局地降雨有极端性" data-date="10-12 15:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:53</span>
          <span class="news-item-title">冷空气频繁来袭 南北方雨水发展 未来三天江南等局地降雨有极端性</span>
          <span class="news-value-point">💡 中国天气网讯 眼下，正有一股冷空气影响我国北方，今天(10月12日)，它将给华北、东北多地带来降雨</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/936.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，今日宜休科技公司创始人王腾今日发文，向网友汇报了 ISHO 今日宜休最新进展。他表示，截止到目前，ISHO 今日宜休在健康科学研究、临床医学验证上，已经累计投入了上千万，远超一家初创公司在科学研究上投入的量级。关于今日宜休为何从一开始就持续与医院和科研团队合作，以及为什么愿意把大量资源投入底层科研这两个问题，王腾回复称因为想做的，不只是一个记录睡眠数据的产品，而是逐步建立一套关于睡眠、恢复与精力的科学研究体系。王腾进一步解释称，人体是一套非常复杂的系统，单一维度的数据很难完整理解一个人的疲劳与恢复状态。只有把人因、代谢、睡眠和临床医学连接起来，持续实验、采集数据、反复验证，才有可能逐步建立更科学的精力评估方法。关于何时可以买到 ISHO 今日宜休的产品，王腾" data-title="王腾称 ISHO 今日宜休在健康科学研究、临床医学验证上已累计投入上千万，今年圣诞节前能买到产品" data-date="10-12 15:48" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 15:48</span>
          <span class="news-item-title">王腾称 ISHO 今日宜休在健康科学研究、临床医学验证上已累计投入上千万，今年圣诞节前能买到产品</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，今日宜休科技公司创始人王腾今日发文，向网友汇报了 ISHO 今日宜休最新进展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712072.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网忻州10月12日电 (杨静 王春梅)秋收时节，走进位于山西省忻州市河曲县的山西晋神沙坪洗煤厂王玉庄生态复垦示范园，层层梯田错落有致，樟子松、柠条绿意盎然，土豆、花生等农作物长势喜人，西红柿、茄子等蔬菜挂满枝头。昔日尘土飞扬的矸石山，如今变成瓜果飘香、庄稼满坡的生态田园。" data-title="山西河曲：矿山复绿结硕果 生态复垦迎丰收" data-date="10-12 15:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:47</span>
          <span class="news-item-title">山西河曲：矿山复绿结硕果 生态复垦迎丰收</span>
          <span class="news-value-point">💡 中新网忻州10月12日电 (杨静 王春梅)秋收时节，走进位于山西省忻州市河曲县的山西晋神沙坪洗煤厂王玉庄生态复垦示范园，层层梯田错落有致，樟子松…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/934.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，苏宁易购宣布正式开启 2026 年度双 11 大促，推出多重补贴低至 3 折、大家电保值换新、365 天只换不修、最长 100 天价保等主题活动。苏宁易购表示，今年平台双 11 活动将从 10 月 12 日持续至 11 月 13 日。其中线上 10 月 12 日（今日）晚 8 点现货提前抢，全程覆盖 10.20 首轮放价、10.30 开门红、11.9 全民嘉年华等核心节点，并通过超级类目日、超级品牌日等主题活动持续追加新品与补贴。线下门店主打“天天都是双 11”，10.23“内购超级加补”、10.30“万店同庆全国联动”、11.6“超级爆发火力全开”等。服务层面，苏宁易购将上线大家电“保值换新”服务，消费者支付少量费用即可获得 30 天全额退货、365 天只" data-title="苏宁易购开启 2026 年度双 11 大促：提供“大家电保值换新”、“365 天只换不修”等主题活动" data-date="10-12 15:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 15:44</span>
          <span class="news-item-title">苏宁易购开启 2026 年度双 11 大促：提供“大家电保值换新”、“365 天只换不修”等主题活动</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，苏宁易购宣布正式开启 2026 年度双 11 大促，推出多重补贴低至 3 折、大家电保值换新、365 天只换不…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712037.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网成都10月12日电 (单鹏)四川省政府新闻办12日在成都举行新闻发布会，介绍大熊猫国家公园四川片区五周年建设成效。大熊猫国家公园四川管理局副局长古晓东表示，依托特有的自然景观、自然遗迹，四川片区年均生态体验超300万人次。" data-title="大熊猫国家公园四川片区：年均生态体验超300万人次" data-date="10-12 15:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 15:36</span>
          <span class="news-item-title">大熊猫国家公园四川片区：年均生态体验超300万人次</span>
          <span class="news-value-point">💡 中新网成都10月12日电 (单鹏)四川省政府新闻办12日在成都举行新闻发布会，介绍大熊猫国家公园四川片区五周年建设成效</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712020.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="总台报道有反馈丨吉林松原回应“大棚撂荒仍领补贴”：成立联合调查组开展调查" data-title="吉林松原回应“大棚撂荒仍领补贴”：成立联合调查组开展调查" data-date="10-12 14:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 14:44</span>
          <span class="news-item-title">吉林松原回应“大棚撂荒仍领补贴”：成立联合调查组开展调查</span>
          <span class="news-value-point">💡 总台报道有反馈丨吉林松原回应“大棚撂荒仍领补贴”：成立联合调查组开展调查</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/world/israel-election-india-protests-riyadh.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="许多人说，两周内的投票可能是以色列历史上最重要的事情。" data-title="An Israeli Election Like No Other" data-date="10-12 13:33" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 13:33</span>
          <span class="news-item-title">与众不同的以色列大选</span>
          <span class="news-item-title-en">An Israeli Election Like No Other</span>
          <span class="news-value-point">💡 许多人说，两周内的投票可能是以色列历史上最重要的事情</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/12/world/asia/europe-taliban-deportations-migrants.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="谴责塔利班政府人权记录的欧洲国家正在寻求其帮助，将难民遣返回阿富汗。" data-title="The Taliban Are Using Europe’s Fear of Migrants to Their Advantage" data-date="10-12 13:17" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 13:17</span>
          <span class="news-item-title">塔利班正在利用欧洲对移民的恐惧来获得优势</span>
          <span class="news-item-title-en">The Taliban Are Using Europe’s Fear of Migrants to Their Advantage</span>
          <span class="news-value-point">💡 谴责塔利班政府人权记录的欧洲国家正在寻求其帮助，将难民遣返回阿富汗</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c3vgx1jxyejyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="印度“蟑螂人民党”再次发起抗议，要求该国最高选举官员辞职，数千名抗议者被拘留。" data-title="走进印度新一轮Z世代主导的“蟑螂”抗议" data-date="10-12 12:29" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 12:29</span>
          <span class="news-item-title">走进印度新一轮Z世代主导的“蟑螂”抗议</span>
          <span class="news-value-point">💡 印度“蟑螂人民党”再次发起抗议，要求该国最高选举官员辞职，数千名抗议者被拘留</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6lyk8d5d7ygo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="五角大厦表示，胡德堡枪击案枪手纳达尔·马里克·哈桑（Nidal Malik Hasan）的处决将进行直播，但专家认为，官员可能误判了美国民意。" data-title="美国停止公开处决已近一个世纪，如今为何重启？" data-date="10-12 08:08" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 08:08</span>
          <span class="news-item-title">美国停止公开处决已近一个世纪，如今为何重启？</span>
          <span class="news-value-point">💡 五角大厦表示，胡德堡枪击案枪手纳达尔·马里克·哈桑（Nidal Malik Hasan）的处决将进行直播，但专家认为，官员可能误判了美国民意</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c63el43dw8pko/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="陷入困境的军政府正与各民族武装组织及平民抵抗力量展开一场消耗战。" data-title="缅甸年轻人的恐惧：走在街头，随时被“抓壮丁”卖给军方" data-date="10-12 08:08" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 08:08</span>
          <span class="news-item-title">缅甸年轻人的恐惧：走在街头，随时被“抓壮丁”卖给军方</span>
          <span class="news-value-point">💡 陷入困境的军政府正与各民族武装组织及平民抵抗力量展开一场消耗战</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/will-the-homeview-be-apples-first-smart-home-success/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在过去的几年里，我们已经看到多份报告称苹果正在开发一款新的智能家居产品，但现在看来该产品有一个名称和一个发布日期。" data-title="Will the HomeView be Apple’s first smart home success?" data-date="10-12 05:14" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-12 05:14</span>
          <span class="news-item-title">HomeView会是苹果智能家居的首次成功吗？</span>
          <span class="news-item-title-en">Will the HomeView be Apple’s first smart home success?</span>
          <span class="news-value-point">💡 在过去的几年里，我们已经看到多份报告称苹果正在开发一款新的智能家居产品，但现在看来该产品有一个名称和一个发布日期</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1009411/elgin-community-college-flock-safety-cameras" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2025年4月，埃尔金社区学院安装了六个Flock安全摄像头，以“加强学生的安全保障。“但到那年9月，学校管理层越来越担心Flock与海关和" data-title="A college in Illinois tried to cancel its Flock contact and it refused" data-date="10-12 04:06" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-12 04:06</span>
          <span class="news-item-title">伊利诺伊州的一所大学试图取消与Flock的联系，但它拒绝了</span>
          <span class="news-item-title-en">A college in Illinois tried to cancel its Flock contact and it refused</span>
          <span class="news-value-point">💡 2025年4月，埃尔金社区学院安装了六个Flock安全摄像头，以“加强学生的安全保障</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/48-hours-to-techcrunch-disrupt-2026-hear-directly-from-the-people-building-whats-next/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在不到48小时的时间里， TechCrunch Disrupt 2026在旧金山的Moscone West启动。在价格上涨之前，通行证最多可节省$ 100 ，第二张通行证还可享受50%的优惠。或获得其他优惠。" data-title="48 hours to TechCrunch Disrupt 2026 — hear directly from the people building what’s next" data-date="10-12 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-12 03:00</span>
          <span class="news-item-title">距离TechCrunch Disrupt 2026有48小时的路程—直接聆听开发人员的心声</span>
          <span class="news-item-title-en">48 hours to TechCrunch Disrupt 2026 — hear directly from the people building what’s next</span>
          <span class="news-value-point">💡 在不到48小时的时间里， TechCrunch Disrupt 2026在旧金山的Moscone West启动</span>
        </a>
  </div>
</div>

<script>
const NEWS_COLLAPSE_LIMIT = 10;

function applyNewsCollapse(forceExpand) {
  document.querySelectorAll('.news-category').forEach(cat => {
    const items = cat.querySelectorAll('.news-item');
    let btn = cat.querySelector('.news-expand-btn');
    if (items.length <= NEWS_COLLAPSE_LIMIT) {
      cat.removeAttribute('data-collapse');
      if (btn) btn.remove();
      return;
    }
    if (!btn) {
      btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'news-expand-btn';
      cat.appendChild(btn);
      btn.addEventListener('click', () => {
        const collapsed = cat.getAttribute('data-collapse') === '1';
        const next = collapsed ? '0' : '1';
        cat.setAttribute('data-collapse', next);
        const total = cat.querySelectorAll('.news-item').length;
        btn.textContent = next === '1'
          ? `展开其余 ${total - NEWS_COLLAPSE_LIMIT} 条（共 ${total} 条）`
          : '收起列表';
      });
    }
    if (forceExpand) {
      cat.setAttribute('data-collapse', '0');
      btn.style.display = 'none';
      btn.textContent = '收起列表';
    } else {
      if (cat.getAttribute('data-collapse') !== '0') {
        cat.setAttribute('data-collapse', '1');
      }
      btn.style.display = '';
      const total = items.length;
      const collapsed = cat.getAttribute('data-collapse') === '1';
      btn.textContent = collapsed
        ? `展开其余 ${total - NEWS_COLLAPSE_LIMIT} 条（共 ${total} 条）`
        : '收起列表';
    }
  });
}

function restoreNewsCollapse() {
  applyNewsCollapse(false);
}

function onNewsSearch(query) {
  query = (query || '').trim().toLowerCase();
  const terms = query.split(/\s+/).filter(Boolean);
  const items = document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card');
  let matched = 0;

  if (!terms.length) {
    if (typeof filterNewsChannel === 'function') {
      const activeBtn = document.querySelector('.channel-btn.active');
      const channel = activeBtn ? (activeBtn.getAttribute('onclick') || '').match(/'([^']+)'/)?.[1] || 'all' : 'all';
      filterNewsChannel(channel, activeBtn);
    } else {
      items.forEach(el => el.style.display = '');
      document.querySelectorAll('.news-category').forEach(cat => cat.style.display = '');
    }
    restoreNewsCollapse();
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  applyNewsCollapse(true);
  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'grid' : 'block') : 'none';
    if (isMatch) matched++;
  });

  document.querySelectorAll('.news-category').forEach(cat => {
    const visibleChildren = cat.querySelectorAll('.news-item:not([style*="display: none"])');
    cat.style.display = visibleChildren.length > 0 ? 'block' : 'none';
  });

  const countEl = document.getElementById('news-search-count');
  if (countEl) {
    countEl.innerText = `🔍 找到 ${matched} 条`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  applyNewsCollapse(false);
  const readKey = 'loneforme_read_news';
  let readLinks = [];
  try {
    readLinks = JSON.parse(localStorage.getItem(readKey) || '[]');
  } catch(e) {}

  document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card').forEach(el => {
    const link = el.getAttribute('href');
    if (readLinks.includes(link)) {
      el.classList.add('news-read-card');
    }
    el.addEventListener('click', () => {
      if (link && !readLinks.includes(link)) {
        readLinks.push(link);
        if (readLinks.length > 300) readLinks = readLinks.slice(-300);
        try { localStorage.setItem(readKey, JSON.stringify(readLinks)); } catch(e) {}
        el.classList.add('news-read-card');
      }
    });
  });
});
</script>
<style>
.news-read-card {
  opacity: 0.62 !important;
}
.news-read-card .news-item-title, .news-read-card .hero-featured-title, .news-read-card .hero-sub-title {
  color: var(--color-muted, #888) !important;
}
</style>


<p class="news-updated">🕐 抓取更新于 2026-10-12 16:10（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
