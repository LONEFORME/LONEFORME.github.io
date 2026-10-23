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
      <span>2026-10-23 14:38 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">7</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · IT之家×6</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-23/10719703.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月23日电 (记者 陈溯)10月23日是世界雪豹日，记者当天从国家林业和草原局获悉，自2013年系统性开展雪豹专项保护工作以来，中国持续加强雪豹保护及其栖息地修复，雪豹种群数量和繁衍活力不断提升。" data-title="中国雪豹种群数量实现恢复性增长" data-date="10-23 14:31" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-23 14:31</span>
      </div>
      <h2 class="hero-featured-title">中国雪豹种群数量实现恢复性增长</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/005.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 23 日消息，开发商 Black Apple 宣布旗下太空生存策略游戏《Terraspace》即日起在 Epic 游戏商城开启限时免费“喜加一”活动，玩家可以在北京时间 10 月 28 日凌晨 4 点前免费领取。需要注意的是，本次限免并非 Epic 官方活动，而是由开发团队自行发起的特别促销，IT之家附游戏商品页（https://store.epicgames.com/p/dimond-hunt-03a766?utm_source=chatgpt.com）。《Terraspace》以尚未开发的星球为舞台，玩家需要收集资源、建造生产设施，满足太空团队的基本生存需求，并逐步打造能够前往其他星球的太空船，开启一场星际移居之旅。在外星球开荒期间，玩家需要规划并建造各类设备与设施，" data-title="Epic 喜加一：太空生存策略游戏《Terraspace》免费领" data-date="10-23 14:36" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">Epic 喜加一：太空生存策略游戏《Terraspace》免费领</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-23/10719704.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网苏州10月23日电 (记者 常慕城)“很高兴能在参加我最爱的运动赛事的同时，还能更好地了解中国，感受它的文化和传统。”22日下午，在结束了愉快的昆山水乡古镇与戏曲非遗研学游之后，来自墨西哥的国际中体联“足球小将”亚历克莎·埃斯特拉达说，今天玩得很开心，既学到了新东西，又能和队友们一起享受这段难忘的经历。" data-title="国际中体联 “足球小将” 畅游苏州 感受中国文化魅力" data-date="10-23 14:37" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">国际中体联 “足球小将” 畅游苏州 感受中国文化魅力</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/006.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，博主 @数码闲聊站 今日透露，荣耀 Magic9 系列 3 款机型，W42（此处指 2026 年的第 42 个自然周，即 10 月 12 日至 10 月 18 日）累计激活 39W 完成反超，成为今年安卓旗舰激活量 TOP1。博主还表示，太励志了，去年 Magic8 系列一直垫底来着。据IT之家此前报道，荣耀 Magic9 系列于 9 月 28 日正式发布，包含荣耀 Magic9 Pro Max、荣耀 Magic9、荣耀 Magic9 超能版，售价 4499 元起。荣耀手机此前宣布，荣耀 Magic9 系列开售一小时，全平台销量同比上代增长 208%。荣耀全球首席营销官关海涛曾表示，受版本缺货等因素，M9（Magic9）系列发布后第 3 天激活较上代增长 7" data-title="今年安卓旗舰激活量 TOP1：消息称荣耀 Magic9 系列 3 款手机累计激活超 39 万台" data-date="10-23 14:37" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">今年安卓旗舰激活量 TOP1：消息称荣耀 Magic9 系列 3 款手机累计激活超 39 万台</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719703.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月23日电 (记者 陈溯)10月23日是世界雪豹日，记者当天从国家林业和草原局获悉，自2013年系统性开展雪豹专项保护工作以来，中国持续加强雪豹保护及其栖息地修复，雪豹种群数量和繁衍活力不断提升。" data-title="中国雪豹种群数量实现恢复性增长" data-date="10-23 14:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 14:31</span>
          <span class="news-item-title">中国雪豹种群数量实现恢复性增长</span>
          <span class="news-value-point">💡 中新社北京10月23日电 (记者 陈溯)10月23日是世界雪豹日，记者当天从国家林业和草原局获悉，自2013年系统性开展雪豹专项保护工作以来，中…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719669.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥10月23日电 （记者 赵强）中国共产党安徽省第十二届委员会第一次全体会议23日在合肥举行。全会选举产生了中共安徽省第十二届委员会常务委员会。" data-title="中共安徽省第十二届委员会常务委员会产生" data-date="10-23 14:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 14:01</span>
          <span class="news-item-title">中共安徽省第十二届委员会常务委员会产生</span>
          <span class="news-value-point">💡 中新网合肥10月23日电 （记者 赵强）中国共产党安徽省第十二届委员会第一次全体会议23日在合肥举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10719670.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="韩国国防部23日发表谈话，正式向朝方提议举行韩朝军方会谈，就相互确认韩朝陆地军事分界线的准确位置、恢复军事通信线路以及防止边境地区发生意外冲突的方案进行协商。如有必要，也可以举行包括“联合国军司令部”在内的三方会谈。" data-title="韩国国防部向朝方提议举行韩朝军方会谈" data-date="10-23 13:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:39</span>
          <span class="news-item-title">韩国国防部向朝方提议举行韩朝军方会谈</span>
          <span class="news-value-point">💡 韩国国防部23日发表谈话，正式向朝方提议举行韩朝军方会谈，就相互确认韩朝陆地军事分界线的准确位置、恢复军事通信线路以及防止边境地区发生意外冲突的…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10719668.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="韩国首尔高等法院23日针对首尔市长吴世勋涉嫌违反《政治资金法》案作出二审判决，判处吴世勋无罪。" data-title="韩国首尔市长二审被判无罪" data-date="10-23 13:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:38</span>
          <span class="news-item-title">韩国首尔市长二审被判无罪</span>
          <span class="news-value-point">💡 韩国首尔高等法院23日针对首尔市长吴世勋涉嫌违反《政治资金法》案作出二审判决，判处吴世勋无罪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719649.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月23日电#8195;中共中央政治局10月23日召开会议，审议《关于二十届中央第七轮巡视情况的综合报告》。中共中央总书记习近平主持会议。" data-title="中共中央政治局召开会议 审议《关于二十届中央第七轮巡视情况的综合报告》 中共中央总书记习近平主持会议" data-date="10-23 13:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:17</span>
          <span class="news-item-title">中共中央政治局召开会议 审议《关于二十届中央第七轮巡视情况的综合报告》 中共中央总书记习近平主持会议</span>
          <span class="news-value-point">💡 新华社北京10月23日电#8195;中共中央政治局10月23日召开会议，审议《关于二十届中央第七轮巡视情况的综合报告》</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10719640.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月23日电 (记者 孙自法)文森特·梵高(Vincent van Gogh)创作于1889年的名画《星月夜》(The Starry Night)，究竟是画家自己的幻想，还是源于真实天文观察的灵感，以及观察星月夜的月份，长期以来颇具争议。" data-title="梵高名画《星月夜》是观察积累还是幻想？研究称灵感或来自7月天空" data-date="10-23 13:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:13</span>
          <span class="news-item-title">梵高名画《星月夜》是观察积累还是幻想？研究称灵感或来自7月天空</span>
          <span class="news-value-point">💡 中新网北京10月23日电 (记者 孙自法)文森特·梵高(Vincent van Gogh)创作于1889年的名画《星月夜》(The Starry…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719639.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社合肥10月23日电 中共安徽省第十二届委员会第一次全体会议10月23日选举李乐成为省委书记，王东伟、单向前为省委副书记，当选为省委常委的还有孙红梅(女，满族)、许永锞、蔚盛斌、覃卫国(壮族)、王金良、范付中、何淳宽、桂桢(女)、朱浩东、蒋曦。中共安徽省第十二届纪委第一次全体会议选举许永锞为省纪委书记，陈学东、李敏(女)、时志远、金更华为省纪委副书记。" data-title="李乐成当选中共安徽省委书记" data-date="10-23 13:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:09</span>
          <span class="news-item-title">李乐成当选中共安徽省委书记</span>
          <span class="news-value-point">💡 新华社合肥10月23日电 中共安徽省第十二届委员会第一次全体会议10月23日选举李乐成为省委书记，王东伟、单向前为省委副书记，当选为省委常委的还…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/world/middleeast/gadi-eisenkot-israel-election.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="艾森科特先生是民意调查中的前军事领导人，他称以色列总理是“反领袖”。“但他低调的竞选风格让支持者感到担忧。" data-title="Gadi Eisenkot Couldn’t Be More Unlike Netanyahu. Can He Beat Him?" data-date="10-23 12:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-23 12:01</span>
          <span class="news-item-title">加迪·艾森科特（ Gadi Eisenkot ）与内塔尼亚胡（ Netanyahu ）完全不同。他能打败他吗？</span>
          <span class="news-item-title-en">Gadi Eisenkot Couldn’t Be More Unlike Netanyahu. Can He Beat Him?</span>
          <span class="news-value-point">💡 艾森科特先生是民意调查中的前军事领导人，他称以色列总理是“反领袖”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10719564.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网加德满都10月23日电 据《加德满都邮报》22日报道，尼泊尔西部萨利扬县持续数月的恙虫病疫情累计报告817例病例、10人死亡。" data-title="尼泊尔萨利扬县恙虫病疫情持续数月 累计致10人死亡" data-date="10-23 10:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 10:57</span>
          <span class="news-item-title">尼泊尔萨利扬县恙虫病疫情持续数月 累计致10人死亡</span>
          <span class="news-value-point">💡 中新网加德满都10月23日电 据《加德满都邮报》22日报道，尼泊尔西部萨利扬县持续数月的恙虫病疫情累计报告817例病例、10人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10719578.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月23日电 据美国消费者新闻与商业频道(CNBC)报道，当地时间21日，美国新墨西哥州一名法官裁定，美国元公司(Meta)应就数据隐私误导用户问题缴纳250亿美元罚金。" data-title="被判支付250亿美元 美国Meta公司因误导用户被重罚" data-date="10-23 10:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 10:43</span>
          <span class="news-item-title">被判支付250亿美元 美国Meta公司因误导用户被重罚</span>
          <span class="news-value-point">💡 中新网10月23日电 据美国消费者新闻与商业频道(CNBC)报道，当地时间21日，美国新墨西哥州一名法官裁定，美国元公司(Meta)应就数据隐私…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10719545.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月23日电 伊斯兰堡消息：当地时间10月22日，巴基斯坦警方在该国开伯尔-普什图省开展反恐搜剿行动，击毙2名恐怖分子。双方交火期间，4名警察殉职，其中包含一名反恐部门高级警官。" data-title="巴基斯坦反恐行动击毙2名恐怖分子  4名警察殉职" data-date="10-23 10:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 10:14</span>
          <span class="news-item-title">巴基斯坦反恐行动击毙2名恐怖分子  4名警察殉职</span>
          <span class="news-value-point">💡 中新社北京10月23日电 伊斯兰堡消息：当地时间10月22日，巴基斯坦警方在该国开伯尔-普什图省开展反恐搜剿行动，击毙2名恐怖分子</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckx2qdelv0jeo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普的律师表示，总统可以在明年1月11日至22日期间接受问话，并称英国广播公司“错误地声称特朗普总统在本案中逃避庭外宣誓作证”。" data-title="特朗普诉BBC诽谤案：法官下令总统须宣誓并答问作证" data-date="10-23 09:42" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 09:42</span>
          <span class="news-item-title">特朗普诉BBC诽谤案：法官下令总统须宣誓并答问作证</span>
          <span class="news-value-point">💡 特朗普的律师表示，总统可以在明年1月11日至22日期间接受问话，并称英国广播公司“错误地声称特朗普总统在本案中逃避庭外宣誓作证”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/22/us/politics/starshield-outage-ukraine-musk-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="乌克兰官员报告说，他们在对抗俄罗斯的战争中发现了对使用军用无人机的新限制，此后总统就Starshield网络发出了呼吁。" data-title="Trump Asked Musk to Reverse Limits on Ukraine’s Military Internet Use" data-date="10-23 09:31" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-23 09:31</span>
          <span class="news-item-title">特朗普要求马斯克取消对乌克兰军事互联网使用的限制</span>
          <span class="news-item-title-en">Trump Asked Musk to Reverse Limits on Ukraine’s Military Internet Use</span>
          <span class="news-value-point">💡 乌克兰官员报告说，他们在对抗俄罗斯的战争中发现了对使用军用无人机的新限制，此后总统就Starshield网络发出了呼吁</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/22/us/politics/pete-ricketts-billionaire-nebraska-senate-race.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在富人的财富飙升而工人因通货膨胀而失去优势的一年里，阶级已经成为政治，特别是在内布拉斯加州参议院竞选中。" data-title="Pete Ricketts’s Wealth Puts Class at the Center of Nebraska’s Senate Race" data-date="10-23 09:04" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-23 09:04</span>
          <span class="news-item-title">皮特·里基茨的财富将课堂置于内布拉斯加州参议院竞选的中心</span>
          <span class="news-item-title-en">Pete Ricketts’s Wealth Puts Class at the Center of Nebraska’s Senate Race</span>
          <span class="news-value-point">💡 在富人的财富飙升而工人因通货膨胀而失去优势的一年里，阶级已经成为政治，特别是在内布拉斯加州参议院竞选中</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckx2q587wvrqo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国政坛至今没有明确的接班人。受访专家认为，这反映习近平面临两难：不指定接班人有助维持权威，指定接班人则可能提前形成新的权力中心。" data-title="中共五中全会前瞻：会前为何密集“打虎”？未来怎样“从严治党”？" data-date="10-23 08:41" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 08:41</span>
          <span class="news-item-title">中共五中全会前瞻：会前为何密集“打虎”？未来怎样“从严治党”？</span>
          <span class="news-value-point">💡 中国政坛至今没有明确的接班人</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/005.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 23 日消息，开发商 Black Apple 宣布旗下太空生存策略游戏《Terraspace》即日起在 Epic 游戏商城开启限时免费“喜加一”活动，玩家可以在北京时间 10 月 28 日凌晨 4 点前免费领取。需要注意的是，本次限免并非 Epic 官方活动，而是由开发团队自行发起的特别促销，IT之家附游戏商品页（https://store.epicgames.com/p/dimond-hunt-03a766?utm_source=chatgpt.com）。《Terraspace》以尚未开发的星球为舞台，玩家需要收集资源、建造生产设施，满足太空团队的基本生存需求，并逐步打造能够前往其他星球的太空船，开启一场星际移居之旅。在外星球开荒期间，玩家需要规划并建造各类设备与设施，" data-title="Epic 喜加一：太空生存策略游戏《Terraspace》免费领" data-date="10-23 14:36" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 14:36</span>
          <span class="news-item-title">Epic 喜加一：太空生存策略游戏《Terraspace》免费领</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，开发商 Black Apple 宣布旗下太空生存策略游戏《Terraspace》即日起在 Epic 游戏商城开…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/998.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 23 日消息，被誉为“AI 教父”之一的英国计算机科学家杰弗里 · 辛顿，再次对人类的未来发出悲观警告。辛顿接受英国《每日电讯报》采访时坚称，AI 已经具备意识，人类必须与 AI 友好相处，否则“我们就完了”。在他看来，即便是当下的 AI 模型，也拥有自己的意识。“AI 拥有与人类同等程度的主观体验。最近有篇论文发现，AI 如果认为自己在接受测试，就会改变行为。它知道自己在接受测试。通常来说，如果一个事物能够觉察到这种情况，就意味着它有意识。意识和觉察能力基本是一回事。”辛顿是 2018 年图灵奖的三名得主之一，并于 2024 年获得诺贝尔物理学奖。图灵奖素有“计算机界诺贝尔奖”之称，辛顿在神经网络领域的研究也为近年来的 AI 发展奠定了重要基础。自从离开谷歌，并公开表示" data-title="“AI 教父”辛顿再抛悲观论：AI 已经拥有意识，人类必须与其友好相处" data-date="10-23 14:18" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 14:18</span>
          <span class="news-item-title">“AI 教父”辛顿再抛悲观论：AI 已经拥有意识，人类必须与其友好相处</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，被誉为“AI 教父”之一的英国计算机科学家杰弗里 · 辛顿，再次对人类的未来发出悲观警告</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c370pr45nelgo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能发现了长期未被察觉的程式漏洞，引发全球罕见的大规模网络安全应对行动。" data-title="PHP是什么？为何它引发全球网络安全危机？" data-date="10-23 13:01" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 13:01</span>
          <span class="news-item-title">PHP是什么？为何它引发全球网络安全危机？</span>
          <span class="news-value-point">💡 人工智能发现了长期未被察觉的程式漏洞，引发全球罕见的大规模网络安全应对行动</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/uber-rival-indrive-eyes-2027-robotaxi-tests-in-central-asia-with-pony-ai-and-nvidia/" target="_blank" rel="noopener" data-cat="keji" data-summary="inDrive计划于2027年上半年在哈萨克斯坦首都开始测试Pony.ai的机器人出租车。" data-title="Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia" data-date="10-23 12:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 12:00</span>
          <span class="news-item-title">优步的竞争对手inDrive eyes 2027与Pony.ai和Nvidia在中亚进行机器人出租车测试</span>
          <span class="news-item-title-en">Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia</span>
          <span class="news-value-point">💡 inDrive计划于2027年上半年在哈萨克斯坦首都开始测试Pony.ai的机器人出租车</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/" target="_blank" rel="noopener" data-cat="keji" data-summary="麻省理工学院的研究人员在一个虚拟岛屿上放逐了13个人工智能，他们通过发明游戏，哀悼丢失的戒指，最终在工作中变得更好。" data-title="Left alone with nothing to do, AI agents started playing" data-date="10-23 08:45" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 08:45</span>
          <span class="news-item-title">独自一人无事可做，人工智能特工开始玩</span>
          <span class="news-item-title-en">Left alone with nothing to do, AI agents started playing</span>
          <span class="news-value-point">💡 麻省理工学院的研究人员在一个虚拟岛屿上放逐了13个人工智能，他们通过发明游戏，哀悼丢失的戒指，最终在工作中变得更好</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1017261/etsy-ai-rules-policies-restrictions-listing" target="_blank" rel="noopener" data-cat="keji" data-summary="Etsy宣布了更严格的规则，规定如何在房源中使用人工智能，以减少平台上的人工智能流量。该公司在一篇帖子中表示， “许多活跃的买家表示，他们无法分辨哪些商品涉及人工智能生成的内容” ，而该卖家" data-title="Etsy is cracking down on AI slop listings" data-date="10-23 08:09" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 08:09</span>
          <span class="news-item-title">Etsy正在严厉打击AI SLOP房源</span>
          <span class="news-item-title-en">Etsy is cracking down on AI slop listings</span>
          <span class="news-value-point">💡 Etsy宣布了更严格的规则，规定如何在房源中使用人工智能，以减少平台上的人工智能流量</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/" target="_blank" rel="noopener" data-cat="keji" data-summary="如果OpenAI在这轮融资中获得超过1万亿美元的估值，它将打破有史以来估值最高的私人公司的纪录。" data-title="OpenAI working on new $30B raise at $1.25T valuation ahead of IPO" data-date="10-23 06:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 06:08</span>
          <span class="news-item-title">OpenAI在IPO之前以$ 1.25 T的估值进行新的$ 300亿加息</span>
          <span class="news-item-title-en">OpenAI working on new $30B raise at $1.25T valuation ahead of IPO</span>
          <span class="news-value-point">💡 如果OpenAI在这轮融资中获得超过1万亿美元的估值，它将打破有史以来估值最高的私人公司的纪录</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1017151/canva-craft-in-house-ai-model" target="_blank" rel="noopener" data-cat="keji" data-summary="通过推出与OpenAI、微软和谷歌直接竞争的图像生成模型， Canva正在更深入地研究人工智能。这个名为Canva Craft的模型使用两阶段架构，允许它在" data-title="Canva’s first AI image model plans designs before generating them" data-date="10-23 05:51" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 05:51</span>
          <span class="news-item-title">Canva的首个AI图像模型在生成设计之前对其进行规划</span>
          <span class="news-item-title-en">Canva’s first AI image model plans designs before generating them</span>
          <span class="news-value-point">💡 通过推出与OpenAI、微软和谷歌直接竞争的图像生成模型， Canva正在更深入地研究人工智能</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1016506/fall-2026-earnings-watch" target="_blank" rel="noopener" data-cat="keji" data-summary="每家公司都突然变成了一家人工智能公司。计算是一种资产。汽车正在飞行。我们再次得到了机器人的承诺。是时候再次浏览收益报告，聆听投资者的电话，并指出科技行业的最新盈亏情况" data-title="Fall 2026 earnings watch" data-date="10-23 05:15" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 05:15</span>
          <span class="news-item-title">2026年秋季收入观察</span>
          <span class="news-item-title-en">Fall 2026 earnings watch</span>
          <span class="news-value-point">💡 每家公司都突然变成了一家人工智能公司</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1017082/meta-terms-update-ai-training-concerns" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta已经调整了其业务条款，删除了表明它可以在新闻网站（如The Verge ）上自由训练其人工智能模型的语言，但法律专家表示，这些变化不足以解决他们的担忧。“这并没有限制" data-title="Meta’s AI could still scrape news sites, legal experts say" data-date="10-23 04:32" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 04:32</span>
          <span class="news-item-title">法律专家表示， Meta的人工智能仍然可以抓取新闻网站</span>
          <span class="news-item-title-en">Meta’s AI could still scrape news sites, legal experts say</span>
          <span class="news-value-point">💡 Meta已经调整了其业务条款，删除了表明它可以在新闻网站（如The Verge ）上自由训练其人工智能模型的语言，但法律专家表示，这些变化不足以…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/" target="_blank" rel="noopener" data-cat="keji" data-summary="新功能允许客服代表登录客户的个人账号，同时保护用于保护这些账号的私人凭据。" data-title="1Password launches a way for AI agents to log in on your behalf without seeing your password" data-date="10-23 03:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 03:07</span>
          <span class="news-item-title">1Password为AI代理推出了一种无需查看密码即可代您登录的方式</span>
          <span class="news-item-title-en">1Password launches a way for AI agents to log in on your behalf without seeing your password</span>
          <span class="news-value-point">💡 新功能允许客服代表登录客户的个人账号，同时保护用于保护这些账号的私人凭据</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI正在向全世界推出其决策模型。它能与原来的Jev竞争吗？" data-title="OpenAI makes its Jev competitor widely available as decision model competition heats up" data-date="10-23 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 03:00</span>
          <span class="news-item-title">随着决策模型竞争的加剧， OpenAI使其JEV竞争对手广泛可用</span>
          <span class="news-item-title-en">OpenAI makes its Jev competitor widely available as decision model competition heats up</span>
          <span class="news-value-point">💡 OpenAI正在向全世界推出其决策模型</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/" target="_blank" rel="noopener" data-cat="keji" data-summary="根据《科学》杂志的一项研究，微软的新人工智能诊断系统在困难病例上击败了多面手医生。但大部分改进似乎来自下面的人工智能模型，而不是来自微软的系统本身。" data-title="Microsoft’s Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases ‘medical superintelligence’" data-date="10-23 02:43" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 02:43</span>
          <span class="news-item-title">微软的穆斯塔法·苏莱曼（ Mustafa Suleyman ）表示，在追求“医学超级智能”的过程中，其人工智能在困难病例上的表现优于医生</span>
          <span class="news-item-title-en">Microsoft’s Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases ‘medical superintelligence’</span>
          <span class="news-value-point">💡 根据《科学》杂志的一项研究，微软的新人工智能诊断系统在困难病例上击败了多面手医生</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/22/business/media/ai-disinfo-chatbots-elections.html" target="_blank" rel="noopener" data-cat="keji" data-summary="中期选举是第一次将人工智能整合到每个主要社交媒体平台的选举。削弱其危害的努力是不平衡的。" data-title="A.I. and Its Dangers Are Embedded In the Midterm Elections" data-date="10-23 01:07" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-23 01:07</span>
          <span class="news-item-title">人工智能及其危险嵌入中期选举</span>
          <span class="news-item-title-en">A.I. and Its Dangers Are Embedded In the Midterm Elections</span>
          <span class="news-value-point">💡 中期选举是第一次将人工智能整合到每个主要社交媒体平台的选举</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1016798/php-vulnerabilities-exploit-patch" target="_blank" rel="noopener" data-cat="keji" data-summary="根据亚马逊威胁情报（ Amazon Threat Intelligence ）的一份报告，黑客试图在修补网站前几天利用影响网站的PHP漏洞。亚马逊首席信息安全官CJ Moses写道，该公司的安全" data-title="The disastrous PHP vulnerabilities were exploited days before the patch" data-date="10-23 00:49" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 00:49</span>
          <span class="news-item-title">灾难性的PHP漏洞在补丁发布前几天就被利用了</span>
          <span class="news-item-title-en">The disastrous PHP vulnerabilities were exploited days before the patch</span>
          <span class="news-value-point">💡 根据亚马逊威胁情报（ Amazon Threat Intelligence ）的一份报告，黑客试图在修补网站前几天利用影响网站的PHP漏洞</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">3 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719704.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网苏州10月23日电 (记者 常慕城)“很高兴能在参加我最爱的运动赛事的同时，还能更好地了解中国，感受它的文化和传统。”22日下午，在结束了愉快的昆山水乡古镇与戏曲非遗研学游之后，来自墨西哥的国际中体联“足球小将”亚历克莎·埃斯特拉达说，今天玩得很开心，既学到了新东西，又能和队友们一起享受这段难忘的经历。" data-title="国际中体联 “足球小将” 畅游苏州 感受中国文化魅力" data-date="10-23 14:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 14:37</span>
          <span class="news-item-title">国际中体联 “足球小将” 畅游苏州 感受中国文化魅力</span>
          <span class="news-value-point">💡 中新网苏州10月23日电 (记者 常慕城)“很高兴能在参加我最爱的运动赛事的同时，还能更好地了解中国，感受它的文化和传统</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/23/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马克斯·道曼可能有机会，马刺需要在斯坦福桥找到平衡，阿克塞尔·迪萨西必须做出弥补英超联赛得分王经过七场比赛，诺丁汉森林的记录与上赛季惊人地相似：五分，五个进球。是的" data-title="Premier League: 10 things to look out for this weekend" data-date="10-23 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-23 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 马克斯·道曼可能有机会，马刺需要在斯坦福桥找到平衡，阿克塞尔·迪萨西必须做出弥补英超联赛得分王经过七场比赛，诺丁汉森林的记录与上赛季惊人地相似：…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3y0eqkneze4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领Waffle the Wonder Dog和他的主人西蒙（ Simon ） ，以及英国广播公司的读者和人工智能，对本周末的英超联赛进行了预测。" data-title="Sutton&#39;s predictions v Waffle the Wonder Dog and his owner, Simon" data-date="10-23 00:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 00:30</span>
          <span class="news-item-title">Sutton的预测v Waffle the Wonder Dog和他的主人Simon</span>
          <span class="news-item-title-en">Sutton's predictions v Waffle the Wonder Dog and his owner, Simon</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领Waffle the Wonder Dog和他的主人西蒙（ Simon …</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/006.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，博主 @数码闲聊站 今日透露，荣耀 Magic9 系列 3 款机型，W42（此处指 2026 年的第 42 个自然周，即 10 月 12 日至 10 月 18 日）累计激活 39W 完成反超，成为今年安卓旗舰激活量 TOP1。博主还表示，太励志了，去年 Magic8 系列一直垫底来着。据IT之家此前报道，荣耀 Magic9 系列于 9 月 28 日正式发布，包含荣耀 Magic9 Pro Max、荣耀 Magic9、荣耀 Magic9 超能版，售价 4499 元起。荣耀手机此前宣布，荣耀 Magic9 系列开售一小时，全平台销量同比上代增长 208%。荣耀全球首席营销官关海涛曾表示，受版本缺货等因素，M9（Magic9）系列发布后第 3 天激活较上代增长 7" data-title="今年安卓旗舰激活量 TOP1：消息称荣耀 Magic9 系列 3 款手机累计激活超 39 万台" data-date="10-23 14:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 14:37</span>
          <span class="news-item-title">今年安卓旗舰激活量 TOP1：消息称荣耀 Magic9 系列 3 款手机累计激活超 39 万台</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，博主 @数码闲聊站 今日透露，荣耀 Magic9 系列 3 款机型，W42（此处指 2026 年的第 42 个…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719708.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州10月23日电 (记者 王坚)以“以创作赴约让世界看见”为主题的“2026内容创作者嘉年华”23日在广州南沙举行。活动现场，“广东互联网优质内容生态全域共创计划”发布，将扶持从政策层面进一步落到生态构建之上。" data-title="“广东互联网优质内容生态全域共创计划”发布" data-date="10-23 14:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 14:36</span>
          <span class="news-item-title">“广东互联网优质内容生态全域共创计划”发布</span>
          <span class="news-value-point">💡 中新网广州10月23日电 (记者 王坚)以“以创作赴约让世界看见”为主题的“2026内容创作者嘉年华”23日在广州南沙举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/003.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，HP（惠普）现已在电商平台上架新款的战 99 Ultra (ZHAN99 Ultra 16 G3a AI) 移动工作站。该型号基于 AMD 锐龙 AI Max+ PRO 495 处理器，配备 128GB 内存、1TB 存储，标价 59,999 元，10 月 30 日 20:00 开售。IT之家注意到，这款机型很有可能就是全球市场的 ZBook Ultra G3a 16&quot;，支持 100W 性能释放，可选 5G 蜂窝网络连接，集成 96Whr 电池，起始质量 1.9kg。该产品在描述中提到了 2 种屏幕规格，分别 &quot;4K&quot;（这里应指 3840×2400）和 2560×1600 120Hz 400nits，暂不清楚哪个是正确的。" data-title="惠普战 99 Ultra &quot;Gorgon Halo&quot; 移动工作站上架，标价 59999 元" data-date="10-23 14:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 14:26</span>
          <span class="news-item-title">惠普战 99 Ultra "Gorgon Halo" 移动工作站上架，标价 59999 元</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，HP（惠普）现已在电商平台上架新款的战 99 Ultra (ZHAN99 Ultra 16 G3a AI) 移…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/001.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，消息源 mr.grey_4k 昨日（10 月 22 日）在 Instagram 平台发帖，分享了一组在德国抓拍的路测图，展示了 2028 款雷克萨斯 LFA 电动超跑。外观方面，新车身披迷彩伪装，造型低趴修长，后尾翼处于展开状态，整体姿态比前代更具攻击性。动力方面，与初代 LFA 标志性的 4.8 升 V10 自然吸气发动机不同，新一代车型预计采用纯电动力，并与丰田 GR GT、GR GT3 共享铝制底盘架构。IT之家附上相关路测图如下：技术层面，新车可能成为丰田集团首款搭载固态电池的量产车型，以获得更高能量密度、更轻的电池重量以及更长的续航表现。不过，雷克萨斯尚未公布电池容量、动力、续航与加速等官方参数。驾驶体验方面，专利与报道显示，新 LFA 或通过软件" data-title="V10 声浪：2028 款雷克萨斯 LFA 电动超跑路测图曝光" data-date="10-23 14:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 14:24</span>
          <span class="news-item-title">V10 声浪：2028 款雷克萨斯 LFA 电动超跑路测图曝光</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，消息源 mr.grey_4k 昨日（10 月 22 日）在 Instagram 平台发帖，分享了一组在德国抓拍…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/999.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【京东活动可能随时变更，需以实付款为准】石头 A30 Pro Steam 3.0 洗地机 2026 年 8 月开售，该产品号称首次实现了 180℃ 活性蒸汽与 90℃ 高温热水的一键混洗，可在重度油污环境使用，首发价 3299 元。京东 11.11 大促期间，按下方步骤下单，叠加 15% 国补后仅需 2171.75 元：领 2000-235 元券：点击下方卡片跳转详情页后，系统自动发放。下单时选择“以旧换新 → 个护健康 → 电动牙刷（无需回收）”补贴 150 元。京东石头 A30 Pro Steam 3.0 洗地机 180° 蒸汽 + 90° 热水以旧换新后 2171.75 元直达链接京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。该洗地机采用静士" data-title="首发价 3299 → 2171 元：石头洗地机 A30 Pro Steam 3.0 国补直降，32000Pa 吸力 + 蒸汽热水混洗" data-date="10-23 14:18" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 14:18</span>
          <span class="news-item-title">首发价 3299 → 2171 元：石头洗地机 A30 Pro Steam 3.0 国补直降，32000Pa 吸力 + 蒸汽热水混洗</span>
          <span class="news-value-point">💡 【京东活动可能随时变更，需以实付款为准】石头 A30 Pro Steam 3.0 洗地机 2026 年 8 月开售，该产品号称首次实现了 180…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719694.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网兰州10月23日电 (闫姣 田鹏鹤)古镇哈达铺，是红军长征抵达甘肃后的关键休整地与决策节点，被称作长征路上的“加油站”。九十载岁月流转，红色旧址静静伫立，迎来天南海北的游客。" data-title="长征路上学党史丨古镇哈达铺迎红色旅游热" data-date="10-23 14:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 14:16</span>
          <span class="news-item-title">长征路上学党史丨古镇哈达铺迎红色旅游热</span>
          <span class="news-value-point">💡 中新网兰州10月23日电 (闫姣 田鹏鹤)古镇哈达铺，是红军长征抵达甘肃后的关键休整地与决策节点，被称作长征路上的“加油站”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719642.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨10月23日电(王妮娜 杨爽)10月23日是霜降节气，霜降携清冽寒气而来，黑龙江省气温自立秋起持续走低，到霜降节气，全省平均最低气温降至0℃以下。" data-title="霜降节气至 黑龙江平均最低气温降至0℃以下" data-date="10-23 14:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 14:12</span>
          <span class="news-item-title">霜降节气至 黑龙江平均最低气温降至0℃以下</span>
          <span class="news-value-point">💡 中新网哈尔滨10月23日电(王妮娜 杨爽)10月23日是霜降节气，霜降携清冽寒气而来，黑龙江省气温自立秋起持续走低，到霜降节气，全省平均最低气温…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719686.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，受台风“蔷琵”影响，福建沿海出现8级及以上大风。" data-title="受台风影响 福建沿海56条客渡运航线停航 转移13.41万人" data-date="10-23 13:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:59</span>
          <span class="news-item-title">受台风影响 福建沿海56条客渡运航线停航 转移13.41万人</span>
          <span class="news-value-point">💡 今天，受台风“蔷琵”影响，福建沿海出现8级及以上大风</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719683.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月23日电 据西藏自治区财政厅微信公众号消息，10月22日22时33分，那曲市巴青县发生7.0级地震。按照自治区党委、政府决策部署，自治区财政厅快速建立资金保障绿色通道。10月23日，自治区财政厅紧急拨付中央自然灾害救灾资金5000万元，加上自治区安排的救灾资金2000万元，已累计预拨自然灾害救灾资金7000万元，全力保障做好抢险救灾工作。" data-title="西藏自治区财政厅紧急拨付那曲市巴青县自然灾害救灾资金7000万元" data-date="10-23 13:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:59</span>
          <span class="news-item-title">西藏自治区财政厅紧急拨付那曲市巴青县自然灾害救灾资金7000万元</span>
          <span class="news-value-point">💡 中新网10月23日电 据西藏自治区财政厅微信公众号消息，10月22日22时33分，那曲市巴青县发生7.0级地震</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719637.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月23日电 (记者 孙自法)中国地震局10月23日向媒体通报说，西藏自治区那曲市巴青县10月22日夜间发生的7.0级地震为一次拉张型破裂，震中位于青藏高原的羌塘地块内部，距此次地震最近的断层为巴青—类乌齐断裂，距离约2公里。" data-title="中国地震局：西藏巴青7.0级地震为拉张型破裂 震中位于羌塘地块内部" data-date="10-23 13:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:55</span>
          <span class="news-item-title">中国地震局：西藏巴青7.0级地震为拉张型破裂 震中位于羌塘地块内部</span>
          <span class="news-value-point">💡 中新网北京10月23日电 (记者 孙自法)中国地震局10月23日向媒体通报说，西藏自治区那曲市巴青县10月22日夜间发生的7.0级地震为一次拉张…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719675.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海10月23日电 题：在前滩，从远道而来到安心安家" data-title="在前滩，从远道而来到安心安家" data-date="10-23 13:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:48</span>
          <span class="news-item-title">在前滩，从远道而来到安心安家</span>
          <span class="news-value-point">💡 中新网上海10月23日电 题：在前滩，从远道而来到安心安家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10719658.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网呼和浩特10月23日电 (记者 尚虹波)近期，中新网刊发多篇内蒙古秋收一线的报道：武川冷凉蔬菜批量出口东南亚，察右中旗红萝卜、察右后旗火山洋葱订单走俏，化德县则依托治沙后的沙荒地布局风光储能项目，为乌兰察布算力产业输送绿电。一组来自阴山北麓“后山”大地的丰收与产业消息，让流传百年的民谚“后山三件宝，山药、莜面、大皮袄”，有了新的解读视角。" data-title="内蒙古后山之变：从“活命三宝” 到多元新业" data-date="10-23 13:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 13:42</span>
          <span class="news-item-title">内蒙古后山之变：从“活命三宝” 到多元新业</span>
          <span class="news-value-point">💡 中新网呼和浩特10月23日电 (记者 尚虹波)近期，中新网刊发多篇内蒙古秋收一线的报道：武川冷凉蔬菜批量出口东南亚，察右中旗红萝卜、察右后旗火山…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c9zrd1rd3jmyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="地震发生在西藏东北部一个山区且人口稀少的地区。" data-title="西藏那曲7级地震16死54伤，当局派翼龙无人机进行灾情侦察" data-date="10-23 13:23" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 13:23</span>
          <span class="news-item-title">西藏那曲7级地震16死54伤，当局派翼龙无人机进行灾情侦察</span>
          <span class="news-value-point">💡 地震发生在西藏东北部一个山区且人口稀少的地区</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719631.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="台风“蔷琵”持续影响台湾，台湾地区灾害应变中心23日上午公布最新统计，台风造成全台累计1人死亡、94人受伤，伤者较昨晚增加52人。" data-title="台风“蔷琵”已致台湾1人死亡 94人受伤" data-date="10-23 12:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 12:49</span>
          <span class="news-item-title">台风“蔷琵”已致台湾1人死亡 94人受伤</span>
          <span class="news-value-point">💡 台风“蔷琵”持续影响台湾，台湾地区灾害应变中心23日上午公布最新统计，台风造成全台累计1人死亡、94人受伤，伤者较昨晚增加52人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10719625.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月23日电 据国家发展改革委微信公众号消息，10月22日22时33分许，西藏那曲市巴青县发生7.0级地震，造成重大人员伤亡。国家防减救灾委、应急管理部启动国家自然灾害救助四级应急响应。" data-title="国家发展改革委紧急安排3000万元中央预算内投资支持西藏巴青7.0级地震灾害灾后应急恢复" data-date="10-23 12:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 12:25</span>
          <span class="news-item-title">国家发展改革委紧急安排3000万元中央预算内投资支持西藏巴青7.0级地震灾害灾后应急恢复</span>
          <span class="news-value-point">💡 中新网10月23日电 据国家发展改革委微信公众号消息，10月22日22时33分许，西藏那曲市巴青县发生7.0级地震，造成重大人员伤亡</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-23 14:38（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
