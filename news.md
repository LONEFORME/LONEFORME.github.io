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
      <span>2026-10-30 22:25 抓取更新</span>
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
        <span class="channel-count">61</span>
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
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">1</span>
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
  <div class="ov-item"><span class="ov-num">61</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×14 · BBC×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-30/10723653.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网昆明10月30日电 (黄欣媛)云南省加快推动“十五五”时期退役军人工作高质量发展新闻发布会10月30日在昆明举行。云南省退役军人事务厅党组书记、厅长姜若宁称，云南将推动优秀退役军人名录事迹载入地方志。" data-title="云南推动“戎光”入史志" data-date="10-30 21:43" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-30 21:43</span>
      </div>
      <h2 class="hero-featured-title">云南推动“戎光”入史志</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1023057/arrowmax-arrowspace-s1-electric-screwdriver-ai-camera-kickstarter" target="_blank" rel="noopener" data-cat="keji" data-summary="像Hoto和Fanttik这样的公司已经提升了电动螺丝刀等工具的设计和功能，但Arrowmax希望通过添加相机和人工智能来使它们更智能，这些相机和人工智能可以协同工作，从而消除寻找" data-title="This electric screwdriver uses a camera and AI to figure out what bit you need" data-date="10-30 22:23" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">This electric screwdriver uses a camera and AI to figure out what bit you need</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/30/premier-league-news-carabao-cup-and-wcl-reaction-and-more-football-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本周末⚽英超联赛⚽的新闻和预览：需要注意的10件事| Mail AndyDejan Kulusevski在17个月的伤病裁员后重返托特纳姆热刺的比赛，在俱乐部3-1 ho的最后几分钟比赛" data-title="Forest Green launch legal proceedings against Savage departure, England win controversial U-15 World Cup match, and more – football live" data-date="10-30 22:23" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Forest Green launch legal proceedings against Savage departure, England win controversial U-15 World Cup match, and more – football live</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/020/367.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【京东活动可能随时变更，需以实付款为准】小米 17 开售于 2025 年 9 月，16GB+512GB 首发价 4999 元。京东 11.11 大促期间，按下方步骤下单，叠加 15% 国补后仅需 3836.55 元：领 9.5 折券：微信“京东购物”小程序打开链接（点此查看）领 800-80 元 PLUS 专享券（需 2 积分兑换）：点此查看。领券后进入“京东购物”小程序购物车结算，即可查看优惠后价格。京东小米 1716GB+512GB 国补后 3836.55 元直达链接京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。京东小米 1716GB+512GB 国补后 3836.55 元直达链接淘宝 11.11 主会场：点此前往京东 11.11 主会场：点此" data-title="7000mAh 大电池：小米 17 手机 16GB+512GB 国补后 4999 → 3836 元新低" data-date="10-30 22:19" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">7000mAh 大电池：小米 17 手机 16GB+512GB 国补后 4999 → 3836 元新低</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723653.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网昆明10月30日电 (黄欣媛)云南省加快推动“十五五”时期退役军人工作高质量发展新闻发布会10月30日在昆明举行。云南省退役军人事务厅党组书记、厅长姜若宁称，云南将推动优秀退役军人名录事迹载入地方志。" data-title="云南推动“戎光”入史志" data-date="10-30 21:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:43</span>
          <span class="news-item-title">云南推动“戎光”入史志</span>
          <span class="news-value-point">💡 中新网昆明10月30日电 (黄欣媛)云南省加快推动“十五五”时期退役军人工作高质量发展新闻发布会10月30日在昆明举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723651.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州10月30日电 (记者 程景伟)据广东省退役军人事务厅30日消息，《广东省退役军人服务和保障“十五五”规划》(以下简称《规划》)近日印发，对“十五五”时期全省退役军人工作作出全面安排，明确实施“退役军人服务中心(站)提质增效”“‘戎归南粤’就业创业升级”“烈士纪念设施提质改造”“优抚医疗康养体系建设”“军休服务体系提质”“退役军人事务信息化”等十大工程。" data-title="广东明确“十五五”退役军人服务和保障十大工程" data-date="10-30 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:41</span>
          <span class="news-item-title">广东明确“十五五”退役军人服务和保障十大工程</span>
          <span class="news-value-point">💡 中新网广州10月30日电 (记者 程景伟)据广东省退役军人事务厅30日消息，《广东省退役军人服务和保障“十五五”规划》(以下简称《规划》)近日印…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723650.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州10月30日电 题：一江珠水连濠江，十年共治润民心" data-title="一江珠水连濠江，十年共治润民心" data-date="10-30 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:41</span>
          <span class="news-item-title">一江珠水连濠江，十年共治润民心</span>
          <span class="news-value-point">💡 中新网广州10月30日电 题：一江珠水连濠江，十年共治润民心</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723647.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网杭州10月30日电 (张斌)浙江省政府新闻办30日在杭州举行新闻发布会介绍，2026中非经贸和文化论坛(下称：论坛)将于11月7日在浙江金华义乌开幕。" data-title="相聚“世界义乌” 2026中非经贸和文化论坛将举办" data-date="10-30 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:41</span>
          <span class="news-item-title">相聚“世界义乌” 2026中非经贸和文化论坛将举办</span>
          <span class="news-value-point">💡 中新网杭州10月30日电 (张斌)浙江省政府新闻办30日在杭州举行新闻发布会介绍，2026中非经贸和文化论坛(下称：论坛)将于11月7日在浙江金…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723645.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网拉萨10月30日电 (贡嘎来松)30日，西藏自治区财政厅召开民生保障工作新闻发布会，亮出“十四五”民生投入成绩单，公布2026年民生实事资金安排，并就民生资金监管、“十五五”民生规划作出详细介绍。" data-title="西藏持续加大民生财政投入 筑牢各族群众幸福底线" data-date="10-30 21:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:40</span>
          <span class="news-item-title">西藏持续加大民生财政投入 筑牢各族群众幸福底线</span>
          <span class="news-value-point">💡 中新网拉萨10月30日电 (贡嘎来松)30日，西藏自治区财政厅召开民生保障工作新闻发布会，亮出“十四五”民生投入成绩单，公布2026年民生实事资…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723618.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社昆明10月30日电 (罗婕)云南省公安厅30日消息，第170次中老缅泰湄公河联合巡逻执法行动当天结束。" data-title="第170次中老缅泰湄公河联合巡逻执法行动结束" data-date="10-30 21:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:39</span>
          <span class="news-item-title">第170次中老缅泰湄公河联合巡逻执法行动结束</span>
          <span class="news-value-point">💡 中新社昆明10月30日电 (罗婕)云南省公安厅30日消息，第170次中老缅泰湄公河联合巡逻执法行动当天结束</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723634.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="8月21日，中共中央在中南海召开党外人士座谈会，就中共中央关于持之以恒推进全面从严治党若干重大问题的决定听取各民主党派中央、全国工商联负责人和无党派人士代表的意见建议。中共中央总书记习近平主持座谈会并发表重要讲话。他指出——" data-title="习言道｜治国必先治党，强国必先强党" data-date="10-30 21:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:39</span>
          <span class="news-item-title">习言道｜治国必先治党，强国必先强党</span>
          <span class="news-value-point">💡 8月21日，中共中央在中南海召开党外人士座谈会，就中共中央关于持之以恒推进全面从严治党若干重大问题的决定听取各民主党派中央、全国工商联负责人和无…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723643.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月30日电(记者温馨)10月30日下午，国家主席习近平夫人彭丽媛在北京和陪同德国总统施泰因迈尔来华进行国事访问的德国总统夫人比登本德茶叙。" data-title="彭丽媛同德国总统夫人比登本德茶叙" data-date="10-30 21:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:38</span>
          <span class="news-item-title">彭丽媛同德国总统夫人比登本德茶叙</span>
          <span class="news-value-point">💡 新华社北京10月30日电(记者温馨)10月30日下午，国家主席习近平夫人彭丽媛在北京和陪同德国总统施泰因迈尔来华进行国事访问的德国总统夫人比登本…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c3j47p5gwj5lo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“这次全会进一步表明，习近平的反腐运动没有终点。”专家说，“持续施加纪律压力不应只是阶段性运动，而必须成为中共运作方式中永久存在的一部分。”" data-title="中共五中全会“空椅子”背后：常态化高压反腐如何改变中国官场？" data-date="10-30 21:23" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 21:23</span>
          <span class="news-item-title">中共五中全会“空椅子”背后：常态化高压反腐如何改变中国官场？</span>
          <span class="news-value-point">💡 “这次全会进一步表明，习近平的反腐运动没有终点</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1023054/altman-cheeky-pint-ai-math-interview" target="_blank" rel="noopener" data-cat="shizheng" data-summary="OpenAI首席执行官萨姆·奥尔特曼（ Sam Altman ）表示，经过数月的轰炸，数学家获得了源源不断的人工智能结果，他同情那些努力理解这一切的研究人员。但他无意停下来-并暗示可能会有" data-title="Sam Altman sympathizes with mathematicians, but says OpenAI’s math onslaught won’t stop" data-date="10-30 21:01" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 21:01</span>
          <span class="news-item-title">山姆·奥尔特曼（ Sam Altman ）同情数学家，但表示OpenAI的数学冲击不会停止</span>
          <span class="news-item-title-en">Sam Altman sympathizes with mathematicians, but says OpenAI’s math onslaught won’t stop</span>
          <span class="news-value-point">💡 OpenAI首席执行官萨姆·奥尔特曼（ Sam Altman ）表示，经过数月的轰炸，数学家获得了源源不断的人工智能结果，他同情那些努力理解这一…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723583.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达10月30日电 (记者 李志全)印度尼西亚林业部30日发布消息称，位于西爪哇省庞岸达兰的帕南宗自然保护区近日迎来第三只爪哇野牛幼崽。目前，该保护区爪哇野牛数量已增至7头。" data-title="印尼爪哇野牛诞下第三只幼崽" data-date="10-30 20:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 20:29</span>
          <span class="news-item-title">印尼爪哇野牛诞下第三只幼崽</span>
          <span class="news-value-point">💡 中新社雅加达10月30日电 (记者 李志全)印度尼西亚林业部30日发布消息称，位于西爪哇省庞岸达兰的帕南宗自然保护区近日迎来第三只爪哇野牛幼崽</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cm9wzeg8ql22o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="作为全台人口最多的直辖市，新北市被视为“最关键战场”，将判定蓝绿整体胜负，并可能牵动2028年总统大选。" data-title="台湾新北市长选战：“政二代”苏巧慧对决“专业副手”李四川，谁能拿下蓝绿关键一城？" data-date="10-30 19:31" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 19:31</span>
          <span class="news-item-title">台湾新北市长选战：“政二代”苏巧慧对决“专业副手”李四川，谁能拿下蓝绿关键一城？</span>
          <span class="news-value-point">💡 作为全台人口最多的直辖市，新北市被视为“最关键战场”，将判定蓝绿整体胜负，并可能牵动2028年总统大选</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723546.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着10月31日法国新一轮全国性示威活动临近，澳大利亚、美国、德国、加拿大等国近日相继发布或更新针对法国的旅行安全提醒，警告示威活动可能引发暴力冲突和交通中断。" data-title="多国发布旅行安全提醒 警告公民注意法国新一轮示威活动" data-date="10-30 19:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 19:18</span>
          <span class="news-item-title">多国发布旅行安全提醒 警告公民注意法国新一轮示威活动</span>
          <span class="news-value-point">💡 随着10月31日法国新一轮全国性示威活动临近，澳大利亚、美国、德国、加拿大等国近日相继发布或更新针对法国的旅行安全提醒，警告示威活动可能引发暴力…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/30/us/politics/michigan-senate-democratic-presidential-primary.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="竞选中的进步候选人阿卜杜勒·赛义德（ Abdul El-Sayed ）博士的命运将成为检验左翼进入下一届总统竞选的力量的试金石。" data-title="How Michigan’s Midterm Senate Race Could Influence the 2028 Democratic Presidential Primary" data-date="10-30 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 17:02</span>
          <span class="news-item-title">密歇根州的中期参议院竞选如何影响2028年民主党总统初选</span>
          <span class="news-item-title-en">How Michigan’s Midterm Senate Race Could Influence the 2028 Democratic Presidential Primary</span>
          <span class="news-value-point">💡 竞选中的进步候选人阿卜杜勒·赛义德（ Abdul El-Sayed ）博士的命运将成为检验左翼进入下一届总统竞选的力量的试金石</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723346.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 苏瓦消息：据斐济《太阳报》当地时间30日报道，斐济电信管理局首席执行官普里特·昌德表示，该国通信基站高度依赖电网，备用电源续航有限，若热带气旋与网络攻击同时发生，可能导致通信网络大范围中断，影响应急救援及公共通信。" data-title="斐济官员：气旋及网络攻击恐致全国通信瘫痪" data-date="10-30 16:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 16:57</span>
          <span class="news-item-title">斐济官员：气旋及网络攻击恐致全国通信瘫痪</span>
          <span class="news-value-point">💡 中新网北京10月30日电 苏瓦消息：据斐济《太阳报》当地时间30日报道，斐济电信管理局首席执行官普里特·昌德表示，该国通信基站高度依赖电网，备用…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1023057/arrowmax-arrowspace-s1-electric-screwdriver-ai-camera-kickstarter" target="_blank" rel="noopener" data-cat="keji" data-summary="像Hoto和Fanttik这样的公司已经提升了电动螺丝刀等工具的设计和功能，但Arrowmax希望通过添加相机和人工智能来使它们更智能，这些相机和人工智能可以协同工作，从而消除寻找" data-title="This electric screwdriver uses a camera and AI to figure out what bit you need" data-date="10-30 22:23" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 22:23</span>
          <span class="news-item-title">这款电动螺丝刀使用摄像头和人工智能来确定您需要什么位</span>
          <span class="news-item-title-en">This electric screwdriver uses a camera and AI to figure out what bit you need</span>
          <span class="news-value-point">💡 像Hoto和Fanttik这样的公司已经提升了电动螺丝刀等工具的设计和功能，但Arrowmax希望通过添加相机和人工智能来使它们更智能，这些相机…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/30/business/stock-market-october-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="标准普尔500指数本月将出现小幅下跌，尽管一些对指数产生重大影响的人工智能股票下跌幅度更大。" data-title="Tech Stocks Tumble, but Broader Market Is Holding On" data-date="10-30 22:10" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 22:10</span>
          <span class="news-item-title">科技股下跌，但更广泛的市场仍在继续</span>
          <span class="news-item-title-en">Tech Stocks Tumble, but Broader Market Is Holding On</span>
          <span class="news-value-point">💡 标准普尔500指数本月将出现小幅下跌，尽管一些对指数产生重大影响的人工智能股票下跌幅度更大</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/366.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，随着 AI 技术突飞猛进，许多开发者在大模型辅助加持之下对各种老旧机型进行折腾，例如在诺记吧贴吧就有一位开发者 FORZGC 宣布在 AI 辅助之下为“死亡”多年的微软 Windows Phone 系统打造了一系列应用。该开发者表示，其利用 AI 扒取各大网站 API，进而将其打包为 Windows Phone 系统可用的应用包，虽然只是“简单实现，只能浏览”，但“如果愿意折腾还可以实现更多功能”。同时其进一步表示，“没想到当年没落的系统，现在可以凭借 AI 发挥发挥余热，不至于完全无用”。参考IT之家此前报道，微软现任首席执行官萨蒂亚・纳德拉（Satya Nadella）在接受媒体采访时候，承认放弃 Windows Phone 和移动设备是错误决定，这也是" data-title="梦想不灭：开发者拒绝 Windows Phone 死亡，利用 AI 辅助为微软 Lumia 640 开发新应用" data-date="10-30 22:04" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 22:04</span>
          <span class="news-item-title">梦想不灭：开发者拒绝 Windows Phone 死亡，利用 AI 辅助为微软 Lumia 640 开发新应用</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，随着 AI 技术突飞猛进，许多开发者在大模型辅助加持之下对各种老旧机型进行折腾，例如在诺记吧贴吧就有一位开发者…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/29/technology/amazon-earnings-tech-spending.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在股价下跌的情况下，亚马逊成为最新一家宣布对人工智能进行大量投资的科技公司。" data-title="Big Tech’s Data Center Blitz Is Burning Through Cash and Scaring Wall St." data-date="10-30 22:02" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 22:02</span>
          <span class="news-item-title">大科技公司的数据中心闪电战正在烧毁现金和吓坏华尔街</span>
          <span class="news-item-title-en">Big Tech’s Data Center Blitz Is Burning Through Cash and Scaring Wall St.</span>
          <span class="news-value-point">💡 在股价下跌的情况下，亚马逊成为最新一家宣布对人工智能进行大量投资的科技公司</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/364.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，当地时间 10 月 30 日开盘后，英特尔股价大幅下挫，盘中跌幅一度超过 30%，公司市值蒸发超过 1,370 亿美元（IT之家注：现汇率约合 9,147.3 亿元人民币），超过 2024 年最大单日跌幅（约 26%），如果能达到 31% 将超越 1974 年 7 月 5 日创下的终极历史纪录。路透社报道称，此次暴跌主要源于英特尔发布低于市场预期的第四季度业绩指引，同时警告个人电脑市场疲软、内存价格上涨等问题可能持续至 2027 年上半年。英特尔 2026 年第三季度财报显示，尽管公司当季营收同比增长 21%，达到 165.1 亿美元（现汇率约合 1,102.35 亿元人民币），但第四季度业绩指引低于市场预期，令投资者对其业务复苏前景产生担忧。根据路透社报道" data-title="英特尔股价开盘跌超 30%，或将创下有记录以来最大单日跌幅" data-date="10-30 22:00" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 22:00</span>
          <span class="news-item-title">英特尔股价开盘跌超 30%，或将创下有记录以来最大单日跌幅</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，当地时间 10 月 30 日开盘后，英特尔股价大幅下挫，盘中跌幅一度超过 30%，公司市值蒸发超过 1,370…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/363.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，华为官方今日公开了鸿蒙 HarmonyOS 7 系统最新适配进度。目前，Mate 80、Pura 90、nova 16、MatePad Pro Max 等系列产品开启了全网推送升级，nova 12、nova 13、MatePad Pro 13.2 英寸 2023 等系列开启花粉 Beta 招募。IT之家附更多机型升级计划详情如下（升级方式：打开设置 &gt; 搜索“软件更新”）：延伸阅读鸿蒙 HarmonyOS 7 操作系统于 2026 年 9 月 7 日在华为“HarmonyOS 7 | HUAWEI Mate XT 2 及全场景新品发布会”上正式发布，并即日起开启公测。该系统主打全新空间美学，搭载 Harmony Intelligence 智能架构。此次开启全" data-title="华为鸿蒙 HarmonyOS 7 系统最新适配进度公开：Mate 80 全网推送、nova 13 等开启花粉 Beta 招募" data-date="10-30 21:55" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 21:55</span>
          <span class="news-item-title">华为鸿蒙 HarmonyOS 7 系统最新适配进度公开：Mate 80 全网推送、nova 13 等开启花粉 Beta 招募</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，华为官方今日公开了鸿蒙 HarmonyOS 7 系统最新适配进度</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/" target="_blank" rel="noopener" data-cat="keji" data-summary="DoorDash表示愿意与第三方代理商合作" data-title="DoorDash said it’s only received ‘several hundred’ orders from AI agents" data-date="10-30 21:54" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 21:54</span>
          <span class="news-item-title">DoorDash表示，它只收到了人工智能代理的“数百个”订单</span>
          <span class="news-item-title-en">DoorDash said it’s only received ‘several hundred’ orders from AI agents</span>
          <span class="news-value-point">💡 DoorDash表示愿意与第三方代理商合作</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/361.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，OpenAI CEO 萨姆・奥尔特曼（Sam Altman）在参加《Cheeky Pint》播客节目时表示，他理解数学家面对 AI 研究成果大量涌现时的处境，但 OpenAI 需继续公布具有重要价值的科学发现。他认为，人类有权了解宇宙运行的基本规律，公司不应将重大的基础科学发现长期保留在内部。奥尔特曼在节目中承认，OpenAI 此前公布数学研究成果的方式存在需要改进之处。他表示，希望在推动科学进步的同时，尽可能尊重数百年来推动数学等学科发展的研究群体，并帮助相关领域的研究人员适应 AI 带来的变化。OpenAI 今年已经陆续公布了大量由 AI 开展的数学研究成果，引发数学界对成果发布方式、证明质量和学术归属的争议。研究人员批评，公司部分论文缺乏充分的背景说明" data-title="奥尔特曼回应 AI 冲击：理解数学家的处境，但 OpenAI 不会停止研究" data-date="10-30 21:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 21:50</span>
          <span class="news-item-title">奥尔特曼回应 AI 冲击：理解数学家的处境，但 OpenAI 不会停止研究</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，OpenAI CEO 萨姆・奥尔特曼（Sam Altman）在参加《Cheeky Pint》播客节目时表示，他…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/usb-flash-drives/intelligence-agency-misplaced-a-very-significant-number-of-removable-drives-storage-media-have-been-missing-for-years-but-exact-number-of-lost-devices-remain-unknown" target="_blank" rel="noopener" data-cat="keji" data-summary="一项调查显示，已有数千个驱动器丢失，官员不知道它们可能在哪里。" data-title="Intelligence agency misplaced &#39;a very significant number&#39; of removable drives" data-date="10-30 21:35" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 21:35</span>
          <span class="news-item-title">情报机构错放了“非常大量”的可移动驱动器</span>
          <span class="news-item-title-en">Intelligence agency misplaced 'a very significant number' of removable drives</span>
          <span class="news-value-point">💡 一项调查显示，已有数千个驱动器丢失，官员不知道它们可能在哪里</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/a-primer-on-key-ai-llm-concepts-kv-cache-weights-quantization-and-how-inference-actually-works" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能模型是如何工作的？本入门课程解释了理解法学硕士如何工作的关键概念，并对所有人工智能新术语进行了定义和解释。" data-title="A primer on key AI LLM concepts — KV cache, weights, quantization, and how inference actually works" data-date="10-30 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 21:30</span>
          <span class="news-item-title">AI LLM关键概念入门— KV缓存、权重、量化以及推理实际工作原理</span>
          <span class="news-item-title-en">A primer on key AI LLM concepts — KV cache, weights, quantization, and how inference actually works</span>
          <span class="news-value-point">💡 人工智能模型是如何工作的</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1023070/anthropic-ipo-risk-factors-filing-miracles" target="_blank" rel="noopener" data-cat="keji" data-summary="投资任何股票有点像赌博，因为你把钱押在公司未来的表现上。但是，在最坏的情况下，您如何押注一种可能“对人类构成灾难性或生存风险”的技术？" data-title="Silicon Valley wants you to invest in miracles" data-date="10-30 21:11" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 21:11</span>
          <span class="news-item-title">硅谷希望您投资奇迹</span>
          <span class="news-item-title-en">Silicon Valley wants you to invest in miracles</span>
          <span class="news-value-point">💡 投资任何股票有点像赌博，因为你把钱押在公司未来的表现上</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/30/can-ai-data-centers-be-mass-produced-like-cars-and-online-in-48-hours-this-startup-aims-to-find-out/" target="_blank" rel="noopener" data-cat="keji" data-summary="Runware正在建造一个工厂，在装配线上生产预制AI数据中心。真正的考验将是它是否能够以这样的规模交付。" data-title="Can AI data centers be mass-produced like cars? This startup aims to find out" data-date="10-30 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 21:00</span>
          <span class="news-item-title">人工智能数据中心能像汽车一样大规模生产吗？这家初创公司旨在了解</span>
          <span class="news-item-title-en">Can AI data centers be mass-produced like cars? This startup aims to find out</span>
          <span class="news-value-point">💡 Runware正在建造一个工厂，在装配线上生产预制AI数据中心</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506819.html" target="_blank" rel="noopener" data-cat="keji" data-summary="xs，还要给机器人打绩效" data-title="榜一，拿来吧你！智元这波双模型杀穿多榜榜单" data-date="10-30 20:58" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-30 20:58</span>
          <span class="news-item-title">榜一，拿来吧你！智元这波双模型杀穿多榜榜单</span>
          <span class="news-value-point">💡 xs，还要给机器人打绩效</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/5-years-worth-of-salary-in-bonuses-given-to-700-eligible-micron-workers-as-company-continues-to-battle-union-more-than-4-300-production-line-staff-to-receive-three-bonuses-of-more-than-usd31-000-plus-quarterly-profit-bonuses-starting-next-year" target="_blank" rel="noopener" data-cat="keji" data-summary="符合条件的员工可获得年度绩效奖金、批量生产奖金和一次性升值奖金。从2027年1月开始，还推出了季度利润奖金。" data-title="5 years’ worth of salary in bonuses given to 700 eligible Micron workers as company continues to battle union" data-date="10-30 19:44" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 19:44</span>
          <span class="news-item-title">随着公司继续与工会作斗争，向700名符合条件的美光员工发放5年的奖金</span>
          <span class="news-item-title-en">5 years’ worth of salary in bonuses given to 700 eligible Micron workers as company continues to battle union</span>
          <span class="news-value-point">💡 符合条件的员工可获得年度绩效奖金、批量生产奖金和一次性升值奖金</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-leaker-reveals-moon-lake-chip-as-a-likely-replacement-for-n-series-socs-four-lower-power-efficiency-cores-no-performance-cores-and-a-6-w-tdp" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔泄密者透露， Moon Lake芯片可能取代具有四个低功耗效率内核、无性能内核和6瓦TDP的N系列SoC" data-title="Intel leaker reveals Moon Lake chip as a likely replacement for N" data-date="10-30 19:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 19:40</span>
          <span class="news-item-title">英特尔泄密者透露月湖芯片可能取代N</span>
          <span class="news-item-title-en">Intel leaker reveals Moon Lake chip as a likely replacement for N</span>
          <span class="news-value-point">💡 英特尔泄密者透露， Moon Lake芯片可能取代具有四个低功耗效率内核、无性能内核和6瓦TDP的N系列SoC</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/30/premier-league-news-carabao-cup-and-wcl-reaction-and-more-football-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本周末⚽英超联赛⚽的新闻和预览：需要注意的10件事| Mail AndyDejan Kulusevski在17个月的伤病裁员后重返托特纳姆热刺的比赛，在俱乐部3-1 ho的最后几分钟比赛" data-title="Forest Green launch legal proceedings against Savage departure, England win controversial U-15 World Cup match, and more – football live" data-date="10-30 22:23" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 22:23</span>
          <span class="news-item-title">Forest Green启动针对Savage离开的法律诉讼，英格兰赢得有争议的U-15世界杯比赛等–足球直播</span>
          <span class="news-item-title-en">Forest Green launch legal proceedings against Savage departure, England win controversial U-15 World Cup match, and more – football live</span>
          <span class="news-value-point">💡 本周末⚽英超联赛⚽的新闻和预览：需要注意的10件事| Mail AndyDejan Kulusevski在17个月的伤病裁员后重返托特纳姆热刺的…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/30/regis-le-bris-sunderland-coventry-reunion" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="欧洲足球已经耗尽了资源，但经理坚持认为，忙碌的日程安排是一个写下新篇章的机会。当恩佐·勒菲（ Enzo Le Fée ）拿起球并在转弯前亲吻球时，还剩下20秒的停球时间。正如预期的那样， Frenchma" data-title="‘Where we want to be’: Le Bris stays positive as faltering Sunderland face Coventry reunion" data-date="10-30 21:59" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 21:59</span>
          <span class="news-item-title">“我们想去的地方” ： Le Bris在桑德兰面对考文垂重聚时保持乐观</span>
          <span class="news-item-title-en">‘Where we want to be’: Le Bris stays positive as faltering Sunderland face Coventry reunion</span>
          <span class="news-value-point">💡 欧洲足球已经耗尽了资源，但经理坚持认为，忙碌的日程安排是一个写下新篇章的机会</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13605765/hollie-doyle-grateful-for-another-chance-to-do-what-i-love" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育赛车的大使为她周六在索斯韦尔的首次骑行做准备，并在周六的饲养员杯上预览基恩兰的重要比赛。" data-title="Doyle: Glad to be back in the saddle" data-date="10-30 21:48" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 21:48</span>
          <span class="news-item-title">多伊尔：很高兴回到马鞍上</span>
          <span class="news-item-title-en">Doyle: Glad to be back in the saddle</span>
          <span class="news-value-point">💡 天空体育赛车的大使为她周六在索斯韦尔的首次骑行做准备，并在周六的饲养员杯上预览基恩兰的重要比赛</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmzxj2e2e5p2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）问道，杰克·格雷利什（ Jack Grealish ）因违反俱乐部纪律而被埃弗顿（ Everton ）抛弃后，是“现在还是永远" data-title="Popular and talented - but Grealish is running out of chances" data-date="10-30 21:42" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 21:42</span>
          <span class="news-item-title">受欢迎且才华横溢-但Grealish的机会已经不多了</span>
          <span class="news-item-title-en">Popular and talented - but Grealish is running out of chances</span>
          <span class="news-value-point">💡 首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）问道，杰克·格雷利什（ Jack Grealish ）因违反俱乐部纪律而被埃弗顿（ …</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/30/the-academy-system-needs-a-refresh-but-now-is-the-time-for-carrick-to-trust-in-youth" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联最著名的时代是围绕他们的学院产品建立的，所以为什么不给目前的作物一个闪耀的机会呢？看着曼联温顺地屈服于COMO和伯恩茅斯，让我想起了与你们的问题和比较" data-title="The academy system needs a refresh but now is the time for Carrick to trust in youth | David Pleat" data-date="10-30 20:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 20:00</span>
          <span class="news-item-title">学院系统需要更新，但现在是Carrick信任年轻人的时候了| David Pleat</span>
          <span class="news-item-title-en">The academy system needs a refresh but now is the time for Carrick to trust in youth | David Pleat</span>
          <span class="news-value-point">💡 曼联最著名的时代是围绕他们的学院产品建立的，所以为什么不给目前的作物一个闪耀的机会呢</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605766/max-dowman-red-card-mikel-artetas-tough-love-after-dismissal-this-isnt-disneyland" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔（ Mikel Arteta ）在弗利特伍德（ Fleetwood ）获得红牌后，与马克斯·道曼（ Max Dowman ）一起走上了艰难的爱情道路，称“这是英超联赛，而不是迪士尼乐园” ，关于这位16岁的年轻人需要控制" data-title="Arteta shows tough love to Dowman after red - &#39;This isn&#39;t Disneyland&#39;" data-date="10-30 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 20:00</span>
          <span class="news-item-title">Arteta在红色之后向Dowman展示了强硬的爱- “这不是迪士尼乐园”</span>
          <span class="news-item-title-en">Arteta shows tough love to Dowman after red - 'This isn't Disneyland'</span>
          <span class="news-value-point">💡 米克尔·阿尔特塔（ Mikel Arteta ）在弗利特伍德（ Fleetwood ）获得红牌后，与马克斯·道曼（ Max Dowman ）一起…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Arteta quizzed on Rice, Madueke and Calafiori fitness" data-title="Arsenal latest: Arteta quizzed on Rice, Madueke and Calafiori fitness" data-date="10-30 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 18:00</span>
          <span class="news-item-title">阿森纳最新消息： Arteta在水稻、Madueke和Calafiori健身方面进行测验</span>
          <span class="news-item-title-en">Arsenal latest: Arteta quizzed on Rice, Madueke and Calafiori fitness</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cked3zen65d1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heisenberg ）回答了经理们在第九场比赛中面临的一些最大困境。" data-title="Time to invest in Bournemouth? - FPL gameweek nine dilemmas" data-date="10-30 15:51" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 15:51</span>
          <span class="news-item-title">是时候投资伯恩茅斯了？ - FPL游戏周九大难题</span>
          <span class="news-item-title-en">Time to invest in Bournemouth? - FPL gameweek nine dilemmas</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heise…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqy0r31kwne0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么文森特·康帕尼（ Vincent Kompany ）的健康恐慌提醒我们，管理层会造成身心损失" data-title="Why managers must put their own fitness first" data-date="10-30 15:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 15:41</span>
          <span class="news-item-title">为什么经理必须把自己的健身放在第一位</span>
          <span class="news-item-title-en">Why managers must put their own fitness first</span>
          <span class="news-value-point">💡 英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么文森特·康帕尼（ Vincent Kompany ）的健康恐慌提醒我…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjn5v3pl0159o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联的挣扎比以往任何时候都更加深刻-尤其是前球员。" data-title="How talking about Man Utd&#39;s cycle of doom became an industry" data-date="10-30 14:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 14:14</span>
          <span class="news-item-title">谈论曼联的厄运循环如何成为一个行业</span>
          <span class="news-item-title-en">How talking about Man Utd's cycle of doom became an industry</span>
          <span class="news-value-point">💡 曼联的挣扎比以往任何时候都更加深刻-尤其是前球员</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/30/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布鲁诺·费尔南德斯（ Bruno Fernandes ）欠曼联一场演出，马蒂斯·泰尔（ Mathys Tel ）已抵达马刺队，利物浦正在改善英超联赛最佳射手迈克尔·卡里克（ Michael Carrick ）和布鲁诺·费尔南德斯（ Bruno Fernandes ）本周举行费尔南德斯是一个未使用的替代品" data-title="Premier League: 10 things to look out for this weekend" data-date="10-30 08:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 08:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 布鲁诺·费尔南德斯（ Bruno Fernandes ）欠曼联一场演出，马蒂斯·泰尔（ Mathys Tel ）已抵达马刺队，利物浦正在改善英超…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq1m4j79x50jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）以他对本周末英超联赛赛事的预测，扮演了办公室糟糕的一天明星约翰·汉纳（ John Hannah ） ，以及BBC读者和人工智能。" data-title="Sutton&#39;s predictions v Bad Day At The Office star John Hannah" data-date="10-30 03:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 03:55</span>
          <span class="news-item-title">Sutton的预测v办公室糟糕的一天明星John Hannah</span>
          <span class="news-item-title-en">Sutton's predictions v Bad Day At The Office star John Hannah</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）以他对本周末英超联赛赛事的预测，扮演了办公室糟糕的一天明星约翰·汉纳（ Jo…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/29/chelseas-fine-finishing-has-them-flying-high-but-how-long-can-it-last" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="根据Opta的预期积分模型，尽管处于桌子的两端，但切尔西的表现比周六的对手曼联更糟糕迈克尔·卡里克（ Michael Carrick ）将在周六抵达斯坦福桥（ Stamford Bridge ） ，带着一个死人走路的空气" data-title="Chelsea’s fine finishing has them flying high – but how long can it last?" data-date="10-30 01:21" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 01:21</span>
          <span class="news-item-title">切尔西的精美装饰让他们飞得很高–但它能持续多久？</span>
          <span class="news-item-title-en">Chelsea’s fine finishing has them flying high – but how long can it last?</span>
          <span class="news-value-point">💡 根据Opta的预期积分模型，尽管处于桌子的两端，但切尔西的表现比周六的对手曼联更糟糕迈克尔·卡里克（ Michael Carrick ）将在周六…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605317/tottenham-vs-crystal-palace-have-spurs-genuinely-turned-a-corner-in-the-premier-league-under-roberto-de-zerbi" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="到周六结束时，托特纳姆热刺上次在反弹中赢得三场英超比赛已经有616天了。自从上次取得这一壮举以来，已经有三位不同的经理人来来去去，没有人能够将马刺队带到一个连胜的早晨" data-title="It&#39;s been 616 days: Can Spurs finally win three in a row?" data-date="10-29 23:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 23:30</span>
          <span class="news-item-title">已经616天了：马刺队终于可以连续赢得三场比赛吗？</span>
          <span class="news-item-title-en">It's been 616 days: Can Spurs finally win three in a row?</span>
          <span class="news-value-point">💡 到周六结束时，托特纳姆热刺上次在反弹中赢得三场英超比赛已经有616天了</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605389/arsenals-kai-havertz-in-goal-drought-so-should-mikel-arteta-keep-faith-in-him-ahead-of-viktor-gyokeres-against-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal striker dilemma: Should Arteta keep faith in Havertz?" data-title="Arsenal striker dilemma: Should Arteta keep faith in Havertz?" data-date="10-29 23:13" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 23:13</span>
          <span class="news-item-title">阿森纳前锋困境： Arteta是否应该对Havertz保持信心？</span>
          <span class="news-item-title-en">Arsenal striker dilemma: Should Arteta keep faith in Havertz?</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/020/367.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【京东活动可能随时变更，需以实付款为准】小米 17 开售于 2025 年 9 月，16GB+512GB 首发价 4999 元。京东 11.11 大促期间，按下方步骤下单，叠加 15% 国补后仅需 3836.55 元：领 9.5 折券：微信“京东购物”小程序打开链接（点此查看）领 800-80 元 PLUS 专享券（需 2 积分兑换）：点此查看。领券后进入“京东购物”小程序购物车结算，即可查看优惠后价格。京东小米 1716GB+512GB 国补后 3836.55 元直达链接京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。京东小米 1716GB+512GB 国补后 3836.55 元直达链接淘宝 11.11 主会场：点此前往京东 11.11 主会场：点此" data-title="7000mAh 大电池：小米 17 手机 16GB+512GB 国补后 4999 → 3836 元新低" data-date="10-30 22:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 22:19</span>
          <span class="news-item-title">7000mAh 大电池：小米 17 手机 16GB+512GB 国补后 4999 → 3836 元新低</span>
          <span class="news-value-point">💡 【京东活动可能随时变更，需以实付款为准】小米 17 开售于 2025 年 9 月，16GB+512GB 首发价 4999 元</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025496/newcastle-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Newcastle latest: Jaissle calls for players to turn frustration into motivation" data-title="Newcastle latest: Jaissle calls for players to turn frustration into motivation" data-date="10-30 22:09" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 22:09</span>
          <span class="news-item-title">纽卡斯尔最新消息：贾斯尔呼吁球员将挫折感转化为动力</span>
          <span class="news-item-title-en">Newcastle latest: Jaissle calls for players to turn frustration into motivation</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13605771/weekend-winners-breeders-cup-nap-next-best-and-longshot" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在比赛的另一个星期六之前，周末获胜者团队重新召开会议，讨论最佳投注角度。" data-title="Weekend Winners: Best bets for the Breeders&#39; Cup" data-date="10-30 22:03" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 22:03</span>
          <span class="news-item-title">周末获胜者：饲养员杯最佳赌注</span>
          <span class="news-item-title-en">Weekend Winners: Best bets for the Breeders' Cup</span>
          <span class="news-value-point">💡 在比赛的另一个星期六之前，周末获胜者团队重新召开会议，讨论最佳投注角度</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/365.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="HKC 27 英寸显示器“天启”27U240B 开售于 2026 年 6 月，该机主打 4K 240Hz QD-OLED，提供了 DP 2.1 和 USB-C 90W 接口，首发价 4799 元。京东 11.11 大促期间，按下方步骤下单，叠加 10% 国补后仅需 3805.91 元：领 3000-400 元券：点此查看。点击下方卡片，可领 190 元券。京东 HKC 天启 27U240B 电竞显示器 4K 240Hz、原生 10bit 国补后 3805.91 元领 190 元券京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。该机配备三星四代 QD-OLED 面板（3840x2160 分辨率 240Hz 刷新率），GtG 响应速度 0.03ms，显示" data-title="HKC“天启”27U240B 电竞显示器 4799 → 3805 元：4K 240Hz 三星四代 QD-OLED、配 DP 2.1 + 90W USB-C" data-date="10-30 22:02" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 22:02</span>
          <span class="news-item-title">HKC“天启”27U240B 电竞显示器 4799 → 3805 元：4K 240Hz 三星四代 QD-OLED、配 DP 2.1 + 90W USB-C</span>
          <span class="news-value-point">💡 HKC 27 英寸显示器“天启”27U240B 开售于 2026 年 6 月，该机主打 4K 240Hz QD-OLED，提供了 DP 2.1 …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/30/skip-the-small-talk-make-game-changing-connections-at-techcrunch-founder-summit-with-braindate/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在11月4日在波士顿SoWa电站举行的2026年TechCrunch创始人峰会上，由Braindate提供支持的网络旨在使人们更容易找到这些对话，无论是在一对一会议还是小团体现场会议中。" data-title="Skip the small talk: Make game-changing connections at TechCrunch Founder Summit with Braindate" data-date="10-30 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 22:00</span>
          <span class="news-item-title">跳过闲聊：与Braindate在TechCrunch创始人峰会上建立改变游戏规则的联系</span>
          <span class="news-item-title-en">Skip the small talk: Make game-changing connections at TechCrunch Founder Summit with Braindate</span>
          <span class="news-value-point">💡 在11月4日在波士顿SoWa电站举行的2026年TechCrunch创始人峰会上，由Braindate提供支持的网络旨在使人们更容易找到这些对话…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/monitors/gaming-monitors/tcl-27c2a-pro-27-inch-qd-mini-led-4k-gaming-monitor-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TCL的27C2A Pro是一款超亮27英寸4K迷你LED游戏显示器，具有全阵列局部调光（ 2,304个区域）、量子点颜色、160 Hz、320 Hz/FHD模式、HDR10和自适应同步。它还具有高端视频处理的色彩准确性。" data-title="TCL 27C2A Pro 27-inch QD-Mini LED 4K gaming monitor review: Extreme color and brightness" data-date="10-30 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 22:00</span>
          <span class="news-item-title">TCL 27C2A Pro 27英寸QD-Mini LED 4K游戏显示器评论：极致色彩和亮度</span>
          <span class="news-item-title-en">TCL 27C2A Pro 27-inch QD-Mini LED 4K gaming monitor review: Extreme color and brightness</span>
          <span class="news-value-point">💡 TCL的27C2A Pro是一款超亮27英寸4K迷你LED游戏显示器，具有全阵列局部调光（ 2,304个区域）、量子点颜色、160 Hz、320…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723655.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月30日电 据应急管理部网站消息，10月30日，国家防灾减灾救灾委员会办公室、应急管理部针对西藏巴青县地震灾区降雪影响，在前期已向西藏调拨中央救灾物资，协调救灾板房基础上，会同国家粮食和物资储备局向西藏增加调拨1000套救灾板房，组织各方高效有序搭建，支持灾区妥善做好受灾群众过渡期安置和冬春生活保障工作。" data-title="三部门增加调拨1000套中央救灾物资板房 保障西藏受灾群众安全温暖过冬" data-date="10-30 21:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:53</span>
          <span class="news-item-title">三部门增加调拨1000套中央救灾物资板房 保障西藏受灾群众安全温暖过冬</span>
          <span class="news-value-point">💡 中新网10月30日电 据应急管理部网站消息，10月30日，国家防灾减灾救灾委员会办公室、应急管理部针对西藏巴青县地震灾区降雪影响，在前期已向西藏…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1023112/waymos-next-robotaxi-is-a-purpose-built-toyota-bz4x" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Waymo今天宣布，当它于2027年在东京推出机器人出租车服务时，它将使用在日本组装的丰田bZ4X电动汽车。这一消息建立在Waymo和丰田之间的战略合作伙伴关系的基础上，该合作伙伴关系于2013年首次宣布，" data-title="Waymo’s next robotaxi is a purpose" data-date="10-30 21:52" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 21:52</span>
          <span class="news-item-title">Waymo的下一个机器人出租车是一个目的</span>
          <span class="news-item-title-en">Waymo’s next robotaxi is a purpose</span>
          <span class="news-value-point">💡 Waymo今天宣布，当它于2027年在东京推出机器人出租车服务时，它将使用在日本组装的丰田bZ4X电动汽车</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/29/technology/binance-hack-crypto.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="加密货币交易所表示，它在可能是有史以来最大的加密货币抢劫案中受到了损害。一家研究实验室将盗窃归咎于“朝鲜精英黑客部队”。" data-title="Binance Suspends Withdrawals After Crypto Hackers Steal $6.3 Billion" data-date="10-30 21:46" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 21:46</span>
          <span class="news-item-title">币安在加密黑客窃取63亿美元后暂停提款</span>
          <span class="news-item-title-en">Binance Suspends Withdrawals After Crypto Hackers Steal $6.3 Billion</span>
          <span class="news-value-point">💡 加密货币交易所表示，它在可能是有史以来最大的加密货币抢劫案中受到了损害</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723652.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨10月30日电 (王颖 贡嘎来松)十月底的隆子，紫外线依然强烈，寒意初起。西藏自治区山南市隆子县人民医院内，等候眼科筛查的群众排起长龙，现场忙碌有序。人群中，一名年逾古稀的老人，由县集中供养中心护理员推着轮椅慕名前来就诊，感慨道：“在家门口等到了来自内地的医疗专家，太方便了。”" data-title="跨越三千公里的“光明接力” 常德援藏守护西藏隆子群众“视”界" data-date="10-30 21:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:43</span>
          <span class="news-item-title">跨越三千公里的“光明接力” 常德援藏守护西藏隆子群众“视”界</span>
          <span class="news-value-point">💡 中新网拉萨10月30日电 (王颖 贡嘎来松)十月底的隆子，紫外线依然强烈，寒意初起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723638.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨10月30日电(记者 江飞波)西藏自治区巴青7.0级地震灾害应急处置指挥部(以下简称指挥部)30日公布，截至10月29日18时，地震灾害造成死亡16人、受伤76人、已康复出院67人、在院患者9人。灾区板房需求3299间，现有3192间、已搭建2787间，已入住民众1644户、9136人，入住率70.4%，板房缺口276间(未到位107间、损坏169间)，剩余3828人预计10月30日全部入住。" data-title="西藏巴青7.0级地震：受灾民众板房入住率超七成" data-date="10-30 21:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 21:39</span>
          <span class="news-item-title">西藏巴青7.0级地震：受灾民众板房入住率超七成</span>
          <span class="news-value-point">💡 中新网拉萨10月30日电(记者 江飞波)西藏自治区巴青7.0级地震灾害应急处置指挥部(以下简称指挥部)30日公布，截至10月29日18时，地震灾…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13605757/maybank-championship-charley-hull-four-shots-off-the-lead-after-second-round-in-malaysia" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在马来西亚举行的LPGA马来亚银行锦标赛第二轮之后，英格兰的查理·赫尔（ Charley Hull ）领先四杆。" data-title="Hull remains in contention at LPGA Tour&#39;s Maybank Championship" data-date="10-30 21:23" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 21:23</span>
          <span class="news-item-title">赫尔在LPGA巡回赛的马来亚银行锦标赛上仍然存在争议</span>
          <span class="news-item-title-en">Hull remains in contention at LPGA Tour's Maybank Championship</span>
          <span class="news-value-point">💡 在马来西亚举行的LPGA马来亚银行锦标赛第二轮之后，英格兰的查理·赫尔（ Charley Hull ）领先四杆</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/30/5-days-left-your-last-chance-to-connect-scale-and-save-at-techcrunch-founder-summit-2026/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="5天可节省高达100 $ ， 11月4日在波士顿举行的2026年TechCrunch创始人峰会还可免费获得第二张通行证。立即注册。" data-title="5 days left: Your last chance to connect, scale, and save at TechCrunch Founder Summit 2026" data-date="10-30 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 21:00</span>
          <span class="news-item-title">还剩5天：在2026年TechCrunch创始人峰会上建立联系、扩展规模并享受优惠的最后机会</span>
          <span class="news-item-title-en">5 days left: Your last chance to connect, scale, and save at TechCrunch Founder Summit 2026</span>
          <span class="news-value-point">💡 5天可节省高达100 $ ， 11月4日在波士顿举行的2026年TechCrunch创始人峰会还可免费获得第二张通行证</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/this-is-your-chance-to-secure-an-entire-entry-level-abs-gaming-pc-for-only-usd849-amazing-walmart-deal-sets-you-up-with-an-rtx-5060-graphics-card-and-shaves-usd350-off-the-list-price" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一款价格实惠的桌面游戏PC ，内置腾讯通5060显卡，价格低于$ 850。" data-title="This is your chance to secure an entire entry-level ABS gaming PC for only $849" data-date="10-30 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 21:00</span>
          <span class="news-item-title">这是您仅需$ 849即可获得整台入门级ABS游戏电脑的机会</span>
          <span class="news-item-title-en">This is your chance to secure an entire entry-level ABS gaming PC for only $849</span>
          <span class="news-value-point">💡 一款价格实惠的桌面游戏PC ，内置腾讯通5060显卡，价格低于$ 850</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022592/apple-homeview-amazon-echo-show-16-smart-display-family-computer" target="_blank" rel="noopener" data-cat="zonghe" data-summary="三年前，我为智能显示器写了一篇讣告。该类别-带有触摸屏的智能扬声器-被谷歌和亚马逊的一些动力不足的小工具所困扰，这些小工具试图做得太多，做得太少。那时候，我" data-title="The HomeView and Echo Show 16 could be the family computers I’ve been asking for" data-date="10-30 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 21:00</span>
          <span class="news-item-title">HomeView和Echo Show 16可能是我一直想要的家用电脑</span>
          <span class="news-item-title-en">The HomeView and Echo Show 16 could be the family computers I’ve been asking for</span>
          <span class="news-value-point">💡 三年前，我为智能显示器写了一篇讣告</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ck4g18ql0vj9o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="姆巴佩有关一名“中国领导人”的言论引发众怒，但网络审查令许多人仍不清楚事件究竟是怎么回事。" data-title="中国施压下姆巴佩道歉，但许多人仍不知道他究竟说了什么" data-date="10-30 08:23" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 08:23</span>
          <span class="news-item-title">中国施压下姆巴佩道歉，但许多人仍不知道他究竟说了什么</span>
          <span class="news-value-point">💡 姆巴佩有关一名“中国领导人”的言论引发众怒，但网络审查令许多人仍不清楚事件究竟是怎么回事</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-30 22:25（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
