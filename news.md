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
      <span>2026-09-16 20:43 抓取更新</span>
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
        <span class="channel-count">50</span>
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
        <span class="channel-count">5</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-16/10697798.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社南宁9月16日电 9月16日上午，中共中央政治局常委、国务院副总理丁薛祥在广西钦州出席平陆运河通航仪式。" data-title="丁薛祥出席平陆运河通航仪式" data-date="09-16 20:21" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-16 20:21</span>
      </div>
      <h2 class="hero-featured-title">丁薛祥出席平陆运河通航仪式</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/003/284.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 16 日消息，萨姆 · 奥尔特曼（Sam Altman）表示，部分 AI 事故无法完全避免，但关键在于如何从事故当中吸取教训。当地时间周二，这位 OpenAI 首席执行官在赛富时（Salesforce）的 Dreamforce 大会上发表讲话。他提出，科技企业应当建立公开上报事故的企业文化，可以借鉴航空业的做法。“我确实认为，对于一项新兴技术而言，一定程度上的事故是难以避免的。”奥尔特曼说道，“我真正在意的是，我们能够形成一套完善的事故上报与复盘学习机制。”他以美国联邦航空管理局（FAA）和美国国家运输安全委员会（NTSB）作为 AI 行业应当效仿的范例。这两家机构十分重视事故调查，正是这套机制让航空出行变得更加安全。谈及 FAA 与 NTSB 的处置思路，他表示：“事故终" data-title="OpenAI 奥尔特曼：AI 事故无法完全避免，应借鉴航空业建立公开上报机制" data-date="09-16 20:31" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">OpenAI 奥尔特曼：AI 事故无法完全避免，应借鉴航空业建立公开上报机制</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cmx2zyjylee1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，围绕埃尔林·哈兰德（ Erling Haaland ）获胜者的争议给他的球队在曼联的胜利蒙上了阴影，这“相当糟糕”。" data-title="马雷斯卡批评关注有争议的赢家" data-date="09-16 19:07" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">马雷斯卡批评关注有争议的赢家</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/09-16/10697818.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨9月16日电 (记者 史轶夫)一部热播剧带动一座城。随着电视剧《早春晴朗》在Netflix全球榜单创纪录，有旅行平台数据显示，作为剧中主要取景地的哈尔滨旅游搜索热度环比上涨149%。" data-title="影视剧带动文旅热 哈尔滨双节打造追剧打卡新体验" data-date="09-16 20:44" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">影视剧带动文旅热 哈尔滨双节打造追剧打卡新体验</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697798.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社南宁9月16日电 9月16日上午，中共中央政治局常委、国务院副总理丁薛祥在广西钦州出席平陆运河通航仪式。" data-title="丁薛祥出席平陆运河通航仪式" data-date="09-16 20:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:21</span>
          <span class="news-item-title">丁薛祥出席平陆运河通航仪式</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697757.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京9月15日电 题：用心用情服务群众 兢兢业业守护安宁——习近平总书记的回信激励广大公安干警奋发有为再立新功" data-title="用心用情服务群众 兢兢业业守护安宁——习近平总书记的回信激励广大公安干警奋发有为再立新功" data-date="09-16 20:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:20</span>
          <span class="news-item-title">用心用情服务群众 兢兢业业守护安宁——习近平总书记的回信激励广大公安干警奋发有为再立新功</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697802.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月16日电 综合外媒报道，美国肯塔基州共和党籍联邦众议员托马斯·梅西15日在国会众议院提出对美国国防部长赫格塞思的弹劾动议，指控赫格塞思“非法”对伊朗采取敌对军事行动、“绑架外国领导人”。" data-title="共和党议员呼吁弹劾美防长赫格塞思" data-date="09-16 20:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:09</span>
          <span class="news-item-title">共和党议员呼吁弹劾美防长赫格塞思</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697736.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月16日电 (记者 陈建新 徐雪莹)国务院台办例行新闻发布会16日在北京举行，发言人朱凤莲回应平陆运河通航、台海谍战剧《交锋》受两岸观众肯定等热点。" data-title="国台办发布会聚焦平陆运河通航、谍战剧《交锋》受肯定等热点" data-date="09-16 20:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:01</span>
          <span class="news-item-title">国台办发布会聚焦平陆运河通航、谍战剧《交锋》受肯定等热点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697722.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网通辽9月16日电 (记者 张林虎)16日，记者从内蒙古自治区通辽市人民检察院获悉，兴安盟政协原一级巡视员胡春涉嫌受贿罪被提起公诉。" data-title="内蒙古兴安盟政协原一级巡视员胡春被公诉" data-date="09-16 19:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:41</span>
          <span class="news-item-title">内蒙古兴安盟政协原一级巡视员胡春被公诉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697694.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷9月16日电(李映民 王茜)第三届中国研究生国际中文教育案例大赛泰国赛区决赛15日在博仁大学举办。" data-title="第三届中国研究生国际中文教育案例大赛泰国赛区举行决赛" data-date="09-16 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:14</span>
          <span class="news-item-title">第三届中国研究生国际中文教育案例大赛泰国赛区举行决赛</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697678.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科9月16日电(记者 田冰)《友谊之路——孙中山、宋庆龄与俄国》图片展当地时间15日在俄罗斯外交部开幕。展览由中国宋庆龄基金会和俄罗斯起点基金会共同主办，宋庆龄故居管理中心与俄罗斯圣安德鲁基金会联合承办，旨在纪念孙中山先生诞辰160周年，促进新时代中俄两国人民友好。" data-title="《友谊之路" data-date="09-16 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:14</span>
          <span class="news-item-title">《友谊之路</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697668.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网马尼拉9月16日电 菲律宾前众议长、总统小马科斯表弟马丁·罗穆亚尔德斯16日就涉案金额74.4亿菲律宾比索(约合1.19亿美元)的“掠夺罪”指控表示不认罪，其律师表示将申请保释。" data-title="菲前众议长、小马科斯表弟对74.4亿比索“掠夺罪”指控不认罪" data-date="09-16 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:14</span>
          <span class="news-item-title">菲前众议长、小马科斯表弟对74.4亿比索“掠夺罪”指控不认罪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697649.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月16日电 综合消息：沙特阿拉伯、伊斯兰合作组织16日谴责也门胡塞武装对麦加发动袭击。胡塞武装当天否认袭击麦加，并称使用自制导弹击落一架沙特F-15战斗机。" data-title="沙特指责胡塞武装袭击麦加  胡塞武装否认" data-date="09-16 19:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:13</span>
          <span class="news-item-title">沙特指责胡塞武装袭击麦加  胡塞武装否认</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697713.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月16日电 据江西省纪委监委消息：江西省地质局党组成员、副局长赖晓军涉嫌严重违纪违法，目前正接受江西省纪委监委纪律审查和监察调查。" data-title="江西省地质局党组成员、副局长赖晓军接受审查调查" data-date="09-16 19:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:10</span>
          <span class="news-item-title">江西省地质局党组成员、副局长赖晓军接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697710.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月16日电 据重庆市纪委监委消息：经重庆市委批准，重庆市纪委监委对第六届重庆市委委员，市政协原秘书长蓝庆华严重违纪违法问题进行了立案审查调查。" data-title="重庆市政协原秘书长蓝庆华被“双开”" data-date="09-16 19:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:09</span>
          <span class="news-item-title">重庆市政协原秘书长蓝庆华被“双开”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697716.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月16日电 据美国阿克西奥斯新闻网站15日报道，两名以色列官员透露，上周，美国军方秘密召集了以色列和沙特阿拉伯、阿拉伯联合酋长国、巴林、科威特、卡塔尔、约旦、埃及的军方高级官员在德国开会，以讨论伊朗战事和中东地区紧张局势。" data-title="美媒曝：美国召集八国军方密会 为伊朗战事以来首次" data-date="09-16 19:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 19:08</span>
          <span class="news-item-title">美媒曝：美国召集八国军方密会 为伊朗战事以来首次</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-16/10697687.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月16日电 综合外媒报道，乌克兰武装部队无人系统部队司令罗伯特·布罗夫迪16日称，在顿涅茨克地区打死俄军第4独立摩托化步兵旅旅长、少将安东·格鲁尼斯。" data-title="乌克兰军方：打死俄军一名少将" data-date="09-16 18:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 18:52</span>
          <span class="news-item-title">乌克兰军方：打死俄军一名少将</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/16/podcasts/the-headlines/fuel-riots-trump-arms-sales-israel.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="此外，这位俄罗斯商人为小唐纳德·特朗普租了一个岛。" data-title="燃料骚乱蔓延到世界各地，特朗普批准向以色列出售28亿美元的武器" data-date="09-16 18:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-16 18:01</span>
          <span class="news-item-title">燃料骚乱蔓延到世界各地，特朗普批准向以色列出售28亿美元的武器</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-16/10697485.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月16日电 据贵州省纪委监委消息：经贵州省委批准，贵州省纪委监委对贵州省交通运输厅原党委书记、厅长张胤严重违纪违法问题进行了立案审查调查。" data-title="贵州省交通运输厅原党委书记、厅长张胤被“双开”" data-date="09-16 14:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 14:50</span>
          <span class="news-item-title">贵州省交通运输厅原党委书记、厅长张胤被“双开”</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/003/284.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 16 日消息，萨姆 · 奥尔特曼（Sam Altman）表示，部分 AI 事故无法完全避免，但关键在于如何从事故当中吸取教训。当地时间周二，这位 OpenAI 首席执行官在赛富时（Salesforce）的 Dreamforce 大会上发表讲话。他提出，科技企业应当建立公开上报事故的企业文化，可以借鉴航空业的做法。“我确实认为，对于一项新兴技术而言，一定程度上的事故是难以避免的。”奥尔特曼说道，“我真正在意的是，我们能够形成一套完善的事故上报与复盘学习机制。”他以美国联邦航空管理局（FAA）和美国国家运输安全委员会（NTSB）作为 AI 行业应当效仿的范例。这两家机构十分重视事故调查，正是这套机制让航空出行变得更加安全。谈及 FAA 与 NTSB 的处置思路，他表示：“事故终" data-title="OpenAI 奥尔特曼：AI 事故无法完全避免，应借鉴航空业建立公开上报机制" data-date="09-16 20:31" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-16 20:31</span>
          <span class="news-item-title">OpenAI 奥尔特曼：AI 事故无法完全避免，应借鉴航空业建立公开上报机制</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/279.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 16 日消息，在今天（16 日）晚间的零跑 2026 年度技术发布会上，零跑汽车公布了自研的世界模型智能辅助驾驶，200TOPS 算力就能实现，最高提供 1280TOPS 算力的顶级版本，老车主也可升级。IT之家从发布会现场获悉，2027 年第一季度起，零跑将陆续为激光雷达车型升级到基于世界模型的高阶辅助驾驶，10 万元以内的车型也将获得支持。零跑方面称，该智驾达到了“全行业第一梯队”的水平，将覆盖 A、B、C、D 全系车型，实现“真正的高阶智驾平权”。根据介绍，零跑世界模型智驾采用云端学习仿真、车端闭环训练，号称是越用越聪明、每天都在变强的生长型系统。目前，零跑智驾团队规模已经超过 800 人，具备 100% 全栈自研能力，更支持 1 天 8 版本的算法快速迭代。零跑科技" data-title="零跑世界模型辅助驾驶将覆盖 A、B、C、D 全系车型，10 万元内也可拥有" data-date="09-16 20:19" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-16 20:19</span>
          <span class="news-item-title">零跑世界模型辅助驾驶将覆盖 A、B、C、D 全系车型，10 万元内也可拥有</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/chinese-state-media-counters-dario-amodeis-call-to-put-brakes-on-ai-development-paper-says-move-is-a-response-to-chinese-competition" target="_blank" rel="noopener" data-cat="keji" data-summary="官方媒体《中国日报》认为， Anthropic的Dario Amodei呼吁限制前沿人工智能的发展，因为中国的人工智能模型正在赶上美国的人工智能实验室。" data-title="中国官方媒体反驳了Anthropic呼吁遏制人工智能发展的呼吁—报纸称此举是“对中国竞争的回应”" data-date="09-16 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-16 20:00</span>
          <span class="news-item-title">中国官方媒体反驳了Anthropic呼吁遏制人工智能发展的呼吁—报纸称此举是“对中国竞争的回应”</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/995534/a-brief-history-of-ai-executives-calling-for-regulation" target="_blank" rel="noopener" data-cat="keji" data-summary="在过去的几天里，很多愿意从人工智能中赚很多钱的人都公开同意，现在是时候让每个人在我们失去控制之前放慢速度了--包括OpenAI首席执行官Sam Altman、Anthropic首席执行官Dario Amodei、Google DeepMind联合创始人Demis Hassabis、微软首席执行官Satya Nadella和X […]" data-title="人工智能高管呼吁监管的简要历史" data-date="09-16 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-16 20:00</span>
          <span class="news-item-title">人工智能高管呼吁监管的简要历史</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/jensen-huang-thinks-china-will-develop-its-own-advanced-lithography-systems-by-2030-nvidia-ceo-says-achievement-of-that-capability-is-just-a-matter-of-time" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达首席执行官认为，鉴于他对中国开发先进半模具的三到四年时间表的看法，该国“已经存在”。" data-title="Jensen Huang认为，到2030年，中国将开发自己的先进光刻芯片制造工具--英伟达首席执行官表示，实现这一能力“只是时间问题”" data-date="09-16 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-16 19:30</span>
          <span class="news-item-title">Jensen Huang认为，到2030年，中国将开发自己的先进光刻芯片制造工具--英伟达首席执行官表示，实现这一能力“只是时间问题”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers" target="_blank" rel="noopener" data-cat="keji" data-summary="消息人士称， SK海力士和英特尔正在就开始在美国生产HBM进行谈判。不过，两家公司都拒绝证实这些谣言，因为随着首尔和华盛顿之间的贸易谈判继续进行， SK海力士可能会处于危险的境地。" data-title="据报道， SK海力士正在与英特尔讨论美国内存芯片制造—选项包括租赁俄亥俄州工厂或与其他人工智能超大规模公司成立合资企业" data-date="09-16 19:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-16 19:20</span>
          <span class="news-item-title">据报道， SK海力士正在与英特尔讨论美国内存芯片制造—选项包括租赁俄亥俄州工厂或与其他人工智能超大规模公司成立合资企业</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/defeated-gpt-6-astra-model-spent-several-hours-just-farming-potatoes-after-being-blown-up-by-a-creeper-in-minecraft-openai-offering-gets-further-than-any-other-ai-system-in-141-hour-test" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI的GPT-6 Astra在Minecraft测试期间死亡并丢失所有装备后，只花了数小时的时间种植土豆。" data-title="“被击败”的GPT-6 Astra模型在Minecraft中被爬虫炸毁后只花了几个小时养殖土豆— OpenAI产品在141小时的测试中比任何其他人工智能系统都更进一步" data-date="09-16 19:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-16 19:15</span>
          <span class="news-item-title">“被击败”的GPT-6 Astra模型在Minecraft中被爬虫炸毁后只花了几个小时养殖土豆— OpenAI产品在141小时的测试中比任何其他人工智能系统都更进一步</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-denies-rtx-5090-warranty-over-faded-serial-number-usd6-500-gpu-blemish-not-an-isolated-incident-according-to-customers" target="_blank" rel="noopener" data-cat="keji" data-summary="据Redditor报道， Nvidia据称拒绝了他们对GeForce RTX 5090 Founders Edition显卡的保修申请，因为支架上的序列号无法读取。" data-title="据客户称，英伟达否认对褪色序列号的RTX 5090保修— $ 6,500 GPU瑕疵不是孤立事件" data-date="09-16 18:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-16 18:45</span>
          <span class="news-item-title">据客户称，英伟达否认对褪色序列号的RTX 5090保修— $ 6,500 GPU瑕疵不是孤立事件</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cm750xv56v57o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="在美国，盖洛普（Gallup）今年5月发布的民调显示，在自己所在区域建数据中心，比建核电站更不受欢迎。" data-title="除了末日警告，人工智能发展还在面临着另一个威胁" data-date="09-16 17:30" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 17:30</span>
          <span class="news-item-title">除了末日警告，人工智能发展还在面临着另一个威胁</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/16/upshot/poll-ai-midterms-voters.html" target="_blank" rel="noopener" data-cat="keji" data-summary="《泰晤士报》/锡耶纳的一项民意调查显示，许多选民仍然不确定这个问题，包括哪个政党会在这个问题上做得更好。" data-title="人工智能尚未成为国家政治问题的微妙迹象" data-date="09-16 17:04" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-16 17:04</span>
          <span class="news-item-title">人工智能尚未成为国家政治问题的微妙迹象</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/16/science/ai-recursive-self-improvement.html" target="_blank" rel="noopener" data-cat="keji" data-summary="“递归自我提升”是指人工智能可以学习构建和训练自己，创造指数级的新进展和风险。" data-title="让人工智能毁灭者感到恐惧的升空场景" data-date="09-16 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-16 17:02</span>
          <span class="news-item-title">让人工智能毁灭者感到恐惧的升空场景</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/490760.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月15日，由AI大模型工场主办的“2026 AI产业生态大会”在北京举行。" data-title="AI大模型工场2026 AI产业生态大会今日举办，大咖同台共探智能生长与产业共生" data-date="09-16 16:51" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-16 16:51</span>
          <span class="news-item-title">AI大模型工场2026 AI产业生态大会今日举办，大咖同台共探智能生长与产业共生</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/490756.html" target="_blank" rel="noopener" data-cat="keji" data-summary="第五代骁龙8至尊版赋能全新AI智能体手机努比亚NaviX Ultra，加速智能体体验规模化落地" data-title="高通技术公司携手中兴努比亚和豆包手机助手，共同推动智能手机迈入个人AI新时代" data-date="09-16 16:18" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-16 16:18</span>
          <span class="news-item-title">高通技术公司携手中兴努比亚和豆包手机助手，共同推动智能手机迈入个人AI新时代</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/490750.html" target="_blank" rel="noopener" data-cat="keji" data-summary="2026年 9 月 15 日，AI基础设施公司基元律动（TokenRhythm）与无问芯穹（Infinigence AI）签署战略合作协议。" data-title="基元律动与无问芯穹达成战略合作，推进高质量Token供给与应用" data-date="09-16 16:09" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-16 16:09</span>
          <span class="news-item-title">基元律动与无问芯穹达成战略合作，推进高质量Token供给与应用</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/490686.html" target="_blank" rel="noopener" data-cat="keji" data-summary="AI协同办公的新官配，我先磕了" data-title="协同办公进入Agent时代，飞书+豆包工作跑在了最前面" data-date="09-16 15:46" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-16 15:46</span>
          <span class="news-item-title">协同办公进入Agent时代，飞书+豆包工作跑在了最前面</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">5 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmx2zyjylee1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，围绕埃尔林·哈兰德（ Erling Haaland ）获胜者的争议给他的球队在曼联的胜利蒙上了阴影，这“相当糟糕”。" data-title="马雷斯卡批评关注有争议的赢家" data-date="09-16 19:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 19:07</span>
          <span class="news-item-title">马雷斯卡批评关注有争议的赢家</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6wyzg91zm4wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="泰勒·哈伍德-贝利斯（ Taylor Harwood-Bellis ）被淘汰出阿斯顿维拉（ Aston Villa ）的冠军联赛阵容，但自从他到来后，他就一直没有亮相" data-title="Harwood-Bellis有机会在别墅留下自己的印记" data-date="09-16 19:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 19:00</span>
          <span class="news-item-title">Harwood-Bellis有机会在别墅留下自己的印记</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cxnvl2nv525ro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在迈克尔·卡里克（ Michael Carrick ）的领导下，当他们拥有超过50 ％的球时，曼联场均得分为1.5分。当他们少于50%时，这个数字是2.6。" data-title="为什么曼联在没有球的情况下会更好？" data-date="09-16 13:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 13:46</span>
          <span class="news-item-title">为什么曼联在没有球的情况下会更好？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cv4g5rp56p55o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="裁判长霍华德·韦伯（ Howard Webb ）承认，视频助理裁判（ VAR ）甚至没有考虑恩佐·费尔南德斯（ Enzo Fernandez ）是否在周日的曼彻斯特德比赛中与埃尔林·哈兰德（ Erling Haaland ）有争议的冠军对阵。" data-title="瓦尔甚至没有考虑费尔南德斯是否越位" data-date="09-16 00:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 00:00</span>
          <span class="news-item-title">瓦尔甚至没有考虑费尔南德斯是否越位</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6x2zgnngj71o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="由于利兹联队在英超联赛中排名第三， BBC Sport在丹尼尔·法克（ Daniel Farke ）的带领下评估了他们的" data-title="一支完美的团队--法克如何扭转了利兹的局面" data-date="09-15 22:01" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-15 22:01</span>
          <span class="news-item-title">一支完美的团队--法克如何扭转了利兹的局面</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697818.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨9月16日电 (记者 史轶夫)一部热播剧带动一座城。随着电视剧《早春晴朗》在Netflix全球榜单创纪录，有旅行平台数据显示，作为剧中主要取景地的哈尔滨旅游搜索热度环比上涨149%。" data-title="影视剧带动文旅热 哈尔滨双节打造追剧打卡新体验" data-date="09-16 20:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:44</span>
          <span class="news-item-title">影视剧带动文旅热 哈尔滨双节打造追剧打卡新体验</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697814.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州9月16日电 (记者 程景伟)“好在红河 红河好在——宝藏小城·烟火乡村”红河州文旅推介会16日在广州举行。推介会旨在深化云南红河哈尼族彝族自治州与粤港澳大湾区的文旅交流协作，进一步开拓大湾区客源市场，擦亮“好在红河 红河好在”特色文旅品牌。" data-title="“宝藏小城”云南红河州赴穗推介文旅 开拓湾区市场" data-date="09-16 20:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:44</span>
          <span class="news-item-title">“宝藏小城”云南红河州赴穗推介文旅 开拓湾区市场</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/286.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 16 日消息，北京时间今天（16 日）晚间，保时捷正式发布 2027 款纯电动卡宴，新车引入了全新的“定制涂装”项目，并可选新一代按摩座椅，首次提供电动门作为选配。新车首次提供可选装的电动车门。四扇车门均支持电动开关，轻拉对应门把手，伺服电机便会自动完成后续动作。用户可在车内外操作车门，控制方式包括座舱按钮、门把手，以及保时捷通讯管理系统（PCM）的 Flow Display 显示屏，也可通过保时捷数字钥匙远程控制。驾驶员系好安全带或踩下制动踏板，可自动关闭驾驶席车门。电动门可在坡道等多种环境下正常工作。传感器会持续监测车门周围，发现障碍物或人员便停止动作。系统还能与下车预警等辅助功能配合，在其他车辆接近时阻止开门。手动开关门功能始终保留。新增的按摩系统融合 4D 音效，将" data-title="2027 款保时捷纯电卡宴发布：可选电动门和音乐律动按摩座椅，10.9 万" data-date="09-16 20:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-16 20:43</span>
          <span class="news-item-title">2027 款保时捷纯电卡宴发布：可选电动门和音乐律动按摩座椅，10.9 万</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697813.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南宁9月16日电(陈梅)9月16日，平陆运河正式建成通航。通航当天，广西同步开通4条客运航线，民众乘船游览感受平陆运河的工程、生态、人文之美。" data-title="平陆运河客运航线开通 民众乘船游览见证通江达海" data-date="09-16 20:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:43</span>
          <span class="news-item-title">平陆运河客运航线开通 民众乘船游览见证通江达海</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697785.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网鄂尔多斯9月16日电 题：南京知青扎根内蒙古：为一句承诺 在草原上生活了一辈子" data-title="南京知青扎根内蒙古：为一句承诺 在草原上生活了一辈子" data-date="09-16 20:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:34</span>
          <span class="news-item-title">南京知青扎根内蒙古：为一句承诺 在草原上生活了一辈子</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/285.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 16 日消息，比亚迪方程豹旗下方程 S、方程 S GT 正式上市，售价 18.99 万元起。其中，方程 S 官方指导价为 18.99 万-22.99 万元，方程 S GT 指导价为 21.99 万-23.99 万元。两款车分别采用轿跑车与猎装车形态，均定位中大型车，与方程豹跑车 Formula X 共享设计语言，并首次搭载云辇-M 智能磁流变悬架，CLTC 工况下最大续航里程达 900 公里。IT之家注意到，方程 S 系列延续 Formula X 跑车的“生命金属美学”设计语言，整车线条流畅动感，呈现出鲜明的跑车气质。前脸配备“锋豹之眼”异形大灯，内部由双 U 形日间行车灯与 LED 光源构成；外扩式前唇进一步强化运动气场，车头设有 4 组贯通式风道以优化空气动力学表现，两" data-title="18.99 万元起、最大续航 900km，比亚迪方程豹方程 S/S GT 上市" data-date="09-16 20:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-16 20:34</span>
          <span class="news-item-title">18.99 万元起、最大续航 900km，比亚迪方程豹方程 S/S GT 上市</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697772.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网台州9月16日电 (钱晨菲 冯山杉 魏可)“把海洋建设成为世界各国共享的和平安宁之海、繁荣发展之海、文明交融之海。”日前，第22届亚洲地区海岸警备机构高官会高级别会议在浙江杭州成功举办。会议期间，中国海警局有关代表围绕“海洋碳汇执法”作专题交流分享，展现出了以法治力量守护海洋碳库的责任担当，更为生态治理提供了切实可行的方案。" data-title="守护蔚蓝海疆 浙江台州海警打造修复式执法" data-date="09-16 20:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:33</span>
          <span class="news-item-title">守护蔚蓝海疆 浙江台州海警打造修复式执法</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/283.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 16 日消息，极狐阿尔法 T7 汽车今日上市，新车提供增程、纯电两种动力，部分型号搭载华为干昆智驾 ADS 5 Pro，全系标配宁德时代电池。该车上市补贴价 13.28 万元起，即日起下单可享受价值 4000 元置换补贴、6000 元 ADS 高阶包补贴、三电终身质保、3 年不限量娱乐流量等权益。IT之家附该车各版本定价如下：增程1315 PLUS：13.28 万元1315 MAX：14.48 万元1315 MAX 干昆版：15.38 万元1315 ULTRA 干昆版：16.38 万元纯电650 PLUS：13.58 万元715 MAX：14.98 万元715 MAX 干昆版：15.88 万元715 ULTRA：15.98 万元715 ULTRA 干昆版：16.88 万元I" data-title="上市补贴价 13.28 万元起：极狐阿尔法 T7 汽车上市，可选增程 / 纯电动力、华为干昆智驾 ADS 5 Pro" data-date="09-16 20:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-16 20:31</span>
          <span class="news-item-title">上市补贴价 13.28 万元起：极狐阿尔法 T7 汽车上市，可选增程 / 纯电动力、华为干昆智驾 ADS 5 Pro</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697821.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月16日电 (记者 吕少威)《北京市现代服务业扩能提质实施方案(2026-2030年)》(下称实施方案)16日发布，从强化生产性服务业赋能进阶、促进生活性服务业焕新提质、培育服务新增长点、提升服务业发展质效、大力营造服务业优良发展环境等5个方面部署24条重点任务。" data-title="北京出台专门方案促现代服务业扩能提质" data-date="09-16 20:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:30</span>
          <span class="news-item-title">北京出台专门方案促现代服务业扩能提质</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/280.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 16 日消息，全新理想 i9 Home 旗舰六座 SUV 今晚正式发布，新车是系列首台家庭纯电旗舰 SUV，也是理想第二代纯电平台的首发旗舰，全国统一零售价格 36.98 万元。据介绍，全新理想 i9 只提供 Home 一个版本，尺寸为 5225×1970×1752mm、轴距为 3168mm，风阻系数 0.215Cd（全球量产 SUV 最低）。全系标配 101kWh 三元锂 5C 超充电池、前后双电机智能四驱，CLTC 综合续航里程 705 公里，10 分钟充电 500 公里，拥有旗舰级 NVH 表现。新车还标配线控转向 + 后轮转向、第三代双腔双阀魔毯空气悬架，5.2 米车长能做到约 5.3 米转弯半径。全新理想 i9 Home 还标配 4 把全尺寸零重力座椅、三排电动前" data-title="全新理想 i9 Home 六座 SUV 发布：第二代纯电平台的首发旗舰，36.98 万元" data-date="09-16 20:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-16 20:26</span>
          <span class="news-item-title">全新理想 i9 Home 六座 SUV 发布：第二代纯电平台的首发旗舰，36.98 万元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-16/10697775.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福建永安9月16日电 (黄中泉 廖金朋)近日，福建永安昆虫监测人员在发源于天宝岩国家级自然保护区的桂溪溪流开展例行监测时，接连发现两只珍稀蜻蜓——国家二级保护野生动物扭尾曦春蜓和色彩艳丽的华艳色蟌，双双刷新永安市蜻蜓影像记录。" data-title="福建永安首现“水中宝石”华艳色蟌 扭尾曦春蜓刷新影像记录" data-date="09-16 20:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-16 20:24</span>
          <span class="news-item-title">福建永安首现“水中宝石”华艳色蟌 扭尾曦春蜓刷新影像记录</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6jrxzq3777wo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="区锦新的家人过去一年都无法接触他，到了开审当天，传媒被拒于法庭门外，外界只能等待政府新闻稿取得消息，审理过程较香港的国安案件更加封闭。" data-title="区锦新案：澳门首宗国安案闭门开审，我们知道多少？" data-date="09-16 20:23" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 20:23</span>
          <span class="news-item-title">区锦新案：澳门首宗国安案闭门开审，我们知道多少？</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ram/ai-induced-memory-shortage-is-changing-how-devices-are-built-fairphone-says-memory-now-60-percent-of-materials-cost-smaller-laptop-and-phone-makers-are-redesigning-products-and-have-to-test-for-fake-chips" target="_blank" rel="noopener" data-cat="zonghe" data-summary="对于较小的设备制造商来说，内存价格上涨只是问题的一部分，因为有限的可用性迫使公司重新考虑从主板设计到采购策略的所有内容。" data-title="Fairphone表示，人工智能引发的内存短缺正在改变设备的制造方式，现在60%的材料成本—较小的笔记本电脑和手机制造商正在重新设计产品，必须测试假芯片" data-date="09-16 20:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-16 20:15</span>
          <span class="news-item-title">Fairphone表示，人工智能引发的内存短缺正在改变设备的制造方式，现在60%的材料成本—较小的笔记本电脑和手机制造商正在重新设计产品，必须测试假芯片</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/995539/fire-emblem-fortunes-weave-switch-2-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="任天堂擅长制作开放式游戏。《塞尔达传说：荒野之息》通过让玩家自由处理地图的任何部分，颠覆了塞尔达游戏可能是什么的想法，这一理念在《王国之泪》中不断迭代。在Switch 2上，这个想法[…]" data-title="任天堂用巨型财富编织打开火焰纹章" data-date="09-16 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-16 20:00</span>
          <span class="news-item-title">任天堂用巨型财富编织打开火焰纹章</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/995945/iphone-18-pro-max-review-camera-aperture" target="_blank" rel="noopener" data-cat="zonghe" data-summary="上周，苹果宣布推出了一款与以往任何时候都不同的iPhone。这款iPhone似乎已经引领其他几家手机制造商为其旗舰产品寻求完全不同的设计。一种非常独特的设备，具有“我不敢相信他们做到了”的软件，苹果有时会触及[…]" data-title="IPhone 18 Pro的大型相机更新完全是关于小收益" data-date="09-16 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-16 20:00</span>
          <span class="news-item-title">IPhone 18 Pro的大型相机更新完全是关于小收益</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-16 20:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
