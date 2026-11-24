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
      <span>2026-11-24 08:08 抓取更新</span>
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
        <span class="channel-count">57</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">57</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×15 · 中国新闻网×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-24/10736745.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据中国载人航天工程办公室介绍，空间站应用与发展阶段飞行任务总指挥部定于北京时间11月24日上午9时，在酒泉卫星发射中心召开神舟二十四号载人飞行任务新闻发布会，通报此次任务有关情况。" data-title="神舟二十四号载人飞行任务新闻发布会将于今天上午召开" data-date="11-24 08:01" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-24 08:01</span>
      </div>
      <h2 class="hero-featured-title">神舟二十四号载人飞行任务新闻发布会将于今天上午召开</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/031/258.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，据《首尔经济日报》今日报道，三星电子计划将位于中国陕西西安的半导体工厂打造成面向人工智能（AI）数据中心企业级固态硬盘（eSSD）的核心生产基地，重点扩大第九代垂直 NAND 闪存（V9）产能。截至今年第二季度，三星西安一厂（X1）和二厂（X2）的晶圆月投入能力均为 5 万片，合计达到 10 万片（IT之家注：单位为 300mm 晶圆）。这相当于三星平泽四座工厂月产能总和（20 万片）的一半。三星两地 NAND 工厂的晶圆月产能合计约为 30 万片，其中西安工厂占比约 33%。消息人士称，三星计划升级 X2 洁净室内的电镀工艺设备，并将生产线调整为以最新第九代垂直 NAND（V9）工艺为主。除了在 X2 新增一条月产能约 2 万片的生产线外，三星还打算将现有" data-title="三星拟扩大西安工厂先进 NAND 产能、升级 V9 闪存产线，扩大面向 AI 数据中心的 eSSD 供应" data-date="11-24 07:52" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">三星拟扩大西安工厂先进 NAND 产能、升级 V9 闪存产线，扩大面向 AI 数据中心的 eSSD 供应</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c34gn2p5d0zwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队。你同意他的选择吗？" data-title="Who has made Troy&#39;s Premier League team of the week?" data-date="11-24 07:26" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">谁入选了特洛伊本周的英超联赛球队？</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/031/256.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，科技媒体 GSMArena 昨日（11 月 23 日）发布博文，报道称摩托罗拉首款宽折叠手机 Razr Flex 已通过无线充电联盟（WPC）认证，型号为 XT2761。根据认证信息显示，该机支持扩展功率配置文件（EPP），标准无线充电功率最高为 15W；此前传闻中的 25W 无线快充，可能需要通过其他协议或厂商私有方案才能实现。IT之家附上相关截图如下：不过“证件照”尚未正确对应手机外观，所附图片仍显示传统纵向翻盖式 Razr，应该只是认证资料中的占位图。发布时间方面，早前消息曾指向 12 月中旬亮相，但摩托罗拉官方支持网站的线索则暗示 Razr Flex 或将推迟至 2027 年上市。" data-title="摩托罗拉首款宽折叠手机 Razr Flex 通过认证，15W 无线充电" data-date="11-24 07:44" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">摩托罗拉首款宽折叠手机 Razr Flex 通过认证，15W 无线充电</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10736745.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据中国载人航天工程办公室介绍，空间站应用与发展阶段飞行任务总指挥部定于北京时间11月24日上午9时，在酒泉卫星发射中心召开神舟二十四号载人飞行任务新闻发布会，通报此次任务有关情况。" data-title="神舟二十四号载人飞行任务新闻发布会将于今天上午召开" data-date="11-24 08:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 08:01</span>
          <span class="news-item-title">神舟二十四号载人飞行任务新闻发布会将于今天上午召开</span>
          <span class="news-value-point">💡 据中国载人航天工程办公室介绍，空间站应用与发展阶段飞行任务总指挥部定于北京时间11月24日上午9时，在酒泉卫星发射中心召开神舟二十四号载人飞行任…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10736742.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据路透社报道，当地时间23日，美国总统特朗普表示，已命令美军暂停推进在艾奥瓦州引爆68桶有毒含铅化合物的计划。" data-title="特朗普下令：暂停美军在艾奥瓦州引爆有毒化学物质" data-date="11-24 07:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 07:48</span>
          <span class="news-item-title">特朗普下令：暂停美军在艾奥瓦州引爆有毒化学物质</span>
          <span class="news-value-point">💡 中新网11月24日电 据路透社报道，当地时间23日，美国总统特朗普表示，已命令美军暂停推进在艾奥瓦州引爆68桶有毒含铅化合物的计划</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/climate/iowa-army-ammunition-explosion.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="The ruling capped a day of uncertainty in which President Trump spoke out on a crisis that threatens to launch a cloud of toxic lead dust across homes and farmland." data-title="Federal Court Clears the Way for Planned Ammunition Explosion in Iowa" data-date="11-24 07:43" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 07:43</span>
          <span class="news-item-title">Federal Court Clears the Way for Planned Ammunition Explosion in Iowa</span>
          <span class="news-value-point">💡 The ruling capped a day of uncertainty in which President Trump spoke ou…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10736730.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据路透社报道，当地时间23日，以色列对加沙发动多轮空袭，造成3人死亡，其中包括一名联合国近东巴勒斯坦难民救济和工程处(近东救济工程处)的工作人员。" data-title="外媒：以军空袭加沙致3死 其中含1名联合国工作人员" data-date="11-24 07:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 07:11</span>
          <span class="news-item-title">外媒：以军空袭加沙致3死 其中含1名联合国工作人员</span>
          <span class="news-value-point">💡 中新网11月24日电 据路透社报道，当地时间23日，以色列对加沙发动多轮空袭，造成3人死亡，其中包括一名联合国近东巴勒斯坦难民救济和工程处(近东…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/world/europe/russia-ukraine-war-deaths.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Hacked government data underscores the immense human cost of President Vladimir V. Putin’s war of attrition." data-title="Over 700,000 Russian Soldiers Have Died in Ukraine, Analysis Indicates" data-date="11-24 03:19" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 03:19</span>
          <span class="news-item-title">Over 700,000 Russian Soldiers Have Died in Ukraine, Analysis Indicates</span>
          <span class="news-value-point">💡 Hacked government data underscores the immense human cost of President V…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1038020/shows-to-stream-instead-of-harry-potter" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Since we wrote earlier this year about J.K. Rowling using her money to support groups and policies harming transgender people, she has accused the United Nations of promoting &quot;sex denialism&quot; and described trans rights activists as &quot;elitists&quot; whose work creates &quot;a climate of fear and intimidation.&quot; Also, her upcoming HBO Harry Potter series has not" data-title="New magical shows worth watching instead of Harry Potter" data-date="11-24 03:17" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 03:17</span>
          <span class="news-item-title">New magical shows worth watching instead of Harry Potter</span>
          <span class="news-value-point">💡 Since we wrote earlier this year about J.K. Rowling using her money to s…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/world/europe/ukraine-libya-russian-ships.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="President Volodymyr Zelensky said that Ukrainian drones had sunk a corvette and hit a dry cargo vessel, in attacks that involved special operations forces." data-title="Ukraine Attack Off Coast of Libya Shows Reach of Its Naval Drones" data-date="11-24 02:09" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 02:09</span>
          <span class="news-item-title">Ukraine Attack Off Coast of Libya Shows Reach of Its Naval Drones</span>
          <span class="news-value-point">💡 President Volodymyr Zelensky said that Ukrainian drones had sunk a corve…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-23/10736723.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉11月23日电 (记者 周璟)据菲律宾媒体23日消息，菲南部棉兰老岛日前发生一起武装袭击事件，当地一名政府官员的住宅遭火箭弹袭击，周边数百名居民被迫撤离。" data-title="菲律宾南部官员住宅遭火箭弹袭击 数百居民再度撤离" data-date="11-23 23:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 23:23</span>
          <span class="news-item-title">菲律宾南部官员住宅遭火箭弹袭击 数百居民再度撤离</span>
          <span class="news-value-point">💡 中新社马尼拉11月23日电 (记者 周璟)据菲律宾媒体23日消息，菲南部棉兰老岛日前发生一起武装袭击事件，当地一名政府官员的住宅遭火箭弹袭击，周…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-23/10736714.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月23日电 (记者 黄钰钦)针对中俄美元首会晤若机制化是否会削弱现有多边机制，中国外交部发言人郭嘉昆23日在例行记者会上应询指出，中国不搞地缘争夺，不搞势力范围，而是在相互尊重、平等相待的基础上，同各国开展友好交往。" data-title="外交部：中国不搞地缘争夺，不搞势力范围" data-date="11-23 23:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 23:09</span>
          <span class="news-item-title">外交部：中国不搞地缘争夺，不搞势力范围</span>
          <span class="news-value-point">💡 中新社北京11月23日电 (记者 黄钰钦)针对中俄美元首会晤若机制化是否会削弱现有多边机制，中国外交部发言人郭嘉昆23日在例行记者会上应询指出，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-23/10736715.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社悉尼11月23日电 题：澳大利亚艺术家赴华采风：于山水林石间见中国" data-title="澳大利亚艺术家赴华采风：于山水林石间见中国" data-date="11-23 22:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 22:54</span>
          <span class="news-item-title">澳大利亚艺术家赴华采风：于山水林石间见中国</span>
          <span class="news-value-point">💡 中新社悉尼11月23日电 题：澳大利亚艺术家赴华采风：于山水林石间见中国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-23/10736713.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月23日电 综合消息：伊朗外交部发言人巴加埃23日表示，伊朗已制定政治、外交和防御相结合的综合措施，以应对美国的非法制裁和封锁。卡塔尔首相兼外交大臣穆罕默德23日赴美，继续推动美伊达成协议。" data-title="伊朗制定综合措施应对制裁和封锁 卡塔尔首相赴美继续调解" data-date="11-23 22:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 22:53</span>
          <span class="news-item-title">伊朗制定综合措施应对制裁和封锁 卡塔尔首相赴美继续调解</span>
          <span class="news-value-point">💡 中新社北京11月23日电 综合消息：伊朗外交部发言人巴加埃23日表示，伊朗已制定政治、外交和防御相结合的综合措施，以应对美国的非法制裁和封锁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-23/10736676.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月23日电 (记者 谢雁冰)刑事法律援助全球会议23日在北京开幕，中国国务委员、公安部部长王小洪出席并致辞。" data-title="刑事法律援助全球会议在北京开幕 王小洪出席并致辞" data-date="11-23 21:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-23 21:36</span>
          <span class="news-item-title">刑事法律援助全球会议在北京开幕 王小洪出席并致辞</span>
          <span class="news-value-point">💡 中新社北京11月23日电 (记者 谢雁冰)刑事法律援助全球会议23日在北京开幕，中国国务委员、公安部部长王小洪出席并致辞</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/031/258.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，据《首尔经济日报》今日报道，三星电子计划将位于中国陕西西安的半导体工厂打造成面向人工智能（AI）数据中心企业级固态硬盘（eSSD）的核心生产基地，重点扩大第九代垂直 NAND 闪存（V9）产能。截至今年第二季度，三星西安一厂（X1）和二厂（X2）的晶圆月投入能力均为 5 万片，合计达到 10 万片（IT之家注：单位为 300mm 晶圆）。这相当于三星平泽四座工厂月产能总和（20 万片）的一半。三星两地 NAND 工厂的晶圆月产能合计约为 30 万片，其中西安工厂占比约 33%。消息人士称，三星计划升级 X2 洁净室内的电镀工艺设备，并将生产线调整为以最新第九代垂直 NAND（V9）工艺为主。除了在 X2 新增一条月产能约 2 万片的生产线外，三星还打算将现有" data-title="三星拟扩大西安工厂先进 NAND 产能、升级 V9 闪存产线，扩大面向 AI 数据中心的 eSSD 供应" data-date="11-24 07:52" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:52</span>
          <span class="news-item-title">三星拟扩大西安工厂先进 NAND 产能、升级 V9 闪存产线，扩大面向 AI 数据中心的 eSSD 供应</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，据《首尔经济日报》今日报道，三星电子计划将位于中国陕西西安的半导体工厂打造成面向人工智能（AI）数据中心企业级…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/257.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，据科技媒体 TechCrunch 昨天报道，Anthropic 现已推出 Claude Ship Beta 测试版。这是一套 AI 智能体组成的工具，可自动完成代码审查、修复和批准等工作。IT之家从原报道获悉，Claude Ship 包含 Code Review、PR Steward 和 Claude Approvals 三项功能。其中 Code Review 已正式开放使用，另外两项目前处于 Beta 测试阶段。在这些工具中，PR Steward 主要负责处理 CI 检查失败、合并冲突，以及 Code Review 提出的反馈问题。每次代码推送完成后，它会在评论说明自己修改了哪些内容，以及在必要时如何撤销这些修改。Claude Approvals 可根据开" data-title="Anthropic 推出 Claude Ship 测试版：AI 可自动审查、修复及批准代码" data-date="11-24 07:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:49</span>
          <span class="news-item-title">Anthropic 推出 Claude Ship 测试版：AI 可自动审查、修复及批准代码</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，据科技媒体 TechCrunch 昨天报道，Anthropic 现已推出 Claude Ship Beta 测…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/us/politics/trump-nvidia-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The president set in motion a weekend of maneuvering, led by Vice President JD Vance, to help Jensen Huang get his old job back." data-title="Trump Is Said to Have Pushed to Reinstate Nvidia CEO Jensen Huang" data-date="11-24 07:41" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 07:41</span>
          <span class="news-item-title">Trump Is Said to Have Pushed to Reinstate Nvidia CEO Jensen Huang</span>
          <span class="news-value-point">💡 The president set in motion a weekend of maneuvering, led by Vice Presid…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/253.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，当地时间 11 月 23 日，美国证券交易委员会（SEC）披露的 Form 4 文件显示，Anthropic CEO 达里奥 · 阿莫代伊（Dario Amodei）于 IPO 上市当天出售了 3,378,378 股 Class A 普通股，成交价格为每股 83 美元（即 IPO 发行价）。按该价格计算，交易总额约为 2.804 亿美元（IT之家注：现汇率约合 18.73 亿元人民币）。截至 11 月 23 日美股收盘，Anthropic 股价报 87.64 美元，当日下跌 1.27 美元（-1.43%），总市值约 1.15 万亿美元（现汇率约合 7.68 万亿元人民币）。文件还披露，2026 年 11 月 19 日，Anthropic 从阿莫代伊持有的股份" data-title="Anthropic CEO 达里奥 · 阿莫代伊出售 337.8 万股股票，IPO 当天套现约 2.8 亿美元" data-date="11-24 07:29" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:29</span>
          <span class="news-item-title">Anthropic CEO 达里奥 · 阿莫代伊出售 337.8 万股股票，IPO 当天套现约 2.8 亿美元</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，当地时间 11 月 23 日，美国证券交易委员会（SEC）披露的 Form 4 文件显示，Anthropic …</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10736732.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="当前，人工智能生成内容(AIGC)技术加速迭代，AI绘画、AI视频、AI写作、数字人直播等新业态蓬勃兴起，催生了大量“AI创作者”。他们中既有全职的提示词工程师、AI画师，也有兼职的内容创作者，还有运营数字人主播的多频道网络(MCN)机构等。随着AI创作收益的快速增长，一系列涉税问题随之而来：AI创作者的收入究竟是劳务报酬还是经营所得？平台支付创作分成时是否需要代扣代缴？数字人主播的收入又该归谁纳税？" data-title="AI创作收入如何纳税" data-date="11-24 07:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 07:28</span>
          <span class="news-item-title">AI创作收入如何纳税</span>
          <span class="news-value-point">💡 当前，人工智能生成内容(AIGC)技术加速迭代，AI绘画、AI视频、AI写作、数字人直播等新业态蓬勃兴起，催生了大量“AI创作者”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/252.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="“IT早报”时间，大家好，现在是 2026 年 11 月 24 日星期二，今天的重要科技资讯有：1. 英伟达董事会恢复黄仁勋总裁兼首席执行官职务，英伟达美股盘前涨幅最高达 30%英伟达官方 24 日宣布，黄仁勋即日起复任总裁兼首席执行官及董事会成员。公告提到，董事会在与黄仁勋进行一系列讨论和会议后，一致投票决定恢复其职务。英伟达表示，董事会经过与黄仁勋多轮讨论和会议，对其坦诚程度及领导公司能力表示认可，并认为恢复其职务符合股东、员工、合作伙伴及客户的最佳利益。&gt;&gt; 查看详情2. 中国汽车在 39 国的份额超过日本汽车2026 年，德国、巴西等 14 个国家的份额发生逆转。受全球原油价格上涨影响，中国企业擅长的纯电动汽车（EV）销量增长，抢占了市场份额。&gt;&gt; 查看详情3. 3399 元起荣耀" data-title="IT早报 1124：英伟达恢复黄仁勋 CEO 职务；中国汽车在 39 国的份额超过日本汽车；3399 元起荣耀 700 系列手机发布；智谱 GLM" data-date="11-24 07:22" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:22</span>
          <span class="news-item-title">IT早报 1124：英伟达恢复黄仁勋 CEO 职务；中国汽车在 39 国的份额超过日本汽车；3399 元起荣耀 700 系列手机发布；智谱 GLM</span>
          <span class="news-value-point">💡 “IT早报”时间，大家好，现在是 2026 年 11 月 24 日星期二，今天的重要科技资讯有：1. 英伟达董事会恢复黄仁勋总裁兼首席执行官职务…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/business/trump-administration-megaspeed-trade-blacklist-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The administration added Megaspeed to the entity list, a trade blacklist, after weeks of sparring among top officials on the decision." data-title="Trump Administration Imposes Sanctions on Megaspeed, Singaporean Firm at Center of Nvidia Scandal" data-date="11-24 07:18" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 07:18</span>
          <span class="news-item-title">Trump Administration Imposes Sanctions on Megaspeed, Singaporean Firm at Center of Nvidia Scandal</span>
          <span class="news-value-point">💡 The administration added Megaspeed to the entity list, a trade blacklist…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/245.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，OpenAI 昨日（11 月 23 日）宣布携手思科（Cisco）推出开源安全运行时 Shirudo，基于 eBPF 技术为运行中的系统提供无需重启的临时漏洞防护，已通过 Java4Shell 攻击拦截测试。OpenAI 在博文中指出，传统安全响应中，企业发现漏洞后往往要经历修复开发、测试、灰度发布和全量上线等环节，可能耗时数天甚至数周。但攻击者不会等待企业完全修复，一旦漏洞被公开或被利用，正在运行的服务就可能暴露在风险中。更棘手的是，漏洞利用与正常业务请求有时会调用相同的 Linux 系统操作，若简单封禁相关行为，可能导致服务中断。双方本次合作推出的 Shirudo 主要为运行中的系统加装一层可验证的“盾牌”，通过基于 Linux 的 eBPF 技术工作，" data-title="告别“重启才能修复”：OpenAI 携手思科开源 Shirudo，给 Linux 装上临时盾牌" data-date="11-24 07:00" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:00</span>
          <span class="news-item-title">告别“重启才能修复”：OpenAI 携手思科开源 Shirudo，给 Linux 装上临时盾牌</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，OpenAI 昨日（11 月 23 日）宣布携手思科（Cisco）推出开源安全运行时 Shirudo，基于 e…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10736728.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网11月24日电 据美国有线电视新闻网(CNN)等美媒报道，当地时间23日，美国纽约股市三大股指大幅上涨。受黄仁勋复职消息提振，英伟达股价当天收盘上涨31.5%。" data-title="美媒：英伟达股价暴涨超31% 单日市值增加近1万亿美元" data-date="11-24 06:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 06:53</span>
          <span class="news-item-title">美媒：英伟达股价暴涨超31% 单日市值增加近1万亿美元</span>
          <span class="news-value-point">💡 中新网11月24日电 据美国有线电视新闻网(CNN)等美媒报道，当地时间23日，美国纽约股市三大股指大幅上涨</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1040872/ladybird-indie-browser-engine-alpha-testing" target="_blank" rel="noopener" data-cat="keji" data-summary="Ladybird, an independent web browser with a built-from-scratch engine, is finally available for testing. On Monday, Ladybird developer Andreas Kling announced that the browser is launching in alpha on macOS and Linux following more than four years of development. The release makes Ladybird the first browser in years to arrive with an entirely new e" data-title="Ladybird, the first new browser engine in years, is now available to test" data-date="11-24 06:38" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 06:38</span>
          <span class="news-item-title">Ladybird, the first new browser engine in years, is now available to test</span>
          <span class="news-value-point">💡 Ladybird, an independent web browser with a built-from-scratch engine, i…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1040652/jensen-huang-nvidia-trump-reinstated" target="_blank" rel="noopener" data-cat="keji" data-summary="After Nvidia&#39;s board accepted Jensen Huang&#39;s resignation as CEO, following reports that Huang had an affair with an alleged Chinese spy, President Donald Trump, too, appeared to submit to the new reality. Appearing on Stephen A. Smith&#39;s radio show shortly after the news came out, Trump said that Huang would &quot;end up on his feet.&quot; […]" data-title="Trump engineered a risky comeback for Jensen Huang" data-date="11-24 06:25" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 06:25</span>
          <span class="news-item-title">Trump engineered a risky comeback for Jensen Huang</span>
          <span class="news-value-point">💡 After Nvidia's board accepted Jensen Huang's resignation as CEO, followi…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/business/trump-jensen-huang-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="President Trump intervened on behalf of the returning Nvidia chief in a bid to boost a key company driving the stock market. The company’s share price soared." data-title="Jensen Huang Returns to Nvidia, Showing What Trump Will Do for AI" data-date="11-24 06:19" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 06:19</span>
          <span class="news-item-title">Jensen Huang Returns to Nvidia, Showing What Trump Will Do for AI</span>
          <span class="news-value-point">💡 President Trump intervened on behalf of the returning Nvidia chief in a …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1030422/nvidia-jensen-huang-ai-china-alice-huang" target="_blank" rel="noopener" data-cat="keji" data-summary="After the leather-jacketed CEO, president, and co-founder of Nvidia, Jensen Huang, acknowledged an affair with Megaspeed exec Alice Huang, his company initially announced an investigation. However, after The New York Times reported there was evidence of another affair, this time with an Nvidia executive who reported directly to him, a board meeting" data-title="Nvidia CEO Jensen Huang is back. What happens next?" data-date="11-24 06:10" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 06:10</span>
          <span class="news-item-title">Nvidia CEO Jensen Huang is back. What happens next?</span>
          <span class="news-value-point">💡 After the leather-jacketed CEO, president, and co-founder of Nvidia, Jen…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1040819/welcome-to-elite-impunity-jensen-huang" target="_blank" rel="noopener" data-cat="keji" data-summary="I suppose I must issue a hearty congratulations to Jensen Huang. Huang is CEO of Nvidia again, to the surprise of basically everyone except President Donald Trump and Vice President JD Vance, who made sure it happened. Now, those of us who had some kind of basic education on what a &quot;free market&quot; is might […]" data-title="Welcome to elite impunity, Jensen Huang" data-date="11-24 06:09" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 06:09</span>
          <span class="news-item-title">Welcome to elite impunity, Jensen Huang</span>
          <span class="news-value-point">💡 I suppose I must issue a hearty congratulations to Jensen Huang. Huang i…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/" target="_blank" rel="noopener" data-cat="keji" data-summary="As AI-generated code piles up, Anthropic&#39;s new developer tools aim to eliminate another bottleneck by letting agents handle routine approvals." data-title="Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes" data-date="11-24 06:05" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-24 06:05</span>
          <span class="news-item-title">Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes</span>
          <span class="news-value-point">💡 As AI-generated code piles up, Anthropic's new developer tools aim to el…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c34gn2p5d0zwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队。你同意他的选择吗？" data-title="Who has made Troy&#39;s Premier League team of the week?" data-date="11-24 07:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 07:26</span>
          <span class="news-item-title">谁入选了特洛伊本周的英超联赛球队？</span>
          <span class="news-item-title-en">Who has made Troy's Premier League team of the week?</span>
          <span class="news-value-point">💡 在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279303/everton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Everton latest: Moyes unsure over Tarkowski appeal with Liverpool up next" data-title="Everton latest: Moyes unsure over Tarkowski appeal with Liverpool up next" data-date="11-24 07:02" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 07:02</span>
          <span class="news-item-title">Everton latest: Moyes unsure over Tarkowski appeal with Liverpool up next</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279280/brentford-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Brentford latest: &#39;Get real&#39; - Andrews pushes back against rising expectations" data-title="Brentford latest: &#39;Get real&#39; - Andrews pushes back against rising expectations" data-date="11-24 07:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 07:00</span>
          <span class="news-item-title">Brentford latest: 'Get real' - Andrews pushes back against rising expectations</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmqx5eynvpqno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Everton captain James Tarkowski was sent off for the first time in his Premier League career in Monday&#39;s 4-0 loss at Brentford - but was it a harsh decision?" data-title="Tarkowski&#39;s first Premier League red ruins Moyes&#39; night" data-date="11-24 06:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 06:43</span>
          <span class="news-item-title">Tarkowski's first Premier League red ruins Moyes' night</span>
          <span class="news-value-point">💡 Everton captain James Tarkowski was sent off for the first time in his P…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13615837/man-utd-transfer-news-brentford-defender-nathan-collins-emerges-as-january-target-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二报纸的热门报道和转移谣言……" data-title="Papers: Brentford defender emerges as Man Utd target as January budget revealed" data-date="11-24 06:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 06:40</span>
          <span class="news-item-title">Papers: Brentford defender emerges as Man Utd target as January budget revealed</span>
          <span class="news-value-point">💡 周二报纸的热门报道和转移谣言……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13615837/man-utd-transfer-news-brentford-defender-nathan-collins-emerges-as-january-target-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二报纸的热门报道和转移谣言……" data-title="Papers: Brentford defender emerges as Man Utd target as January budget revealed" data-date="11-24 06:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 06:40</span>
          <span class="news-item-title">Papers: Brentford defender emerges as Man Utd target as January budget revealed</span>
          <span class="news-value-point">💡 周二报纸的热门报道和转移谣言……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13615825/goal-v-janelt-67-brentford-3-0-everton" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Janelt rifles rocket for Brentford’s third against Everton in the Premier League" data-title="WHAT A STRIKE! Janelt rifles rocket for Brentford’s third" data-date="11-24 05:41" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 05:41</span>
          <span class="news-item-title">WHAT A STRIKE! Janelt rifles rocket for Brentford’s third</span>
          <span class="news-value-point">💡 Janelt rifles rocket for Brentford’s third against Everton in the Premie…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/brentford-vs-everton/report/559546" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Keane Lewis-Potter’s first-half double set Brentford on their way to a comprehensive 4-0 Premier League win over 10-man Everton." data-title="Lewis-Potter scores twice as Brentford thump four past 10-man Everton" data-date="11-24 05:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 05:30</span>
          <span class="news-item-title">Lewis-Potter scores twice as Brentford thump four past 10-man Everton</span>
          <span class="news-value-point">💡 Keane Lewis-Potter’s first-half double set Brentford on their way to a c…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025499/man-city-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City latest: De Bruyne speaks for first time on club&#39;s guilty verdict" data-title="Man City latest: De Bruyne speaks for first time on club&#39;s guilty verdict" data-date="11-24 05:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 05:10</span>
          <span class="news-item-title">Man City latest: De Bruyne speaks for first time on club's guilty verdict</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13615787/off-j-tarkowski-40-brentford-2-0-everton" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="VAR controversy as Tarkowski sent off after review during Everton&#39;s Premier League match against Brentford." data-title="RED CARD! VAR controversy as Tarkowski sent off after review" data-date="11-24 04:46" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 04:46</span>
          <span class="news-item-title">RED CARD! VAR controversy as Tarkowski sent off after review</span>
          <span class="news-value-point">💡 VAR controversy as Tarkowski sent off after review during Everton's Prem…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13615552/are-manchester-united-in-a-relegation-battle-gary-neville-and-jamie-carragher-assess-their-survival-chances" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="What started as a blip has become a problem far more systemic for Man Utd." data-title="Are Man Utd genuinely in a relegation battle?" data-date="11-24 03:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 03:45</span>
          <span class="news-item-title">Are Man Utd genuinely in a relegation battle?</span>
          <span class="news-value-point">💡 What started as a blip has become a problem far more systemic for Man Ut…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13615552/are-manchester-united-in-a-relegation-battle-gary-neville-and-jamie-carragher-assess-their-survival-chances" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="What started as a blip has become a problem far more systemic for Man Utd." data-title="Are Man Utd genuinely in a relegation battle?" data-date="11-24 03:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 03:45</span>
          <span class="news-item-title">Are Man Utd genuinely in a relegation battle?</span>
          <span class="news-value-point">💡 What started as a blip has become a problem far more systemic for Man Ut…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/brentford-vs-everton/live/559546" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Grealish on bench for Everton as Wilson starts for Brentford LIVE!" data-title="Grealish on bench for Everton as Wilson starts for Brentford LIVE!" data-date="11-24 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 02:30</span>
          <span class="news-item-title">Grealish on bench for Everton as Wilson starts for Brentford LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! Williams-Barnett agrees long-term Spurs contract" data-title="Transfer Centre LIVE! Williams-Barnett agrees long-term Spurs contract" data-date="11-24 01:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 01:30</span>
          <span class="news-item-title">Transfer Centre LIVE! Williams-Barnett agrees long-term Spurs contract</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Carragher gives relegation verdict" data-title="Man Utd latest: Carragher gives relegation verdict" data-date="11-24 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 01:00</span>
          <span class="news-item-title">Man Utd latest: Carragher gives relegation verdict</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/031/256.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，科技媒体 GSMArena 昨日（11 月 23 日）发布博文，报道称摩托罗拉首款宽折叠手机 Razr Flex 已通过无线充电联盟（WPC）认证，型号为 XT2761。根据认证信息显示，该机支持扩展功率配置文件（EPP），标准无线充电功率最高为 15W；此前传闻中的 25W 无线快充，可能需要通过其他协议或厂商私有方案才能实现。IT之家附上相关截图如下：不过“证件照”尚未正确对应手机外观，所附图片仍显示传统纵向翻盖式 Razr，应该只是认证资料中的占位图。发布时间方面，早前消息曾指向 12 月中旬亮相，但摩托罗拉官方支持网站的线索则暗示 Razr Flex 或将推迟至 2027 年上市。" data-title="摩托罗拉首款宽折叠手机 Razr Flex 通过认证，15W 无线充电" data-date="11-24 07:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:44</span>
          <span class="news-item-title">摩托罗拉首款宽折叠手机 Razr Flex 通过认证，15W 无线充电</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，科技媒体 GSMArena 昨日（11 月 23 日）发布博文，报道称摩托罗拉首款宽折叠手机 Razr Fle…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10736737.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凌晨，宋星在自家烧烤店出完最后一单外卖餐，准备打烊。“滴滴——”外卖平台后台的提示音突然响起，宋星心里猛地一沉。点开评论区，是10多条匿名账号发来的信息：“有异味”“吃后拉肚子”“中毒”……没有图片、视频，更奇怪的是这些差评连着的是四星好评。这已经不是第一次了，他越发认为：这不是普通消费者表达不满，而是恶意差评。" data-title="谁在操控“恶意差评”" data-date="11-24 07:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 07:38</span>
          <span class="news-item-title">谁在操控“恶意差评”</span>
          <span class="news-value-point">💡 凌晨，宋星在自家烧烤店出完最后一单外卖餐，准备打烊</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/255.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，瑞典厂商 Teenage Engineering 现已推出复古 CD 播放器 EP / BC-1。该产品主要面向专业用户和 DJ，采用模块化设计，可以安装扬声器配件。据介绍，EP / BC-1 采用复古的浅灰色设计，外观很容易让人联想到 20 世纪 90 年代的电子产品。该机内置电池，续航时间可达 6 小时。配备 USB-C 接口，支持 CD 抓轨功能，采样规格为 16-bit/44.1 kHz。同时，该 CD 播放器支持将播放速度调整为 50%-150%，配备数码显示屏，可以显示当前曲目、播放时间以及 VU 音量表。用户可以通过蓝牙或 3.5 mm AUX 接口连接耳机和扬声器。此外，Teenage Engineering 还为这款播放器推出了配套的 K." data-title="Teenage Engineering 推出复古 CD 播放器 EP / BC" data-date="11-24 07:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:37</span>
          <span class="news-item-title">Teenage Engineering 推出复古 CD 播放器 EP / BC</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，瑞典厂商 Teenage Engineering 现已推出复古 CD 播放器 EP / BC-1</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/254.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，红魔 12 Pro+ 全新“氘锋透明冰蓝”配色将于 11 月 24 日 10:00 正式开售，16GB+512GB 版本 7999 元，部分地区政府补贴 500 元，到手价 7499 元起。京东红魔 12 Pro+ 氘锋透明冰蓝 7499 元直达链接IT之家此前报道，红魔 12 Pro+ 手机于 10 月 15 日发布，提供氘锋透明暗夜、氘锋透明银翼、氘锋透明冰蓝三款透明配色。机身采用红魔独家纯平背板，背部使用独家一体化镜片后盖，主打镜片级透光、耐磨与抗刮花，并把水冷系统做成可视化，红魔称其为行业唯一风冷、水冷双散热手机。▲ IT之家开箱：红魔 12 Pro+ 氘锋透明冰蓝，下同该机搭载第九代屏下技术，带来行业首款 185Hz 全面屏，采用“电竞双芯”：第六" data-title="红魔 12 Pro+ 氘锋透明冰蓝今日开售：16GB+512GB 版 7499 元" data-date="11-24 07:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:34</span>
          <span class="news-item-title">红魔 12 Pro+ 氘锋透明冰蓝今日开售：16GB+512GB 版 7499 元</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，红魔 12 Pro+ 全新“氘锋透明冰蓝”配色将于 11 月 24 日 10:00 正式开售，16GB+512…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1040966/arion-kurtaj-gta-vi-leaks-sentenced-released" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Arion Kurtaj, who pleaded guilty last week to hacking Grand Theft Auto VI developer Rockstar Games and other companies, including Uber and Revolut, was sentenced to seven years in prison but released on license, the BBC reports. After hacking Rockstar, Kurtaj leaked 90 videos of GTA VI in 2022, years before the game&#39;s public release […]" data-title="The hacker behind early GTA VI leaks has been sentenced" data-date="11-24 07:25" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 07:25</span>
          <span class="news-item-title">The hacker behind early GTA VI leaks has been sentenced</span>
          <span class="news-value-point">💡 Arion Kurtaj, who pleaded guilty last week to hacking Grand Theft Auto V…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1026041/holiday-gift-guide-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="送礼不仅仅是在确定的消费限额下获取可靠的东西。这是一种爱的表达，一种向别人展示你真正了解他们的方式。但是，这并不意味着您必须自己完成所有工作。有时您只需" data-title="The Verge’s 2026 holiday gift guide" data-date="11-24 07:14" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 07:14</span>
          <span class="news-item-title">The Verge 2026年节日礼品指南</span>
          <span class="news-item-title-en">The Verge’s 2026 holiday gift guide</span>
          <span class="news-value-point">💡 送礼不仅仅是在确定的消费限额下获取可靠的东西</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13615841/lpga-tour-q-series-megan-khang-secures-tour-card-for-2027-as-megha-ganne-wins-final-qualifying-stage" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Megha Ganne won the 2026 LPGA Q-Series final qualifying stage as 27 tour cards were claimed for the 2027 season, with five-time USA Solheim Cup team member Megan Khang among those successful." data-title="Five-time Solheim Cup player Khang secures LPGA Tour card for 2027" data-date="11-24 06:26" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 06:26</span>
          <span class="news-item-title">Five-time Solheim Cup player Khang secures LPGA Tour card for 2027</span>
          <span class="news-value-point">💡 Megha Ganne won the 2026 LPGA Q-Series final qualifying stage as 27 tour…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/health/measles-adults-vaccine-boosters.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="The danger is greatest for those who are unvaccinated, but vaccinated people born before 1989 may no longer be sufficiently protected, medical experts said." data-title="Measles Is a Growing Risk for Adults in the United States" data-date="11-24 06:19" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 06:19</span>
          <span class="news-item-title">Measles Is a Growing Risk for Adults in the United States</span>
          <span class="news-value-point">💡 The danger is greatest for those who are unvaccinated, but vaccinated pe…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/networking/routers/grab-a-speedy-tp-link-tri-band-wi-fi-7-router-for-less-than-usd90-archer-be9500-router-is-55-percent-off-sports-10-gbe-wan-and-two-2-5-gbe-lan-ports" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TP-Link is aiming for the value crown with a $90 tri-band Wi-Fi 7 router." data-title="Grab a TP-Link tri-band Wi-Fi 7 router for less than $90" data-date="11-24 06:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 06:00</span>
          <span class="news-item-title">Grab a TP-Link tri-band Wi-Fi 7 router for less than $90</span>
          <span class="news-value-point">💡 TP-Link is aiming for the value crown with a $90 tri-band Wi-Fi 7 router…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13615831/henry-patten-ends-partnership-with-harri-heliovaara-to-team-up-with-fellow-briton-neal-skupski" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Henry Patten has ended his world No 1 doubles partnership with Harri Heliovaara in shock fashion in favour of teaming up with British compatriot Neal Skupski for 2027." data-title="Patten ends Grand Slam-winning doubles pairing to partner fellow Brit Skupski" data-date="11-24 06:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 06:00</span>
          <span class="news-item-title">Patten ends Grand Slam-winning doubles pairing to partner fellow Brit Skupski</span>
          <span class="news-value-point">💡 Henry Patten has ended his world No 1 doubles partnership with Harri Hel…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1034512/apple-watch-series-12-black-friday-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="If you’re still sporting an Apple Watch that launched five or so years ago, now is a good time to upgrade. Apple’s latest smartwatch, the 42mm Apple Watch Series 12 with Wi-Fi and GPS connectivity, has dropped to a new all-time low of $299 ($100 off) at Amazon and Walmart, beating its most sale price […]" data-title="The Apple Watch Series 12 is cheaper than ever ahead of Black Friday" data-date="11-24 05:36" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 05:36</span>
          <span class="news-item-title">在黑色星期五之前，Apple Watch Series 12的价格比以往任何时候都便宜。</span>
          <span class="news-item-title-en">The Apple Watch Series 12 is cheaper than ever ahead of Black Friday</span>
          <span class="news-value-point">💡 If you’re still sporting an Apple Watch that launched five or so years a…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/macbook-neo-falls-to-all-time-low-usd599-in-amazon-black-friday-sale-256gb-citrus-model-price-matches-its-original-launch" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Apple&#39;s MacBook Neo in citrus is down to $599, its original launch price from earlier this year, at Amazon." data-title="MacBook Neo falls to all-time low $599 in Amazon Black Friday sale — 256GB Citrus model price matches its original launch (Update: now $649)" data-date="11-24 05:09" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 05:09</span>
          <span class="news-item-title">MacBook Neo falls to all-time low $599 in Amazon Black Friday sale — 256GB Citrus model price matches its original launch (Update: now $649)</span>
          <span class="news-value-point">💡 Apple's MacBook Neo in citrus is down to $599, its original launch price…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/grab-this-usd1199-asus-prime-rtx-5070-ti-for-a-1440p-or-4k-gaming-upgrade-best-buy-deal-gets-you-into-high-end-blackwell-for-hundreds-less" target="_blank" rel="noopener" data-cat="zonghe" data-summary="RTX 5070 Ti graphics cards have been selling for close to twice their MSRP of late, but you can this Asus card for $1199 at Best Buy right now — the cheapest we&#39;ve seen so far in the Black Friday frenzy." data-title="Grab this $1199 Asus Prime RTX 5070 Ti for a 1440p or 4K gaming upgrade" data-date="11-24 03:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 03:58</span>
          <span class="news-item-title">Grab this $1199 Asus Prime RTX 5070 Ti for a 1440p or 4K gaming upgrade</span>
          <span class="news-value-point">💡 RTX 5070 Ti graphics cards have been selling for close to twice their MS…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/style/amy-nelson-riveter-amazon-fbi-investigation.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Amy Nelson, a champion of women in the “girlboss” era, found her family in Amazon’s cross hairs and found herself in a new role as anti-corporate crusader." data-title="Amy Nelson Was a Corporate Feminist Darling. Then a Corporation Upended Her Life." data-date="11-24 03:33" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 03:33</span>
          <span class="news-item-title">Amy Nelson Was a Corporate Feminist Darling. Then a Corporation Upended Her Life.</span>
          <span class="news-value-point">💡 Amy Nelson, a champion of women in the “girlboss” era, found her family …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1040357/nothing-ear-note-earbuds-ai-recording" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Nothing&#39;s new AI device is the Ear Note, a set of earbuds and their microphone-equipped charging case that can record and transcribe conversations, with a connected app to manage the recordings, transcriptions and AI-generated summaries, similar to Apple&#39;s new Watch feature and devices like Amazon&#39;s Bee wearable. Nothing CEO Carl Pei demonstrated t" data-title="Nothing’s upcoming Ear Note is a pair of earbuds with AI transcription" data-date="11-24 03:04" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-24 03:04</span>
          <span class="news-item-title">Nothing’s upcoming Ear Note is a pair of earbuds with AI transcription</span>
          <span class="news-value-point">💡 Nothing's new AI device is the Ear Note, a set of earbuds and their micr…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-24 08:08（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
