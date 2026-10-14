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
      <span>2026-10-14 20:58 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">52</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-14/10714658.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="德国外交部长瓦德富尔当地时间10月14日表示，德国政府将等待“北溪”天然气管道爆炸案的审判结果，并将其纳入今后的政治考量。" data-title="德外长：将把“北溪”爆炸案审判结果纳入政治考量" data-date="10-14 20:47" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-14 20:47</span>
      </div>
      <h2 class="hero-featured-title">德外长：将把“北溪”爆炸案审判结果纳入政治考量</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/013/094.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，苹果公司今日推送 iOS 27.2 Beta 4 开发者预览版（24B5110a）操作系统，为 Siri AI 新增五种语言。本次更新后，Siri AI 将支持英语、法语、日语、韩语、葡萄牙语和西班牙语。苹果已在此前确认这些语言扩展支持，具体可用性仍取决于用户所在地区和设备。IT之家了解到，Siri AI 是苹果最新的人工智能助理，支持 Apple 智能的各种新本领，其调用方法和平时使用 Siri 一样，理解个人情境，执行 App 操作、感知屏幕、理解图像、以及调用广博的世界知识。除此之外还拥有全新的专属 App，具备可跨平台提供视觉智能、集成工具来写作和编辑功能。" data-title="苹果 iOS 27.2 Beta 4 系统 Siri AI 新增支持法语、日语、西班牙语等" data-date="10-14 20:53" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">苹果 iOS 27.2 Beta 4 系统 Siri AI 新增支持法语、日语、西班牙语等</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/news/articles/c83vq9vpwwr1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力。" data-title="Burnham had two hospitality dinners with Man City chairman, deleted records show" data-date="10-14 20:47" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Burnham had two hospitality dinners with Man City chairman, deleted records show</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/013/093.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，在今天的维信诺 × iQOO × 清华大学屏幕技术沟通会上，iQOO 产品副总裁罗峰现场宣布，iQOO Neo12“十月底见”（PPT 显示十月见）。据介绍，iQOO Neo12 手机将行业首发搭载 pTSF 技术的 2K 185Hz 超冠屏、行业首发“天空之镜”发光材料、行业首发 2K 185Hz 高性能驱动芯片。另外，新机将行业首发 2K 185FPS 超分超帧并发、行业首批适配原生 2K 超高清游戏、适配超 50 款原生 185 帧游戏等。新机将在本月发布。IT之家整理 iQOO Neo12 手机已公布 / 曝光配置如下：性能：第五代骁龙 8 至尊版处理器 | 自研电竞芯片 Q3 | 全新一代 Monster 超核引擎散热：冰穹风冷散热系统（主动散热风" data-title="iQOO Neo12 手机官宣“十月底见”：pTSF 技术 2K 185Hz 超冠屏、第五代骁龙 8 至尊版芯片" data-date="10-14 20:51" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">iQOO Neo12 手机官宣“十月底见”：pTSF 技术 2K 185Hz 超冠屏、第五代骁龙 8 至尊版芯片</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714658.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="德国外交部长瓦德富尔当地时间10月14日表示，德国政府将等待“北溪”天然气管道爆炸案的审判结果，并将其纳入今后的政治考量。" data-title="德外长：将把“北溪”爆炸案审判结果纳入政治考量" data-date="10-14 20:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 20:47</span>
          <span class="news-item-title">德外长：将把“北溪”爆炸案审判结果纳入政治考量</span>
          <span class="news-value-point">💡 德国外交部长瓦德富尔当地时间10月14日表示，德国政府将等待“北溪”天然气管道爆炸案的审判结果，并将其纳入今后的政治考量</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-starlink-energy.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星计划似乎在没有任何警告的情况下受到遏制。" data-title="Sudden Starlink Restrictions Deepen Ukraine’s Vulnerability as Russia Escalates" data-date="10-14 20:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 20:39</span>
          <span class="news-item-title">随着俄罗斯升级，突如其来的Starlink限制加深了乌克兰的脆弱性</span>
          <span class="news-item-title-en">Sudden Starlink Restrictions Deepen Ukraine’s Vulnerability as Russia Escalates</span>
          <span class="news-value-point">💡 一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星计划似乎在没有任何警告的情况下受到遏制</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/us/politics/susan-collins-trump-maine-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="缅因州的竞选可能会决定参议院的控制权，这场竞选正在考验柯林斯在急剧两极分化的总统任期内是否仍然有温和的空间。" data-title="A Trump Backlash Endangers Susan Collins in the Maine Senate Race" data-date="10-14 20:26" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 20:26</span>
          <span class="news-item-title">在缅因州参议院竞选中，特朗普的强烈反对危及苏珊·柯林斯</span>
          <span class="news-item-title-en">A Trump Backlash Endangers Susan Collins in the Maine Senate Race</span>
          <span class="news-value-point">💡 缅因州的竞选可能会决定参议院的控制权，这场竞选正在考验柯林斯在急剧两极分化的总统任期内是否仍然有温和的空间</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714627.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月14日电 (马帅莎 张艳)北京时间10月14日19时40分，朱雀二号改进型遥四运载火箭在东风商业航天创新试验区发射升空，将搭载的国星宇航星时代-39、44~50星，光传-03、04星共10颗卫星顺利送入预定轨道，飞行试验任务取得圆满成功。" data-title="一箭十星 朱雀二号改进型遥四运载火箭发射成功" data-date="10-14 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 20:07</span>
          <span class="news-item-title">一箭十星 朱雀二号改进型遥四运载火箭发射成功</span>
          <span class="news-value-point">💡 中新网北京10月14日电 (马帅莎 张艳)北京时间10月14日19时40分，朱雀二号改进型遥四运载火箭在东风商业航天创新试验区发射升空，将搭载的…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714630.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月14日电 2026年国际议员友好交流论坛天津宣言" data-title="2026年国际议员友好交流论坛天津宣言" data-date="10-14 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 20:07</span>
          <span class="news-item-title">2026年国际议员友好交流论坛天津宣言</span>
          <span class="news-value-point">💡 新华社北京10月14日电 2026年国际议员友好交流论坛天津宣言</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714625.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据广西壮族自治区纪委监委消息：广西壮族自治区国资委原党委副书记、副主任聂江武涉嫌严重违纪违法，目前正接受广西壮族自治区纪委监委纪律审查和监察调查。" data-title="广西壮族自治区国资委原副主任聂江武接受审查调查" data-date="10-14 19:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:57</span>
          <span class="news-item-title">广西壮族自治区国资委原副主任聂江武接受审查调查</span>
          <span class="news-value-point">💡 中新网10月14日电 据广西壮族自治区纪委监委消息：广西壮族自治区国资委原党委副书记、副主任聂江武涉嫌严重违纪违法，目前正接受广西壮族自治区纪委…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714589.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月14日电 全国人大常委会委员长赵乐际14日在北京集体会见出席2026年国际议员友好交流论坛的各国代表。" data-title="赵乐际集体会见出席2026年国际议员友好交流论坛的各国代表" data-date="10-14 19:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:55</span>
          <span class="news-item-title">赵乐际集体会见出席2026年国际议员友好交流论坛的各国代表</span>
          <span class="news-value-point">💡 新华社北京10月14日电 全国人大常委会委员长赵乐际14日在北京集体会见出席2026年国际议员友好交流论坛的各国代表</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714622.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据广西壮族自治区纪委监委消息：广西壮族自治区南宁职业技术大学原党委书记黄明瑞涉嫌严重违纪违法，目前正接受广西壮族自治区纪委监委纪律审查和监察调查。" data-title="广西壮族自治区南宁职业技术大学原党委书记黄明瑞被查" data-date="10-14 19:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:55</span>
          <span class="news-item-title">广西壮族自治区南宁职业技术大学原党委书记黄明瑞被查</span>
          <span class="news-value-point">💡 中新网10月14日电 据广西壮族自治区纪委监委消息：广西壮族自治区南宁职业技术大学原党委书记黄明瑞涉嫌严重违纪违法，目前正接受广西壮族自治区纪委…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714621.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据上海市纪委监委消息：日前，上海市纪委监委对上海建工集团股份有限公司原副总裁张惠忠严重违纪违法问题进行了立案审查调查。" data-title="上海建工集团股份有限公司原副总裁张惠忠被“双开”" data-date="10-14 19:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:53</span>
          <span class="news-item-title">上海建工集团股份有限公司原副总裁张惠忠被“双开”</span>
          <span class="news-value-point">💡 中新网10月14日电 据上海市纪委监委消息：日前，上海市纪委监委对上海建工集团股份有限公司原副总裁张惠忠严重违纪违法问题进行了立案审查调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714626.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="哥伦比亚驻以色列大使馆14日在耶路撒冷举行新馆开馆仪式。" data-title="哥伦比亚在耶路撒冷设立驻以色列大使馆" data-date="10-14 19:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:52</span>
          <span class="news-item-title">哥伦比亚在耶路撒冷设立驻以色列大使馆</span>
          <span class="news-value-point">💡 哥伦比亚驻以色列大使馆14日在耶路撒冷举行新馆开馆仪式</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714620.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据江西省纪委监委消息：经中共江西省委批准，江西省纪委监委对中共江西省第十五届委员会委员、南昌市政协原党组书记、主席肖玉文严重违纪违法问题进行了立案审查调查。" data-title="江西省南昌市政协原党组书记、主席肖玉文被“双开”" data-date="10-14 19:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:51</span>
          <span class="news-item-title">江西省南昌市政协原党组书记、主席肖玉文被“双开”</span>
          <span class="news-value-point">💡 中新网10月14日电 据江西省纪委监委消息：经中共江西省委批准，江西省纪委监委对中共江西省第十五届委员会委员、南昌市政协原党组书记、主席肖玉文严…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714616.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网成都10月14日电 (记者 张浪)四川省广安市纪委监委14日消息：日前，经广安市委批准，广安市纪委监委对华蓥市人大常委会原党组书记、主任刘光文严重违纪违法问题进行了立案审查调查。" data-title="四川省华蓥市人大常委会原党组书记、主任刘光文严重违纪违法被开除党籍" data-date="10-14 19:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:50</span>
          <span class="news-item-title">四川省华蓥市人大常委会原党组书记、主任刘光文严重违纪违法被开除党籍</span>
          <span class="news-value-point">💡 中新网成都10月14日电 (记者 张浪)四川省广安市纪委监委14日消息：日前，经广安市委批准，广安市纪委监委对华蓥市人大常委会原党组书记、主任刘…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714599.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网太原10月14日电 (杨杰英 裴囡囡)10月14日，“晋城好风光·青春向太行”晋城市文旅推介高校行暨校地合作系列活动在太原理工大学启动。晋城市委书记薛明耀，共青团山西省委书记吴兴，太原理工大学党委书记沈兴全，太原理工大学党委常委、副校长任喜莹，晋城市委常委、市委宣传部部长邓志蓉，晋城市委常委、市委秘书长高一钧，副市长黄登宇出席。" data-title="山西晋城邀青年学子赴太行之约 文旅推介高校行系列活动启动" data-date="10-14 19:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:45</span>
          <span class="news-item-title">山西晋城邀青年学子赴太行之约 文旅推介高校行系列活动启动</span>
          <span class="news-value-point">💡 中新网太原10月14日电 (杨杰英 裴囡囡)10月14日，“晋城好风光·青春向太行”晋城市文旅推介高校行暨校地合作系列活动在太原理工大学启动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714573.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月14日电 据印度媒体报道，10月14日，原计划从德国法兰克福飞往印度德里的印度航空AI2030号航班，在进入印度领空时发出了7500应答机代码，这是国际上用于表示劫机或非法干扰的标识。备降印度斋浦尔国际机场后，经过检查并认定威胁已解除后，再度起飞。" data-title="印度航空一飞机发出劫机警报，威胁解除后再度起飞" data-date="10-14 18:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 18:41</span>
          <span class="news-item-title">印度航空一飞机发出劫机警报，威胁解除后再度起飞</span>
          <span class="news-value-point">💡 中新网10月14日电 据印度媒体报道，10月14日，原计划从德国法兰克福飞往印度德里的印度航空AI2030号航班，在进入印度领空时发出了7500…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714568.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科10月14日电 俄罗斯外交部发言人扎哈罗娃14日表示，日本记者涉嫌在俄从事间谍活动被拘捕并非首例案件，日方以新闻工作为掩护从事情报活动是不可接受的。" data-title="俄外交部：日方在俄以记者身份从事情报活动并非孤例" data-date="10-14 18:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 18:40</span>
          <span class="news-item-title">俄外交部：日方在俄以记者身份从事情报活动并非孤例</span>
          <span class="news-value-point">💡 中新社莫斯科10月14日电 俄罗斯外交部发言人扎哈罗娃14日表示，日本记者涉嫌在俄从事间谍活动被拘捕并非首例案件，日方以新闻工作为掩护从事情报活…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/013/094.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，苹果公司今日推送 iOS 27.2 Beta 4 开发者预览版（24B5110a）操作系统，为 Siri AI 新增五种语言。本次更新后，Siri AI 将支持英语、法语、日语、韩语、葡萄牙语和西班牙语。苹果已在此前确认这些语言扩展支持，具体可用性仍取决于用户所在地区和设备。IT之家了解到，Siri AI 是苹果最新的人工智能助理，支持 Apple 智能的各种新本领，其调用方法和平时使用 Siri 一样，理解个人情境，执行 App 操作、感知屏幕、理解图像、以及调用广博的世界知识。除此之外还拥有全新的专属 App，具备可跨平台提供视觉智能、集成工具来写作和编辑功能。" data-title="苹果 iOS 27.2 Beta 4 系统 Siri AI 新增支持法语、日语、西班牙语等" data-date="10-14 20:53" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:53</span>
          <span class="news-item-title">苹果 iOS 27.2 Beta 4 系统 Siri AI 新增支持法语、日语、西班牙语等</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，苹果公司今日推送 iOS 27.2 Beta 4 开发者预览版（24B5110a）操作系统，为 Siri AI…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/analyzing-intels-emib-and-foveros-advanced-packaging-roadmaps-how-intel-plans-to-scale-chips-in-every-direction" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔是第一家在2017 – 2019年开始使用先进封装方法的大型芯片制造商。但英特尔的EMIB和Foveros技术如今在哪里，它们的发展方向又在哪里？" data-title="Analyzing Intel&#39;s EMIB and Foveros advanced packaging roadmaps" data-date="10-14 20:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 20:50</span>
          <span class="news-item-title">分析英特尔的EMIB和Foveros高级封装路线图</span>
          <span class="news-item-title-en">Analyzing Intel's EMIB and Foveros advanced packaging roadmaps</span>
          <span class="news-value-point">💡 英特尔是第一家在2017 – 2019年开始使用先进封装方法的大型芯片制造商</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/091.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，格芯（GlobalFoundries，GF）刚刚宣布，公司已被选定为美国纽约州马耳他市两座新半导体制造工厂的技术提供商和运营方。该项目是美日此前达成的 5,500 亿美元（现汇率约合 3.69 万亿元人民币）投资协议的一部分。除新工厂外，格芯还与美国商务部达成协议，重新调整其《芯片与科学法案》获得 9.55 亿美元资金，并为美国商务部分配约 4% 的格芯股权，使其在格芯的总持股比例升至约 7%。该项目由美国与日本之间的贸易和投资协议推动，日本将提供最高 210 亿美元（IT之家注：现汇率约合 1,408.06 亿元人民币）投资，用于扩大美国本土半导体制造能力。根据格芯公告，首期约 100 亿美元（现汇率约合 670.5 亿元人民币）投资将用于加快一座全新 3" data-title="格芯获选在纽约建设两座晶圆厂，与美国商务部达成协议调整 9.55 亿美元资助并为其额外分配约 4% 股权" data-date="10-14 20:48" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:48</span>
          <span class="news-item-title">格芯获选在纽约建设两座晶圆厂，与美国商务部达成协议调整 9.55 亿美元资助并为其额外分配约 4% 股权</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，格芯（GlobalFoundries，GF）刚刚宣布，公司已被选定为美国纽约州马耳他市两座新半导体制造工厂的技…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-will-reportedly-receive-its-first-euv-tool-from-asml-in-mid-2027-cutting-edge-scanner-could-sit-idle-for-some-time-as-experimental-facility-is-completed" target="_blank" rel="noopener" data-cat="keji" data-summary="埃隆·马斯克（ Elon Musk ）可能更喜欢FEL光源用于内部芯片生产，但Terafab将从ASML的成熟技术开始。" data-title="Elon Musk&#39;s Terafab will reportedly receive its first EUV tool from ASML in mid" data-date="10-14 20:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 20:30</span>
          <span class="news-item-title">据报道，埃隆·马斯克（ Elon Musk ）的Terafab将于今年中旬从ASML获得其首个EUV工具</span>
          <span class="news-item-title-en">Elon Musk's Terafab will reportedly receive its first EUV tool from ASML in mid</span>
          <span class="news-value-point">💡 埃隆·马斯克（ Elon Musk ）可能更喜欢FEL光源用于内部芯片生产，但Terafab将从ASML的成熟技术开始</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/086.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，在今天的维信诺 × iQOO × 清华大学屏幕技术沟通会上，iQOO 宣布，iQOO Neo12 新机拥有三大首发技术 + 七大争锋屏幕体验 + 2K 185Hz 超豪华游戏生态，并喊话“让 185Hz 进入 2K 时代”。据介绍，iQOO Neo12 手机将行业首发搭载 pTSF 技术的 2K 185Hz 超冠屏、行业首发“天空之镜”发光材料、行业首发 2K 185Hz 高性能驱动芯片。新机屏幕将拥有 2K 分辨率、185Hz 超高刷、2200nits 全屏峰值亮度、自研 XDR 动态范围增强、游戏眩光防护、圆偏振光显示 2.0、1nit 睡眠屏、iQOO 16 同款 Q-flex 操控技术、低功耗特性等。另外，iQOO Neo12 将行业首发 2K 18" data-title="iQOO Neo12 官宣首发 pTSF 技术超冠屏：“天空之镜”发光材料，号称让 185Hz 进入 2K 时代" data-date="10-14 20:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:28</span>
          <span class="news-item-title">iQOO Neo12 官宣首发 pTSF 技术超冠屏：“天空之镜”发光材料，号称让 185Hz 进入 2K 时代</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，在今天的维信诺 × iQOO × 清华大学屏幕技术沟通会上，iQOO 宣布，iQOO Neo12 新机拥有三大…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-intelligence-sharing-zelensky-uk.html" target="_blank" rel="noopener" data-cat="keji" data-summary="乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾表示，华盛顿仍在“分享情报”。" data-title="Zelensky to Visit U.K. as Ukraine Presses Allies on Intelligence Sharing" data-date="10-14 20:15" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 20:15</span>
          <span class="news-item-title">泽伦斯基将访问英国，乌克兰向盟友施压，要求分享情报</span>
          <span class="news-item-title-en">Zelensky to Visit U.K. as Ukraine Presses Allies on Intelligence Sharing</span>
          <span class="news-value-point">💡 乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/qualcomm-wins-architecture-breach-verdict-against-arm-but-gets-just-usd2-judge-could-still-suspend-royalty-fees-for-five-years" target="_blank" rel="noopener" data-cat="keji" data-summary="联邦陪审团在特定问题上与Arm站在一起，在其他案件中则支持高通。这场法律斗争将持续下去。" data-title="Qualcomm wins architecture breach verdict against Arm but gets just $2" data-date="10-14 20:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 20:10</span>
          <span class="news-item-title">高通赢得针对Arm的架构违规裁决，但仅获得$ 2</span>
          <span class="news-item-title-en">Qualcomm wins architecture breach verdict against Arm but gets just $2</span>
          <span class="news-value-point">💡 联邦陪审团在特定问题上与Arm站在一起，在其他案件中则支持高通</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-engineer-arrested-for-allegedly-planting-usd14-recording-device-in-company-office-cheap-microcontroller-was-meant-to-secretly-capture-sensitive-communications-about-the-companys-super-intelligence-technology" target="_blank" rel="noopener" data-cat="keji" data-summary="一名OpenAI工程师被指控使用或试图使用电子、机械或其他设备来拦截口头通信，并面临最高五年的监禁和25万美元的罚款。" data-title="Saudi OpenAI engineer arrested for allegedly planting $14 recording device in company office" data-date="10-14 19:48" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 19:48</span>
          <span class="news-item-title">沙特OpenAI工程师因涉嫌在公司办公室种植$ 14录音设备而被捕</span>
          <span class="news-item-title-en">Saudi OpenAI engineer arrested for allegedly planting $14 recording device in company office</span>
          <span class="news-value-point">💡 一名OpenAI工程师被指控使用或试图使用电子、机械或其他设备来拦截口头通信，并面临最高五年的监禁和25万美元的罚款</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/the-imf-highlights-how-a-financial-wipeout-in-the-ai-sector-could-become-a-global-contagion-agency-report-shines-light-on-circular-economics-and-leveraged-loans" target="_blank" rel="noopener" data-cat="keji" data-summary="国际货币基金组织（ IMF ）发布了一份报告，研究如果该行业未能实现其承诺的利润，全球人工智能建设的融资将如何导致疫情蔓延。" data-title="AI sector wipeout risks global financial contagion, IMF report warns" data-date="10-14 19:35" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 19:35</span>
          <span class="news-item-title">国际货币基金组织报告警告称，人工智能行业面临全球金融蔓延的风险</span>
          <span class="news-item-title-en">AI sector wipeout risks global financial contagion, IMF report warns</span>
          <span class="news-value-point">💡 国际货币基金组织（ IMF ）发布了一份报告，研究如果该行业未能实现其承诺的利润，全球人工智能建设的融资将如何导致疫情蔓延</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-researchers-turn-idle-macs-into-a-virtual-gpu-cloud-with-minions-researchers-say-the-distributed-scheme-could-scale-globally-and-support-model-training" target="_blank" rel="noopener" data-cat="keji" data-summary="苹果研究人员描述了Minions ，这是一个内部系统，在GPU稀缺时在闲置的Apple Silicon Mac上运行AI推理作业。" data-title="Apple researchers turn idle Macs into a virtual GPU cloud with ‘Minions’" data-date="10-14 19:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 19:15</span>
          <span class="news-item-title">苹果研究人员将闲置的Mac变成带有“小小兵”的虚拟GPU云</span>
          <span class="news-item-title-en">Apple researchers turn idle Macs into a virtual GPU cloud with ‘Minions’</span>
          <span class="news-value-point">💡 苹果研究人员描述了Minions ，这是一个内部系统，在GPU稀缺时在闲置的Apple Silicon Mac上运行AI推理作业</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503294.html" target="_blank" rel="noopener" data-cat="keji" data-summary="“具身进实景，劳动最光荣”" data-title="抢先盘点2026全球开发者先锋大会暨国际具身智能技能大赛十大亮点！" data-date="10-14 18:41" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 18:41</span>
          <span class="news-item-title">抢先盘点2026全球开发者先锋大会暨国际具身智能技能大赛十大亮点！</span>
          <span class="news-value-point">💡 “具身进实景，劳动最光荣”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503244.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这妥妥是个物理版Agent啊！" data-title="阶跃终端首款“Agent手机”STEPX Neo正式发布，创客先行" data-date="10-14 16:01" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 16:01</span>
          <span class="news-item-title">阶跃终端首款“Agent手机”STEPX Neo正式发布，创客先行</span>
          <span class="news-value-point">💡 这妥妥是个物理版Agent啊</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/861.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，OSAT 龙头日月光半导体 (ASE) 昨日宣布推出基于 PowerSiP 平台的 3D 系统级封装解决方案。这一方案可实现 VRM（电压调节模块）的垂直整合，大幅缩短电流传输路径，降低超半数寄生布线损耗。日月光表示，先进的高性能 AI SoC 功耗已突破 1000W，这意味着需要 1V 以下电压传输超 1000A 的峰值电流，传统的横向架构在电力通过 PCB、封装基板、互连结构到达处理器的过程中可能产生严重的布线损耗。该企业的 PowerSiP 垂直整合工具箱包括夹在无芯基板之间的双面连接电容、具备外露端子的电容阵列模块、4:1 高纵横比铜柱整合技术、单 / 双面模塑高密度主 / 被动元件整合技术。这些技术可解决在空间受限的计算托盘中将电压调节模块配置于" data-title="日月光推出 3D 垂直整合 PowerSiP 解决方案，可减半寄生布线损耗" data-date="10-14 14:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 14:46</span>
          <span class="news-item-title">日月光推出 3D 垂直整合 PowerSiP 解决方案，可减半寄生布线损耗</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，OSAT 龙头日月光半导体 (ASE) 昨日宣布推出基于 PowerSiP 平台的 3D 系统级封装解决方案</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503201.html" target="_blank" rel="noopener" data-cat="keji" data-summary="2026年10月13日，大模型原生AI终端品牌STEPX（阶跃终端）旗下首款大模型原生智能体手机STEPX Neo正式发布" data-title="STEPX首款大模型原生智能体手机STEPX Neo正式发布" data-date="10-14 14:45" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-14 14:45</span>
          <span class="news-item-title">STEPX首款大模型原生智能体手机STEPX Neo正式发布</span>
          <span class="news-value-point">💡 2026年10月13日，大模型原生AI终端品牌STEPX（阶跃终端）旗下首款大模型原生智能体手机STEPX Neo正式发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714404.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="近日，交通运输部办公厅印发了《水运领域人工智能应用场景指引》(交办水〔2026〕63号，以下简称《指引》)。为便于各方更好地理解相关内容，切实做好贯彻落实工作，现解读如下：" data-title="《水运领域人工智能应用场景指引》解读" data-date="10-14 14:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 14:42</span>
          <span class="news-item-title">《水运领域人工智能应用场景指引》解读</span>
          <span class="news-value-point">💡 近日，交通运输部办公厅印发了《水运领域人工智能应用场景指引》(交办水〔2026〕63号，以下简称《指引》)</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/news/articles/c83vq9vpwwr1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力。" data-title="Burnham had two hospitality dinners with Man City chairman, deleted records show" data-date="10-14 20:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 20:47</span>
          <span class="news-item-title">伯纳姆与曼城主席共进了两顿招待晚餐，删除了记录显示</span>
          <span class="news-item-title-en">Burnham had two hospitality dinners with Man City chairman, deleted records show</span>
          <span class="news-value-point">💡 自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckwy4nj4842qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="延长三周的休息时间可能比英超联赛中任何其他球队都更能让切尔西受益。" data-title="Did Chelsea benefit most from extended international break?" data-date="10-14 18:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 18:43</span>
          <span class="news-item-title">切尔西是否从延长的国际休息中获益最多？</span>
          <span class="news-item-title-en">Did Chelsea benefit most from extended international break?</span>
          <span class="news-value-point">💡 延长三周的休息时间可能比英超联赛中任何其他球队都更能让切尔西受益</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx054n684g7do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="由于别墅公园的北展台目前因建筑工程而关闭，容量减少是否会影响阿斯顿维拉的表现？" data-title="&#39;No excuses&#39; - but is Villa&#39;s stadium rebuild affecting team?" data-date="10-14 13:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 13:41</span>
          <span class="news-item-title">“没有借口” -但维拉的体育场重建是否会影响球队？</span>
          <span class="news-item-title-en">'No excuses' - but is Villa's stadium rebuild affecting team?</span>
          <span class="news-value-point">💡 由于别墅公园的北展台目前因建筑工程而关闭，容量减少是否会影响阿斯顿维拉的表现</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck9qzwp9ejgro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在上个月被排除在托特纳姆热刺的英超球队之外之后，理查利森被留给了21岁以下球队。" data-title="Goal crisis &amp; in drop zone - so why is Spurs&#39; £60m striker stuck in U21s?" data-date="10-14 04:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 04:39</span>
          <span class="news-item-title">进球危机和落后区-那么为什么马刺队的£ 6000万前锋被困在U21中？</span>
          <span class="news-item-title-en">Goal crisis & in drop zone - so why is Spurs' £60m striker stuck in U21s?</span>
          <span class="news-value-point">💡 在上个月被排除在托特纳姆热刺的英超球队之外之后，理查利森被留给了21岁以下球队</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/13/why-most-manchester-city-fans-stand-by-their-club" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安德鲁·伯顿（ Andrew Burton ）怀疑，如果其他球队取得了类似的成功，球迷们也会原谅他们的主人瑞·肖恩·英格尔（ Re Sean Ingle ）的文章（一些曼城球迷是如何成为一个民族国家政权的积极捍卫者的？ ， 10月5日） ，我暂停" data-title="Why most Manchester City fans stand by their club | Letters" data-date="10-14 00:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-14 00:50</span>
          <span class="news-item-title">为什么大多数曼城球迷都支持他们的俱乐部|来信</span>
          <span class="news-item-title-en">Why most Manchester City fans stand by their club | Letters</span>
          <span class="news-value-point">💡 安德鲁·伯顿（ Andrew Burton ）怀疑，如果其他球队取得了类似的成功，球迷们也会原谅他们的主人瑞·肖恩·英格尔（ Re Sean I…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjkge245n0gzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰足球独立监管机构负责人表示，如果他遇到对曼城未来的任何政治干预，他将辞职。" data-title="Regulator would quit over Man City interference" data-date="10-14 00:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 00:00</span>
          <span class="news-item-title">监管机构将因曼城的干扰而退出</span>
          <span class="news-item-title-en">Regulator would quit over Man City interference</span>
          <span class="news-value-point">💡 英格兰足球独立监管机构负责人表示，如果他遇到对曼城未来的任何政治干预，他将辞职</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckn9r1ygv81wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="主教练恩佐·马雷斯卡（ Enzo Maresca ）在曼城在利物浦获胜后对曼城庆祝活动的批评做出了回应，他说： “你想让我们做什么？”" data-title="&#39;Criticised for what?&#39; - Maresca defends celebrations" data-date="10-13 21:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-13 21:04</span>
          <span class="news-item-title">“批评什么？” - Maresca为庆祝活动辩护</span>
          <span class="news-item-title-en">'Criticised for what?' - Maresca defends celebrations</span>
          <span class="news-value-point">💡 主教练恩佐·马雷斯卡（ Enzo Maresca ）在曼城在利物浦获胜后对曼城庆祝活动的批评做出了回应，他说： “你想让我们做什么</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/013/093.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，在今天的维信诺 × iQOO × 清华大学屏幕技术沟通会上，iQOO 产品副总裁罗峰现场宣布，iQOO Neo12“十月底见”（PPT 显示十月见）。据介绍，iQOO Neo12 手机将行业首发搭载 pTSF 技术的 2K 185Hz 超冠屏、行业首发“天空之镜”发光材料、行业首发 2K 185Hz 高性能驱动芯片。另外，新机将行业首发 2K 185FPS 超分超帧并发、行业首批适配原生 2K 超高清游戏、适配超 50 款原生 185 帧游戏等。新机将在本月发布。IT之家整理 iQOO Neo12 手机已公布 / 曝光配置如下：性能：第五代骁龙 8 至尊版处理器 | 自研电竞芯片 Q3 | 全新一代 Monster 超核引擎散热：冰穹风冷散热系统（主动散热风" data-title="iQOO Neo12 手机官宣“十月底见”：pTSF 技术 2K 185Hz 超冠屏、第五代骁龙 8 至尊版芯片" data-date="10-14 20:51" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:51</span>
          <span class="news-item-title">iQOO Neo12 手机官宣“十月底见”：pTSF 技术 2K 185Hz 超冠屏、第五代骁龙 8 至尊版芯片</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，在今天的维信诺 × iQOO × 清华大学屏幕技术沟通会上，iQOO 产品副总裁罗峰现场宣布，iQOO Neo…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/089.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，在今晚举行的发布会上，奇瑞捷途全新旅行者 7 上市，共提供 8 款车型，提供 1.5T 汽油、2.0T 汽油以及 1.5T 插混三种动力，超级焕新价 12.59 万元起。1.5TD 两驱探索：上市指导价 13.99 万元，超级焕新价 12.59 万元1.5TD 两驱探索 +：上市指导价 14.99 万元，超级焕新价 13.59 万元2.0TD XWD 四驱发现：上市指导价 15.99 万元，超级焕新价 14.59 万元2.0TD XWD 四驱穿越：上市指导价 16.99 万元，超级焕新价 15.59 万元2.0TD XWD 四驱征服：上市指导价 17.99 万元，超级焕新价 16.59 万元C-DM 两驱 Pro：上市指导价 15.29 万元，超级焕新价 1" data-title="奇瑞捷途全新旅行者 7 上市：燃油 / 插混版可选，超级焕新价 12.59 万元起" data-date="10-14 20:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:43</span>
          <span class="news-item-title">奇瑞捷途全新旅行者 7 上市：燃油 / 插混版可选，超级焕新价 12.59 万元起</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，在今晚举行的发布会上，奇瑞捷途全新旅行者 7 上市，共提供 8 款车型，提供 1.5T 汽油、2.0T 汽油以…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/088.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="海尔 77E 洗烘套装（云溪 4.0 顶配版）定价 9998 元，今日官方旗舰店 11.11 五折仅需 4999 元即可入手。下单前需咨询客服“是 4999 元吗”，客服可能会让下单待支付（选择微信支付不付款即可），然后把订单发给客服，客服登记后到货返差价。京东海尔 77E 洗烘套装云溪 4.0 顶配版返差价后 4999 元领 500 元券京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。官方对比：产品参数京东海尔 77E 洗烘套装云溪 4.0 顶配版返差价后 4999 元领 500 元券" data-title="半价 4999 元：海尔云溪 4.0 顶配版 77E 洗烘套装 11.11 官方直降" data-date="10-14 20:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:33</span>
          <span class="news-item-title">半价 4999 元：海尔云溪 4.0 顶配版 77E 洗烘套装 11.11 官方直降</span>
          <span class="news-value-point">💡 海尔 77E 洗烘套装（云溪 4.0 顶配版）定价 9998 元，今日官方旗舰店 11.11 五折仅需 4999 元即可入手</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/085.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，世嘉《全面战争：幕府将军 2》完全版于 10 月 13 日正式发售。目前在 Steam 上，完全版国区价格为 198 元，原版玩家可享 75% 折扣升级（仅限发售后的 30 天内有效）。本作以细致刻画的乱世日本为舞台，时间跨越源平合战、战国时代直至戊辰战争。据 Steam 商店页面信息，完全版收录游戏本体及所有 DLC，包括《武家之殇》与《武家崛起》两大战役，并带来全面提升的画质、光影及材质，1440p 及 4K 分辨率下的 UI 缩放，现代化操作，全新中文 / 日文语音及文本本地化，50 余种全新可玩子阵营，以及 64 位升级等内容。然而上线不足一天，该版本已遭遇大量差评。截至发稿，Steam 页面显示评价为“差评如潮”，在约 1900 篇用户评测中好评率" data-title="差评如潮：世嘉《全面战争: 幕府将军 2》完全版发售，Steam 国区 198 元" data-date="10-14 20:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 20:26</span>
          <span class="news-item-title">差评如潮：世嘉《全面战争: 幕府将军 2》完全版发售，Steam 国区 198 元</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，世嘉《全面战争：幕府将军 2》完全版于 10 月 13 日正式发售</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714623.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南京10月14日电 (记者 徐珊珊)10月14日，参加2026年“一带一路”记者组织论坛暨主题采风活动的中外记者走进南京云锦博物馆，了解非物质文化遗产南京云锦织造技艺。" data-title="外媒记者走进南京云锦博物馆 感受“寸锦寸金”里的文明互鉴" data-date="10-14 19:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:53</span>
          <span class="news-item-title">外媒记者走进南京云锦博物馆 感受“寸锦寸金”里的文明互鉴</span>
          <span class="news-value-point">💡 中新网南京10月14日电 (记者 徐珊珊)10月14日，参加2026年“一带一路”记者组织论坛暨主题采风活动的中外记者走进南京云锦博物馆，了解非…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714613.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网西宁10月14日电 (记者 潘雨洁)14日，记者从青海湖国家级自然保护区管理局获悉，该局工作人员于13日在青海湖鸟岛湿地内发现一只国家二级重点保护野生动物红胸黑雁。" data-title="红胸黑雁现身青海湖国家级自然保护区" data-date="10-14 19:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:50</span>
          <span class="news-item-title">红胸黑雁现身青海湖国家级自然保护区</span>
          <span class="news-value-point">💡 中新网西宁10月14日电 (记者 潘雨洁)14日，记者从青海湖国家级自然保护区管理局获悉，该局工作人员于13日在青海湖鸟岛湿地内发现一只国家二级…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714600.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网云南怒江10月14日电题：独龙江“生命线”畅通背后的朝夕守护" data-title="独龙江“生命线”畅通背后的朝夕守护" data-date="10-14 19:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:47</span>
          <span class="news-item-title">独龙江“生命线”畅通背后的朝夕守护</span>
          <span class="news-value-point">💡 中新网云南怒江10月14日电题：独龙江“生命线”畅通背后的朝夕守护</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714595.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆10月14日电 (罗永皓)“世界上有两个桃花源，一个在您的心中，一个在重庆酉阳。”这句文化IP，让地处武陵山区腹地的小城被越来越多的人们记住。" data-title="重庆酉阳“十五五”：山水之间兴文旅 桃花源里谋“城”长" data-date="10-14 19:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:47</span>
          <span class="news-item-title">重庆酉阳“十五五”：山水之间兴文旅 桃花源里谋“城”长</span>
          <span class="news-value-point">💡 中新网重庆10月14日电 (罗永皓)“世界上有两个桃花源，一个在您的心中，一个在重庆酉阳</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714594.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨10月14日电 (贡嘎来松)近日，“拉萨粮仓”西藏林周县迎来丰收时节。万亩高标准农田如金色绸缎铺展大地，沉甸甸的青稞穗在微风中摇曳，大型收割机在田间穿梭作业，蓝天白云下，一幅壮美的高原秋收画卷徐徐展开。" data-title="农民的“高标田”，就是纪委的“责任田”——拉萨市纪检监察机关以精准监督护航高标准农田建设" data-date="10-14 19:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:44</span>
          <span class="news-item-title">农民的“高标田”，就是纪委的“责任田”——拉萨市纪检监察机关以精准监督护航高标准农田建设</span>
          <span class="news-value-point">💡 中新网拉萨10月14日电 (贡嘎来松)近日，“拉萨粮仓”西藏林周县迎来丰收时节</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714592.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月14日电 (记者 陈溯)记者14日从中国气象局获悉，影响中国的冷空气活动逐渐频繁，未来十天，将先后有两股冷空气影响中国。" data-title="两股冷空气将接连影响中国 雨雪大风降温齐聚" data-date="10-14 19:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:44</span>
          <span class="news-item-title">两股冷空气将接连影响中国 雨雪大风降温齐聚</span>
          <span class="news-value-point">💡 中新社北京10月14日电 (记者 陈溯)记者14日从中国气象局获悉，影响中国的冷空气活动逐渐频繁，未来十天，将先后有两股冷空气影响中国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714611.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="最近，一位韩国博主的延边旅行视频在网络走红。" data-title="韩国博主在延边“破大防”？" data-date="10-14 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 19:34</span>
          <span class="news-item-title">韩国博主在延边“破大防”？</span>
          <span class="news-value-point">💡 最近，一位韩国博主的延边旅行视频在网络走红</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/offset-extortionate-memory-pricing-with-32gb-of-ddr5-6000-ram-for-usd151-with-this-9800x3d-bundle-combo-also-features-an-x870e-mobo-aio-cooler-onimusha-game-and-a-2tb-ssd" target="_blank" rel="noopener" data-cat="zonghe" data-summary="通过Newegg的组合优惠抵消高昂的内存和存储价格。" data-title="Offset extortionate memory pricing with 32GB of DDR5-6000 RAM for $151 with this 9800X3D bundle" data-date="10-14 19:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 19:20</span>
          <span class="news-item-title">借助这款9800X3D捆绑包， 32GB DDR5-6000内存，以151 $的价格抵消过高的内存定价</span>
          <span class="news-item-title-en">Offset extortionate memory pricing with 32GB of DDR5-6000 RAM for $151 with this 9800X3D bundle</span>
          <span class="news-value-point">💡 通过Newegg的组合优惠抵消高昂的内存和存储价格</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/scimplify-raises-25m-to-challenge-chinas-grip-on-critical-materials-with-ai/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Scimplify的年化收入运行率增加了两倍，达到2亿美元，因为它着眼于美国的扩张。" data-title="Scimplify raises $25M to challenge China’s grip on critical materials with AI" data-date="10-14 19:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 19:00</span>
          <span class="news-item-title">Scimplify筹集了2500万美元，通过人工智能挑战中国对关键材料的控制</span>
          <span class="news-item-title-en">Scimplify raises $25M to challenge China’s grip on critical materials with AI</span>
          <span class="news-value-point">💡 Scimplify的年化收入运行率增加了两倍，达到2亿美元，因为它着眼于美国的扩张</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1010694/tesla-roadster-reveal-vaporware-spacex-elon-musk" target="_blank" rel="noopener" data-cat="zonghe" data-summary="对于一辆应该是有史以来制造最快的汽车之一，新的特斯拉Roadster当然花了很长时间才来到这里。自从埃隆·马斯克（ Elon Musk ）出人意料地宣布计划建造下一代敞篷跑车以来，将近十年了。" data-title="The Tesla Roadster could have stayed vaporware" data-date="10-14 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-14 19:00</span>
          <span class="news-item-title">特斯拉敞篷跑车本来可以保持蒸汽器</span>
          <span class="news-item-title-en">The Tesla Roadster could have stayed vaporware</span>
          <span class="news-value-point">💡 对于一辆应该是有史以来制造最快的汽车之一，新的特斯拉Roadster当然花了很长时间才来到这里</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1010906/fairphone-fairbuds-2-price-release-audio-repairability" target="_blank" rel="noopener" data-cat="zonghe" data-summary="可维修、合乎道德的手机品牌Fairphone发布了第二副耳机。Fairbuds 2与第一代一样可维修，但音质得到改善，电池续航时间几乎延长了一倍。Fairbuds 2现已在英国和" data-title="Fairphone’s latest repairable earbuds are smaller, lighter, and longer" data-date="10-14 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-14 19:00</span>
          <span class="news-item-title">Fairphone最新的可维修耳机更小、更轻、更长</span>
          <span class="news-item-title-en">Fairphone’s latest repairable earbuds are smaller, lighter, and longer</span>
          <span class="news-value-point">💡 可维修、合乎道德的手机品牌Fairphone发布了第二副耳机</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-14 20:58（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
