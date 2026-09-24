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
      <span>2026-09-24 14:51 抓取更新</span>
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
        <span class="channel-count">6</span>
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
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/09/23/business/media/cnn-ms-now-politico-white-house-trump-ban-ruling.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="法官蒂莫西· J ·凯利（ Timothy J. Kelly ）发布了临时限制令，并告诉白宫立即恢复三家新闻媒体员工的新闻证书。" data-title="法院阻止特朗普对CNN、MS NOW和Politico的白宫禁令" data-date="09-24 14:45" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 09-24 14:45</span>
      </div>
      <h2 class="hero-featured-title">法院阻止特朗普对CNN、MS NOW和Politico的白宫禁令</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/006/785.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 24 日消息，小米智能摄像机 5 Pro 全彩夜视现已在小米有品开启众筹，活动时间为 9 月 23 日 10 点-9 月 30 日 10 点，众筹价 429 元（点击前往）。作为小米首款全彩夜视室内摄像机，新品配备 8MP+4MP 双镜头协同，可拍摄 4K 高清画面，支持多种夜视模式，满足不同场景使用需求。IT之家从商品页面获悉，新品可开启机身小夜灯进行补光，摄像机可实现整夜彩色成像。无人时黑白成像，识别到人自动开启小夜灯并自动切换彩色画面。内置 940nm 红外补光灯，镜头无红曝干扰，夜间呈现清晰黑白影像。新品采用独特外观结构，内置柔光小夜灯。夜间识别人形、宠物自动柔和亮灯；定制光学透镜搭配磨砂透光面，光线匀散不刺眼，兼顾看护与夜间微光照明。新品搭载 1.5T 高算力芯片" data-title="小米首款全彩夜视室内摄像机开启众筹：4K 超清、AI 检测，429 元" data-date="09-24 14:49" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">小米首款全彩夜视室内摄像机开启众筹：4K 超清、AI 检测，429 元</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/crd68ev059y8o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育专栏作家托尼·普利斯（ Tony Pulis ）解释了不同的因素，这意味着热刺老板罗伯托·德·泽比（ Roberto de Zerbi ）需要时间和他的球员一起打造一支" data-title="为什么这次休息对De Zerbi &amp; Spurs来说是最糟糕的时刻" data-date="09-24 13:37" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">为什么这次休息对De Zerbi & Spurs来说是最糟糕的时刻</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/006/788.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 24 日消息，微星 (MSI) 现已在电商平台销售便携显示器 PRO MP161E6，到手价低至 659 元。PRO MP161E6 采用一块 15.6&quot; 的 FHD 60Hz IPS LCD 面板，亮度 250nits，静态对比度 1000:1，色深 6bit+FRC，色域 45.1% sRGB，支持防闪烁、减蓝光、防眩光。其提供 2 个全功能 USB-C、1 个 Mini HDMI 1.4b，集成 2 个 1W 扬声器，支持 0~180° 开合调节，提供 1/4&quot; 三脚架接口，兼容 75×75 (mm) 的 VESA 壁挂规范。京东微星 PRO MP161E6 便携显示器 659 元直达链接" data-title="微星便携显示器 PRO MP161E6 上架：15.6&quot; FHD 60Hz 低色域，659 元" data-date="09-24 14:52" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">微星便携显示器 PRO MP161E6 上架：15.6" FHD 60Hz 低色域，659 元</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/09/23/business/media/cnn-ms-now-politico-white-house-trump-ban-ruling.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="法官蒂莫西· J ·凯利（ Timothy J. Kelly ）发布了临时限制令，并告诉白宫立即恢复三家新闻媒体员工的新闻证书。" data-title="法院阻止特朗普对CNN、MS NOW和Politico的白宫禁令" data-date="09-24 14:45" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-24 14:45</span>
          <span class="news-item-title">法院阻止特朗普对CNN、MS NOW和Politico的白宫禁令</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-24/10702941.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【中亚专线】中哈媒体圆桌会在阿拉木图举行 探讨数智时代新闻合作" data-title="中哈媒体圆桌会在阿拉木图举行 探讨数智时代新闻合作" data-date="09-24 14:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 14:13</span>
          <span class="news-item-title">中哈媒体圆桌会在阿拉木图举行 探讨数智时代新闻合作</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cjzxze5peg76o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="BBC中文整理，习近平抵达华盛顿一刻，外界关注的重点看点：谁是习近平访美团成员？美国共和党及人民对中国的态度为何？" data-title="习近平访美首日看点：谁同行？第一夫人角色？高规格接待引反弹？" data-date="09-24 13:12" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 13:12</span>
          <span class="news-item-title">习近平访美首日看点：谁同行？第一夫人角色？高规格接待引反弹？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-24/10702873.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宜春9月24日电(记者 刘力鑫)23日晚，“寻美江西 泉月宜春”暨网络人士共创大会在江西宜春启动，来自全国各地的百余名网络人士齐聚明月山，将在为期3天的时间里，展开面对面交流和采风创作。" data-title="百余名网络人士齐聚明月山 开启“寻美江西 泉月宜春”共创之旅" data-date="09-24 12:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 12:50</span>
          <span class="news-item-title">百余名网络人士齐聚明月山 开启“寻美江西 泉月宜春”共创之旅</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/23/us/politics/mary-peltola-alaska-senate-race.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Democrats hope that Mary Peltola can flip a Republican Senate seat in Alaska. Former aides describe a campaign and congressional office marked by chaos." data-title="玛丽·佩尔托拉（ Mary Peltola ）在阿拉斯加州的参议院竞选活动受到愤怒爆发和诽谤的震撼" data-date="09-24 11:24" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-24 11:24</span>
          <span class="news-item-title">玛丽·佩尔托拉（ Mary Peltola ）在阿拉斯加州的参议院竞选活动受到愤怒爆发和诽谤的震撼</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-24/10702841.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网约翰内斯堡9月24日电(记者 孙翔)南非代理国家警察总监普伦·迪姆帕内(Puleng Dimpane)23日指示夸祖卢-纳塔尔省(简称夸纳省)警察总监立即启动为期72小时的追捕行动，搜捕涉嫌枪杀11人的3名男子。" data-title="南非夸纳省枪击事件致11人死亡  警方启动72小时追捕行动" data-date="09-24 10:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 10:56</span>
          <span class="news-item-title">南非夸纳省枪击事件致11人死亡  警方启动72小时追捕行动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-24/10702777.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网金边9月24日电 (杨强 张堰林)当地时间9月23日，在顺利完结柬埔寨磅士卑省消除白内障致盲项目后，中国香港共享基金会与合作医疗团队转移至磅通省开展新一站免费白内障手术任务。" data-title="香港共享基金会柬埔寨消除白内障致盲项目向磅通省推展" data-date="09-24 10:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 10:11</span>
          <span class="news-item-title">香港共享基金会柬埔寨消除白内障致盲项目向磅通省推展</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/23/us/politics/des-moines-register-trump-lawsuit.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该诉讼挑战了一项民意调查，该民意调查显示特朗普在2024年比赛的最后几周落后于卡马拉·哈里斯。一名法官警告说，类似的法律挑战可能会对新闻报道产生寒蝉效应。" data-title="爱荷华州法官驳回特朗普对得梅因登记处的诉讼" data-date="09-24 10:07" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-24 10:07</span>
          <span class="news-item-title">爱荷华州法官驳回特朗普对得梅因登记处的诉讼</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-24/10702797.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月24日电 综合消息：也门胡塞武装当地时间23日表示，9月11日至21日，共有408艘商船通过曼德海峡，这一数字高于本月1日至10日期间记录的393艘商船。" data-title="也门胡塞武装称近期超400艘商船通过曼德海峡" data-date="09-24 10:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 10:04</span>
          <span class="news-item-title">也门胡塞武装称近期超400艘商船通过曼德海峡</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/23/us/politics/timothy-mellon-republicans-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Timothy Mellon, one of the party’s biggest donors in 2024, has so far withheld his midterm donations for Republican senators because he is unhappy about the failure to pass a key Trump priority." data-title="Timothy Mellon, a G.O.P. Billionaire, Pulls Back His Money From Senate Republicans" data-date="09-24 09:42" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-24 09:42</span>
          <span class="news-item-title">Timothy Mellon, a G.O.P. Billionaire, Pulls Back His Money From Senate Republicans</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx980mjemv73o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国总统亲赴机场迎接外国元首极为罕见。若不计教宗访美的特例，这将是超过 60 年来美国总统首次以这种方式迎接他国元首。" data-title="习近平抵美，特朗普罕有接机" data-date="09-24 07:46" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 07:46</span>
          <span class="news-item-title">习近平抵美，特朗普罕有接机</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-24/10702709.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社联合国9月23日电(记者 王帆)伊朗总统佩泽希齐扬23日在纽约联合国总部举行的第81届联大一般性辩论上发言表示，伊朗始终致力于对话谈判，但面对武力威胁绝不会屈膝投降。" data-title="伊朗总统联大发言：致力对话谈判，绝不屈膝投降" data-date="09-24 07:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 07:25</span>
          <span class="news-item-title">伊朗总统联大发言：致力对话谈判，绝不屈膝投降</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-24/10702704.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月24日电 综合外媒报道，伊朗总统佩泽希齐扬当地时间23日在联合国大会一般性辩论发言中表示，伊朗“永不低头、也不会屈膝投降”，并呼吁各国共同努力实现和平。" data-title="伊朗总统在联大演讲 誓言“永不屈膝投降”" data-date="09-24 06:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 06:54</span>
          <span class="news-item-title">伊朗总统在联大演讲 誓言“永不屈膝投降”</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwp847n9n7m2o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="分析人士指，北京可能推动德黑兰重启谈判，但不太可能停止购买伊朗石油。" data-title="中国希望伊朗战争结束，但不是以特朗普想要的方式" data-date="09-24 06:52" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 06:52</span>
          <span class="news-item-title">中国希望伊朗战争结束，但不是以特朗普想要的方式</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/23/us/politics/trump-xi-china-visit.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="尽管美国和中国之间存在竞争，但特朗普总统一再想方设法让中国国家主席习近平获得通行证，将他描绘成私人朋友而不是竞争对手。" data-title="当习近平访问华盛顿时，特朗普贬低中国对美国利益的行动" data-date="09-24 05:14" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-24 05:14</span>
          <span class="news-item-title">当习近平访问华盛顿时，特朗普贬低中国对美国利益的行动</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/006/785.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 24 日消息，小米智能摄像机 5 Pro 全彩夜视现已在小米有品开启众筹，活动时间为 9 月 23 日 10 点-9 月 30 日 10 点，众筹价 429 元（点击前往）。作为小米首款全彩夜视室内摄像机，新品配备 8MP+4MP 双镜头协同，可拍摄 4K 高清画面，支持多种夜视模式，满足不同场景使用需求。IT之家从商品页面获悉，新品可开启机身小夜灯进行补光，摄像机可实现整夜彩色成像。无人时黑白成像，识别到人自动开启小夜灯并自动切换彩色画面。内置 940nm 红外补光灯，镜头无红曝干扰，夜间呈现清晰黑白影像。新品采用独特外观结构，内置柔光小夜灯。夜间识别人形、宠物自动柔和亮灯；定制光学透镜搭配磨砂透光面，光线匀散不刺眼，兼顾看护与夜间微光照明。新品搭载 1.5T 高算力芯片" data-title="小米首款全彩夜视室内摄像机开启众筹：4K 超清、AI 检测，429 元" data-date="09-24 14:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-24 14:49</span>
          <span class="news-item-title">小米首款全彩夜视室内摄像机开启众筹：4K 超清、AI 检测，429 元</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq39me0emplyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI在事发后两个月才察觉事件，并迟至本月中，才用一般电邮的方式通知澳洲政府。澳洲政府形容事件令人震惊，批评OpenAI的处理手法“不可接受”。" data-title="OpenAI智能体入侵澳洲政府网站窃取资料 官方两月后才发觉" data-date="09-24 14:35" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 14:35</span>
          <span class="news-item-title">OpenAI智能体入侵澳洲政府网站窃取资料 官方两月后才发觉</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496779.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Stripe Managed Payments (SMP) 现已全面上线" data-title="Stripe Tour 中国首秀：构建 AI 经济基础设施，赋能全球商业增长" data-date="09-24 13:46" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-24 13:46</span>
          <span class="news-item-title">Stripe Tour 中国首秀：构建 AI 经济基础设施，赋能全球商业增长</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496778.html" target="_blank" rel="noopener" data-cat="keji" data-summary="专治人机动作对不齐" data-title="教机器人干活，光“刷课时”可不够！灵初这次较真数据质量" data-date="09-24 13:45" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-24 13:45</span>
          <span class="news-item-title">教机器人干活，光“刷课时”可不够！灵初这次较真数据质量</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496767.html" target="_blank" rel="noopener" data-cat="keji" data-summary="开源一座具身智能的新“塔台”" data-title="5分钟完成机器人纳管、10秒启动跨集群任务，清华大学联合无问芯穹开源具身智能云原生平台RLark" data-date="09-24 13:19" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-24 13:19</span>
          <span class="news-item-title">5分钟完成机器人纳管、10秒启动跨集群任务，清华大学联合无问芯穹开源具身智能云原生平台RLark</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496740.html" target="_blank" rel="noopener" data-cat="keji" data-summary="懂出海，能记忆，自进化" data-title="出海Agent“小元AI”入驻腾讯WorkBuddy：找买家写开发信谈生意" data-date="09-24 12:11" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-24 12:11</span>
          <span class="news-item-title">出海Agent“小元AI”入驻腾讯WorkBuddy：找买家写开发信谈生意</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496658.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月23日，2026海信电视秋季新品发布会上，定位“原生真彩，性能旗舰”的RGB-Mini LED新品E7S Pro+正式发布" data-title="海信新一代性能旗舰E7S Pro+正式发布，原生真彩再进阶" data-date="09-24 10:51" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-24 10:51</span>
          <span class="news-item-title">海信新一代性能旗舰E7S Pro+正式发布，原生真彩再进阶</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/496647.html" target="_blank" rel="noopener" data-cat="keji" data-summary="美国也开启了全民养虾狂潮" data-title="Meta靠自研Manus翻身！股价一夜暴涨11%，登顶苹果商店，增速反超ChatGPT" data-date="09-24 10:23" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-24 10:23</span>
          <span class="news-item-title">Meta靠自研Manus翻身！股价一夜暴涨11%，登顶苹果商店，增速反超ChatGPT</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/" target="_blank" rel="noopener" data-cat="keji" data-summary="首席执行官马克·扎克伯格(Mark Zuckerberg)周三在门洛帕克(Menlo Park)拉开了公司年度Connect活动的序幕，发表了一篇主题演讲，明确表达了一件事情： Meta正在全力投入Muse。它甚至出现在Meta的人工智能眼镜上。" data-title="Meta的人工智能代理Muse即将推出的所有新功能" data-date="09-24 09:13" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-24 09:13</span>
          <span class="news-item-title">Meta的人工智能代理Muse即将推出的所有新功能</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c9kgv31pg8eeo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="美国与中国正争夺人工智能领先地位，同时寻求确保这项技术仍在人类掌控之中。" data-title="习近平访美晤特朗普：中美AI超级强国的雄心成为焦点" data-date="09-24 07:30" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 07:30</span>
          <span class="news-item-title">习近平访美晤特朗普：中美AI超级强国的雄心成为焦点</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/998480/meta-connect-2026-biggest-news-announcements" target="_blank" rel="noopener" data-cat="keji" data-summary="现在是该公司年度产品发布会Meta Connect的时候了。今年，鉴于该公司主要关注人工智能和智能眼镜等可穿戴设备，我们很可能会看到首席执行官马克·扎克伯格(Mark Zuckerberg)及其团队对这些类别的更新。该公司一直面临严格的审查，因为一些用户[…]" data-title="Meta Connect 2026 ：重大新闻和公告" data-date="09-24 06:45" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-24 06:45</span>
          <span class="news-item-title">Meta Connect 2026 ：重大新闻和公告</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/23/anthropic-says-its-biology-lab-has-already-found-something-big/" target="_blank" rel="noopener" data-cat="keji" data-summary="但也许最大的启示是， Anthropic并没有让Claude在其生物学实验室中逍遥法外。到目前为止，人类仍然处于循环中。" data-title="Anthropic表示，其生物实验室已经发现了一些重要的东西，" data-date="09-24 06:17" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-24 06:17</span>
          <span class="news-item-title">Anthropic表示，其生物实验室已经发现了一些重要的东西，</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/23/enveda-secures-311m-to-bring-more-nature-derived-ai-drugs-into-clinical-trials/" target="_blank" rel="noopener" data-cat="keji" data-summary="这轮融资对AI生物技术的估值为20 $。它目前正在测试治疗皮肤病并在停止GLP-1s后保持体重的药物。" data-title="Enveda获得3.11亿美元，用于将更多自然衍生的人工智能药物纳入临床试验" data-date="09-24 03:31" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-24 03:31</span>
          <span class="news-item-title">Enveda获得3.11亿美元，用于将更多自然衍生的人工智能药物纳入临床试验</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/23/chatgpt-mobile-app-gets-voice-based-agentic-features/" target="_blank" rel="noopener" data-cat="keji" data-summary="Pro和Plus用户将能够使用手机上的“工作”选项卡来完成代理任务。" data-title="ChatGPT移动应用获得基于语音的代理功能" data-date="09-24 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-24 01:00</span>
          <span class="news-item-title">ChatGPT移动应用获得基于语音的代理功能</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/23/even-americans-who-use-ai-every-day-are-worried-about-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="该报告表明，更大的曝光率不会解决围绕该技术的不安，也不会减少公众对人工智能监管的支持。" data-title="即使是每天使用人工智能的美国人也对此感到担忧" data-date="09-24 00:49" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-24 00:49</span>
          <span class="news-item-title">即使是每天使用人工智能的美国人也对此感到担忧</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">6 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crd68ev059y8o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育专栏作家托尼·普利斯（ Tony Pulis ）解释了不同的因素，这意味着热刺老板罗伯托·德·泽比（ Roberto de Zerbi ）需要时间和他的球员一起打造一支" data-title="为什么这次休息对De Zerbi &amp; Spurs来说是最糟糕的时刻" data-date="09-24 13:37" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 13:37</span>
          <span class="news-item-title">为什么这次休息对De Zerbi & Spurs来说是最糟糕的时刻</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5evwlmdmy00o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尽管吉姆·拉特克利夫爵士（ Sir Jim Ratcliffe ）采取了广泛的成本削减措施，但曼联的总债务仍超过10亿英镑，俱乐部还确认已花费6350万英镑购买新体育场的土地。" data-title="曼联仍有10亿英镑的债务，其中6350万英镑用于新体育场" data-date="09-23 22:10" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-23 22:10</span>
          <span class="news-item-title">曼联仍有10亿英镑的债务，其中6350万英镑用于新体育场</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/23/florian-wirtz-liverpool-playmaker-opta" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这位23岁的组织者对利物浦一直很失望，但他真的那么糟糕吗？ Opta分析师Florian Wirtz在2025年夏天签约利物浦时，只有一个合乎逻辑的假设。当时的英超冠军招募了世界足球界最热门的年轻球员之一–拜耳勒沃库森队的关键球员，他在2023-24赛季赢得了双冠王，并在德国队中成为明星。一个令人兴奋的和生产" data-title="弗洛里安·维尔茨看起来不像是£ 1.16亿的球员，但现在注销他还为时过早" data-date="09-23 21:33" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-23 21:33</span>
          <span class="news-item-title">弗洛里安·维尔茨看起来不像是£ 1.16亿的球员，但现在注销他还为时过早</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/23/chelsea-sale-american-sports-capitalism" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="蓝军缺乏成功并不妨碍Todd Boehly和Mark Walter从俱乐部出售中收回利润。这就是切尔西足球俱乐部在历史学家可能选择隆重称呼第一清湖时代或Boehly Bungle期间所取得的成就。自2022年5月从受制裁的俄罗斯寡头Roman Abramovich手中购买俱乐部以来，托德·博伊利（ Todd Boehly ）接管了" data-title="切尔西已进入美国体育资本主义后期| Leander Schaerlaeckens" data-date="09-23 21:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-23 21:16</span>
          <span class="news-item-title">切尔西已进入美国体育资本主义后期| Leander Schaerlaeckens</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/23/summer-football-transfer-window-best-value-deals" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从经验丰富的前锋到令人兴奋的年轻人才，这里有10名签约球员可以证明他们的新球队可以讨价还价，即使在这个无情的转会膨胀时代，超过2000万英镑的费用通常也不代表讨价还价。不过，罗马对波尔图组织者莫拉的转会可能是个例外。现年19岁的他自15岁时为波尔图的B队主演以来一直在欧洲精英球队的雷达上，波尔图为他的7000万欧元（ 5950万英镑）的发行做好了准备。" data-title="今年夏季转会窗口的十大超值优惠" data-date="09-23 19:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-23 19:25</span>
          <span class="news-item-title">今年夏季转会窗口的十大超值优惠</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/23/premier-league-season-ticket-holders-pecking-order-new-fans-football-tourists" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="它是球迷和俱乐部之间联系的象征，但人们越来越担心高管们会更喜欢挤满一次性游客的体育场馆。这份被称为“世界上最古老的足球季票”的文件承诺，其持有者可以参加1884-85赛季的每一场伯恩利主场比赛。这是一张比足球联赛早四年的门票，所有比赛都与东兰开夏郡的邻居比赛。尽管如此，传说" data-title="滑开：足球赛季门票持有者害怕摔倒啄食顺序" data-date="09-23 19:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-23 19:00</span>
          <span class="news-item-title">滑开：足球赛季门票持有者害怕摔倒啄食顺序</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/006/788.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 24 日消息，微星 (MSI) 现已在电商平台销售便携显示器 PRO MP161E6，到手价低至 659 元。PRO MP161E6 采用一块 15.6&quot; 的 FHD 60Hz IPS LCD 面板，亮度 250nits，静态对比度 1000:1，色深 6bit+FRC，色域 45.1% sRGB，支持防闪烁、减蓝光、防眩光。其提供 2 个全功能 USB-C、1 个 Mini HDMI 1.4b，集成 2 个 1W 扬声器，支持 0~180° 开合调节，提供 1/4&quot; 三脚架接口，兼容 75×75 (mm) 的 VESA 壁挂规范。京东微星 PRO MP161E6 便携显示器 659 元直达链接" data-title="微星便携显示器 PRO MP161E6 上架：15.6&quot; FHD 60Hz 低色域，659 元" data-date="09-24 14:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-24 14:52</span>
          <span class="news-item-title">微星便携显示器 PRO MP161E6 上架：15.6" FHD 60Hz 低色域，659 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/787.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 24 日消息，科技媒体 Ars Technica 今天（9 月 24 日）发布博文，报道称宾利（Bentley）正式发布其首款纯电动车型 Torcal，该车将作为 2028 款车型于 2027 年年初上市。Torcal 车身尺寸小于添越（Bentayga），吸收 EXP 15 概念车的部分设计元素，前脸最具辨识度的是“悬浮钻石格栅”（Floating Diamond Grille），宾利用 76 颗手工装配的水晶状菱形元素，置于透明聚碳酸酯面板后方，并在解锁时呈现渐变点亮的欢迎灯效。车身侧面强调“长轴距、短前后悬、骄傲的前脸比例”，形成直立而优雅的姿态；腰线干净，减少多余折线，让光影在车身上流动来塑造性格。宾利将其侧面与后轮拱的饱满外扩称为“Resting Beast（静卧" data-title="宾利首款纯电 Torcal 发布：875 马力、零百加速最快 2.9 秒，WLTP 续航 600 公里" data-date="09-24 14:50" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-24 14:50</span>
          <span class="news-item-title">宾利首款纯电 Torcal 发布：875 马力、零百加速最快 2.9 秒，WLTP 续航 600 公里</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/786.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 24 日消息，长城哈弗今天宣布，长城大狗 PLUS 混动版将于 9 月 28 日正式上市，新车延续大狗系列方盒子造型，搭载全新混动系统。IT之家从原报道获悉，该车提供多种前脸设计方案，除保留现款车型格栅样式外，新车新增半封闭式中网饰板版本，部分版本还提供三色点状装饰件。前面的复古圆形大灯得到保留，外扩轮眉搭配铆钉装饰。车身侧面造型与现款基本保持一致，顶部标配车顶行李架和天窗。同时，该车还将搭载 Coffee Pilot 3 Lite 辅助驾驶系统，拥有 4D 毫米波雷达，支持高速、城市 NOA，无需依赖高精地图。该车预计将搭载 1.5T 混动系统，发动机最大功率 115 千瓦。车辆系统综合扭矩可达 670 牛 · 米，零百加速 6.6 秒。配备电控机械牙嵌式差速锁、iTVC" data-title="长城大狗 PLUS 混动版 9 月 28 日上市，两驱版本油耗 5.2L/100km" data-date="09-24 14:49" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-24 14:49</span>
          <span class="news-item-title">长城大狗 PLUS 混动版 9 月 28 日上市，两驱版本油耗 5.2L/100km</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/006/783.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 24 日消息，特斯拉首次开始向北美搭载 HW3 硬件的 Model S 和 Model X 推送 FSD v14.2 Lite。此前，搭载 HW3 的 Model 3 和 Model Y 已于今年 7 月获得 FSD v14 Lite，这是更新后的 FSD 技术栈首次推送至 Model S 和 Model X。此次软件更新随 2026.27.10 和 2026.27.11 版本一同发布，这两个版本也是目前最新的 FSD 更新。不过，特斯拉目前尚未向所有符合条件的车辆推送该更新。现阶段收到更新的 Model S 和 Model X 数量非常少，特斯拉可能希望先确认不会出现严重问题，再进一步扩大推送范围。特斯拉自动驾驶软件负责人埃隆 · 阿肖克（Ashok Elluswamy）" data-title="特斯拉向北美 HW3 版 Model S/X 推送 FSD v14.2 Lite" data-date="09-24 14:46" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-24 14:46</span>
          <span class="news-item-title">特斯拉向北美 HW3 版 Model S/X 推送 FSD v14.2 Lite</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-24/10702954.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网陕西杨凌9月24日电 (记者 张一辰)2026年陕西省农民丰收节体育健身活动23日在杨凌示范区揉谷镇揉谷中心广场举行，活动为期两天。来自陕西全省的85支参赛队伍齐聚此间，现场参与总规模约1500人。" data-title="陕西省农民丰收节体育健身活动启幕 竞技赛场赓续农耕文脉" data-date="09-24 14:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 14:45</span>
          <span class="news-item-title">陕西省农民丰收节体育健身活动启幕 竞技赛场赓续农耕文脉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702939.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月24日电(记者 刁炜)近日，歼-35A官方代号公布：云龙。此举表明歼-35A延续空军命名传统，正式加入新锐云集的“龙”系列国产战斗机家族，与歼-20“威龙”、歼-16“潜龙”、歼-11“应龙”、歼-10“猛龙”共同构成空军新一代主战装备的剑锋刀刃。" data-title="“空中李云龙”？歼" data-date="09-24 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 14:14</span>
          <span class="news-item-title">“空中李云龙”？歼</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702945.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月24日电 9月24日，国新办就“十五五”时期推进文化和旅游高质量发展有关情况举行新闻发布会。会上，文化和旅游部资源开发司司长满宏卫介绍，“十五五”期间，将在三个方面发力，让更多的人民群众通过旅游体会到获得感、幸福感和安全感。" data-title="文旅部：严厉打击强迫购物、非法网络招徕" data-date="09-24 13:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 13:55</span>
          <span class="news-item-title">文旅部：严厉打击强迫购物、非法网络招徕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702944.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="珠宝加工，考验毫厘之间的手工精度与耐心。从起版到镶嵌、抛光，每一道工序都没有捷径，都需要把工匠精神发挥到极致。" data-title="成品允许误差仅0.02毫米 拆解世赛珠宝加工“盲盒考题”" data-date="09-24 13:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 13:44</span>
          <span class="news-item-title">成品允许误差仅0.02毫米 拆解世赛珠宝加工“盲盒考题”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-24/10702897.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网伦敦9月24日电(记者 欧阳开宇)中秋佳节来临之际，中国驻伦敦旅游办事处携手英国中华餐饮文化协会，23日在伦敦举办“天涯共此时·中国味道”文旅品鉴交流会。活动依托文化和旅游部两大国家级文旅推广品牌，以中秋民俗和中华美食为载体，搭建中英文旅交流与民间友好往来平台。" data-title="“天涯共此时·中国味道”文旅品鉴交流会在伦敦举办" data-date="09-24 13:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 13:08</span>
          <span class="news-item-title">“天涯共此时·中国味道”文旅品鉴交流会在伦敦举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702905.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明9月24日电 (缪超 袁鸿凯 李嘉娴)9月23日是第九个中国农民丰收节，滇池畔花好迎月圆，稻穗翻金浪。当天，来自泰国、老挝、印度、俄罗斯等14个国家的50名青年代表，在云南省昆明市呈贡区与当地农民共享花“漾”秋景，共庆丰收佳节。" data-title="14国青年在滇池之畔与中国农民共享花“漾”秋景共庆丰收佳节" data-date="09-24 13:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 13:05</span>
          <span class="news-item-title">14国青年在滇池之畔与中国农民共享花“漾”秋景共庆丰收佳节</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702903.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网济南9月24日电 题：AI破译地下成矿密码 为金矿“攻深找盲”装上数字引擎" data-title="AI破译地下成矿密码 为金矿“攻深找盲”装上数字引擎" data-date="09-24 13:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 13:00</span>
          <span class="news-item-title">AI破译地下成矿密码 为金矿“攻深找盲”装上数字引擎</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702900.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨9月24日电 (李林)日前，西藏亚东出入境边防检查站立足戍边本职，在亚东县城、仁青岗边贸市场和各边境执勤点位同步开展综合普法宣传活动，以法治力量守护边疆安宁。" data-title="西藏亚东出入境边防检查站开展普法宣传" data-date="09-24 12:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 12:59</span>
          <span class="news-item-title">西藏亚东出入境边防检查站开展普法宣传</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-24/10702866.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网延边9月24日电 (高龙安 李彦国)一手握相机，一手为游客演示摆拍姿势，身材健硕的朝鲜族小伙吴权吉，示范动作透着温婉柔美，游客们被逗得合不拢嘴，笑称摄影师的姿势比女生更有韵味。" data-title="一张写真尽展中华家风：延边文旅出圈厚植民族文脉" data-date="09-24 12:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 12:47</span>
          <span class="news-item-title">一张写真尽展中华家风：延边文旅出圈厚植民族文脉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-24/10702909.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社伦敦9月24日电 (记者 欧阳开宇)当地时间9月23日，英国向中国返还12件流失文物艺术品的交接仪式在中国驻英国使馆举行。中国文化和旅游部副部长、国家文物局局长饶权视频致辞，中国驻英国大使郑泽光，英国伦敦大都会警察厅，英国外交发展部，英国数字、文化、媒体和体育部，欧洲安全与合作组织代表出席仪式。" data-title="英国向中国返还12件流失文物艺术品" data-date="09-24 12:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 12:13</span>
          <span class="news-item-title">英国向中国返还12件流失文物艺术品</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-24/10702852.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月24日电 (记者 周昕)由世界知识出版社主办的“走进中华文明——传承历史·共创未来”主题人文交流活动23日在北京王府学校举办。英国北爱尔兰米尔本小学师生访华团与中方师生相聚校园，同台体验秦腔艺术，在戏曲互动之中探寻文化共鸣。" data-title="中英少年同台以秦腔为桥觅共鸣" data-date="09-24 12:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-24 12:06</span>
          <span class="news-item-title">中英少年同台以秦腔为桥觅共鸣</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-24 14:51（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
