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
      <span>2026-09-02 20:25 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar" style="margin: 12px 0 8px; display: flex; align-items: center; gap: 8px; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.2); border-radius: 8px; padding: 7px 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity: 0.65;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)" style="flex: 1; background: transparent; border: none; outline: none; color: inherit; font-size: 13px;">
    <span id="news-search-count" style="font-size: 12px; opacity: 0.7; font-weight: 500;"></span>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">51</span>
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
        <span class="channel-count">6</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">0</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="http://www.chinanews.com.cn/tp/hd2011/2026/09-02/1202955.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="习近平同埃及总统塞西会谈" data-title="习近平同埃及总统塞西会谈" data-date="09-02 20:22" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-02 20:22</span>
      </div>
      <h2 class="hero-featured-title">习近平同埃及总统塞西会谈</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/cameras/korean-researchers-build-usd7-hidden-camera-detector-gadget-uses-led-lights-and-ai-to-separate-reflections-from-lenses" target="_blank" rel="noopener" data-cat="keji" data-summary="这个小工具只需 7 美元，但可以通过使用安装在手机上的配套 AI 应用程序来帮助您捕获隐藏的摄像机。它的工作原理是通过改变 LED 光源的位置来比较不同的反射并确定它是否是隐藏摄像头。" data-title="研究人员打造了一款售价 7 美元的智能手机夹，可以发现隐藏的摄像头——人工智能和动态 LED 网格可提供 94% 的准确度" data-date="09-02 20:20" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">研究人员打造了一款售价 7 美元的智能手机夹，可以发现隐藏的摄像头——人工智能和动态 LED 网格可提供 94% 的准确度</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/clyjmd19887o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从恩佐·费尔南德斯到马克斯森斯·拉克鲁瓦，BBC 体育频道列出了夏窗期间 20 笔最大的转会。" data-title="今夏20笔最昂贵的转会" data-date="09-02 19:59" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">今夏20笔最昂贵的转会</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/09-02/10689015.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社西藏吉隆9月2日电(记者杨守勇、格桑边觉、格桑朗杰)记者9月2日西藏自治区政府新闻办召开的新闻发布会上获悉，截至9月2日12时，灾害已致21人遇难，541人失联，发现遗物847件。" data-title="西藏吉隆泥石流灾害累计已致21人遇难541人失联" data-date="09-02 20:18" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">西藏吉隆泥石流灾害累计已致21人遇难541人失联</p>
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
        <a class="news-item" href="http://www.chinanews.com.cn/tp/hd2011/2026/09-02/1202955.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="习近平同埃及总统塞西会谈" data-title="习近平同埃及总统塞西会谈" data-date="09-02 20:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:22</span>
          <span class="news-item-title">习近平同埃及总统塞西会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-02/10689012.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月2日电 (记者 张杨彬)中央民族大学民族学与社会学学院院长关凯2日接受中新社记者采访时表示，新疆地处欧亚腹地，是东西方文明交流重要通道，多种宗教在此传播交融，形成了世界宗教史上极具特色的多元宗教交汇格局。" data-title="学者：新疆形成世界宗教史极具特色的多元交汇格局" data-date="09-02 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:15</span>
          <span class="news-item-title">学者：新疆形成世界宗教史极具特色的多元交汇格局</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/dwq/2026/09-02/10688984.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网香港9月2日电 (记者 赵静怡)“诗韵长安·对话香江”西安城市文化交流活动2日在香港举办。本次活动通过主题推介、秦腔表演、主题展览等形式，向香港呈现西安的文化底蕴与现代风貌。" data-title="“诗韵长安”走进香港   共话陕港人文交融" data-date="09-02 20:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:12</span>
          <span class="news-item-title">“诗韵长安”走进香港   共话陕港人文交融</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/cj/2026/09-02/10689006.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网海口9月2日电 (记者 符宇群)环新英湾自贸港新城是海南儋洋一体化核心区和海南自贸港“港产城科”融合发展先行区、示范区。“十五五”时期，儋州市如何统筹推进这个自贸港新城融合发展？" data-title="海南产经新观察：环新英湾自贸港新城推进“港产城科”融合发展" data-date="09-02 20:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:11</span>
          <span class="news-item-title">海南产经新观察：环新英湾自贸港新城推进“港产城科”融合发展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/cul/2026/09-02/10689005.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月2日电 (记者 张杨彬)《中国新疆地区历史》《中国新疆地区宗教史》2日在北京发布。两本新书运用考古实证、文物遗存、史料典籍、研究成果等，图文互证，阐释厘清新疆地区的历史、民族、文化、宗教情况。" data-title="详述中国新疆地区历史及宗教史的两本新书在北京发布" data-date="09-02 20:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:10</span>
          <span class="news-item-title">详述中国新疆地区历史及宗教史的两本新书在北京发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/kong/2026/09-02/10688990.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社开罗9月2日电#8195;中华人民共和国和阿拉伯埃及共和国关于进一步深化全面战略伙伴关系的联合声明" data-title="中华人民共和国和阿拉伯埃及共和国关于进一步深化全面战略伙伴关系的联合声明" data-date="09-02 19:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">中华人民共和国和阿拉伯埃及共和国关于进一步深化全面战略伙伴关系的联合声明</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/kong/2026/09-02/10688986.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="金秋启新学，奋进正当时。随着各地中小学、高校陆续开学，青春活力重回校园，广大青年学子踏上求知求索、逐梦成长的全新征程。" data-title="青春华章｜我苏青评：以科学之光，照亮开学第一课" data-date="09-02 19:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:37</span>
          <span class="news-item-title">青春华章｜我苏青评：以科学之光，照亮开学第一课</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/cul/2026/09-02/10688976.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州9月2日电 (记者 孙秋霞)第六届粤港澳大湾区文学周正在广州举行，来自国内外的知名作家、专家学者相聚一堂，围绕“APEC视野下的文学表达”主题，探索在跨文化交流新语境下，文学表达从“区域叙事”向“国际对话”的拓展路径，共答“文明互鉴”“如何共鸣”的文学之问。" data-title="中外知名作家畅谈“APEC视野下的文学表达”" data-date="09-02 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:34</span>
          <span class="news-item-title">中外知名作家畅谈“APEC视野下的文学表达”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-02/10688975.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网太原9月2日电 题：从“卖场”变“磁场” 线上阅读时代实体书店破局新路" data-title="从“卖场”变“磁场” 线上阅读时代实体书店破局新路" data-date="09-02 19:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:25</span>
          <span class="news-item-title">从“卖场”变“磁场” 线上阅读时代实体书店破局新路</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/world/middleeast/us-iran-strikes.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国军方表示，此次袭击是对最近针对美军和海上交通的袭击的报复。伊朗官员称，一场婚礼遭到袭击，平民丧生。" data-title="美国和伊朗在一夜的猛烈袭击后调查损失" data-date="09-02 18:43" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:43</span>
          <span class="news-item-title">美国和伊朗在一夜的猛烈袭击后调查损失</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/world/middleeast/iran-nuclear-program-iaea.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着战争的继续，国际原子能机构的一份内部报告称，伊朗拒绝允许其检查人员进入是一个紧迫的问题。" data-title="联合国监督机构称伊朗核计划状况尚不清楚" data-date="09-02 18:32" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:32</span>
          <span class="news-item-title">联合国监督机构称伊朗核计划状况尚不清楚</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/podcasts/the-headlines/russia-kyiv-strikes-whistleblower-warning-mail-voting.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="另外，在 91 岁时徒步旅行了 2,190 英里。" data-title="俄罗斯折磨基辅的新举措以及举报人对邮寄投票的警告" data-date="09-02 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:00</span>
          <span class="news-item-title">俄罗斯折磨基辅的新举措以及举报人对邮寄投票的警告</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/business/health-insurance-increases.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国的一项新调查预计，除非福利被削减，否则平均增幅将达到 11%，这是几十年来的最高水平。其他调查结果也预测该数字将急剧上升。" data-title="雇主健康成本预计将在 2027 年飙升" data-date="09-02 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:00</span>
          <span class="news-item-title">雇主健康成本预计将在 2027 年飙升</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/world/asia/uss-lincoln-arrives-thailand.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="数千名水手和海军陆战队员在美国服役。亚伯拉罕·林肯因在伊朗战争中的艰难部署而成为人们关注的焦点。" data-title="美国亚伯拉罕·林肯在泰国靠岸，让疲惫的船员休息一下" data-date="09-02 17:32" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 17:32</span>
          <span class="news-item-title">美国亚伯拉罕·林肯在泰国靠岸，让疲惫的船员休息一下</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/us/politics/trump-washington-renovation-projects-approval.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="最高法院为新的白宫宴会厅开了绿灯，但总统在华盛顿的其他几个项目仍然停滞不前。" data-title="谁批准了特朗普的华盛顿改造项目？" data-date="09-02 17:04" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 17:04</span>
          <span class="news-item-title">谁批准了特朗普的华盛顿改造项目？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/cameras/korean-researchers-build-usd7-hidden-camera-detector-gadget-uses-led-lights-and-ai-to-separate-reflections-from-lenses" target="_blank" rel="noopener" data-cat="keji" data-summary="这个小工具只需 7 美元，但可以通过使用安装在手机上的配套 AI 应用程序来帮助您捕获隐藏的摄像机。它的工作原理是通过改变 LED 光源的位置来比较不同的反射并确定它是否是隐藏摄像头。" data-title="研究人员打造了一款售价 7 美元的智能手机夹，可以发现隐藏的摄像头——人工智能和动态 LED 网格可提供 94% 的准确度" data-date="09-02 20:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-02 20:20</span>
          <span class="news-item-title">研究人员打造了一款售价 7 美元的智能手机夹，可以发现隐藏的摄像头——人工智能和动态 LED 网格可提供 94% 的准确度</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-02/10689016.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="国际在线专稿：8月31日至9月1日，2026年上海合作组织峰会在吉尔吉斯斯坦首都比什凯克举行。适逢上海合作组织成立25周年，多家海外主流媒体观察指出，此次峰会不仅为中国等新兴大国深化与全球南方国家的交流协作搭建了重要舞台，更以“求同存异、管控分歧”的独特实践，再次印证上合组织在复杂地缘环境下维系并拓展区域合作的制度韧性。随着合作议程从传统安全延伸至互联互通、数字经济与人工智能等新兴领域，上合组织正日益成为欧亚大陆融合发展的重要引擎。从天津到比什凯克，中国与吉尔吉斯斯坦等上合伙伴正借助这一多边平台，持续夯实伙伴关系，书写互信互利的崭新篇章。" data-title="外媒眼中的上合25年：跨越分歧的“多边样本” 全球南方的“发展引擎”" data-date="09-02 20:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:17</span>
          <span class="news-item-title">外媒眼中的上合25年：跨越分歧的“多边样本” 全球南方的“发展引擎”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/cj/2026/09-02/10689010.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京9月2日电 (记者 陈杭)“十五五”时期，北京市海淀区将形成一批具有全球技术主导权和核心竞争力的世界级产业集群，成为全球人工智能创新策源地和产业高地，预计到2030年地区生产总值在2020年基础上翻一番，年均增速5.5%，新增3到5个千亿级产业集群。" data-title="“十五五”时期北京海淀剑指全球人工智能创新策源地和产业高地" data-date="09-02 20:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:13</span>
          <span class="news-item-title">“十五五”时期北京海淀剑指全球人工智能创新策源地和产业高地</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/cj/2026/09-02/10688983.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网青冈9月2日电(姜禹帆 李梦 刘璐)初秋的松嫩平原黑土广袤、物产丰饶。作为黑龙江省农牧产业重点县域，绥化市青冈县立足黑土资源禀赋，持续深耕农牧食品全产业链，以科技赋能生产、以标准严控品质、以产业集群激活县域动能。" data-title="（活力中国调研行）黑龙江青冈：科技赋能 百亿级农牧食品产业集群加速成型" data-date="09-02 20:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:11</span>
          <span class="news-item-title">（活力中国调研行）黑龙江青冈：科技赋能 百亿级农牧食品产业集群加速成型</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/651.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，宏碁在 IFA 2026 前夕的 next@acer 年度全球记者会上一口气发布了 8 款桌面显示器产品。其中的 Predator XB253Q U1 不仅可在 FHD 分辨率下提供 1000Hz 刷新率，还支持圆偏振光护眼。Predator XB253Q U124.5&quot; IPS LCD，FHD 1000Hz，VESA DisplayHDR 400 认证。响应时间 0.3ms，峰值亮度 450nits，色域 90% DCI-P3。支持圆偏振光护眼，内置电源。Predator X32 V331.5&quot; QD-OLED Penta Tandem，UHD 180Hz，VESA DisplayHDR True Black 400 认证。SDR APL 100% 亮度 25" data-title="宏碁 IFA 2026 显示器集体上新，1000Hz + 圆偏振光护眼型号在列" data-date="09-02 20:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 20:10</span>
          <span class="news-item-title">宏碁 IFA 2026 显示器集体上新，1000Hz + 圆偏振光护眼型号在列</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/650.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="7 月 22 日，三星电子在伦敦举办 Galaxy Unpacked 2026 夏季新品发布会，正式推出了第八代折叠屏家族 ——Galaxy Z 系列，共包括三款新品：主打专业 AI 生产力的“大折叠旗舰” Galaxy Z Fold8 Ultra、主打纤薄便携与个性表达的“小折叠” Galaxy Z Flip8，以及最受瞩目的全新成员 —— 主打沉浸式内容与娱乐体验的“阔折叠” Galaxy Z Fold8。三星将经典 Fold 命名让给了阔屏形态，传统大折叠顺理成章升级为 Ultra，从产品定位来讲，也确实是名正言顺。三星首款阔折叠 Galaxy Z Fold8而作为三星的首款“阔折叠”手机，Galaxy Z Fold8 采用了 7.6 英寸 4:3 比例的内屏与 5.5 英寸外屏，展开" data-title="三星首款阔折叠 Galaxy Z Fold8 体验：更宽的屏幕，更多的可能" data-date="09-02 20:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 20:10</span>
          <span class="news-item-title">三星首款阔折叠 Galaxy Z Fold8 体验：更宽的屏幕，更多的可能</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/02/openai-faces-30-more-lawsuits-tied-to-tumbler-ridge-shooting/" target="_blank" rel="noopener" data-cat="keji" data-summary="Edelson PC正在就Tumbler Ridge枪击事件对OpenAI提起30起新的诉讼，升级了对协助、教唆和命名Chris Lehane的指控，尽管证据尚未得到证实。" data-title="OpenAI 面临 30 多起与 Tumbler Ridge 枪击事件相关的诉讼" data-date="09-02 20:09" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-02 20:09</span>
          <span class="news-item-title">OpenAI 面临 30 多起与 Tumbler Ridge 枪击事件相关的诉讼</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/649.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，ColorOS 设计总监陈希今日透露，在 ColorOS 17 上，采用全新“渐进式运动”效果，让通知与控制中心的切换更带感。当通控界面切换时，各种界面元素会随着手势滑动位置、力度与速度渐进呈现。陈希还在评论区补充，上方切换 / 下方切换，渐进运动的方向也不同。IT之家注意到，OPPO 官方今日早些时候宣布，OPPO ColorOS 17 发布暨开发者大会将于 2026 年 9 月 17 日 10:00 在珠海举行。本次大会主论坛将发布全新 ColorOS 17 操作系统，该系统将由 OPPO Find X10 系列首发搭载。ColorOS 17 设计上采用全新的“浮岛式导航”，该设计贯穿系统全局，覆盖几乎所有内置应用。系统还继承了 ColorOS 16 的流体" data-title="OPPO ColorOS 17 采用全新渐进式运动效果：通控界面切换时，界面元素随手势滑动位置、力度与速度渐进呈现" data-date="09-02 20:07" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 20:07</span>
          <span class="news-item-title">OPPO ColorOS 17 采用全新渐进式运动效果：通控界面切换时，界面元素随手势滑动位置、力度与速度渐进呈现</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/647.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，Netflix 今天（2 日）公布了《GTA 6：分量十足的一瞥》的观看数据：在截至 8 月 30 日的统计周期内获得 3110 万次观看，登上了 93 个国家和地区中的 87 个市场观看排行榜第一。视频上线 Netflix 后约 6 小时，Rockstar Games 便将其上传至 YouTube，目前该视频在 R 星官方 YouTube 频道上的观看量进一步达到 1700 万次。不过，Netflix 和 YouTube 对于观看次数的统计标准并不相同。YouTube 自 8 月 24 日起采用新的计算方式，只要用户开始播放视频一秒，就会计入一次观看。因此，即使用户只观看 10 秒后退出，也会被计算在内。Netflix 则按照总观看时长计算观看次数，即所有用户" data-title="Netflix《GTA 6：分量十足的一瞥》狂揽 3110 万次观看数，登上 87 个地区榜首" data-date="09-02 20:02" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 20:02</span>
          <span class="news-item-title">Netflix《GTA 6：分量十足的一瞥》狂揽 3110 万次观看数，登上 87 个地区榜首</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/646.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，据韩媒今天报道，Nexon 计划开发《星际争霸》系列续作。该系列游戏距离最初发售已过去近 30 年，当前仍在韩国网吧热门游戏榜保持前十排名。据匿名游戏界高层人士透露：“Nexon 与暴雪关于《星际争霸》IP 的授权合同已经接近达成。如果本次合同签订顺利，Nexon 将获得《星际争霸》续作开发权。”如果这笔交易最终达成，其规模将相当可观。作为参考，《星际争霸》上一次发售新作还是 16 年前的《星际争霸 II：自由之翼》。暴雪和 Nexon 暂未就上述传言作出回应，我们现在仍需要等待这笔交易正式公布。" data-title="消息称 Nexon 计划开发《星际争霸》新作，与暴雪的 IP 授权合同接近达成" data-date="09-02 20:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 20:01</span>
          <span class="news-item-title">消息称 Nexon 计划开发《星际争霸》新作，与暴雪的 IP 授权合同接近达成</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/987901/tesla-cybercab-launch-elon-musk-robotaxi-camera-lidar" target="_blank" rel="noopener" data-cat="keji" data-summary="不管你信不信，特斯拉 Cyber​​cab 即将到来。埃隆·马斯克首次推出金色、鸥翼门运动型、无方向盘的两座汽车作为特斯拉自动驾驶的未来，近两年后，该公司终于将其投入运营，作为德克萨斯州奥斯汀机器人出租车服务的一部分。公共游乐设施在这里，并且作为[...]" data-title="埃隆·马斯克的非正统机器人出租车理念受到考验" data-date="09-02 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-02 20:00</span>
          <span class="news-item-title">埃隆·马斯克的非正统机器人出租车理念受到考验</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/644.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，据外媒 Futurism 当地时间 1 日报道，去年 11 月，科学家曾警告，一场 20 多年来最强的“严重”太阳风暴即将袭击地球。太阳活动突然增强时，太阳会释放大量带电粒子，形成太阳风暴。这些粒子抵达地球磁层后，可以制造壮观的极光，也可能严重干扰通信卫星和无线电信号。去年 11 月的太阳风暴不仅强烈到迫使美国国家航空航天局推迟一艘火星探测器的发射，还让地面的 GPS 系统连续数小时出现严重异常。图源：Pexels发表在《地球物理研究快报》的一项新研究发现，全球导航卫星系统在这场超强太阳风暴期间出现了超过 33 英尺（10 米）的“显著定位误差”，幅度足以影响美国本土的精准农业和自动驾驶运输行业。如此明显的风险，也让研究此类太阳风暴究竟会怎样影响人类活动变得十分" data-title="研究警告：GPS 偏差 33 英尺将足以导致无人驾驶汽车发生事故" data-date="09-02 19:55" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 19:55</span>
          <span class="news-item-title">研究警告：GPS 偏差 33 英尺将足以导致无人驾驶汽车发生事故</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/643.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，宏碁现已在全球市场推出 SFF RTX Spark 迷你主机，新品采用英伟达 RTX Spark 平台，最高可选 128GB 内存。据介绍，这款产品将搭载 20 核 RTX Spark Superchip 芯片，集成 Blackwell 架构的 GPU，含有 6144 个 CUDA 核心。IT之家注意到，这款产品最高可选 128GB 统一内存，配备一个 HDMI 接口和一个 RJ45 以太网接口，以及四个 USB Type-C 接口，截至目前宏碁暂未公布这款产品的上市时间和售价。" data-title="宏碁推出 SFF RTX Spark 迷你主机，最高 128GB 内存" data-date="09-02 19:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 19:44</span>
          <span class="news-item-title">宏碁推出 SFF RTX Spark 迷你主机，最高 128GB 内存</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/642.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，月之暗面宣布，为满足大家在 Codex 和 Claude Code 中接入 Kimi API 的需求，Kimi API 现已支持 OpenAI 的 Responses API 格式，base_url 为 https://api.moonshot.cn/v1；同时支持 Anthropic 的 Messages API 格式，base_url 为 https://api.moonshot.cn/ anthropic。据IT之家了解，使用 Codex 或 Claude Code 的用户，无需转换格式或本地代理，即可通过自定义 model provider 直连 kimi-k3、kimi-k2.7-code-highspeed、kimi-k2.7-code、kimi-k" data-title="Kimi API 已原生支持 Codex 和 Claude Code" data-date="09-02 19:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 19:44</span>
          <span class="news-item-title">Kimi API 已原生支持 Codex 和 Claude Code</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/997/641.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 2 日消息，据彭博社今天（2 日）晚间报道，优步（Uber）将裁减约 3300 个岗位，相当于全球员工总数的 10%。公司将通过此次大规模重组压缩管理层级，并把更多资金转向网约车、配送和 Robotaxi 业务。优步 CEO 达拉 · 霍斯劳沙希在内部邮件中宣布了调整方案。“优步近年来不断扩张，也带来了更多层级、更多协调工作、更分散的职责归属。有些组织架构在业务规模较小时很合理，但已经不再适合我们目前的规模。”优步发言人表示，调整完成后，公司管理人员数量将减少 20%，部分管理人员会转为非管理岗位。优步没有公布管理人员中具体有多少人会被裁，非管理岗位员工同样在裁员范围内。霍斯劳沙希指出，为了让优步变得“更精简、更迅速”，公司将把仅有 1 至 2 名成员的团队数量削减近半，同" data-title="优步全球裁员 10%：为网约车、Robotaxi 业务省钱，3300 岗位受波及" data-date="09-02 19:40" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-02 19:40</span>
          <span class="news-item-title">优步全球裁员 10%：为网约车、Robotaxi 业务省钱，3300 岗位受波及</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/clyjmd19887o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从恩佐·费尔南德斯到马克斯森斯·拉克鲁瓦，BBC 体育频道列出了夏窗期间 20 笔最大的转会。" data-title="今夏20笔最昂贵的转会" data-date="09-02 19:59" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 19:59</span>
          <span class="news-item-title">今夏20笔最昂贵的转会</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/clyjmd19887o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从恩佐·费尔南德斯到马克斯森斯·拉克鲁瓦，BBC 体育频道列出了夏窗期间 20 笔最大的转会。" data-title="夏季最昂贵的20种接送服务" data-date="09-02 19:59" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 19:59</span>
          <span class="news-item-title">夏季最昂贵的20种接送服务</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-02/10688980.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新社北京9月2日电 (记者 李纯)正在泥石流灾害中方受灾区域一线的消防救援人员1日晚间接受中新社记者电话采访时表示，中方此次救援运用了“水陆空”立体搜救战术，可最大限度扩大搜寻范围，多项先进科技手段在救援中得到运用。" data-title="中国消防救援队伍“水陆空”并进扩大泥石流搜寻范围" data-date="09-02 19:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:54</span>
          <span class="news-item-title">中国消防救援队伍“水陆空”并进扩大泥石流搜寻范围</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj9x212829vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尽管人们普遍期待他们会在今年夏天签下一名左后卫，但曼联决定不这么做--这意味着什么？" data-title="曼联和他们计算的左边" data-date="09-02 18:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 18:46</span>
          <span class="news-item-title">曼联和他们计算的左边</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj9x212829vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尽管人们普遍期望他们会在今年夏天签下一名左后卫，但曼联最终决定反对——这意味着什么？" data-title="曼联和他们计算出的左翼" data-date="09-02 18:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 18:46</span>
          <span class="news-item-title">曼联和他们计算出的左翼</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx2z4q00pg7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="最终，在截止日期当天，尼克·沃尔特梅德（ Nick Woltemade ）离开纽卡斯尔联队加盟尤文图斯，俱乐部宣布马蒂亚斯·费尔南德斯-帕尔多（ Matias Fernandez-Pardo ）的到来，这是两个截然不同的前锋" data-title="Woltemade的举动凸显了纽卡斯尔夏季的变化" data-date="09-02 18:01" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 18:01</span>
          <span class="news-item-title">Woltemade的举动凸显了纽卡斯尔夏季的变化</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx2z4q00pg7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这最终是两个截然不同的前锋在截止日的故事，尼克·沃尔特马德离开纽卡斯尔联队租借加盟尤文图斯，俱乐部宣布马蒂亚斯·费尔南德斯·帕尔多的到来。" data-title="沃尔特马德的举动凸显了纽卡斯尔夏季的变化" data-date="09-02 18:01" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 18:01</span>
          <span class="news-item-title">沃尔特马德的举动凸显了纽卡斯尔夏季的变化</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx2zg85eyrqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="害怕受到攻击，但后面却很轻？利物浦在转会窗口花费了2亿多£ ，但关于球队是否有足够的深度仍然存在疑问。" data-title="害怕攻击，背后轻松-为什么利物浦的转会窗口会留下问题" data-date="09-02 17:10" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 17:10</span>
          <span class="news-item-title">害怕攻击，背后轻松-为什么利物浦的转会窗口会留下问题</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx2zg85eyrqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进攻时害怕，但后面却轻松？利物浦在转会窗口上花费了超过2亿英镑，但球队是否有足够的深度仍然存在疑问。" data-title="进攻令人畏惧，后防线光芒四射——为什么利物浦的转会窗口留下了疑问" data-date="09-02 17:10" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 17:10</span>
          <span class="news-item-title">进攻令人畏惧，后防线光芒四射——为什么利物浦的转会窗口留下了疑问</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/02/premier-league-transfer-window-club-analysis-summer-2026" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS" data-title="转会窗口裁决：每个英超俱乐部的表现如何" data-date="09-02 16:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-02 16:30</span>
          <span class="news-item-title">转会窗口裁决：每个英超俱乐部的表现如何</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/02/premier-league-transfer-window-club-analysis-summer-2026" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS" data-title="转会窗口判决：每个英超俱乐部的表现如何" data-date="09-02 16:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-02 16:30</span>
          <span class="news-item-title">转会窗口判决：每个英超俱乐部的表现如何</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c783x812dk5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳一直忙于转会市场，因为他们希望捍卫自己的英超联赛冠军，但他们还缺少一名世界级的前锋吗？" data-title="阿森纳是否会冒险不签约一个世界" data-date="09-02 15:25" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 15:25</span>
          <span class="news-item-title">阿森纳是否会冒险不签约一个世界</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c783x812dk5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳在转会市场上一直很忙碌，他们希望卫冕英超冠军，但他们还缺少一名世界级前锋吗？" data-title="阿森纳不签下世界冠军是否会冒险" data-date="09-02 15:25" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 15:25</span>
          <span class="news-item-title">阿森纳不签下世界冠军是否会冒险</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c804y5e1333o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着夏季转会窗口的关闭，首席足球作家菲尔·麦克纳尔蒂询问阿森纳的对手是否已经做了足够的努力来挑战冠军？" data-title="冠军争夺者在转会窗口中的表现是否足以挑战阿森纳？" data-date="09-02 14:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 14:12</span>
          <span class="news-item-title">冠军争夺者在转会窗口中的表现是否足以挑战阿森纳？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c804y5e1333o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着夏季转会窗口的关闭，首席足球作家菲尔·麦克纳尔蒂询问阿森纳的对手是否已经做了足够的努力来挑战冠军？" data-title="冠军争夺者在转会窗口做得足够足以挑战阿森纳吗？" data-date="09-02 14:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 14:12</span>
          <span class="news-item-title">冠军争夺者在转会窗口做得足够足以挑战阿森纳吗？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">6 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-02/10689015.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社西藏吉隆9月2日电(记者杨守勇、格桑边觉、格桑朗杰)记者9月2日西藏自治区政府新闻办召开的新闻发布会上获悉，截至9月2日12时，灾害已致21人遇难，541人失联，发现遗物847件。" data-title="西藏吉隆泥石流灾害累计已致21人遇难541人失联" data-date="09-02 20:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:18</span>
          <span class="news-item-title">西藏吉隆泥石流灾害累计已致21人遇难541人失联</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/tp/2026/09-02/10689007.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月2日，航拍镜头下的贵州省黔南布依族苗族自治州贵定县盘江镇金海坝区稻穗渐黄，与村庄、道路、河流交相辉映，构成一幅秋日丰收画卷。（无人机照片）中新社记者 瞿宏伦 摄 9月2日，航拍镜头下的贵州省黔南布依族苗族自治州贵定县盘江镇金海坝区稻穗渐黄，与村庄、道路、河流交相辉映，构成一幅秋日丰收画卷。（无人机照片）中新社记者 瞿宏伦 摄 9月2日，航拍镜头下的贵州省黔南布依族苗族自治州贵定县盘江镇金海坝区稻穗渐黄，与村庄、道路、河流交相辉映，构成一幅秋日丰收画卷。（无人机照片）中新社记者 瞿宏伦 摄 9月2日，航拍镜头下的贵州省黔南布依族苗族自治州贵定县盘江镇金海坝区稻穗渐黄，与村庄、道路、河流交相辉映，构成一幅秋日丰收画卷。（无人机照片）中新社记者 瞿宏伦 摄 9月2日，航拍镜头下的贵州省黔南布依" data-title="贵州贵定：金海坝区稻穗渐黄铺展丰收色" data-date="09-02 20:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 20:13</span>
          <span class="news-item-title">贵州贵定：金海坝区稻穗渐黄铺展丰收色</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-02/10688972.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网克拉玛依9月2日电 题：在新疆牧区，AI开始给牛羊“看”病" data-title="在新疆牧区，AI开始给牛羊“看”病" data-date="09-02 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:34</span>
          <span class="news-item-title">在新疆牧区，AI开始给牛羊“看”病</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-02/10688969.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社台北9月2日电 台湾一黄姓男子及其妻子涉嫌组织“爱情诈骗集团”，通过人工智能(AI)变声等技术行骗，犯罪所得超过9亿元新台币，受害者逾2万人。台北地方检察署2日起诉57名被告，对黄姓男子及其妻子分别求刑25年以上、18年以上。" data-title="台湾一诈骗集团利用AI变声行骗逾9亿元新台币" data-date="09-02 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:34</span>
          <span class="news-item-title">台湾一诈骗集团利用AI变声行骗逾9亿元新台币</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c4g5djd75gpo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年从巴基斯坦和伊朗遭遣返回阿富汗的人数，已再增加100万。" data-title="“我从未去过的祖国”：600万阿富汗人遭邻国驱逐，在塔利班治下重新开始" data-date="09-02 17:18" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 17:18</span>
          <span class="news-item-title">“我从未去过的祖国”：600万阿富汗人遭邻国驱逐，在塔利班治下重新开始</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cz6zpzwwxlzo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="事发河谷上游已形成两个堰塞湖。与此同时，原本散布在喜马拉雅山区的冰川湖，在灾区内有10座被标记为高风险，专家形容它们是“定时炸弹”。" data-title="尼泊尔—西藏泥石流：堰塞湖和冰湖是下一个“定时炸弹”？" data-date="09-02 08:01" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 08:01</span>
          <span class="news-item-title">尼泊尔—西藏泥石流：堰塞湖和冰湖是下一个“定时炸弹”？</span>
        </a>
  </div>
</div>

<script>
function onNewsSearch(query) {
  query = (query || '').trim().toLowerCase();
  const items = document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card');
  let matched = 0;
  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const isMatch = !query || title.includes(query) || summary.includes(query) || source.includes(query);
    el.style.display = isMatch ? '' : 'none';
    if (isMatch) matched++;
  });
  document.querySelectorAll('.news-category').forEach(cat => {
    const visibleChildren = cat.querySelectorAll('.news-item:not([style*="display: none"])');
    cat.style.display = (visibleChildren.length > 0 || !query) ? '' : 'none';
  });
  const countEl = document.getElementById('news-search-count');
  if (countEl) {
    countEl.innerText = query ? `🔍 找到 ${matched} 条` : '';
  }
}

document.addEventListener('DOMContentLoaded', () => {
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


---

<p class="news-updated">🕐 抓取更新于 2026-09-02 20:25（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
