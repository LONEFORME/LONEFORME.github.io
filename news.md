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
      <span>2026-11-03 01:19 抓取更新</span>
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
        <span class="channel-count">60</span>
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
  <div class="ov-item"><span class="ov-num">60</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×17 · 量子位×6</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-02/10725080.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月2日凌晨，瑞典、比利时、卢森堡、爱沙尼亚等欧洲多国超市遭到黑客攻击，冷藏和冷冻系统受到影响，冷柜温度被远程调高至50摄氏度，导致食品变质。这与上个月法国多个连锁超市发生的事件如出一辙。比利时检方今天表示，已就此启动刑事调查。" data-title="冰箱变烤箱 欧洲多国超市冷柜再遭网络攻击" data-date="11-02 23:56" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-02 23:56</span>
      </div>
      <h2 class="hero-featured-title">冰箱变烤箱 欧洲多国超市冷柜再遭网络攻击</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior/" target="_blank" rel="noopener" data-cat="keji" data-summary="这里有一个直接来自科幻小说的问题：如果人工智能可以在你决定之前预测你要做什么，即使是在一个全新的情况下？" data-title="42AI comes out of stealth with $62.5M and a world model that can ‘predict human behavior’" data-date="11-03 00:30" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">42AI comes out of stealth with $62.5M and a world model that can ‘predict human behavior’</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/nov/02/arsenal-liverpool-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日在利物浦的胜利表明，枪手更深入，更有经验，并且与比上赛季更弱的竞争者对抗。在此处注册我们的免费通讯阿森纳在英超联赛排行榜上占据三分。" data-title="Arsenal have everything they need to repeat as Premier League champions | Jonathan Wilson" data-date="11-02 23:47" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Arsenal have everything they need to repeat as Premier League champions | Jonathan Wilson</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/02/well/kratom-wellness-marketing-addiction.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="有些人说，他们是通过健康播客、健身房的免费样品或健身影响者来介绍这种药物的。" data-title="They Tried Kratom for Its Health Benefits, Then They Became Addicted" data-date="11-03 01:11" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">They Tried Kratom for Its Health Benefits, Then They Became Addicted</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10725080.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月2日凌晨，瑞典、比利时、卢森堡、爱沙尼亚等欧洲多国超市遭到黑客攻击，冷藏和冷冻系统受到影响，冷柜温度被远程调高至50摄氏度，导致食品变质。这与上个月法国多个连锁超市发生的事件如出一辙。比利时检方今天表示，已就此启动刑事调查。" data-title="冰箱变烤箱 欧洲多国超市冷柜再遭网络攻击" data-date="11-02 23:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 23:56</span>
          <span class="news-item-title">冰箱变烤箱 欧洲多国超市冷柜再遭网络攻击</span>
          <span class="news-value-point">💡 当地时间11月2日凌晨，瑞典、比利时、卢森堡、爱沙尼亚等欧洲多国超市遭到黑客攻击，冷藏和冷冻系统受到影响，冷柜温度被远程调高至50摄氏度，导致食…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1024357/florida-governors-race-donalds-jolly-data-centers" target="_blank" rel="noopener" data-cat="shizheng" data-summary="终身共和党人帕蒂·齐胡特（ Patti Zirhut ）几周来一直在研究她的选票。Zirhut在2016年， 2020年和2024年热切地投票支持唐纳德·特朗普总统，但她今年没有遵守党的路线。“我的选票搞混了，”她说。她在投票f" data-title="Could data center backlash flip Florida?" data-date="11-02 23:05" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-02 23:05</span>
          <span class="news-item-title">数据中心的反弹会翻转佛罗里达州吗？</span>
          <span class="news-item-title-en">Could data center backlash flip Florida?</span>
          <span class="news-value-point">💡 终身共和党人帕蒂·齐胡特（ Patti Zirhut ）几周来一直在研究她的选票</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10725074.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月2日，伊朗总统佩泽希齐扬表示，政府正努力通过对话解决问题，在这方面，伊朗最高领袖也赋予了政府一定的权力。" data-title="伊总统：伊朗最高领袖已赋予政府在谈判领域一定的权力" data-date="11-02 22:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 22:55</span>
          <span class="news-item-title">伊总统：伊朗最高领袖已赋予政府在谈判领域一定的权力</span>
          <span class="news-value-point">💡 当地时间11月2日，伊朗总统佩泽希齐扬表示，政府正努力通过对话解决问题，在这方面，伊朗最高领袖也赋予了政府一定的权力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10725073.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【东盟专线】柬埔寨累计清理逾3600平方公里受战争爆炸物污染土地" data-title="柬埔寨累计清理逾3600平方公里受战争爆炸物污染土地" data-date="11-02 22:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 22:45</span>
          <span class="news-item-title">柬埔寨累计清理逾3600平方公里受战争爆炸物污染土地</span>
          <span class="news-value-point">💡 【东盟专线】柬埔寨累计清理逾3600平方公里受战争爆炸物污染土地</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10725065.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月2日电 11月2日，受中共中央委托，中共中央政治局委员、中央统战部部长李干杰向党外人士通报中共二十届五中全会精神。" data-title="李干杰受中共中央委托向党外人士通报中共二十届五中全会精神" data-date="11-02 22:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 22:33</span>
          <span class="news-item-title">李干杰受中共中央委托向党外人士通报中共二十届五中全会精神</span>
          <span class="news-value-point">💡 新华社北京11月2日电 11月2日，受中共中央委托，中共中央政治局委员、中央统战部部长李干杰向党外人士通报中共二十届五中全会精神</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10725066.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月2日电 十四届全国人大常委会第二十五次会议2日上午在北京人民大会堂举行第一次全体会议。赵乐际委员长主持。" data-title="十四届全国人大常委会第二十五次会议在京举行 审议检察公益诉讼法草案、水法修订草案等 赵乐际主持" data-date="11-02 22:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 22:22</span>
          <span class="news-item-title">十四届全国人大常委会第二十五次会议在京举行 审议检察公益诉讼法草案、水法修订草案等 赵乐际主持</span>
          <span class="news-value-point">💡 新华社北京11月2日电 十四届全国人大常委会第二十五次会议2日上午在北京人民大会堂举行第一次全体会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10725049.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月2日，中共中央政治局委员、中央外办主任王毅在京同沙特国务大臣、内阁成员、国家安全顾问艾班举行会谈。艾班转交了沙特王储兼首相穆罕默德就中沙双边关系发展和双方共同关心的问题致习近平主席的信函。" data-title="王毅同沙特国家安全顾问艾班会谈" data-date="11-02 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:59</span>
          <span class="news-item-title">王毅同沙特国家安全顾问艾班会谈</span>
          <span class="news-value-point">💡 11月2日，中共中央政治局委员、中央外办主任王毅在京同沙特国务大臣、内阁成员、国家安全顾问艾班举行会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724992.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网悉尼11月2日电 (记者 薄雯雯)由悉尼华星艺术团旗下紫藤舞苑原创的大型舞蹈诗《大合之舞》11月1日晚在澳大利亚悉尼上演。" data-title="舞蹈诗《大合之舞》澳大利亚悉尼上演" data-date="11-02 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:54</span>
          <span class="news-item-title">舞蹈诗《大合之舞》澳大利亚悉尼上演</span>
          <span class="news-value-point">💡 中新网悉尼11月2日电 (记者 薄雯雯)由悉尼华星艺术团旗下紫藤舞苑原创的大型舞蹈诗《大合之舞》11月1日晚在澳大利亚悉尼上演</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724976.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷11月2日电 (梁峻祥 李映民)泰国旅游与体育部2日公布的统计数据显示，2026年1月至10月，泰国累计接待外国游客2546.43万人次，较去年同期减少4.59%。其中，中国游客累计达424.44万人次，同比增长12.44%。" data-title="泰国前十个月接待外国游客2546万人次  同比下降4.59%" data-date="11-02 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:54</span>
          <span class="news-item-title">泰国前十个月接待外国游客2546万人次  同比下降4.59%</span>
          <span class="news-value-point">💡 中新社曼谷11月2日电 (梁峻祥 李映民)泰国旅游与体育部2日公布的统计数据显示，2026年1月至10月，泰国累计接待外国游客2546.43万人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724989.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网银川11月2日电 (杨迪 李琪梁)“存量用地盘活难”是基层反映强烈的问题。记者2日从“加强国土空间规划管控引领优化自然资源要素配置—宁夏‘十五五’高质量发展新闻发布会”上获悉，宁夏相关部门在供地政策上积极探索，打通低效用地再开发的“最后一公里”。" data-title="宁夏打通低效用地再开发“最后一公里”" data-date="11-02 21:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:50</span>
          <span class="news-item-title">宁夏打通低效用地再开发“最后一公里”</span>
          <span class="news-value-point">💡 中新网银川11月2日电 (杨迪 李琪梁)“存量用地盘活难”是基层反映强烈的问题</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724971.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网银川11月2日电 (杨迪 李琪梁)记者2日从“加强国土空间规划管控引领优化自然资源要素配置—宁夏‘十五五’高质量发展新闻发布会”上获悉，宁夏编制《宁夏回族自治区乡村风貌提升导则(试行)》(下称《导则》)，构建“宏观分区定基调、中观村域控要素、微观建筑优营建”的乡村风貌指引体系，指导各地因地制宜提升乡村风貌。" data-title="宁夏构建乡村风貌指引体系" data-date="11-02 21:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:44</span>
          <span class="news-item-title">宁夏构建乡村风貌指引体系</span>
          <span class="news-value-point">💡 中新网银川11月2日电 (杨迪 李琪梁)记者2日从“加强国土空间规划管控引领优化自然资源要素配置—宁夏‘十五五’高质量发展新闻发布会”上获悉，宁…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/02/magazine/identity-politics-economy-class.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="自特朗普回归以来，关于多元化的讨论已经平静下来。今年的中期选举表明，美国人可以为新的事物做好准备。" data-title="Identity Politics Have Entered a New Phase" data-date="11-02 21:42" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 21:42</span>
          <span class="news-item-title">身份政治已进入新阶段</span>
          <span class="news-item-title-en">Identity Politics Have Entered a New Phase</span>
          <span class="news-value-point">💡 自特朗普回归以来，关于多元化的讨论已经平静下来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10725027.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网成都11月2日电 (记者 张浪)四川省纪委监委2日消息：内江市委原常委、宣传部原部长蒋学东涉嫌严重违纪违法，目前正接受四川省纪委监委纪律审查和监察调查。" data-title="四川省内江市委原常委、宣传部原部长蒋学东接受纪律审查和监察调查" data-date="11-02 21:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:40</span>
          <span class="news-item-title">四川省内江市委原常委、宣传部原部长蒋学东接受纪律审查和监察调查</span>
          <span class="news-value-point">💡 中新网成都11月2日电 (记者 张浪)四川省纪委监委2日消息：内江市委原常委、宣传部原部长蒋学东涉嫌严重违纪违法，目前正接受四川省纪委监委纪律审…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724960.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月2日电 11月2日，中共中央政治局委员、中央外办主任王毅在北京会见伊朗最高国家安全委员会副秘书巴盖里。" data-title="王毅会见伊朗最高国家安全委员会副秘书巴盖里" data-date="11-02 21:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:19</span>
          <span class="news-item-title">王毅会见伊朗最高国家安全委员会副秘书巴盖里</span>
          <span class="news-value-point">💡 中新社北京11月2日电 11月2日，中共中央政治局委员、中央外办主任王毅在北京会见伊朗最高国家安全委员会副秘书巴盖里</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724973.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月2日电 中共中央政治局常委、全国政协主席王沪宁2日在京分别会见俄罗斯联邦委员会主席马特维延科，由越共中央政治局委员、中央书记处书记、中央政策战略部部长阮青毅率领的越南共产党代表团。" data-title="王沪宁分别会见俄罗斯联邦委员会主席马特维延科、越南共产党代表团" data-date="11-02 21:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:18</span>
          <span class="news-item-title">王沪宁分别会见俄罗斯联邦委员会主席马特维延科、越南共产党代表团</span>
          <span class="news-value-point">💡 新华社北京11月2日电 中共中央政治局常委、全国政协主席王沪宁2日在京分别会见俄罗斯联邦委员会主席马特维延科，由越共中央政治局委员、中央书记处书…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior/" target="_blank" rel="noopener" data-cat="keji" data-summary="这里有一个直接来自科幻小说的问题：如果人工智能可以在你决定之前预测你要做什么，即使是在一个全新的情况下？" data-title="42AI comes out of stealth with $62.5M and a world model that can ‘predict human behavior’" data-date="11-03 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 00:30</span>
          <span class="news-item-title">42AI凭借$ 6250万和一个可以“预测人类行为”的世界模型脱颖而出</span>
          <span class="news-item-title-en">42AI comes out of stealth with $62.5M and a world model that can ‘predict human behavior’</span>
          <span class="news-value-point">💡 这里有一个直接来自科幻小说的问题：如果人工智能可以在你决定之前预测你要做什么，即使是在一个全新的情况下</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/277.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 2 日消息，Anthropic PBC 披露，截至 9 月 30 日的第三季度营收接近 170 亿美元（IT之家注：现汇率约合 1,132.35 亿元人民币），同比暴涨 11 倍，市场对这家 AI 实验室有望创下纪录的 IPO 预期进一步升温。这家 Claude 大模型背后的公司当地时间周一向美国证券交易委员会（SEC）提交文件显示：截至 9 月末的三个月，净亏损 233 亿美元（现汇率约合 1,551.98 亿元人民币）；去年同期净亏损为 121 亿美元（现汇率约合 805.96 亿元人民币）。本季度运营费用飙升至 175 亿美元（现汇率约合 1,165.65 亿元人民币），同比增幅 292%。文件显示，公司已敲定总额 8,950 亿美元（现汇率约合 5.96 万亿元人" data-title="Anthropic 第三季度营收 170 亿美元同比暴涨 11 倍，冲刺史上最大 IPO" data-date="11-02 23:02" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 23:02</span>
          <span class="news-item-title">Anthropic 第三季度营收 170 亿美元同比暴涨 11 倍，冲刺史上最大 IPO</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，Anthropic PBC 披露，截至 9 月 30 日的第三季度营收接近 170 亿美元（IT之家注：现汇率约…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10725075.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京11月2日电 (记者 张素)人工智能(AI)正在改变人们获取知识、处理信息和开展交流的方式，但技术进步并不能替代人的情感体验、价值判断和自我认识。如何面对技术发展带来的心理变化，如何理解人的内在需求？" data-title="聚焦AI时代人的意义 心理分析与中国文化国际学术论坛将举行" data-date="11-02 23:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 23:00</span>
          <span class="news-item-title">聚焦AI时代人的意义 心理分析与中国文化国际学术论坛将举行</span>
          <span class="news-value-point">💡 中新网北京11月2日电 (记者 张素)人工智能(AI)正在改变人们获取知识、处理信息和开展交流的方式，但技术进步并不能替代人的情感体验、价值判断…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10725067.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网嘉兴11月2日电 (钱晨菲)11月2日，2026年“互联网之光”博览会在浙江嘉兴乌镇启幕，“人工智能+低空安全”装备应用展同步开幕。展区入口，身高2.6米的交管机甲“潮安甲”与参观者互动，科普交通安全知识，成为现场人气颇高的打卡点。展区内81件警用智能装备有序排布，集中展示了浙江公安深化警企合作、推动警用装备研究的探索。" data-title="警用智能装备亮相浙江乌镇 “空地网”筑牢安全防线" data-date="11-02 22:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 22:32</span>
          <span class="news-item-title">警用智能装备亮相浙江乌镇 “空地网”筑牢安全防线</span>
          <span class="news-value-point">💡 中新网嘉兴11月2日电 (钱晨菲)11月2日，2026年“互联网之光”博览会在浙江嘉兴乌镇启幕，“人工智能+低空安全”装备应用展同步开幕</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/274.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 2 日消息，萨姆 · 奥尔特曼近期关于内存的言论引发越来越多人反对，埃隆 · 马斯克也加入了这场声讨。上周，这位 OpenAI 首席执行官的一番话在全网、尤其是玩家群体中引发强烈不满。他称，人们把内存装在个人电脑里，而不是放在数据中心，是一件“很糟糕”的事。在和博主 Cheeky Pint 的访谈中，奥尔特曼说：“从全球资源分配角度来看，所有人都把全球有限的 DRAM 资源放在自家电脑里，而内存大部分时间利用率只有 5%，这其实非常糟糕。在供给紧张的大环境下，资源放在云端才能实现利用率最大化。可很多人的直觉恰恰相反。”这番言论遭到大量嘲讽。不少人认为，无论他本意如何，听起来像是想剥夺个人对内存的所有权，迫使全社会把资源交给 OpenAI 这类 AI 企业使用。社交媒体上充" data-title="OpenAI CEO 奥尔特曼称个人电脑浪费内存遭全网声讨，马斯克也来补刀" data-date="11-02 22:21" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 22:21</span>
          <span class="news-item-title">OpenAI CEO 奥尔特曼称个人电脑浪费内存遭全网声讨，马斯克也来补刀</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，萨姆 · 奥尔特曼近期关于内存的言论引发越来越多人反对，埃隆 · 马斯克也加入了这场声讨</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse" target="_blank" rel="noopener" data-cat="keji" data-summary="在10月4日至10月20日期间检测到未经授权的活动后，英伟达正在调查涉及其Brev云开发平台的安全事件。事件可能暴露了用于访问客户虚拟机的SSH密钥。NVIDIA" data-title="NVIDIA Brev security breach may have exposed SSH keys used to access customer VMs — investigation finds unauthorized activity spanning 16 days, but no evidence of misuse" data-date="11-02 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-02 22:00</span>
          <span class="news-item-title">NVIDIA BREV安全漏洞可能暴露了用于访问客户虚拟机的SSH密钥—调查发现跨越16天的未经授权的活动，但没有滥用的证据</span>
          <span class="news-item-title-en">NVIDIA Brev security breach may have exposed SSH keys used to access customer VMs — investigation finds unauthorized activity spanning 16 days, but no evidence of misuse</span>
          <span class="news-value-point">💡 在10月4日至10月20日期间检测到未经授权的活动后，英伟达正在调查涉及其Brev云开发平台的安全事件</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI表示， ChatGPT和Codex将在此更改后从相同的分配池中提取使用情况。" data-title="OpenAI is finally merging ChatGPT’s Chat and Work tabs" data-date="11-02 21:57" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-02 21:57</span>
          <span class="news-item-title">OpenAI终于合并了ChatGPT的“聊天”和“工作”选项卡</span>
          <span class="news-item-title-en">OpenAI is finally merging ChatGPT’s Chat and Work tabs</span>
          <span class="news-value-point">💡 OpenAI表示， ChatGPT和Codex将在此更改后从相同的分配池中提取使用情况</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507277.html" target="_blank" rel="noopener" data-cat="keji" data-summary="商汤SenseNova 6.8 Flash" data-title="顶级AI翻车的活儿，被这个新出的免费国产AI接住了！" data-date="11-02 21:36" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 21:36</span>
          <span class="news-item-title">顶级AI翻车的活儿，被这个新出的免费国产AI接住了！</span>
          <span class="news-value-point">💡 商汤SenseNova 6.8 Flash</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom" target="_blank" rel="noopener" data-cat="keji" data-summary="Qwenputer是股票Qwen 3.5 4B LLM与32位RISC-V CPU的实验性混合，编译并直接插入其权重。" data-title="AI model gets a 32-bit RISC-V CPU compiled directly into its weights, then runs DOOM on it" data-date="11-02 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-02 21:30</span>
          <span class="news-item-title">AI模型将32位RISC-V CPU直接编译为其权重，然后在其上运行厄运</span>
          <span class="news-item-title-en">AI model gets a 32-bit RISC-V CPU compiled directly into its weights, then runs DOOM on it</span>
          <span class="news-value-point">💡 Qwenputer是股票Qwen 3.5 4B LLM与32位RISC-V CPU的实验性混合，编译并直接插入其权重</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507260.html" target="_blank" rel="noopener" data-cat="keji" data-summary="上海仪电与上海创智学院联合发布“飞轮转・万象生”仪电智算数链生态。" data-title="从“能调用”到“敢托付”：仪电智算云 Token 工厂的三重可信" data-date="11-02 15:47" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 15:47</span>
          <span class="news-item-title">从“能调用”到“敢托付”：仪电智算云 Token 工厂的三重可信</span>
          <span class="news-value-point">💡 上海仪电与上海创智学院联合发布“飞轮转・万象生”仪电智算数链生态</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507225.html" target="_blank" rel="noopener" data-cat="keji" data-summary="新版“机器人三定律”。" data-title="OpenAI重写大模型法则，第一条：忠于人类！！" data-date="11-02 15:27" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 15:27</span>
          <span class="news-item-title">OpenAI重写大模型法则，第一条：忠于人类！！</span>
          <span class="news-value-point">💡 新版“机器人三定律”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507150.html" target="_blank" rel="noopener" data-cat="keji" data-summary="模型管线双驱动" data-title="央视严选“中国AI创业十骏”：唯一AI制药公司是清华系" data-date="11-02 14:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 14:28</span>
          <span class="news-item-title">央视严选“中国AI创业十骏”：唯一AI制药公司是清华系</span>
          <span class="news-value-point">💡 模型管线双驱动</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507107.html" target="_blank" rel="noopener" data-cat="keji" data-summary="能指挥Agent干活，还能控制智能家居" data-title="小米开源了个150元的AI小玩意，火到配件都涨价了" data-date="11-02 14:08" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 14:08</span>
          <span class="news-item-title">小米开源了个150元的AI小玩意，火到配件都涨价了</span>
          <span class="news-value-point">💡 能指挥Agent干活，还能控制智能家居</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507082.html" target="_blank" rel="noopener" data-cat="keji" data-summary="HuggingFace疑似泄露权重已被下5000次" data-title="GPT-6.2 Astra开启灰测！Claude Mythos 5.5同日曝光" data-date="11-02 12:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 12:28</span>
          <span class="news-item-title">GPT-6.2 Astra开启灰测！Claude Mythos 5.5同日曝光</span>
          <span class="news-value-point">💡 HuggingFace疑似泄露权重已被下5000次</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5djvk2dm33xo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="这些数据中心正滚存着数百亿英镑的债务。" data-title="人工智能泡沫将爆破？这群“新云端”公司正加剧市场担忧" data-date="11-02 08:17" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 08:17</span>
          <span class="news-item-title">人工智能泡沫将爆破？这群“新云端”公司正加剧市场担忧</span>
          <span class="news-value-point">💡 这些数据中心正滚存着数百亿英镑的债务</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/02/arsenal-liverpool-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日在利物浦的胜利表明，枪手更深入，更有经验，并且与比上赛季更弱的竞争者对抗。在此处注册我们的免费通讯阿森纳在英超联赛排行榜上占据三分。" data-title="Arsenal have everything they need to repeat as Premier League champions | Jonathan Wilson" data-date="11-02 23:47" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 23:47</span>
          <span class="news-item-title">阿森纳拥有成为英超冠军所需的一切|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Arsenal have everything they need to repeat as Premier League champions | Jonathan Wilson</span>
          <span class="news-value-point">💡 周日在利物浦的胜利表明，枪手更深入，更有经验，并且与比上赛季更弱的竞争者对抗</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13607004/beat-luke-littler-fallon-sherrock-should-not-have-been-selected-to-play-in-netflix-show-but-you-cant-blame-queen-of-the-palace" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育专家马克·韦伯斯特（ Mark Webster ）表示，法伦·谢罗克（ Fallon Sherrock ） “不应该被选中”为Netflix的“击败卢克·利特勒” （ Beat Luke Littler ）效力，她赢得了£ 501,000的奖金。" data-title="Sherrock &#39;should not have been selected to play&#39; for Beat Luke Littler show" data-date="11-02 23:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 23:45</span>
          <span class="news-item-title">Sherrock “不应该被选中参加” Beat Luke Littler节目</span>
          <span class="news-item-title-en">Sherrock 'should not have been selected to play' for Beat Luke Littler show</span>
          <span class="news-value-point">💡 天空体育专家马克·韦伯斯特（ Mark Webster ）表示，法伦·谢罗克（ Fallon Sherrock ） “不应该被选中”为Netfl…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13607133/oliver-glasner-nottingham-forest-hierarchy-welcome-strong-reaction-from-head-coach-after-brentford-defeat" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻了解到，奥利弗·格拉斯纳（ Oliver Glasner ）对他的团队的强硬言论受到了诺丁汉森林体系中许多人的欢迎。" data-title="Forest hierarchy welcome Glasner&#39;s strong words after Brentford loss" data-date="11-02 22:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 22:45</span>
          <span class="news-item-title">森林等级制度欢迎格拉斯纳在布伦特福德失利后的强硬言论</span>
          <span class="news-item-title-en">Forest hierarchy welcome Glasner's strong words after Brentford loss</span>
          <span class="news-value-point">💡 天空体育新闻了解到，奥利弗·格拉斯纳（ Oliver Glasner ）对他的团队的强硬言论受到了诺丁汉森林体系中许多人的欢迎</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607133/oliver-glasner-nottingham-forest-hierarchy-welcome-strong-reaction-from-head-coach-after-brentford-defeat" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻了解到，奥利弗·格拉斯纳（ Oliver Glasner ）对他的团队的强硬言论受到了诺丁汉森林体系中许多人的欢迎。" data-title="Forest hierarchy welcome Glasner&#39;s strong words after Brentford loss" data-date="11-02 22:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 22:45</span>
          <span class="news-item-title">森林等级制度欢迎格拉斯纳在布伦特福德失利后的强硬言论</span>
          <span class="news-item-title-en">Forest hierarchy welcome Glasner's strong words after Brentford loss</span>
          <span class="news-value-point">💡 天空体育新闻了解到，奥利弗·格拉斯纳（ Oliver Glasner ）对他的团队的强硬言论受到了诺丁汉森林体系中许多人的欢迎</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724985.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网首尔11月2日电 (记者 金旭)当地时间11月1日，首届“中韩大学生校园足球友谊赛”决赛及闭幕式在韩国京畿大学举行。中国驻韩国大使馆公使包旭辉为获奖代表颁奖并致辞，中国驻韩国大使馆公使衔参赞马贵生及中韩有关机构代表、参赛球员、高校师生200多人参加。" data-title="首届“中韩大学生校园足球友谊赛”落幕" data-date="11-02 21:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 21:48</span>
          <span class="news-item-title">首届“中韩大学生校园足球友谊赛”落幕</span>
          <span class="news-value-point">💡 中新网首尔11月2日电 (记者 金旭)当地时间11月1日，首届“中韩大学生校园足球友谊赛”决赛及闭幕式在韩国京畿大学举行</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13607007/harriet-dart-former-wimbledon-champion-marion-bartoli-on-pushing-brit-beyond-her-limits-after-maiden-wta-title" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前温布尔登网球公开赛冠军和天空体育分析师马里昂·巴托利（ Marion Bartoli ）承认，这位英国人周末在中国广州公开赛上赢得了她的第一个WTA冠军，推动哈丽特·达特（ Harriet Dart ） “超越了她的极限”。" data-title="Former Wimbledon champion Bartoli pushing Dart &#39;beyond her limits&#39;" data-date="11-02 20:48" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 20:48</span>
          <span class="news-item-title">前温布尔登网球公开赛冠军巴托利推动飞镖“超越极限”</span>
          <span class="news-item-title-en">Former Wimbledon champion Bartoli pushing Dart 'beyond her limits'</span>
          <span class="news-value-point">💡 前温布尔登网球公开赛冠军和天空体育分析师马里昂·巴托利（ Marion Bartoli ）承认，这位英国人周末在中国广州公开赛上赢得了她的第一个…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj75pglrq794o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰主教练雷吉斯·勒布里斯（ Regis le Bris ）将获得更多时间来扭转局面，尽管他的球队在英超赛季的开局不佳。" data-title="Bottom club Sunderland to stick with manager Le Bris" data-date="11-02 20:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 20:04</span>
          <span class="news-item-title">BOTTOM CLUB SUNDERLAND与经理Le Bris共舞</span>
          <span class="news-item-title-en">Bottom club Sunderland to stick with manager Le Bris</span>
          <span class="news-value-point">💡 桑德兰主教练雷吉斯·勒布里斯（ Regis le Bris ）将获得更多时间来扭转局面，尽管他的球队在英超赛季的开局不佳</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmx285n4l81lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉不会对Jamie Carragher采取任何法律行动。" data-title="Villa drop legal action threat against Carragher" data-date="11-02 19:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 19:49</span>
          <span class="news-item-title">针对Carragher的Villa Drop法律诉讼威胁</span>
          <span class="news-item-title-en">Villa drop legal action threat against Carragher</span>
          <span class="news-value-point">💡 阿斯顿维拉不会对Jamie Carragher采取任何法律行动</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607031/man-utd-will-be-in-premier-league-relegation-zone-in-december-says-paul-merson-as-michael-carricks-side-hit-by-poor-recruitment" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="保罗·默森（ Paul Merson ）带着他最新的天空体育专栏回来，谴责曼联最近的形式，并对他们即将到来的前景做出严峻的预测。" data-title="Merse: Man Utd will be in relegation zone in a month" data-date="11-02 19:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 19:20</span>
          <span class="news-item-title">Merse ：曼联将在一个月内进入降级区</span>
          <span class="news-item-title-en">Merse: Man Utd will be in relegation zone in a month</span>
          <span class="news-value-point">💡 保罗·默森（ Paul Merson ）带着他最新的天空体育专栏回来，谴责曼联最近的形式，并对他们即将到来的前景做出严峻的预测</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/02/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Marco Rose的战术提升了伯恩茅斯， Roméo Lavia在切尔西取得了进步， Roberto De Zerbi为年轻人提供了马刺的机会。良好的防守是冠军的标志。在安菲尔德，阿森纳在过去的13次访问中没有获胜， Mikel Arteta" data-title="Premier League: 10 talking points from the weekend’s action" data-date="11-02 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 16:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 Marco Rose的战术提升了伯恩茅斯， Roméo Lavia在切尔西取得了进步， Roberto De Zerbi为年轻人提供了马刺的机会</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/01/andoni-iraola-responds-liverpool-penalty-denial-arsenal-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理对裁判驳回的两项罚款索赔表示遗憾伊拉奥拉抱怨“如果你不下去，你就不叫它‘安东尼·伊拉奥拉说，在亚历山大·伊萨克（ Alexander Isak ）在阿森期间被拒绝罚款后，他将指示利物浦球员将来进入禁区" data-title="‘We have to tell them to go down’: Iraola responds to Isak penalty denial for Liverpool" data-date="11-02 05:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 05:25</span>
          <span class="news-item-title">“我们必须告诉他们失败” ：伊拉奥拉回应伊萨克对利物浦的罚款否认</span>
          <span class="news-item-title-en">‘We have to tell them to go down’: Iraola responds to Isak penalty denial for Liverpool</span>
          <span class="news-value-point">💡 经理对裁判驳回的两项罚款索赔表示遗憾伊拉奥拉抱怨“如果你不下去，你就不叫它‘安东尼·伊拉奥拉说，在亚历山大·伊萨克（ Alexander Isa…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvp8grpjk4leo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安东尼·伊拉奥拉（ Andoni Iraola ）表示，在利物浦在周日被阿森纳击败后被罚下场后，他将告诉他的球员们将来会倒下。" data-title="I&#39;ll tell my players to dive in future" data-date="11-02 05:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 05:00</span>
          <span class="news-item-title">我会告诉我的玩家将来潜水</span>
          <span class="news-item-title-en">I'll tell my players to dive in future</span>
          <span class="news-value-point">💡 安东尼·伊拉奥拉（ Andoni Iraola ）表示，在利物浦在周日被阿森纳击败后被罚下场后，他将告诉他的球员们将来会倒下</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c39wz2epven4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳从二级联赛弗利特伍德的失利低点反弹回来，确保了他们在安菲尔德14年来的首次胜利-并在英超联赛的顶端开启了三分领先优势。" data-title="From Fleetwood embarrassment to &#39;magical&#39; Anfield win 14 years in making" data-date="11-02 04:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 04:16</span>
          <span class="news-item-title">从Fleetwood的尴尬到“神奇”的安菲尔德赢得了14年的制作经验</span>
          <span class="news-item-title-en">From Fleetwood embarrassment to 'magical' Anfield win 14 years in making</span>
          <span class="news-value-point">💡 阿森纳从二级联赛弗利特伍德的失利低点反弹回来，确保了他们在安菲尔德14年来的首次胜利-并在英超联赛的顶端开启了三分领先优势</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/cmly09yv9xl6o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳自2012年以来首次在安菲尔德获胜，在一场端到端的比赛之后，在安菲尔德获得了三分领先优势，这让利物浦对一无所获感到沮丧。" data-title="Arsenal move clear at the top with a rare win at Liverpool" data-date="11-02 04:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 04:00</span>
          <span class="news-item-title">阿森纳凭借在利物浦的罕见胜利在顶部清除</span>
          <span class="news-item-title-en">Arsenal move clear at the top with a rare win at Liverpool</span>
          <span class="news-value-point">💡 阿森纳自2012年以来首次在安菲尔德获胜，在一场端到端的比赛之后，在安菲尔德获得了三分领先优势，这让利物浦对一无所获感到沮丧</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/01/liverpool-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kai Havertz的目标足以让阿森纳自2012年9月以来首次在安菲尔德取得胜利，并让他们在积分榜上获得三分。那么比赛在哪里？当阿森纳拿到球时，利物浦将寻求让球员绕过球，" data-title="Liverpool 0-1 Arsenal: Premier League – as it happened" data-date="11-02 02:55" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 02:55</span>
          <span class="news-item-title">利物浦0-1阿森纳：英超联赛–事实如此</span>
          <span class="news-item-title-en">Liverpool 0-1 Arsenal: Premier League – as it happened</span>
          <span class="news-value-point">💡 Kai Havertz的目标足以让阿森纳自2012年9月以来首次在安菲尔德取得胜利，并让他们在积分榜上获得三分</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/02/well/kratom-wellness-marketing-addiction.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="有些人说，他们是通过健康播客、健身房的免费样品或健身影响者来介绍这种药物的。" data-title="They Tried Kratom for Its Health Benefits, Then They Became Addicted" data-date="11-03 01:11" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-03 01:11</span>
          <span class="news-item-title">他们尝试了Kratom的健康益处，然后他们上瘾了</span>
          <span class="news-item-title-en">They Tried Kratom for Its Health Benefits, Then They Became Addicted</span>
          <span class="news-value-point">💡 有些人说，他们是通过健康播客、健身房的免费样品或健身影响者来介绍这种药物的</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1024496/apple-homeview-ultra-robot-rumor-delay" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据The Information报道，据报道，苹果公司已将其传闻中的智能家居机器人推迟到明年最早推出，甚至可能推迟到2028年。它说机器人的硬件“已经完成了大约两年” ，但软件" data-title="Apple’s ‘Ultra’ smart home robot might have to wait until 2028" data-date="11-03 01:06" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-03 01:06</span>
          <span class="news-item-title">苹果的“Ultra”智能家居机器人可能需要等到2028年</span>
          <span class="news-item-title-en">Apple’s ‘Ultra’ smart home robot might have to wait until 2028</span>
          <span class="news-value-point">💡 据The Information报道，据报道，苹果公司已将其传闻中的智能家居机器人推迟到明年最早推出，甚至可能推迟到2028年</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13606955/canelo-alvarez-could-have-influenced-referee-in-christian-mbilli-fight-says-promoter-camille-estephan" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡内洛·阿尔瓦雷斯（ Canelo Alvarez ）本可以“影响”裁判，在他们的世界冠军争夺战中从克里斯蒂安·姆比利（ Christian Mbilli ）身上拿下一分， Mbilli的发起人卡米尔·埃斯特凡（" data-title="Canelo could have ‘influenced’ referee, says Mbilli’s team" data-date="11-03 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 01:00</span>
          <span class="news-item-title">Mbilli的团队表示， Canelo本可以“影响”裁判</span>
          <span class="news-item-title-en">Canelo could have ‘influenced’ referee, says Mbilli’s team</span>
          <span class="news-value-point">💡 卡内洛·阿尔瓦雷斯（ Canelo Alvarez ）本可以“影响”裁判，在他们的世界冠军争夺战中从克里斯蒂安·姆比利（ Christian M…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1024447/squarespace-layoffs-19-percent" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Squarespace发言人Jeff Seedman在给The Verge的一份声明中表示， Squarespace正在努力“简化”其运营，网站建设平台Squarespace正在裁员19%的员工。裁员将影响大约300个Squarespace的" data-title="Squarespace is laying off 19 percent of employees" data-date="11-03 00:50" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-03 00:50</span>
          <span class="news-item-title">Squarespace将裁员19%</span>
          <span class="news-item-title-en">Squarespace is laying off 19 percent of employees</span>
          <span class="news-value-point">💡 Squarespace发言人Jeff Seedman在给The Verge的一份声明中表示， Squarespace正在努力“简化”其运营，网站…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/creality-k3-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Creality的四色换刀器不错，但为时已晚吗？" data-title="Creality K3 Review: It’s a Tool Changer, not a game changer" data-date="11-03 00:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-03 00:40</span>
          <span class="news-item-title">Creality K3评论：这是一个工具改变者，而不是游戏规则改变者</span>
          <span class="news-item-title-en">Creality K3 Review: It’s a Tool Changer, not a game changer</span>
          <span class="news-value-point">💡 Creality的四色换刀器不错，但为时已晚吗</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/elon-musk-throttles-grok-bot-limits-due-to-unsustainably-high-costs/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="马斯克最近将Grok Bot称为“我一生中见过的产品中增长最快的产品”。" data-title="Elon Musk throttles Grok Bot limits due to ‘unsustainably high’ costs" data-date="11-03 00:23" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 00:23</span>
          <span class="news-item-title">埃隆·马斯克（ Elon Musk ）因“不可持续的高成本”而限制了Grok Bot的限制</span>
          <span class="news-item-title-en">Elon Musk throttles Grok Bot limits due to ‘unsustainably high’ costs</span>
          <span class="news-value-point">💡 马斯克最近将Grok Bot称为“我一生中见过的产品中增长最快的产品”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/02/us/nathalia-filgueiras-florida-plane-crash-pilot.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="她的母亲在接受采访时说， Nathalia Filgueiras在17岁时获得了飞行员执照，飞行时间超过1300小时，并且是周日的副驾驶。" data-title="20-Year-Old Nathalia Filgueiras Was a Pilot on Learjet That Crashed in Florida" data-date="11-03 00:19" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-03 00:19</span>
          <span class="news-item-title">20岁的纳塔莉亚·菲尔格拉斯（ Nathalia Filgueiras ）是佛罗里达州坠毁的里尔喷气式飞机的飞行员</span>
          <span class="news-item-title-en">20-Year-Old Nathalia Filgueiras Was a Pilot on Learjet That Crashed in Florida</span>
          <span class="news-value-point">💡 她的母亲在接受采访时说， Nathalia Filgueiras在17岁时获得了飞行员执照，飞行时间超过1300小时，并且是周日的副驾驶</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/raspberry-pi/16gb-raspberry-pi-5-hiked-to-usd385-more-than-triple-its-launch-price-makers-are-already-shifting-to-pico-esp32-for-small-projects-mini-pcs-for-more-ambitious-tasks" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Raspberry Pi 16GB的价格上涨了80 $至385 $。现在它的价格是2025年1月推出价格的三倍多。" data-title="16GB Raspberry Pi 5 hiked to $385, more than triple its launch price — makers are already shifting to Pico/ESP32 for small projects, mini PCs for more ambitious tasks" data-date="11-03 00:17" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-03 00:17</span>
          <span class="news-item-title">16GB Raspberry Pi 5升至385 $ ，是其推出价格的三倍多—制造商已经转向Pico/ESP32用于小型项目，迷你PC用于更雄心勃勃的任务</span>
          <span class="news-item-title-en">16GB Raspberry Pi 5 hiked to $385, more than triple its launch price — makers are already shifting to Pico/ESP32 for small projects, mini PCs for more ambitious tasks</span>
          <span class="news-value-point">💡 Raspberry Pi 16GB的价格上涨了80 $至385 $</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1024228/matt-strauss-nbc-univerisal-versant-comcast-peacock-streaming-tv" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，我正在和Matt Strauss谈话，他现在是NBC环球媒体集团的主席。这是Matt第二次和我一起参加这个节目，自从他和我上次合作以来， NBCU的组织和结构发生了很大的变化。" data-title="Why Peacock is making a huge bet on YouTube" data-date="11-03 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-03 00:00</span>
          <span class="news-item-title">为什么孔雀在YouTube上下了巨大的赌注</span>
          <span class="news-item-title-en">Why Peacock is making a huge bet on YouTube</span>
          <span class="news-value-point">💡 今天，我正在和Matt Strauss谈话，他现在是NBC环球媒体集团的主席</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10725079.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国地震台网正式测定：11月2日23时35分，在西藏那曲市巴青县(北纬32.38度，东经93.86度)发生4.2级地震，震源深度10公里。" data-title="西藏那曲市巴青县发生4.2级地震" data-date="11-02 23:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 23:49</span>
          <span class="news-item-title">西藏那曲市巴青县发生4.2级地震</span>
          <span class="news-value-point">💡 中国地震台网正式测定：11月2日23时35分，在西藏那曲市巴青县(北纬32.38度，东经93.86度)发生4.2级地震，震源深度10公里</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/280.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，据《The Information》今日报道，苹果正在开发 HomeView 的机器人版本。这款设备传闻被称作“HomeView Ultra”或“HomeView Max”，不过最终命名尚不确定。记者艾伦・蒂利（Aaron Tilley）表示，该设备原型机将一块 9 英寸屏幕搭载在可旋转机械臂上，整体外观类似苹果早年的 iMac G4，或是皮克斯的经典台灯吉祥物。它保留 FaceTime 通话这类 HomeView 已有的常规功能，同时还能够充分感知周边环境，并自主执行操作。▲ 苹果首款智能家庭中枢 HomeView报道写道：“这款机器人当前的设计方案，计划依靠摄像头与各类传感器感知周遭环境、自主行动。比如有人走进房间，设备可以自动开灯；甚至还能尝试把猫咪从桌" data-title="消息称 HomeView Ultra 硬件已定型两年，但苹果内部仍存在“分歧”" data-date="11-02 23:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 23:40</span>
          <span class="news-item-title">消息称 HomeView Ultra 硬件已定型两年，但苹果内部仍存在“分歧”</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，据《The Information》今日报道，苹果正在开发 HomeView 的机器人版本</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/us/learjet-crash-florida-palm-beach.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="周日，一架小型喷气式飞机坠落地面，爆炸成火球，机上所有人死亡。当局没有立即公布有关受害者的信息。" data-title="What to Know About the Florida Plane Crash That Killed 9" data-date="11-02 23:29" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 23:29</span>
          <span class="news-item-title">关于造成9人死亡的佛罗里达州飞机失事的须知事项</span>
          <span class="news-item-title-en">What to Know About the Florida Plane Crash That Killed 9</span>
          <span class="news-value-point">💡 周日，一架小型喷气式飞机坠落地面，爆炸成火球，机上所有人死亡</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/279.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，韩国起亚汽车今日公告，2026 年 10 月，起亚在全球市场销售 291,219 辆，其中韩国国内 51,007 辆，其他 239,308 辆，904 辆专用单位，同比增长 10.3%。（基于批发销售）具体数据如下：全球市场总销量达到 291,219 辆，较上一年增长 10.3%韩国国内市场售出 51,007 辆，较上一年增长 27.5%其他市场销量 239,308 辆，较上一年增长 7.2%起亚汽车此前发布 2026 财年（2026 年 1 月～2026 年 12 月）前三季度（2026 年 1 月～2026 年 9 月）业绩快报及第三财季（2026 年 7 月～2026 年 9 月）业绩快报报告：2026 财年前三季度营业总收入：94.14 万亿韩元（IT" data-title="起亚汽车 10 月全球总销量达到 29.12 万辆，同比增长 10.3%" data-date="11-02 23:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 23:19</span>
          <span class="news-item-title">起亚汽车 10 月全球总销量达到 29.12 万辆，同比增长 10.3%</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，韩国起亚汽车今日公告，2026 年 10 月，起亚在全球市场销售 291,219 辆，其中韩国国内 51,007…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一个新网站旨在提取超过410个地方政府对社区数据中心的10,000多条公众意见，人们的共识是人们一点也不喜欢它们。" data-title="&#39;America hates data centers&#39; — New data highlights public sentiment" data-date="11-02 23:19" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-02 23:19</span>
          <span class="news-item-title">“美国讨厌数据中心” --新数据凸显公众情绪</span>
          <span class="news-item-title-en">'America hates data centers' — New data highlights public sentiment</span>
          <span class="news-value-point">💡 一个新网站旨在提取超过410个地方政府对社区数据中心的10,000多条公众意见，人们的共识是人们一点也不喜欢它们</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1023131/vivo-x500-pro-max-review-cameras-specs-price" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年春天，当我宣布Vivo的X300 Ultra拥有任何手机中最好的相机时，有两件事让我印象深刻：其出色的主相机具有窄35毫米焦距，以及在任何手机世界中仍然是最强大的超宽" data-title="Vivo’s first Pro Max phone proves its Ultra is still in a league of its own" data-date="11-02 23:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-02 23:15</span>
          <span class="news-item-title">Vivo的首款Pro Max手机证明其Ultra仍处于自己的联赛中</span>
          <span class="news-item-title-en">Vivo’s first Pro Max phone proves its Ultra is still in a league of its own</span>
          <span class="news-value-point">💡 今年春天，当我宣布Vivo的X300 Ultra拥有任何手机中最好的相机时，有两件事让我印象深刻：其出色的主相机具有窄35毫米焦距，以及在任何手…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-03 01:19（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
