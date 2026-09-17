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
      <span>2026-09-17 14:50 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-17/10698158.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社南昌9月17日电(记者陈浚武)9月17日，2026上海合作组织传统医学论坛在江西南昌开幕。全国政协副主席、上合组织睦邻友好合作委员会主席沈跃跃出席开幕式并发表主旨讲话。" data-title="沈跃跃出席2026上海合作组织传统医学论坛开幕式并发表主旨讲话" data-date="09-17 13:52" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-17 13:52</span>
      </div>
      <h2 class="hero-featured-title">沈跃跃出席2026上海合作组织传统医学论坛开幕式并发表主旨讲话</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/003/584.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 17 日消息，TypeSafe AI 昨日（9 月 16 日）发布公告，宣布推出 Jev，该 AI 模型定位为“System One Model”（系统一模型），不生成文本，直接返回结构化决策，其成本和延迟远低于大型语言模型。IT之家查询公开资料，TypeSafe AI 由 Diogo Almeida 成立，他曾在 OpenAI 工作，是 RLHF 研究的幕后功臣之一，而该研究催生了 ChatGPT。该公司成立于 2 年前，本周宣布结束隐身状态，宣布完成由 DCVC 领投的 4,000 万美元（IT之家注：现汇率约合 2.69 亿元人民币）种子轮融资。该公司将 Jev 定义为“System One Model”（系统一模型），对应快速、低延迟的重复决策场景。该定义借用心理学" data-title="ChatGPT 背后功臣：Almeida 推出 AI 模型 Jev，不生成文本、输出免费" data-date="09-17 14:49" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">ChatGPT 背后功臣：Almeida 推出 AI 模型 Jev，不生成文本、输出免费</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cmwyzr576y9zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理迈克尔·卡里克（ Michael Carrick ）坚称，在曼联EFL杯退出后，他没有感到压力。" data-title="卡里克“不被压力打扰” -但他应该在这最近的混乱之后吗？" data-date="09-17 07:31" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">卡里克“不被压力打扰” -但他应该在这最近的混乱之后吗？</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/003/583.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，雷柏 VT2sMAX 大师版 V2 游戏鼠标现已在京东开启预约，新品支持有线 / 2.4G 双模连接，配备原相 PAW3955 传感器，回报率可达 8K，售价 399 元。据介绍，这款鼠标适配中小手手型，尤其适合抓握、指握，采用 Nordic 54H20 方案，主频可达 320MHz。规格方面，该鼠标配备原生 8K 接收器，拥有原相 PAW3955 Ultimate 传感器，号称可带来职业级性能，DPI 可在 1-60000 之间调节。此外，该鼠标采用龙骨结构设计，表面带有亲肤防滑涂层，拥有 800mAh 电池，支持多种充电方式，适配 Windows、macOS 操作系统，拥有网页驱动。目前该鼠标已在京东开启预约，售价 399 元。京东雷柏（Rapoo）VT2" data-title="399 元，雷柏 VT2sMAX 大师版 V2 双模游戏鼠标开启预约" data-date="09-17 14:47" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">399 元，雷柏 VT2sMAX 大师版 V2 双模游戏鼠标开启预约</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698158.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社南昌9月17日电(记者陈浚武)9月17日，2026上海合作组织传统医学论坛在江西南昌开幕。全国政协副主席、上合组织睦邻友好合作委员会主席沈跃跃出席开幕式并发表主旨讲话。" data-title="沈跃跃出席2026上海合作组织传统医学论坛开幕式并发表主旨讲话" data-date="09-17 13:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:52</span>
          <span class="news-item-title">沈跃跃出席2026上海合作组织传统医学论坛开幕式并发表主旨讲话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698180.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 据美联社报道，两名地区官员当地时间16日表示，沙特阿拉伯的拦截弹储备即将耗尽，已向地区和西方盟友寻求支援。" data-title="沙特拦截弹储备告急，求助法英巴埃，“美方库存已大幅减少”" data-date="09-17 13:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:49</span>
          <span class="news-item-title">沙特拦截弹储备告急，求助法英巴埃，“美方库存已大幅减少”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698186.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网雄安9月17日电 题：白洋淀建生态监测“数智网”：从“跑断腿”到一屏观全域" data-title="白洋淀建生态监测“数智网”：从“跑断腿”到一屏观全域" data-date="09-17 13:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:43</span>
          <span class="news-item-title">白洋淀建生态监测“数智网”：从“跑断腿”到一屏观全域</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698185.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今天(17日)，第十三届北京香山论坛进入最后一天。这两天，来自近100个国家、地区和国际组织的官方代表，以及国内外专家学者，围绕世界多极化、全球安全治理等议题展开对话。" data-title="北京香山论坛今天闭幕：从“对话”到“共治” 凝聚全球安全治理共识" data-date="09-17 13:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:41</span>
          <span class="news-item-title">北京香山论坛今天闭幕：从“对话”到“共治” 凝聚全球安全治理共识</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698164.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【学习进行时】9月12日至13日，习近平主席出席金砖国家领导人第十八次会晤，分别在第一阶段、第二阶段会议上发表了重要讲话。" data-title="学习进行时丨让新兴技术照亮共同繁荣之路" data-date="09-17 13:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:37</span>
          <span class="news-item-title">学习进行时丨让新兴技术照亮共同繁荣之路</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/16/world/canada/eu-canada-associate-member-trade.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="欧盟向渥太华提出的“准成员”地位表明，美国的盟友正在更加紧密地团结在一起。但他们的计划面临重大障碍。" data-title="作为特朗普的鬃毛，欧盟-加拿大野心面对现实" data-date="09-17 13:33" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 13:33</span>
          <span class="news-item-title">作为特朗普的鬃毛，欧盟-加拿大野心面对现实</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698167.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近日，习近平总书记给福建省“漳州110”全体队员回信。“守百姓幸福，护家国平安”，总书记对人民公安寄予厚望。" data-title="拾光纪·“守百姓幸福，护家国平安”，总书记这样嘱托人民公安" data-date="09-17 13:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:33</span>
          <span class="news-item-title">拾光纪·“守百姓幸福，护家国平安”，总书记这样嘱托人民公安</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698172.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月17日电 (记者 马帅莎)据中国航天科技集团消息，北京时间9月17日8时32分，中国在海南商业航天发射场使用长征十二号运载火箭，成功将卫星互联网低轨25组卫星发射升空，卫星顺利进入预定轨道，发射任务获得圆满成功。" data-title="中国成功发射卫星互联网低轨25组卫星" data-date="09-17 13:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:30</span>
          <span class="news-item-title">中国成功发射卫星互联网低轨25组卫星</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698145.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 据卡塔尔半岛电视台17日报道，美国国务院宣布延长对巴勒斯坦权力机构官员和巴勒斯坦解放组织成员的签证制裁，这意味着巴勒斯坦总统阿巴斯将连续第二年遭美国拒签，无法前往纽约出席联合国大会并发表演讲。" data-title="美国再次拒绝向阿巴斯发放入境签证" data-date="09-17 13:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:26</span>
          <span class="news-item-title">美国再次拒绝向阿巴斯发放入境签证</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698161.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 综合美联社等外媒报道，当地时间16日，美军参谋长联席会议主席丹·凯恩表示，美军不仅需要为在地球轨道上的作战做好准备，还需要准备好在月球周边空间作战。" data-title="美高官称需为月球周边作战做准备，美国要把战场延伸至太空？" data-date="09-17 13:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:09</span>
          <span class="news-item-title">美高官称需为月球周边作战做准备，美国要把战场延伸至太空？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698153.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 据新疆生产建设兵团纪委监委消息：新疆生产建设兵团卫生健康委员会原党组成员、副主任刘惟涉嫌严重违纪违法，目前正接受新疆生产建设兵团纪委监委纪律审查和监察调查。" data-title="新疆生产建设兵团卫生健康委员会原副主任刘惟被查" data-date="09-17 12:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 12:54</span>
          <span class="news-item-title">新疆生产建设兵团卫生健康委员会原副主任刘惟被查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698152.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 据日本共同社报道，当地时间17日，日本首相高市早苗改组内阁，日本维新会前干事长中司宏入阁，担任规制改革担当大臣，这也是维新会成员首次入阁。" data-title="日本首相高市早苗改组内阁 日本维新会成员首次入阁" data-date="09-17 12:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 12:49</span>
          <span class="news-item-title">日本首相高市早苗改组内阁 日本维新会成员首次入阁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698150.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本首相高市早苗17日改组内阁，当日下午公布的阁僚名单显示，内阁官房长官木原稔、外务大臣茂木敏充、防卫大臣小泉进次郎、财务大臣片山皋月等人留任；日本众议员关芳弘首次入阁，担任文部科学大臣；日本维新会前干事长中司宏入阁，担任规制改革担当大臣，这也是维新会成员首次入阁。(总台报道员 柏春洋)" data-title="日本首相高市早苗改组内阁" data-date="09-17 12:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 12:31</span>
          <span class="news-item-title">日本首相高市早苗改组内阁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698134.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月17日电 喀土穆消息：苏丹西科尔多凡州一座金矿日前发生坍塌事故，截至当地时间16日已造成82人死亡，仍有数十人失联。" data-title="苏丹一金矿坍塌已致82人遇难  仍有人员失联" data-date="09-17 12:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 12:15</span>
          <span class="news-item-title">苏丹一金矿坍塌已致82人遇难  仍有人员失联</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698144.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：习近平就发展先进制造业作出重要指示强调" data-title="习近平就发展先进制造业作出重要指示" data-date="09-17 12:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 12:12</span>
          <span class="news-item-title">习近平就发展先进制造业作出重要指示</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/003/584.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 17 日消息，TypeSafe AI 昨日（9 月 16 日）发布公告，宣布推出 Jev，该 AI 模型定位为“System One Model”（系统一模型），不生成文本，直接返回结构化决策，其成本和延迟远低于大型语言模型。IT之家查询公开资料，TypeSafe AI 由 Diogo Almeida 成立，他曾在 OpenAI 工作，是 RLHF 研究的幕后功臣之一，而该研究催生了 ChatGPT。该公司成立于 2 年前，本周宣布结束隐身状态，宣布完成由 DCVC 领投的 4,000 万美元（IT之家注：现汇率约合 2.69 亿元人民币）种子轮融资。该公司将 Jev 定义为“System One Model”（系统一模型），对应快速、低延迟的重复决策场景。该定义借用心理学" data-title="ChatGPT 背后功臣：Almeida 推出 AI 模型 Jev，不生成文本、输出免费" data-date="09-17 14:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:49</span>
          <span class="news-item-title">ChatGPT 背后功臣：Almeida 推出 AI 模型 Jev，不生成文本、输出免费</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/business/king-charles-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The gathering in Scotland brings together industry leaders amid a growing debate about the safety risks of unchecked artificial intelligence." data-title="King Charles Meets With A.I. Executives About Safety Risks" data-date="09-17 13:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 13:00</span>
          <span class="news-item-title">King Charles Meets With A.I. Executives About Safety Risks</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491280.html" target="_blank" rel="noopener" data-cat="keji" data-summary="AI正火嘛，老马的待遇也算提升了一点：这回至少有房车了（doge）" data-title="马斯克睡进工地！为AI基建拼了" data-date="09-17 12:37" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 12:37</span>
          <span class="news-item-title">马斯克睡进工地！为AI基建拼了</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/16/your-startups-next-teammate-might-be-an-ai-agent-gusto-insight-partners-and-leland-explain-what-that-changes-at-techcrunch-disrupt-2026/" target="_blank" rel="noopener" data-cat="keji" data-summary="本课程将探讨早期公司如何构建人类和人工智能代理并肩工作的团队，以及创始人如何在不牺牲速度、问责制或文化的情况下做到这一点。如需了解更多信息，请访问TechCrunch Disrupt 2026。请在9月25日前登记，最多可节省$ 200。" data-title="您的创业公司的下一个队友可能是人工智能代理： Gusto、Insight Partners和Leland在TechCrunch Disrupt 2026上解释了这些变化" data-date="09-17 11:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-17 11:30</span>
          <span class="news-item-title">您的创业公司的下一个队友可能是人工智能代理： Gusto、Insight Partners和Leland在TechCrunch Disrupt 2026上解释了这些变化</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491091.html" target="_blank" rel="noopener" data-cat="keji" data-summary="1亿Tokens人人免费领" data-title="国产RSI模型交卷！Flash模型靠它反打旗舰" data-date="09-17 11:26" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 11:26</span>
          <span class="news-item-title">国产RSI模型交卷！Flash模型靠它反打旗舰</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/490974.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月16日，网易有道“NEXT，AGENT｜有道AI Open Day”在北京举办。" data-title="网易有道周枫：AI能力竞争，正在进入“Model + Agent + Workflow”时代，网易有道AI Open Day展示AI时代“有道解法”" data-date="09-17 09:55" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 09:55</span>
          <span class="news-item-title">网易有道周枫：AI能力竞争，正在进入“Model + Agent + Workflow”时代，网易有道AI Open Day展示AI时代“有道解法”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/490950.html" target="_blank" rel="noopener" data-cat="keji" data-summary="奖励曲线、显卡故障全公开" data-title="罗福莉沉寂半年官宣小米强化学习！直播新模型训练过程，一小时烧3万美元" data-date="09-17 09:09" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 09:09</span>
          <span class="news-item-title">罗福莉沉寂半年官宣小米强化学习！直播新模型训练过程，一小时烧3万美元</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/16/technology/openai-model-safety-guardrails.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这家人工智能公司还发布了一个框架，用于在其系统出错时进行报告。" data-title="OpenAI披露六起“涉及”人工智能行为的新事件" data-date="09-17 08:12" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 08:12</span>
          <span class="news-item-title">OpenAI披露六起“涉及”人工智能行为的新事件</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/16/al-gore-has-a-surprisingly-calm-take-on-the-ai-data-center-backlash/" target="_blank" rel="noopener" data-cat="keji" data-summary="在接受TechCrunch采访时，戈尔表示，他并没有因为人工智能数据中心的排放而失眠--他更担心人工智能行业自己对技术发展方向的警告。" data-title="阿尔·戈尔说，真正的人工智能风险不是数据中心" data-date="09-17 07:43" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-17 07:43</span>
          <span class="news-item-title">阿尔·戈尔说，真正的人工智能风险不是数据中心</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/996078/snap-specs-intelligence-ai-agent-ios-mac" target="_blank" rel="noopener" data-cat="keji" data-summary="Snap推出了“Specs Intelligence” ，这是一种新的人工智能助手，可以连接其他数字帐户，帮助您完成工作任务和跟踪差旅信息等。这似乎类似于像Meta的Muse和Gemini的Spark这样的人工智能助手，尽管Snap正在将Specs Intelligence作为一种“预期的人工智能服务” ， “帮助您[…]" data-title="Snap正在推出一款新的Specs AI工具，即将在iOS和Mac上推出" data-date="09-17 07:40" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-17 07:40</span>
          <span class="news-item-title">Snap正在推出一款新的Specs AI工具，即将在iOS和Mac上推出</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic和OpenAI希望在其人工智能实验室中嵌入独立的安全评估人员。研究人员欢迎前所未有的访问，但警告有意义的监督需要透明度、独立性以及最终的监管。" data-title="Anthropic和OpenAI希望嵌入安全评估人员。他们真的会独立吗？" data-date="09-17 05:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-17 05:07</span>
          <span class="news-item-title">Anthropic和OpenAI希望嵌入安全评估人员。他们真的会独立吗？</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/996470/ai-data-center-e-waste-ban" target="_blank" rel="noopener" data-cat="keji" data-summary="一份新的报告警告说，人工智能热潮产生的电子废物被大大低估了。到2050年，它可能成为足够装满2300万个集装箱的垃圾--如果连续排成一排，大约有足够的40英尺集装箱绕地球六圈。与之前的研究相比，人工智能电子废物的估计值要高得多[…]" data-title="人工智能数据中心的电子垃圾问题是巨大的，而且正在变得越来越大" data-date="09-17 04:40" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-17 04:40</span>
          <span class="news-item-title">人工智能数据中心的电子垃圾问题是巨大的，而且正在变得越来越大</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/16/ai-labs-want-in-house-auditors-but-maybe-they-should-shut-the-front-door-first/" target="_blank" rel="noopener" data-cat="keji" data-summary="对于躲在显而易见的地方的流氓特工，可能有更简单、更有效的解决方案。" data-title="人工智能实验室需要内部审核员—但也许他们应该先关上前门" data-date="09-17 02:25" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-17 02:25</span>
          <span class="news-item-title">人工智能实验室需要内部审核员—但也许他们应该先关上前门</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/996321/apple-servers-ai-nvidia" target="_blank" rel="noopener" data-cat="keji" data-summary="据The Information报道，苹果计划重返服务器游戏，并可能与Nvidia合作实现这一目标。苹果公司于2011年退役其Xserve生产线，此后基本上将企业机器留给了其他制造商。但随着人工智能行业继续[…] ，对计算能力的需求不断增长" data-title="苹果可能会再次制造服务器，以兑现人工智能热潮" data-date="09-17 01:20" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-17 01:20</span>
          <span class="news-item-title">苹果可能会再次制造服务器，以兑现人工智能热潮</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/16/your-ai-agents-can-now-control-your-google-home-devices/" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌正在为Google Home推出抢先访问新的MCP服务器，允许Claude、ChatGPT等人工智能代理使用自然语言控制连接的设备、查看相机摘要和访问智能家居活动。" data-title="您的AI代理现在可以控制您的Google Home设备" data-date="09-17 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-17 01:00</span>
          <span class="news-item-title">您的AI代理现在可以控制您的Google Home设备</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmwyzr576y9zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理迈克尔·卡里克（ Michael Carrick ）坚称，在曼联EFL杯退出后，他没有感到压力。" data-title="卡里克“不被压力打扰” -但他应该在这最近的混乱之后吗？" data-date="09-17 07:31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 07:31</span>
          <span class="news-item-title">卡里克“不被压力打扰” -但他应该在这最近的混乱之后吗？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvrl6egl1254o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Clearlake Capital获得了对切尔西的全部控制权，董事长Todd Boehly、董事Mark Walter和Hansjorg Wyss出售了他们在俱乐部的股份。" data-title="Boehly和Walter将切尔西的股份出售给Clearlake" data-date="09-17 07:29" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 07:29</span>
          <span class="news-item-title">Boehly和Walter将切尔西的股份出售给Clearlake</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cr5yev4y101eo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport的Ask Me Anything团队了解青少年参加英超联赛时球员和俱乐部必须遵守的规则" data-title="对于青训学院球员，英超联赛的规则是什么？" data-date="09-17 00:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 00:26</span>
          <span class="news-item-title">对于青训学院球员，英超联赛的规则是什么？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crgjqw0l01njo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在JJ加布里埃尔本应成为曼联历史上最年轻球员的那天晚上，人们争先恐后地说服他不要辞职。" data-title="Gabriel和Man Utd的下一步是什么？" data-date="09-16 23:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 23:48</span>
          <span class="news-item-title">Gabriel和Man Utd的下一步是什么？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmx2zyjylee1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，围绕埃尔林·哈兰德（ Erling Haaland ）获胜者的争议给他的球队在曼联的胜利蒙上了阴影，这“相当糟糕”。" data-title="“我们仍在等待道歉” - Maresca谈城市VAR的挫败感" data-date="09-16 19:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 19:07</span>
          <span class="news-item-title">“我们仍在等待道歉” - Maresca谈城市VAR的挫败感</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6wyzg91zm4wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="泰勒·哈伍德-贝利斯（ Taylor Harwood-Bellis ）被淘汰出阿斯顿维拉（ Aston Villa ）的冠军联赛阵容，但自从他到来后，他就一直没有亮相" data-title="Harwood-Bellis有机会在别墅留下自己的印记" data-date="09-16 19:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 19:00</span>
          <span class="news-item-title">Harwood-Bellis有机会在别墅留下自己的印记</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crwyz819xw4po?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport探讨了詹姆斯·加纳如何成为埃弗顿最重要的球员。" data-title="切尔西想要的“Mini Valverde” -加纳现在是埃弗顿的主角" data-date="09-16 18:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 18:56</span>
          <span class="news-item-title">切尔西想要的“Mini Valverde” -加纳现在是埃弗顿的主角</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/003/583.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，雷柏 VT2sMAX 大师版 V2 游戏鼠标现已在京东开启预约，新品支持有线 / 2.4G 双模连接，配备原相 PAW3955 传感器，回报率可达 8K，售价 399 元。据介绍，这款鼠标适配中小手手型，尤其适合抓握、指握，采用 Nordic 54H20 方案，主频可达 320MHz。规格方面，该鼠标配备原生 8K 接收器，拥有原相 PAW3955 Ultimate 传感器，号称可带来职业级性能，DPI 可在 1-60000 之间调节。此外，该鼠标采用龙骨结构设计，表面带有亲肤防滑涂层，拥有 800mAh 电池，支持多种充电方式，适配 Windows、macOS 操作系统，拥有网页驱动。目前该鼠标已在京东开启预约，售价 399 元。京东雷柏（Rapoo）VT2" data-title="399 元，雷柏 VT2sMAX 大师版 V2 双模游戏鼠标开启预约" data-date="09-17 14:47" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:47</span>
          <span class="news-item-title">399 元，雷柏 VT2sMAX 大师版 V2 双模游戏鼠标开启预约</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/582.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，Twitch 首席执行官丹 · 克兰西（Dan Clancy）表示，《侠盗猎车手 6（GTA 6）》在今年假日游戏旺季，大概率不会遭遇能够分流玩家注意力的强力竞品，在他看来，这正是开发商所采取的正确策略。外界普遍预计本作将成为电子游戏史上热度最高的首发作品。游戏定于 11 月 19 日发售，届时将成为索尼 PlayStation 5 以及微软 Xbox Series 主机平台上的重磅焦点。克兰西此次到访日本，是为了出席东京电玩展，会见来自整个亚洲的游戏开发者与内容创作者。他认为，玩家对于 Rockstar 游戏公司这款新作的狂热，很有可能会一直延续到明年 1 月份。克兰西管理着全球最头部的游戏直播平台。他提到，各家游戏厂商如今的发行规划分为两种思路：要么选择在" data-title="Twitch CEO 克兰西：今年假日档没有谁能分流《GTA 6》的玩家" data-date="09-17 14:46" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:46</span>
          <span class="news-item-title">Twitch CEO 克兰西：今年假日档没有谁能分流《GTA 6》的玩家</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/581.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，华为商城迎来调整，在鸿蒙智行板块，“五界”品牌被重新排序，问界系列被移动至最下方，目前的排序为“尊界-享界-智界-尚界-问界”（此前为“尊界-问界-享界-智界-尚界”）。▲ IT之家 9 月 17 日截图▲ IT之家 9 月 15 日截图目前，华为商城尚未对此次调整作出说明，IT之家询问客户服务，对方表示：“暂时没有相关信息。”今年 9 月 15 日，鸿蒙智行发布了关于问界合作模式的说明，宣布即日起，问界将在鸿蒙智行合作框架下探索新合作模式：产品定义、产品设计、品牌营销、渠道零售、服务体系由赛力斯主导，华为终端参与赋能。所有问界用户的既有权益及后续服务不受影响。相关阅读：《消息称原鸿蒙智行部分店面将划归赛力斯，只陈列和销售问界车型》《问界发布关于鸿蒙智行合作模" data-title="华为商城鸿蒙智行板块迎调整：“五界”品牌重新排序，问界被移至最后一位" data-date="09-17 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:43</span>
          <span class="news-item-title">华为商城鸿蒙智行板块迎调整：“五界”品牌重新排序，问界被移至最后一位</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/580.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，赛车模拟硬件制造商 Fanatec 当地时间 16 日公布了“ClubSport F1 赛车系统”。该套件专为 PlayStation 5、PlayStation 4 和 PC 平台设计，将在 TGS2026 东京游戏展上首次公开亮相。“ClubSport F1 赛车系统”是此前推出的 ClubSport Racing Wheel F1 套件的升级版本，延续了上一代的 ClubSport DD+ 方向盘底座，并升级至 ClubSport F1 V3 方向盘。ClubSport DD+ 搭载高性能直驱电机，可提供多达 18N·m 的保持扭矩，带来逼真的力反馈，FullForce 技术则能提供沉浸式遥测效果。ClubSport F1 V3 方向盘在 ClubSpo" data-title="Fanatec 公布 ClubSport F1 赛车系统驾驶模拟套件，含 18N·m 扭矩直驱底座" data-date="09-17 14:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:40</span>
          <span class="news-item-title">Fanatec 公布 ClubSport F1 赛车系统驾驶模拟套件，含 18N·m 扭矩直驱底座</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/578.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，沃尔沃汽车今日公布了其 99 年历史中最大、最具雄心的全球产品推广，从现在到 2030 年底将推出 13 款全新车型。届时，沃尔沃汽车将拥有明确的区域化产品线，涵盖电气化汽车、纯电动车以及面向区域市场的第三代混合动力车。产品计划包括 7 款面向西方市场的新车和 6 款面向中国市场的新车。更多细节将在今天的沃尔沃汽车战略更新中公布。通过该产品计划，沃尔沃汽车计划通过扩大快速增长的纯电动（BEV）细分市场，以及为仍不愿全电动化的客户推出第三代混合动力车，实现市场份额翻倍。此次新产品攻势将成为沃尔沃汽车打造长期强劲增长和超过 8% 息税前利润率的重要因素。新产品推广还将涵盖新细分市场，扩大其在三大区域的供应：欧洲、美国和中国。这将带领沃尔沃汽车迈入设计新时代，拓宽沃" data-title="沃尔沃官宣有史以来最大规模产品计划：全球 13 款新车，中国市场独占 6 款，与吉利合作打造" data-date="09-17 14:35" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:35</span>
          <span class="news-item-title">沃尔沃官宣有史以来最大规模产品计划：全球 13 款新车，中国市场独占 6 款，与吉利合作打造</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/577.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，抖音宣布上线声音侵权举报入口，并升级相关维权机制。抖音表示，随着 AI 合成、仿冒音色等技术门槛降低，克隆明星或配音演员声音等侵权行为更易发生。据抖音介绍，近一个月来，侵权投诉中提及声音侵权的举报量同比翻倍，声音被冒用正成为不容忽视的新型侵权形态。此次升级后，抖音上线专属维权入口与可核验的举证方式，使声音维权有入口、可举证、能判定，同时提供申诉通道，提升信息对称性，保障双方权益。抖音表示，声音权益是数字时代人格权益的重要组成部分。平台还将持续优化 App 端的声纹识别与核验能力，将推进构建覆盖肖像、声音等多类人格权益的立体化保护体系。IT之家附抖音官方举报地址：https://www.douyin.com/qinquan/report。" data-title="抖音宣布上线声音侵权举报入口，应对 AI 合成、仿冒音色等侵权行为" data-date="09-17 14:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:34</span>
          <span class="news-item-title">抖音宣布上线声音侵权举报入口，应对 AI 合成、仿冒音色等侵权行为</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698203.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月17日电 一些产品宣称能够利用“宇宙能量”“能量场”等方式调节身体，甚至治疗头疼、增强免疫力。但目前没有可靠的科学证据证明，存在一种可以被这类仪器接收、储存并用于治疗疾病的特殊“宇宙能量”。(来源：@科学辟谣 中国新闻网微博)" data-title="“宇宙能量”仪器可治头疼脑热、强身健体？千万别上当！丨中新真探" data-date="09-17 14:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 14:13</span>
          <span class="news-item-title">“宇宙能量”仪器可治头疼脑热、强身健体？千万别上当！丨中新真探</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698177.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月17日电 据“绥中融媒”微信公众号消息，9月17日，辽宁省葫芦岛市绥中县食品安全委员会办公室发布情况通报称，2026年9月16日19时，辽宁东戴河志臻中学部分学生先后出现恶心、呕吐等不适症状，已被及时送医诊治。" data-title="辽宁绥中一中学部分学生出现呕吐等症状 当地通报" data-date="09-17 13:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:58</span>
          <span class="news-item-title">辽宁绥中一中学部分学生出现呕吐等症状 当地通报</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698194.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国新闻周刊记者：倪纷纷" data-title="黑攀乱象调查" data-date="09-17 13:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:56</span>
          <span class="news-item-title">黑攀乱象调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698171.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网贵州遵义9月17日电 (记者 杨茜)“我接待过法国、英国、美国以及非洲一些国家的游客。他们对文物和四渡赤水最感兴趣。我最常听到的感叹就是‘Amazing’。”遵义会议纪念馆解说员赵美珺告诉记者。" data-title="（长征胜利90周年）遵义会议纪念馆多维度升级游客参观体验" data-date="09-17 13:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 13:26</span>
          <span class="news-item-title">（长征胜利90周年）遵义会议纪念馆多维度升级游客参观体验</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/16/iceland-based-treble-raises-18-million-for-its-voice-simulation-platform/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="高音的语音模拟平台被语音AI模型开发商、AI可穿戴设备和机器人公司使用" data-title="总部位于冰岛的Treble为其语音模拟平台筹集了1800万美元$" data-date="09-17 13:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-17 13:00</span>
          <span class="news-item-title">总部位于冰岛的Treble为其语音模拟平台筹集了1800万美元$</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698146.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="北京市反诈中心近期发布预警，警惕境外支票“假到账”诈骗。这类诈骗，明明账户余额显示钱款到账，真要花钱的时候，这笔钱却凭空消失。骗子利用的就是群众对境外支票兑付规则的认知盲区来设下骗局。不久前，北京的王先生就掉进了骗子精心布设的圈套。" data-title="账户余额到账用钱时却凭空消失 北京反诈中心揭秘私下换汇骗局" data-date="09-17 12:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 12:16</span>
          <span class="news-item-title">账户余额到账用钱时却凭空消失 北京反诈中心揭秘私下换汇骗局</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698133.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福建长汀9月17日电 题：福建长汀中复村：红色遗址交织乡村新貌引八方来客" data-title="（长征胜利90周年）福建长汀中复村：红色遗址交织乡村新貌引八方来客" data-date="09-17 11:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 11:48</span>
          <span class="news-item-title">（长征胜利90周年）福建长汀中复村：红色遗址交织乡村新貌引八方来客</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491147.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从9月15日开始，SkyProduction（天工工作台）和火山引擎(Seedance 2.5)隆重推出中秋国庆特惠活动" data-title="首购积分加赠70%：SkyProduction天工工作台联合火山引擎推出中秋国庆三重福利" data-date="09-17 11:39" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 11:39</span>
          <span class="news-item-title">首购积分加赠70%：SkyProduction天工工作台联合火山引擎推出中秋国庆三重福利</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698088.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月17日电 国新办17日就“十五五”时期加快推动广播电视和网络视听高质量发展有关情况举行新闻发布会。会上，广电总局新闻发言人、副局长何飚表示，过去三年，广电总局联合多部门持续推进电视“套娃”收费和操作复杂治理，成效显著。" data-title="国家广电总局：机顶盒功能将以软件形态内置于电视机" data-date="09-17 11:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 11:14</span>
          <span class="news-item-title">国家广电总局：机顶盒功能将以软件形态内置于电视机</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-17 14:50（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
