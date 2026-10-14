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
      <span>2026-10-14 14:49 抓取更新</span>
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
        <span class="channel-count">49</span>
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
        <span class="channel-count">4</span>
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
  <div class="ov-item"><span class="ov-num">49</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · IT之家×7</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-14/10714353.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 (记者 刘大炜 李百加)就民进党当局领导人赖清德10日发表的所谓“双十”讲话，国务院台办发言人陈斌华14日在北京举行的国台办例行新闻发布会上强调，这篇讲话充满欺骗性。" data-title="二度回应赖清德今年“双十”讲话 国台办指充满欺骗性" data-date="10-14 14:42" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-14 14:42</span>
      </div>
      <h2 class="hero-featured-title">二度回应赖清德今年“双十”讲话 国台办指充满欺骗性</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/012/861.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，OSAT 龙头日月光半导体 (ASE) 昨日宣布推出基于 PowerSiP 平台的 3D 系统级封装解决方案。这一方案可实现 VRM（电压调节模块）的垂直整合，大幅缩短电流传输路径，降低超半数寄生布线损耗。日月光表示，先进的高性能 AI SoC 功耗已突破 1000W，这意味着需要 1V 以下电压传输超 1000A 的峰值电流，传统的横向架构在电力通过 PCB、封装基板、互连结构到达处理器的过程中可能产生严重的布线损耗。该企业的 PowerSiP 垂直整合工具箱包括夹在无芯基板之间的双面连接电容、具备外露端子的电容阵列模块、4:1 高纵横比铜柱整合技术、单 / 双面模塑高密度主 / 被动元件整合技术。这些技术可解决在空间受限的计算托盘中将电压调节模块配置于" data-title="日月光推出 3D 垂直整合 PowerSiP 解决方案，可减半寄生布线损耗" data-date="10-14 14:46" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">日月光推出 3D 垂直整合 PowerSiP 解决方案，可减半寄生布线损耗</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/13/why-most-manchester-city-fans-stand-by-their-club" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安德鲁·伯顿（ Andrew Burton ）怀疑，如果其他球队取得了类似的成功，球迷们也会原谅他们的主人瑞·肖恩·英格尔（ Re Sean Ingle ）的文章（一些曼城球迷是如何成为一个民族国家政权的积极捍卫者的？ ， 10月5日） ，我暂停" data-title="Why most Manchester City fans stand by their club | Letters" data-date="10-14 00:50" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Why most Manchester City fans stand by their club | Letters</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/012/865.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，比亚迪发布媒体邀请函，确认第二代海鸥将于 10 月 20 日在郑州赛车场正式上市。新车在内饰质感、空间表现与智能化配置上均进行了全面升级。此前 10 月 9 日，比亚迪汽车海洋网销售事业部总经理张卓宣布该车开启盲订，提供青柠绿、莓莓粉、芒芒橙、冰椰蓝、奶油白及芝麻灰六款外观配色。据工信部申报信息，第二代海鸥长宽高为 4205/1810/1570mm，轴距 2650mm，较现款车长增加 425mm、轴距加长 150mm，整体体量已接近比亚迪海豚。同时，其座椅布局由 4 座升级为 5 座，后排横向空间和腿部空间均有所改善。储物方面，新车新增 94L 前备箱，后备箱放倒第二排座椅后最大可扩展至 1380L，二排座椅下方还设有隐藏式储物盒。外观方面，新车采用最新设计" data-title="比亚迪第二代海鸥车型 10 月 20 日上市：尺寸动力底盘全面升级" data-date="10-14 14:47" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">比亚迪第二代海鸥车型 10 月 20 日上市：尺寸动力底盘全面升级</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714353.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 (记者 刘大炜 李百加)就民进党当局领导人赖清德10日发表的所谓“双十”讲话，国务院台办发言人陈斌华14日在北京举行的国台办例行新闻发布会上强调，这篇讲话充满欺骗性。" data-title="二度回应赖清德今年“双十”讲话 国台办指充满欺骗性" data-date="10-14 14:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:42</span>
          <span class="news-item-title">二度回应赖清德今年“双十”讲话 国台办指充满欺骗性</span>
          <span class="news-value-point">💡 中新社北京10月14日电 (记者 刘大炜 李百加)就民进党当局领导人赖清德10日发表的所谓“双十”讲话，国务院台办发言人陈斌华14日在北京举行的…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714380.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 (记者 张素)中国最高人民法院14日发布5件植物新品种保护典型案例，涉及依法平等保护境外育种者合法权益等内容。" data-title="中国最高法发布典型案例 平等保护境外育种者合法权益" data-date="10-14 14:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:25</span>
          <span class="news-item-title">中国最高法发布典型案例 平等保护境外育种者合法权益</span>
          <span class="news-value-point">💡 中新社北京10月14日电 (记者 张素)中国最高人民法院14日发布5件植物新品种保护典型案例，涉及依法平等保护境外育种者合法权益等内容</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714286.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据美联社报道，美国佛罗里达州一名囚犯于当地时间13日被执行死刑。这名囚犯供述，当年杀害狱友就是为了被判处死刑，行凶案件距今已近18年。" data-title="美国佛州一囚犯被执行注射死刑" data-date="10-14 14:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:23</span>
          <span class="news-item-title">美国佛州一囚犯被执行注射死刑</span>
          <span class="news-value-point">💡 中新网10月14日电 据美联社报道，美国佛罗里达州一名囚犯于当地时间13日被执行死刑</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714365.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海10月14日电 (李秋莹 何宝新)10月12日，第二十六届中国国际工业博览会(CIIF)在国家会展中心(上海)开幕，CIIF大奖也正式揭晓。中国船舶第七〇四研究所自主研制的全海域、全海深极渊布放回收系统在列。" data-title="中船七〇四所自主研制极渊布放回收系统获第二十六届CIIF大奖" data-date="10-14 14:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:18</span>
          <span class="news-item-title">中船七〇四所自主研制极渊布放回收系统获第二十六届CIIF大奖</span>
          <span class="news-value-point">💡 中新网上海10月14日电 (李秋莹 何宝新)10月12日，第二十六届中国国际工业博览会(CIIF)在国家会展中心(上海)开幕，CIIF大奖也正式…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714368.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥10月14日电 (记者 赵强)记者14日从安徽省政府新闻办举行的新闻发布会上获悉，该省美丽河湖保护与建设成效初显，建成美丽河湖23个。" data-title="安徽建成美丽河湖23个" data-date="10-14 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:08</span>
          <span class="news-item-title">安徽建成美丽河湖23个</span>
          <span class="news-value-point">💡 中新网合肥10月14日电 (记者 赵强)记者14日从安徽省政府新闻办举行的新闻发布会上获悉，该省美丽河湖保护与建设成效初显，建成美丽河湖23个</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714362.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 综合日媒最新报道，随着日本农林水产大臣梁和生的不当言论及涉嫌违反《公职选举法》的风波持续发酵，日本首相高市早苗陷入困境。日本专家指出，无论其是否辞职，高市政权都将遭受沉重打击。" data-title="高市因农相问题陷困境 日本专家：应对迟缓政权将受重挫" data-date="10-14 14:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:05</span>
          <span class="news-item-title">高市因农相问题陷困境 日本专家：应对迟缓政权将受重挫</span>
          <span class="news-value-point">💡 中新网10月14日电 综合日媒最新报道，随着日本农林水产大臣梁和生的不当言论及涉嫌违反《公职选举法》的风波持续发酵，日本首相高市早苗陷入困境</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714360.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 据印度亚洲新闻国际通讯社当地时间14日报道，印度东部比哈尔邦13日晚发生一起船只倾覆事故，造成至少13人死亡。当地官员称，遇难者均在15岁以下。" data-title="印度比哈尔邦翻船事故已致13人死亡" data-date="10-14 13:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 13:59</span>
          <span class="news-item-title">印度比哈尔邦翻船事故已致13人死亡</span>
          <span class="news-value-point">💡 中新社北京10月14日电 据印度亚洲新闻国际通讯社当地时间14日报道，印度东部比哈尔邦13日晚发生一起船只倾覆事故，造成至少13人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714154.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 综合外媒报道，美国驻希腊大使金伯莉·吉尔福伊尔当地时间13日宣布辞职，并表示，她将“坚决为自己辩护”。" data-title="美国驻希腊大使辞职，曾与特朗普长子订婚" data-date="10-14 13:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 13:28</span>
          <span class="news-item-title">美国驻希腊大使辞职，曾与特朗普长子订婚</span>
          <span class="news-value-point">💡 中新网10月14日电 综合外媒报道，美国驻希腊大使金伯莉·吉尔福伊尔当地时间13日宣布辞职，并表示，她将“坚决为自己辩护”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714314.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据韩联社报道，韩国法务部13日就佩戴电子脚镣的男子当天在仁川市一大型商业设施持刀伤人一事表示，此次事件给#8204;公众#8204;带来担忧，政府对此#8204;深表歉意#8204;。" data-title="就佩戴电子脚镣男子持刀伤人事件 韩国法务部道歉" data-date="10-14 13:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 13:13</span>
          <span class="news-item-title">就佩戴电子脚镣男子持刀伤人事件 韩国法务部道歉</span>
          <span class="news-value-point">💡 中新网10月14日电 据韩联社报道，韩国法务部13日就佩戴电子脚镣的男子当天在仁川市一大型商业设施持刀伤人一事表示，此次事件给#8204;公众#…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714283.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 路易港消息：毛里求斯总理拉姆古兰当地时间13日晚在全国电视讲话中宣布该国多地实施宵禁，时段为当地时间13日20时30分至14日6时。" data-title="毛里求斯多地因暴力事件实施宵禁" data-date="10-14 12:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 12:11</span>
          <span class="news-item-title">毛里求斯多地因暴力事件实施宵禁</span>
          <span class="news-value-point">💡 中新社北京10月14日电 路易港消息：毛里求斯总理拉姆古兰当地时间13日晚在全国电视讲话中宣布该国多地实施宵禁，时段为当地时间13日20时30分…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/13/us/politics/georgia-senate-debate-ossoff-collins.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在民意调查中落后于参议员乔恩·奥索夫（ Jon Ossoff ）的众议员迈克·柯林斯（ Mike Collins ）在周二的第二场也是最后一场辩论中对" data-title="7 Takeaways From the Second Georgia Senate Debate" data-date="10-14 11:58" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 11:58</span>
          <span class="news-item-title">乔治亚州参议院第二次辩论的7个要点</span>
          <span class="news-item-title-en">7 Takeaways From the Second Georgia Senate Debate</span>
          <span class="news-value-point">💡 在民意调查中落后于参议员乔恩·奥索夫（ Jon Ossoff ）的众议员迈克·柯林斯（ Mike Collins ）在周二的第二场也是最后一场辩…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/13/nyregion/cornell-president-interview-takeaways.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="迈克尔·科特利科夫（ Michael Kotlikoff ）谈到了对大学处理一名前学生声称她在兄弟会聚会上被轮奸的担忧。" data-title="Five Key Moments From The Times’s Interview With Cornell’s President" data-date="10-14 11:16" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 11:16</span>
          <span class="news-item-title">《泰晤士报》采访康奈尔大学总裁的五个关键时刻</span>
          <span class="news-item-title-en">Five Key Moments From The Times’s Interview With Cornell’s President</span>
          <span class="news-value-point">💡 迈克尔·科特利科夫（ Michael Kotlikoff ）谈到了对大学处理一名前学生声称她在兄弟会聚会上被轮奸的担忧</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/13/us/politics/kimberly-guilfoyle-resign.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一系列破坏性报道之后，白宫要求吉尔福伊尔辞职，包括她要求共和党捐赠者偿还信用卡。" data-title="Kimberly Guilfoyle Resigns as Ambassador to Greece" data-date="10-14 09:54" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 09:54</span>
          <span class="news-item-title">Kimberly Guilfoyle辞去驻希腊大使一职</span>
          <span class="news-item-title-en">Kimberly Guilfoyle Resigns as Ambassador to Greece</span>
          <span class="news-value-point">💡 在一系列破坏性报道之后，白宫要求吉尔福伊尔辞职，包括她要求共和党捐赠者偿还信用卡</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/13/us/politics/guilfoyle-fall.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在关于她担任驻希腊大使的负面新闻报道之后，特朗普总统解雇了她。她曾是特朗普的知名内幕人士，她建议自己现在将为捍卫自己的声誉而战。" data-title="‘Honey Please’: The Steep Rise and Sudden Fall of Kimberly Guilfoyle." data-date="10-14 09:49" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 09:49</span>
          <span class="news-item-title">“Honey Please” ： Kimberly Guilfoyle的陡峭崛起和突然坠落。</span>
          <span class="news-item-title-en">‘Honey Please’: The Steep Rise and Sudden Fall of Kimberly Guilfoyle.</span>
          <span class="news-value-point">💡 在关于她担任驻希腊大使的负面新闻报道之后，特朗普总统解雇了她</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/13/nyregion/cornell-president-interview-missteps.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在接受《纽约时报》采访时，迈克尔·科特利科夫（ Michael Kotlikoff ）谈到了他的政府对一名前学生提出的性侵犯指控的处理情况。" data-title="Cornell’s President Acknowledges Missteps in Handling of Rape Accusations" data-date="10-14 09:47" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 09:47</span>
          <span class="news-item-title">康奈尔大学总裁承认在处理强奸指控方面的失误</span>
          <span class="news-item-title-en">Cornell’s President Acknowledges Missteps in Handling of Rape Accusations</span>
          <span class="news-value-point">💡 在接受《纽约时报》采访时，迈克尔·科特利科夫（ Michael Kotlikoff ）谈到了他的政府对一名前学生提出的性侵犯指控的处理情况</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/012/861.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，OSAT 龙头日月光半导体 (ASE) 昨日宣布推出基于 PowerSiP 平台的 3D 系统级封装解决方案。这一方案可实现 VRM（电压调节模块）的垂直整合，大幅缩短电流传输路径，降低超半数寄生布线损耗。日月光表示，先进的高性能 AI SoC 功耗已突破 1000W，这意味着需要 1V 以下电压传输超 1000A 的峰值电流，传统的横向架构在电力通过 PCB、封装基板、互连结构到达处理器的过程中可能产生严重的布线损耗。该企业的 PowerSiP 垂直整合工具箱包括夹在无芯基板之间的双面连接电容、具备外露端子的电容阵列模块、4:1 高纵横比铜柱整合技术、单 / 双面模塑高密度主 / 被动元件整合技术。这些技术可解决在空间受限的计算托盘中将电压调节模块配置于" data-title="日月光推出 3D 垂直整合 PowerSiP 解决方案，可减半寄生布线损耗" data-date="10-14 14:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:46</span>
          <span class="news-item-title">日月光推出 3D 垂直整合 PowerSiP 解决方案，可减半寄生布线损耗</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，OSAT 龙头日月光半导体 (ASE) 昨日宣布推出基于 PowerSiP 平台的 3D 系统级封装解决方案</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714404.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="近日，交通运输部办公厅印发了《水运领域人工智能应用场景指引》(交办水〔2026〕63号，以下简称《指引》)。为便于各方更好地理解相关内容，切实做好贯彻落实工作，现解读如下：" data-title="《水运领域人工智能应用场景指引》解读" data-date="10-14 14:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:42</span>
          <span class="news-item-title">《水运领域人工智能应用场景指引》解读</span>
          <span class="news-value-point">💡 近日，交通运输部办公厅印发了《水运领域人工智能应用场景指引》(交办水〔2026〕63号，以下简称《指引》)</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714399.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网10月14日电 据交通运输部微信公众号消息，为贯彻落实交通运输部等七部门印发的《关于“人工智能＋交通运输”的实施意见》，加快推动人工智能在水运领域创新应用，交通运输部办公厅印发《水运领域人工智能应用场景指引》，具体内容如下。" data-title="交通运输部办公厅印发《水运领域人工智能应用场景指引》" data-date="10-14 14:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:42</span>
          <span class="news-item-title">交通运输部办公厅印发《水运领域人工智能应用场景指引》</span>
          <span class="news-value-point">💡 中新网10月14日电 据交通运输部微信公众号消息，为贯彻落实交通运输部等七部门印发的《关于“人工智能＋交通运输”的实施意见》，加快推动人工智能在…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714372.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="记者今天(14日)了解到，2026年1月至9月，我国在国际标准化组织和国际电工委员会共牵头制定智慧城市数据利用顶层框架、钢铁行业智能制造指南等国际标准220项，新提出固态电池、人形机器人数据集等国际标准提案318项。截至目前，我国牵头和发布的国际标准共计2368个，提出的国际提案共计4079项，标准化国际影响力持续提升。" data-title="2026年1月至9月我国牵头制定国际标准220项" data-date="10-14 14:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:09</span>
          <span class="news-item-title">2026年1月至9月我国牵头制定国际标准220项</span>
          <span class="news-value-point">💡 记者今天(14日)了解到，2026年1月至9月，我国在国际标准化组织和国际电工委员会共牵头制定智慧城市数据利用顶层框架、钢铁行业智能制造指南等国…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503172.html" target="_blank" rel="noopener" data-cat="keji" data-summary="给Ego补上缺失的交互信息" data-title="国内最年轻AI教授创业：要让世界模型走向全身全模态" data-date="10-14 12:51" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 12:51</span>
          <span class="news-item-title">国内最年轻AI教授创业：要让世界模型走向全身全模态</span>
          <span class="news-value-point">💡 给Ego补上缺失的交互信息</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503173.html" target="_blank" rel="noopener" data-cat="keji" data-summary="从“懂空间”到“能干活”" data-title="调度效率提升80%！商汤大装置助力上海量子城市首批智能体落地" data-date="10-14 12:09" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 12:09</span>
          <span class="news-item-title">调度效率提升80%！商汤大装置助力上海量子城市首批智能体落地</span>
          <span class="news-value-point">💡 从“懂空间”到“能干活”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503165.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月13日，APUS AI（麒麟合盛网络技术股份有限公司）宣布开源Personal Agent产品Reflex Agent" data-title="响应速度比Claude Code快3倍，实现真正无限上下文！APUS AI开源Reflex Agent" data-date="10-14 11:32" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 11:32</span>
          <span class="news-item-title">响应速度比Claude Code快3倍，实现真正无限上下文！APUS AI开源Reflex Agent</span>
          <span class="news-value-point">💡 10月13日，APUS AI（麒麟合盛网络技术股份有限公司）宣布开源Personal Agent产品Reflex Agent</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crvg9n72v9p2o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能已主导翻译行业，但高风险的范畴仍然需要人类，例如法律、医疗等领域。" data-title="AI翻译：还有多久会完全取代人类？" data-date="10-14 10:38" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 10:38</span>
          <span class="news-item-title">AI翻译：还有多久会完全取代人类？</span>
          <span class="news-value-point">💡 人工智能已主导翻译行业，但高风险的范畴仍然需要人类，例如法律、医疗等领域</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503157.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一次采集，反复使用" data-title="告别资料散落，让知识持续积累：openJiuwen首发个人知识空间，重塑个人办公智能体新体验！" data-date="10-14 10:14" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 10:14</span>
          <span class="news-item-title">告别资料散落，让知识持续积累：openJiuwen首发个人知识空间，重塑个人办公智能体新体验！</span>
          <span class="news-value-point">💡 一次采集，反复使用</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/13/cerebras-ceo-says-were-nearing-a-future-where-everyone-has-a-personal-ai-assistant-at-home/" target="_blank" rel="noopener" data-cat="keji" data-summary="Cerebras首席执行官安德鲁·费尔德曼（ Andrew Feldman ）预测，未来个人人工智能助理将像家用电器一样普遍，部分在本地设备上运行，部分在云中运行。" data-title="Cerebras CEO says we’re nearing a future where everyone has a personal AI assistant at home" data-date="10-14 07:05" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 07:05</span>
          <span class="news-item-title">Cerebras首席执行官表示，我们即将迎来每个人在家都有个人AI助手的未来</span>
          <span class="news-item-title-en">Cerebras CEO says we’re nearing a future where everyone has a personal AI assistant at home</span>
          <span class="news-value-point">💡 Cerebras首席执行官安德鲁·费尔德曼（ Andrew Feldman ）预测，未来个人人工智能助理将像家用电器一样普遍，部分在本地设备上运…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/13/cerebras-ceo-pushes-back-on-ai-doomsday-warnings/" target="_blank" rel="noopener" data-cat="keji" data-summary="Cerebras首席执行官安德鲁·费尔德曼（ Andrew Feldman ）向人工智能领导者发出了世界末日警告：也许停止说话？在TechCrunch Disrupt上，他认为业界对人工智能风险的关注正在淹没其潜在的好处。" data-title="Cerebras CEO pushes back on AI doomsday warnings" data-date="10-14 06:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 06:36</span>
          <span class="news-item-title">Cerebras首席执行官拒绝接受人工智能世界末日警告</span>
          <span class="news-item-title-en">Cerebras CEO pushes back on AI doomsday warnings</span>
          <span class="news-value-point">💡 Cerebras首席执行官安德鲁·费尔德曼（ Andrew Feldman ）向人工智能领导者发出了世界末日警告：也许停止说话</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1010642/openai-employee-arrested-recording-device" target="_blank" rel="noopener" data-cat="keji" data-summary="一名OpenAI工程师在该公司表示在其一个办公室发现了一个隐藏的“精密录音设备”后被捕。这名员工被确认为Abdulrahman Alfozan ， 35岁，沙特国民。Alfozan被指控使用或" data-title="OpenAI employee arrested for allegedly planting a bug in a conference room" data-date="10-14 04:45" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-14 04:45</span>
          <span class="news-item-title">OpenAI员工因涉嫌在会议室植入臭虫而被捕</span>
          <span class="news-item-title-en">OpenAI employee arrested for allegedly planting a bug in a conference room</span>
          <span class="news-value-point">💡 一名OpenAI工程师在该公司表示在其一个办公室发现了一个隐藏的“精密录音设备”后被捕</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/13/judge-orders-openai-to-turn-over-hiring-records-in-apple-trade-secrets-case/" target="_blank" rel="noopener" data-cat="keji" data-summary="一名联邦法官裁定，苹果可以访问OpenAI涉及前苹果员工的采访材料，以及此案中关键人物的私人消息和证词。" data-title="Judge orders OpenAI to turn over hiring records in Apple trade secrets case" data-date="10-14 04:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 04:36</span>
          <span class="news-item-title">法官命令OpenAI交出苹果商业机密案件的招聘记录</span>
          <span class="news-item-title-en">Judge orders OpenAI to turn over hiring records in Apple trade secrets case</span>
          <span class="news-value-point">💡 一名联邦法官裁定，苹果可以访问OpenAI涉及前苹果员工的采访材料，以及此案中关键人物的私人消息和证词</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1010365/shopify-opens-its-catalog-up-to-more-ai-agents" target="_blank" rel="noopener" data-cat="keji" data-summary="更多的人工智能代理商将很快能够从Shopify房源中浏览和购买，这标志着该公司代理商商业野心的扩大。Shopify周二宣布，它将允许购物者配置他们的人工智能代理，以便在" data-title="Shopify opens its catalog up to more AI agents" data-date="10-14 03:42" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-14 03:42</span>
          <span class="news-item-title">Shopify向更多人工智能代理开放其目录</span>
          <span class="news-item-title-en">Shopify opens its catalog up to more AI agents</span>
          <span class="news-value-point">💡 更多的人工智能代理商将很快能够从Shopify房源中浏览和购买，这标志着该公司代理商商业野心的扩大</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/13/flox-intelligence-is-building-ai-to-keep-wildlife-away-from-trains-airports-and-roads/" target="_blank" rel="noopener" data-cat="keji" data-summary="Flox的边缘设备可以识别动物，并使用特定物种的声音来驱使它们远离关键基础设施。" data-title="Flox Intelligence is building AI to keep wildlife away from trains, airports, and roads" data-date="10-14 02:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 02:30</span>
          <span class="news-item-title">Flox Intelligence正在构建人工智能，让野生动物远离火车、机场和道路</span>
          <span class="news-item-title-en">Flox Intelligence is building AI to keep wildlife away from trains, airports, and roads</span>
          <span class="news-value-point">💡 Flox的边缘设备可以识别动物，并使用特定物种的声音来驱使它们远离关键基础设施</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">4 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/13/why-most-manchester-city-fans-stand-by-their-club" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安德鲁·伯顿（ Andrew Burton ）怀疑，如果其他球队取得了类似的成功，球迷们也会原谅他们的主人瑞·肖恩·英格尔（ Re Sean Ingle ）的文章（一些曼城球迷是如何成为一个民族国家政权的积极捍卫者的？ ， 10月5日） ，我暂停" data-title="Why most Manchester City fans stand by their club | Letters" data-date="10-14 00:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-14 00:50</span>
          <span class="news-item-title">为什么大多数曼城球迷都支持他们的俱乐部|来信</span>
          <span class="news-item-title-en">Why most Manchester City fans stand by their club | Letters</span>
          <span class="news-value-point">💡 安德鲁·伯顿（ Andrew Burton ）怀疑，如果其他球队取得了类似的成功，球迷们也会原谅他们的主人瑞·肖恩·英格尔（ Re Sean I…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckn9r1ygv81wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="主教练恩佐·马雷斯卡（ Enzo Maresca ）在曼城在利物浦获胜后对曼城庆祝活动的批评做出了回应，他说： “你想让我们做什么？”" data-title="&#39;Criticised for what?&#39; - Maresca defends celebrations" data-date="10-13 21:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-13 21:04</span>
          <span class="news-item-title">“批评什么？” - Maresca为庆祝活动辩护</span>
          <span class="news-item-title-en">'Criticised for what?' - Maresca defends celebrations</span>
          <span class="news-value-point">💡 主教练恩佐·马雷斯卡（ Enzo Maresca ）在曼城在利物浦获胜后对曼城庆祝活动的批评做出了回应，他说： “你想让我们做什么</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/articles/cmje5wl5ek32o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育的Ask Me Anything团队着眼于俱乐部被判违反英超财务规则期间是否有曼城球员被签约。" data-title="Were any current Man City players signed during charges period?" data-date="10-13 18:13" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-13 18:13</span>
          <span class="news-item-title">在收费期间，是否有任何现任曼城球员签约？</span>
          <span class="news-item-title-en">Were any current Man City players signed during charges period?</span>
          <span class="news-value-point">💡 BBC体育的Ask Me Anything团队着眼于俱乐部被判违反英超财务规则期间是否有曼城球员被签约</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmq5nljx7972o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城违反规则的潜在影响深远，包括错过冠军联赛资格赛、降级和英超联赛奖金。" data-title="How much did Man City&#39;s rule breaking cost your team?" data-date="10-13 16:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-13 16:12</span>
          <span class="news-item-title">曼城打破规则花费了你的团队多少钱？</span>
          <span class="news-item-title-en">How much did Man City's rule breaking cost your team?</span>
          <span class="news-value-point">💡 曼城违反规则的潜在影响深远，包括错过冠军联赛资格赛、降级和英超联赛奖金</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/012/865.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，比亚迪发布媒体邀请函，确认第二代海鸥将于 10 月 20 日在郑州赛车场正式上市。新车在内饰质感、空间表现与智能化配置上均进行了全面升级。此前 10 月 9 日，比亚迪汽车海洋网销售事业部总经理张卓宣布该车开启盲订，提供青柠绿、莓莓粉、芒芒橙、冰椰蓝、奶油白及芝麻灰六款外观配色。据工信部申报信息，第二代海鸥长宽高为 4205/1810/1570mm，轴距 2650mm，较现款车长增加 425mm、轴距加长 150mm，整体体量已接近比亚迪海豚。同时，其座椅布局由 4 座升级为 5 座，后排横向空间和腿部空间均有所改善。储物方面，新车新增 94L 前备箱，后备箱放倒第二排座椅后最大可扩展至 1380L，二排座椅下方还设有隐藏式储物盒。外观方面，新车采用最新设计" data-title="比亚迪第二代海鸥车型 10 月 20 日上市：尺寸动力底盘全面升级" data-date="10-14 14:47" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:47</span>
          <span class="news-item-title">比亚迪第二代海鸥车型 10 月 20 日上市：尺寸动力底盘全面升级</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，比亚迪发布媒体邀请函，确认第二代海鸥将于 10 月 20 日在郑州赛车场正式上市</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/862.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="iPhone Duo 定价 15999 元起，国行 10 月 16 日晚 8 点接受预购。京东今日开售“早鸟先享权益包”，价格 7999 元。除早鸟先享资格外 + 4 项补贴服务外，加赠 999 元原厂手机壳 + 329 元原厂充电头。京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。京东京东 iPhone Duo 早鸟先享权益包不支持退换 手机需另付款 7999 元直达链接需要注意的是：此权益下单后不支持退换iPhone Duo 仅支持 eSIM早鸟机需激活后签收早鸟权益支持 256G 与 512G 机型下单权益包后，手机仍需支付全款哦：京东 Apple iPhone Duo 需签收激活 仅支持 eSIM15999 元起直达链接7999 元早鸟先享权益包包含：i" data-title="7999 元：苹果 iPhone Duo 京东早鸟先享权益包开售，赠 999 元官方手机壳" data-date="10-14 14:47" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:47</span>
          <span class="news-item-title">7999 元：苹果 iPhone Duo 京东早鸟先享权益包开售，赠 999 元官方手机壳</span>
          <span class="news-value-point">💡 iPhone Duo 定价 15999 元起，国行 10 月 16 日晚 8 点接受预购</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/854.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，索尼 ECM-AX10 手机空间音频麦克风现已在京东开售，定价 1499 元。新品采用 Type-C 接口与手机连接，可带来真实的空间音频采集与编辑功能。据介绍，这款产品采用 24g 轻量化设计，尺寸与手机相匹配，可为视频注入真实临场感。内置 6 轴运动传感器，可感应麦克风状态并自动调节横屏 / 竖屏模式。同时，这款产品搭载四颗全指向性麦克风拾音头，均匀捕捉从低频到高频的细节，并以 3D 声像定位编码出清晰音频。拥有专业调音参数，号称“开箱即是好声音”。此外，这款产品带有防风罩、冷靴麦克风支架、Type-C 延长线、垫片等配件，机身带有实体按键，可快速切换空间模式、立体声模式等。兼容配套 App“Spatial Audio and Video Tool”，让" data-title="索尼 ECM-AX10 手机空间音频麦克风开售，1499 元" data-date="10-14 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:43</span>
          <span class="news-item-title">索尼 ECM-AX10 手机空间音频麦克风开售，1499 元</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，索尼 ECM-AX10 手机空间音频麦克风现已在京东开售，定价 1499 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/853.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，地面沉降指地表缓慢下沉的现象，会损毁建筑物、地基、排水与污水管网，还会加剧洪涝风险。但目前关于地面沉降动态变化的相关资料仍然有限，政策制定者难以定位风险加剧区域，无法判断哪里需要紧急治理。以往各类评估所采用的方法、监测时段各不相同，或是仅针对少数城市开展研究，难以进行全球横向对比。陶胜利（Shengli Tao，音译）、胡谢（Xie Hu，音译）及其团队分析了 2014 至 2023 年间采集的高分辨率卫星数据，以此测量 107 个国家 465 座城市的地表形变情况。研究成果发表于《自然・城市》（Nature Cities）期刊。IT之家注意到，墨西哥城部分区域的局部下沉速率全球最高，约为每年 217 毫米；不过整座城市的沉降中位数为每年 8 毫米。同样位于" data-title="卫星数据揭示：全球多个大城市正发生地面沉降" data-date="10-14 14:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:39</span>
          <span class="news-item-title">卫星数据揭示：全球多个大城市正发生地面沉降</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，地面沉降指地表缓慢下沉的现象，会损毁建筑物、地基、排水与污水管网，还会加剧洪涝风险</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/852.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，华为 Freebuds Neo × 王者荣耀朵莉亚 · 限定款无线耳机今日正式开售，内含专属保护壳、限定手办等，定价 799 元、优惠价 749 元。京东华为 FreeBuds Neo【王者荣耀 朵莉亚 · 限定款】749 元直达链接据介绍，华为 FreeBuds Neo 搭载鸿蒙 HarmonyOS 7 操作系统，耳机舱采用“星际小飞碟”全曲面飞梭设计，灵感源自黄金分割比例，人体工学流线造型贴合掌心；耳机本体采用“流光小灵杆”全新设计形态，单只耳机轻至 4.8 克、触控区域占比达 60%。该耳机搭载自研第三代音频 AI 芯片，双 DSP 架构与 NPU AI 处理器协同驱动 + 高阶自适应算法，每秒采集环境噪音信息高达 40 万次，噪音处理时延低至 8 微" data-title="华为 Freebuds Neo × 王者荣耀朵莉亚 · 限定款无线耳机开售，优惠价 749 元" data-date="10-14 14:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:38</span>
          <span class="news-item-title">华为 Freebuds Neo × 王者荣耀朵莉亚 · 限定款无线耳机开售，优惠价 749 元</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，华为 Freebuds Neo × 王者荣耀朵莉亚 · 限定款无线耳机今日正式开售，内含专属保护壳、限定手办等…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/851.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，be quiet!（德商德静界）近日推出了 Light Wings Pro IO 系列风扇，包括 360 (3×120) 与 420 (3×140) 规格的单框连体型号和以“扩展”形式推出的单体版本。Light Wings Pro IO 家族风扇均采用 28mm 厚度设计，可选黑 / 白配色、正叶 / 反叶风向。其 360 / 420 / 120 / 140 版本的定价分别为 132.9 / 142.9 / 54.9 / 59.9 美元或 109.9 / 119.9 / 42.9 / 45.9 欧元。Light Wings Pro IO 单框连体风扇拥有 4 个可独立控制的 ARGB 灯区，容纳至多 124 颗 LED 灯珠。其采用流体动力轴承和一体式橡胶框" data-title="be quiet! 推出 Light Wings Pro IO 系列单框连体风扇，可选 360 / 420 规格" data-date="10-14 14:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:37</span>
          <span class="news-item-title">be quiet! 推出 Light Wings Pro IO 系列单框连体风扇，可选 360 / 420 规格</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，be quiet!（德商德静界）近日推出了 Light Wings Pro IO 系列风扇，包括 360 (3…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714382.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南昌10月14日电 (李韵涵 刘小虎)14日，记者从江西省林业局了解到，《江西省“十五五”林业发展规划》(以下简称《规划》)近日由江西省林业局、江西省发展和改革委员会印发。《规划》提出高水平保护、高质量发展、高效能治理与高素质队伍，建设现代化林业强省的“四高一强”发展思路，为未来5年林业高质量发展指明了方向。" data-title="筑牢生态屏障 江西林业“十五五”规划谋篇高质量发展" data-date="10-14 14:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:35</span>
          <span class="news-item-title">筑牢生态屏障 江西林业“十五五”规划谋篇高质量发展</span>
          <span class="news-value-point">💡 中新网南昌10月14日电 (李韵涵 刘小虎)14日，记者从江西省林业局了解到，《江西省“十五五”林业发展规划》(以下简称《规划》)近日由江西省林…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714386.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月14日电(鲍梦妮)电子档案是数字时代国家记忆的核心载体，也是一座亟待唤醒的价值富矿。如何让它既“存得久”又“用得好”？" data-title="电子档案如何“存得久”又“用得好”？ 政企学共探破题之道" data-date="10-14 14:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:32</span>
          <span class="news-item-title">电子档案如何“存得久”又“用得好”？ 政企学共探破题之道</span>
          <span class="news-value-point">💡 中新网杭州10月14日电(鲍梦妮)电子档案是数字时代国家记忆的核心载体，也是一座亟待唤醒的价值富矿</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714384.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网吉林10月14日电(记者 张焕迪)记者14日随“美丽中国行”主题采访团走进吉林桦甸夹皮沟镇，来到依托拥有200多年开采历史的“中国黄金第一矿”建设的黄金博物馆，了解夹皮沟采金历史传承及博物馆展陈活化利用的实际成效。" data-title="吉林桦甸：两百年金矿变身“黄金博物馆” 工业遗产焕发新活力" data-date="10-14 14:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:21</span>
          <span class="news-item-title">吉林桦甸：两百年金矿变身“黄金博物馆” 工业遗产焕发新活力</span>
          <span class="news-value-point">💡 中新网吉林10月14日电(记者 张焕迪)记者14日随“美丽中国行”主题采访团走进吉林桦甸夹皮沟镇，来到依托拥有200多年开采历史的“中国黄金第一…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714383.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥10月14日电 (记者 赵强)安徽省水利厅二级巡视员崔黎14日在安徽省政府新闻办举行的新闻发布会上透露，该省全面推进幸福河湖建设，目前建成国家级幸福河湖5个，数量位居全国第一。" data-title="安徽建成的国家级幸福河湖数量位居全国第一" data-date="10-14 14:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:20</span>
          <span class="news-item-title">安徽建成的国家级幸福河湖数量位居全国第一</span>
          <span class="news-value-point">💡 中新网合肥10月14日电 (记者 赵强)安徽省水利厅二级巡视员崔黎14日在安徽省政府新闻办举行的新闻发布会上透露，该省全面推进幸福河湖建设，目前…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714361.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月14日电 (记者 李百加 刘大炜)“十一”国庆期间，多位台湾艺人发文为祖国献上祝福。国务院台办发言人陈斌华14日在北京表示，台湾是中国的一部分，台湾同胞自发表达爱国之情是自然而然的事。" data-title="多位台湾艺人为祖国献祝福 国台办：表达爱国之情自然而然" data-date="10-14 14:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:18</span>
          <span class="news-item-title">多位台湾艺人为祖国献祝福 国台办：表达爱国之情自然而然</span>
          <span class="news-value-point">💡 中新社北京10月14日电 (记者 李百加 刘大炜)“十一”国庆期间，多位台湾艺人发文为祖国献上祝福</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714367.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网东莞10月14日电 (记者 郭军)“爱在岭南 同心守护”两岸婚姻家庭系列活动成果展暨第五届广东省两岸婚姻家庭湾区行13日在东莞举行，台胞、两岸婚姻家庭代表等各界人士约600人参与。" data-title="两岸婚姻家庭系列活动成果展在东莞举行" data-date="10-14 14:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:09</span>
          <span class="news-item-title">两岸婚姻家庭系列活动成果展在东莞举行</span>
          <span class="news-value-point">💡 中新网东莞10月14日电 (记者 郭军)“爱在岭南 同心守护”两岸婚姻家庭系列活动成果展暨第五届广东省两岸婚姻家庭湾区行13日在东莞举行，台胞、…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714322.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新一轮冷空气即将影响我国 北方将掀气温创新低浪潮" data-title="新一轮冷空气即将影响我国 北方多地气温将创新低" data-date="10-14 13:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 13:20</span>
          <span class="news-item-title">新一轮冷空气即将影响我国 北方多地气温将创新低</span>
          <span class="news-value-point">💡 新一轮冷空气即将影响我国 北方将掀气温创新低浪潮</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crpdgz701dyzo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="梵蒂冈方面表示，教宗良十四世成功接受了右肺下叶切除手术。" data-title="梵蒂冈证实教宗患上肺腺癌，但手术成功" data-date="10-14 12:37" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 12:37</span>
          <span class="news-item-title">梵蒂冈证实教宗患上肺腺癌，但手术成功</span>
          <span class="news-value-point">💡 梵蒂冈方面表示，教宗良十四世成功接受了右肺下叶切除手术</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c3n07pkpk5ggo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“北蓝南绿”是描述台湾政治版图的常见概念，但近年选举结果显示，这样的区域分野并非一成不变，中间选民的流向在这次地方选举可能左右大局。" data-title="台湾选举解读：“北蓝南绿”的政治版图是否“铁板一块”？" data-date="10-14 11:36" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 11:36</span>
          <span class="news-item-title">台湾选举解读：“北蓝南绿”的政治版图是否“铁板一块”？</span>
          <span class="news-value-point">💡 “北蓝南绿”是描述台湾政治版图的常见概念，但近年选举结果显示，这样的区域分野并非一成不变，中间选民的流向在这次地方选举可能左右大局</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-14 14:49（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
