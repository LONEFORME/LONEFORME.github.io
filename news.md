---
layout: default
title: 热点新闻
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">时政国际、AI 与芯片、足球及综合资讯</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>2026-11-27 18:13 抓取更新</span>
    </div>
  </div>
  <div class="news-search-bar">
    <svg class="news-search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="search" id="news-search-input" class="news-search-input" aria-label="搜索新闻" placeholder="搜索标题、摘要、人物或信源" oninput="onNewsSearch(this.value)">
    <span id="news-search-count" class="news-search-count"></span>
  </div>
  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">60</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">15</span>
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
  <div class="ov-item"><span class="ov-num">60</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · 天空体育×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-27/10738898.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安11月27日电 (记者 张一辰 李一璠)“近五年来，西安法院传承和发扬‘马锡五审判方式’，把‘深入群众、调查研究、巡回审判、调解优先’的优良传统，深度融入新时代家事审判实践，走实柔性解纷之路。”西安市中级人民法院党组书记、院长赵雷27日表示。" data-title="源头化解协同共治 西安法院深化家事纠纷化解体系" data-date="11-27 18:03" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-27 18:03</span>
      </div>
      <h2 class="hero-featured-title">源头化解协同共治 西安法院深化家事纠纷化解体系</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/033/624.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 27 日消息，韩媒 Economy Tribune 当地时间今日爆料称，Google（谷歌）计划为其第 10 代 TPU 芯片配备 512GB 的定制 HBM5 内存。谷歌 TPU 是当前最主要的 AI ASIC 产品，其规格可作为窥视未来 AI 芯片竞争的窗口。从各位消息人士的近期泄露来看，TPU 10 当下指的是代号 &quot;Quillfish&quot; 的项目，预计由联发科技 (MediaTek) 负责设计服务工作，有望继续采用 Intel（英特尔）的 EMIB-T 先进封装，量产时间点落在 2029 年。由于还有约 3 年的时间，一切情况都可能发生变化。谷歌近期在原版 TPU 8 系列的基础上推出 8tx、8i Max 两款芯片。此次更新并未在裸片的层面进行调整，而是通过封装集" data-title="曝谷歌第 10 代 TPU 芯片将配备 512GB 定制 HBM5 内存" data-date="11-27 17:54" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">曝谷歌第 10 代 TPU 芯片将配备 512GB 定制 HBM5 内存</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13616787/pascal-gross-and-luka-vuskovic-helping-drive-fabian-hurzelers-brighton-and-their-stunning-premier-league-start" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="It was a painful Sunday afternoon at Hull, but by the time Brighton pair Luka Vuskovic and Pascal Gross arrived at the beachside restaurant on Tuesday, you got the impression they didn&#39;t need too much of the bracing near-frozen sea air to boost the mood." data-title="Brighton&#39;s perfect blend: The duo key to Seagulls&#39; rise" data-date="11-27 18:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Brighton's perfect blend: The duo key to Seagulls' rise</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-27/10738902.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网武汉11月27日电(余哲 熊欢)到2030年，武汉市人均预期寿命达到84.2岁，居民健康素养水平达到48%，全力争创全国健康城市。武汉市政府新闻办27日召开新闻发布会，发布《武汉市卫生健康事业发展“十五五”规划》(以下简称“规划”)，明确以“实施健康优先发展战略”为核心，为群众提供均衡普惠、优质高效的卫生健康服务。" data-title="武汉预期到2030年人均寿命达84.2岁" data-date="11-27 18:08" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">武汉预期到2030年人均寿命达84.2岁</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10738898.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安11月27日电 (记者 张一辰 李一璠)“近五年来，西安法院传承和发扬‘马锡五审判方式’，把‘深入群众、调查研究、巡回审判、调解优先’的优良传统，深度融入新时代家事审判实践，走实柔性解纷之路。”西安市中级人民法院党组书记、院长赵雷27日表示。" data-title="源头化解协同共治 西安法院深化家事纠纷化解体系" data-date="11-27 18:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 18:03</span>
          <span class="news-item-title">源头化解协同共治 西安法院深化家事纠纷化解体系</span>
          <span class="news-value-point">💡 中新网西安11月27日电 (记者 张一辰 李一璠)“近五年来，西安法院传承和发扬‘马锡五审判方式’，把‘深入群众、调查研究、巡回审判、调解优先’…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10738890.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网太原11月27日电 (记者 杨杰英)一项坚持多年的“窗帘行动”，让社区老人在日常走动中自然融到一起；几部拍摄制作的网络短剧，把新的社会阶层人士的文化资源与统战工作串了起来；一场统战青年干部“传帮带”座谈交流会，围绕新时代党的统战工作交流经验、共话成长……11月24日至27日，2026年山西省委统战部学习贯彻党的二十届五中全会精神暨党务干部培训班在太原举办，学员们先后走进赛马场区域党群服务中心和太原古县城新的社会阶层人士统战工作活动站等基层实践点，看阵地、听介绍、谈体会。" data-title="“窗帘”暖民心，“短剧”聚新力——山西统战干部培训班走进实践点看“小阵地”如何“大作为”" data-date="11-27 17:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:45</span>
          <span class="news-item-title">“窗帘”暖民心，“短剧”聚新力——山西统战干部培训班走进实践点看“小阵地”如何“大作为”</span>
          <span class="news-value-point">💡 中新网太原11月27日电 (记者 杨杰英)一项坚持多年的“窗帘行动”，让社区老人在日常走动中自然融到一起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10738868.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆11月27日电 (记者 钟旖)当前，重庆市党员队伍结构呈现年轻化、专业化趋势，思想观念更加开放活跃，学习方式发生深刻变化，党员、干部思想建设面临新的情况。在此背景下，重庆如何用好党的创新理论凝心铸魂，持续引导党员群众统一思想、凝聚共识，把思想力量转化为干事创业、推动高质量发展的实际成效？" data-title="党的创新理论如何更深入人心？重庆将从三方面强化理论武装" data-date="11-27 17:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:37</span>
          <span class="news-item-title">党的创新理论如何更深入人心？重庆将从三方面强化理论武装</span>
          <span class="news-value-point">💡 中新网重庆11月27日电 (记者 钟旖)当前，重庆市党员队伍结构呈现年轻化、专业化趋势，思想观念更加开放活跃，学习方式发生深刻变化，党员、干部思…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10738880.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月27日电 据安徽省纪委监委消息：安徽省民政厅原党组成员、巡视员王佛生涉嫌严重违纪违法，目前正接受安徽省纪委监委纪律审查和监察调查。" data-title="安徽省民政厅原党组成员、巡视员王佛生接受审查调查" data-date="11-27 17:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:33</span>
          <span class="news-item-title">安徽省民政厅原党组成员、巡视员王佛生接受审查调查</span>
          <span class="news-value-point">💡 中新网11月27日电 据安徽省纪委监委消息：安徽省民政厅原党组成员、巡视员王佛生涉嫌严重违纪违法，目前正接受安徽省纪委监委纪律审查和监察调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10738878.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月27日电 据广东省纪委监委消息：广东省珠海市人大常委会原党组副书记、副主任邓群芳涉嫌严重违纪违法，主动向组织交代问题，目前正接受广东省纪委监委纪律审查和监察调查。" data-title="广东省珠海市人大常委会原副主任邓群芳接受审查调查" data-date="11-27 17:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:32</span>
          <span class="news-item-title">广东省珠海市人大常委会原副主任邓群芳接受审查调查</span>
          <span class="news-value-point">💡 中新网11月27日电 据广东省纪委监委消息：广东省珠海市人大常委会原党组副书记、副主任邓群芳涉嫌严重违纪违法，主动向组织交代问题，目前正接受广东…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738860.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社悉尼11月27日电 (记者 薄雯雯)2026第七届悉尼茶博会27日在澳大利亚悉尼开幕。展会现场，绿茶、红茶、乌龙茶等多种中国传统茶叶受到当地民众欢迎。" data-title="第七届悉尼茶博会开幕 中国茶受青睐" data-date="11-27 17:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:29</span>
          <span class="news-item-title">第七届悉尼茶博会开幕 中国茶受青睐</span>
          <span class="news-value-point">💡 中新社悉尼11月27日电 (记者 薄雯雯)2026第七届悉尼茶博会27日在澳大利亚悉尼开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738828.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="25日，神舟二十四号载人飞船成功发射。连日来，拉美多国媒体关注中国神舟二十四号载人飞船成功发射并与天宫空间站对接，以及巴基斯坦航天员首次进入中国空间站的消息。" data-title="拉美媒体积极报道中国航天国际合作成果" data-date="11-27 16:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 16:44</span>
          <span class="news-item-title">拉美媒体积极报道中国航天国际合作成果</span>
          <span class="news-value-point">💡 25日，神舟二十四号载人飞船成功发射</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738748.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社伊斯兰堡11月25日电 题：“我们为同胞进入中国空间站而自豪”——巴基斯坦各界热议中巴航天员携手赴“天宫”" data-title="“我们为同胞进入中国空间站而自豪”——巴基斯坦各界热议中巴航天员携手赴“天宫”" data-date="11-27 15:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 15:37</span>
          <span class="news-item-title">“我们为同胞进入中国空间站而自豪”——巴基斯坦各界热议中巴航天员携手赴“天宫”</span>
          <span class="news-value-point">💡 新华社伊斯兰堡11月25日电 题：“我们为同胞进入中国空间站而自豪”——巴基斯坦各界热议中巴航天员携手赴“天宫”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738727.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月27日电 (记者 孙自法 郑莹莹)由中国天文学家领衔的科研团队，最近综合利用国际积分视场光谱仪(IFS)巡天提供的恒星运动数据以及“中国天眼”(FAST)提供的星系外围气体运动数据，对近邻宇宙的136个近邻星系开展迄今规模最大的“集体称重”，系统测量了它们从中心到外围的暗物质分布。" data-title="中国天文学家领衔“集体称重”136个近邻星系 系统测量暗物质分布" data-date="11-27 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 15:30</span>
          <span class="news-item-title">中国天文学家领衔“集体称重”136个近邻星系 系统测量暗物质分布</span>
          <span class="news-value-point">💡 中新网北京11月27日电 (记者 孙自法 郑莹莹)由中国天文学家领衔的科研团队，最近综合利用国际积分视场光谱仪(IFS)巡天提供的恒星运动数据以…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738709.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网首尔11月27日电 (记者 金旭)中国驻韩国大使戴兵同30多家中韩主流媒体一线记者举行座谈。中国驻韩国大使馆公使包旭辉、中国驻韩国大使馆参赞邓明富等参加。" data-title="中国驻韩国大使馆举行中韩媒体座谈会" data-date="11-27 15:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 15:29</span>
          <span class="news-item-title">中国驻韩国大使馆举行中韩媒体座谈会</span>
          <span class="news-value-point">💡 中新网首尔11月27日电 (记者 金旭)中国驻韩国大使戴兵同30多家中韩主流媒体一线记者举行座谈</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx053e8yr348o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="台湾选举传统中，素有“决战中台湾”一称。江启臣若当选，卢路线将得到选民加持，其在国民党内的声望也有望进一步升高。" data-title="台中市选战：江启臣对决何欣纯，卢秀燕问鼎总统前哨战" data-date="11-27 13:47" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 13:47</span>
          <span class="news-item-title">台中市选战：江启臣对决何欣纯，卢秀燕问鼎总统前哨战</span>
          <span class="news-value-point">💡 台湾选举传统中，素有“决战中台湾”一称</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738473.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月26日电 (记者 欧阳开宇)当地时间11月26日，伦敦地铁司机正式启动今冬首轮24小时罢工行动。据悉，本次冬季罢工共计八日，分多时段开展，将持续至2027年2月，预计持续扰乱伦敦公共交通秩序，影响数百万通勤民众出行。" data-title="英国伦敦地铁司机开启冬季罢工" data-date="11-26 23:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 23:34</span>
          <span class="news-item-title">英国伦敦地铁司机开启冬季罢工</span>
          <span class="news-value-point">💡 中新社伦敦11月26日电 (记者 欧阳开宇)当地时间11月26日，伦敦地铁司机正式启动今冬首轮24小时罢工行动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738472.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月26日电 (记者 欧阳开宇)英国国防部26日宣布，已与本国企业巴布科克签署为期五年、总额80亿英镑的合作协议，用于升级英国海军核潜艇的维护保障体系，提升核潜艇战备水平。" data-title="英国斥资80亿英镑提升核潜艇战备水平" data-date="11-26 23:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 23:32</span>
          <span class="news-item-title">英国斥资80亿英镑提升核潜艇战备水平</span>
          <span class="news-value-point">💡 中新社伦敦11月26日电 (记者 欧阳开宇)英国国防部26日宣布，已与本国企业巴布科克签署为期五年、总额80亿英镑的合作协议，用于升级英国海军核…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/26/business/democrats-congress-agenda-taxes-spending.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Many Democratic plans are unlikely to become law under President Trump. But the party is still grappling with the difficult budget math of its agenda." data-title="Democrats Confront a Familiar Question: How Are You Going to Pay for That?" data-date="11-26 22:50" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 22:50</span>
          <span class="news-item-title">Democrats Confront a Familiar Question: How Are You Going to Pay for That?</span>
          <span class="news-value-point">💡 Many Democratic plans are unlikely to become law under President Trump. …</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738469.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="科威特军方发言人26日证实，两名意大利公民在当天伊朗无人机袭击科威特事件中受伤，后不治身亡。" data-title="两名意大利公民在伊朗无人机袭击科威特事件中身亡" data-date="11-26 22:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 22:49</span>
          <span class="news-item-title">两名意大利公民在伊朗无人机袭击科威特事件中身亡</span>
          <span class="news-value-point">💡 科威特军方发言人26日证实，两名意大利公民在当天伊朗无人机袭击科威特事件中受伤，后不治身亡</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/033/624.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 27 日消息，韩媒 Economy Tribune 当地时间今日爆料称，Google（谷歌）计划为其第 10 代 TPU 芯片配备 512GB 的定制 HBM5 内存。谷歌 TPU 是当前最主要的 AI ASIC 产品，其规格可作为窥视未来 AI 芯片竞争的窗口。从各位消息人士的近期泄露来看，TPU 10 当下指的是代号 &quot;Quillfish&quot; 的项目，预计由联发科技 (MediaTek) 负责设计服务工作，有望继续采用 Intel（英特尔）的 EMIB-T 先进封装，量产时间点落在 2029 年。由于还有约 3 年的时间，一切情况都可能发生变化。谷歌近期在原版 TPU 8 系列的基础上推出 8tx、8i Max 两款芯片。此次更新并未在裸片的层面进行调整，而是通过封装集" data-title="曝谷歌第 10 代 TPU 芯片将配备 512GB 定制 HBM5 内存" data-date="11-27 17:54" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:54</span>
          <span class="news-item-title">曝谷歌第 10 代 TPU 芯片将配备 512GB 定制 HBM5 内存</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，韩媒 Economy Tribune 当地时间今日爆料称，Google（谷歌）计划为其第 10 代 TPU 芯…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/623.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 27 日消息，长城汽车今日在广州车展发布 Hi-HEV 混动架构，官方称其为“全球首个量产大电量真智能 HEV 架构”，首搭车型魏牌高山 8 已量产落地。官方介绍称，Hi-HEV 全称为 Hyper-Intelligent HEV（超级智能 HEV），以归元全动力技术为底座，主打智慧动力、智享空间、智能安全，目标是打破 “燃油、HEV 车型与智能化无缘” 的固有认知。据官方公布信息，Hi-HEV 的电池容量比普通 HEV 高 2-3 倍，放电功率高 3.5 倍，最大放电功率超过 250kW，三擎协同下零百加速达到 5 秒级，官方称比同级 HEV 至少快 2.4 秒。官方称，该架构行业首发 AI 动力算法，可对前方 400m 路况进行实时预测，实现燃油与电能的精准分配；首搭" data-title="长城发布全球首个量产大电量真智能 HEV 架构“Hi-HEV”：电池容量翻 2-3 倍，首搭魏牌高山 8" data-date="11-27 17:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:49</span>
          <span class="news-item-title">长城发布全球首个量产大电量真智能 HEV 架构“Hi-HEV”：电池容量翻 2-3 倍，首搭魏牌高山 8</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，长城汽车今日在广州车展发布 Hi-HEV 混动架构，官方称其为“全球首个量产大电量真智能 HEV 架构”，首搭…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10738889.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社哈尔滨11月27日电 (记者 史轶夫)哈尔滨工程大学深海机器人研究院成立大会27日在哈尔滨举行。成立仪式上发布了全球首个海洋通用基座大模型“沧穹 CEORION”。" data-title="全球首个海洋通用基座大模型“沧穹 CEORION”发布" data-date="11-27 17:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:42</span>
          <span class="news-item-title">全球首个海洋通用基座大模型“沧穹 CEORION”发布</span>
          <span class="news-value-point">💡 中新社哈尔滨11月27日电 (记者 史轶夫)哈尔滨工程大学深海机器人研究院成立大会27日在哈尔滨举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/619.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 27 日消息，韩媒 MTN 近日报道称，韩国政府今年 10 月对三星电子提出要求，希望这家本土企业能开发一款可在机器人算力芯片领域与 NVIDIA（英伟达）Jetson Thor 竞争的产品，但三星电子的反应谨慎。韩国将物理 AI 视为自身国家战略的关键部分。在增强机器人整机制造能力外，实现算力基座的国产化也是韩国政府的目标之一。英伟达的 Jetson 系列平台目前是物理 AI 和机器人领域的主导方案。不过对于三星而言，这一任务并不轻松：韩国国内市场有限，如果想要在该项目盈利必须扩展全球销路；英伟达一路走来，在物理 AI 生态上具备显著的先发优势；三星电子负责芯片设计的系统 LSI 业务深陷亏损，不得不谨慎开案。参考https://news.mtn.co.kr/artic" data-title="消息称韩国政府要求三星电子开发 Jetson Thor 竞品，企业方反应谨慎" data-date="11-27 17:30" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:30</span>
          <span class="news-item-title">消息称韩国政府要求三星电子开发 Jetson Thor 竞品，企业方反应谨慎</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，韩媒 MTN 近日报道称，韩国政府今年 10 月对三星电子提出要求，希望这家本土企业能开发一款可在机器人算力芯…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq62p0n4er0wo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋戏剧性地重返英伟达执行长职位，引发亚洲股市剧烈波动，也暴露出区内经济体高度依赖AI产业及英伟达所带来的风险。" data-title="押注英伟达发展AI，亚洲在黄仁勋复职后前景如何？" data-date="11-27 15:40" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 15:40</span>
          <span class="news-item-title">押注英伟达发展AI，亚洲在黄仁勋复职后前景如何？</span>
          <span class="news-value-point">💡 黄仁勋戏剧性地重返英伟达执行长职位，引发亚洲股市剧烈波动，也暴露出区内经济体高度依赖AI产业及英伟达所带来的风险</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513305.html" target="_blank" rel="noopener" data-cat="keji" data-summary="网页App双端亮出聊天账单" data-title="DeepSeek APP突然更新账单，网友：要收费了？" data-date="11-27 15:29" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 15:29</span>
          <span class="news-item-title">DeepSeek APP突然更新账单，网友：要收费了？</span>
          <span class="news-value-point">💡 网页App双端亮出聊天账单</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513227.html" target="_blank" rel="noopener" data-cat="keji" data-summary="地图能随时修，记忆能跨任务用" data-title="刚刚，首个带跨任务空间记忆的原生基模开源！机器人端侧就能跑" data-date="11-27 15:01" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 15:01</span>
          <span class="news-item-title">刚刚，首个带跨任务空间记忆的原生基模开源！机器人端侧就能跑</span>
          <span class="news-value-point">💡 地图能随时修，记忆能跨任务用</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513194.html" target="_blank" rel="noopener" data-cat="keji" data-summary="企业需要有用的 AI" data-title="钛动科技 × 腾讯云达成战略合作，用AI打开企业全球增长新空间" data-date="11-27 12:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 12:05</span>
          <span class="news-item-title">钛动科技 × 腾讯云达成战略合作，用AI打开企业全球增长新空间</span>
          <span class="news-value-point">💡 企业需要有用的 AI</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513211.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11 月 27 日，蚂蚁灵波科技发布流式三维重建模型 LingBot-Map 2.0" data-title="蚂蚁灵波发布LingBot-Map 2.0，模型自己修正“空间记忆”，把地图画更准" data-date="11-27 12:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 12:05</span>
          <span class="news-item-title">蚂蚁灵波发布LingBot-Map 2.0，模型自己修正“空间记忆”，把地图画更准</span>
          <span class="news-value-point">💡 11 月 27 日，蚂蚁灵波科技发布流式三维重建模型 LingBot-Map 2.0</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513163.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Quickwit查询总耗时降31%，最高降87%" data-title="20个AI Agents组队，4天狂跑350次实验，超越ClickBench最佳公开成绩" data-date="11-27 11:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 11:53</span>
          <span class="news-item-title">20个AI Agents组队，4天狂跑350次实验，超越ClickBench最佳公开成绩</span>
          <span class="news-value-point">💡 Quickwit查询总耗时降31%，最高降87%</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513155.html" target="_blank" rel="noopener" data-cat="keji" data-summary="3D生成的竞争重点正在从“能看”转向“能用”" data-title="腾讯混元发布 Hy3D 3.6：高模表面更整洁、结构更清晰、刻画更细腻" data-date="11-27 11:45" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 11:45</span>
          <span class="news-item-title">腾讯混元发布 Hy3D 3.6：高模表面更整洁、结构更清晰、刻画更细腻</span>
          <span class="news-value-point">💡 3D生成的竞争重点正在从“能看”转向“能用”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513125.html" target="_blank" rel="noopener" data-cat="keji" data-summary="具身公司抱团回应：通用大模型跨维打击？没那么简单" data-title="具身公司抱团回应：通用大模型跨维打击？没那么简单" data-date="11-27 11:33" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 11:33</span>
          <span class="news-item-title">具身公司抱团回应：通用大模型跨维打击？没那么简单</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/dennys-touts-renewed-support-for-nvidia-ceo-jensen-huang-following-reinstatement-says-some-things-you-just-dont-take-off-the-menu" target="_blank" rel="noopener" data-cat="keji" data-summary="Denny&#39;s, the diner where Jensen Huang came up with the idea for Nvidia, has posted a 200-word statement to X in which it expressed its delight at his return to Nvidia after he initially resigned and admitted to an affair with a suspected Chinese spy." data-title="Denny’s touts renewed support for Nvidia CEO Jensen Huang following reinstatement" data-date="11-27 05:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 05:00</span>
          <span class="news-item-title">Denny’s touts renewed support for Nvidia CEO Jensen Huang following reinstatement</span>
          <span class="news-value-point">💡 Denny's, the diner where Jensen Huang came up with the idea for Nvidia, …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia has told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand and Indonesia as the U.S. tightens its push to keep AI chips out of China." data-title="Nvidia hits pause on chip shipments to Southeast Asia" data-date="11-27 04:03" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-27 04:03</span>
          <span class="news-item-title">Nvidia hits pause on chip shipments to Southeast Asia</span>
          <span class="news-value-point">💡 Nvidia has told manufacturing partners to pause server shipments to Mala…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/two-californian-nvidia-ai-chip-customers-are-really-chinese-owned-companies-used-as-workaround-for-government-export-controls" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia sells its advanced AI chips to two Californian companies with links to Chinese parent companies, including one that has already been blacklisted. Nvidia is only allowed to sell to specific companies, with export controls intended to prevent these chips from falling into the wrong hands in China." data-title="Two Californian Nvidia AI chip customers are really Chinese" data-date="11-27 02:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 02:00</span>
          <span class="news-item-title">Two Californian Nvidia AI chip customers are really Chinese</span>
          <span class="news-value-point">💡 Nvidia sells its advanced AI chips to two Californian companies with lin…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616787/pascal-gross-and-luka-vuskovic-helping-drive-fabian-hurzelers-brighton-and-their-stunning-premier-league-start" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="It was a painful Sunday afternoon at Hull, but by the time Brighton pair Luka Vuskovic and Pascal Gross arrived at the beachside restaurant on Tuesday, you got the impression they didn&#39;t need too much of the bracing near-frozen sea air to boost the mood." data-title="Brighton&#39;s perfect blend: The duo key to Seagulls&#39; rise" data-date="11-27 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 18:00</span>
          <span class="news-item-title">Brighton's perfect blend: The duo key to Seagulls' rise</span>
          <span class="news-value-point">💡 It was a painful Sunday afternoon at Hull, but by the time Brighton pair…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616313/why-sky-is-the-limit-for-luca-williams-barnett-as-roberto-de-zerbi-makes-lamine-yamal-comparisons" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="To earn comparisons to Lamine Yamal after just three Premier League appearances might seem a little far-fetched, but Roberto De Zerbi showed no hesitation." data-title="The English Lamine Yamal? Why Williams-Barnett is getting Spurs fans excited" data-date="11-27 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 18:00</span>
          <span class="news-item-title">The English Lamine Yamal? Why Williams-Barnett is getting Spurs fans excited</span>
          <span class="news-value-point">💡 To earn comparisons to Lamine Yamal after just three Premier League appe…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616787/pascal-gross-and-luka-vuskovic-helping-drive-fabian-hurzelers-brighton-and-their-stunning-premier-league-start" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="It was a painful Sunday afternoon at Hull, but by the time Brighton pair Luka Vuskovic and Pascal Gross arrived at the beachside restaurant on Tuesday, you got the impression they didn&#39;t need too much of the bracing near-frozen sea air to boost the mood." data-title="Brighton&#39;s perfect blend: The duo key to Seagulls&#39; rise" data-date="11-27 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 18:00</span>
          <span class="news-item-title">Brighton's perfect blend: The duo key to Seagulls' rise</span>
          <span class="news-value-point">💡 It was a painful Sunday afternoon at Hull, but by the time Brighton pair…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616882/man-utd-being-relegated-would-be-the-biggest-shock-in-history-but-it-wont-happen-says-paul-merson" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="In his latest Sky Sports column, Paul Merson previews a big weekend for Manchester United, before Arsenal take on Manchester City in a huge game live this Sunday." data-title="&#39;Man Utd being relegated would be the biggest shock in history... but it won&#39;t happen&#39;" data-date="11-27 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 17:00</span>
          <span class="news-item-title">'Man Utd being relegated would be the biggest shock in history... but it won't happen'</span>
          <span class="news-value-point">💡 In his latest Sky Sports column, Paul Merson previews a big weekend for …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616834/hull-city-should-be-in-league-one-this-season-according-to-expected-goals-so-how-do-the-tigers-keep-winning-in-the-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Hull aren&#39;t doing much wrong as a newly promoted club so far. A great start to the campaign has them middle of the Premier League table, clear of the relegation zone and unbeaten at home all season." data-title="Hull should be in League One, says xG - so how do they keep winning?" data-date="11-27 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 16:00</span>
          <span class="news-item-title">Hull should be in League One, says xG - so how do they keep winning?</span>
          <span class="news-value-point">💡 Hull aren't doing much wrong as a newly promoted club so far. A great st…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616834/hull-city-should-be-in-league-one-this-season-according-to-expected-goals-so-how-do-the-tigers-keep-winning-in-the-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Hull aren&#39;t doing much wrong as a newly promoted club so far. A great start to the campaign has them middle of the Premier League table, clear of the relegation zone and unbeaten at home all season." data-title="Hull should be in League One, says xG - so how do they keep winning?" data-date="11-27 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 16:00</span>
          <span class="news-item-title">Hull should be in League One, says xG - so how do they keep winning?</span>
          <span class="news-value-point">💡 Hull aren't doing much wrong as a newly promoted club so far. A great st…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13617029/jonny-wilkinson-showcases-nfl-skills-as-he-slots-drop-goals-with-both-feet" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Jonny Wilkinson shows off his American Football skills as he scores drop goals with his left and right foot!" data-title="Wilkinson showcases NFL skills as he slots drop goals with both feet!" data-date="11-27 06:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 06:30</span>
          <span class="news-item-title">Wilkinson showcases NFL skills as he slots drop goals with both feet!</span>
          <span class="news-value-point">💡 Jonny Wilkinson shows off his American Football skills as he scores drop…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/torreense-vs-celtic/report/577828" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Camilo Duran came off the bench to keep Celtic&#39;s Europa League hopes alive with a vital win against Torreense." data-title="Duran scores late Celtic winner to keep Europa League hopes alive" data-date="11-27 06:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 06:00</span>
          <span class="news-item-title">Duran scores late Celtic winner to keep Europa League hopes alive</span>
          <span class="news-value-point">💡 Camilo Duran came off the bench to keep Celtic's Europa League hopes ali…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/celta-vigo-vs-bournemouth/report/577814" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Bournemouth continued their magnificent run of form with a 2-1 victory against Celta Vigo, creating two bits of history in the process." data-title="Bournemouth make European history after coming from behind to beat Celta Vigo" data-date="11-27 04:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 04:00</span>
          <span class="news-item-title">Bournemouth make European history after coming from behind to beat Celta Vigo</span>
          <span class="news-value-point">💡 Bournemouth continued their magnificent run of form with a 2-1 victory a…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616785/tonda-eckert-southampton-boss-wants-to-close-the-chapter-on-spygate-ahead-of-middlesbrough-reunion" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="&quot;I think we&#39;ve experienced a little bit more in the last 12 months than normal.&quot;" data-title="Eckert: Time to &#39;close the chapter&#39; on Spygate ahead of Boro reunion" data-date="11-27 03:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 03:00</span>
          <span class="news-item-title">Eckert: Time to 'close the chapter' on Spygate ahead of Boro reunion</span>
          <span class="news-value-point">💡 "I think we've experienced a little bit more in the last 12 months than …</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx62pnz1evv4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="England international Dominic Calvert-Lewin signs a new contract to stay with Leeds United until 2029." data-title="Calvert-Lewin signs new Leeds deal until 2029" data-date="11-27 02:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 02:00</span>
          <span class="news-item-title">Calvert-Lewin signs new Leeds deal until 2029</span>
          <span class="news-value-point">💡 England international Dominic Calvert-Lewin signs a new contract to stay…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616913/dominic-calvert-lewis-leeds-striker-signs-new-deal-until-2029-with-premier-league-club" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Dominic Calvert-Lewin has signed a new deal at Leeds, keeping him at the club until the summer of 2029." data-title="Calvert-Lewin signs new Leeds deal" data-date="11-27 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 02:00</span>
          <span class="news-item-title">Calvert-Lewin signs new Leeds deal</span>
          <span class="news-value-point">💡 Dominic Calvert-Lewin has signed a new deal at Leeds, keeping him at the…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616913/dominic-calvert-lewis-leeds-striker-signs-new-deal-until-2029-with-premier-league-club" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Dominic Calvert-Lewin has signed a new deal at Leeds, keeping him at the club until the summer of 2029." data-title="Calvert-Lewin signs new Leeds deal" data-date="11-27 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 02:00</span>
          <span class="news-item-title">Calvert-Lewin signs new Leeds deal</span>
          <span class="news-value-point">💡 Dominic Calvert-Lewin has signed a new deal at Leeds, keeping him at the…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: Savio set for several weeks out" data-title="Spurs latest: Savio set for several weeks out" data-date="11-27 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 01:00</span>
          <span class="news-item-title">热刺最新消息：萨维奥将缺席数周</span>
          <span class="news-item-title-en">Spurs latest: Savio set for several weeks out</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5wy43j1l3rwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西主教练哈维·阿隆索表示，后卫韦斯利·福法纳已就其在未经俱乐部许可的情况下接受采访时发表的争议言论道歉。" data-title="Fofana has apologised for interview" data-date="11-27 00:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 00:47</span>
          <span class="news-item-title">福法纳就采访一事道歉</span>
          <span class="news-item-title-en">Fofana has apologised for interview</span>
          <span class="news-value-point">💡 切尔西主教练哈维·阿隆索表示，后卫韦斯利·福法纳已就其在未经俱乐部许可的情况下接受采访时发表的争议言论道歉</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-27/10738902.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网武汉11月27日电(余哲 熊欢)到2030年，武汉市人均预期寿命达到84.2岁，居民健康素养水平达到48%，全力争创全国健康城市。武汉市政府新闻办27日召开新闻发布会，发布《武汉市卫生健康事业发展“十五五”规划》(以下简称“规划”)，明确以“实施健康优先发展战略”为核心，为群众提供均衡普惠、优质高效的卫生健康服务。" data-title="武汉预期到2030年人均寿命达84.2岁" data-date="11-27 18:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 18:08</span>
          <span class="news-item-title">武汉预期到2030年人均寿命达84.2岁</span>
          <span class="news-value-point">💡 中新网武汉11月27日电(余哲 熊欢)到2030年，武汉市人均预期寿命达到84.2岁，居民健康素养水平达到48%，全力争创全国健康城市</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/ukrainian-11th-grader-builds-ai-powered-gps-free-drone-autopilot-to-beat-frontline-jamming-earns-the-future-of-ukraine-award-from-president-zelenskyy" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Yaroslav Sheiko&#39;s innovation allows drones to fly accurately even if they don&#39;t have a GPS signal or encounter GPS jamming." data-title="Ukrainian 11th-grader builds AI-powered, GPS-free drone autopilot to beat frontline jamming" data-date="11-27 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 18:00</span>
          <span class="news-item-title">Ukrainian 11th-grader builds AI-powered, GPS-free drone autopilot to beat frontline jamming</span>
          <span class="news-value-point">💡 Yaroslav Sheiko's innovation allows drones to fly accurately even if the…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-27/10738900.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从城市枝头的飞鸟，到近郊水库的“鸟浪”，成群候鸟成了北京冬日的限定景观，也让城市生态走进大众视野。随着能观测到的鸟类增多，越来越多市民留意到林间觅食的鸟儿，不少人会准备小米、杂粮等食物，在家中阳台或外出投喂。那么，这种方式是否会对鸟类产生影响？" data-title="面包饼干别乱喂！专家提醒：盲目投喂候鸟有害无益" data-date="11-27 17:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:59</span>
          <span class="news-item-title">面包饼干别乱喂！专家提醒：盲目投喂候鸟有害无益</span>
          <span class="news-value-point">💡 从城市枝头的飞鸟，到近郊水库的“鸟浪”，成群候鸟成了北京冬日的限定景观，也让城市生态走进大众视野</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/625.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 27 日消息，支付宝今日发布“支付宝车载助手 3.0”，官方称其为 AI 原生车载智能体，让汽车座舱从“会聊天”升级到“能办事”。IT之家从官方信息获悉，目前已有 80 多个汽车品牌与支付宝车载助手 3.0 达成定点合作，比亚迪、理想、奇瑞、神行者、东风奕派、东风风神、深蓝、北汽极狐等品牌的相关车型陆续量产交付，极氪等多个品牌将在广州车展后启动 OTA 升级。据介绍，点外卖、购电影票、加油、高速通行等服务正在进入汽车座舱。用户无需反复打开不同 App、搜索服务或手动查单，从语音提出需求到完成下单、支付，车载助手可一站式完成。官方举例称，车辆发现油量不足时会主动推荐附近加油站并联动导航；加完油后，车辆识别油枪订单，车主全程不用下车，说句话即可完成支付。想喝咖啡时，车机可结合" data-title="支付宝车载助手 3.0 与 80 多家车企达成定点合作，含比亚迪、理想、奇瑞等" data-date="11-27 17:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:56</span>
          <span class="news-item-title">支付宝车载助手 3.0 与 80 多家车企达成定点合作，含比亚迪、理想、奇瑞等</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，支付宝今日发布“支付宝车载助手 3.0”，官方称其为 AI 原生车载智能体，让汽车座舱从“会聊天”升级到“能办…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/622.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 27 日消息，荣耀终端股份有限公司 CEO 李健宣布，荣耀 700 系列今天 10:08 开售以来，销量已打破 2026 年安卓新品首销日纪录，成功登顶安卓首销排行榜第一。据IT之家此前报道，荣耀 700 系列手机于 11 月 23 日发布，包含荣耀 700S、荣耀 700、荣耀 700 Pro 三款产品，首销 3399 元起，国补到手价 2899-5099 元。荣耀 700 系列配备一块 6.57 英寸 1.5K 120Hz LTPS 绿洲护眼屏，配备 1.59 英寸 AI 灵动背屏；搭载 200Mp 1/1.56&quot; 主摄（荣耀 700 / Pro）、12Mp 超广角、50Mp 3.5X 潜望长焦（荣耀 700 / Pro）。性能方面，荣耀 700 手机搭载骁龙 8s" data-title="李健：荣耀 700 系列手机销量已打破 2026 年安卓新品首销日纪录" data-date="11-27 17:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:43</span>
          <span class="news-item-title">李健：荣耀 700 系列手机销量已打破 2026 年安卓新品首销日纪录</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，荣耀终端股份有限公司 CEO 李健宣布，荣耀 700 系列今天 10:08 开售以来，销量已打破 2026 年…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/621.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 27 日消息，据新浪汽车报道，在今日的 2026 广州车展上，广汽集团昊铂埃安 BU 副总裁杨龙表示，埃安今年的产品定义有了非常大的变化，今年 C 端（消费者端）销量占比已达 81%。杨龙表示，埃安今年针对 C 端用户需求推出了 i60、N60、Ray7 等车型，尤其 Ray7 车型发布后 35 岁以下年轻用户占比达 70%。广汽埃安今日公布最新销量数据，1-10 月累计销量 32.69 万辆同比增长 56%，预计全年零售将重回 40 万辆以上。海外市场成为其重要的增量来源。广汽埃安近期在东南亚、中亚及拉美等地区的本地化渠道布局逐步落地，出口销量的提升对整体数据起到了拉动作用。IT之家注：广汽埃安曾于 2023 年达到年销 48 万辆的高点，随后在 2024 至 2025" data-title="不只能卖网约车，广汽杨龙称埃安今年 C 端销量占比已达 81%" data-date="11-27 17:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:37</span>
          <span class="news-item-title">不只能卖网约车，广汽杨龙称埃安今年 C 端销量占比已达 81%</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，据新浪汽车报道，在今日的 2026 广州车展上，广汽集团昊铂埃安 BU 副总裁杨龙表示，埃安今年的产品定义有了…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1039190/best-black-friday-2026-deals-tech-gadgets-gift-ideas" target="_blank" rel="noopener" data-cat="zonghe" data-summary="This year’s Black Friday deals have launched in waves over the past several weeks, but now the floodgates have officially opened. You can now take advantage of the lowest prices we’ve seen in-store and online for video games, wireless earbuds, TVs, e-readers, robot vacuums, and so much more. We can’t guarantee a deal you’ve had […]" data-title="The absolute best Black Friday deals we’ve found (so far)" data-date="11-27 17:35" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 17:35</span>
          <span class="news-item-title">The absolute best Black Friday deals we’ve found (so far)</span>
          <span class="news-value-point">💡 This year’s Black Friday deals have launched in waves over the past seve…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/27/nyregion/national-weather-service-thanksgiving-storm.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="National Weather Service meteorologists keep their offices running all year, even on weekends and holidays. Here’s what was on the menu over a wet and gusty Thanksgiving." data-title="What’s on the Thanksgiving Menu for National Weather Service Meteorologists" data-date="11-27 17:34" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-27 17:34</span>
          <span class="news-item-title">What’s on the Thanksgiving Menu for National Weather Service Meteorologists</span>
          <span class="news-value-point">💡 National Weather Service meteorologists keep their offices running all y…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/620.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 27 日消息，中国铁路今日宣布，近期，徐兰高速铁路郑州至徐州段（以下简称徐兰高铁郑徐段）安全标准示范线建设工程动态检测拉通试验圆满成功，高速综合检测列车最高试验时速达 385 公里，各项设备指标表现良好。徐兰高铁郑徐段目前常态化按时速 300 公里运行，此次徐兰高铁郑徐段建成安全标准示范线后，郑州至徐州间复兴号动车组列车可常态化按时速 350 公里高标运行，将进一步释放高铁路网整体效能。徐兰高铁郑徐段是国家“八纵八横”高铁网陆桥通道的组成部分，西起郑州东站，东至徐州东站，线路全长 357 公里，横贯河南、安徽、江苏三省，衔接京沪、京广、京港高铁等多条线路，是中原地区通往长三角地区的快速客运通道，干线地位十分重要。为全面检验工程质量，11 月份以来，国铁集团组织开展了动态检" data-title="徐兰高铁郑徐段完成动态检测拉通试验，为按时速 350 公里高标运营做好准备" data-date="11-27 17:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:33</span>
          <span class="news-item-title">徐兰高铁郑徐段完成动态检测拉通试验，为按时速 350 公里高标运营做好准备</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，中国铁路今日宣布，近期，徐兰高速铁路郑州至徐州段（以下简称徐兰高铁郑徐段）安全标准示范线建设工程动态检测拉通试…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/618.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 27 日消息，苹果中国官网现已上架 mophie Frost 支架保护壳（点此访问），提供 iPhone 17e/17/18 Pro/18 Pro Max / Air 版本，定价为 398 元。系列保护壳重量约 63g，提供 4 种半透明雾面配色，自带一体式支架，同时提供了相机控制按钮和挂绳孔，IT之家附官方介绍：mophie Frost 支架保护壳以浓郁的半透明色彩，为你的 iPhone 增添别样质感。染色背板让色彩自然透出，同时柔和地散射光线；雾面外观则令日常的磨损和划痕不易显现。贴合手型的侧边设计带来稳固的握持感，出色的防摔保护可从容应对日常使用。保护壳自带一体式支架，展开后支持横屏和竖屏观看，无论是看视频、FaceTime 通话或跟着食谱做美食，都无需手持 iPh" data-title="苹果官网上架 mophie Frost 支架保护壳：适用于 iPhone 17 / 18 Pro / Air 系列机型，398 元" data-date="11-27 17:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 17:28</span>
          <span class="news-item-title">苹果官网上架 mophie Frost 支架保护壳：适用于 iPhone 17 / 18 Pro / Air 系列机型，398 元</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，苹果中国官网现已上架 mophie Frost 支架保护壳（点此访问），提供 iPhone 17e/17/18…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-27/10738855.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网苏州11月27日电 题：针尖上的“超弦”：科学大家李政道的苏绣情缘" data-title="针尖上的“超弦”：科学大家李政道的苏绣情缘" data-date="11-27 17:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:24</span>
          <span class="news-item-title">针尖上的“超弦”：科学大家李政道的苏绣情缘</span>
          <span class="news-value-point">💡 中新网苏州11月27日电 题：针尖上的“超弦”：科学大家李政道的苏绣情缘</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-27/10738851.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆11月27日电 (记者 钟旖)“作风建设只有进行时，没有完成时。”27日，重庆市纪委负责常务工作的副书记、重庆市监委副主任梅哲在当地召开的中共重庆市委六届十次全会精神解读新闻发布会上表示，为推进作风建设常态化、长效化，11月26日召开的中共重庆市委六届十次全会作出新部署，并提出了很多实招硬招。" data-title="重庆亮实招、硬招推进作风建设常态化、长效化" data-date="11-27 17:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:05</span>
          <span class="news-item-title">重庆亮实招、硬招推进作风建设常态化、长效化</span>
          <span class="news-value-point">💡 中新网重庆11月27日电 (记者 钟旖)“作风建设只有进行时，没有完成时</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-27/10738849.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口11月27日电 (记者 王晓斌)作为我国水产出口创汇的“主力军”，同时也是老百姓餐桌上极具性价比的优质蛋白，罗非鱼长期面临“墙内开花墙外香”的局面。五年前，为了打破内销无品牌的困局，海南业界将其更名为“海南鲷”。五年时间过去，这条海南鲷，还是那条罗非鱼吗？" data-title="更名“海南鲷”已逾五年，罗非鱼还是那条罗非鱼吗？" data-date="11-27 17:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:04</span>
          <span class="news-item-title">更名“海南鲷”已逾五年，罗非鱼还是那条罗非鱼吗？</span>
          <span class="news-value-point">💡 中新网海口11月27日电 (记者 王晓斌)作为我国水产出口创汇的“主力军”，同时也是老百姓餐桌上极具性价比的优质蛋白，罗非鱼长期面临“墙内开花墙…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-27/10738844.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川11月27日电 (杨迪 李琪梁)小雪已过、大雪将至，宁夏入冬后气温走低、空气干燥，呼吸道疾病、睡眠障碍、内分泌问题进入高发期。11月27日，宁夏回族自治区卫生健康委员会举办“时令节气与健康”(小雪、大雪)发布会，多位医学专家针对群众冬季养生的各类困惑答疑解惑。" data-title="供暖季寒燥多发 宁夏医学专家科普冬令养生“避坑”要点" data-date="11-27 17:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:04</span>
          <span class="news-item-title">供暖季寒燥多发 宁夏医学专家科普冬令养生“避坑”要点</span>
          <span class="news-value-point">💡 中新网银川11月27日电 (杨迪 李琪梁)小雪已过、大雪将至，宁夏入冬后气温走低、空气干燥，呼吸道疾病、睡眠障碍、内分泌问题进入高发期</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/save-a-huge-usd1-020-on-a-240hz-oled-gaming-laptop-from-lenovo-with-an-rtx-5070-ti-now-just-usd1-999-portable-legion-5i-rig-features-an-18-core-intel-cpu-and-a-1tb-ssd" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Grab a 16-inch OLED gaming laptop with an RTX 5070 Ti from Lenovo for just $1,999.99 right now." data-title="Save a huge $1,020 on a 240Hz OLED gaming laptop from Lenovo with an RTX 5070 Ti, now just $1,999" data-date="11-27 16:49" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 16:49</span>
          <span class="news-item-title">Save a huge $1,020 on a 240Hz OLED gaming laptop from Lenovo with an RTX 5070 Ti, now just $1,999</span>
          <span class="news-value-point">💡 Grab a 16-inch OLED gaming laptop with an RTX 5070 Ti from Lenovo for ju…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-27 18:13（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
