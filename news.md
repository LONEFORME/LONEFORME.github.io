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
      <span>2026-09-08 20:14 抓取更新</span>
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
        <span class="channel-count">52</span>
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
        <span class="channel-count">7</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-08/10692839.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月8日电 9月8日，中共中央政治局委员、外交部长王毅在北京同卡塔尔首相兼外交大臣穆罕默德举行会谈。" data-title="王毅同卡塔尔首相兼外交大臣会谈：愿同卡方等地区各方加强沟通协调" data-date="09-08 20:10" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-08 20:10</span>
      </div>
      <h2 class="hero-featured-title">王毅同卡塔尔首相兼外交大臣会谈：愿同卡方等地区各方加强沟通协调</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/0/999/910.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，掌阅旗下 Tango2S 黑白墨水屏手机造型电纸书现已在京东发售，该机配备一块 5.84 英寸 300PPI Carta 1300 面板，定价 1799 元，今日首发价 1599 元。京东掌阅 Tango 2S 5.84 英寸智能阅读本 1599 元直达链接其整体尺寸 154.3 x 77.3 x 7.7mm，重量 147g，采用一块 5.84 英寸 1576x788 分辨率（300PPI）黑白墨水屏 Carta 1300 面板，支持 50 帧 / 秒快刷技术。该机配备蓝牙 5.0 技术，内置“8 核处理器”，匹配 4GB RAM 和 64GB 存储空间，内置 3900 毫安时电池，IT之家附产品参数如下：" data-title="掌阅 Tango2S 墨水屏电纸书发布：5.84 英寸 Carta 1300 面板，首发价 1599 元" data-date="09-08 20:09" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">掌阅 Tango2S 墨水屏电纸书发布：5.84 英寸 Carta 1300 面板，首发价 1599 元</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/09-08/10692381.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 “《原野》回响——中法歌剧艺术分享会”当地时间4日在巴黎中国文化中心举办。中国歌剧舞剧院演出团当天为150余名法国观众带来了一场中法歌剧艺术的对话。" data-title="“《原野》回响" data-date="09-08 11:31" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">“《原野》回响</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/09-08/10692835.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网云南迪庆9月8日电 (时文枝)“22年来，沪迪对口支援已从传统帮扶迭代为山海联动、优势互补、双向赋能、互利共赢的高质量协作新格局，成为迪庆补齐发展短板、激活乡村动能、夯实振兴根基的关键支撑。”8日，云南省迪庆藏族自治州农业农村局党委书记、局长孙红梅在沪迪对口支援研讨会上如是说。" data-title="从“输血”到“造血” 沪迪协作22载让高原振兴路越走越宽" data-date="09-08 20:11" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">从“输血”到“造血” 沪迪协作22载让高原振兴路越走越宽</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692839.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月8日电 9月8日，中共中央政治局委员、外交部长王毅在北京同卡塔尔首相兼外交大臣穆罕默德举行会谈。" data-title="王毅同卡塔尔首相兼外交大臣会谈：愿同卡方等地区各方加强沟通协调" data-date="09-08 20:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:10</span>
          <span class="news-item-title">王毅同卡塔尔首相兼外交大臣会谈：愿同卡方等地区各方加强沟通协调</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692827.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月8日电 (记者 陈杭)记者8日从北京市人大获悉，北京市区和乡镇人大换届选举工作已全面展开，宣传发动和选民集中登记工作正在进行。此次换届选举涉及全市16个区、近180个乡镇，将直接选举产生近4900名区人大代表和一万余名乡镇人大代表。" data-title="北京市区和乡镇人大换届选举全面展开" data-date="09-08 20:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:09</span>
          <span class="news-item-title">北京市区和乡镇人大换届选举全面展开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692834.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月8日电 综合报道，伊朗总统佩泽希齐扬8日在社交媒体上发文表示，伊朗将继续全力抵抗，直到侵略者感到后悔为止。" data-title="伊朗总统最新发声：将全力抵抗直到侵略者后悔为止" data-date="09-08 20:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:01</span>
          <span class="news-item-title">伊朗总统最新发声：将全力抵抗直到侵略者后悔为止</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692831.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月8日电 综合伊朗媒体8日报道，伊朗拉斯克发生恐怖袭击，民兵武装“动员穷人组织”的一名指挥官在袭击中死亡。" data-title="伊朗发生恐怖袭击 一名民兵武装指挥官身亡" data-date="09-08 20:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:00</span>
          <span class="news-item-title">伊朗发生恐怖袭击 一名民兵武装指挥官身亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692823.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京9月8日电 9月8日晚，国家主席习近平应约同英国首相伯纳姆通电话。" data-title="习近平同英国首相伯纳姆通电话" data-date="09-08 19:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:47</span>
          <span class="news-item-title">习近平同英国首相伯纳姆通电话</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/08/business/oil-prices-iran-war.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="分析师表示，他们预计国际基准布伦特原油价格将在今年剩余时间内保持高位。" data-title="胡塞武装袭击后油价攀升至每桶 100 美元" data-date="09-08 19:45" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-08 19:45</span>
          <span class="news-item-title">胡塞武装袭击后油价攀升至每桶 100 美元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692820.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京9月8日电 9月8日，国务院以“高质量推进城市更新、促进城市内涵式发展”为主题，进行第二十一次专题学习。国务院总理李强在主持学习时强调，要深入学习贯彻习近平总书记关于城市更新工作的重要指示精神和党中央有关决策部署，建立可持续的城市更新模式，促进城市结构优化、功能完善、文脉赓续、品质提升，以城市高质量发展更好满足人民美好生活需要。" data-title="李强主持国务院第二十一次专题学习" data-date="09-08 19:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:40</span>
          <span class="news-item-title">李强主持国务院第二十一次专题学习</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692817.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社罗马9月8日电(记者 李洋)联合国粮农组织渔业委员会第37届会议当地时间7日在位于意大利罗马的粮农组织总部开幕。" data-title="联合国粮农组织渔业委员会第37届会议在罗马开幕" data-date="09-08 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:29</span>
          <span class="news-item-title">联合国粮农组织渔业委员会第37届会议在罗马开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692816.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月8日电(记者 韩辉)韩国知名医美预约平台“江南姐姐”(Gangnam Unni)发生用户个人信息泄露事件。运营方Healing Paper表示，共计219665名用户受影响，其中包括近5000名中国人。" data-title="韩国医美平台“江南姐姐”22万用户信息泄露 近5000中国人受波及" data-date="09-08 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:29</span>
          <span class="news-item-title">韩国医美平台“江南姐姐”22万用户信息泄露 近5000中国人受波及</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692806.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉9月8日电(记者 周璟)菲律宾统计局(PSA)8日公布的劳动力调查数据显示，2026年7月该国失业率升至6%，为2022年6月以来最高水平。当月失业人数达314万，创2021年12月以来最高。" data-title="菲律宾7月失业率升至6% 创四年多新高" data-date="09-08 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:28</span>
          <span class="news-item-title">菲律宾7月失业率升至6% 创四年多新高</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社罗马9月8日电(记者 李洋)《关于预防、制止和消除非法、不报告、不管制捕鱼的港口国措施协定》(“港口国措施协定”)十周年高级别活动当地时间7日在意大利罗马举行。" data-title="“港口国措施协定”十周年高级别活动在罗马举行" data-date="09-08 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:28</span>
          <span class="news-item-title">“港口国措施协定”十周年高级别活动在罗马举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692785.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网海口9月8日电 (张茜翼 王俞力)记者8日从海南省第八届少数民族传统体育运动会新闻发布会获悉，本届运动会将于10月16日至21日在陵水黎族自治县举行。这是海南自贸港全岛封关运作后的首个完整年度举办的重大民族体育活动。" data-title="海南省第八届少数民族传统体育运动会10月在陵水举行" data-date="09-08 19:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:13</span>
          <span class="news-item-title">海南省第八届少数民族传统体育运动会10月在陵水举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692780.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月8日电 (记者 张素)记者从中国最高人民法院获悉，9月8日，河南省信阳市中级人民法院一审公开宣判山西省委原副书记、省政府原省长金湘军受贿一案。" data-title="山西省原省长金湘军一审被判死缓" data-date="09-08 19:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:11</span>
          <span class="news-item-title">山西省原省长金湘军一审被判死缓</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/08/world/middleeast/saudi-arabia-yemen-houthis-energy-attack.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="最近的升级有可能将沙特阿拉伯和伊朗支持的胡塞民兵拖入全面战争。" data-title="沙特阿拉伯誓言在胡塞武装袭击造成数十人受伤后进行报复" data-date="09-08 18:54" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-08 18:54</span>
          <span class="news-item-title">沙特阿拉伯誓言在胡塞武装袭击造成数十人受伤后进行报复</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692745.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月8日电 综合消息：伊朗媒体8日报道称，伊朗外交部长阿拉格齐表示，伊朗议会正在审议霍尔木兹海峡未来管理事项，多部门专家参与。伊拉克、卡塔尔、阿联酋等国就霍尔木兹海峡通航问题密集表态。" data-title="伊朗正审议霍尔木兹海峡管理事项 多国就海峡通航表态" data-date="09-08 18:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 18:52</span>
          <span class="news-item-title">伊朗正审议霍尔木兹海峡管理事项 多国就海峡通航表态</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/999/910.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，掌阅旗下 Tango2S 黑白墨水屏手机造型电纸书现已在京东发售，该机配备一块 5.84 英寸 300PPI Carta 1300 面板，定价 1799 元，今日首发价 1599 元。京东掌阅 Tango 2S 5.84 英寸智能阅读本 1599 元直达链接其整体尺寸 154.3 x 77.3 x 7.7mm，重量 147g，采用一块 5.84 英寸 1576x788 分辨率（300PPI）黑白墨水屏 Carta 1300 面板，支持 50 帧 / 秒快刷技术。该机配备蓝牙 5.0 技术，内置“8 核处理器”，匹配 4GB RAM 和 64GB 存储空间，内置 3900 毫安时电池，IT之家附产品参数如下：" data-title="掌阅 Tango2S 墨水屏电纸书发布：5.84 英寸 Carta 1300 面板，首发价 1599 元" data-date="09-08 20:09" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 20:09</span>
          <span class="news-item-title">掌阅 Tango2S 墨水屏电纸书发布：5.84 英寸 Carta 1300 面板，首发价 1599 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/909.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，据彭博社今天（8 日）晚间报道，经济合作与发展组织（OECD）最新教育报告显示，不使用或较少使用 AI 聊天机器人完成课业的学生，整体表现优于经常使用 AI 的学生。报告提供了迄今覆盖范围最广的一批证据，显示 AI 可能对儿童学习产生负面影响。报告指出，从不或几乎从不使用 AI 为写作作业起草文本的学生，科学测试平均得分为 509 分；每天或几乎每天使用 AI 完成这类任务的学生平均只有 481 分。即使控制社会经济地位因素，两组学生仍相差 28 分，约相当于一年半的教学差距。经合组织教育与技能司司长安德烈亚斯 · 施莱歇尔指出，就像观看体育比赛不会让我们变得强健，只有亲自运动才能做到一样，学习也不是靠被动接收内容完成的，而是需要大脑面对新材料时主动进行认知上的" data-title="经合组织最新报告：不用或少用 AI 完成课业的学生，整体表现优于常用 AI 的学生" data-date="09-08 20:09" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 20:09</span>
          <span class="news-item-title">经合组织最新报告：不用或少用 AI 完成课业的学生，整体表现优于常用 AI 的学生</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/907.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，六联智能 (SIXUNITED) 今日发布了全球首批搭载 AMD 锐龙 AI Max+ 400 &quot;Gorgon Halo&quot; 处理器的笔记本电脑 AXN88B-160M-YD。这款笔电性能释放可达 120W；支持 192GB LPDDR5X-8533 内存，提供 2 个 M.2 2280 (PCIe Gen4 ×4) SSD 盘位；搭载可翻转 145° 的 16&quot; 2560×1600 120Hz 广色域屏幕；配套 Wi-Fi 7 &amp; 蓝牙 5.4 无需网卡。AXN88B-160M-YD 采用金属机身，内含 99.9Whr / 85Whr 电池，集成 2MP + IR 相机模组、2 个 2W 4Ω 扬声器，提供全键 RGB 背光键盘，支持指纹识别。其机身厚度 18." data-title="六联智能发布全球首批 &quot;Gorgon Halo&quot; 笔电 AXN88B" data-date="09-08 20:07" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 20:07</span>
          <span class="news-item-title">六联智能发布全球首批 "Gorgon Halo" 笔电 AXN88B</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692825.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社台北9月8日电 受益于人工智能与半导体产业的强劲需求，台湾今年上半年经济表现突出，但不同产业与群体之间的感受差异明显。台湾《经济日报》近日一篇社论指出，岛内正逐步形成“双速经济”格局。" data-title="AI难惠及传统产业 台媒指台湾经济呈“双速”格局" data-date="09-08 20:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:06</span>
          <span class="news-item-title">AI难惠及传统产业 台媒指台湾经济呈“双速”格局</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/08/business/stock-market-interest-rates.html" target="_blank" rel="noopener" data-cat="keji" data-summary="投资者关注强劲的企业盈利和人工智能，同时关注伊朗战争。但利率上升给股市上涨带来的风险越来越大。" data-title="为什么股票会反抗重力以及什么会导致它们下跌" data-date="09-08 20:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-08 20:03</span>
          <span class="news-item-title">为什么股票会反抗重力以及什么会导致它们下跌</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/all-in-one-dlss-unlocked-mod-brings-dlss-5-and-multi-frame-gen-to-rtx-20-30-and-40-series-hybrid-tool-taps-amd-fsr-3-1-to-boost-frame-rates-up-to-6x" target="_blank" rel="noopener" data-cat="keji" data-summary="该模组的性能尚未经过测试，但 DLSS Unlocked 的纯粹实用性很容易将其置于 RTX GPU 模组列表的首位。它将 OptiScaler_DLSSNR 与 DLSS Enabled 相结合，为所有 RTX GPU 带来神经渲染和多帧生成。" data-title="一体化“DLSS Unlocked”模组为 RTX 20、30 和 40 系列带来 DLSS 5 和多帧生成 — 混合工具利用 AMD FSR 3.1 将帧速率提高至 6 倍" data-date="09-08 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-08 20:00</span>
          <span class="news-item-title">一体化“DLSS Unlocked”模组为 RTX 20、30 和 40 系列带来 DLSS 5 和多帧生成 — 混合工具利用 AMD FSR 3.1 将帧速率提高至 6 倍</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/991141/apple-first-foldable-iphone-launch-influence-john-ternus" target="_blank" rel="noopener" data-cat="keji" data-summary="苹果几乎肯定会在明天推出首款可折叠 iPhone，距离三星 Galaxy Fold 首次上市七年。尽管苹果可能迟到了几年，但这次发布会的筹备证明了新任首席执行官约翰·特努斯(John Ternus)继承了一家一如既往具有影响力的公司。 […]" data-title="苹果说“折叠”，竞争对手问“多宽？”" data-date="09-08 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-08 20:00</span>
          <span class="news-item-title">苹果说“折叠”，竞争对手问“多宽？”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/905.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，据路透社报道，一项全球学生评估显示，如今青少年的阅读水平已跌至本世纪以来的最低点，并进一步拖累整体教育表现。经济合作与发展组织（OECD）2025 年对全球 91 个国家和经济体的 76 万名 15 岁学生进行的测试显示，学生的阅读、数学和科学成绩均跌至 2000 年开始收集相关数据以来的最低水平。根据 OECD 周二公布的最新国际学生评估项目（PISA）报告，如今学生的平均阅读水平相当于过去比他们小一岁的学生所达到的水平。PISA 阅读成绩曾在 2012 年达到 501 分的高点，但到去年已经下降至 466 分。PISA 被广泛认为是全球最重要的教育表现评估指标之一，其结果一直受到各国政府和教育工作者的密切关注。OECD 秘书长马蒂亚斯 · 科尔曼在新闻发布会" data-title="受屏幕时间激增影响，青少年阅读水平跌至本世纪最低" data-date="09-08 19:58" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 19:58</span>
          <span class="news-item-title">受屏幕时间激增影响，青少年阅读水平跌至本世纪最低</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/904.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，工信部发布第 411 批《道路机动车辆生产企业及产品公告》新产品公示，华晨宝马除了带来新世代 i3 轿车以外，还带来了新世代的 iX3 纯电 SUV，此次申报的车型具体为 iX3 30L。IT之家注意到，该车型为纯电动多用途乘用车，由华晨宝马汽车有限公司生产，长宽高分别为 4885/1895/1634mm，轴距达到 3005mm，整备质量 2230kg，总质量 2680kg，额定载客 5 人，最高车速 180km/h。该车提供轮胎规格可选，包括 255/40 R21 和 255/45 R20，同时支持选装制动钳、轮辋、饰条以及车顶后摄像头，还可选装 ETC 车载装置，标配汽车事件数据记录系统（EDR），防抱死制动系统型号为 IBC2，由 ZF Group（采埃孚" data-title="华晨宝马新世代 iX3 纯电 SUV 申报：此前已开启预订，26.99 万" data-date="09-08 19:48" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 19:48</span>
          <span class="news-item-title">华晨宝马新世代 iX3 纯电 SUV 申报：此前已开启预订，26.99 万</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/quantum-computing/nec-has-quietly-quit-quantum-computing-hardware-development-report-claims-company-says-it-will-continue-to-evaluate-practical-applications-and-industrialization-of-quantum-technologies" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，NEC 已停止量子计算机的开发，但计划探索此类系统的实际应用。" data-title="报道称，NEC 已悄然退出量子计算硬件开发，该公司表示将继续评估量子技术的实际应用和产业化" data-date="09-08 19:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-08 19:45</span>
          <span class="news-item-title">报道称，NEC 已悄然退出量子计算硬件开发，该公司表示将继续评估量子技术的实际应用和产业化</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/903.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，Alphabet 旗下谷歌当地时间周二宣布调整其在欧洲地区的在线搜索结果，以满足欧盟反垄断监管机构的要求。谷歌表示，这一调整将降低用户的搜索体验，同时增加欧洲企业的运营成本。谷歌一名高管向路透社表示，这是这家全球最受欢迎的互联网搜索引擎成立 29 年来，对服务质量做出的最大幅度削减。谷歌表示，欧盟将此次调整定位为让不同企业在广告竞争中获得更加公平的机会。然而，谷歌认为，实际结果可能恰恰相反，因为这些变化将更有利于价格比较网站，也就是所谓的垂直搜索服务（VSS）。这类服务覆盖酒店、航空、餐饮等行业，例如 Expedia 和 Booking.com。按照新的搜索结果展示方式，这些垂直搜索服务的排名和曝光度将高于相关行业中那些仅提供网站链接、电话号码和地址的企业。今年" data-title="谷歌为避免欧盟罚款调整欧洲搜索结果，称搜索质量大幅降低" data-date="09-08 19:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 19:44</span>
          <span class="news-item-title">谷歌为避免欧盟罚款调整欧洲搜索结果，称搜索质量大幅降低</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/902.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，工信部发布第 411 批《道路机动车辆生产企业及产品公告》新产品公示，华晨宝马国产的宝马新世代 i3 40L 纯电动轿车完成申报。宝马 i3 40L 定位纯电动轿车，长宽高为 4864/1865/1490mm，轴距达到 3005mm，整备质量 2074kg，总质量 2550kg，额定载客（含驾驶员）座位数为 5 人，最高车速 200km/h。动力方面，该车搭载型号为 HD1001N0 的驱动电机，峰值功率为 235 kW，配备三元锂离子动力电池，储能装置单体由宁德时代生产，储能装置总成由华晨宝马生产。IT之家注意到，该车可选装不同样式的轮辋以及不同颜色的制动钳，轮胎规格为 245/40 R20 / 255/40 R20；配备防抱死制动系统，ABS 型号为 IBC" data-title="华晨宝马新世代 i3 纯电轿车申报，计划今年 Q4 上市" data-date="09-08 19:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 19:41</span>
          <span class="news-item-title">华晨宝马新世代 i3 纯电轿车申报，计划今年 Q4 上市</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/retro-gaming/vintage-emulator-studio-recreates-44-legendary-synths-down-to-the-chip-level-free-mame-powered-component-level-emulation-should-offer-exceedingly-accurate-sound" target="_blank" rel="noopener" data-cat="keji" data-summary="Vintage Emulator Studio 将标志性的复古合成器和采样器带入生活 — MAME 驱动的组件级仿真应提供极其准确的声音" data-title="Vintage Emulator Studio 重新创建了 44 个传奇合成器，直至芯片级别 - 免费的 MAME 驱动的组件级模拟应该提供极其准确的声音" data-date="09-08 19:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-08 19:40</span>
          <span class="news-item-title">Vintage Emulator Studio 重新创建了 44 个传奇合成器，直至芯片级别 - 免费的 MAME 驱动的组件级模拟应该提供极其准确的声音</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/991190/lg-tv-spying-standby-recording-wi-fi-scanning-gamers-nexus" target="_blank" rel="noopener" data-cat="keji" data-summary="根据 YouTube 频道 Gamers Nexus 的一份新报告，LG 智能电视几乎不断记录和上传有关用户及其家庭的数据，即使在离线或待机模式下也是如此。该公司的电视机扫描 Wi-Fi 网络以查找附近的设备，通过麦克风记录音频日志，并使用音频和视频采样来 [...]" data-title="LG 电视即使在离线或待机状态下也会被发现间谍活动" data-date="09-08 19:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-08 19:30</span>
          <span class="news-item-title">LG 电视即使在离线或待机状态下也会被发现间谍活动</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/901.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，英伟达 GeForce RTX 50 系列（代号 Blackwell）显卡目前仍是市场上性能最强的显卡之一。正因如此，这些备受追捧的 Blackwell 显卡也成为诈骗分子眼中的“肥肉”，不法分子试图利用消费者购买显卡的需求实施诈骗。虽然“空壳显卡”骗局并不是什么新鲜事，但近期这类骗局出现得越来越频繁，传播范围也不断扩大，令人担忧。德国最新曝光的案例显示，至少有两名买家遭遇了同一种骗局，而且据称两人面对的还是同一名卖家。“空壳显卡”或“幽灵显卡”可能不是日常生活中常听到的说法。简单来说，这类显卡缺少 GPU 芯片和显存芯片。诈骗分子会将这些关键芯片拆走，再把无法正常工作的显卡卖给受害者。对于普通消费者来说，在拆开显卡之前，基本无法确认这些关键芯片是否存在，而普通" data-title="德国出现 RTX 5090 空壳显卡诈骗：核心显存被拆除，两名买家损失超 4000 欧元" data-date="09-08 19:29" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 19:29</span>
          <span class="news-item-title">德国出现 RTX 5090 空壳显卡诈骗：核心显存被拆除，两名买家损失超 4000 欧元</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692381.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 “《原野》回响——中法歌剧艺术分享会”当地时间4日在巴黎中国文化中心举办。中国歌剧舞剧院演出团当天为150余名法国观众带来了一场中法歌剧艺术的对话。" data-title="“《原野》回响" data-date="09-08 11:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:31</span>
          <span class="news-item-title">“《原野》回响</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692367.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 法国西南部部分地区气温当地时间7日超过40摄氏度，从而突破9月历史同期高温纪录。" data-title="法国西南部气温超过40摄氏度 突破9月历史同期高温纪录" data-date="09-08 11:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:30</span>
          <span class="news-item-title">法国西南部气温超过40摄氏度 突破9月历史同期高温纪录</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692366.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 中国驻法国大使邓励当地时间4日应邀出席第八届吉维尼世界论坛闭幕式，就中欧经贸合作阐述中方立场，介绍中国绿色转型成就。" data-title="中国驻法国大使邓励：中欧经贸相互依赖，应加强对话合作" data-date="09-08 11:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:28</span>
          <span class="news-item-title">中国驻法国大使邓励：中欧经贸相互依赖，应加强对话合作</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj06m1e3e75o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="全球足球主管埃杜在城市球场工作一年多后离开诺丁汉森林。" data-title="埃杜在经历了动荡之后离开了诺丁汉森林" data-date="09-08 00:45" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 00:45</span>
          <span class="news-item-title">埃杜在经历了动荡之后离开了诺丁汉森林</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgrvx1jxrv0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西最近对富勒姆的桑德伯格表现出了兴趣，因为他们试图在恩佐·费尔南德斯离开之前加强中场选择。" data-title="切尔西正在考虑引进富勒姆中场贝尔格" data-date="09-08 00:03" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 00:03</span>
          <span class="news-item-title">切尔西正在考虑引进富勒姆中场贝尔格</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5yw73ppwd1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="接替理查德·休斯的可能候选人——以及利物浦下一任体育总监面临的众多任务。" data-title="谁将成为新任利物浦体育总监——他们面临哪些问题？" data-date="09-07 23:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-07 23:52</span>
          <span class="news-item-title">谁将成为新任利物浦体育总监——他们面临哪些问题？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/07/arsenals-season-could-hardly-have-started-better" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="现在还为时过早，但Mikel Arteta的球队正在发挥他们上赛季有时无法企及的权威和新鲜感在这里注册我们的免费通讯三场联赛，赢了三场比赛。对于阿森纳来说，本赛季只有在曼城（看起来像是他们两个最严肃的挑战者之一）丢掉积分的情况下才能更好地开始。但这不仅仅是结果：阿森纳在eac中表现得更好" data-title="更健康、更快乐、更有成效：阿森纳开局再好不过了乔纳森·威尔逊" data-date="09-07 22:34" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-07 22:34</span>
          <span class="news-item-title">更健康、更快乐、更有成效：阿森纳开局再好不过了乔纳森·威尔逊</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692835.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网云南迪庆9月8日电 (时文枝)“22年来，沪迪对口支援已从传统帮扶迭代为山海联动、优势互补、双向赋能、互利共赢的高质量协作新格局，成为迪庆补齐发展短板、激活乡村动能、夯实振兴根基的关键支撑。”8日，云南省迪庆藏族自治州农业农村局党委书记、局长孙红梅在沪迪对口支援研讨会上如是说。" data-title="从“输血”到“造血” 沪迪协作22载让高原振兴路越走越宽" data-date="09-08 20:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:11</span>
          <span class="news-item-title">从“输血”到“造血” 沪迪协作22载让高原振兴路越走越宽</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692826.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月8日电(林波 曹丹 孙琳茹)沙滩、民宿、海鲜大排档，摩托车不时穿梭在沿海街道之上。浙江省宁波市象山县鹤浦镇的早晨，海风中带着咸湿气。" data-title="浙江“00后”教师与课堂的双向奔赴" data-date="09-08 20:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 20:06</span>
          <span class="news-item-title">浙江“00后”教师与课堂的双向奔赴</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692822.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社南昌9月8日电(记者范帆)记者从江西遂川高坪镇明坑村泥石流灾害救援现场获悉，截至8日18时，5日凌晨发生的泥石流灾害现场已致12人遇难，其中包括1名后续排查出的新增失联人员。目前还有1人失联，救援力量正进一步加大搜救力度。" data-title="江西遂川高坪镇泥石流已致12人遇难" data-date="09-08 19:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:46</span>
          <span class="news-item-title">江西遂川高坪镇泥石流已致12人遇难</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692815.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月8日电 便携式甲醛检测仪靠谱吗？很多网上销售的便携式甲醛检测仪，主要是通过内部的电化学传感器检测甲醛。但受成本和技术限制，这类检测仪精确度往往不够，而且空气温度、湿度以及其他挥发性有机物的存在也可能会影响检测的结果。京津冀三地消协曾经对50个品牌的甲醛检测仪进行过检测，价格从几十元到几千元不等。结果发现没有一款产品能真正做到“精准检测”。(来源：@科学辟谣 中国新闻网微博)" data-title="网上销售的便携式甲醛检测仪，精准度高达99.9%？丨中新真探" data-date="09-08 19:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:21</span>
          <span class="news-item-title">网上销售的便携式甲醛检测仪，精准度高达99.9%？丨中新真探</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692814.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南宁9月8日电(钟闯瑜)南宁海关8日介绍，9月7日凌晨，装载70个外贸空集装箱的“北港南宁博润”轮办结海关监管手续后从钦州港离泊，经平陆运河驶往南宁六景港。这是平陆运河船舶通航全要素综合演练的首艘外贸船舶，标志着平陆运河进入外贸货物运输实战检验阶段。" data-title="平陆运河船舶通航全要素综合演练首艘外贸船舶顺利完成试航" data-date="09-08 19:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:20</span>
          <span class="news-item-title">平陆运河船舶通航全要素综合演练首艘外贸船舶顺利完成试航</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692807.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社银川9月8日电 (记者 杨迪)中国多地老年大学9月初迎来开学季，智能潮流、健康生活相关课程颇受“银发族”学员关注。" data-title="中国“银发族”迎开学季 智能潮流与健康生活课程受关注" data-date="09-08 19:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:18</span>
          <span class="news-item-title">中国“银发族”迎开学季 智能潮流与健康生活课程受关注</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692799.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明9月8日电 (陆希成)云南省人民政府近日印发《云南省“十五五”城市更新行动规划》(下称《规划》)，提出以“近期排危、中期更新、长期提质”为序，统筹推进好房子、好小区、好社区、好城区建设，到2035年基本建成具有边疆民族地区特色的现代化人民城市。" data-title="云南城市更新转向存量提质 力建“四好”" data-date="09-08 19:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:18</span>
          <span class="news-item-title">云南城市更新转向存量提质 力建“四好”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692788.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月8日电(郭其钰)当虚拟数字人在直播间直播时，观众打赏的是数字人形象还是背后的真人？“中之人”(为虚拟形象提供声音和动作捕捉的工作者)驱动虚拟数字人进行直播互动，在“劳动合同+合作协议”混合签约模式下，“中之人”与运营公司之间是合作关系还是劳动关系？" data-title="虚拟主播“中之人”是否算员工？法院认定事实劳动关系" data-date="09-08 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 19:14</span>
          <span class="news-item-title">虚拟主播“中之人”是否算员工？法院认定事实劳动关系</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692736.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月8日电 综合外媒8日报道，位于法国东南部城市滨海卡涅的雷诺阿博物馆当天发生盗窃案，4件艺术品被盗，其中一件在窃贼逃跑过程中被丢弃。据估计，被盗物品总价值约900万欧元。" data-title="突发：法国雷诺阿博物馆遭窃 损失或达900万欧元" data-date="09-08 18:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 18:03</span>
          <span class="news-item-title">突发：法国雷诺阿博物馆遭窃 损失或达900万欧元</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/08/nyregion/9-11-children-health.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="大多数关于接触世贸中心残留物的研究都集中在急救人员身上，但那里的人们年轻时表示他们的健康也面临风险。" data-title="9/11 的灰尘和灰烬覆盖了他们的童年。它仍然让他们生病吗？" data-date="09-08 15:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-08 15:00</span>
          <span class="news-item-title">9/11 的灰尘和灰烬覆盖了他们的童年。它仍然让他们生病吗？</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/689.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 8 日消息，《旅行青蛙 · 中国之旅》手游今日发布停运公告，由于 IP 授权合作到期，《旅行青蛙 · 中国之旅》将于 2026 年 12 月 8 日正式停止运营。2026 年 9 月 8 日 14 时：关闭全平台下载入口，玩家将无法下载本游戏，同时停止游戏充值、新用户注册；2026 年 12 月 8 日 18 时：正式停止游戏运营，关闭游戏服务器；游戏官网下架。届时玩家将无法通过游戏服务器登录游戏。在游戏服务器关闭后，各服务器内有关游戏的所有帐号数据及角色资料等信息将被全部清空。注意：游戏服务器关闭后，玩家将无法再次登录游戏，可自行提前保存希望保留的角色信息，以供于后续其他问题需要提供。游戏官方会针对游戏内未消耗的虚拟货币（近 3 月充值获得的三叶草）提供以下退款方案：（一" data-title="《旅行青蛙 · 中国之旅》手游宣布 12 月 8 日停止运营，IP 授权合作到期" data-date="09-08 14:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:41</span>
          <span class="news-item-title">《旅行青蛙 · 中国之旅》手游宣布 12 月 8 日停止运营，IP 授权合作到期</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692567.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="直播海报：“梅姨案”进入审判阶段 申军良父子分享案件心路历程" data-title="直播海报：“梅姨案”进入审判阶段 申军良父子分享案件心路历程" data-date="09-08 14:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:36</span>
          <span class="news-item-title">直播海报：“梅姨案”进入审判阶段 申军良父子分享案件心路历程</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c87v33gxr01o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="专家称，航母给美国盟友的是心理保证。印太区域没有航母，“会加强一种整体感觉：美国正被中东局势分心。”" data-title="美军航母全数撤离印太：台湾该担心“空窗期”吗？" data-date="09-08 14:35" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 14:35</span>
          <span class="news-item-title">美军航母全数撤离印太：台湾该担心“空窗期”吗？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692566.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="打着“助农”的旗号，却专门骗取种植户的保证金——安徽警方近日侦破一起新型涉农诈骗案，全国各地数百家农户上当受骗，涉案金额超过800万元。" data-title="打着“助农”旗号设局 警方破获新型涉农诈骗案" data-date="09-08 14:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:33</span>
          <span class="news-item-title">打着“助农”旗号设局 警方破获新型涉农诈骗案</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cly4lngg6npo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="纽卡斯尔联队体育总监罗斯·威尔逊表示，俱乐部正在为前主教练埃迪·豪的离职做长达九个月的准备。" data-title="纽卡斯尔为豪的离开“准备了几个月”" data-date="09-08 14:21" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 14:21</span>
          <span class="news-item-title">纽卡斯尔为豪的离开“准备了几个月”</span>
        </a>
  </div>
</div>

<script>
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
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'flex' : 'block') : 'none';
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

<p class="news-updated">🕐 抓取更新于 2026-09-08 20:14（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
