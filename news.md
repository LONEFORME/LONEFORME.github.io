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
      <span>2026-11-14 03:54 抓取更新</span>
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
        <span class="channel-count">12</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">8</span>
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
  <div class="ov-item"><span class="ov-num">50</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×11 · The Verge×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/13/books/review/promise-me-america-joe-biden.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位前总统的新回忆录大肆宣扬他的成就，同时为他竞选连任的决定以及他对以色列在加沙的战争的支持进行辩护。" data-title="Book Review: ‘Promise Me, America,’ by Joe Biden" data-date="11-14 02:55" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-14 02:55</span>
      </div>
      <h2 class="hero-featured-title">书评：《向我承诺，美国》，作者：乔·拜登</h2>
      <div class="hero-featured-title-en">Book Review: ‘Promise Me, America,’ by Joe Biden</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/13/business/jensen-huang-nvidia-wall-street.html" target="_blank" rel="noopener" data-cat="keji" data-summary="被罢免的英伟达首席执行官是一位出色的交易撮合者，他领导了价值万亿美元的人工智能的建设。" data-title="Wall Street Loses a Powerful Dealmaker After Nvidia’s CEO Is Ousted" data-date="11-14 03:52" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Wall Street Loses a Powerful Dealmaker After Nvidia’s CEO Is Ousted</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cmd61qne8352o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺在解释他为何离开美国去执教曼联时泪流满面。" data-title="Tearful Pochettino on &#39;difficult&#39; decision to leave USA for Man Utd" data-date="11-13 23:28" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Tearful Pochettino on 'difficult' decision to leave USA for Man Utd</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1033046/playstation-xbox-gift-card-gta-vi-6-preorder-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="备受期待的《GTA VI》即将于下周五（11月19日）正式发布。虽然游戏本身的折扣在一段时间内会很少见，但有一个巧妙的变通方法可以让您在购买数字版时省下几美元。我们找到了折扣" data-title="Here’s how you can save on your GTA VI preorder ahead of launch" data-date="11-14 03:14" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Here’s how you can save on your GTA VI preorder ahead of launch</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/books/review/promise-me-america-joe-biden.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位前总统的新回忆录大肆宣扬他的成就，同时为他竞选连任的决定以及他对以色列在加沙的战争的支持进行辩护。" data-title="Book Review: ‘Promise Me, America,’ by Joe Biden" data-date="11-14 02:55" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 02:55</span>
          <span class="news-item-title">书评：《向我承诺，美国》，作者：乔·拜登</span>
          <span class="news-item-title-en">Book Review: ‘Promise Me, America,’ by Joe Biden</span>
          <span class="news-value-point">💡 这位前总统的新回忆录大肆宣扬他的成就，同时为他竞选连任的决定以及他对以色列在加沙的战争的支持进行辩护</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731867.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷11月13日电(李映民 王茜 梁峻祥)为期一个月的泰国湄南河灯光节13日晚拉开帷幕。活动以“想象之光”为主题，通过灯光、色彩、音乐及多媒体技术，将湄南河两岸历史地标和文化景观装点成光影舞台。" data-title="湄南河灯光节展现泰国历史文化魅力" data-date="11-13 23:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 23:19</span>
          <span class="news-item-title">湄南河灯光节展现泰国历史文化魅力</span>
          <span class="news-value-point">💡 中新社曼谷11月13日电(李映民 王茜 梁峻祥)为期一个月的泰国湄南河灯光节13日晚拉开帷幕</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/us/politics/scott-colom-mississippi-democrat-defied-odds.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在科洛姆先生的参议院竞选活动的大部分时间里，很少有人对他给予太多关注。然后，他击败了共和党的现任议员。" data-title="Even Scott Colom’s Backers Were Skeptical. Here’s How He Won in Mississippi." data-date="11-13 23:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 23:01</span>
          <span class="news-item-title">就连斯科特·科洛姆的支持者也持怀疑态度。以下是他如何在密西西比州获胜的。</span>
          <span class="news-item-title-en">Even Scott Colom’s Backers Were Skeptical. Here’s How He Won in Mississippi.</span>
          <span class="news-value-point">💡 在科洛姆先生的参议院竞选活动的大部分时间里，很少有人对他给予太多关注</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731860.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月13日电 11月13日，中共中央政治局委员、外交部长王毅在北京同韩国外交部长赵显举行会谈。" data-title="王毅同韩国外长赵显会谈" data-date="11-13 22:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 22:55</span>
          <span class="news-item-title">王毅同韩国外长赵显会谈</span>
          <span class="news-value-point">💡 中新社北京11月13日电 11月13日，中共中央政治局委员、外交部长王毅在北京同韩国外交部长赵显举行会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731846.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科11月13日电 题：“乌克兰困局”能否迎来破局时刻？" data-title="（国际观察）“乌克兰困局”能否迎来破局时刻？" data-date="11-13 22:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 22:32</span>
          <span class="news-item-title">（国际观察）“乌克兰困局”能否迎来破局时刻？</span>
          <span class="news-value-point">💡 中新社莫斯科11月13日电 题：“乌克兰困局”能否迎来破局时刻</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731842.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月13日电 (燕新台)“我看《实业计划》这本书已经看了40年了，我还没有看完。”近日，孙中山外曾孙王祖耀在接受中新网“燕新台”工作室专访时说道。" data-title="孙中山外曾孙王祖耀：中国共产党把《实业计划》变成现实" data-date="11-13 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 22:03</span>
          <span class="news-item-title">孙中山外曾孙王祖耀：中国共产党把《实业计划》变成现实</span>
          <span class="news-value-point">💡 中新网11月13日电 (燕新台)“我看《实业计划》这本书已经看了40年了，我还没有看完</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731828.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月13日电 11月13日，中国国家副主席韩正在北京出席2026世界中文大会开幕式并致辞。" data-title="韩正出席2026世界中文大会开幕式并致辞" data-date="11-13 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 21:59</span>
          <span class="news-item-title">韩正出席2026世界中文大会开幕式并致辞</span>
          <span class="news-value-point">💡 中新社北京11月13日电 11月13日，中国国家副主席韩正在北京出席2026世界中文大会开幕式并致辞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731824.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月13日电 据辽宁省纪委监委消息：经辽宁省委批准，辽宁省纪委监委对辽宁省沈抚改革创新示范区原党工委委员、管委会副主任范静国严重违纪违法问题进行了立案审查调查。" data-title="辽宁省沈抚改革创新示范区原管委会副主任范静国被“双开”" data-date="11-13 21:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 21:48</span>
          <span class="news-item-title">辽宁省沈抚改革创新示范区原管委会副主任范静国被“双开”</span>
          <span class="news-value-point">💡 中新网11月13日电 据辽宁省纪委监委消息：经辽宁省委批准，辽宁省纪委监委对辽宁省沈抚改革创新示范区原党工委委员、管委会副主任范静国严重违纪违法…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731724.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社澳大利亚伍伦贡11月13日电(记者 薄雯雯)“达尔富拉姆事件”88周年纪念活动13日在澳大利亚伍伦贡市肯布拉港举行，纪念1938年当地码头工人为反对日本军国主义、声援中国抗战而发起的罢工行动。" data-title="“达尔富拉姆事件”88周年纪念活动在澳大利亚举行" data-date="11-13 21:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 21:40</span>
          <span class="news-item-title">“达尔富拉姆事件”88周年纪念活动在澳大利亚举行</span>
          <span class="news-value-point">💡 中新社澳大利亚伍伦贡11月13日电(记者 薄雯雯)“达尔富拉姆事件”88周年纪念活动13日在澳大利亚伍伦贡市肯布拉港举行，纪念1938年当地码头…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731715.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社柏林11月13日电 根据德国警方13日凌晨通报，德国东北部梅克伦堡-前波美拉尼亚州维斯马市一栋多户住宅楼12日晚发生火灾，造成2人死亡、14人受伤。" data-title="德国东北部一城市住宅楼发生火灾致2死14伤" data-date="11-13 21:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 21:38</span>
          <span class="news-item-title">德国东北部一城市住宅楼发生火灾致2死14伤</span>
          <span class="news-value-point">💡 中新社柏林11月13日电 根据德国警方13日凌晨通报，德国东北部梅克伦堡-前波美拉尼亚州维斯马市一栋多户住宅楼12日晚发生火灾，造成2人死亡、1…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社上海11月13日电 (记者 许婧)今年是孙中山先生诞辰160周年，上海近日举办系列活动，纪念缅怀这位革命先驱，传承中山精神。" data-title="上海举办系列活动纪念孙中山诞辰160周年" data-date="11-13 21:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 21:37</span>
          <span class="news-item-title">上海举办系列活动纪念孙中山诞辰160周年</span>
          <span class="news-value-point">💡 中新社上海11月13日电 (记者 许婧)今年是孙中山先生诞辰160周年，上海近日举办系列活动，纪念缅怀这位革命先驱，传承中山精神</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731807.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月13日电 (记者 阮煜琳)中国海警局13日发布消息，11月9日至13日，中国海警三都舰到马来西亚槟城开展港口访问，此次活动旨在进一步加深中马两国海警机构之间友好交流合作，提升海上执法合作水平，共同维护南海地区和平稳定。" data-title="中国海警三都舰结束对马来西亚槟城港口访问" data-date="11-13 21:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 21:34</span>
          <span class="news-item-title">中国海警三都舰结束对马来西亚槟城港口访问</span>
          <span class="news-value-point">💡 中新社北京11月13日电 (记者 阮煜琳)中国海警局13日发布消息，11月9日至13日，中国海警三都舰到马来西亚槟城开展港口访问，此次活动旨在进…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/business/jensen-huang-nvidia-wall-street.html" target="_blank" rel="noopener" data-cat="keji" data-summary="被罢免的英伟达首席执行官是一位出色的交易撮合者，他领导了价值万亿美元的人工智能的建设。" data-title="Wall Street Loses a Powerful Dealmaker After Nvidia’s CEO Is Ousted" data-date="11-14 03:52" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 03:52</span>
          <span class="news-item-title">英伟达首席执行官被罢免，华尔街失去一位强有力的交易撮合者</span>
          <span class="news-item-title-en">Wall Street Loses a Powerful Dealmaker After Nvidia’s CEO Is Ousted</span>
          <span class="news-value-point">💡 被罢免的英伟达首席执行官是一位出色的交易撮合者，他领导了价值万亿美元的人工智能的建设</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/technology/anthropic-ipo-spending-plans.html" target="_blank" rel="noopener" data-cat="keji" data-summary="随着公司处理员工股票报酬和人工智能成本的不断增加，其财务状况可能会变得不明朗。" data-title="Wall Street Braces for Anthropic’s Spending" data-date="11-14 02:52" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 02:52</span>
          <span class="news-item-title">华尔街为Anthropic的支出做好准备</span>
          <span class="news-item-title-en">Wall Street Braces for Anthropic’s Spending</span>
          <span class="news-value-point">💡 随着公司处理员工股票报酬和人工智能成本的不断增加，其财务状况可能会变得不明朗</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/" target="_blank" rel="noopener" data-cat="keji" data-summary="一项新研究表明，中国最先进的人工智能模型是在被禁用的英伟达芯片上训练的。" data-title="Export-banned Nvidia chips are behind China’s most powerful AI models — uh oh, Jensen!" data-date="11-14 02:40" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-14 02:40</span>
          <span class="news-item-title">被禁止出口的英伟达芯片是支撑中国最强大人工智能模型的基础——哎呀，Jensen！</span>
          <span class="news-item-title-en">Export-banned Nvidia chips are behind China’s most powerful AI models — uh oh, Jensen!</span>
          <span class="news-value-point">💡 一项新研究表明，中国最先进的人工智能模型是在被禁用的英伟达芯片上训练的</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1033051/nvidia-jensen-huang-chips-gpu-supply-chain-climate-pollution" target="_blank" rel="noopener" data-cat="keji" data-summary="在联合创始人黄仁勋的领导下，英伟达已成为人工智能繁荣的引擎，也是科技行业最大的环境负担之一。该公司备受追捧的芯片引发了新一波耗水耗化学品工厂的兴起，消耗了大量电力，" data-title="Jensen Huang was reckless with the environment, too" data-date="11-14 01:44" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 01:44</span>
          <span class="news-item-title">黄仁勋对环境也同样不以为然</span>
          <span class="news-item-title-en">Jensen Huang was reckless with the environment, too</span>
          <span class="news-value-point">💡 在联合创始人黄仁勋的领导下，英伟达已成为人工智能繁荣的引擎，也是科技行业最大的环境负担之一</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/technology/jensen-huang-silicon-valley-start-ups.html" target="_blank" rel="noopener" data-cat="keji" data-summary="黄先生大力支持初创企业，截至7月底，英伟达在229家私营公司中持有价值480亿美元的股份，其中包括OpenAI和Anthropic。" data-title="Jensen Huang’s Resignation From Nvidia Worries the A.I. Start" data-date="11-14 00:36" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 00:36</span>
          <span class="news-item-title">Jensen Huang从Nvidia辞职令人工智能初创企业感到担忧</span>
          <span class="news-item-title-en">Jensen Huang’s Resignation From Nvidia Worries the A.I. Start</span>
          <span class="news-value-point">💡 黄先生大力支持初创企业，截至7月底，英伟达在229家私营公司中持有价值480亿美元的股份，其中包括OpenAI和Anthropic</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/unannounced-intel-core-ultra-7-260k-cpu-surfaces-in-newegg-prebuilt-gaming-pcs-intel-doesnt-have-official-specs-list-available-for-exclusive-arrow-lake-chip" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管英特尔方面并未正式提及这款芯片，但神秘的英特尔酷睿Ultra 7 260K已在新蛋的一些预装游戏电脑中亮相。" data-title="Unannounced Intel Core Ultra 7 260K CPU surfaces in Newegg prebuilt gaming PCs" data-date="11-14 00:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 00:30</span>
          <span class="news-item-title">未发布英特尔酷睿Ultra 7 260K处理器出现在Newegg预组装游戏电脑中</span>
          <span class="news-item-title-en">Unannounced Intel Core Ultra 7 260K CPU surfaces in Newegg prebuilt gaming PCs</span>
          <span class="news-value-point">💡 尽管英特尔方面并未正式提及这款芯片，但神秘的英特尔酷睿Ultra 7 260K已在新蛋的一些预装游戏电脑中亮相</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/malaysia-and-singapore-step-up-nvidia-ai-chip-probes-as-charges-brought-against-chinese-national-over-917-smuggled-servers-firm-at-center-of-jensen-huang-controversy-announces-inventory-audit-to-account-for-all-restricted-gpus" target="_blank" rel="noopener" data-cat="keji" data-summary="马来西亚正在调查Nvidia人工智能硬件可能被再出口的情况，原因是人们担心有人规避美国对中国的限制，而新加坡则指控一名高管涉嫌购买917台人工智能服务器。" data-title="Malaysia and Singapore step up Nvidia AI chip probes amidst Jensen Huang controversy" data-date="11-14 00:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 00:15</span>
          <span class="news-item-title">在黄仁勋争议之际，马来西亚和新加坡加紧对英伟达AI芯片的调查</span>
          <span class="news-item-title-en">Malaysia and Singapore step up Nvidia AI chip probes amidst Jensen Huang controversy</span>
          <span class="news-value-point">💡 马来西亚正在调查Nvidia人工智能硬件可能被再出口的情况，原因是人们担心有人规避美国对中国的限制，而新加坡则指控一名高管涉嫌购买917台人工智…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/technology/anthropic-dario-amodei-ai-openai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司的首席执行官达里奥·阿莫代（Dario Amodei）公开对人工智能的危险表示担忧，并因此与同行结下了梁子。" data-title="Why Anthropic’s Dario Amodei Has Angered OpenAI and Other A.I. Peers" data-date="11-14 00:11" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 00:11</span>
          <span class="news-item-title">为什么Anthropic的Dario Amodei惹怒了OpenAI和其他人工智能同行？</span>
          <span class="news-item-title-en">Why Anthropic’s Dario Amodei Has Angered OpenAI and Other A.I. Peers</span>
          <span class="news-value-point">💡 该公司的首席执行官达里奥·阿莫代（Dario Amodei）公开对人工智能的危险表示担忧，并因此与同行结下了梁子</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/" target="_blank" rel="noopener" data-cat="keji" data-summary="ChatGPT钱包让AI代理能够代表用户购物和结账，该功能将首先有限度地向美国Pro版订阅用户推出。" data-title="ChatGPT’s new Wallet lets AI agents shop and check out for you" data-date="11-14 00:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-14 00:00</span>
          <span class="news-item-title">ChatGPT 的新钱包让 AI 代理为您购物和结账</span>
          <span class="news-item-title-en">ChatGPT’s new Wallet lets AI agents shop and check out for you</span>
          <span class="news-value-point">💡 ChatGPT钱包让AI代理能够代表用户购物和结账，该功能将首先有限度地向美国Pro版订阅用户推出</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/13/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响。" data-title="The unfolding Jensen Huang scandal: a timeline" data-date="11-13 23:58" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 23:58</span>
          <span class="news-item-title">正在发酵的黄仁勋丑闻：时间线</span>
          <span class="news-item-title-en">The unfolding Jensen Huang scandal: a timeline</span>
          <span class="news-value-point">💡 Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/994.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 13 日消息，OpenAI 今天（13 日）宣布推出支付功能 ChatGPT Wallet，让旗下 dot AI 智能体代替用户购物。ChatGPT Wallet 由 OpenAI 与美国运通、万事达卡和 Visa 合作开发，用户使用现有信用卡付款时，仍可享受原有的积分奖励和权益保障。符合条件的用户只需录入一次银行卡信息，随后便可让 dot 智能体帮忙寻找商品，每笔交易都需要通过安全验证才能完成。OpenAI 强调，dot 智能体不会接触用户的真实银行卡信息。支付网络会为每笔交易生成专用的支付令牌，其中包含限定用途的卡号、安全码和有效期，供智能体完成付款。当今，越来越多消费者开始尝试用个人 AI 智能体管理日程、预订旅行和处理其他日常事务，ChatGPT Wallet 在" data-title="让智能体帮你购物，OpenAI 推出支付功能 ChatGPT Wallet" data-date="11-13 23:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-13 23:49</span>
          <span class="news-item-title">让智能体帮你购物，OpenAI 推出支付功能 ChatGPT Wallet</span>
          <span class="news-value-point">💡 IT之家 11 月 13 日消息，OpenAI 今天（13 日）宣布推出支付功能 ChatGPT Wallet，让旗下 dot AI 智能体代替…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/993.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 13 日消息，华为麒麟官方公众号继续揭秘首款“逻辑折叠”技术 τ 芯片 —— 麒麟 9050 系列更多配置信息，新一代灵犀 CPU 详情已公开。据介绍，麒麟 9050 系列搭载新一代灵犀 CPU，支持 9 核 16 线程超线程技术，多核性能提升 23%、GPU 渲染性能提升 40%、NPU 性能提升 140%，配合鸿蒙应用并行化与智能调度，多任务更流畅。重载场景（应用启动、大文件加载、游戏运行）由 1 超大核 + 2 性能大核负责；多任务场景（UX 交互、悬浮窗、视频通话、分屏）由 4 能效大核负责；日常场景（浏览资讯、短视频）由 2 小核负责。此外，麒麟 9050 系列芯片还支持内存压缩加速器，压缩率提升 45%，可用内存平均增加 3GB，后台多任务会更从容；智能异构调" data-title="华为麒麟 9050 系列芯片新一代灵犀 CPU 详细信息公开：9 核 16 线程并行调度，支持内存压缩加速" data-date="11-13 23:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-13 23:47</span>
          <span class="news-item-title">华为麒麟 9050 系列芯片新一代灵犀 CPU 详细信息公开：9 核 16 线程并行调度，支持内存压缩加速</span>
          <span class="news-value-point">💡 IT之家 11 月 13 日消息，华为麒麟官方公众号继续揭秘首款“逻辑折叠”技术 τ 芯片 —— 麒麟 9050 系列更多配置信息，新一代灵犀 …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/broken-and-shattered-nvidia-ceo-jensen-huang-surrendered-during-resignation-meeting-report-claims-thousands-of-employees-rally-calling-for-reinstatement-on-internal-forum" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，在被迫离职后，黄仁勋自称为“一坨屎”，但员工仍然希望他回来。" data-title="‘Broken and shattered’ Nvidia CEO Jensen Huang surrendered during resignation meeting, report claims" data-date="11-13 21:16" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-13 21:16</span>
          <span class="news-item-title">据报道，英伟达首席执行官黄仁勋在辞职会上“心灰意冷、意志消沉”地投降了</span>
          <span class="news-item-title-en">‘Broken and shattered’ Nvidia CEO Jensen Huang surrendered during resignation meeting, report claims</span>
          <span class="news-value-point">💡 据报道，在被迫离职后，黄仁勋自称为“一坨屎”，但员工仍然希望他回来</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/13/israels-vcs-see-opportunity-for-challengers-in-nvidias-turmoil/" target="_blank" rel="noopener" data-cat="keji" data-summary="鉴于Nvidia在人工智能领域的强势地位及其在以色列的重要性，该国初创企业生态系统中的许多人对他的离职所带来的影响感到担忧。" data-title="Israel’s VCs see opportunity for challengers in Nvidia’s turmoil" data-date="11-13 20:52" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 20:52</span>
          <span class="news-item-title">以色列的风险投资机构认为，Nvidia的动荡为挑战者带来了机会</span>
          <span class="news-item-title-en">Israel’s VCs see opportunity for challengers in Nvidia’s turmoil</span>
          <span class="news-value-point">💡 鉴于Nvidia在人工智能领域的强势地位及其在以色列的重要性，该国初创企业生态系统中的许多人对他的离职所带来的影响感到担忧</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/walmart-has-slashed-usd730-off-this-monster-gaming-pc-with-rtx-5070-ti-also-features-a-24-core-intel-processor-32gb-ddr5-2tb-ssd" target="_blank" rel="noopener" data-cat="keji" data-summary="购买这款搭载英特尔酷睿Ultra 9 285和RTX 5070 Ti的CyberPowerPC，立省$730。" data-title="Walmart has slashed $730 off this monster gaming PC with RTX 5070 Ti" data-date="11-13 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-13 19:30</span>
          <span class="news-item-title">沃尔玛将这款搭载RTX 5070 Ti的超强游戏电脑降价730美元</span>
          <span class="news-item-title-en">Walmart has slashed $730 off this monster gaming PC with RTX 5070 Ti</span>
          <span class="news-value-point">💡 购买这款搭载英特尔酷睿Ultra 9 285和RTX 5070 Ti的CyberPowerPC，立省$730</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">8 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmd61qne8352o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺在解释他为何离开美国去执教曼联时泪流满面。" data-title="Tearful Pochettino on &#39;difficult&#39; decision to leave USA for Man Utd" data-date="11-13 23:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 23:28</span>
          <span class="news-item-title">波切蒂诺含泪谈及离开美国队执教曼联的“艰难”决定</span>
          <span class="news-item-title-en">Tearful Pochettino on 'difficult' decision to leave USA for Man Utd</span>
          <span class="news-value-point">💡 情绪激动的毛里西奥·波切蒂诺在解释他为何离开美国去执教曼联时泪流满面</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13611887/mauricio-pochettino-new-man-utd-head-coach-in-tears-as-he-labels-leaving-usmnt-toughest-decision-of-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会。" data-title="Tearful Pochettino admits he &#39;couldn&#39;t say no to Man Utd&#39;" data-date="11-13 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 23:00</span>
          <span class="news-item-title">泪流满面的波切蒂诺承认他“无法拒绝曼联”</span>
          <span class="news-item-title-en">Tearful Pochettino admits he 'couldn't say no to Man Utd'</span>
          <span class="news-value-point">💡 情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611887/mauricio-pochettino-new-man-utd-head-coach-in-tears-as-he-labels-leaving-usmnt-toughest-decision-of-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会。" data-title="Tearful Pochettino admits he &#39;couldn&#39;t say no to Man Utd&#39;" data-date="11-13 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 23:00</span>
          <span class="news-item-title">泪流满面的波切蒂诺承认他“无法拒绝曼联”</span>
          <span class="news-item-title-en">Tearful Pochettino admits he 'couldn't say no to Man Utd'</span>
          <span class="news-value-point">💡 情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13611928/mauricio-pochettino-left-in-tears-on-leaving-us-job-most-difficult-decision" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="新任曼联主帅毛里西奥·波切蒂诺在感谢美国足球联合会时情绪非常激动。" data-title="Pochettino left in tears on leaving US job - &#39;Most difficult decision&#39;" data-date="11-13 22:49" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 22:49</span>
          <span class="news-item-title">波切蒂诺泪洒离别之际，告别美国队主帅一职——“最艰难的决定”</span>
          <span class="news-item-title-en">Pochettino left in tears on leaving US job - 'Most difficult decision'</span>
          <span class="news-value-point">💡 新任曼联主帅毛里西奥·波切蒂诺在感谢美国足球联合会时情绪非常激动</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13611911/from-usa-to-manchester-utd-mauricio-pochettinos-hectic-schedule-explained" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的罗布·多塞特解释了为什么曼联新任主教练毛里西奥·波切蒂诺在接下来的几天里会非常忙碌。" data-title="The HECTIC schedule Pochettino will face ahead of new life at Man Utd!" data-date="11-13 21:48" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 21:48</span>
          <span class="news-item-title">波切蒂诺在曼联开启新生活前将面临的繁忙日程！</span>
          <span class="news-item-title-en">The HECTIC schedule Pochettino will face ahead of new life at Man Utd!</span>
          <span class="news-value-point">💡 天空体育的罗布·多塞特解释了为什么曼联新任主教练毛里西奥·波切蒂诺在接下来的几天里会非常忙碌</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm2kljzkw77ko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着毛里西奥·波切蒂诺即将成为曼联主帅，我们来分析一下他能否克服其他教练未能克服的战术障碍。" data-title="How Ferguson-inspired Pochettino can succeed where Carrick failed at Man Utd" data-date="11-13 20:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 20:09</span>
          <span class="news-item-title">波切蒂诺如何借鉴弗格森的经验，在曼联取得卡里克未能取得的成功</span>
          <span class="news-item-title-en">How Ferguson-inspired Pochettino can succeed where Carrick failed at Man Utd</span>
          <span class="news-value-point">💡 随着毛里西奥·波切蒂诺即将成为曼联主帅，我们来分析一下他能否克服其他教练未能克服的战术障碍</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610882/mauricio-pochettino-appointed-as-manchester-united-head-coach-after-michael-carricks-sacking-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在迈克尔·卡里克被解雇后，毛里西奥·波切蒂诺被任命为曼联的新任主教练。" data-title="Man Utd appoint Pochettino as head coach" data-date="11-13 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 20:00</span>
          <span class="news-item-title">曼联任命波切蒂诺为主教练</span>
          <span class="news-item-title-en">Man Utd appoint Pochettino as head coach</span>
          <span class="news-value-point">💡 在迈克尔·卡里克被解雇后，毛里西奥·波切蒂诺被任命为曼联的新任主教练</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm782d4pz9jyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联队长布鲁诺·费尔南德斯拒绝了俱乐部的第二份合同报价，他目前的合同将于本赛季末到期。" data-title="Fernandes rejects second Man Utd contract offer" data-date="11-13 17:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 17:55</span>
          <span class="news-item-title">费尔南德斯拒绝曼联的第二份合同报价</span>
          <span class="news-item-title-en">Fernandes rejects second Man Utd contract offer</span>
          <span class="news-value-point">💡 曼联队长布鲁诺·费尔南德斯拒绝了俱乐部的第二份合同报价，他目前的合同将于本赛季末到期</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1033046/playstation-xbox-gift-card-gta-vi-6-preorder-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="备受期待的《GTA VI》即将于下周五（11月19日）正式发布。虽然游戏本身的折扣在一段时间内会很少见，但有一个巧妙的变通方法可以让您在购买数字版时省下几美元。我们找到了折扣" data-title="Here’s how you can save on your GTA VI preorder ahead of launch" data-date="11-14 03:14" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 03:14</span>
          <span class="news-item-title">以下是您如何在《GTA VI》发售前节省预购费用的方法</span>
          <span class="news-item-title-en">Here’s how you can save on your GTA VI preorder ahead of launch</span>
          <span class="news-value-point">💡 备受期待的《GTA VI》即将于下周五（11月19日）正式发布</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/technology/microsoft-outage-what-to-know.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="该公司表示，在努力克服其电子邮件、消息和其他服务连续第二天出现的中断方面取得了“令人鼓舞”的进展。" data-title="Microsoft’s Global Outage and Fixes: What We Know" data-date="11-14 03:04" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 03:04</span>
          <span class="news-item-title">微软的全球性宕机及其解决方案：我们所了解的信息</span>
          <span class="news-item-title-en">Microsoft’s Global Outage and Fixes: What We Know</span>
          <span class="news-value-point">💡 该公司表示，在努力克服其电子邮件、消息和其他服务连续第二天出现的中断方面取得了“令人鼓舞”的进展</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/scotland-vs-north-macedonia/live/554098" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Robertson equals cap record as Scotland host North Macedonia LIVE!" data-title="Robertson equals cap record as Scotland host North Macedonia LIVE!" data-date="11-14 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 02:30</span>
          <span class="news-item-title">苏格兰主场迎战北马其顿时，罗伯逊将追平出场纪录！敬请观看直播！</span>
          <span class="news-item-title-en">Robertson equals cap record as Scotland host North Macedonia LIVE!</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/keyboards-and-keyboard-accessories-under-usd100-budget-friendly-gifts-for-keyboard-enthusiasts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="送给您身边键盘爱好者的最佳百元以下礼物——即使他们已经拥有了终极键盘。" data-title="Keyboards and keyboard accessories under $100 — budget-friendly gifts for keyboard enthusiasts" data-date="11-14 02:25" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 02:25</span>
          <span class="news-item-title">100 美元以下的键盘和键盘配件——适合键盘爱好者的经济实惠的礼物</span>
          <span class="news-item-title-en">Keyboards and keyboard accessories under $100 — budget-friendly gifts for keyboard enthusiasts</span>
          <span class="news-value-point">💡 送给您身边键盘爱好者的最佳百元以下礼物——即使他们已经拥有了终极键盘</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1033159/keychron-t1-he-trackball-wireless-mouse-adjustable" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Nape Pro是Keychron的首款轨迹球设备，于2026年CES上推出，采用纤薄紧凑的设计，可紧贴键盘放置。该公司的新款 T1 HE 则更像其他已经上市的轨迹球鼠标。" data-title="You can adjust the position of the trackball on Keychron’s new wireless mouse" data-date="11-14 02:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 02:10</span>
          <span class="news-item-title">您可以在 Keychron 的新款无线鼠标上调整轨迹球的位置</span>
          <span class="news-item-title-en">You can adjust the position of the trackball on Keychron’s new wireless mouse</span>
          <span class="news-value-point">💡 Nape Pro是Keychron的首款轨迹球设备，于2026年CES上推出，采用纤薄紧凑的设计，可紧贴键盘放置</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13612006/viddal-riley-determined-to-prove-himself-a-world-champion-in-waiting-in-european-title-fight-against-seydi-coupe" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果Viddal Riley能在周六的比赛中击败Seydi Coupe，卫冕欧洲冠军，他将踏上争夺次重量级世界冠军头衔的征程。" data-title="Riley determined to prove himself a world champion in waiting" data-date="11-14 01:53" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 01:53</span>
          <span class="news-item-title">Riley 决心证明自己是未来的世界冠军</span>
          <span class="news-item-title-en">Riley determined to prove himself a world champion in waiting</span>
          <span class="news-value-point">💡 如果Viddal Riley能在周六的比赛中击败Seydi Coupe，卫冕欧洲冠军，他将踏上争夺次重量级世界冠军头衔的征程</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1033026/camp-snap-retro-digital-video-campcorder-cs-8-micro-keychain" target="_blank" rel="noopener" data-cat="zonghe" data-summary="上周，Camp Snap推出了其无屏CS-8摄像机的迷你版，其尺寸是原版的一半，手柄更小，旨在让孩子们更容易握持。但事实证明，该公司并没有停止缩小其硬件的尺寸。" data-title="The smallest version of Camp Snap’s retro digital camcorder fits on your keychain" data-date="11-14 01:12" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 01:12</span>
          <span class="news-item-title">Camp Snap复古数码摄像机的最小版本可挂在钥匙链上</span>
          <span class="news-item-title-en">The smallest version of Camp Snap’s retro digital camcorder fits on your keychain</span>
          <span class="news-value-point">💡 上周，Camp Snap推出了其无屏CS-8摄像机的迷你版，其尺寸是原版的一半，手柄更小，旨在让孩子们更容易握持</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/10-great-pc-upgrades-for-under-usd100-spice-up-your-setup-for-less-with-these-gifts-and-impulse-purchases" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果您想以更便宜的价格升级电脑，以下是 10 款 100 美元以下的商品。" data-title="10 great PC upgrades for under $100" data-date="11-14 01:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 01:00</span>
          <span class="news-item-title">10款不到100美元的超值电脑升级产品</span>
          <span class="news-item-title-en">10 great PC upgrades for under $100</span>
          <span class="news-value-point">💡 如果您想以更便宜的价格升级电脑，以下是 10 款 100 美元以下的商品</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1033076/apple-tv-4k-youtube-error" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天收到全新Apple TV 4k的用户在打开YouTube应用后，立即看到了一些奇怪的错误消息。当首批设备到货时，该应用最初只显示一个带有二维码的黑屏，以及一条显示“YouT”的错误消息。" data-title="The new Apple TV has a YouTube problem" data-date="11-14 00:55" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 00:55</span>
          <span class="news-item-title">新款Apple TV存在YouTube问题</span>
          <span class="news-item-title-en">The new Apple TV has a YouTube problem</span>
          <span class="news-value-point">💡 今天收到全新Apple TV 4k的用户在打开YouTube应用后，立即看到了一些奇怪的错误消息</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-14/10731870.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网11月14日电 据中国地震台网微博消息，中国地震台网正式测定：11月14日00时17分在新疆阿克苏地区库车市(北纬42.22度，东经83.64度)发生5.0级地震，震源深度20千米。" data-title="新疆阿克苏地区库车市发生5.0级地震" data-date="11-14 00:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 00:34</span>
          <span class="news-item-title">新疆阿克苏地区库车市发生5.0级地震</span>
          <span class="news-value-point">💡 中新网11月14日电 据中国地震台网微博消息，中国地震台网正式测定：11月14日00时17分在新疆阿克苏地区库车市(北纬42.22度，东经83.…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1032862/microsoft-outlook-down-outage" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在经历了近两天的中断，影响到全球数百万用户之后，Microsoft Outlook 和 365 的服务正在恢复。周五上午，一些应用程序和功能仍处于运行受限状态，一些人（包括Verge的员工）" data-title="Microsoft’s massive Outlook outage might be over" data-date="11-14 00:17" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 00:17</span>
          <span class="news-item-title">微软的Outlook大规模宕机可能已经结束</span>
          <span class="news-item-title-en">Microsoft’s massive Outlook outage might be over</span>
          <span class="news-value-point">💡 在经历了近两天的中断，影响到全球数百万用户之后，Microsoft Outlook 和 365 的服务正在恢复</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/live-blog/12040/13611964/france-vs-south-africa-live-nations-championship-updates-latest-scores-team-news-commentary-from-stade-de-france" target="_blank" rel="noopener" data-cat="zonghe" data-summary="France vs South Africa LIVE! Injury-hit hosts face Springboks in blockbuster" data-title="France vs South Africa LIVE! Injury-hit hosts face Springboks in blockbuster" data-date="11-14 00:12" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 00:12</span>
          <span class="news-item-title">法国对阵南非直播！饱受伤病困扰的主队将在焦点大战中迎战春boks队</span>
          <span class="news-item-title-en">France vs South Africa LIVE! Injury-hit hosts face Springboks in blockbuster</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/popular-gaming-chair-and-desk-maker-secretlab-launches-dedicated-us-brick-and-mortar-locations-new-shop-in-la-spaces-in-best-buy" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Secretlab目前在百思买（Best Buy）和洛杉矶的一家专卖店销售其产品。" data-title="Popular gaming chair and desk maker Secretlab launches dedicated US brick-and-mortar locations — new shop in LA, spaces in Best Buy" data-date="11-14 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 00:00</span>
          <span class="news-item-title">热门电竞椅和办公桌制造商Secretlab开设实体店——在洛杉矶开设新店，在百思买开设专区</span>
          <span class="news-item-title-en">Popular gaming chair and desk maker Secretlab launches dedicated US brick-and-mortar locations — new shop in LA, spaces in Best Buy</span>
          <span class="news-value-point">💡 Secretlab目前在百思买（Best Buy）和洛杉矶的一家专卖店销售其产品</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1024777/best-gifts-for-dad-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="您再也不用像以前那样，随便给父亲买一条领带、一个包着皮革的酒具或一套剃须套装了。爸爸们想要——不，他们值得拥有——一件令人难忘的礼物。幸运的是，找到他会喜欢的特别礼物并不难。" data-title="The Verge’s 2026 gift guide for dads" data-date="11-14 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 00:00</span>
          <span class="news-item-title">The Verge 2026年父亲节礼物指南</span>
          <span class="news-item-title-en">The Verge’s 2026 gift guide for dads</span>
          <span class="news-value-point">💡 您再也不用像以前那样，随便给父亲买一条领带、一个包着皮革的酒具或一套剃须套装了</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1032141/paprika-4-recipe-grocery-pantry-app-update-subscription-hands-on" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在 Paprika 3 发布近 10 年后，这款用于管理食谱、整理储藏室、制作购物清单的应用程序迎来了重大升级，几乎在每个方面都增加了更多功能。我测试了 Paprika 4 几个星期，同时" data-title="My favorite recipe app just got a big upgrade — and a subscription fee" data-date="11-14 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 00:00</span>
          <span class="news-item-title">我最喜爱的食谱应用程序刚刚进行了重大升级，并开始收取订阅费</span>
          <span class="news-item-title-en">My favorite recipe app just got a big upgrade — and a subscription fee</span>
          <span class="news-value-point">💡 在 Paprika 3 发布近 10 年后，这款用于管理食谱、整理储藏室、制作购物清单的应用程序迎来了重大升级，几乎在每个方面都增加了更多功能</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-14 03:54（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
