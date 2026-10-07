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
      <span>2026-10-07 22:38 抓取更新</span>
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
        <span class="channel-count">48</span>
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
        <span class="channel-count">3</span>
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
  <div class="ov-item"><span class="ov-num">48</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×17 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-07/10708819.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月7日电 题：长征胜利90周年主题展览观展侧记：于回望中汲取前行力量" data-title="（长征胜利90周年）长征胜利90周年主题展览观展侧记：于回望中汲取前行力量" data-date="10-07 21:34" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-07 21:34</span>
      </div>
      <h2 class="hero-featured-title">（长征胜利90周年）长征胜利90周年主题展览观展侧记：于回望中汲取前行力量</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/" target="_blank" rel="noopener" data-cat="keji" data-summary="Google Labs正在开发一个名为Playground的新型人工智能游戏创建平台，供用户使用简单的文本提示构建基于浏览器的游戏。" data-title="Google experiments with an AI-powered gaming platform" data-date="10-07 22:36" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Google experiments with an AI-powered gaming platform</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c9p8gxgm71zzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰比赛中的高级人物担心曼城下赛季可能会参加冠军联赛，即使他们因违反金融法规而被降级。" data-title="Senior figures worried about Man City being in next season&#39;s Champions League" data-date="10-07 19:44" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Senior figures worried about Man City being in next season's Champions League</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1006727/apple-lg-leak-smart-home-deadbolt-lock-thermostat-temperature-sensor" target="_blank" rel="noopener" data-cat="zonghe" data-summary="继昨天彭博社报道苹果正在与LG合作开发一系列新的智能家居设备和配件之后， X上的一个名为“pdfu”的可靠泄密者透露了有关几款新产品的更多细节，包括" data-title="New leaks provide our first look at Apple and LG’s smart home devices" data-date="10-07 22:34" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">New leaks provide our first look at Apple and LG’s smart home devices</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708819.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月7日电 题：长征胜利90周年主题展览观展侧记：于回望中汲取前行力量" data-title="（长征胜利90周年）长征胜利90周年主题展览观展侧记：于回望中汲取前行力量" data-date="10-07 21:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 21:34</span>
          <span class="news-item-title">（长征胜利90周年）长征胜利90周年主题展览观展侧记：于回望中汲取前行力量</span>
          <span class="news-value-point">💡 中新社北京10月7日电 题：长征胜利90周年主题展览观展侧记：于回望中汲取前行力量</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-07/10708815.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月7日电 (记者 金旭)据韩国宇宙航空厅当地时间7日消息，韩国自主研制的运载火箭“世界”号第五次发射取得成功。此次发射搭载的5颗对地观测卫星均已与地面完成首次通信。" data-title="韩国“世界”号运载火箭第五次发射取得成功" data-date="10-07 20:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 20:59</span>
          <span class="news-item-title">韩国“世界”号运载火箭第五次发射取得成功</span>
          <span class="news-value-point">💡 中新社首尔10月7日电 (记者 金旭)据韩国宇宙航空厅当地时间7日消息，韩国自主研制的运载火箭“世界”号第五次发射取得成功</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-07/10708812.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="俄罗斯联邦消费者权益保护和公益监督局6日在其官网发布通告称，供职于该国伊尔库茨克西伯利亚与远东防鼠疫研究所的一名患病工作人员病因诊断为“不明原因肺炎”。事发后当地已第一时间采取综合防疫措施，目前伊尔库茨克州和相关城市防疫形势平稳。" data-title="俄官方称鼠疫研究机构一名员工确诊“不明原因肺炎”" data-date="10-07 20:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 20:50</span>
          <span class="news-item-title">俄官方称鼠疫研究机构一名员工确诊“不明原因肺炎”</span>
          <span class="news-value-point">💡 俄罗斯联邦消费者权益保护和公益监督局6日在其官网发布通告称，供职于该国伊尔库茨克西伯利亚与远东防鼠疫研究所的一名患病工作人员病因诊断为“不明原因…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708792.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="文化兴国运兴，文化强民族强。2023年10月，全国宣传思想文化工作会议正式提出习近平文化思想。习近平文化思想是新时代党领导文化建设实践经验的理论总结，丰富和发展了马克思主义文化理论，构成了习近平新时代中国特色社会主义思想的文化篇。" data-title="学习原声丨以文化滋养精神家园" data-date="10-07 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 20:26</span>
          <span class="news-item-title">学习原声丨以文化滋养精神家园</span>
          <span class="news-value-point">💡 文化兴国运兴，文化强民族强</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708798.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月7日电 (记者 刘文文)记者7日从中国交通运输部获悉，国庆假期(10月1日至7日)累计全社会跨区域人员流动量预计达21.44亿人次，日均3.06亿人次，同比(2025年中秋国庆假期8天日均，下同)增长0.7%。" data-title="国庆假期中国跨区域人员流动量料达21.44亿人次" data-date="10-07 20:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 20:24</span>
          <span class="news-item-title">国庆假期中国跨区域人员流动量料达21.44亿人次</span>
          <span class="news-value-point">💡 中新社北京10月7日电 (记者 刘文文)记者7日从中国交通运输部获悉，国庆假期(10月1日至7日)累计全社会跨区域人员流动量预计达21.44亿人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-07/10708780.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月7日电 斯德哥尔摩消息：瑞典皇家科学院7日宣布，将2026年诺贝尔化学奖授予法国科学家亨利·B·卡甘(Henri B. Kagan)和日本科学家硖合宪三(Kenso Soai)，以表彰他们在不对称有机合成中发现非线性效应和自催化现象。" data-title="两位科学家获得2026年诺贝尔化学奖" data-date="10-07 19:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 19:32</span>
          <span class="news-item-title">两位科学家获得2026年诺贝尔化学奖</span>
          <span class="news-value-point">💡 中新社北京10月7日电 斯德哥尔摩消息：瑞典皇家科学院7日宣布，将2026年诺贝尔化学奖授予法国科学家亨利·B·卡甘(Henri B. Kaga…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-07/10708757.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月7日电(管娜)当地时间10月7日，瑞典皇家科学院决定将2026年诺贝尔化学奖授予2名科学家。奖项授予Henri B. Kagan和Kenso Soai，以表彰他们在不对称有机合成中的非线性效应和自催化方面的发现。" data-title="2026年诺贝尔化学奖揭晓：2位科学家获奖" data-date="10-07 18:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 18:02</span>
          <span class="news-item-title">2026年诺贝尔化学奖揭晓：2位科学家获奖</span>
          <span class="news-value-point">💡 中新网10月7日电(管娜)当地时间10月7日，瑞典皇家科学院决定将2026年诺贝尔化学奖授予2名科学家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708751.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月7日，瑞典皇家科学院决定将2026年诺贝尔化学奖授予2名科学家。" data-title="2026年诺贝尔化学奖揭晓" data-date="10-07 17:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 17:50</span>
          <span class="news-item-title">2026年诺贝尔化学奖揭晓</span>
          <span class="news-value-point">💡 当地时间10月7日，瑞典皇家科学院决定将2026年诺贝尔化学奖授予2名科学家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708746.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“十五五”时期，我国将投入超过5万亿元建设新型电网。新型电网怎么建？要攻克哪些技术难题？就在几天前，一台世界最大容量的柔性直流变压器在广州城市中心就位。" data-title="大国重器就位！世界最大容量“电力心脏”有多强" data-date="10-07 17:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 17:43</span>
          <span class="news-item-title">大国重器就位！世界最大容量“电力心脏”有多强</span>
          <span class="news-value-point">💡 “十五五”时期，我国将投入超过5万亿元建设新型电网</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708738.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网三亚10月7日电 (张月和)记者从7日在三亚举行的南繁硅谷第一张生命底图——崖州湾“揭榜挂帅”联合攻关成果新闻发布会上了解到，来自崖州湾国家实验室、华大生命科学研究院等机构的12个科研团队分工协作，首次构建了覆盖水稻从种子萌发到开花结实全过程的三维时空细胞图谱，整合了基因组、细胞发育阶段与空间转录组信息，为在个体尺度上理解植物发育提供了重要基础。" data-title="中国科研团队成功绘制水稻全生命周期时空细胞图谱" data-date="10-07 17:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 17:20</span>
          <span class="news-item-title">中国科研团队成功绘制水稻全生命周期时空细胞图谱</span>
          <span class="news-value-point">💡 中新网三亚10月7日电 (张月和)记者从7日在三亚举行的南繁硅谷第一张生命底图——崖州湾“揭榜挂帅”联合攻关成果新闻发布会上了解到，来自崖州湾国…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/07/us/politics/angela-paxton-texas-senate-republican.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="安吉拉·帕克斯顿（ Angela Paxton ）敦促德克萨斯州选民支持帕克斯顿的参议院竞选活动，尽管她正在与他离婚并指责他通奸。她有自己的政治抱负。" data-title="Why Ken Paxton’s Estranged Wife Is Making the Case for His Senate Campaign" data-date="10-07 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-07 17:02</span>
          <span class="news-item-title">为什么肯·帕克斯顿的疏远妻子为他的参议院竞选辩护</span>
          <span class="news-item-title-en">Why Ken Paxton’s Estranged Wife Is Making the Case for His Senate Campaign</span>
          <span class="news-value-point">💡 安吉拉·帕克斯顿（ Angela Paxton ）敦促德克萨斯州选民支持帕克斯顿的参议院竞选活动，尽管她正在与他离婚并指责他通奸</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqdjv34xrmd3o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="乘搭火车出行的乌克兰人，愈来愈成为俄罗斯攻击的目标。" data-title="在俄罗斯无人机轰炸中，乌克兰铁路冒着恐惧匍匐前进" data-date="10-07 16:24" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-07 16:24</span>
          <span class="news-item-title">在俄罗斯无人机轰炸中，乌克兰铁路冒着恐惧匍匐前进</span>
          <span class="news-value-point">💡 乘搭火车出行的乌克兰人，愈来愈成为俄罗斯攻击的目标</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708712.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月7日电 中国外交部发言人7日宣布：俄罗斯总统助理、海事委员会主席帕特鲁舍夫将于10月8日至13日访问中国，中共中央政治局委员、中央外办主任王毅将与其会谈交流。(完)" data-title="俄罗斯总统助理、海事委员会主席帕特鲁舍夫将访华" data-date="10-07 15:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 15:47</span>
          <span class="news-item-title">俄罗斯总统助理、海事委员会主席帕特鲁舍夫将访华</span>
          <span class="news-value-point">💡 中新社北京10月7日电 中国外交部发言人7日宣布：俄罗斯总统助理、海事委员会主席帕特鲁舍夫将于10月8日至13日访问中国，中共中央政治局委员、中…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708713.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社海南三亚10月7日电 题：访中国海军遵义舰：迈向深蓝新长征" data-title="访中国海军遵义舰：迈向深蓝新长征" data-date="10-07 15:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 15:45</span>
          <span class="news-item-title">访中国海军遵义舰：迈向深蓝新长征</span>
          <span class="news-value-point">💡 中新社海南三亚10月7日电 题：访中国海军遵义舰：迈向深蓝新长征</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-07/10708702.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="外交部发言人宣布：" data-title="俄罗斯总统助理、海事委员会主席帕特鲁舍夫将访华" data-date="10-07 15:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 15:16</span>
          <span class="news-item-title">俄罗斯总统助理、海事委员会主席帕特鲁舍夫将访华</span>
          <span class="news-value-point">💡 外交部发言人宣布：</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/" target="_blank" rel="noopener" data-cat="keji" data-summary="Google Labs正在开发一个名为Playground的新型人工智能游戏创建平台，供用户使用简单的文本提示构建基于浏览器的游戏。" data-title="Google experiments with an AI-powered gaming platform" data-date="10-07 22:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-07 22:36</span>
          <span class="news-item-title">谷歌在人工智能驱动的游戏平台上进行实验</span>
          <span class="news-item-title-en">Google experiments with an AI-powered gaming platform</span>
          <span class="news-value-point">💡 Google Labs正在开发一个名为Playground的新型人工智能游戏创建平台，供用户使用简单的文本提示构建基于浏览器的游戏</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/07/openais-alexander-embiricos-is-coming-to-techcrunch-disrupt-2026-days-after-the-launch-of-dots/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI的Alexander Embiricos将在TechCrunch Disrupt 2026上登上人工智能舞台，就在Dots推出几天后。注册通行证即可加入此对话。立即获取通行证，最多可节省$ 100 ，还可享受半价优惠。" data-title="OpenAI’s Alexander Embiricos is coming to TechCrunch Disrupt 2026 — days after the launch of Dots" data-date="10-07 22:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-07 22:30</span>
          <span class="news-item-title">OpenAI的Alexander Embiricos即将加入TechCrunch Disrupt 2026--就在Dots推出几天后</span>
          <span class="news-item-title-en">OpenAI’s Alexander Embiricos is coming to TechCrunch Disrupt 2026 — days after the launch of Dots</span>
          <span class="news-value-point">💡 OpenAI的Alexander Embiricos将在TechCrunch Disrupt 2026上登上人工智能舞台，就在Dots推出几天后</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/07/get-hands-on-the-full-lineup-of-interactive-roundtables-at-techcrunch-disrupt-2026/" target="_blank" rel="noopener" data-cat="keji" data-summary="从Nvidia和Chime到Obvious Ventures和Anthropic ，在TechCrunch Disrupt 2026上探索整个圆桌会议议程。立即注册，通行证最高可节省$ 100 ，并以50%的优惠获得第二张通行证。" data-title="Get hands-on: The full lineup of interactive roundtables at TechCrunch Disrupt 2026" data-date="10-07 22:15" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-07 22:15</span>
          <span class="news-item-title">亲身体验： TechCrunch Disrupt 2026互动圆桌会议的完整阵容</span>
          <span class="news-item-title-en">Get hands-on: The full lineup of interactive roundtables at TechCrunch Disrupt 2026</span>
          <span class="news-value-point">💡 从Nvidia和Chime到Obvious Ventures和Anthropic ，在TechCrunch Disrupt 2026上探索整个圆…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/07/googles-new-synthid-website-can-identify-ai-generated-media/" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌周二推出了一个新网站，允许任何人验证一段媒体（无论是图像、视频还是音频剪辑）是否使用人工智能生成。" data-title="Google’s new SynthID website can identify AI" data-date="10-07 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-07 22:00</span>
          <span class="news-item-title">谷歌新的SynthID网站可以识别AI</span>
          <span class="news-item-title-en">Google’s new SynthID website can identify AI</span>
          <span class="news-value-point">💡 谷歌周二推出了一个新网站，允许任何人验证一段媒体（无论是图像、视频还是音频剪辑）是否使用人工智能生成</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/287.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，据科技媒体 CNBC 今天报道，芬兰许可与监督局（LVV）周二向谷歌子公司 Tuike Finland Oy 发出通知，要求其暂停穆奥斯、卡亚尼数据中心建设工作，直至完成环境影响评估。据报道，谷歌上个月才承诺在芬兰投资 150 亿美元（IT之家注：现汇率约合 1,006.79 亿元人民币），建设 AI 基础设施。LVV 表示，谷歌现已被要求暂停砍伐树木、清除表土、挖掘、采石。谷歌发言人对此表示：“我们理解当局担忧，并承认该项目没有达到自身设定的高标准。我们开展工作时遵守当地《森林法》且进行了自然环境调查。我们未来将继续在相关地区开展长期工作，确保土地能够维持生物多样性，计划在穆奥斯种植覆盖 130 公顷土地的树木。”随着人工智能热潮持续升温，芬兰已经成为各大科" data-title="谷歌在芬兰栽跟头：两座数据中心被当局勒令停工，环评成拦路虎" data-date="10-07 21:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 21:45</span>
          <span class="news-item-title">谷歌在芬兰栽跟头：两座数据中心被当局勒令停工，环评成拦路虎</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，据科技媒体 CNBC 今天报道，芬兰许可与监督局（LVV）周二向谷歌子公司 Tuike Finland Oy 发…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/286.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，华为海外 X 账号昨日发布了 9 月 29 日的国际媒体圆桌会议摘要。华为常务董事、产品投资评审委员会主任、终端 BG 董事长余承东与多家国际媒体的记者就华为消费者业务及 HarmonyOS 生态系统进行了交流。在被问及关于 AI、硬件与 EUV 的问题时，余承东表示，极紫外光刻（EUV）设备当然是制造先进芯片的关键。中国目前正在研发这些设备，但现阶段国内仍然依靠深紫外光刻（DUV）。逻辑折叠（LogicFolding）技术，是在获取某些技术受到限制的情况下，用来提升能力的一种方法。另外，手机的主处理器需要先进制程，但手机中的许多其他部件并没有那么高的制程要求。因此，华为采用系统工程的方法，持续优化整体性能，弥补无法获得更先进制程的不足。据IT之家此前报道，在" data-title="华为余承东：极紫外光刻（EUV）设备是制造先进芯片的关键，国内目前正在研发" data-date="10-07 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 21:32</span>
          <span class="news-item-title">华为余承东：极紫外光刻（EUV）设备是制造先进芯片的关键，国内目前正在研发</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，华为海外 X 账号昨日发布了 9 月 29 日的国际媒体圆桌会议摘要</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1006292/microsoft-windows-surface-event-rtx-spark-how-to-watch" target="_blank" rel="noopener" data-cat="keji" data-summary="微软今天早上将前往旧金山，揭示Windows和Surface的下一步发展，以及“关于本地人工智能将如何塑造PC下一章的对话”。“这次对话将包括微软首席执行官萨蒂亚·纳德拉，英伟达首席执行官" data-title="Windows and Surface event: how to watch and what to expect" data-date="10-07 21:12" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 21:12</span>
          <span class="news-item-title">Windows和Surface事件：如何观看和期待什么</span>
          <span class="news-item-title-en">Windows and Surface event: how to watch and what to expect</span>
          <span class="news-value-point">💡 微软今天早上将前往旧金山，揭示Windows和Surface的下一步发展，以及“关于本地人工智能将如何塑造PC下一章的对话”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/284.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，据科技媒体 TechRadar 今天报道，AMD 首席执行官苏姿丰向外界保证，公司将于 2027 年增加 AI 数据中心芯片产量。苏姿丰在中国台湾地区接受采访时表示：“随着 2026 年的推进，我们已经能确保增加供应。到 2027 年，我们将大幅增加供应。”据悉，她此次行程访问了富士康、台积电，旨在确保 AMD 能够扩大 CPU 和 GPU 产能，满足不断增长的 AI 需求。IT之家从原报道获悉，苏姿丰此番言论完全没有提到消费级产品，这对普通消费者来说并不是什么好消息。从商业利益层面来看，生产 AI 芯片的利润显然比消费级 CPU、GPU 高得多。" data-title="AMD 苏姿丰承诺 2027 年大幅增加 AI 数据中心芯片供应" data-date="10-07 21:06" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 21:06</span>
          <span class="news-item-title">AMD 苏姿丰承诺 2027 年大幅增加 AI 数据中心芯片供应</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，据科技媒体 TechRadar 今天报道，AMD 首席执行官苏姿丰向外界保证，公司将于 2027 年增加 AI …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/qualcomm-will-license-patents-behind-huaweis-logicfolding-chip-architecture-report-says-the-kirin-9050-pro-already-uses-it-with-a-teardown-showing-its-lower-die-is-mostly-cache-and-i-o" target="_blank" rel="noopener" data-cat="keji" data-summary="根据一份报告，高通公司将获得华为LogicFolding背后的专利许可，因为拆解展示了麒麟9050 Pro的两个模具。" data-title="Qualcomm will license patents behind Huawei’s LogicFolding chip architecture, report says" data-date="10-07 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-07 21:00</span>
          <span class="news-item-title">高通将授权华为LogicFolding芯片架构背后的专利，报告称</span>
          <span class="news-item-title-en">Qualcomm will license patents behind Huawei’s LogicFolding chip architecture, report says</span>
          <span class="news-value-point">💡 根据一份报告，高通公司将获得华为LogicFolding背后的专利许可，因为拆解展示了麒麟9050 Pro的两个模具</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1005726/doordash-ai-agentic-food-delivery-bites" target="_blank" rel="noopener" data-cat="keji" data-summary="领先的送餐应用DoorDash今年第二季度处理了9.7亿个订单，创造了45亿美元的收入。相比之下，一家名为Bites的10人创业公司只是一个昙花一现：它在" data-title="AI could upend food delivery" data-date="10-07 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 20:00</span>
          <span class="news-item-title">人工智能可能会颠覆送餐服务</span>
          <span class="news-item-title-en">AI could upend food delivery</span>
          <span class="news-value-point">💡 领先的送餐应用DoorDash今年第二季度处理了9.7亿个订单，创造了45亿美元的收入</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501796.html" target="_blank" rel="noopener" data-cat="keji" data-summary="晕…这年头还有说人话的AI不" data-title="晕…这年头还有说人话的AI不" data-date="10-07 16:41" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-07 16:41</span>
          <span class="news-item-title">晕…这年头还有说人话的AI不</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/218.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，华硕 (ASUS) 近日在官网上线了 NUC 14 Essential Fanless 迷你主机。这一机型是 NUC 14 Essential 的无风扇被动散热衍生型号，体积仅 0.74L。NUC 14 Essential Fanless 支持英特尔 N150 / N250 两款 TDP 为 6W 的 &quot;Twin Lake&quot; 处理器。其拥有与原版 NUC 14 Essential 相当的扩展能力，但厚度从原版的 36mm 提升至 48.2mm。该迷你主机的长宽依旧是 135×115 (mm)，提供 1 条 DDR5 SO-DIMM 插槽、1 个 M.2 2280 PCIe 盘位、1 个 M.2 2242 SATA 盘位，支持 Wi-Fi 6E &amp; 蓝牙 5.3" data-title="华硕推出 NUC 14 Essential Fanless 迷你主机：无风扇被动散热，0.74L 体积" data-date="10-07 15:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 15:39</span>
          <span class="news-item-title">华硕推出 NUC 14 Essential Fanless 迷你主机：无风扇被动散热，0.74L 体积</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，华硕 (ASUS) 近日在官网上线了 NUC 14 Essential Fanless 迷你主机</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/215.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，华为与高通 10 月 5 日宣布达成一项长期、广泛的专利许可协议，该协议包含双方在 5G、计算、人工智能、网络等多个技术领域的专利组合交叉许可，同时高通将收购华为在计算、人工智能、网络及其他技术领域的部分美国专利。随后彭博社报道称，高通公司已获得支撑华为逻辑折叠芯片制造技术的专利许可。这一消息引发网络热议。10 月 6 日，高通官网发布补充声明，回应了目前的网传消息。IT之家附官方译文如下：高通与华为达成了一项多年期、广泛的专利许可协议，涵盖双方在多个技术领域的交叉许可。协议具体条款属于保密内容，但称高通为该协议下的净支付方的相关报道并不准确。关于该协议与逻辑折叠芯片技术有关的说法也不属实。此外，高通已同意收购华为在多个技术领域的部分非蜂窝通信美国专利。" data-title="高通官网发布与华为专利许可协议补充声明：关于该协议与逻辑折叠芯片技术有关的说法不属实" data-date="10-07 15:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 15:32</span>
          <span class="news-item-title">高通官网发布与华为专利许可协议补充声明：关于该协议与逻辑折叠芯片技术有关的说法不属实</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，华为与高通 10 月 5 日宣布达成一项长期、广泛的专利许可协议，该协议包含双方在 5G、计算、人工智能、网络等…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/214.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，谷歌现已推出全新 macOS 应用 AI Edge Foresight，向苹果用户展示 EmbeddingGemma 2 端侧多模态模型的实力。这款应用可以帮助用户处理线上、线下会议笔记，支持完全离线运行。据介绍，这款应用采用 EmbeddingGemma 2 模型，它可以调用 Mac 的麦克风和系统音频，自动结合用户的笔记，整理出润色的线上、线下会议纪要。同时，这款应用还支持实时问答功能，用户可以使用会议内容和其他知识库，向 AI 询问各种问题。IT之家注意到，这款应用兼容 Apple 芯片的 Mac 计算机，用户可免费下载。参考：https://developers.google.com/edge/foresight" data-title="谷歌推出全新 macOS 应用 AI Edge Foresight，支持离线记录会议纪要" data-date="10-07 15:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 15:32</span>
          <span class="news-item-title">谷歌推出全新 macOS 应用 AI Edge Foresight，支持离线记录会议纪要</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，谷歌现已推出全新 macOS 应用 AI Edge Foresight，向苹果用户展示 EmbeddingGem…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/210.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 7 日消息，科技媒体 Wccftech 昨日（10 月 6 日）发布博文，报道称在 10 月 5 日发布的 8.40.8510 Beta 版 AIDA64 Extreme 更新中，新证据表明英特尔 Nova Lake-S 处理器采用酷睿 Ultra 4000 命名方案。在更新日志中，有一条写道：“识别英特尔酷睿 Ultra 5/7/9 4xxx 系列（又名 Nova Lake-S）”，其中系列数字采用 4xxx 表述，再次表明英特尔新系列会采用四位数。IT之家此前报道，此次出现的这些名称的数字部分均为四位数，拥有大型末级缓存 (bLLC) 的款式使用了新的“BFC”后缀。P 核E 核LP-E 核bLLC核显TDPvPRO酷睿 Ultra 9 4970K BFC8164√3" data-title="改为 4 位数：英特尔 Nova Lake-S 处理器命名添新证据，AIDA64 列出 4xxx 系列" data-date="10-07 15:13" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 15:13</span>
          <span class="news-item-title">改为 4 位数：英特尔 Nova Lake-S 处理器命名添新证据，AIDA64 列出 4xxx 系列</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，科技媒体 Wccftech 昨日（10 月 6 日）发布博文，报道称在 10 月 5 日发布的 8.40.851…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">3 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9p8gxgm71zzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰比赛中的高级人物担心曼城下赛季可能会参加冠军联赛，即使他们因违反金融法规而被降级。" data-title="Senior figures worried about Man City being in next season&#39;s Champions League" data-date="10-07 19:44" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-07 19:44</span>
          <span class="news-item-title">资深人士担心曼城进入下赛季的冠军联赛</span>
          <span class="news-item-title-en">Senior figures worried about Man City being in next season's Champions League</span>
          <span class="news-value-point">💡 英格兰比赛中的高级人物担心曼城下赛季可能会参加冠军联赛，即使他们因违反金融法规而被降级</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crz65j5p8l57o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔（ Mikel Arteta ）表示，这只是阿森纳在2030年前与英超冠军签订新合同后取得成功的“开始”。" data-title="Arteta signs new contract with champions Arsenal" data-date="10-07 19:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-07 19:00</span>
          <span class="news-item-title">阿尔特塔与阿森纳冠军签订新合同</span>
          <span class="news-item-title-en">Arteta signs new contract with champions Arsenal</span>
          <span class="news-value-point">💡 米克尔·阿尔特塔（ Mikel Arteta ）表示，这只是阿森纳在2030年前与英超冠军签订新合同后取得成功的“开始”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c623d8707k5lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="许多英超俱乐部希望曼城在未来受到追溯性惩罚和制裁。" data-title="Rival clubs want retrospective and future punishments for Man City" data-date="10-07 03:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-07 03:30</span>
          <span class="news-item-title">对手俱乐部希望对曼城进行追溯和未来的惩罚</span>
          <span class="news-item-title-en">Rival clubs want retrospective and future punishments for Man City</span>
          <span class="news-value-point">💡 许多英超俱乐部希望曼城在未来受到追溯性惩罚和制裁</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1006727/apple-lg-leak-smart-home-deadbolt-lock-thermostat-temperature-sensor" target="_blank" rel="noopener" data-cat="zonghe" data-summary="继昨天彭博社报道苹果正在与LG合作开发一系列新的智能家居设备和配件之后， X上的一个名为“pdfu”的可靠泄密者透露了有关几款新产品的更多细节，包括" data-title="New leaks provide our first look at Apple and LG’s smart home devices" data-date="10-07 22:34" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 22:34</span>
          <span class="news-item-title">新的泄漏事件让我们首次看到了苹果和LG的智能家居设备</span>
          <span class="news-item-title-en">New leaks provide our first look at Apple and LG’s smart home devices</span>
          <span class="news-value-point">💡 继昨天彭博社报道苹果正在与LG合作开发一系列新的智能家居设备和配件之后， X上的一个名为“pdfu”的可靠泄密者透露了有关几款新产品的更多细节，…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/291.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 7 日消息，《四海兄弟 2：最终版》《四海兄弟 3：最终版》PS5、XBOX Series X|S 版本已获美国 ESRB 评级，两款游戏均为 Mature 分级，适合 17 岁以上玩家。其中，《四海兄弟 2：最终版》包含强烈暴力、血腥、粗俗语言和药物使用等，《四海兄弟 3：最终版》除上述内容外还带有血液喷溅、强烈暴力、强烈性内容和药物使用等。据IT之家了解，通常情况下，一款游戏获得 ESRB 评级意味着发售日期已经临近。预计不久后的将来，我们能看到两款《四海兄弟》在主机平台官宣。作为参考，《四海兄弟 2：最终版》对原作进行了高清化，《四海兄弟 3：最终版》仅是整合了所有剧情 DLC 和奖励内容。" data-title="《四海兄弟 2》《四海兄弟 3》最终版 PS5/XBOX 平台版获 ESRB 评级，有望即将发售" data-date="10-07 22:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-07 22:25</span>
          <span class="news-item-title">《四海兄弟 2》《四海兄弟 3》最终版 PS5/XBOX 平台版获 ESRB 评级，有望即将发售</span>
          <span class="news-value-point">💡 IT之家 10 月 7 日消息，《四海兄弟 2：最终版》《四海兄弟 3：最终版》PS5、XBOX Series X|S 版本已获美国 ESRB …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/hdds/seagate-and-toshiba-battle-for-tdks-hdd-head-business-a-critical-hard-drive-component-multi-billion-dollar-deal-threatens-sole-independent-supplier-as-shortages-intensify" target="_blank" rel="noopener" data-cat="zonghe" data-summary="希捷和东芝都期待从TDK收购HDD磁头业务， TDK是唯一剩下的独立磁头供应商。" data-title="Seagate and Toshiba battle for TDK&#39;s HDD head business, a critical hard drive component" data-date="10-07 22:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-07 22:20</span>
          <span class="news-item-title">希捷和东芝争夺TDK的硬盘头业务，这是一个关键的硬盘组件</span>
          <span class="news-item-title-en">Seagate and Toshiba battle for TDK's HDD head business, a critical hard drive component</span>
          <span class="news-value-point">💡 希捷和东芝都期待从TDK收购HDD磁头业务， TDK是唯一剩下的独立磁头供应商</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-07/10708823.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月7日电 记者7日从中国公安部获悉，截至7日16时，国庆假期全国社会大局稳定、治安秩序良好，刑事、治安警情同比分别下降23.7%、7%，2700余场大型活动安全顺利，全国道路交通总体平稳有序，旅游景区秩序井然。" data-title="国庆假期中国刑事警情同比下降23.7%" data-date="10-07 22:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 22:15</span>
          <span class="news-item-title">国庆假期中国刑事警情同比下降23.7%</span>
          <span class="news-value-point">💡 中新社北京10月7日电 记者7日从中国公安部获悉，截至7日16时，国庆假期全国社会大局稳定、治安秩序良好，刑事、治安警情同比分别下降23.7%、…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501825.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="迟到25年！诺贝尔化学奖揭晓，95岁法国教授圆梦" data-title="迟到25年！诺贝尔化学奖揭晓，95岁法国教授圆梦" data-date="10-07 22:10" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-07 22:10</span>
          <span class="news-item-title">迟到25年！诺贝尔化学奖揭晓，95岁法国教授圆梦</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/07/6-days-to-techcrunch-disrupt-2026-save-on-your-pass-before-doors-open/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在6天内，来自全球创业公司和技术生态系统的1万多名员工将齐聚旧金山Moscone West ，参加TechCrunch Disrupt 2026。如果您计划成为其中一员，请不要等到机票价格上涨才登记" data-title="6 days to TechCrunch Disrupt 2026: Save on your pass before doors open" data-date="10-07 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-07 22:00</span>
          <span class="news-item-title">距离TechCrunch Disrupt 2026还有6天：开门前享受通行证优惠</span>
          <span class="news-item-title-en">6 days to TechCrunch Disrupt 2026: Save on your pass before doors open</span>
          <span class="news-value-point">💡 在6天内，来自全球创业公司和技术生态系统的1万多名员工将齐聚旧金山Moscone West ，参加TechCrunch Disrupt 2026</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1005916/amazon-ring-smart-home-lock-dial-recharge-camera-security-pricing-availability" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊宣布推出其首款智能锁，当您外出时，如果其可充电电池电量不足，则无需使用物理备用钥匙。而其他智能锁依靠隐藏的USB端口或金属触点来连接9伏电池" data-title="Ring’s first smart lock can be charged by turning a dial when the battery unexpectedly dies" data-date="10-07 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 22:00</span>
          <span class="news-item-title">Ring的第一个智能锁可以在电池意外耗尽时通过转动表盘进行充电</span>
          <span class="news-item-title-en">Ring’s first smart lock can be charged by turning a dial when the battery unexpectedly dies</span>
          <span class="news-value-point">💡 亚马逊宣布推出其首款智能锁，当您外出时，如果其可充电电池电量不足，则无需使用物理备用钥匙</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1006710/bissell-carpet-cleaning-prime-day-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="有一段时间，我用Bissell的小绿地毯清洁剂发誓。我喜欢低于100 $的价格，因为它足够小，可以放在壁橱架上，而且它可以很好地清理小杂物。但是，在您清理了足够的斑点后，" data-title="My cats hate to see this great upright carpet cleaner coming" data-date="10-07 21:55" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 21:55</span>
          <span class="news-item-title">我的猫不喜欢看到这款很棒的直立式地毯清洁剂</span>
          <span class="news-item-title-en">My cats hate to see this great upright carpet cleaner coming</span>
          <span class="news-value-point">💡 有一段时间，我用Bissell的小绿地毯清洁剂发誓</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/handheld-gaming/the-best-switch-2-accessories-on-sale-now-controllers-cameras-cases-screen-protectors-and-more" target="_blank" rel="noopener" data-cat="zonghe" data-summary="使用这些必备配件升级您的Nintendo Switch 2" data-title="The best Switch 2 accessories on sale now" data-date="10-07 21:41" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-07 21:41</span>
          <span class="news-item-title">现在销售的最好的Switch 2配件</span>
          <span class="news-item-title-en">The best Switch 2 accessories on sale now</span>
          <span class="news-value-point">💡 使用这些必备配件升级您的Nintendo Switch 2</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1006712/amazon-about-you-shopping-data" target="_blank" rel="noopener" data-cat="zonghe" data-summary="大多数人都知道，亚马逊会收集有关您的购物历史记录的数据，以提供个性化的产品推荐。但我们中的一些人没有意识到的是，你可以在你的结算中准确地检查亚马逊对你的了解-或者认为它知道什么-" data-title="Amazon uses its tracking data to guess whether shoppers have a flat butt and no friends" data-date="10-07 21:40" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 21:40</span>
          <span class="news-item-title">亚马逊使用其跟踪数据来猜测购物者是否有扁平的屁股和没有朋友</span>
          <span class="news-item-title-en">Amazon uses its tracking data to guess whether shoppers have a flat butt and no friends</span>
          <span class="news-value-point">💡 大多数人都知道，亚马逊会收集有关您的购物历史记录的数据，以提供个性化的产品推荐</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale-some-are-even-under-usd25" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从电动螺丝刀到高分辨率网络摄像头，这些都是便宜的游戏规则改变者。" data-title="These 15 under-$50 gadgets have upgraded my tech life, and they&#39;re all on sale — some are even under $25" data-date="10-07 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-07 21:20</span>
          <span class="news-item-title">这15个低于$ 50的小工具升级了我的科技生活，它们都在出售—有些甚至低于$ 25</span>
          <span class="news-item-title-en">These 15 under-$50 gadgets have upgraded my tech life, and they're all on sale — some are even under $25</span>
          <span class="news-value-point">💡 从电动螺丝刀到高分辨率网络摄像头，这些都是便宜的游戏规则改变者</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-07/10708813.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福州10月7日电(叶秋云)“自从端午后，怀人直到今，移步上楼房，隔树闹蝉声……”7日在福建福州三坊七巷历史文化街区的古厝里，闽剧经典剧目《荔枝换绛桃》选段丝竹声悠悠响起。两位演员水袖轻扬、台步缓移，闽韵乡音绕着天井飞檐，轻轻落到游客耳边。" data-title="国庆假期福建“好戏连连” 古厝街区成戏台" data-date="10-07 21:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 21:00</span>
          <span class="news-item-title">国庆假期福建“好戏连连” 古厝街区成戏台</span>
          <span class="news-value-point">💡 中新社福州10月7日电(叶秋云)“自从端午后，怀人直到今，移步上楼房，隔树闹蝉声……”7日在福建福州三坊七巷历史文化街区的古厝里，闽剧经典剧目《…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1005997/the-social-reconing-review-facebook-zuckerberg-frances-haugen" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当大卫·芬奇（ David Fincher ）的《社交网络》（ The Social Network ）于2010年首次亮相时，许多人仍然认为马克·扎克伯格（ Mark Zuckerberg ）是一位天才，他通过创建作家亚伦·索尔金（ Aaron Sorkin ）的剧本批评了扎克伯格的性格和他的车辙" data-title="The Social Reckoning is a tepid thriller that reminds us of how we got here" data-date="10-07 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-07 21:00</span>
          <span class="news-item-title">《社会清算》是一部不温不火的惊悚片，提醒我们如何来到这里</span>
          <span class="news-item-title-en">The Social Reckoning is a tepid thriller that reminds us of how we got here</span>
          <span class="news-value-point">💡 当大卫·芬奇（ David Fincher ）的《社交网络》（ The Social Network ）于2010年首次亮相时，许多人仍然认为马…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-07/10708816.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="总台报道有反馈丨三亚整治红树林保护区内涉嫌违法违规商业旅游行为" data-title="三亚整治红树林保护区内涉嫌违法违规商业旅游行为" data-date="10-07 20:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 20:56</span>
          <span class="news-item-title">三亚整治红树林保护区内涉嫌违法违规商业旅游行为</span>
          <span class="news-value-point">💡 总台报道有反馈丨三亚整治红树林保护区内涉嫌违法违规商业旅游行为</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-07/10708806.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月7日电 (记者 徐婧) 北京市公园管理中心7日介绍，今年国庆假期全市公园迎客1381.36万人次，其中，天坛公园、颐和园、朝阳公园最受游客青睐，分别接待游客103.54万人次、89.98万人次和67.58万人次。" data-title="国庆假期北京全市公园迎客超1381万人次" data-date="10-07 20:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-07 20:54</span>
          <span class="news-item-title">国庆假期北京全市公园迎客超1381万人次</span>
          <span class="news-value-point">💡 中新网北京10月7日电 (记者 徐婧) 北京市公园管理中心7日介绍，今年国庆假期全市公园迎客1381.36万人次，其中，天坛公园、颐和园、朝阳公…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-07 22:38（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
