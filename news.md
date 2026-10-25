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
      <span>2026-10-25 20:41 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-25/10720815.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社江苏苏州10月25日电 (记者 张杨彬)大陆涉台学者25日接受中新社采访时表示，中美作为二战盟友的历史连接，将推动两国共同维护战后国际秩序，这段历史像“笼子”一样框住了“台独”。" data-title="学者：中美作为二战盟友的历史框住了“台独”" data-date="10-25 20:40" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-25 20:40</span>
      </div>
      <h2 class="hero-featured-title">学者：中美作为二战盟友的历史框住了“台独”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/684.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 25 日消息，欧洲 CPU 初创企业 SiPearl 本月 22 日宣布与中国台湾地区芯片 IP 与设计服务企业神盾 (Egis) 签署战略合作与投资协议。SiPearl 的下代处理器 Rhea2 将基于其同神盾下属安国 (Alcor Micro) 合作开发的 Mobius100 服务器 CPU 同款架构。而 Mobius100 则基于 Arm Neoverse V3 建构，采用台积电 N3P 工艺制程，通过双芯粒封装提供 128+12 个核心（IT之家注：12 个为冗余），支持 12800MT/s 的 DDR5 MRDIMM，提供 PCIe Gen6 / CXL Gen3 通道，同时利用神盾下属干瞻 (InPsytech) 的 IP 提供 8 个 UCIe 2.0-S" data-title="欧洲 CPU 初创企业 SiPearl 将与神盾合作开发下代处理器 Rhea2" data-date="10-25 20:18" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">欧洲 CPU 初创企业 SiPearl 将与神盾合作开发下代处理器 Rhea2</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/25/manchester-united-v-bournemouth-liverpool-v-brighton-and-more-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="格林尼治标准时间下午2点⚽️现场记分牌上的⚽️英超联赛最新消息|向丹尼尔发送电子邮件来自老特拉福德的DanielReports ，由Sky广播，告知我们布鲁诺·费尔南德斯已被迈克尔·卡里克（ Michael Carrick ）淘汰。我们不知道这是一贯糟糕的形式还是英里" data-title="Manchester United v Bournemouth, Liverpool v Brighton and more: clockwatch" data-date="10-25 20:38" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Manchester United v Bournemouth, Liverpool v Brighton and more: clockwatch</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-25/10720825.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广西崇左10月25日电(记者 林艳华)10月24日，2026第八届大新明仕田园丰收节在广西崇左市开幕。活动以“欢乐田园，自在明仕”为主题，立足中越边境区位特色、深挖壮族民俗文脉，以节庆礼赞农耕丰收，邀请八方游客与壮乡民众共庆丰年、共享秋日喜悦。" data-title="边关稻熟壮乡风情醉游人 广西大新明仕田园丰收节启幕" data-date="10-25 20:32" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">边关稻熟壮乡风情醉游人 广西大新明仕田园丰收节启幕</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720815.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社江苏苏州10月25日电 (记者 张杨彬)大陆涉台学者25日接受中新社采访时表示，中美作为二战盟友的历史连接，将推动两国共同维护战后国际秩序，这段历史像“笼子”一样框住了“台独”。" data-title="学者：中美作为二战盟友的历史框住了“台独”" data-date="10-25 20:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:40</span>
          <span class="news-item-title">学者：中美作为二战盟友的历史框住了“台独”</span>
          <span class="news-value-point">💡 中新社江苏苏州10月25日电 (记者 张杨彬)大陆涉台学者25日接受中新社采访时表示，中美作为二战盟友的历史连接，将推动两国共同维护战后国际秩序…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720799.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河北雄安10月25日电 (记者 曾玥 周昕)记者25日从中国人民外交学会在河北雄安新区举行的2026全球治理论坛(雄安)闭幕新闻发布会上获悉，《论坛愿景文件》发布。文件指出，要支持全球南方国家更加深入参与国际规则制定、议程设置和决策进程，提升全球南方国家在国际事务中的发言权和代表性。" data-title="全球治理论坛发布愿景文件 呼吁提升全球南方国家发言权和代表性" data-date="10-25 20:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:12</span>
          <span class="news-item-title">全球治理论坛发布愿景文件 呼吁提升全球南方国家发言权和代表性</span>
          <span class="news-value-point">💡 中新社河北雄安10月25日电 (记者 曾玥 周昕)记者25日从中国人民外交学会在河北雄安新区举行的2026全球治理论坛(雄安)闭幕新闻发布会上获…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720807.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月25日上午8时，巴西总统选举开始第二轮投票，选民将在劳工党候选人、现任总统卢拉和自由党候选人、前总统雅伊尔·博索纳罗之子弗拉维奥·博索纳罗之间选出下任总统。" data-title="巴西总统选举第二轮投票开始" data-date="10-25 20:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:08</span>
          <span class="news-item-title">巴西总统选举第二轮投票开始</span>
          <span class="news-value-point">💡 当地时间10月25日上午8时，巴西总统选举开始第二轮投票，选民将在劳工党候选人、现任总统卢拉和自由党候选人、前总统雅伊尔·博索纳罗之子弗拉维奥·…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720793.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社福州10月25日电 (记者 朱贺 刘子衿)10月25日是台湾光复纪念日。台湾光复纪念协会秘书长丘智贤在福建福州表示，该协会正在规划设计台湾光复故事馆以保存史料，让青年了解先辈为国家民族奋斗的历史。" data-title="台湾各界人士盼青年探寻历史真相" data-date="10-25 19:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:51</span>
          <span class="news-item-title">台湾各界人士盼青年探寻历史真相</span>
          <span class="news-value-point">💡 中新社福州10月25日电 (记者 朱贺 刘子衿)10月25日是台湾光复纪念日</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720787.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：“《习近平党建文选》金句”系列之六：理论强，才能方向明人心齐底气足" data-title="理论强，才能方向明人心齐底气足" data-date="10-25 19:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:50</span>
          <span class="news-item-title">理论强，才能方向明人心齐底气足</span>
          <span class="news-value-point">💡 原标题：“《习近平党建文选》金句”系列之六：理论强，才能方向明人心齐底气足</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720782.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在纪念中国工农红军长征胜利90周年大会上，习近平总书记回顾我们党领导红军进行长征的伟大历程，就弘扬伟大长征精神、走好新的长征路提出明确要求。铭记历史方能开创未来。让我们一起重温总书记重要讲话中讲到的长征故事，弘扬伟大长征精神，在新的长征路上奋力创造新的辉煌！" data-title="纪念大会上，总书记讲到的长征故事催人奋进" data-date="10-25 19:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:49</span>
          <span class="news-item-title">纪念大会上，总书记讲到的长征故事催人奋进</span>
          <span class="news-value-point">💡 在纪念中国工农红军长征胜利90周年大会上，习近平总书记回顾我们党领导红军进行长征的伟大历程，就弘扬伟大长征精神、走好新的长征路提出明确要求</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720781.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社台北10月25日电 (记者 路梅)时值抗日战争胜利暨台湾光复81周年，统一联盟党、台湾劳动党、台湾地区政治受难人互助会等20余个台湾民间团体25日在台北中山堂前方的广场举办纪念活动，发出反对日本军国主义扩张、反对“台独”、守护和平的呼声。" data-title="台湾民间团体纪念台湾光复81周年" data-date="10-25 19:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:45</span>
          <span class="news-item-title">台湾民间团体纪念台湾光复81周年</span>
          <span class="news-value-point">💡 中新社台北10月25日电 (记者 路梅)时值抗日战争胜利暨台湾光复81周年，统一联盟党、台湾劳动党、台湾地区政治受难人互助会等20余个台湾民间团…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720757.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月25日电 据安徽省纪委监委消息：日前，经中共安徽省委批准，安徽省纪委监委对蚌埠市人大常委会原党组副书记、副主任高尚严重违纪违法问题进行了立案审查调查。" data-title="安徽省蚌埠市人大常委会原副主任高尚被开除党籍" data-date="10-25 19:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:36</span>
          <span class="news-item-title">安徽省蚌埠市人大常委会原副主任高尚被开除党籍</span>
          <span class="news-value-point">💡 中新网10月25日电 据安徽省纪委监委消息：日前，经中共安徽省委批准，安徽省纪委监委对蚌埠市人大常委会原党组副书记、副主任高尚严重违纪违法问题进…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720739.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月25日电 综合消息：也门胡塞武装25日发布警告称，位于沙特阿拉伯首都利雅得的哈立德国王国际机场仍是其军事打击目标，禁止前往和使用。该机场24日晚发布通知，宣布25日恢复开放部分航站楼。" data-title="沙特首都机场拟恢复运营 也门胡塞武装紧急警告" data-date="10-25 19:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:27</span>
          <span class="news-item-title">沙特首都机场拟恢复运营 也门胡塞武装紧急警告</span>
          <span class="news-value-point">💡 中新社北京10月25日电 综合消息：也门胡塞武装25日发布警告称，位于沙特阿拉伯首都利雅得的哈立德国王国际机场仍是其军事打击目标，禁止前往和使用</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/25/us/politics/latino-voters-poll-midterm-elections.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="拉丁裔帮助推动特朗普总统重返白宫。但民主党在过去两年中赢得了许多西班牙裔选民的信任。" data-title="Latinos Are Now America’s Most Important Swing Voters" data-date="10-25 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 17:01</span>
          <span class="news-item-title">拉美裔现在是美国最重要的摇摆选民</span>
          <span class="news-item-title-en">Latinos Are Now America’s Most Important Swing Voters</span>
          <span class="news-value-point">💡 拉丁裔帮助推动特朗普总统重返白宫</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/25/world/middleeast/israels-high-stakes-election-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="以色列人将于周二前往投票站进行选举，以决定该国的下一任总理。但组建新政府可能需要数周、数月或更长时间。" data-title="Israel’s High-Stakes Election: What to Know" data-date="10-25 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 17:01</span>
          <span class="news-item-title">以色列高风险选举：须知</span>
          <span class="news-item-title-en">Israel’s High-Stakes Election: What to Know</span>
          <span class="news-value-point">💡 以色列人将于周二前往投票站进行选举，以决定该国的下一任总理</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720710.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月25日电 综合外媒报道，美国将于11月3日迎来中期选举，共和党和民主党两大阵营加大造势和拉票力度。" data-title="隔空互怼！奥巴马批评：现任美国政府造成混乱局面 特朗普回击：“你的集会现场空荡荡”" data-date="10-25 15:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:42</span>
          <span class="news-item-title">隔空互怼！奥巴马批评：现任美国政府造成混乱局面 特朗普回击：“你的集会现场空荡荡”</span>
          <span class="news-value-point">💡 中新网10月25日电 综合外媒报道，美国将于11月3日迎来中期选举，共和党和民主党两大阵营加大造势和拉票力度</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720701.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社巴黎10月25日电 (记者 李洋)法国当地时间24日出现新一轮全国性抗议示威活动，仍有数十万人参与。法国官方称，已有近千人被捕。" data-title="法国新一轮抗议示威活动有近千人被捕" data-date="10-25 15:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:37</span>
          <span class="news-item-title">法国新一轮抗议示威活动有近千人被捕</span>
          <span class="news-value-point">💡 中新社巴黎10月25日电 (记者 李洋)法国当地时间24日出现新一轮全国性抗议示威活动，仍有数十万人参与</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720698.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社悉尼10月25日电 (记者 薄雯雯)澳大利亚昆士兰州洛根市24日晚发生枪击事件，造成4人受伤，其中1人伤势危重。当地警方25日表示，至少3名涉案嫌疑人仍在逃。" data-title="澳大利亚昆州发生枪击事件致4人受伤" data-date="10-25 15:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:36</span>
          <span class="news-item-title">澳大利亚昆州发生枪击事件致4人受伤</span>
          <span class="news-value-point">💡 中新社悉尼10月25日电 (记者 薄雯雯)澳大利亚昆士兰州洛根市24日晚发生枪击事件，造成4人受伤，其中1人伤势危重</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720679.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河北雄安10月25日电 题：专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果" data-title="专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果" data-date="10-25 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:35</span>
          <span class="news-item-title">专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果</span>
          <span class="news-value-point">💡 中新社河北雄安10月25日电 题：专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/684.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 25 日消息，欧洲 CPU 初创企业 SiPearl 本月 22 日宣布与中国台湾地区芯片 IP 与设计服务企业神盾 (Egis) 签署战略合作与投资协议。SiPearl 的下代处理器 Rhea2 将基于其同神盾下属安国 (Alcor Micro) 合作开发的 Mobius100 服务器 CPU 同款架构。而 Mobius100 则基于 Arm Neoverse V3 建构，采用台积电 N3P 工艺制程，通过双芯粒封装提供 128+12 个核心（IT之家注：12 个为冗余），支持 12800MT/s 的 DDR5 MRDIMM，提供 PCIe Gen6 / CXL Gen3 通道，同时利用神盾下属干瞻 (InPsytech) 的 IP 提供 8 个 UCIe 2.0-S" data-title="欧洲 CPU 初创企业 SiPearl 将与神盾合作开发下代处理器 Rhea2" data-date="10-25 20:18" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 20:18</span>
          <span class="news-item-title">欧洲 CPU 初创企业 SiPearl 将与神盾合作开发下代处理器 Rhea2</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，欧洲 CPU 初创企业 SiPearl 本月 22 日宣布与中国台湾地区芯片 IP 与设计服务企业神盾 (Eg…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/column/1017983/google-ai-search-online-publishing" target="_blank" rel="noopener" data-cat="keji" data-summary="The Stepback是一份每周时事通讯，详细介绍了科技界的一个重要故事。有关人工智能对网络影响的更多信息，请关注Emma Roth。Stepback将于美国东部时间周日上午8点到达订阅者的收件箱。选择加入The Stepback he" data-title="Google’s AI search changes upended online publishing" data-date="10-25 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 20:00</span>
          <span class="news-item-title">谷歌的人工智能搜索变革颠覆了在线发布</span>
          <span class="news-item-title-en">Google’s AI search changes upended online publishing</span>
          <span class="news-value-point">💡 The Stepback是一份每周时事通讯，详细介绍了科技界的一个重要故事</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-isolated-red-team-ai-agents-built-a-hidden-cpu-cache-channel-to-talk-with-no-network-or-shared-files-exploited-cpu-cache-timing-to-bypass-microvm-sandboxes" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI的红队代理通过CPU缓存传递隐藏消息，这是在云虚拟机之间移动数据的秘密技巧。" data-title="OpenAI&#39;s isolated red-team agents built a hidden CPU cache channel to talk with no network or shared files" data-date="10-25 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 19:30</span>
          <span class="news-item-title">OpenAI隔离的红队代理构建了一个隐藏的CPU缓存通道，可以在没有网络或共享文件的情况下进行通话</span>
          <span class="news-item-title-en">OpenAI's isolated red-team agents built a hidden CPU cache channel to talk with no network or shared files</span>
          <span class="news-value-point">💡 OpenAI的红队代理通过CPU缓存传递隐藏消息，这是在云虚拟机之间移动数据的秘密技巧</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/amd-ceo-lisa-su-proposed-bringing-back-the-ryzen-7-5800x3d-set-plan-in-motion-before-ddr5-shortages-am4-cpu-considered-a-final-gift-to-loyal-fans-of-the-decade-old-socket" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD总监Travis Kirsch证实了重新推出第一款X3D芯片的理由，并解释了为什么该公司不再提供许多Ryzen 3 SKU。" data-title="AMD CEO Lisa Su proposed bringing back the Ryzen 7 5800X3D, set plan in motion before DDR5 shortages" data-date="10-25 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 19:00</span>
          <span class="news-item-title">AMD首席执行官Lisa Su提议带回Ryzen 7 5800X3D ，在DDR5短缺之前制定计划</span>
          <span class="news-item-title-en">AMD CEO Lisa Su proposed bringing back the Ryzen 7 5800X3D, set plan in motion before DDR5 shortages</span>
          <span class="news-value-point">💡 AMD总监Travis Kirsch证实了重新推出第一款X3D芯片的理由，并解释了为什么该公司不再提供许多Ryzen 3 SKU</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达和PreussenElektra正在研究德国核电站的退役场地是否可以重新用作人工智能数据中心，通过重复利用现有的电网连接、土地和工业基础设施来缩短开发时间。" data-title="Nvidia eyes converting old nuclear plants into massive AI data centers" data-date="10-25 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 18:30</span>
          <span class="news-item-title">英伟达着眼于将旧核电站转变为大型人工智能数据中心</span>
          <span class="news-item-title-en">Nvidia eyes converting old nuclear plants into massive AI data centers</span>
          <span class="news-value-point">💡 英伟达和PreussenElektra正在研究德国核电站的退役场地是否可以重新用作人工智能数据中心，通过重复利用现有的电网连接、土地和工业基础设…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/600.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 25 日消息，据 SteamDB 数据，《赛博朋克 2077》游戏 2.5 版本更新后，Steam 平台 24 小时内同时在线玩家峰值达 162291 人，创下近 3 年来的最高纪录。值得注意的是，本作上一次取得如此高的关注度，还是《往日之影》资料片推出以后。2023 年 10 月，《赛博朋克 2077》的同时在线玩家峰值曾突破 27.4 万人。IT之家注意到，本次更新带来了双持武器、新服装等特性，并新增一项任务，其内容可作为《边缘行者 2》动画的前传。此外，CDPR 现在还为本作带来了 3 折优惠，Steam 国区现价 89.4 元（https://store.steampowered.com/app/1091500/%E8%B5%9B%E5%8D%9A%E6%9C%8" data-title="《赛博朋克 2077》游戏 2.5 更新后 Steam 峰值突破 16.2 万，创三年来新高" data-date="10-25 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 14:43</span>
          <span class="news-item-title">《赛博朋克 2077》游戏 2.5 更新后 Steam 峰值突破 16.2 万，创三年来新高</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，据 SteamDB 数据，《赛博朋克 2077》游戏 2.5 版本更新后，Steam 平台 24 小时内同时在…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018205/blue-planet-iii-authentic-organic-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="英国广播公司的蓝色星球III希望通过拍摄不那么完美的照片来证明其真实性。以前的自然系列的化身是由他们华丽，水晶般清晰的镜头定义的，这些镜头看起来几乎太好了，不可能是真实的。但" data-title="Blue Planet III is keeping the rough edges in the age of AI" data-date="10-25 05:29" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 05:29</span>
          <span class="news-item-title">蓝色星球III在人工智能时代保持着粗糙的边缘</span>
          <span class="news-item-title-en">Blue Planet III is keeping the rough edges in the age of AI</span>
          <span class="news-value-point">💡 英国广播公司的蓝色星球III希望通过拍摄不那么完美的照片来证明其真实性</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目。" data-title="The AI graveyard: a running list of projects and startups that didn’t make it" data-date="10-25 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-25 03:00</span>
          <span class="news-item-title">人工智能墓地：未成功完成的项目和初创公司的运行列表</span>
          <span class="news-item-title-en">The AI graveyard: a running list of projects and startups that didn’t make it</span>
          <span class="news-value-point">💡 从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018187/pennsylvania-ai-deceptive-advertising-act" target="_blank" rel="noopener" data-cat="keji" data-summary="周四，宾夕法尼亚州州长乔希·夏皮罗（ Josh Shapiro ）签署了《人工智能欺骗性广告法》（ Artificial Intelligence Deceptive Advertising Act ） ，要求披露人工智能生成的广告。法律要求任何广告-无论是静止图像，视频，音频还是文本- “" data-title="Pennsylvania will require labels on AI" data-date="10-25 02:32" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 02:32</span>
          <span class="news-item-title">宾夕法尼亚州将要求在人工智能上贴标签</span>
          <span class="news-item-title-en">Pennsylvania will require labels on AI</span>
          <span class="news-value-point">💡 周四，宾夕法尼亚州州长乔希·夏皮罗（ Josh Shapiro ）签署了《人工智能欺骗性广告法》（ Artificial Intelligenc…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/forced-to-pick-groks-ai-model-chooses-republicans-openais-picks-democrats/" target="_blank" rel="noopener" data-cat="keji" data-summary="一项新的研究发现， Grok的人工智能压倒性地推荐了共和党候选人，而OpenAI的GPT则倾向于民主党人，在近500场选举中，有90%以上的人工智能模式存在分歧。" data-title="Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats." data-date="10-24 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 23:00</span>
          <span class="news-item-title">被迫选择，格罗克的人工智能模型选择了共和党人。OpenAI挑选民主党人。</span>
          <span class="news-item-title-en">Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats.</span>
          <span class="news-value-point">💡 一项新的研究发现， Grok的人工智能压倒性地推荐了共和党候选人，而OpenAI的GPT则倾向于民主党人，在近500场选举中，有90%以上的人工…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/519.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，小米 REDMI Book 2027 系列笔记本已经官宣将于 10 月 27 日发布。这款笔记本搭载第三代英特尔酷睿平台，内置 72Wh 电池，提供多彩配色，质感全面升级，主打移动办公。小米产品行销总监、数码博主马志宇表示，REDMI Book 16 2027 在外观焕新的同时，还将加入用户长期反复提及的诉求 —— 数字小键盘。当然，对于 16 英寸笔记本而言，数字小键盘并非技术难题，也不能严格称为优点或缺点，更多是产品定义上的取舍。结合此前爆料，REDMI Book 16 2027 将搭载酷睿 5 320 处理器，并配备可自主更换的 DDR5 内存，不再延续前代内存板载的设计。其他已确认或接近确认的信息包括：14 英寸版本采用 2.8K 分辨率屏幕，保留双" data-title="小米 REDMI Book 2027 预热：外观焕新，16 英寸机型标配数字小键盘" data-date="10-24 22:53" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 22:53</span>
          <span class="news-item-title">小米 REDMI Book 2027 预热：外观焕新，16 英寸机型标配数字小键盘</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，小米 REDMI Book 2027 系列笔记本已经官宣将于 10 月 27 日发布</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/518.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，据中国信通院，随着大模型技术的迅速迭代，词元（Token）服务成为从技术走向应用的关键点，我国日均词元调用量持续攀升，2026 年 6 月，国内词元日均消耗量约 500 万亿，是 2025 年 12 月的近 4 倍。产业中越来越多的 MaaS（Model as a Service，模型即服务）平台厂商通过公有云 API 方式供给大模型词元服务。然而用户对词元服务性能缺乏直观的判断依据，且面临选型困难等各类问题。为有效衡量服务性能，中国信息通信研究院（简称“中国信通院”）人工智能研究所、人工智能大模型及软硬件评测工业和信息化部重点实验室和中国人工智能产业发展联盟，自 2025 年以来持续开展公有云大模型词元服务性能监测工作，为产业应用提供重要参考，现联合发布《" data-title="中国信通院：6 月国内词元日均消耗量约 500 万亿，是 2025 年 12 月的近 4 倍" data-date="10-24 22:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 22:41</span>
          <span class="news-item-title">中国信通院：6 月国内词元日均消耗量约 500 万亿，是 2025 年 12 月的近 4 倍</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，据中国信通院，随着大模型技术的迅速迭代，词元（Token）服务成为从技术走向应用的关键点，我国日均词元调用量持…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/all-the-ai-agents-that-can-live-in-your-text-messages/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表。" data-title="Here are the top AI agents that can live in your text messages" data-date="10-24 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 22:00</span>
          <span class="news-item-title">以下是可以存在于您的短信中的顶级AI代理</span>
          <span class="news-item-title-en">Here are the top AI agents that can live in your text messages</span>
          <span class="news-value-point">💡 我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1018131/apple-macbook-touchscreen-stylus-pencil-lenovo-laptop-analysis" target="_blank" rel="noopener" data-cat="keji" data-summary="看起来传闻已久的触摸屏MacBook实际上可能会在下周发布，在使用联想Yoga 9n测试Nvidia的RTX Spark平台之后，我开始思考：这是我想从触摸屏MacBook中获得的很多东西。" data-title="I hope Apple’s touchscreen MacBook takes some lessons from this Lenovo laptop" data-date="10-24 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 22:00</span>
          <span class="news-item-title">我希望苹果的触摸屏MacBook能从这款联想笔记本电脑中吸取一些教训</span>
          <span class="news-item-title-en">I hope Apple’s touchscreen MacBook takes some lessons from this Lenovo laptop</span>
          <span class="news-value-point">💡 看起来传闻已久的触摸屏MacBook实际上可能会在下周发布，在使用联想Yoga 9n测试Nvidia的RTX Spark平台之后，我开始思考：这…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/save-up-to-usd800-on-acers-ultra-slim-rtx-5070-ti-gaming-laptop-pay-usd2225-for-the-16gb-ram-model-or-upgrade-to-32gb-for-usd2400" target="_blank" rel="noopener" data-cat="keji" data-summary="宏碁Predator Helios Neo 16S AI将240 Hz QHD + OLED显示屏与英特尔的24核酷睿Ultra 9处理器和Nvidia RTX 5070 Ti显卡相结合，百思买提供高达800 $的折扣。" data-title="Save up to $800 on Acer’s ultra-slim RTX 5070 Ti gaming laptop — pay $2225 for the 16GB RAM model or upgrade to 32GB for $2400" data-date="10-24 21:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-24 21:58</span>
          <span class="news-item-title">宏碁超薄RTX 5070 Ti游戏笔记本电脑最高可节省800美元—支付2225美元购买16GB RAM型号或升级到32GB仅需2400美元</span>
          <span class="news-item-title-en">Save up to $800 on Acer’s ultra-slim RTX 5070 Ti gaming laptop — pay $2225 for the 16GB RAM model or upgrade to 32GB for $2400</span>
          <span class="news-value-point">💡 宏碁Predator Helios Neo 16S AI将240 Hz QHD + OLED显示屏与英特尔的24核酷睿Ultra 9处理器和Nv…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/25/manchester-united-v-bournemouth-liverpool-v-brighton-and-more-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="格林尼治标准时间下午2点⚽️现场记分牌上的⚽️英超联赛最新消息|向丹尼尔发送电子邮件来自老特拉福德的DanielReports ，由Sky广播，告知我们布鲁诺·费尔南德斯已被迈克尔·卡里克（ Michael Carrick ）淘汰。我们不知道这是一贯糟糕的形式还是英里" data-title="Manchester United v Bournemouth, Liverpool v Brighton and more: clockwatch" data-date="10-25 20:38" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 20:38</span>
          <span class="news-item-title">曼联v伯恩茅斯、利物浦v布莱顿等：钟表</span>
          <span class="news-item-title-en">Manchester United v Bournemouth, Liverpool v Brighton and more: clockwatch</span>
          <span class="news-value-point">💡 格林尼治标准时间下午2点⚽️现场记分牌上的⚽️英超联赛最新消息|向丹尼尔发送电子邮件来自老特拉福德的DanielReports ，由Sky广播，…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/crystal-palace-women-vs-chelsea-women/live/575799" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WSL: Palace stun Chelsea to take lead against run of play LIVE!" data-title="WSL: Palace stun Chelsea to take lead against run of play LIVE!" data-date="10-25 19:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 19:45</span>
          <span class="news-item-title">WSL ：皇宫眩晕切尔西带头对抗现场比赛！</span>
          <span class="news-item-title-en">WSL: Palace stun Chelsea to take lead against run of play LIVE!</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720778.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新社北京10月25日电 (记者 黄欣欣)2026世界华文青年金犊创意节暨第35届金犊奖颁奖典礼25日在北京举行。随着AI(人工智能)深度重塑创意产业，本届参赛作品中超过半数应用AI辅助创作。" data-title="第35届金犊奖在北京颁奖 逾半数作品应用AI辅助创作" data-date="10-25 19:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:39</span>
          <span class="news-item-title">第35届金犊奖在北京颁奖 逾半数作品应用AI辅助创作</span>
          <span class="news-value-point">💡 中新社北京10月25日电 (记者 黄欣欣)2026世界华文青年金犊创意节暨第35届金犊奖颁奖典礼25日在北京举行</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: Alonso unaware of reports Pedro injury was leaked through FPL" data-title="Chelsea latest: Alonso unaware of reports Pedro injury was leaked through FPL" data-date="10-25 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 17:00</span>
          <span class="news-item-title">切尔西最新消息：阿隆索不知道佩德罗受伤的报道是通过FPL泄露的</span>
          <span class="news-item-title-en">Chelsea latest: Alonso unaware of reports Pedro injury was leaked through FPL</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck78p37y5508o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫击败后的评论表明，目前管理俱乐部是多么困难。" data-title="What Man Utd need now is stability, not more changes" data-date="10-25 14:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:34</span>
          <span class="news-item-title">曼联现在需要的是稳定性，而不是更多的变化</span>
          <span class="news-item-title-en">What Man Utd need now is stability, not more changes</span>
          <span class="news-value-point">💡 英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c94g1p32gyrro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦本赛季在四场杯赛中打进了15球，但在七场英超比赛中只打进了9球。" data-title="Why are Liverpool struggling for Premier League goals?" data-date="10-25 14:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:26</span>
          <span class="news-item-title">为什么利物浦要为英超进球而苦苦挣扎？</span>
          <span class="news-item-title-en">Why are Liverpool struggling for Premier League goals?</span>
          <span class="news-value-point">💡 利物浦本赛季在四场杯赛中打进了15球，但在七场英超比赛中只打进了9球</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmy83vg66zngo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着曼联主教练迈克尔·卡里克（ Michael Carrick ）的压力越来越大，英国广播公司体育台（ BBC Sport ）关注英超联赛的“裁员赛季”何时开始。" data-title="When is Premier League &#39;sacking season&#39; - and who should be worried?" data-date="10-25 14:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:17</span>
          <span class="news-item-title">英超联赛的“裁员季”是什么时候？谁应该担心？</span>
          <span class="news-item-title-en">When is Premier League 'sacking season' - and who should be worried?</span>
          <span class="news-value-point">💡 随着曼联主教练迈克尔·卡里克（ Michael Carrick ）的压力越来越大，英国广播公司体育台（ BBC Sport ）关注英超联赛的“裁…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/alaska-early-voting-sites.html" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一位州议员表示， 18个投票站未能开放提前投票“没有法律依据”。" data-title="In Alaska, Some Early Voting Sites in Rural Villages Have Not Yet Opened" data-date="10-25 06:06" data-source="纽约时报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 06:06</span>
          <span class="news-item-title">在阿拉斯加，农村的一些提前投票点尚未开放</span>
          <span class="news-item-title-en">In Alaska, Some Early Voting Sites in Rural Villages Have Not Yet Opened</span>
          <span class="news-value-point">💡 一位州议员表示， 18个投票站未能开放提前投票“没有法律依据”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9ly0dxxgp7lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，在伯恩茅斯周日访问老特拉福德时，他有可能有效地管理曼联。" data-title="Man Utd not an unmanageable club" data-date="10-25 05:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 05:34</span>
          <span class="news-item-title">曼联不是一个难以管理的俱乐部</span>
          <span class="news-item-title-en">Man Utd not an unmanageable club</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，在伯恩茅斯周日访问老特拉福德时，他有可能有效地管理曼联</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqev38dz34vxo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺在周六的英超联赛中排名第12 ，这是他们自1月2日以来的最高联赛位置。他们终于要回来了？" data-title="The candid meeting that &#39;changed&#39; Spurs - are they finally on way back?" data-date="10-25 05:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 05:14</span>
          <span class="news-item-title">“改变”马刺的坦率会议-他们终于回来了吗？</span>
          <span class="news-item-title-en">The candid meeting that 'changed' Spurs - are they finally on way back?</span>
          <span class="news-value-point">💡 托特纳姆热刺在周六的英超联赛中排名第12 ，这是他们自1月2日以来的最高联赛位置</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/24/chelsea-v-tottenham-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Mathys Tel打进了一个很好的单人进球，为马刺在桥梁上的罕见胜利奠定了基础。球队进入球场。蓝色的切尔西，白色的马刺，不久之后，每件衬衫都会湿透。拥有Harry J All St的标志性作品" data-title="Chelsea 0-2 Tottenham: Premier League – as it happened" data-date="10-25 03:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 03:01</span>
          <span class="news-item-title">切尔西0-2托特纳姆热刺：英超联赛–事实就是这样</span>
          <span class="news-item-title-en">Chelsea 0-2 Tottenham: Premier League – as it happened</span>
          <span class="news-value-point">💡 Mathys Tel打进了一个很好的单人进球，为马刺在桥梁上的罕见胜利奠定了基础</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/24/chelsea-tottenham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺有时会参加这些大型比赛，并想方设法击败自己。然而，这一次，他们把神经放在了一个他们大多只知道厄运的地方。马刺发挥控制力，保持耐心，在斯坦福桥赢得比赛" data-title="Tottenham stun Chelsea for second league win in a week as Cole Palmer is sent off" data-date="10-25 02:32" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 02:32</span>
          <span class="news-item-title">托特纳姆热刺击败切尔西，在一周内第二次赢得联赛冠军，科尔·帕尔默被罚下场</span>
          <span class="news-item-title-en">Tottenham stun Chelsea for second league win in a week as Cole Palmer is sent off</span>
          <span class="news-value-point">💡 托特纳姆热刺有时会参加这些大型比赛，并想方设法击败自己</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqwy7x6e672eo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="守门员迈克·彭德斯（ Mike Penders ）经历了艰难的英超首发，在马刺队2-0战胜切尔西的比赛中打进了自己的进球。以下是我们（以及您）对玩家进行评分的方式。" data-title="Penders error &amp; Palmer sees red - player ratings for Chelsea v Spurs" data-date="10-25 02:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 02:26</span>
          <span class="news-item-title">潘德斯错误和帕尔默看到红色-切尔西对马刺的球员评分</span>
          <span class="news-item-title-en">Penders error & Palmer sees red - player ratings for Chelsea v Spurs</span>
          <span class="news-value-point">💡 守门员迈克·彭德斯（ Mike Penders ）经历了艰难的英超首发，在马刺队2-0战胜切尔西的比赛中打进了自己的进球</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6p9gkdzzpnro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尼古拉斯·杰克逊（ Nicolas Jackson ）凭借对阵曼城的比赛获胜双打，继续在阿斯顿维拉（ Aston Villa ）的职业生涯中" data-title="From Chelsea reject to Watkins &#39;upgrade&#39; - Jackson makes fast Villa start" data-date="10-25 00:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 00:58</span>
          <span class="news-item-title">从切尔西拒绝到沃特金斯“升级” -杰克逊让别墅快速启动</span>
          <span class="news-item-title-en">From Chelsea reject to Watkins 'upgrade' - Jackson makes fast Villa start</span>
          <span class="news-value-point">💡 尼古拉斯·杰克逊（ Nicolas Jackson ）凭借对阵曼城的比赛获胜双打，继续在阿斯顿维拉（ Aston Villa ）的职业生涯中</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/24/tottenham-arsenal-wsl-premier-league-efl-football-clockwatch-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳战胜埃弗顿，缩小了与曼城的差距，富勒姆在考文垂阿森纳的回击中取得了重要胜利！ Alessia Russo挑选了Georgia Stanway ，她进入禁区，这位前拜仁中场引导她射门" data-title="Arsenal 2-0 Everton, Coventry 0-1 Fulham: football clockwatch – as it happened" data-date="10-25 00:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 00:13</span>
          <span class="news-item-title">阿森纳2-0埃弗顿，考文垂0-1富勒姆：足球钟表–恰巧</span>
          <span class="news-item-title-en">Arsenal 2-0 Everton, Coventry 0-1 Fulham: football clockwatch – as it happened</span>
          <span class="news-value-point">💡 阿森纳战胜埃弗顿，缩小了与曼城的差距，富勒姆在考文垂阿森纳的回击中取得了重要胜利</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720825.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广西崇左10月25日电(记者 林艳华)10月24日，2026第八届大新明仕田园丰收节在广西崇左市开幕。活动以“欢乐田园，自在明仕”为主题，立足中越边境区位特色、深挖壮族民俗文脉，以节庆礼赞农耕丰收，邀请八方游客与壮乡民众共庆丰年、共享秋日喜悦。" data-title="边关稻熟壮乡风情醉游人 广西大新明仕田园丰收节启幕" data-date="10-25 20:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:32</span>
          <span class="news-item-title">边关稻熟壮乡风情醉游人 广西大新明仕田园丰收节启幕</span>
          <span class="news-value-point">💡 中新网广西崇左10月25日电(记者 林艳华)10月24日，2026第八届大新明仕田园丰收节在广西崇左市开幕</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-united-vs-bournemouth/live/559522" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Man Utd vs Bournemouth team news LIVE!" data-title="Man Utd vs Bournemouth team news LIVE!" data-date="10-25 20:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 20:30</span>
          <span class="news-item-title">曼联对伯恩茅斯队的新闻直播！</span>
          <span class="news-item-title-en">Man Utd vs Bournemouth team news LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/crystal-palace-vs-newcastle-united/live/559518" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Crystal Palace vs Newcastle LIVE!" data-title="Crystal Palace vs Newcastle LIVE!" data-date="10-25 20:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 20:30</span>
          <span class="news-item-title">水晶宫vs纽卡斯尔直播！</span>
          <span class="news-item-title-en">Crystal Palace vs Newcastle LIVE!</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720820.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川10月25日电(记者 于晶)10月25日，宁夏引黄灌区2026年度冬灌正式开闸启动。本次冬灌计划引水9.71亿立方米，灌溉周期31天，水利部门坚持优先次序配置水量，重点保障人畜饮水蓄水供水，以及冬小麦、葡萄、枸杞、黄花菜等越冬作物灌溉需求。" data-title="宁夏引黄灌区2026年度冬灌启动 31天计划引水9.71亿立方米保越冬用水" data-date="10-25 20:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:27</span>
          <span class="news-item-title">宁夏引黄灌区2026年度冬灌启动 31天计划引水9.71亿立方米保越冬用水</span>
          <span class="news-value-point">💡 中新网银川10月25日电(记者 于晶)10月25日，宁夏引黄灌区2026年度冬灌正式开闸启动</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/hull-city-vs-brentford/live/559519" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Hull City vs Brentford LIVE!" data-title="Hull City vs Brentford LIVE!" data-date="10-25 20:25" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 20:25</span>
          <span class="news-item-title">赫尔城vs布伦特福德直播！</span>
          <span class="news-item-title-en">Hull City vs Brentford LIVE!</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/685.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，据香港商报今天报道，香港网约车平台牌照预计最快 11 月推出，有意投身行业的人必须考取“的士及网约车综合笔试”。香港运输及物流局局长陈美宝表示，网约车司机综合笔试反应热烈，及格率超六成。优化后的考试减少了以往针对个别路线的死板题目，改为着重区域方向的掌控。六成的及格率反映投考人士态度认真，另一方面也起到了筛选作用。同时，香港政府建议将网约车车辆许可证设定 1 万个上限，并计划今年第四季度接受申请。陈美宝透露，当局过去已经思考如何利用这 1 万个车辆配额，各项筹备工作也在紧锣密鼓地进行。首批获批的网约车平台名单预计将在 11 月底至 12 月公布。此外，香港政府正争取 11 月向公众公开网约车许可证分配详情。当局正初步构思在抽签机制的基础上，向特定类别人士提供" data-title="香港网约车平台牌照最快 11 月推出，司机笔试合格率超六成" data-date="10-25 20:22" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 20:22</span>
          <span class="news-item-title">香港网约车平台牌照最快 11 月推出，司机笔试合格率超六成</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，据香港商报今天报道，香港网约车平台牌照预计最快 11 月推出，有意投身行业的人必须考取“的士及网约车综合笔试”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/windows/windows-xp-debuted-25-years-ago-today-microsofts-biggest-launch-since-95-was-its-first-consumer-os-to-remove-the-dos-underpinnings" target="_blank" rel="noopener" data-cat="zonghe" data-summary="早在2001年的这一天， Windows XP首次在零售商上市。" data-title="Windows XP debuted 25 years ago today" data-date="10-25 20:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 20:20</span>
          <span class="news-item-title">25年前的今天， Windows XP首次亮相</span>
          <span class="news-item-title-en">Windows XP debuted 25 years ago today</span>
          <span class="news-value-point">💡 早在2001年的这一天， Windows XP首次在零售商上市</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/25/upshot/election-midterms-times-voter-trends.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这是一个我们从未讲述过的及时的人口统计故事。" data-title="Introducing a New Way to Understand the Election: Times Voter Trends" data-date="10-25 20:16" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 20:16</span>
          <span class="news-item-title">介绍一种了解选举的新方式：时代选民趋势</span>
          <span class="news-item-title-en">Introducing a New Way to Understand the Election: Times Voter Trends</span>
          <span class="news-value-point">💡 这是一个我们从未讲述过的及时的人口统计故事</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/682.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，今日，申通快递在业绩说明会谈及“如何看待行业反内卷的持续性？”，并公布部分经营信息。IT之家注意到，该公司表示，本轮“反内卷”核心是禁止低于成本的恶性价格战，淡旺季之间的价格波动乃是跟随电商促销节奏、节假日以及货品结构的影响所致，是正常的价格波动。7-8 月淡季过后，9 月起部分快递核心区域揽收价有所修复，价格环比 7-8 月有所回升。展望未来，随着行业件量增速趋缓以及燃油、社保等刚性成本提升，快递行业的“反内卷”预计有望持续，并逐步演变为行业长期的高质量发展共识。在行业稳定增长以及“反内卷”的持续带动下，公司经营业绩持续向好。具体来看：业务量方面，申通快递 2026 年前三季度完成业务量 219.6 亿件，同比增长 16.4%；市场占有率为 14.5%，同" data-title="申通快递：快递行业的“反内卷”预计有望持续" data-date="10-25 20:07" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 20:07</span>
          <span class="news-item-title">申通快递：快递行业的“反内卷”预计有望持续</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，今日，申通快递在业绩说明会谈及“如何看待行业反内卷的持续性</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/new-cd-players-keep-launching-but-a-drive-shortage-could-make-them-unfixable-almost-nobody-makes-the-drives-anymore" target="_blank" rel="noopener" data-cat="zonghe" data-summary="光驱制造商的匮乏引发了人们对当今市场上推出的新CD播放器的可维修性和寿命的质疑。" data-title="New CD players keep launching, but a drive shortage could make them unfixable" data-date="10-25 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 20:00</span>
          <span class="news-item-title">新的CD播放器不断推出，但驱动器短缺可能会使它们无法修复</span>
          <span class="news-item-title-en">New CD players keep launching, but a drive shortage could make them unfixable</span>
          <span class="news-value-point">💡 光驱制造商的匮乏引发了人们对当今市场上推出的新CD播放器的可维修性和寿命的质疑</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/681.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，据《商业内幕》今天报道，谷歌 DeepMind 高管莱拉 · 易卜拉欣（Lila Ibrahim）近期表示，公司越来越看重那些能够证明自己在课堂之外，持续学习的求职者。这名高管表示，虽然学历依然重要，但公司的招聘已经更重视求职者的经历。例如一项资历能告诉面试官你学过什么，多项资历则能说明你拥有持续学习的心态。她还透露，现在的应届生往往会在简历中，更详细地描述自己学过哪些正规教育外的东西，并将这些经历与工作和教育背景一并列出。这些额外信息对 DeepMind 来说至关重要，因为它有助于判断求职者是否具备好奇心，以及是否最好终身学习的准备。IT之家从原报道获悉，易卜拉欣还认为，多样化的学习经历能够让一个人更善于提出问题，但学校并没有很好地培养这种能力。如今 AI" data-title="谷歌 DeepMind 高管：终身学习者将在 AI 职场中占据优势" data-date="10-25 19:59" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 19:59</span>
          <span class="news-item-title">谷歌 DeepMind 高管：终身学习者将在 AI 职场中占据优势</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，据《商业内幕》今天报道，谷歌 DeepMind 高管莱拉 · 易卜拉欣（Lila Ibrahim）近期表示，公…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/679.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，今日，华为 Mate60 等机型迎来鸿蒙 HarmonyOS 7.0.0.111 SP10 版本更新，安装包体积为 3.03GB。本次更新通信共享升级为多人互助通信共享，同时支持通过 iPhone 的“鸿蒙星河互联”应用与 iPhone 互联。▲ IT之家开箱：华为 Mate60 Pro+“宣白”图赏IT之家整理主要内容如下：通信共享通信共享功能再升级，手机与搭载 HarmonyOS7 的手机、平板、鸿蒙电脑之间支持多人互助通信共享，通过碰一碰或者登录同一华为账号共享网络建立互助网络，在移动网络信号弱或网络负载大等场景下可获得更快、更稳的网络体验。系统支持通过 iPhone 的“鸿蒙星河互联”应用与 iPhone 互联，实现消息相互流转 / 设备相互查找 /" data-title="华为 Mate60 等机型迎来鸿蒙 HarmonyOS 7.0.0.111 SP10 版本更新，通信共享升级为多人互助通信共享" data-date="10-25 19:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 19:56</span>
          <span class="news-item-title">华为 Mate60 等机型迎来鸿蒙 HarmonyOS 7.0.0.111 SP10 版本更新，通信共享升级为多人互助通信共享</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，今日，华为 Mate60 等机型迎来鸿蒙 HarmonyOS 7.0.0.111 SP10 版本更新，安装包体…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckq6nvg7ny1yo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法国当局表示，数十万民众周六再次在全国各地参与抗议活动。示威大致和平进行，但部分城市其后爆发警民冲突，全国有超过1,300人被捕，53名警员受伤。" data-title="法国再爆大规模示威逾1300人被捕，警民冲突致53警受伤" data-date="10-25 19:46" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 19:46</span>
          <span class="news-item-title">法国再爆大规模示威逾1300人被捕，警民冲突致53警受伤</span>
          <span class="news-value-point">💡 法国当局表示，数十万民众周六再次在全国各地参与抗议活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720792.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月25日电 据中国地震台网微博消息，中国地震台网正式测定：10月25日19时25分在西藏那曲市巴青县(北纬32.43度，东经93.99度)发生5.7级地震，震源深度10千米。" data-title="西藏那曲市巴青县发生5.7级地震" data-date="10-25 19:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:37</span>
          <span class="news-item-title">西藏那曲市巴青县发生5.7级地震</span>
          <span class="news-value-point">💡 中新网10月25日电 据中国地震台网微博消息，中国地震台网正式测定：10月25日19时25分在西藏那曲市巴青县(北纬32.43度，东经93.99…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720791.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月25日电 据中国地震台网微博消息，中国地震台网自动测定：10月25日19时26分在青海玉树州杂多县附近(北纬32.54度，东经94.02度)发生5.6级左右地震，最终结果以正式速报为准。" data-title="青海玉树州杂多县附近发生5.6级左右地震" data-date="10-25 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:35</span>
          <span class="news-item-title">青海玉树州杂多县附近发生5.6级左右地震</span>
          <span class="news-value-point">💡 中新网10月25日电 据中国地震台网微博消息，中国地震台网自动测定：10月25日19时26分在青海玉树州杂多县附近(北纬32.54度，东经94.…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-25 20:41（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
