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
      <span>2026-11-18 00:59 抓取更新</span>
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
        <span class="channel-count">53</span>
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
        <span class="channel-count">11</span>
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
  <div class="ov-item"><span class="ov-num">53</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×11 · 天空体育×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-18/10733805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月18日电(记者周颖、杨深深)韩国总统李在明18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议。" data-title="聚焦APEC｜韩国总统李在明抵达深圳" data-date="11-18 00:51" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-18 00:51</span>
      </div>
      <h2 class="hero-featured-title">聚焦APEC｜韩国总统李在明抵达深圳</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/17/jensen-huang-says-he-would-be-honored-if-allowed-to-return-as-nvidia-ceo/" target="_blank" rel="noopener" data-cat="keji" data-summary="在辞职后的首次公开声明中，英伟达创始人黄仁勋表示愿意重返首席执行官职位。" data-title="Jensen Huang says he would be ‘honored’ if allowed to return as Nvidia CEO" data-date="11-18 00:44" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Jensen Huang表示，如果能重返Nvidia担任首席执行官，他将“深感荣幸”</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal double winner Storey dies aged 81" data-title="Arsenal double winner Storey dies aged 81" data-date="11-18 00:45" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">阿森纳双冠王斯托里去世，享年 81 岁</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/17/us/measles-us-whats-next.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="该国可能需要数年时间才能重新获得消除疟疾的地位。与此同时，社区需要采取多项策略来保护人民。" data-title="Measles Is Officially Back in the United States. What Now?" data-date="11-18 00:50" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">麻疹已正式在美国卷土重来。接下来该怎么办？</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10733805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月18日电(记者周颖、杨深深)韩国总统李在明18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议。" data-title="聚焦APEC｜韩国总统李在明抵达深圳" data-date="11-18 00:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 00:51</span>
          <span class="news-item-title">聚焦APEC｜韩国总统李在明抵达深圳</span>
          <span class="news-value-point">💡 新华社深圳11月18日电(记者周颖、杨深深)韩国总统李在明18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10733804.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月18日电(记者杨深深、周颖)马来西亚总理安瓦尔18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议。" data-title="聚焦APEC｜马来西亚总理安瓦尔抵达深圳" data-date="11-18 00:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 00:33</span>
          <span class="news-item-title">聚焦APEC｜马来西亚总理安瓦尔抵达深圳</span>
          <span class="news-value-point">💡 新华社深圳11月18日电(记者杨深深、周颖)马来西亚总理安瓦尔18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10733803.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月18日电(记者周颖、杨深深)文莱苏丹哈桑纳尔18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议。" data-title="聚焦APEC｜文莱苏丹哈桑纳尔抵达深圳" data-date="11-18 00:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 00:31</span>
          <span class="news-item-title">聚焦APEC｜文莱苏丹哈桑纳尔抵达深圳</span>
          <span class="news-value-point">💡 新华社深圳11月18日电(记者周颖、杨深深)文莱苏丹哈桑纳尔18日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10733801.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日凌晨，文莱苏丹哈桑纳尔乘机抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议。" data-title="文莱苏丹哈桑纳尔抵达深圳 将出席APEC领导人非正式会议" data-date="11-18 00:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 00:15</span>
          <span class="news-item-title">文莱苏丹哈桑纳尔抵达深圳 将出席APEC领导人非正式会议</span>
          <span class="news-value-point">💡 11月18日凌晨，文莱苏丹哈桑纳尔乘机抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733796.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社东京11月17日电 (记者 朱晨曦)日本宇宙航空研究开发机构17日说，超期服役的“隼鸟2”号小行星探测器因4台发动机全部出现故障，不得不放弃此前的探测目标，改为飞掠探测另一天体。" data-title="日本“隼鸟2”号小行星探测器因发动机故障变更探测目标" data-date="11-17 23:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 23:56</span>
          <span class="news-item-title">日本“隼鸟2”号小行星探测器因发动机故障变更探测目标</span>
          <span class="news-value-point">💡 中新社东京11月17日电 (记者 朱晨曦)日本宇宙航空研究开发机构17日说，超期服役的“隼鸟2”号小行星探测器因4台发动机全部出现故障，不得不放…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733794.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年11月17日，中共中央政治局委员、外交部长王毅在深圳会见加拿大外长阿南德。" data-title="王毅会见加拿大外长阿南德" data-date="11-17 23:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 23:47</span>
          <span class="news-item-title">王毅会见加拿大外长阿南德</span>
          <span class="news-value-point">💡 2026年11月17日，中共中央政治局委员、外交部长王毅在深圳会见加拿大外长阿南德</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733789.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="深圳是中国改革开放的试验田，也是中国互利共赢开放战略的重要窗口。一组数字，看深圳与APEC的“双向奔赴”。" data-title="一组数字，看深圳与APEC“双向奔赴”" data-date="11-17 22:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 22:33</span>
          <span class="news-item-title">一组数字，看深圳与APEC“双向奔赴”</span>
          <span class="news-value-point">💡 深圳是中国改革开放的试验田，也是中国互利共赢开放战略的重要窗口</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733780.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月17日电 据美国有线电视新闻网(CNN)报道，当地时间17日，美国总统特朗普在菲律宾马尼拉表示，“我期待访问中国，我们有一些十分重要的议题需要磋商。”" data-title="特朗普最新表态：我期待访问中国" data-date="11-17 22:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 22:10</span>
          <span class="news-item-title">特朗普最新表态：我期待访问中国</span>
          <span class="news-value-point">💡 中新网11月17日电 据美国有线电视新闻网(CNN)报道，当地时间17日，美国总统特朗普在菲律宾马尼拉表示，“我期待访问中国，我们有一些十分重要…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733742.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网东京11月17日电 (记者 朱晨曦)据日本广播协会(NHK)报道，日本神奈川县横须贺市警方17日当场逮捕一名涉嫌酒后损坏财物的驻日美军士兵。" data-title="一名驻日美军涉嫌酒后损坏财物被捕" data-date="11-17 21:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 21:45</span>
          <span class="news-item-title">一名驻日美军涉嫌酒后损坏财物被捕</span>
          <span class="news-value-point">💡 中新网东京11月17日电 (记者 朱晨曦)据日本广播协会(NHK)报道，日本神奈川县横须贺市警方17日当场逮捕一名涉嫌酒后损坏财物的驻日美军士兵</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733746.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月17日电 (记者 周昕)亚太经合组织(APEC)第三十三次领导人非正式会议将启，由多国青年联袂演绎的APEC主题音乐《同一个世界(One World)》受到关注。词曲作者、在深圳生活16年的韩国青年申文燮17日接受中新社专访时说，深圳不断赋予他创作的热情与灵感，期待以音乐架起文化交流之桥。" data-title="（深圳APEC）韩国青年申文燮：深圳赋予我创作热情和灵感" data-date="11-17 21:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 21:44</span>
          <span class="news-item-title">（深圳APEC）韩国青年申文燮：深圳赋予我创作热情和灵感</span>
          <span class="news-value-point">💡 中新社深圳11月17日电 (记者 周昕)亚太经合组织(APEC)第三十三次领导人非正式会议将启，由多国青年联袂演绎的APEC主题音乐《同一个世界…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crgj360lnqv6o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="离开深圳充满科技感的天际线后，你将会看到习近平治下中国所面临的种种挑战。" data-title="中国以AI奇境接待各国领袖，但他们看不到的另一面是什么？" data-date="11-17 19:44" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 19:44</span>
          <span class="news-item-title">中国以AI奇境接待各国领袖，但他们看不到的另一面是什么？</span>
          <span class="news-value-point">💡 离开深圳充满科技感的天际线后，你将会看到习近平治下中国所面临的种种挑战</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cme3d27d7lnpo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新竹市是民众党此前唯一赢得执政权的县市，现任市长高虹安寻求连任，她这次虽已退出民众党、改以无党籍身份参选，但学者指出其选情不仅将影响双方未来合作模式能否延续，也可能牵动2028年全国大选的政治布局。" data-title="“蓝白合”示范区：新竹市选情如何透露台湾第三势力的未来？" data-date="11-17 17:49" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 17:49</span>
          <span class="news-item-title">“蓝白合”示范区：新竹市选情如何透露台湾第三势力的未来？</span>
          <span class="news-value-point">💡 新竹市是民众党此前唯一赢得执政权的县市，现任市长高虹安寻求连任，她这次虽已退出民众党、改以无党籍身份参选，但学者指出其选情不仅将影响双方未来合作…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/jensen-huang-says-he-would-be-honored-if-allowed-to-return-as-nvidia-ceo/" target="_blank" rel="noopener" data-cat="keji" data-summary="在辞职后的首次公开声明中，英伟达创始人黄仁勋表示愿意重返首席执行官职位。" data-title="Jensen Huang says he would be ‘honored’ if allowed to return as Nvidia CEO" data-date="11-18 00:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 00:44</span>
          <span class="news-item-title">Jensen Huang表示，如果能重返Nvidia担任首席执行官，他将“深感荣幸”</span>
          <span class="news-item-title-en">Jensen Huang says he would be ‘honored’ if allowed to return as Nvidia CEO</span>
          <span class="news-value-point">💡 在辞职后的首次公开声明中，英伟达创始人黄仁勋表示愿意重返首席执行官职位</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-says-he-would-be-honored-to-return-as-nvidia-ceo-first-statement-since-resignation-follows-support-from-billionaires-investors-and-some-employees" target="_blank" rel="noopener" data-cat="keji" data-summary="在辞职后的首次发言中，英伟达前首席执行官黄仁勋表示愿意重返其原先的职位。" data-title="Jensen Huang says he would be ‘honored’ to return as Nvidia CEO" data-date="11-18 00:33" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 00:33</span>
          <span class="news-item-title">Jensen Huang表示，他将“荣幸”地重返Nvidia首席执行官的职位</span>
          <span class="news-item-title-en">Jensen Huang says he would be ‘honored’ to return as Nvidia CEO</span>
          <span class="news-value-point">💡 在辞职后的首次发言中，英伟达前首席执行官黄仁勋表示愿意重返其原先的职位</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/daydreams-new-ai-agent-acts-as-your-personal-stylist-and-can-shop-for-you-too/" target="_blank" rel="noopener" data-cat="keji" data-summary="Daydream 的全新 AI 购物助手可以记住您的风格、虚拟试穿衣服、根据您的衣橱搭配服装、跟踪促销活动并完成购物。" data-title="Daydream’s new AI agent acts as your personal stylist — and can shop for you, too" data-date="11-18 00:32" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 00:32</span>
          <span class="news-item-title">Daydream 的新 AI 代理充当您的个人造型师，还可以为您购物</span>
          <span class="news-item-title-en">Daydream’s new AI agent acts as your personal stylist — and can shop for you, too</span>
          <span class="news-value-point">💡 Daydream 的全新 AI 购物助手可以记住您的风格、虚拟试穿衣服、根据您的衣橱搭配服装、跟踪促销活动并完成购物</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1035410/doj-megaspeed-nvidia-investigation-update" target="_blank" rel="noopener" data-cat="keji" data-summary="美国司法部和商务部表示，他们正在调查总部位于新加坡的数据中心公司Megaspeed。此前有报道称，去年一项调查曾被叫停，而该调查与Nvidia首席执行官黄仁勋的辞职有关。" data-title="The DOJ says it’s investigating Megaspeed" data-date="11-18 00:19" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 00:19</span>
          <span class="news-item-title">美国司法部表示正在调查Megaspeed</span>
          <span class="news-item-title-en">The DOJ says it’s investigating Megaspeed</span>
          <span class="news-value-point">💡 美国司法部和商务部表示，他们正在调查总部位于新加坡的数据中心公司Megaspeed</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1035420/jensen-huang-nvidia-return-as-ceo-statement" target="_blank" rel="noopener" data-cat="keji" data-summary="据《华尔街日报》报道，上周辞去英伟达首席执行官职务的黄仁勋在一份声明中表示，如果公司董事会希望他回归，他愿意再次担任首席执行官。“自从我离职以来，我收到了大量呼吁" data-title="Jensen Huang says he’s willing to return as Nvidia CEO" data-date="11-18 00:09" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 00:09</span>
          <span class="news-item-title">黄仁勋表示愿意重返英伟达担任首席执行官</span>
          <span class="news-item-title-en">Jensen Huang says he’s willing to return as Nvidia CEO</span>
          <span class="news-value-point">💡 据《华尔街日报》报道，上周辞去英伟达首席执行官职务的黄仁勋在一份声明中表示，如果公司董事会希望他回归，他愿意再次担任首席执行官</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-safety-legislation-has-a-conflict-of-interest-problem-big-us-labs-are-warning-of-risk-just-as-cheaper-chinese-open-weight-models-erode-their-commercial-edge" target="_blank" rel="noopener" data-cat="keji" data-summary="关于人工智能安全的讨论既是政治话题，也是现实生活中的担忧。我们采访了多位专家，以了解立法如何成为监管人工智能市场的便捷方式。" data-title="AI safety legislation has a conflict-of-interest problem — Big US labs are warning of risk just as cheaper Chinese open-weight models erode their commercial edge" data-date="11-18 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 00:00</span>
          <span class="news-item-title">人工智能安全立法存在利益冲突问题——就在美国大型实验室警告风险之际，更便宜的中国开源模型正在侵蚀它们的商业优势。</span>
          <span class="news-item-title-en">AI safety legislation has a conflict-of-interest problem — Big US labs are warning of risk just as cheaper Chinese open-weight models erode their commercial edge</span>
          <span class="news-value-point">💡 关于人工智能安全的讨论既是政治话题，也是现实生活中的担忧</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/former-nvidia-ceo-jensen-huang-will-appear-before-a-house-foreign-affairs-panel-amid-concerns-over-his-affair-with-a-suspected-chinese-spy-will-testify-behind-closed-doors-december-1-nvidia-lawyer-will-also-appear" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达前首席执行官黄仁勋将于12月1日出席众议院外交事务委员会、情报委员会和中国问题特别委员会的听证会，英伟达的律师将于12月2日随后出席。在此之前，黄仁勋承认与一名女性有染。" data-title="Former Nvidia CEO Jensen Huang will appear before a House Foreign Affairs panel amid concerns over his affair with a suspected Chinese spy" data-date="11-17 23:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 23:50</span>
          <span class="news-item-title">鉴于人们对其与一名疑似中国间谍的婚外情感到担忧，英伟达前首席执行官黄仁勋将出席众议院外交事务委员会的听证会。</span>
          <span class="news-item-title-en">Former Nvidia CEO Jensen Huang will appear before a House Foreign Affairs panel amid concerns over his affair with a suspected Chinese spy</span>
          <span class="news-value-point">💡 英伟达前首席执行官黄仁勋将于12月1日出席众议院外交事务委员会、情报委员会和中国问题特别委员会的听证会，英伟达的律师将于12月2日随后出席</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/563.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 17 日消息，快手可灵 AI 今天（17 日）深夜宣布，全新一代图像创作模型 Kling Image 4.0 正式上线，同时面向企业客户与开发者开放 API 接入。新模型采用“理解生成统一”架构，探索将视觉理解与图像生成融入统一的模型体系，进一步打通从理解创作意图到生成视觉内容的链路。快手表示，在实现模型能力进一步提升的同时，图像创作在真实感、文字表现和内容组织上，也拥有了更多可能。围绕这些方向，Kling Image 4.0 带来了三大核心升级：真实感与原生 8K：将物理规律与视觉感知融入生成过程，让光影、肤质与材质纹理呈现接近相机直出的自然观感；首次支持原生 8K 图像生成，呈现更丰富细节，为高清展示与后期裁切提供更多空间。超强文字表现力：支持单张照片内生成 2000" data-title="快手可灵全新一代图像创作模型 Kling Image 4.0 上线：首次支持原生 8K，单图内可生成 2000 字" data-date="11-17 23:26" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 23:26</span>
          <span class="news-item-title">快手可灵全新一代图像创作模型 Kling Image 4.0 上线：首次支持原生 8K，单图内可生成 2000 字</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，快手可灵 AI 今天（17 日）深夜宣布，全新一代图像创作模型 Kling Image 4.0 正式上线，同时…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/545.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 17 日消息，英伟达今日宣布，董事会已设立国家安全与出口管制监督委员会。这一新设常设委员会负责在董事会层面监督公司的国家安全政策、出口管制合规及全球贸易风险管理。英伟达现有的国家安全团队与全球贸易合规团队，其日常运营情况将直接向该委员会及临时首席执行官科莱特 · 克雷斯（Colette Kress）汇报。委员会由董事苏珊娜 · 诺拉 · 约翰逊（Suzanne Nora Johnson）担任主席，成员包括董事斯蒂芬 ·C· 尼尔（Stephen C. Neal）与约翰 ·O· 达比里（John O. Dabiri）。IT之家注意到，委员会至少每季度召开一次会议，包括与管理层联席开会以及举行董事闭门会议。委员会将聘任独立外部专家，提供法律、国家安全及贸易合规方面的专业支持。" data-title="英伟达董事会设立国家安全与出口管制监督委员会" data-date="11-17 23:05" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 23:05</span>
          <span class="news-item-title">英伟达董事会设立国家安全与出口管制监督委员会</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，英伟达今日宣布，董事会已设立国家安全与出口管制监督委员会</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/taipei-101-lit-up-in-support-of-jensen-huang-skyscraper-adorned-with-messages-of-support-following-resignation-as-nvidia-ceo" target="_blank" rel="noopener" data-cat="keji" data-summary="台北101大楼通宵亮起支持黄仁勋的标语。黄仁勋是英伟达的前首席执行官，他在承认与一位被指控为中国间谍的前客户有染后离开了公司。另一段婚外情，这次" data-title="Taipei 101 lit up in support of Jensen Huang" data-date="11-17 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 23:00</span>
          <span class="news-item-title">台北 101 大楼亮灯支持黄仁勋</span>
          <span class="news-item-title-en">Taipei 101 lit up in support of Jensen Huang</span>
          <span class="news-value-point">💡 台北101大楼通宵亮起支持黄仁勋的标语</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/isomorphic-labs-raises-5b-as-it-looks-to-take-drug-candidates-to-clinical-trials/" target="_blank" rel="noopener" data-cat="keji" data-summary="Isomorphic Labs是一家人工智能药物发现平台，于2021年从谷歌的DeepMind剥离出来，在C轮融资中筹集了50亿美元。" data-title="Isomorphic Labs raises $5B as it looks to take drug candidates to clinical trials" data-date="11-17 22:50" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 22:50</span>
          <span class="news-item-title">Isomorphic Labs筹集50亿美元，旨在将候选药物推向临床试验</span>
          <span class="news-item-title-en">Isomorphic Labs raises $5B as it looks to take drug candidates to clinical trials</span>
          <span class="news-value-point">💡 Isomorphic Labs是一家人工智能药物发现平台，于2021年从谷歌的DeepMind剥离出来，在C轮融资中筹集了50亿美元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/amd-attacks-nvidias-fp64-emulation-at-sc26-touts-native-double-precision-on-instinct-mi430x-says-ozaki-schemes-fit-less-than-10-percent-of-hpc-workloads-and-triple-memory-use-and-emulated-fp64-is-a-poor-fit-for-many-hpc-workloads" target="_blank" rel="noopener" data-cat="keji" data-summary="在2026超算大会上，AMD大肆宣传其MI430X加速器所提供的原生FP64支持的优势。该公司表示，Ozaki FP64 仿真仅能满足一小部分 HPC 工作负载的需求，这使 MI430X 成为一个独特的基础。" data-title="AMD attacks Nvidia&#39;s FP64 emulation at SC26, touts native double-precision on Instinct MI430X" data-date="11-17 22:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 22:30</span>
          <span class="news-item-title">AMD在SC26上抨击Nvidia的FP64仿真，并吹捧Instinct MI430X的原生双精度</span>
          <span class="news-item-title-en">AMD attacks Nvidia's FP64 emulation at SC26, touts native double-precision on Instinct MI430X</span>
          <span class="news-value-point">💡 在2026超算大会上，AMD大肆宣传其MI430X加速器所提供的原生FP64支持的优势</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510695.html" target="_blank" rel="noopener" data-cat="keji" data-summary="82亿美元股票，46天闪电交割" data-title="并购完成，李飞飞正式率队加入AMD！苏妈亲自欢迎" data-date="11-17 22:15" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-17 22:15</span>
          <span class="news-item-title">并购完成，李飞飞正式率队加入AMD！苏妈亲自欢迎</span>
          <span class="news-value-point">💡 82亿美元股票，46天闪电交割</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/nvidias-first-big-move-after-jensen-huangs-exit-targets-national-security/" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司表示，新的常务委员会将对国家安全政策、出口管制合规性和全球贸易风险进行董事会层面的监督。" data-title="Nvidia’s first big move after Jensen Huang’s exit targets national security" data-date="11-17 22:05" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 22:05</span>
          <span class="news-item-title">黄仁勋离任后，英伟达的首个大动作瞄准了国家安全</span>
          <span class="news-item-title-en">Nvidia’s first big move after Jensen Huang’s exit targets national security</span>
          <span class="news-value-point">💡 该公司表示，新的常务委员会将对国家安全政策、出口管制合规性和全球贸易风险进行董事会层面的监督</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/nvidia-warns-customers-of-new-us-rule-that-could-expose-them-to-lawsuits-for-serving-chinese-clients-commerce-department-releases-interim-regulations-preventing-foreign-actors-from-using-advanced-compute-based-on-american-tech" target="_blank" rel="noopener" data-cat="keji" data-summary="这一警告是在黄仁勋丑闻、美国商务部出台新规以及参议院一项待审议法案的背景下发出的。" data-title="Nvidia warns customers of new US rule that could expose them to lawsuits for serving Chinese clients" data-date="11-17 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 22:00</span>
          <span class="news-item-title">英伟达警告客户，美国的新规定可能使他们因服务中国客户而面临诉讼风险</span>
          <span class="news-item-title-en">Nvidia warns customers of new US rule that could expose them to lawsuits for serving Chinese clients</span>
          <span class="news-value-point">💡 这一警告是在黄仁勋丑闻、美国商务部出台新规以及参议院一项待审议法案的背景下发出的</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal double winner Storey dies aged 81" data-title="Arsenal double winner Storey dies aged 81" data-date="11-18 00:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 00:45</span>
          <span class="news-item-title">阿森纳双冠王斯托里去世，享年 81 岁</span>
          <span class="news-item-title-en">Arsenal double winner Storey dies aged 81</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613327/arsenal-transfer-news-david-raya-jurrien-timber-and-piero-hincapie-close-to-finalising-new-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同。" data-title="Arsenal close to new deals for Raya, Timber and Hincapie" data-date="11-18 00:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 00:23</span>
          <span class="news-item-title">阿森纳即将与拉亚、廷伯和欣卡皮埃达成新合同</span>
          <span class="news-item-title-en">Arsenal close to new deals for Raya, Timber and Hincapie</span>
          <span class="news-value-point">💡 阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613327/arsenal-transfer-news-david-raya-jurrien-timber-and-piero-hincapie-close-to-finalising-new-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同。" data-title="Arsenal close to new deals for Raya, Timber and Hincapie" data-date="11-18 00:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 00:23</span>
          <span class="news-item-title">阿森纳即将与拉亚、廷伯和欣卡皮埃达成新合同</span>
          <span class="news-item-title-en">Arsenal close to new deals for Raya, Timber and Hincapie</span>
          <span class="news-value-point">💡 阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613275/wayne-rooney-says-he-contemplated-suicide-during-lowest-point-of-manchester-united-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头。" data-title="Rooney contemplated suicide at ‘lowest point’ of Man Utd career" data-date="11-17 22:36" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 22:36</span>
          <span class="news-item-title">鲁尼在曼联生涯的“最低谷”曾有过自杀念头</span>
          <span class="news-item-title-en">Rooney contemplated suicide at ‘lowest point’ of Man Utd career</span>
          <span class="news-value-point">💡 韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613275/wayne-rooney-says-he-contemplated-suicide-during-lowest-point-of-manchester-united-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头。" data-title="Rooney contemplated suicide at ‘lowest point’ of Man Utd career" data-date="11-17 22:36" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 22:36</span>
          <span class="news-item-title">鲁尼在曼联生涯的“最低谷”曾有过自杀念头</span>
          <span class="news-item-title-en">Rooney contemplated suicide at ‘lowest point’ of Man Utd career</span>
          <span class="news-value-point">💡 韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6ge39lgyzzzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳正与后卫皮耶罗·因卡皮耶就新合同进行深入谈判。" data-title="Hincapie in advanced talks over new Arsenal deal" data-date="11-17 21:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 21:09</span>
          <span class="news-item-title">欣卡皮耶正在就与阿森纳的新合同进行深入谈判</span>
          <span class="news-item-title-en">Hincapie in advanced talks over new Arsenal deal</span>
          <span class="news-value-point">💡 阿森纳正与后卫皮耶罗·因卡皮耶就新合同进行深入谈判</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: Estevao scores in dominant Brazil win" data-title="Chelsea latest: Estevao scores in dominant Brazil win" data-date="11-17 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 20:00</span>
          <span class="news-item-title">切尔西最新消息：埃斯特旺在巴西大胜中进球</span>
          <span class="news-item-title-en">Chelsea latest: Estevao scores in dominant Brazil win</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: Estevao scores in dominant Brazil win" data-title="Chelsea latest: Estevao scores in dominant Brazil win" data-date="11-17 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 20:00</span>
          <span class="news-item-title">切尔西最新消息：埃斯特旺在巴西大胜中进球</span>
          <span class="news-item-title-en">Chelsea latest: Estevao scores in dominant Brazil win</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvgxvg4v981o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自他身穿“为什么总是针对我？”的T恤庆祝曼彻斯特德比以来，已经过去了十五年。曼彻斯特德比T恤庆祝活动已经过去了十五年，BBC体育回顾了前曼城前锋马里奥·巴洛特利的职业生涯。" data-title="Why always him? The rise and fall of Balotelli" data-date="11-17 14:15" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 14:15</span>
          <span class="news-item-title">为什么总是他？巴洛特利的起起落落</span>
          <span class="news-item-title-en">Why always him? The rise and fall of Balotelli</span>
          <span class="news-value-point">💡 自他身穿“为什么总是针对我</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13612986/declan-rice-contract-arsenal-midfielder-verbally-agrees-new-320000-a-week-deal-with-the-premier-league-champions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据天空体育新闻透露，德克兰·赖斯已口头同意阿森纳的新长期合同条款。" data-title="Rice verbally agrees new Arsenal contract" data-date="11-17 05:12" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 05:12</span>
          <span class="news-item-title">赖斯口头同意与阿森纳签订新合同</span>
          <span class="news-item-title-en">Rice verbally agrees new Arsenal contract</span>
          <span class="news-value-point">💡 据天空体育新闻透露，德克兰·赖斯已口头同意阿森纳的新长期合同条款</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmge3y2qjlyro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托马斯·弗兰克——现已确认成为水晶宫的新任主教练——能否在热刺经历一段艰难时期后，在塞尔赫斯特公园重建自己的声誉？" data-title="How Frank can restore reputation and save Crystal Palace" data-date="11-17 01:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 01:46</span>
          <span class="news-item-title">弗兰克如何挽回声誉并拯救水晶宫</span>
          <span class="news-item-title-en">How Frank can restore reputation and save Crystal Palace</span>
          <span class="news-value-point">💡 托马斯·弗兰克——现已确认成为水晶宫的新任主教练——能否在热刺经历一段艰难时期后，在塞尔赫斯特公园重建自己的声誉</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/us/measles-us-whats-next.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="该国可能需要数年时间才能重新获得消除疟疾的地位。与此同时，社区需要采取多项策略来保护人民。" data-title="Measles Is Officially Back in the United States. What Now?" data-date="11-18 00:50" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 00:50</span>
          <span class="news-item-title">麻疹已正式在美国卷土重来。接下来该怎么办？</span>
          <span class="news-item-title-en">Measles Is Officially Back in the United States. What Now?</span>
          <span class="news-value-point">💡 该国可能需要数年时间才能重新获得消除疟疾的地位</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/well/us-measles-elimination-status.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="该国曾被认为是遏制这种高传染性病毒的全球领头羊。如今，导致数千人感染的大规模疫情可能成为常态。" data-title="U.S. Loses Its Measles Elimination Status, a Historic Setback for American Health" data-date="11-18 00:24" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 00:24</span>
          <span class="news-item-title">美国失去麻疹消除地位，这是美国卫生事业的历史性挫折</span>
          <span class="news-item-title-en">U.S. Loses Its Measles Elimination Status, a Historic Setback for American Health</span>
          <span class="news-value-point">💡 该国曾被认为是遏制这种高传染性病毒的全球领头羊</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1035401/school-cell-phone-ban-study-meta-settlement" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一项新的全国性研究发现，在校内禁止使用手机可以使学习成绩略有提高。现在，研究人员希望了解孩子们在课堂之外使用手机是否可能导致学生学习成绩的进一步下降——为此，他们将使用" data-title="Banning phones really does help kids learn, researchers say" data-date="11-18 00:13" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 00:13</span>
          <span class="news-item-title">研究人员表示，禁止使用手机确实有助于孩子学习</span>
          <span class="news-item-title-en">Banning phones really does help kids learn, researchers say</span>
          <span class="news-value-point">💡 一项新的全国性研究发现，在校内禁止使用手机可以使学习成绩略有提高</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10733799.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社首尔11月17日电 (记者 金旭)针对韩国社会近期对利用人工智能(AI)技术实施考试作弊的担忧，韩国总统李在明当地时间17日表示，作弊行为严重破坏公平竞争的根基，损害社会长期积累的信任，是一种严重犯罪。" data-title="韩国高考防作弊“升级” 李在明称作弊行为是严重犯罪" data-date="11-18 00:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 00:02</span>
          <span class="news-item-title">韩国高考防作弊“升级” 李在明称作弊行为是严重犯罪</span>
          <span class="news-value-point">💡 中新社首尔11月17日电 (记者 金旭)针对韩国社会近期对利用人工智能(AI)技术实施考试作弊的担忧，韩国总统李在明当地时间17日表示，作弊行为…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1034392/flipper-devices-one-zero-pocket-linux-computer-multi-tool-preorder-kickstarte" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Flipper Devices于去年5月首次发布了Flipper One，该公司将其描述为“专为高性能计算和IP联网而打造的开放式Linux多功能工具”。现在，Flipper Devices已在Kickstarter上发起众筹活动，您可以在此预订。" data-title="You can now preorder the Flipper One that puts a Linux computer in your pocket" data-date="11-18 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 00:00</span>
          <span class="news-item-title">您现在可以预订 Flipper One，将 Linux 电脑装进口袋</span>
          <span class="news-item-title-en">You can now preorder the Flipper One that puts a Linux computer in your pocket</span>
          <span class="news-value-point">💡 Flipper Devices于去年5月首次发布了Flipper One，该公司将其描述为“专为高性能计算和IP联网而打造的开放式Linux多功…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1034571/gruv-4k-blu-ray-movies-black-friday-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Gruv一直像传说中的消防水带一样，全年源源不断地提供电影优惠，但这家由环球影业运营的在线零售商在黑色星期五前真的要大放异彩了。该网站有一个页面，上面有 4" data-title="Scoop up three great 4K Blu" data-date="11-18 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 00:00</span>
          <span class="news-item-title">入手三部精彩的4K蓝光电影</span>
          <span class="news-item-title-en">Scoop up three great 4K Blu</span>
          <span class="news-value-point">💡 Gruv一直像传说中的消防水带一样，全年源源不断地提供电影优惠，但这家由环球影业运营的在线零售商在黑色星期五前真的要大放异彩了</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/world/europe/ukraine-kyiv-russia-kerch-bridge-crimea.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="摧毁这座将俄罗斯与被占领的克里米亚半岛连接起来的唯一桥梁，长期以来一直是基辅的首要目标。" data-title="Ukraine Attacks Kerch Bridge Linking Russia to Occupied Crimea" data-date="11-17 23:54" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 23:54</span>
          <span class="news-item-title">乌克兰袭击连接俄罗斯与被占领克里米亚的刻赤大桥</span>
          <span class="news-item-title-en">Ukraine Attacks Kerch Bridge Linking Russia to Occupied Crimea</span>
          <span class="news-value-point">💡 摧毁这座将俄罗斯与被占领的克里米亚半岛连接起来的唯一桥梁，长期以来一直是基辅的首要目标</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/wearable-tech/xreal-aura-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Xreal Aura将轻巧的眼镜与电池供电的Computing Puck相结合" data-title="Xreal Aura Review: Android XR combined with lightweight glasses delivers a true next-gen spatial computing experience" data-date="11-17 23:37" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 23:37</span>
          <span class="news-item-title">Xreal Aura评测：Android XR与轻质眼镜相结合，带来真正的下一代空间计算体验</span>
          <span class="news-item-title-en">Xreal Aura Review: Android XR combined with lightweight glasses delivers a true next-gen spatial computing experience</span>
          <span class="news-value-point">💡 Xreal Aura将轻巧的眼镜与电池供电的Computing Puck相结合</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13613272/mercedes-confirm-aduo-turbo-upgrade-ready-for-las-vegas-gp-with-kimi-antonelli-set-to-run-new-engine-part" target="_blank" rel="noopener" data-cat="zonghe" data-summary="世界冠军梅赛德斯车队将在本周末的拉斯维加斯大奖赛上推出ADUO涡轮增压器升级版，不过乔治·拉塞尔将不会使用该升级版，以避免在争夺车手冠军亚军的过程中再次受到发车位处罚。" data-title="Mercedes set to run ADUO engine upgrade in Las Vegas with one driver" data-date="11-17 23:31" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 23:31</span>
          <span class="news-item-title">梅赛德斯计划在拉斯维加斯由一名车手驾驶搭载ADUO升级版发动机的赛车</span>
          <span class="news-item-title-en">Mercedes set to run ADUO engine upgrade in Las Vegas with one driver</span>
          <span class="news-value-point">💡 世界冠军梅赛德斯车队将在本周末的拉斯维加斯大奖赛上推出ADUO涡轮增压器升级版，不过乔治·拉塞尔将不会使用该升级版，以避免在争夺车手冠军亚军的过…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/562.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，松下发布了 Lumix SHX1，这是首款冠以 Lumix 品牌的紧凑型电影摄影机。此前，松下将电影摄影机业务与消费级影像业务分别归属于 Varicam 和 Lumix 两个品牌，如今 SHX1 的推出意味着两大业务正式走向整合。松下表示：“数十年来，松下一直为广播电视和电影行业提供支持，其 Varicam 电影摄影机已被全球众多电影、电视剧和纪录片制作团队采用。这些专业技术也逐渐融入 Lumix 产品线，并催生了 2019 年推出的 Lumix S1H。这是一款具备电影级画质的专业视频设备。2024 年，松下进一步整合了专业视听业务与消费级影像业务，两大业务都致力于激发用户的创作潜力。全新的 Lumix SHX1 将双方的专业技术融为一体，打造出一款紧凑型" data-title="松下发布首款 Lumix 品牌电影摄影机 SHX1：6K 全画幅，售价 4699.99 美元" data-date="11-17 23:13" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 23:13</span>
          <span class="news-item-title">松下发布首款 Lumix 品牌电影摄影机 SHX1：6K 全画幅，售价 4699.99 美元</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，松下发布了 Lumix SHX1，这是首款冠以 Lumix 品牌的紧凑型电影摄影机</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/streaming/1035221/3-body-problem-season-two-trailer-premiere-date-netflix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Netflix《三体》系列第一季的结局是，牛津五人组的幸存成员对人类完全没有做好应对三体人抵达地球的准备这一想法感到幻灭。但在该剧的第一部预告片中，" data-title="The aliens are coming in 3 Body Problem’s first season 2 trailer" data-date="11-17 23:04" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 23:04</span>
          <span class="news-item-title">《三体》第二季首支预告片：外星人来了</span>
          <span class="news-item-title-en">The aliens are coming in 3 Body Problem’s first season 2 trailer</span>
          <span class="news-value-point">💡 Netflix《三体》系列第一季的结局是，牛津五人组的幸存成员对人类完全没有做好应对三体人抵达地球的准备这一想法感到幻灭</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/voyage-labs-raises-12-million-for-a-specialized-ai-travel-assistant/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Voyage Labs的旗舰产品名为Atlas，旨在作为您的行程规划个人助理，目前已推出私人测试版。" data-title="Voyage Labs raises $12 million for a specialized AI travel assistant" data-date="11-17 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 23:00</span>
          <span class="news-item-title">Voyage Labs为专业人工智能旅行助手筹集1200万美元资金</span>
          <span class="news-item-title-en">Voyage Labs raises $12 million for a specialized AI travel assistant</span>
          <span class="news-value-point">💡 Voyage Labs的旗舰产品名为Atlas，旨在作为您的行程规划个人助理，目前已推出私人测试版</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1035258/trmnl-e-ink-spectra-6-frame-dashboard-display-poster-photos" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Trmnl是一家以高度可定制的E Ink仪表板而闻名的公司，这些仪表板可以充当从桌面日历到股票跟踪器的各种工具。该公司推出了一款新显示屏，也非常适合展示艺术品和照片。这不是该公司的" data-title="This E Ink photo frame can double as your family’s digital dashboard" data-date="11-17 22:49" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 22:49</span>
          <span class="news-item-title">这款电子墨水相框也可以用作您家庭的数字仪表板</span>
          <span class="news-item-title-en">This E Ink photo frame can double as your family’s digital dashboard</span>
          <span class="news-value-point">💡 Trmnl是一家以高度可定制的E Ink仪表板而闻名的公司，这些仪表板可以充当从桌面日历到股票跟踪器的各种工具</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/542.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，华为 Mate X8 及全场景新品发布会今日官宣定档 11 月 24 日 14:30 举行。届时，华为将发布最新一代大折叠旗舰手机。华为官方今日也发布了多张宣传图，展示了 Mate X8 的上手效果，紫金锦、青云锦、丹霞锦、苍穹黑、雪域白五款配色全覆盖。据华为董事、终端 BG CEO 何刚介绍，全新华为 Mate X8 把东方美学融入产品设计。新机采用“钇晶宝石嵌入寰宇星环”的设计思路，轴盖处还有鎏光腰线。从官图来看，鎏光腰线的颜色与手机本体是同一配色。IT之家附华为官网 Mate X8 五款配色外观如下：▲ 华为 Mate X8 紫金锦▲ 华为 Mate X8 苍穹黑▲ 华为 Mate X8 雪域白▲ 华为 Mate X8 青云锦▲ 华为 Mate X8" data-title="华为 Mate X8 大折叠手机上手效果图发布，何刚揭秘新机外观设计细节" data-date="11-17 22:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 22:38</span>
          <span class="news-item-title">华为 Mate X8 大折叠手机上手效果图发布，何刚揭秘新机外观设计细节</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，华为 Mate X8 及全场景新品发布会今日官宣定档 11 月 24 日 14:30 举行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/science-corporations-brain-tech-is-worth-3-5-billion-after-new-funding/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Science Corp 完成了 4 亿美元的 D 轮融资，以扩大其抗失明业务。" data-title="Science Corporation’s brain tech is worth $3.5 billion after new funding" data-date="11-17 22:26" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 22:26</span>
          <span class="news-item-title">Science Corporation 的脑科技在新一轮融资后估值达 35 亿美元</span>
          <span class="news-item-title-en">Science Corporation’s brain tech is worth $3.5 billion after new funding</span>
          <span class="news-value-point">💡 Science Corp 完成了 4 亿美元的 D 轮融资，以扩大其抗失明业务</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-18 00:59（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
