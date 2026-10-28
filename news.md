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
      <span>2026-10-29 02:24 抓取更新</span>
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
        <span class="channel-count">59</span>
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
        <span class="channel-count">14</span>
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
  <div class="ov-item"><span class="ov-num">59</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×11 · 天空体育×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/28/world/americas/flavio-bolsonaro-us-miami-brazil-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="博尔索纳罗在周日的总统选举中失利，在警方因调查而取消了他的护照后，他逃离巴西，通过阿根廷前往美国。" data-title="Flávio Bolsonaro Lands in Miami After Fleeing Brazil" data-date="10-29 01:56" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-29 01:56</span>
      </div>
      <h2 class="hero-featured-title">Flávio Bolsonaro逃离巴西后登陆迈阿密</h2>
      <div class="hero-featured-title-en">Flávio Bolsonaro Lands in Miami After Fleeing Brazil</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/019/246.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，苹果今天（10 月 29 日）正式公布配备 512GB 统一内存的 Mac Studio 售价。该配置仅面向搭载 M5 Ultra 芯片（ 36 核 CPU 与 80 核 GPU）的顶配机型，相比较 96GB 版本价格上涨 116,250 元。IT之家注：512GB 内存版目前仅适用于 M5 Ultra 芯片（36 核 CPU 与 80 核 GPU）顶配，用户如果选择 M5 Ultra（30 核 CPU 与 64 核 GPU）会跳出相关提示：在内存配置选项，苹果 Mac Studio 从 96GB 升级到 512GB 需要加价 116,250 元人民币。在存储搭配方面，如果用户选择 M5 Ultra 芯片 + 512GB 内存 +1TB 存储，售价为 172" data-title="苹果上架 512GB 内存版 Mac Studio：较 96GB 配置贵 116250 元" data-date="10-29 01:54" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">苹果上架 512GB 内存版 Mac Studio：较 96GB 配置贵 116250 元</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/liverpool-vs-chelsea/live/578612" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool vs Chelsea LIVE!" data-title="Liverpool vs Chelsea LIVE!" data-date="10-29 01:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Liverpool vs Chelsea LIVE!</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/019/249.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果今日推出首款触控屏 MacBook Pro，定价 22,999 元起。该产品采用双层串联 OLED 面板，HDR 峰值亮度可达 2,000 nits。如今苹果已经公布了这款 MacBook Pro 的第三方应用触控适配情况，IT之家附未来支持名单如下：办公与协作： Notion、Canva、Zoom、Microsoft Word、Excel、PowerPoint、Outlook（Microsoft Office）照片与视频： Adobe Lightroom、DaVinci Resolve3D 与动画： Blender、Maxon Cinema 4D、Maxon ZBrush、Shapr3D音乐： Algoriddim djay Pro需要注意的是，上述应" data-title="苹果触屏 MacBook Pro 应用适配情况：Lightroom、达芬奇、C4D、Office 等今年晚些时候支持" data-date="10-29 02:24" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">苹果触屏 MacBook Pro 应用适配情况：Lightroom、达芬奇、C4D、Office 等今年晚些时候支持</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/world/americas/flavio-bolsonaro-us-miami-brazil-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="博尔索纳罗在周日的总统选举中失利，在警方因调查而取消了他的护照后，他逃离巴西，通过阿根廷前往美国。" data-title="Flávio Bolsonaro Lands in Miami After Fleeing Brazil" data-date="10-29 01:56" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 01:56</span>
          <span class="news-item-title">Flávio Bolsonaro逃离巴西后登陆迈阿密</span>
          <span class="news-item-title-en">Flávio Bolsonaro Lands in Miami After Fleeing Brazil</span>
          <span class="news-value-point">💡 博尔索纳罗在周日的总统选举中失利，在警方因调查而取消了他的护照后，他逃离巴西，通过阿根廷前往美国</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/26/world/americas/brazil-election-lula-win-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="路易斯·伊纳西奥·卢拉·达席尔瓦总统的连任结束了拉丁美洲右翼候选人的一系列胜利。他的对手弗拉维奥·博尔索纳罗（ Flávio Bolsonaro ）逃离巴西前往美国。" data-title="What to Know About Brazil’s Election and Flávio Bolsonaro’s Departure" data-date="10-29 01:31" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 01:31</span>
          <span class="news-item-title">巴西大选和弗拉维奥·博尔索纳罗离境须知</span>
          <span class="news-item-title-en">What to Know About Brazil’s Election and Flávio Bolsonaro’s Departure</span>
          <span class="news-value-point">💡 路易斯·伊纳西奥·卢拉·达席尔瓦总统的连任结束了拉丁美洲右翼候选人的一系列胜利</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-28/10722487.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月28日，西班牙首相桑切斯宣布，自29日起全国哀悼三天，悼念列车相撞事故遇难者。" data-title="西班牙首相宣布为列车相撞事故遇难者全国哀悼三天" data-date="10-28 23:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 23:26</span>
          <span class="news-item-title">西班牙首相宣布为列车相撞事故遇难者全国哀悼三天</span>
          <span class="news-value-point">💡 当地时间10月28日，西班牙首相桑切斯宣布，自29日起全国哀悼三天，悼念列车相撞事故遇难者</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-28/10722486.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据西班牙卡斯蒂利亚-拉曼查自治区方面28日消息，当天上午在其首府托莱多发生的高速铁路列车相撞事故死亡人数上升至68人。" data-title="西班牙列车相撞事故死亡人数上升至68人" data-date="10-28 22:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 22:59</span>
          <span class="news-item-title">西班牙列车相撞事故死亡人数上升至68人</span>
          <span class="news-value-point">💡 据西班牙卡斯蒂利亚-拉曼查自治区方面28日消息，当天上午在其首府托莱多发生的高速铁路列车相撞事故死亡人数上升至68人</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq2038dd7pzxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="刘延东的逝世提醒外界一个现象：从吴仪、刘延东到孙春兰，中共中央政治局曾连续20年保持至少一名女性委员，直到2022年“二十大”中断，权力核心再无女性。" data-title="刘延东逝世：“红二代”“团派”背景，政治局里少见的女性身影" data-date="10-28 22:51" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 22:51</span>
          <span class="news-item-title">刘延东逝世：“红二代”“团派”背景，政治局里少见的女性身影</span>
          <span class="news-value-point">💡 刘延东的逝世提醒外界一个现象：从吴仪、刘延东到孙春兰，中共中央政治局曾连续20年保持至少一名女性委员，直到2022年“二十大”中断，权力核心再无…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722485.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="退役军人事务部28日在北京举行褒扬纪念工作专题新闻发布会。据该部褒扬纪念司(国际合作司)副司长史艺介绍，今年又有8位已迎回在韩中国人民志愿军烈士确认身份。在目前已迎回的十三批在韩志愿军烈士中，已有44名烈士确认身份、找到亲人。" data-title="又有8位已迎回在韩志愿军烈士确认身份！为烈士寻亲，如何寻？难在哪？怎么解？" data-date="10-28 22:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 22:43</span>
          <span class="news-item-title">又有8位已迎回在韩志愿军烈士确认身份！为烈士寻亲，如何寻？难在哪？怎么解？</span>
          <span class="news-value-point">💡 退役军人事务部28日在北京举行褒扬纪念工作专题新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/us/politics/alaska-dan-sullivan-conspiracy-peltola.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="与民主党参议院候选人玛丽·佩尔托拉（ Mary Peltola ）结盟的特工花了数月时间招募候选人，剥夺共和党参议员丹·沙利文（ Dan Sullivan ）的选票。" data-title="Inside Democrats’ Secret Effort to Stack Alaska’s Midterm Ballot With Another Dan Sullivan" data-date="10-28 22:37" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 22:37</span>
          <span class="news-item-title">民主党秘密努力将阿拉斯加的中期投票与另一位丹·沙利文（ Dan Sullivan ）</span>
          <span class="news-item-title-en">Inside Democrats’ Secret Effort to Stack Alaska’s Midterm Ballot With Another Dan Sullivan</span>
          <span class="news-value-point">💡 与民主党参议院候选人玛丽·佩尔托拉（ Mary Peltola ）结盟的特工花了数月时间招募候选人，剥夺共和党参议员丹·沙利文（ Dan Sul…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722477.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网昆明10月28日电 (罗婕)28日，《云南省铁路安全管理条例》(下称《条例》)新闻发布会在昆明市举行。记者从会上获悉，《条例》结合云南区位特点，明确开展跨境铁路安全交流合作，与毗邻国家共同维护跨境铁路安全环境和秩序等内容。" data-title="云南立法保护铁路安全 纳入跨境协作内容" data-date="10-28 22:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 22:18</span>
          <span class="news-item-title">云南立法保护铁路安全 纳入跨境协作内容</span>
          <span class="news-value-point">💡 中新网昆明10月28日电 (罗婕)28日，《云南省铁路安全管理条例》(下称《条例》)新闻发布会在昆明市举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722473.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网南宁10月28日电(记者 黄艳梅)广西壮族自治区卫生健康委员会28日举行新闻发布会，介绍广西加快完善生育支持政策体系、推动建设生育友好型社会的工作进展与成效。从育儿补贴落地、托育服务扩容，到母婴安全保障、人口服务管理夯实，广西正以系列措施回应民众生育关切。" data-title="广西多点发力 加快完善生育支持政策体系" data-date="10-28 22:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 22:17</span>
          <span class="news-item-title">广西多点发力 加快完善生育支持政策体系</span>
          <span class="news-value-point">💡 中新网南宁10月28日电(记者 黄艳梅)广西壮族自治区卫生健康委员会28日举行新闻发布会，介绍广西加快完善生育支持政策体系、推动建设生育友好型社…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722449.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网杭州10月28日电 (钱晨菲 张力 倪纵宾)智能警务装备集中展出、可爱警犬互动打卡、安全普法趣味答疑……10月28日，杭州萧山国际机场T4航站楼热闹十足。浙江省公安厅机场公安局在此举办“浙里有你 飞警守护”警营开放日活动，同步发布全新升级的“小飞警”卡通形象，吸引众多过往旅客驻足参与。" data-title="全国民航公安系统首个自主卡通IP“小飞警”全新亮相" data-date="10-28 21:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 21:29</span>
          <span class="news-item-title">全国民航公安系统首个自主卡通IP“小飞警”全新亮相</span>
          <span class="news-value-point">💡 中新网杭州10月28日电 (钱晨菲 张力 倪纵宾)智能警务装备集中展出、可爱警犬互动打卡、安全普法趣味答疑……10月28日，杭州萧山国际机场T4…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/us-marines-join-nato-mission-in-the-baltic-sea-to-protect-undersea-cables-from-sabotage-as-russia-continues-to-lurk-around-four-dozen-recon-and-intel-specialists-deployed-to-deter-seabed-threats" target="_blank" rel="noopener" data-cat="shizheng" data-summary="50名美国海军陆战队员正在加入北约的任务，以帮助保护和监测波罗的海的海底基础设施。" data-title="US Marines join NATO mission in the Baltic Sea to protect undersea cables from sabotage as Russia continues to lurk" data-date="10-28 21:24" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-28 21:24</span>
          <span class="news-item-title">美国海军陆战队加入北约在波罗的海的任务，以保护海底电缆免受破坏，因为俄罗斯继续潜伏</span>
          <span class="news-item-title-en">US Marines join NATO mission in the Baltic Sea to protect undersea cables from sabotage as Russia continues to lurk</span>
          <span class="news-value-point">💡 50名美国海军陆战队员正在加入北约的任务，以帮助保护和监测波罗的海的海底基础设施</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722424.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥10月28日电 (记者 张强)记者28日从安徽省政府新闻办举行的新闻发布会上获悉，第十六届安徽国际文化旅游节定于11月10日在合肥开幕，马来西亚应邀担任主宾国。" data-title="马来西亚应邀担任第十六届安徽国际文化旅游节主宾国" data-date="10-28 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 21:22</span>
          <span class="news-item-title">马来西亚应邀担任第十六届安徽国际文化旅游节主宾国</span>
          <span class="news-value-point">💡 中新网合肥10月28日电 (记者 张强)记者28日从安徽省政府新闻办举行的新闻发布会上获悉，第十六届安徽国际文化旅游节定于11月10日在合肥开幕…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722445.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆10月28日电(陈媛)28日，第二届西部陆海新通道建设劳动和技能竞赛决赛在重庆市沙坪坝区开幕。来自重庆、内蒙古、湖南、广西、贵州、西藏、陕西、甘肃、青海、宁夏、新疆11个省(区、市)的技能人才，将进行为期3天的技能比拼与交流。" data-title="第二届西部陆海新通道建设劳动和技能竞赛决赛在渝开幕" data-date="10-28 21:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 21:20</span>
          <span class="news-item-title">第二届西部陆海新通道建设劳动和技能竞赛决赛在渝开幕</span>
          <span class="news-value-point">💡 中新网重庆10月28日电(陈媛)28日，第二届西部陆海新通道建设劳动和技能竞赛决赛在重庆市沙坪坝区开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-28/10722435.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：28日，以色列议会选举初步计票结果显示，支持现任总理内塔尼亚胡的右翼阵营与反对派阵营均未获得绝对多数席位。内塔尼亚胡领导的利库德集团仍为议会第一大党。" data-title="初步计票显示以色列两大阵营均未获议会多数席位" data-date="10-28 21:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 21:13</span>
          <span class="news-item-title">初步计票显示以色列两大阵营均未获议会多数席位</span>
          <span class="news-value-point">💡 新华社快讯：28日，以色列议会选举初步计票结果显示，支持现任总理内塔尼亚胡的右翼阵营与反对派阵营均未获得绝对多数席位</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-28/10722423.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="西班牙卡斯蒂利亚-拉曼查自治区政府28日说，当天上午在其首府托莱多发生的高速铁路列车相撞事故死亡人数上升至64人。(总台记者 杨帆）" data-title="西班牙官方公布高铁相撞事故已致64人死亡" data-date="10-28 21:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 21:03</span>
          <span class="news-item-title">西班牙官方公布高铁相撞事故已致64人死亡</span>
          <span class="news-value-point">💡 西班牙卡斯蒂利亚-拉曼查自治区政府28日说，当天上午在其首府托莱多发生的高速铁路列车相撞事故死亡人数上升至64人</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/019/246.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，苹果今天（10 月 29 日）正式公布配备 512GB 统一内存的 Mac Studio 售价。该配置仅面向搭载 M5 Ultra 芯片（ 36 核 CPU 与 80 核 GPU）的顶配机型，相比较 96GB 版本价格上涨 116,250 元。IT之家注：512GB 内存版目前仅适用于 M5 Ultra 芯片（36 核 CPU 与 80 核 GPU）顶配，用户如果选择 M5 Ultra（30 核 CPU 与 64 核 GPU）会跳出相关提示：在内存配置选项，苹果 Mac Studio 从 96GB 升级到 512GB 需要加价 116,250 元人民币。在存储搭配方面，如果用户选择 M5 Ultra 芯片 + 512GB 内存 +1TB 存储，售价为 172" data-title="苹果上架 512GB 内存版 Mac Studio：较 96GB 配置贵 116250 元" data-date="10-29 01:54" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 01:54</span>
          <span class="news-item-title">苹果上架 512GB 内存版 Mac Studio：较 96GB 配置贵 116250 元</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果今天（10 月 29 日）正式公布配备 512GB 统一内存的 Mac Studio 售价</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/242.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，苹果 24 英寸新款 iMac 现已在京东开启预购，新品升级 M6 芯片，设计与旧款没有差别，定价 12499 元起，国补后到手价 10999 元起。外观方面，新款 iMac 沿袭上一代外观，提供银色、蓝色、绿色、粉色等配色可选。搭载 24 英寸 4.5K 分辨率屏幕，最高亮度 500nits，支持 P3 广色域和 10bit 色深，提供纳米纹理玻璃选项。规格方面，新款 iMac 搭载 M6 芯片，双雷雳接口机型为 10 核 CPU、10 核 GPU 及双 16 核 NPU；四雷雳接口型号采用 12 核 CPU、12 核心 GPU 及双 16 核 NPU。标配 16GB 统一内存，可选 24GB 或 32GB。硬盘为 256GB 起步，可选 512GB/1T" data-title="苹果 M6 版 24 英寸 iMac 开启预购，国补后 10999 元起" data-date="10-29 01:40" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 01:40</span>
          <span class="news-item-title">苹果 M6 版 24 英寸 iMac 开启预购，国补后 10999 元起</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果 24 英寸新款 iMac 现已在京东开启预购，新品升级 M6 芯片，设计与旧款没有差别，定价 12499…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub" target="_blank" rel="noopener" data-cat="keji" data-summary="马来西亚海关在吉隆坡国际机场查获了30台服务器，其中包含价值超过1200万$的先进人工智能芯片，当局正在调查与之前多次查获有关的可疑走私网络。" data-title="Malaysia seizes $12 million worth of advanced AI chips hidden inside 30 servers" data-date="10-29 01:02" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 01:02</span>
          <span class="news-item-title">马来西亚查获价值1200万$的隐藏在30台服务器中的高级人工智能芯片</span>
          <span class="news-item-title-en">Malaysia seizes $12 million worth of advanced AI chips hidden inside 30 servers</span>
          <span class="news-value-point">💡 马来西亚海关在吉隆坡国际机场查获了30台服务器，其中包含价值超过1200万$的先进人工智能芯片，当局正在调查与之前多次查获有关的可疑走私网络</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/as-ai-agents-reshape-the-web-google-opens-gemini-and-search-to-more-apps/" target="_blank" rel="noopener" data-cat="keji" data-summary="一个新的开发者平台将允许企业将其服务带入谷歌的人工智能体验，这可能会改变消费者发现和使用应用的方式。" data-title="As AI agents reshape the web, Google opens Gemini and Search to more apps" data-date="10-29 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">随着人工智能代理重塑网络，谷歌将Gemini和Search开放给更多应用程序</span>
          <span class="news-item-title-en">As AI agents reshape the web, Google opens Gemini and Search to more apps</span>
          <span class="news-value-point">💡 一个新的开发者平台将允许企业将其服务带入谷歌的人工智能体验，这可能会改变消费者发现和使用应用的方式</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/ai-execs-may-be-too-out-of-touch-to-build-for-the-general-public/" target="_blank" rel="noopener" data-cat="keji" data-summary="技术领导者吹嘘使用人工智能与家人联系时，他们是多么的脱节。" data-title="AI execs may be too out of touch to build for the general public" data-date="10-28 23:53" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 23:53</span>
          <span class="news-item-title">人工智能高管可能过于脱节，无法为公众打造</span>
          <span class="news-item-title-en">AI execs may be too out of touch to build for the general public</span>
          <span class="news-value-point">💡 技术领导者吹嘘使用人工智能与家人联系时，他们是多么的脱节</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/south-koreas-financial-industry-hit-by-fresh-wave-of-cyberattacks/" target="_blank" rel="noopener" data-cat="keji" data-summary="韩国金融机构受到了另一波网络攻击的打击，凸显了亚洲人工智能驱动黑客攻击的风险日益增加。" data-title="South Korea’s financial industry hit by fresh wave of cyberattacks" data-date="10-28 23:41" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 23:41</span>
          <span class="news-item-title">韩国金融业遭遇新一轮网络攻击</span>
          <span class="news-item-title-en">South Korea’s financial industry hit by fresh wave of cyberattacks</span>
          <span class="news-value-point">💡 韩国金融机构受到了另一波网络攻击的打击，凸显了亚洲人工智能驱动黑客攻击的风险日益增加</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/manufacturing/ai-component-hikes-force-the-worlds-largest-pc-makers-to-return-manufacturing-capacity-to-china-brands-to-seek-lower-production-costs-and-efficiency-in-established-supply-chain" target="_blank" rel="noopener" data-cat="keji" data-summary="由于已建立的供应链和劳动力，中国的个人电脑制造成本往往更低。较小的中国供应商也通过为CXMT等国内芯片制造商提供更便捷的渠道来赢得订单。" data-title="AI component hikes force the world&#39;s largest PC makers to return manufacturing capacity to China" data-date="10-28 23:24" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-28 23:24</span>
          <span class="news-item-title">人工智能组件的增长迫使全球最大的PC制造商将制造能力返回中国</span>
          <span class="news-item-title-en">AI component hikes force the world's largest PC makers to return manufacturing capacity to China</span>
          <span class="news-value-point">💡 由于已建立的供应链和劳动力，中国的个人电脑制造成本往往更低</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-tells-engineers-to-stop-tokenmaxxing-to-look-productive-says-ai-will-be-central-to-software-development-but-usage-is-not-the-goal-new-guidelines-claim" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊发布了新的工程指南，警告开发人员和经理不要使用“tokenmaxxing” ，认为除非与长期结果挂钩，否则人工智能使用指标“存在严重缺陷”。此举是因为优步和Accent也存在类似的支出问题" data-title="Amazon tells engineers to stop ‘tokenmaxxing’ to look productive" data-date="10-28 23:13" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-28 23:13</span>
          <span class="news-item-title">亚马逊告诉工程师停止“tokenmaxxing”以看起来富有成效</span>
          <span class="news-item-title-en">Amazon tells engineers to stop ‘tokenmaxxing’ to look productive</span>
          <span class="news-value-point">💡 亚马逊发布了新的工程指南，警告开发人员和经理不要使用“tokenmaxxing” ，认为除非与长期结果挂钩，否则人工智能使用指标“存在严重缺陷”</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达刚刚发布了一个可以转录多达40种语言的自由语音到文本模型，但它只适用于录音，而不适用于现场音频，因此它是会议和医疗转录工具的重要一步，同时仍然将实时使用留给竞争对手，例如" data-title="Voice AI in vogue: Nvidia releases new open transcription model" data-date="10-28 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 23:00</span>
          <span class="news-item-title">流行的语音人工智能：英伟达发布新的开放式转录模型</span>
          <span class="news-item-title-en">Voice AI in vogue: Nvidia releases new open transcription model</span>
          <span class="news-value-point">💡 英伟达刚刚发布了一个可以转录多达40种语言的自由语音到文本模型，但它只适用于录音，而不适用于现场音频，因此它是会议和医疗转录工具的重要一步，同时…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-28/10722452.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网重庆10月28日电 (马佳欣)28日，在“开局起步十五五·建设现代化新重庆”系列主题新闻发布会南岸专场上，南岸区委书记周和华介绍，“十五五”期间，南岸将释放“两院一湾”建设牵引效应，做强以“两院一湾”为引领的人工智能创新集群。该区将从服务“两院”发展、湾区整体规划、产业发展行动、夯实智算底座、创新体系建设、场景融合应用、创新生态营造七个方面系统推进建设。" data-title="释放“两院一湾”建设牵引效应 重庆南岸做强人工智能创新集群" data-date="10-28 21:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 21:29</span>
          <span class="news-item-title">释放“两院一湾”建设牵引效应 重庆南岸做强人工智能创新集群</span>
          <span class="news-value-point">💡 中新网重庆10月28日电 (马佳欣)28日，在“开局起步十五五·建设现代化新重庆”系列主题新闻发布会南岸专场上，南岸区委书记周和华介绍，“十五五…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/manufacturing/sk-hynix-owned-solidigm-is-plotting-a-new-usd45-billion-flash-memory-factory-for-the-us-report-claims-wants-go-ahead-to-export-equipment-for-china-upgrades-in-return" target="_blank" rel="noopener" data-cat="keji" data-summary="SK海力士的美国子公司Solidigm正在讨论是否可能投资450亿美元在美国建造一家新的闪存芯片工厂。" data-title="SK hynix-owned Solidigm is plotting a new $45 billion flash memory factory for the US, report claims" data-date="10-28 21:01" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-28 21:01</span>
          <span class="news-item-title">报告称， SK海力士旗下的Solidigm正在为美国规划一个新的450亿美元闪存工厂</span>
          <span class="news-item-title-en">SK hynix-owned Solidigm is plotting a new $45 billion flash memory factory for the US, report claims</span>
          <span class="news-value-point">💡 SK海力士的美国子公司Solidigm正在讨论是否可能投资450亿美元在美国建造一家新的闪存芯片工厂</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/505928.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月28 日，蚂蚁集团旗下百灵大模型正式开源 Ling-3.1-flash-1019。" data-title="Personal Agent走向真实任务，蚂蚁百灵开源 Ling" data-date="10-28 12:04" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-28 12:04</span>
          <span class="news-item-title">Personal Agent走向真实任务，蚂蚁百灵开源 Ling</span>
          <span class="news-value-point">💡 10月28 日，蚂蚁集团旗下百灵大模型正式开源 Ling-3.1-flash-1019</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/27/vcs-will-make-billions-on-anthropics-ipo-but-amazon-is-set-to-make-much-much-more/" target="_blank" rel="noopener" data-cat="keji" data-summary="大量音符转换揭示了亚马逊在Anthropic所有权的真实程度。" data-title="VCs will make billions on Anthropic’s IPO, but Amazon is set to make much (much) more" data-date="10-28 09:15" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 09:15</span>
          <span class="news-item-title">风险投资公司将在Anthropic的首次公开募股中赚取数十亿美元，但亚马逊将赚取更多（更多）</span>
          <span class="news-item-title-en">VCs will make billions on Anthropic’s IPO, but Amazon is set to make much (much) more</span>
          <span class="news-value-point">💡 大量音符转换揭示了亚马逊在Anthropic所有权的真实程度</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c623dz784403o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic 的招股说明书长达355页，其中包含大量从未披露过的公司资讯。" data-title="Anthropic 重磅上市" data-date="10-28 08:47" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 08:47</span>
          <span class="news-item-title">Anthropic 重磅上市</span>
          <span class="news-value-point">💡 Anthropic 的招股说明书长达355页，其中包含大量从未披露过的公司资讯</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/27/parents-sue-openai-alleging-gpt-4o-coached-their-daughter-off-seizure-medication/" target="_blank" rel="noopener" data-cat="keji" data-summary="一家人正在起诉OpenAI ，称ChatGPT指导他们的女儿在2月份去世前悄悄减少她的癫痫发作药物，并向她的医生隐瞒。" data-title="Parents sue OpenAI, alleging GPT-4o coached their daughter off seizure medication" data-date="10-28 07:34" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 07:34</span>
          <span class="news-item-title">父母起诉OpenAI ，声称GPT-4o指导他们的女儿戒断癫痫药物</span>
          <span class="news-item-title-en">Parents sue OpenAI, alleging GPT-4o coached their daughter off seizure medication</span>
          <span class="news-value-point">💡 一家人正在起诉OpenAI ，称ChatGPT指导他们的女儿在2月份去世前悄悄减少她的癫痫发作药物，并向她的医生隐瞒</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/liverpool-vs-chelsea/live/578612" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool vs Chelsea LIVE!" data-title="Liverpool vs Chelsea LIVE!" data-date="10-29 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">利物浦vs切尔西直播！</span>
          <span class="news-item-title-en">Liverpool vs Chelsea LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-city-vs-brighton-and-hove-albion/live/578614" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City change NINE to host Brighton LIVE!" data-title="Man City change NINE to host Brighton LIVE!" data-date="10-29 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">曼城改为九号，现场直播布莱顿！</span>
          <span class="news-item-title-en">Man City change NINE to host Brighton LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/chelsea-women-vs-roma-women/live/578251" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WCL: Beever-Jones misses big chance for Chelsea vs Roma LIVE!" data-title="WCL: Beever-Jones misses big chance for Chelsea vs Roma LIVE!" data-date="10-29 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">WCL ： Beever-Jones错过了切尔西对罗马直播的大好机会！</span>
          <span class="news-item-title-en">WCL: Beever-Jones misses big chance for Chelsea vs Roma LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! The stats behind Man Utd&#39;s poor recruitment..." data-title="Transfer Centre LIVE! The stats behind Man Utd&#39;s poor recruitment..." data-date="10-29 00:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 00:45</span>
          <span class="news-item-title">转会中心现场直播！曼联糟糕的招募背后的统计数据...</span>
          <span class="news-item-title-en">Transfer Centre LIVE! The stats behind Man Utd's poor recruitment...</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Details of Arteta&#39;s conversation with Dowman revealed" data-title="Arsenal latest: Details of Arteta&#39;s conversation with Dowman revealed" data-date="10-29 00:09" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 00:09</span>
          <span class="news-item-title">阿森纳最新消息：透露了Arteta与Dowman的对话细节</span>
          <span class="news-item-title-en">Arsenal latest: Details of Arteta's conversation with Dowman revealed</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604803/max-dowman-red-card-arsenals-appeal-against-decision-will-fail-says-former-premier-league-referee-dermot-gallagher" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英超联赛裁判德莫特·加拉格尔（ Dermot Gallagher ）认为，阿森纳对马克斯·道曼（ Max Dowman ）在卡拉宝杯（ Carabao Cup ）击败弗利特伍德镇（ Fleetwood Town ）的冲击" data-title="Ref Watch: Arsenal&#39;s red card appeal will fail - Dowman was aggressive" data-date="10-28 21:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 21:15</span>
          <span class="news-item-title">参考观看：阿森纳的红牌吸引力将失败-道曼咄咄逼人</span>
          <span class="news-item-title-en">Ref Watch: Arsenal's red card appeal will fail - Dowman was aggressive</span>
          <span class="news-value-point">💡 前英超联赛裁判德莫特·加拉格尔（ Dermot Gallagher ）认为，阿森纳对马克斯·道曼（ Max Dowman ）在卡拉宝杯（ Car…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cje36dn5nx36o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）在俱乐部的训练场举行了畅谈。" data-title="Carrick and Fernandes hold clear" data-date="10-28 19:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 19:48</span>
          <span class="news-item-title">卡里克和费尔南德斯保持清醒</span>
          <span class="news-item-title-en">Carrick and Fernandes hold clear</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）在俱乐部的训练场举行…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Should Fernandes start at Chelsea? VOTE!" data-title="Man Utd latest: Should Fernandes start at Chelsea? VOTE!" data-date="10-28 19:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 19:00</span>
          <span class="news-item-title">曼联最新消息：费尔南德斯应该从切尔西开始吗？投票！</span>
          <span class="news-item-title-en">Man Utd latest: Should Fernandes start at Chelsea? VOTE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604738/bruno-fernandes-man-utd-head-coach-michael-carrick-and-club-captain-hold-clear-the-air-talks-ahead-of-chelsea-fixture" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）已经面对面会面，以清除空气，两人都发誓要重新专注于扭转俱乐部的赛季。" data-title="Carrick and Fernandes hold clear-the-air talks ahead of Chelsea fixture" data-date="10-28 18:39" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 18:39</span>
          <span class="news-item-title">卡里克和费尔南德斯在切尔西比赛前举行了晴空会谈</span>
          <span class="news-item-title-en">Carrick and Fernandes hold clear-the-air talks ahead of Chelsea fixture</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）已经面对面会面，以清…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604280/michael-carrick-is-latest-man-utd-manager-under-pressure-but-has-poor-recruitment-made-them-a-mid-table-team-between-the-lines" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在被伯恩茅斯击败后，俱乐部考虑在四年内进行第四次管理层变动后，迈克尔·卡里克被曼联暂停执行。" data-title="Expectation vs reality: What if Man Utd have become a mid" data-date="10-28 17:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 17:35</span>
          <span class="news-item-title">期望与现实：如果曼联已经成为</span>
          <span class="news-item-title-en">Expectation vs reality: What if Man Utd have become a mid</span>
          <span class="news-value-point">💡 在被伯恩茅斯击败后，俱乐部考虑在四年内进行第四次管理层变动后，迈克尔·卡里克被曼联暂停执行</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwly0myd08reo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西前锋若昂·佩德罗的伤病是通过梦幻英超联赛的比赛泄露的，但俱乐部能做些什么吗？" data-title="Can clubs stop team news leaking out through FPL picks?" data-date="10-28 16:36" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 16:36</span>
          <span class="news-item-title">俱乐部能否阻止球队新闻通过FPL选秀权泄露出去？</span>
          <span class="news-item-title-en">Can clubs stop team news leaking out through FPL picks?</span>
          <span class="news-value-point">💡 切尔西前锋若昂·佩德罗的伤病是通过梦幻英超联赛的比赛泄露的，但俱乐部能做些什么吗</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqgkv216dx2no?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦在杰里米·雅克的签约中击败了切尔西，后卫在安菲尔德茁壮成长。事情本可以有很大不同……" data-title="Liverpool gambled on Jacquet and it is paying off" data-date="10-28 16:36" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 16:36</span>
          <span class="news-item-title">利物浦在Jacquet赌博，它正在获得回报</span>
          <span class="news-item-title-en">Liverpool gambled on Jacquet and it is paying off</span>
          <span class="news-value-point">💡 利物浦在杰里米·雅克的签约中击败了切尔西，后卫在安菲尔德茁壮成长</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6x2v4p284ylo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="因在节目中以“独裁者”形容已故中国领导人毛泽东，法国足球明星基利安·姆巴佩（麦巴比）近日在中国引发争议，多家中国大型品牌先后宣布终止与其合作。姆巴佩发表道歉声明也不被中国网民接纳。" data-title="姆巴佩就“中国独裁者”迷因道歉 背后的资讯真空与“毛泽东热”" data-date="10-28 13:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 13:27</span>
          <span class="news-item-title">姆巴佩就“中国独裁者”迷因道歉 背后的资讯真空与“毛泽东热”</span>
          <span class="news-value-point">💡 因在节目中以“独裁者”形容已故中国领导人毛泽东，法国足球明星基利安·姆巴佩（麦巴比）近日在中国引发争议，多家中国大型品牌先后宣布终止与其合作</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwz0vgj35k7mo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）着眼于导致曼联决定让压力不足的迈克尔·卡里克（ Michael Carrick ）担任周六切尔西之行的主教练的48小时。" data-title="Man Utd stick with Carrick - inside a turbulent 48 hours at Old Trafford" data-date="10-28 02:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 02:56</span>
          <span class="news-item-title">与卡里克一起在老特拉福德动荡的48小时内体验曼联</span>
          <span class="news-item-title-en">Man Utd stick with Carrick - inside a turbulent 48 hours at Old Trafford</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）着眼于导致曼联决定让压力不足的迈克尔·卡里克（ Michael Carrick ）担任周六切尔西之…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/019/249.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果今日推出首款触控屏 MacBook Pro，定价 22,999 元起。该产品采用双层串联 OLED 面板，HDR 峰值亮度可达 2,000 nits。如今苹果已经公布了这款 MacBook Pro 的第三方应用触控适配情况，IT之家附未来支持名单如下：办公与协作： Notion、Canva、Zoom、Microsoft Word、Excel、PowerPoint、Outlook（Microsoft Office）照片与视频： Adobe Lightroom、DaVinci Resolve3D 与动画： Blender、Maxon Cinema 4D、Maxon ZBrush、Shapr3D音乐： Algoriddim djay Pro需要注意的是，上述应" data-title="苹果触屏 MacBook Pro 应用适配情况：Lightroom、达芬奇、C4D、Office 等今年晚些时候支持" data-date="10-29 02:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 02:24</span>
          <span class="news-item-title">苹果触屏 MacBook Pro 应用适配情况：Lightroom、达芬奇、C4D、Office 等今年晚些时候支持</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果今日推出首款触控屏 MacBook Pro，定价 22,999 元起</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/248.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，太平洋时间 10 月 28 日上午 10 点（北京时间 10 月 29 日凌晨 1 点）在洛杉矶举行的“Pro and Tell”体验活动中，苹果公司正式推出首款支持触控操作的 MacBook Pro（PROLED XDR 显示屏），国行起售价 22999 元。苹果公司前首席执行官、现任执行董事长蒂姆 · 库克（Tim Cook）发布微博，表示：我们把触控带到了 Mac！从全新 iPad mini，到 14 英寸 MacBook Pro 和 iMac，再到配备 PROLED XDR 显示屏并支持屏幕触控的 MacBook Pro，创作者们有了全新的工具，尽情发挥才华，达到创意新高度。We brought Touch to the Mac! From the" data-title="苹果 CEO 特努斯：MacBook Pro PROLED XDR 显示屏有多出色，亲手一触就知道" data-date="10-29 02:21" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 02:21</span>
          <span class="news-item-title">苹果 CEO 特努斯：MacBook Pro PROLED XDR 显示屏有多出色，亲手一触就知道</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，太平洋时间 10 月 28 日上午 10 点（北京时间 10 月 29 日凌晨 1 点）在洛杉矶举行的“Pro…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1020960/google-xreal-glasses-debut-meta-vr-glasses-price-release-date" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在这种经济环境下，产品在首次亮相前多久会变得更便宜？这刚刚发生在谷歌/Xreal Aura上，这款轻巧的95克眼镜配有系绳式Android XR计算冰球和多个虚拟屏幕，" data-title="Surprise: The Google Xreal glasses debut at a Meta" data-date="10-29 02:14" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 02:14</span>
          <span class="news-item-title">惊喜： Google Xreal眼镜在Meta上首次亮相</span>
          <span class="news-item-title-en">Surprise: The Google Xreal glasses debut at a Meta</span>
          <span class="news-value-point">💡 在这种经济环境下，产品在首次亮相前多久会变得更便宜</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1019109/apple-macbook-pro-m6-proled-xdr-how-to-buy-price-release-date" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果终于在2026年10月的“Pro and Tell”活动中展示了配备PROLED XDR显示屏的14英寸和16英寸MacBook Pro笔记本电脑。期待已久的笔记本电脑配备了具有全触摸功能的Tandem OLED显示屏，同时还削减了一些" data-title="Here’s where to preorder the latest MacBook Pros" data-date="10-29 02:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 02:10</span>
          <span class="news-item-title">这里是预订最新MacBook Pro的地方</span>
          <span class="news-item-title-en">Here’s where to preorder the latest MacBook Pros</span>
          <span class="news-value-point">💡 苹果终于在2026年10月的“Pro and Tell”活动中展示了配备PROLED XDR显示屏的14英寸和16英寸MacBook Pro笔记…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/247.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果首款触控屏 MacBook Pro 最高可选 16TB 存储空间，相比此前 MacBook Pro 最高 8TB 翻倍。需要注意的是，新款 MacBook Pro 仅有 M5 Max 机型支持选择 16TB 硬盘。而且要升级这么高的容量，您需要支付 52,500 元（以 2TB → 16TB 计）。硬件方面，新款 MacBook Pro 采用双层串联 OLED 1Hz-120Hz 自适应刷新率触控屏，支持 1,000 尼特持续全屏亮度、2,000 尼特 HDR 和 SDR 峰值亮度，覆盖 P3 + Adobe RGB 广色域。该机还带有“灵动岛”（1,200 万像素 Center Stage 摄像头）。此外，该机搭载重新设计的六扬声器系统，低音下潜增强" data-title="苹果新 MacBook Pro 最高可选 16TB 存储空间：相比此前 8TB 翻倍，得加 5.25 万元" data-date="10-29 02:09" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 02:09</span>
          <span class="news-item-title">苹果新 MacBook Pro 最高可选 16TB 存储空间：相比此前 8TB 翻倍，得加 5.25 万元</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果首款触控屏 MacBook Pro 最高可选 16TB 存储空间，相比此前 MacBook Pro 最高 …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/column/1020859/optimizer-theranos-haemanthus-you-can-see-everything" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这是由Verge资深评论员Victoria Song发送的每周时事通讯Optimizer ，它剖析并讨论了最新的小玩意和药水，这些小玩意和药水宣称它们将改变你的生活。在此选择Optimizer。从远处看，很容易回头看" data-title="You can see every red flag in Theranos 2.0" data-date="10-29 02:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 02:00</span>
          <span class="news-item-title">您可以在Theranos 2.0中看到每个危险信号</span>
          <span class="news-item-title-en">You can see every red flag in Theranos 2.0</span>
          <span class="news-value-point">💡 这是由Verge资深评论员Victoria Song发送的每周时事通讯Optimizer ，它剖析并讨论了最新的小玩意和药水，这些小玩意和药水宣…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/dining/cheesecake-factory-obama-trump-midterm-elections.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="早在巴洛克风格的装饰和阶级身份成为中期谈话要点之前，这家经久耐用的连锁餐厅就经历了一些枯萎的批评。" data-title="What Does the Cheesecake Factory’s Designer Think of Obama and Trump’s Jabs at His Décor?" data-date="10-29 01:55" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 01:55</span>
          <span class="news-item-title">芝士蛋糕工厂的设计师如何看待奥巴马和特朗普的装饰？</span>
          <span class="news-item-title-en">What Does the Cheesecake Factory’s Designer Think of Obama and Trump’s Jabs at His Décor?</span>
          <span class="news-value-point">💡 早在巴洛克风格的装饰和阶级身份成为中期谈话要点之前，这家经久耐用的连锁餐厅就经历了一些枯萎的批评</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/245.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果公司今日推出首款触控屏 MacBook Pro，提供 14 英寸和 16 英寸两种型号。值得注意的是，这款笔记本支持灵动岛，可将实时活动、聚焦搜索和 Siri AI 整合到屏幕上方交互，这也是苹果首次为 Mac 电脑引入灵动岛。IT之家了解到，苹果公司最早在 2022 年 9 月的 iPhone 14 Pro 系列推出灵动岛。它在苹果手机中取代了刘海设计，摄像头开孔相比原来更小，还能够通过软件界面显示实时活动、音乐播放、计时器等各类控件。而 Mac 上的灵动岛支持接听电话、控制音乐播放，以及显示隔空投送请求等，还能够作为聚焦搜索和 Siri AI 的交互入口。不过新款 MacBook Pro 仍然采用触控 ID，并配备 1200 万像素 Center S" data-title="苹果首度为 Mac 引入灵动岛：支持显示音乐播放、实时活动等，Siri AI 多了个入口" data-date="10-29 01:53" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 01:53</span>
          <span class="news-item-title">苹果首度为 Mac 引入灵动岛：支持显示音乐播放、实时活动等，Siri AI 多了个入口</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果公司今日推出首款触控屏 MacBook Pro，提供 14 英寸和 16 英寸两种型号</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1020084/macos-touchscreen-changes" target="_blank" rel="noopener" data-cat="zonghe" data-summary="触摸屏笔记本电脑在Windows世界中并不是什么新鲜事，但苹果刚刚宣布推出首款带触摸屏的MacBook。不过，苹果并不急于在macOS中改变很多东西来优化触摸：大多数触摸操作将" data-title="Here’s how macOS is changing for touchscreens" data-date="10-29 01:48" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 01:48</span>
          <span class="news-item-title">以下是macOS在触摸屏方面的变化</span>
          <span class="news-item-title-en">Here’s how macOS is changing for touchscreens</span>
          <span class="news-value-point">💡 触摸屏笔记本电脑在Windows世界中并不是什么新鲜事，但苹果刚刚宣布推出首款带触摸屏的MacBook</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/244.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果在今天的特别活动中正式推出了首款触控屏 MacBook Pro（配备 PROLED XDR 显示屏的 MacBook Pro），值得一提的是，该机重新为 A 面带回了发光苹果 Logo。回顾历史，苹果从 1999 年 PowerBook G3 系列开始为笔记本 A 面引入发光苹果 Logo，相应 Logo 并没有配备任何独立的 LED 光源，而是直接“借用”了屏幕自身的背光。具体而言，苹果在 CNC 切割铝合金 A 面时，会在正中央镂空切出苹果 Logo 的形状，并在该孔位嵌入一块高透光率、表面经过磨砂雾面处理的白色聚碳酸酯（塑料）导光板。在屏幕面板内部的反光遮罩层上，苹果也精确对应 Logo 的位置预留了一个没有反光材料的透光区域。当用户打开电脑、屏幕" data-title="时隔 10 年发光 Logo 回归：苹果首款触控屏 MacBook Pro“苹果标”又会亮了" data-date="10-29 01:48" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 01:48</span>
          <span class="news-item-title">时隔 10 年发光 Logo 回归：苹果首款触控屏 MacBook Pro“苹果标”又会亮了</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果在今天的特别活动中正式推出了首款触控屏 MacBook Pro（配备 PROLED XDR 显示屏的 Ma…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/243.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果公司 2026 款 MacBook Pro 已于今天（10 月 29 日）凌晨 1 点 10 分开启预购，起售价 15,999 元，最快 11 月 6 日送达。京东苹果 2026 款 14 英寸 MacBook Pro M6 15999 元直达链接机型芯片起售价14 英寸 M6RMB 15,999 起14 英寸 M5 ProRMB 20,999 起14 英寸 M5 MaxRMB 28,499 起16 英寸 M5 ProRMB 24,999 起16 英寸 M5 MaxRMB 32,499 起新款 M6 芯片的 14 英寸 MacBook Pro 继承了上一代外观，可选深空黑色和银色两种配色，配备 3024 x 1964 分辨率 120Hz 显示屏。该机搭载" data-title="15999 元起，苹果 M6 芯片版 14 英寸 MacBook Pro 开启预购" data-date="10-29 01:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 01:41</span>
          <span class="news-item-title">15999 元起，苹果 M6 芯片版 14 英寸 MacBook Pro 开启预购</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果公司 2026 款 MacBook Pro 已于今天（10 月 29 日）凌晨 1 点 10 分开启预购，…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/world/europe/spain-train-crash-survivor.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="62岁的费尔南多·塞科（ Fernando Seco ）说，他和其他人将至少十几名受伤的乘客从坠机现场转移，将残骸的一部分用作临时担架。" data-title="Spain Crash Survivor Describes a ‘Twisted Tangle of Metal’" data-date="10-29 01:29" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 01:29</span>
          <span class="news-item-title">西班牙坠机幸存者描述“扭曲的金属纠缠”</span>
          <span class="news-item-title-en">Spain Crash Survivor Describes a ‘Twisted Tangle of Metal’</span>
          <span class="news-value-point">💡 62岁的费尔南多·塞科（ Fernando Seco ）说，他和其他人将至少十几名受伤的乘客从坠机现场转移，将残骸的一部分用作临时担架</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1020069/apple-pro-and-tell-event-everything-announced-this-week" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果公司周三以“Pro and Tell”活动结束了为期一周的产品发布会，在那里它结束了传闻已久的触摸屏MacBook Pro。尽管苹果可能已经将其最大和最令人兴奋的更新保存到了最后，但它透露" data-title="Apple ‘Pro and Tell’ event: everything announced this week" data-date="10-29 01:27" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 01:27</span>
          <span class="news-item-title">Apple Pro和Tell活动：本周公布的一切</span>
          <span class="news-item-title-en">Apple ‘Pro and Tell’ event: everything announced this week</span>
          <span class="news-value-point">💡 苹果公司周三以“Pro and Tell”活动结束了为期一周的产品发布会，在那里它结束了传闻已久的触摸屏MacBook Pro</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1020676/apple-touchscreen-macbook-pro-reveal-video" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果刚刚在周三的“Pro and tell”活动上宣布了其首款触摸屏MacBook。在活动期间，它在新款MacBook Pro的视频中展示了期待已久的触摸屏，您可以在这里观看新的显示屏。" data-title="Watch Apple’s reveal video for the touchscreen MacBook Pro" data-date="10-29 01:19" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 01:19</span>
          <span class="news-item-title">观看苹果推出的触摸屏MacBook Pro视频</span>
          <span class="news-item-title-en">Watch Apple’s reveal video for the touchscreen MacBook Pro</span>
          <span class="news-value-point">💡 苹果刚刚在周三的“Pro and tell”活动上宣布了其首款触摸屏MacBook</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1020549/macbook-studio-touchscreen-hands-on" target="_blank" rel="noopener" data-cat="zonghe" data-summary="史蒂夫·乔布斯（ Steve Jobs ）著名地称触摸屏笔记本电脑“人体工程学很糟糕” ，十多年来，苹果公司一直坚决拒绝制造。今天，所有这些都随着MacBook Pro而改变--这是该公司首款采用触摸界面的笔记本电脑。虽然它不是" data-title="Hands-on with Apple’s touchscreen MacBook Pro" data-date="10-29 01:16" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 01:16</span>
          <span class="news-item-title">亲身体验苹果触摸屏MacBook Pro</span>
          <span class="news-item-title-en">Hands-on with Apple’s touchscreen MacBook Pro</span>
          <span class="news-value-point">💡 史蒂夫·乔布斯（ Steve Jobs ）著名地称触摸屏笔记本电脑“人体工程学很糟糕” ，十多年来，苹果公司一直坚决拒绝制造</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-29 02:24（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
