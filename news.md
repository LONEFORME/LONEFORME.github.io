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
      <span>2026-09-23 14:51 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-23/10702244.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月23日电 9月23日，国务院台办举行例行新闻发布会。有记者问：第一个问题，台湾“劳动部长”洪申翰赴南京参加APEC会议，桌牌使用“Chinese Taipei”，对比此前，台北市长蒋万安妻子曾因自称来自“Chinese Taipei”，却遭批评“自我矮化”，此次洪申翰却没有这样的声音。请问如何看待台湾内部的双重标准？第二个问题，台湾“劳动部长”洪申翰赴南京参加APEC会议返台后称，大陆方面有给予其平等参与及尊严，并未发生此前有舆论担心其可能被监听甚至无法返台等情形。请问大陆方面如何评价此次台湾部长级官员赴陆与会？" data-title="台当局以“Chinese Taipei”参加APEC 国台办回应" data-date="09-23 14:48" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-23 14:48</span>
      </div>
      <h2 class="hero-featured-title">台当局以“Chinese Taipei”参加APEC 国台办回应</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/006/253.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 23 日消息，科技媒体 Android Headline 今天（9 月 23 日）发布博文，报道称在 2026 骁龙峰会上，高通宣布将为其旗舰级芯片（主要为至尊版 Elite 系列）提供 8 年内核更新支持。IT之家注：内核是操作系统中负责硬件驱动与底层资源调度的核心程序。芯片厂商向手机厂商提供内核更新，是后者能否推送新版安卓系统及安全补丁的技术前提，直接决定设备软件支持的最长年限。该媒体指出此前制约安卓手机更新的关键瓶颈之一，就是内核更新供给不足。高通向 OEM 厂商发布内核更新，而 OEM 厂商再据此自行安排安卓系统与安全更新节奏，该媒体据此认为旗舰手机有望普及 7 年系统更新支持。在手机行业支持方面，该媒体指出三星和谷歌公司在全系旗舰产品上承诺 7 年更新；荣耀在 M" data-title="高通承诺 Elite 级芯片提供 8 年内核更新，旗舰手机有望普及 7 年安卓升级" data-date="09-23 14:49" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">高通承诺 Elite 级芯片提供 8 年内核更新，旗舰手机有望普及 7 年安卓升级</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ck7v4y7jv182o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="哪些英超球队表现优异，哪些球队表现不佳？" data-title="英超球队是如何真正开始的" data-date="09-23 14:22" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">英超球队是如何真正开始的</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.com/zhongwen/articles/c69v9207z2vwo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果你花一天时间在东京观光，可能会发现自己一路拿着空咖啡杯、7-Eleven蛋三明治的包装纸，以及愈来愈强烈的困惑感。日本以重视整洁闻名，那么，为什么却找不到地方丢垃圾呢？" data-title="日本以街道整洁无瑕而闻名，但为什么公共垃圾桶却如此难找？" data-date="09-23 14:50" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">日本以街道整洁无瑕而闻名，但为什么公共垃圾桶却如此难找？</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-23/10702244.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月23日电 9月23日，国务院台办举行例行新闻发布会。有记者问：第一个问题，台湾“劳动部长”洪申翰赴南京参加APEC会议，桌牌使用“Chinese Taipei”，对比此前，台北市长蒋万安妻子曾因自称来自“Chinese Taipei”，却遭批评“自我矮化”，此次洪申翰却没有这样的声音。请问如何看待台湾内部的双重标准？第二个问题，台湾“劳动部长”洪申翰赴南京参加APEC会议返台后称，大陆方面有给予其平等参与及尊严，并未发生此前有舆论担心其可能被监听甚至无法返台等情形。请问大陆方面如何评价此次台湾部长级官员赴陆与会？" data-title="台当局以“Chinese Taipei”参加APEC 国台办回应" data-date="09-23 14:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:48</span>
          <span class="news-item-title">台当局以“Chinese Taipei”参加APEC 国台办回应</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-23/10702214.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网海口9月23日电 (记者 符宇群)中秋月渐圆，琼州情更浓。22日晚，在中秋佳节来临之际，“月映琼州 共赴未来——2026海南海外联谊会中秋诗会”活动在海口举行，海内外600余名琼籍乡亲现场沉浸式感受中国传统节庆文化以及海南自贸港建设的蓬勃活力。" data-title="2026海南海外联谊会中秋诗会在海口举办" data-date="09-23 14:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:41</span>
          <span class="news-item-title">2026海南海外联谊会中秋诗会在海口举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-23/10702231.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网青岛9月23日电 (王禹)2026年生态环境部岛屿适应气候变化与海洋环境保护能力建设研讨班22日在位于青岛市即墨区的山东大学青岛校区结业。来自斐济、马尔代夫、马来西亚等13个国家的学员，通过此次学习进一步提升应对气候变化与海洋环境保护的能力。" data-title="十余国代表在山东青岛共研气候变化与海洋环境保护" data-date="09-23 14:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:37</span>
          <span class="news-item-title">十余国代表在山东青岛共研气候变化与海洋环境保护</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-23/10702191.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海9月23日电 (记者 许婧)“技能真的可以改变生活、成就自我。”22日，在上海科创职业技术学院举办的第48届世界技能大赛“一校一队”交流日活动现场，该校教师卢俊威对记者说。从赛场夺冠到讲台育人，卢俊威见证了技能改变人生的力量。" data-title="第48届世界技能大赛：技能无声，却让中外青年彼此看见" data-date="09-23 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:14</span>
          <span class="news-item-title">第48届世界技能大赛：技能无声，却让中外青年彼此看见</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-23/10702131.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网天津9月23日电 题：一街旧时光两岸共乡愁：津台同胞走进天津“80年代”怀旧街区" data-title="一街旧时光 两岸共乡愁：津台同胞走进天津“80年代”怀旧街区" data-date="09-23 13:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 13:59</span>
          <span class="news-item-title">一街旧时光 两岸共乡愁：津台同胞走进天津“80年代”怀旧街区</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-23/10702083.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月23日电(记者 孙自法)施普林格·自然旗下专业学术期刊《自然-化学工程》最新发表一篇技术研究论文指出，研究人员研发出一款能在体内给医疗装置供电并最终降解的可吞服纸电池，已在临床前研究(包括在猪体内开展的研究)中展现出应用前景。" data-title="国际最新研发出能给医疗装置供电的可吞服纸电池 展现应用前景" data-date="09-23 13:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 13:25</span>
          <span class="news-item-title">国际最新研发出能给医疗装置供电的可吞服纸电池 展现应用前景</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/23/business/trump-cnn-politico-ms-now-ban.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统认定， CNN、MS NOW和Politico “违反了白宫预期的专业精神和礼仪标准”。" data-title="白宫在法庭文件中为特朗普对CNN、MS NOW和Politico的禁令辩护" data-date="09-23 13:06" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-23 13:06</span>
          <span class="news-item-title">白宫在法庭文件中为特朗普对CNN、MS NOW和Politico的禁令辩护</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq39myp9dm9zo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="BBC记者团队在周二现场采访特朗普于联合国的演讲，并分析了当中的五个关键时刻。" data-title="特朗普联合国演说五个要点：古巴垮台、摧毁伊朗、格陵兰基地，以及把AI改名SI" data-date="09-23 12:24" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-23 12:24</span>
          <span class="news-item-title">特朗普联合国演说五个要点：古巴垮台、摧毁伊朗、格陵兰基地，以及把AI改名SI</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/politics/trump-greenland-denmark-agreement.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统签署了一项格陵兰安全协议，远远没有达到他将格陵兰岛变成美国领土的要求。" data-title="特朗普曾发誓要“拥有”格陵兰岛。他满足于更少的东西。" data-date="09-23 10:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-23 10:39</span>
          <span class="news-item-title">特朗普曾发誓要“拥有”格陵兰岛。他满足于更少的东西。</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/world/canada/carney-united-nations-general-assembly.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="加拿大总理马克·卡尼（ Mark Carney ）表示，世界现在正处于“一个世纪一两次”的阶段。" data-title="在联合国，卡尼为分裂的世界制定了广泛的计划" data-date="09-23 10:27" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-23 10:27</span>
          <span class="news-item-title">在联合国，卡尼为分裂的世界制定了广泛的计划</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-23/10702029.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月23日电 据土耳其阿纳多卢通讯社等外媒报道，当地时间22日，土耳其、阿联酋、印度尼西亚、卡塔尔、埃及、巴基斯坦、沙特阿拉伯和约旦八国外长发表联合声明，呼吁以色列立即履行加沙停火协议第一阶段规定的义务。" data-title="八国外长发声明： 吁以色列履行加沙停火协议有关义务" data-date="09-23 10:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 10:10</span>
          <span class="news-item-title">八国外长发声明： 吁以色列履行加沙停火协议有关义务</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-23/10702010.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月23日电 综合外媒23日报道，伊朗总统办公室宣布，总统佩泽希齐扬已抵达美国纽约。" data-title="伊朗总统佩泽希齐扬已抵达纽约 将出席联合国大会" data-date="09-23 10:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 10:08</span>
          <span class="news-item-title">伊朗总统佩泽希齐扬已抵达纽约 将出席联合国大会</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/politics/un-trump-speech-iran-venezuela-greenland.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统在联合国大会上的讲话等于拒绝了联合国的创始概念。" data-title="特朗普威胁在联合国演讲中消灭伊朗并宣布获胜者" data-date="09-23 09:57" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-23 09:57</span>
          <span class="news-item-title">特朗普威胁在联合国演讲中消灭伊朗并宣布获胜者</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckp84p0pzydgo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="专家分析，美中两国各自想要的东西不同，其中习近平更想要时间，“他一边想尽可能获得美国技术和市场，一边积极降低对美国的依赖性。在这个情况下，中美彼此交易但没有互信，追求和稳不求和解。”" data-title="习近平访美的“僵局控管”：中美如何台上握手、台下算计？" data-date="09-23 08:29" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-23 08:29</span>
          <span class="news-item-title">习近平访美的“僵局控管”：中美如何台上握手、台下算计？</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/politics/trump-arch-national-security.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统在面临其计划的法律挑战时，越来越多地援引这一理由，即使在他的凯旋门等更奇怪的情况下也是如此，他说现在将包括狙击手和无人机。" data-title="特朗普援引国家安全，因为他面临着对新闻禁令，华盛顿特区拱门等等的抵制" data-date="09-23 08:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-23 08:00</span>
          <span class="news-item-title">特朗普援引国家安全，因为他面临着对新闻禁令，华盛顿特区拱门等等的抵制</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/006/253.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 23 日消息，科技媒体 Android Headline 今天（9 月 23 日）发布博文，报道称在 2026 骁龙峰会上，高通宣布将为其旗舰级芯片（主要为至尊版 Elite 系列）提供 8 年内核更新支持。IT之家注：内核是操作系统中负责硬件驱动与底层资源调度的核心程序。芯片厂商向手机厂商提供内核更新，是后者能否推送新版安卓系统及安全补丁的技术前提，直接决定设备软件支持的最长年限。该媒体指出此前制约安卓手机更新的关键瓶颈之一，就是内核更新供给不足。高通向 OEM 厂商发布内核更新，而 OEM 厂商再据此自行安排安卓系统与安全更新节奏，该媒体据此认为旗舰手机有望普及 7 年系统更新支持。在手机行业支持方面，该媒体指出三星和谷歌公司在全系旗舰产品上承诺 7 年更新；荣耀在 M" data-title="高通承诺 Elite 级芯片提供 8 年内核更新，旗舰手机有望普及 7 年安卓升级" data-date="09-23 14:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-23 14:49</span>
          <span class="news-item-title">高通承诺 Elite 级芯片提供 8 年内核更新，旗舰手机有望普及 7 年安卓升级</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/247.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 23 日消息，特斯拉向着车轮上的私人助手不断演进，如今借助 Grok Bot，车辆不再只能回答知识问答或是调节车厢温度，当你正在开车时，它还可以完全免手动执行复杂的外部事务以及各类线上任务。IT之家注意到，特斯拉今日早些时候在 X 平台正式官宣北美上线该功能，并说明驾驶员现在可以查看电子邮件、管理日程、进行线上购物，甚至可以让 Grok Bot 帮你梳理已有对话和待办事项。就在这次正式推送的几周之前，SpaceX 人工智能部门的一名工程师就曾透露，特斯拉计划将 Grok Bot 整合进自家车辆，把原本还处于试验阶段的网页功能，变成车内可用的正式工具。Grok 在特斯拉车内的落地推进速度很快，其最初只是一款对话式 AI 聊天机器人，现已逐步发展成为深度嵌入车机系统的智能车载副" data-title="特斯拉北美车机上线 Grok Bot，开车就能语音下单买咖啡、发邮件" data-date="09-23 14:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-23 14:47</span>
          <span class="news-item-title">特斯拉北美车机上线 Grok Bot，开车就能语音下单买咖啡、发邮件</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/246.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 23 日消息，理想汽车产品线负责人李昕旸今日公布了 2026 款理想 i6 的最新的上市计划。2026 款 i6 原计划 9 月底开启预定并于 11 月初开始交付。在广泛地收集了用户的意见之后，我们希望避免用户下单后等待交付时间过长，因此我们将 2026 款 i6 的上市发布时间调整为 10 月底，开启交付的时间仍然为 11 月初，保持不变。据IT之家此前报道，2026 款理想 i6 已完成申报，新车搭载理想自研 5C 电池和自研马赫芯片。2026 款理想 i6 外形尺寸为长 4950 mm、宽 1935 mm、高 1655 mm，轴距达到 3000 mm；有单电机和双电机四驱两个版本，其中单电机版电机最大功率 250 千瓦，双电机版前后电机功率分别为 150 千瓦和 25" data-title="2026 款理想 i6 上市发布时间调整为 10 月底，11 月初开启交付保持不变" data-date="09-23 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-23 14:43</span>
          <span class="news-item-title">2026 款理想 i6 上市发布时间调整为 10 月底，11 月初开启交付保持不变</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/242.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 23 日消息，欧洲 CPU 初创企业 SiPearl 当地时间 22 日宣布向超算客户 Bull 交付首批 Rhea1 处理器的样品。根据两家企业此前签署的合同，基于 Rhea1 的 CPU 分区将被集成至位于德国的欧洲首台 E 级超算 JUPITER。Bull 已经开始在其 BullSequana XH3000 平台上集成 Rhea1。如果一切顺利，SiPearl 将确认其首笔重要收入。Rhea1 处理器基于台积电 6nm 制程节点，拥有 80 个 Arm Neoverse V1 内核，每个内核包含 2 个 256-bit SVE 单元；集成 4 个 16GB HBM 内存堆栈，提供 4 条支持 2DPC 的 DDR5 内存通道；可扩展出 104 条 PCIe Gen5" data-title="SiPearl 向超算客户 Bull 交付首批 Rhea1 CPU 处理器样品" data-date="09-23 14:33" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-23 14:33</span>
          <span class="news-item-title">SiPearl 向超算客户 Bull 交付首批 Rhea1 CPU 处理器样品</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496304.html" target="_blank" rel="noopener" data-cat="keji" data-summary="两万元，买到的是怎样一个机器人" data-title="稚晖君把机器人卖到2万元一台，可人可狗可开发！" data-date="09-23 13:16" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-23 13:16</span>
          <span class="news-item-title">稚晖君把机器人卖到2万元一台，可人可狗可开发！</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496301.html" target="_blank" rel="noopener" data-cat="keji" data-summary="覆盖MaaS、Agent服务、行业AI解决方案" data-title="阿里千问AI平台全面升级模型服务、Agent服务、AI应用" data-date="09-23 13:13" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-23 13:13</span>
          <span class="news-item-title">阿里千问AI平台全面升级模型服务、Agent服务、AI应用</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496170.html" target="_blank" rel="noopener" data-cat="keji" data-summary="下半场开始了" data-title="GPT-6 Astra搓3D刷屏后，3D生成的竞争规则变了" data-date="09-23 13:01" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-23 13:01</span>
          <span class="news-item-title">GPT-6 Astra搓3D刷屏后，3D生成的竞争规则变了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496221.html" target="_blank" rel="noopener" data-cat="keji" data-summary="缓存读取价砍了60%" data-title="Claude Opus 5.5突袭！68万行代码一天迁完，API价格打8折" data-date="09-23 12:59" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-23 12:59</span>
          <span class="news-item-title">Claude Opus 5.5突袭！68万行代码一天迁完，API价格打8折</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/22/were-already-fighting-yesterdays-battle-greeces-prime-minister-gets-candid-about-ai/" target="_blank" rel="noopener" data-cat="keji" data-summary="大多数贸易代表团的领导人坚持说话，但当我本周采访希腊总理基里亚科斯·米佐塔基斯（ Kyriakos Mitsotakis ）时，他也承认没有政府准备好接受人工智能即将要做的事情。" data-title="“我们已经在打昨天的仗了” ：希腊总理对人工智能直言不讳" data-date="09-23 12:59" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-23 12:59</span>
          <span class="news-item-title">“我们已经在打昨天的仗了” ：希腊总理对人工智能直言不讳</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496129.html" target="_blank" rel="noopener" data-cat="keji" data-summary="押注互联网里的人类经验" data-title="刷视频也能教会机器人干活！1200亿tokens人类动作预训练，误差按幂律下降" data-date="09-23 12:25" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-23 12:25</span>
          <span class="news-item-title">刷视频也能教会机器人干活！1200亿tokens人类动作预训练，误差按幂律下降</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/999167/openai-elite-mathematicians-panel" target="_blank" rel="noopener" data-cat="keji" data-summary="在将一系列引人注目的数学结果转化为声誉危机之后， OpenAI正在咨询人类数学家，以帮助其找到一条不那么灾难性的前进道路。周一，该公司宣布了一个新的独立数学家小组，其任务是就其与数学研究和更广泛的人工智能公司的互动向其和其他人工智能公司提供建议。" data-title="OpenAI希望咨询精英数学家，了解如何不再摸索" data-date="09-23 08:17" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-23 08:17</span>
          <span class="news-item-title">OpenAI希望咨询精英数学家，了解如何不再摸索</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/22/techcrunch-founder-summits-agenda-revealed-unlock-fundraising-hiring-and-ai-insights-in-boston-on-november-4/" target="_blank" rel="noopener" data-cat="keji" data-summary="创始人不应该以最艰难的方式学习最艰难的教训。TechCrunch创始人峰会旨在使创办公司的挑战更容易，更高的挑战也更大。" data-title="TechCrunch创始人峰会的议程揭晓： 11月4日在波士顿解锁筹款、招聘和人工智能洞察" data-date="09-23 07:21" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-23 07:21</span>
          <span class="news-item-title">TechCrunch创始人峰会的议程揭晓： 11月4日在波士顿解锁筹款、招聘和人工智能洞察</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/22/snorkel-ai-triples-valuation-to-3-5b-as-demand-for-ai-training-data-booms/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家拥有七年历史的初创公司已经筹集了3.5亿美元的E轮融资，以推动其数据即服务的方法。" data-title="随着人工智能培训数据需求激增，浮潜人工智能将估值提高三倍至35亿美元（ $ 35亿）" data-date="09-23 05:56" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-23 05:56</span>
          <span class="news-item-title">随着人工智能培训数据需求激增，浮潜人工智能将估值提高三倍至35亿美元（ $ 35亿）</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/999094/rabbit-ai-agent-os3" target="_blank" rel="noopener" data-cat="keji" data-summary="正如《连线》杂志早些时候报道的那样， Rabbit公司正在推出一款独立的人工智能代理，不需要其硬件即可使用。这家初创公司表示，其新的OS3 “代理操作系统”在云中运行，但在Windows、Mac和Linux设备上本地运行。根据Rabbit的说法，您可以[…]" data-title="Rabbit的新AI agent不需要R1就可以运行" data-date="09-23 04:52" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-23 04:52</span>
          <span class="news-item-title">Rabbit的新AI agent不需要R1就可以运行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/22/qualcomm-launches-two-new-smartphone-chips-with-emphasis-on-ai/" target="_blank" rel="noopener" data-cat="keji" data-summary="高通表示，其新的顶级芯片可以在本地运行30B混合专家模型。" data-title="高通推出两款以人工智能为重点的新型智能手机芯片" data-date="09-23 04:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-23 04:00</span>
          <span class="news-item-title">高通推出两款以人工智能为重点的新型智能手机芯片</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">3 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck7v4y7jv182o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="哪些英超球队表现优异，哪些球队表现不佳？" data-title="英超球队是如何真正开始的" data-date="09-23 14:22" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-23 14:22</span>
          <span class="news-item-title">英超球队是如何真正开始的</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701757.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网三亚9月22日电 (高凯 黄翔)2026华语辩论世界杯名校邀请赛(三亚站)日前在海南三亚落幕。经过角逐，中国政法大学夺得冠军，这是该校首次获得华语辩论世界杯系列赛事冠军。" data-title="2026华语辩论世界杯名校邀请赛（三亚站）落幕" data-date="09-22 21:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 21:55</span>
          <span class="news-item-title">2026华语辩论世界杯名校邀请赛（三亚站）落幕</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckd68e40ze3jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔同意与英超冠军阿森纳签订一份经过改进的新合同。" data-title="阿尔特塔同意与阿森纳冠军达成新协议" data-date="09-22 19:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 19:48</span>
          <span class="news-item-title">阿尔特塔同意与阿森纳冠军达成新协议</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c69v9207z2vwo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果你花一天时间在东京观光，可能会发现自己一路拿着空咖啡杯、7-Eleven蛋三明治的包装纸，以及愈来愈强烈的困惑感。日本以重视整洁闻名，那么，为什么却找不到地方丢垃圾呢？" data-title="日本以街道整洁无瑕而闻名，但为什么公共垃圾桶却如此难找？" data-date="09-23 14:50" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-23 14:50</span>
          <span class="news-item-title">日本以街道整洁无瑕而闻名，但为什么公共垃圾桶却如此难找？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-23/10702175.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="金秋时节，五谷丰登，田野间处处洋溢着丰收的喜悦。" data-title="学习新语｜跟着总书记一起话丰收" data-date="09-23 14:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:49</span>
          <span class="news-item-title">学习新语｜跟着总书记一起话丰收</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/244.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 23 日消息，据央视新闻报道，9 月 22 日至 24 日，“FAST 落成十周年学术交流会”在贵州省平塘县举办。2016 年 9 月 25 日，500 米口径球面射电望远镜 FAST 在贵州落成启用。报道称，FAST 启用至今已取得一系列具有标志性意义的创新成果，在工程技术、前沿科学、应用等领域均取得多项成就。在测量与控制技术方法、国产化钢丝绳和高性能接收机研制等方面的技术创新，保障了望远镜的稳定高效运行。在脉冲星、中性氢星系、快速射电暴和引力波研究中取得一系列具有国际影响力的科学成果，已成为全球最重要的天文观测设备之一。在地月空间目标探测、脉冲星时间基准以及小行星防御等应用领域取得重要进展，服务于国家空天安全和重大战略需求。截至目前，基于 FAST 观测数据，科学家们已" data-title="“中国天眼”FAST 落成启用十年，将继续推进 FAST 二期工程" data-date="09-23 14:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-23 14:42</span>
          <span class="news-item-title">“中国天眼”FAST 落成启用十年，将继续推进 FAST 二期工程</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702228.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网郑州9月23日电 (刘鹏杨震)记者23日从中国铁路郑州局集团有限公司(以下简称“国铁集团郑州局”)获悉，2026年铁路中秋国庆假期运输自当日启动，至10月8日结束，为期16天，国铁集团郑州局预计发送旅客1200万人次，日均发送旅客75万人次。其间，计划开行北上广深等多个方向夜间高铁61列，方便旅客多时段错峰出行。" data-title="国铁郑州局“双节”假期将开行61列多方向夜间高铁" data-date="09-23 14:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:38</span>
          <span class="news-item-title">国铁郑州局“双节”假期将开行61列多方向夜间高铁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-23/10702213.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月23日电 据日本广播协会(NHK)23日报道，受今年第25号台风“杜鹃”带来的强降雨影响，日本千叶县和神奈川县发生山体滑坡及河流泛滥等灾害，目前已造成9人死亡，4人失踪。" data-title="台风“杜鹃”致日本9人死亡4人失踪 超2万户家庭停电" data-date="09-23 14:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:37</span>
          <span class="news-item-title">台风“杜鹃”致日本9人死亡4人失踪 超2万户家庭停电</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/243.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 23 日消息，小米刚刚官宣了小米 18 Pro 系列手机的“one more thing”，官方微博配文称上次相见还是 6 年前。今晚，还有点特别的上一次相见，还是 6 年前今晚 7 点见IT之家注意到，小米官方微博的配图，展示了小米 18 Pro 的透明机身。值得一提的是，小米此前最后一款采用透明机身设计的手机 —— 小米 10 Ultra 至尊纪念版 透明版发布于 2020 年 8 月。结合此次官方的预热来看，小米 18 Pro 系列有望带回透明后盖设计。作为参考，小米截至目前已发布三款透明探索版手机，分别是：小米 8 透明探索版小米 9 透明尊享版小米 10 Ultra 至尊纪念版 透明版▲ IT之家开箱：小米 8 透明探索版图赏据IT之家今日早些时候报道，在 202" data-title="小米 18 Pro 系列手机“one more thing”官宣，透明探索版有望回归" data-date="09-23 14:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-23 14:36</span>
          <span class="news-item-title">小米 18 Pro 系列手机“one more thing”官宣，透明探索版有望回归</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702203.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月23日电 (记者 陈杭 徐婧)22日至23日，2026北京文化论坛在北京举办。来自多个国家的与会嘉宾22日晚共乘铛铛车，游览正阳门等古都之脊的文化遗产，体验壮美有序、古今交融的城市画卷。" data-title="乘铛铛车漫游北京中轴线 多国人士同览“古都之脊”" data-date="09-23 14:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:35</span>
          <span class="news-item-title">乘铛铛车漫游北京中轴线 多国人士同览“古都之脊”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702193.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网桂林9月23日电 题：广西酒海井下忠骨还 新圩战地薪火传" data-title="（长征胜利90周年）广西酒海井下忠骨还 新圩战地薪火传" data-date="09-23 14:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:31</span>
          <span class="news-item-title">（长征胜利90周年）广西酒海井下忠骨还 新圩战地薪火传</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702198.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网甘肃武威9月23日电 (记者 李亚龙)9月22日晚，甘肃省2026年“我们的节日·中秋”省级主场活动在武威市启幕。该活动以“月出凉州·诗照团圆”为主题，立足“五凉京华、河西都会”深厚历史底蕴，把诗词文脉、丝路非遗与民俗烟火相融，为民众奉上一场为期多日的沉浸式中秋文化盛宴，以传统佳节为媒迎中秋、国庆双节到来。" data-title="甘肃武威办中秋盛宴：千年古诗词邂逅月饼“大观园”" data-date="09-23 14:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:29</span>
          <span class="news-item-title">甘肃武威办中秋盛宴：千年古诗词邂逅月饼“大观园”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702192.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南京9月23日电 (胡晓炜)中国铁路上海局集团有限公司23日公布，长三角史上最长、为期16天的中秋国庆假期运输当日启动，假期运输期间，长三角铁路预计发送旅客5400万人次。" data-title="长三角铁路2026年中秋国庆假期运输启动 为期16天为史上最长" data-date="09-23 14:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:18</span>
          <span class="news-item-title">长三角铁路2026年中秋国庆假期运输启动 为期16天为史上最长</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702172.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网延边9月23日电 (高龙安 李彦国)金色的稻浪映着湛蓝的天空，是秋季海兰江畔最美的色彩。田与天的交汇处，是一排排青瓦白墙、飞檐翘角的朝鲜族民居。" data-title="稻浪长鼓引客来 吉林朝鲜族村落文旅融合促共富" data-date="09-23 14:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 14:00</span>
          <span class="news-item-title">稻浪长鼓引客来 吉林朝鲜族村落文旅融合促共富</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702128.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网中山9月23日电 (记者 蔡敏婕)记者22日从中山市人民政府获悉，“广货行天下·中山百货进成都”活动当天启动，现场发布中山南洋风情旅游周活动信息。" data-title="广东中山好物登陆蓉城  “南洋风情旅游周” 国庆亮相" data-date="09-23 13:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 13:54</span>
          <span class="news-item-title">广东中山好物登陆蓉城  “南洋风情旅游周” 国庆亮相</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-23/10702122.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月23日电 (记者 孙自法)施普林格·自然旗下学术期刊《自然-通讯》最新发表一篇演化研究论文称，一项建模研究表明，能够维持所谓“RNA世界”(RNA World)这一假定早期生命阶段的环境条件，可能在约43.3亿年前趋于稳定。" data-title="地球生命何时出现？最新研究称约43.3亿年前“RNA世界”趋于稳定" data-date="09-23 13:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 13:47</span>
          <span class="news-item-title">地球生命何时出现？最新研究称约43.3亿年前“RNA世界”趋于稳定</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-23/10702121.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月23日电 据美联社报道，飓风“保罗”(Polo)当地时间9月22日在墨西哥西南近海的东太平洋增强为五级飓风。预报称，风暴将给墨西哥西南部带来强降雨，但不会登陆。" data-title="“保罗”在墨西哥太平洋沿岸附近增强为五级飓风" data-date="09-23 13:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-23 13:26</span>
          <span class="news-item-title">“保罗”在墨西哥太平洋沿岸附近增强为五级飓风</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/politics/supreme-court-missouri-congressional-map.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="联邦上诉法院支持共和党人寻求利用去年重新划定的地区边界，让共和党在即将到来的中期选举中占据优势。" data-title="对密苏里州国会地图的争议再次回到最高法院" data-date="09-23 11:59" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-23 11:59</span>
          <span class="news-item-title">对密苏里州国会地图的争议再次回到最高法院</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-23 14:51（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
