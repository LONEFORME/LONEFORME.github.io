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
      <span>2026-11-14 22:24 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×16 · Tom's Hardware×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/13/us/university-north-carolina-science-research-cuts-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="北卡罗来纳大学校长曾试图保护学校免受特朗普政府的影响。但癌症、自杀、艾滋病和冠状病毒方面的研究工作还是受到了影响。" data-title="How the University of North Carolina Tried to Avoid Trump’s Wrath" data-date="11-14 22:12" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-14 22:12</span>
      </div>
      <h2 class="hero-featured-title">北卡罗来纳大学是如何试图避免招致特朗普的怒火的</h2>
      <div class="hero-featured-title-en">How the University of North Carolina Tried to Avoid Trump’s Wrath</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/027/238.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，Meta 旗下 AI 智能体 Muse 推出代打电话功能，开通高级付费订阅后，用户就能让 Muse 代自己联系美国商家。Meta 称，Muse 可以帮助用户处理各种烦琐事务，完成待办事项。13 日凌晨，Meta 首席 AI 官汪滔在 X 上发文宣布：“Muse 能帮你打完所有不想亲自打的电话。”据悉，用户可以借助 Muse 联系保险公司或有线电视服务商、预约美国车管部门的业务办理时间，或是打电话向餐厅订位。Muse 会使用 AI 合成语音与商家工作人员交谈，但这类功能并非总能顺利完成任务。部分商家的工作人员听出对方是 AI 后便直接挂断电话，有人是为了防范诈骗，也有人认为这类来电可能是恶作剧，只会浪费时间。Meta 此前已面向早期体验用户测试了几个月，现向" data-title="智能体帮你联络商家或保险公司，Meta 旗下 Muse 上线代打电话功能" data-date="11-14 21:46" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">智能体帮你联络商家或保险公司，Meta 旗下 Muse 上线代打电话功能</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/chelsea-women-vs-manchester-city-women/live/575819" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WSL LIVE! Chelsea vs Man City under way, Man Utd lead Palace" data-title="WSL LIVE! Chelsea vs Man City under way, Man Utd lead Palace" data-date="11-14 19:15" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">WSL LIVE! Chelsea vs Man City under way, Man Utd lead Palace</p>
    </a>
    <a class="hero-sub-card" href="https://www.tomshardware.com/maker-stem/contractor-builds-ethernet-cable-untwisting-machine-after-facing-100-000-cat6-termination-job-modified-milwaukee-hackzall-straightens-cables-in-under-two-seconds" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这款以太网电缆解绞工具可以将安装 RJ45 连接器所需的时间缩短一半。" data-title="Contractor turns a Milwaukee Hackzall into a portable Ethernet untwister after facing job requiring 50,000 custom Cat6 cables" data-date="11-14 22:20" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">Contractor turns a Milwaukee Hackzall into a portable Ethernet untwister after facing job requiring 50,000 custom Cat6 cables</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/us/university-north-carolina-science-research-cuts-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="北卡罗来纳大学校长曾试图保护学校免受特朗普政府的影响。但癌症、自杀、艾滋病和冠状病毒方面的研究工作还是受到了影响。" data-title="How the University of North Carolina Tried to Avoid Trump’s Wrath" data-date="11-14 22:12" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 22:12</span>
          <span class="news-item-title">北卡罗来纳大学是如何试图避免招致特朗普的怒火的</span>
          <span class="news-item-title-en">How the University of North Carolina Tried to Avoid Trump’s Wrath</span>
          <span class="news-value-point">💡 北卡罗来纳大学校长曾试图保护学校免受特朗普政府的影响</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/pentagon-struggles-to-account-for-usd31-billion-in-missing-f-35-aircraft-parts-weeks-after-shipment-was-swiped-by-china-tracking-of-estimated-26-million-parts-is-outdated-inaccurate-and-incomplete-says-watchdog" target="_blank" rel="noopener" data-cat="shizheng" data-summary="根据美国政府问责局本周发布的分析报告，五角大楼正竭力追查多达2600万件F-35战斗机零部件的下落，这些零部件的价值估计为310亿美元。" data-title="Pentagon ‘struggles to account for’ $31 billion in missing F-35 aircraft parts, weeks after shipment was swiped by China" data-date="11-14 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 22:00</span>
          <span class="news-item-title">在F-35飞机零部件被中国盗走数周后，五角大楼“难以解释”310亿美元的零部件去向</span>
          <span class="news-item-title-en">Pentagon ‘struggles to account for’ $31 billion in missing F-35 aircraft parts, weeks after shipment was swiped by China</span>
          <span class="news-value-point">💡 根据美国政府问责局本周发布的分析报告，五角大楼正竭力追查多达2600万件F-35战斗机零部件的下落，这些零部件的价值估计为310亿美元</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/14/us/alaska-senate-race-ranked-choice-tabulation.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="参议员丹·沙利文与前众议员佩尔托拉女士之间的角逐是唯一一场尚未宣布结果的参议院竞选。" data-title="Alaska Senate Race Between Dan Sullivan and Mary Peltola Still Counting Votes" data-date="11-14 21:30" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 21:30</span>
          <span class="news-item-title">丹·沙利文与玛丽·佩尔托拉之间的阿拉斯加州参议员竞选仍在计票中</span>
          <span class="news-item-title-en">Alaska Senate Race Between Dan Sullivan and Mary Peltola Still Counting Votes</span>
          <span class="news-value-point">💡 参议员丹·沙利文与前众议员佩尔托拉女士之间的角逐是唯一一场尚未宣布结果的参议院竞选</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732186.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="值孙中山先生诞辰160周年之际" data-title="两岸网友共创视频｜我们的城市有条中山路" data-date="11-14 21:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 21:29</span>
          <span class="news-item-title">两岸网友共创视频｜我们的城市有条中山路</span>
          <span class="news-value-point">💡 值孙中山先生诞辰160周年之际</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/video/us/politics/100000011272223/whats-behind-the-trump-huang-relationship.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在黄仁勋受到抨击之际，特朗普总统对他表示支持，这是两人关系中的一个非凡时刻，而这种关系在两年前几乎不存在。我们的白宫记者Maggie Haberman解释了特朗普先生是如何开始将黄先生视为温和派的。" data-title="What’s Behind the Trump" data-date="11-14 21:27" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 21:27</span>
          <span class="news-item-title">特朗普背后的故事</span>
          <span class="news-item-title-en">What’s Behind the Trump</span>
          <span class="news-value-point">💡 在黄仁勋受到抨击之际，特朗普总统对他表示支持，这是两人关系中的一个非凡时刻，而这种关系在两年前几乎不存在</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732184.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“亚太是我们共同发展的空间，我们都是亚太这片大海中前行的风帆。”" data-title="习近平主席引领亚太大家庭扬帆前行" data-date="11-14 21:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 21:26</span>
          <span class="news-item-title">习近平主席引领亚太大家庭扬帆前行</span>
          <span class="news-value-point">💡 “亚太是我们共同发展的空间，我们都是亚太这片大海中前行的风帆</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732160.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网韩国釜山11月14日电 (记者 金旭)当地时间11月13日至14日，2026釜山国际艺术节在韩国举办。" data-title="2026釜山国际艺术节在韩国举行" data-date="11-14 20:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 20:32</span>
          <span class="news-item-title">2026釜山国际艺术节在韩国举行</span>
          <span class="news-value-point">💡 中新网韩国釜山11月14日电 (记者 金旭)当地时间11月13日至14日，2026釜山国际艺术节在韩国举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732148.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月14日电 综合消息：联合国人道主义事务协调厅、世界粮食计划署等14日警告称，长时间被围困的也门塔伊兹省面临食物短缺、疾病传播等人道主义危机。" data-title="联合国警告：也门塔伊兹省面临人道主义危机" data-date="11-14 20:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 20:32</span>
          <span class="news-item-title">联合国警告：也门塔伊兹省面临人道主义危机</span>
          <span class="news-value-point">💡 中新网北京11月14日电 综合消息：联合国人道主义事务协调厅、世界粮食计划署等14日警告称，长时间被围困的也门塔伊兹省面临食物短缺、疾病传播等人…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/chinas-air-force-builds-drone-that-shoots-painkiller-darts-at-wounded-soldiers-experimental-pla-uav-injects-emergency-meds-from-a-distance-to-keep-medics-out-of-danger-and-buys-time-during-the-golden-hour" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国人民解放军（PLA）空军军医大学制造了这款无人机，以便能够远程为受伤士兵注射止痛药，并使伤员的转移更加容易。" data-title="China’s Air Force builds drone that shoots painkiller darts at wounded soldiers" data-date="11-14 20:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 20:30</span>
          <span class="news-item-title">中国空军研制出可向受伤士兵发射止痛镖的无人机</span>
          <span class="news-item-title-en">China’s Air Force builds drone that shoots painkiller darts at wounded soldiers</span>
          <span class="news-value-point">💡 中国人民解放军（PLA）空军军医大学制造了这款无人机，以便能够远程为受伤士兵注射止痛药，并使伤员的转移更加容易</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732141.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月14日电 (记者 曾玥)旅游特色孔子学院联盟14日在北京揭牌成立。至此，全球范围内已建立38个孔子学院联盟或类似工作机制。" data-title="旅游特色孔子学院联盟揭牌成立" data-date="11-14 20:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 20:27</span>
          <span class="news-item-title">旅游特色孔子学院联盟揭牌成立</span>
          <span class="news-value-point">💡 中新社北京11月14日电 (记者 曾玥)旅游特色孔子学院联盟14日在北京揭牌成立</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732143.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近日，95岁美国老人柏大卫的“中国乡愁”，引发全网关注。他说：“一个人一生只能有一个故乡，湟源是我唯一的、永远的故乡。”中国青海湟源县，为何成为一位美国人永远的故乡？" data-title="主播说联播丨95岁美国老人的“中国乡愁”，为何引发全网关注？" data-date="11-14 19:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 19:56</span>
          <span class="news-item-title">主播说联播丨95岁美国老人的“中国乡愁”，为何引发全网关注？</span>
          <span class="news-value-point">💡 近日，95岁美国老人柏大卫的“中国乡愁”，引发全网关注</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732107.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月14日电 11月14日，中共中央政治局委员、国务院副总理何立峰在深圳出席亚太经合组织(APEC)工商咨询理事会第四次会议开幕式并致辞。" data-title="（深圳APEC）何立峰出席亚太经合组织工商咨询理事会第四次会议开幕式并致辞" data-date="11-14 19:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 19:17</span>
          <span class="news-item-title">（深圳APEC）何立峰出席亚太经合组织工商咨询理事会第四次会议开幕式并致辞</span>
          <span class="news-value-point">💡 中新社深圳11月14日电 11月14日，中共中央政治局委员、国务院副总理何立峰在深圳出席亚太经合组织(APEC)工商咨询理事会第四次会议开幕式并…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732109.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社太原11月14日电 (记者 李庭耀)11月14日，山西省第十四届人民代表大会常务委员会第三十一次会议举行第二次全体会议。会议表决通过了人事任免名单，决定任命鞠振为山西省副省长。" data-title="鞠振任山西省副省长" data-date="11-14 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 19:14</span>
          <span class="news-item-title">鞠振任山西省副省长</span>
          <span class="news-value-point">💡 中新社太原11月14日电 (记者 李庭耀)11月14日，山西省第十四届人民代表大会常务委员会第三十一次会议举行第二次全体会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732095.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网苏州11月14日电 (记者 钟升)以“百年变局下的中阿命运共同体建设：政党的责任与使命”为主题的第五届中国—阿拉伯国家政党对话会13日至14日在江苏省苏州市举行。中联部部长刘海星在主旨讲话中表示，中方将始终做中东和平的建设者、稳定的促进者、发展的贡献者。" data-title="刘海星：中方将始终做中东和平的建设者、稳定的促进者、发展的贡献者" data-date="11-14 18:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 18:41</span>
          <span class="news-item-title">刘海星：中方将始终做中东和平的建设者、稳定的促进者、发展的贡献者</span>
          <span class="news-value-point">💡 中新网苏州11月14日电 (记者 钟升)以“百年变局下的中阿命运共同体建设：政党的责任与使命”为主题的第五届中国—阿拉伯国家政党对话会13日至1…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732065.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月14日电 据日本《读卖新闻》报道，当地时间14日，日本冲绳县警方以涉嫌酒后驾驶逮捕了一名驻冲绳美军上尉。" data-title="因涉嫌酒驾 驻日美军上尉被日本警方逮捕" data-date="11-14 17:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 17:28</span>
          <span class="news-item-title">因涉嫌酒驾 驻日美军上尉被日本警方逮捕</span>
          <span class="news-value-point">💡 中新网11月14日电 据日本《读卖新闻》报道，当地时间14日，日本冲绳县警方以涉嫌酒后驾驶逮捕了一名驻冲绳美军上尉</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/027/238.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，Meta 旗下 AI 智能体 Muse 推出代打电话功能，开通高级付费订阅后，用户就能让 Muse 代自己联系美国商家。Meta 称，Muse 可以帮助用户处理各种烦琐事务，完成待办事项。13 日凌晨，Meta 首席 AI 官汪滔在 X 上发文宣布：“Muse 能帮你打完所有不想亲自打的电话。”据悉，用户可以借助 Muse 联系保险公司或有线电视服务商、预约美国车管部门的业务办理时间，或是打电话向餐厅订位。Muse 会使用 AI 合成语音与商家工作人员交谈，但这类功能并非总能顺利完成任务。部分商家的工作人员听出对方是 AI 后便直接挂断电话，有人是为了防范诈骗，也有人认为这类来电可能是恶作剧，只会浪费时间。Meta 此前已面向早期体验用户测试了几个月，现向" data-title="智能体帮你联络商家或保险公司，Meta 旗下 Muse 上线代打电话功能" data-date="11-14 21:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 21:46</span>
          <span class="news-item-title">智能体帮你联络商家或保险公司，Meta 旗下 Muse 上线代打电话功能</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，Meta 旗下 AI 智能体 Muse 推出代打电话功能，开通高级付费订阅后，用户就能让 Muse 代自己联系…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/233.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，据 NBC News 报道，在一家丹尼餐厅（Denny’s）路边店内，硅谷历史的一角仿佛凭空消失了。30 多年前，黄仁勋与两位好友正是在这里构想出了英伟达，而如今纪念这一确切位置的牌匾已不翼而飞。牌匾上的铭文曾写道：“开启一家万亿美元公司的卡座”，如今只剩下一片空荡荡的砖墙和剥落的墙漆。两名店员证实，牌匾已被撤下。▲ 2023 年，丹尼餐厅 CEO Kelli Valade 与英伟达创始人黄仁勋在加利福尼亚州圣何塞的丹尼餐厅同框IT之家注意到，在该媒体发文后，丹尼餐厅的一位发言人表示，该连锁餐厅正在“重新安装这块牌匾，以纪念在丹尼餐厅促成英伟达诞生的那些对话”。“黄仁勋最初是在丹尼餐厅当洗碗工起家的。多年后，他和联合创始人们聚在我们的一个卡座里，探讨了后来演" data-title="黄仁勋辞任 CEO 后，英伟达诞生地丹尼餐厅移除纪念铭牌、又宣布将重新挂回" data-date="11-14 21:31" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 21:31</span>
          <span class="news-item-title">黄仁勋辞任 CEO 后，英伟达诞生地丹尼餐厅移除纪念铭牌、又宣布将重新挂回</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，据 NBC News 报道，在一家丹尼餐厅（Denny’s）路边店内，硅谷历史的一角仿佛凭空消失了</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/230.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，在第二十三届中国国际半导体博览会（IC China）期间，北京华大九天科技股份有限公司与粤港澳大湾区科技创新产业投资基金，在北京 · 国家会议中心联合举行“国产数字前端 EDA 新平台发布会”，宣布亚科鸿禹与思尔芯合并重组，新平台公司“新禹思”（HyperS2C）正式成立。官方表示，此次思尔芯与亚科鸿禹的整合并非简单的企业合并，而是国内两大头部数字 EDA 企业的优势互补、能力重构与生态完善。整合后的新禹思，拥有专利 205 项、软件著作权 200 项，具备覆盖从架构设计到系统级验证的数字前端全流程供给能力，服务全球客户超过 800 家，实现了技术能力的升级、产品体系的升级、客户网络的升级，全面对标国际顶尖技术水平。IT之家获悉，新平台有助于改变国产工具多为" data-title="华大九天联合大湾区基金完成国产数字前端 EDA 专业化整合，新公司“新禹思”成立" data-date="11-14 21:07" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 21:07</span>
          <span class="news-item-title">华大九天联合大湾区基金完成国产数字前端 EDA 专业化整合，新公司“新禹思”成立</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，在第二十三届中国国际半导体博览会（IC China）期间，北京华大九天科技股份有限公司与粤港澳大湾区科技创新产…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-upgrades-eight-v100-private-ai-server-to-run-80-percent-of-deepseek-v4-1-flash-at-4-bit-nvfp4-precision-adds-1tb-of-ram-an-nvidia-rtx-3090-and-fixes-crashes-caused-by-a-bad-psu" target="_blank" rel="noopener" data-cat="keji" data-summary="一位律师的八个GPU Nvidia V100服务器现在以NVFP4精度（而非2位精度）运行DeepSeek V4.1 Flash最常用的专家模型。" data-title="Lawyer’s eight-V100 AI server moves DeepSeek from 2-bit to near-NVFP4 precision" data-date="11-14 20:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 20:50</span>
          <span class="news-item-title">Lawyer 的八卡 V100 AI 服务器将 DeepSeek 从 2 位精度提升至接近 NVFP4 的精度</span>
          <span class="news-item-title-en">Lawyer’s eight-V100 AI server moves DeepSeek from 2-bit to near-NVFP4 precision</span>
          <span class="news-value-point">💡 一位律师的八个GPU Nvidia V100服务器现在以NVFP4精度（而非2位精度）运行DeepSeek V4.1 Flash最常用的专家模型</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/228.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，英伟达应用深度学习研究副总裁布莱恩 · 卡坦扎罗（Bryan Catanzaro）在社交平台 X 上公开发文辟谣，否认自己参与签署网传要求前 CEO 黄仁勋复职的公开信，称该信件系伪造，并明确表态支持英伟达董事会及临时 CEO 科莱特 · 克雷斯（Colette Kress）。布莱恩 · 卡坦扎罗声称，即便（公开信）是真的，他也不会签字。IT之家注意到，黄仁勋离任后，网络上流传出一封公开信，以布莱恩 · 卡坦扎罗在内的多名英伟达高管与员工名义要求董事会让黄仁勋复职。据悉，该公开信之所以很快被识破，除了布莱恩 · 卡坦扎罗下场辟谣外，还因为信件文本直接照搬了 2023 年 11 月 OpenAI 员工要求萨姆 · 奥尔特曼（Sam Altman）复职的联名信模" data-title="英伟达副总裁卡坦扎罗否认签署要求前 CEO 黄仁勋复职的公开信，表态支持董事会和临时 CEO 克雷斯" data-date="11-14 20:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 20:45</span>
          <span class="news-item-title">英伟达副总裁卡坦扎罗否认签署要求前 CEO 黄仁勋复职的公开信，表态支持董事会和临时 CEO 克雷斯</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，英伟达应用深度学习研究副总裁布莱恩 · 卡坦扎罗（Bryan Catanzaro）在社交平台 X 上公开发文辟…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/226.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，当地时间 13 日，据外媒 Tom&#39;s Hardware 报道，美国的一名 AI 爱好者穆罕默德 · 祖拉利靠着 AI 和简单的电子接线操作，成功让一辆有 32 年车龄的 1994 款 Jeep 切诺基通过了美国加州的尾气检测。这辆老车的发动机电脑功能十分有限，但祖拉利借助 Arduino Nano 开发板将其连接到笔记本电脑后，不仅能够读取车辆数据，还逐步实现了对部分参数的控制。其发布的视频记录了祖拉利解决尾气排放问题的全过程：从连续检测不合格，到成功连接发动机电脑并读取数据，再到调整发动机、解决排放超标问题。整个过程中，Claude 负责指导，Codex 则负责写代码。切诺基此前多次未能通过加州尾气检测，原因是在特定车速下氮氧化物排放超标。最初，车辆在" data-title="借助 Claude 和 Arduino 开发板，达人让 1994 款切诺基通过加州排放检测" data-date="11-14 20:36" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 20:36</span>
          <span class="news-item-title">借助 Claude 和 Arduino 开发板，达人让 1994 款切诺基通过加州排放检测</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，当地时间 13 日，据外媒 Tom's Hardware 报道，美国的一名 AI 爱好者穆罕默德 · 祖拉利靠…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/commemorative-plaque-at-dennys-booth-where-nvidia-was-born-has-been-removed-sign-removed-in-wake-of-jensens-scandals-marked-the-booth-that-launched-a-usd1-trillion-company" target="_blank" rel="noopener" data-cat="keji" data-summary="加利福尼亚州圣何塞的Denny&#39;s分店曾挂有一块牌匾，纪念Jensen Huang和另外两位联合创始人在这里的卡座上努力创立Nvidia。" data-title="Commemorative plaque at Denny’s booth where Nvidia was born has been removed in wake of Jensen Huang scandals" data-date="11-14 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 20:00</span>
          <span class="news-item-title">在黄仁勋丑闻曝出后，Nvidia诞生地Denny's餐厅的纪念牌匾已被移除</span>
          <span class="news-item-title-en">Commemorative plaque at Denny’s booth where Nvidia was born has been removed in wake of Jensen Huang scandals</span>
          <span class="news-value-point">💡 加利福尼亚州圣何塞的Denny's分店曾挂有一块牌匾，纪念Jensen Huang和另外两位联合创始人在这里的卡座上努力创立Nvidia</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/linux/nearly-20-years-after-launch-ancient-radeon-hd-2000-and-3000-gpus-finally-get-a-linux-fix-for-corrupted-video-playback-ai-helps-squash-a-decades-old-uvd-bug" target="_blank" rel="noopener" data-cat="keji" data-summary="一位新的内核贡献者使用人工智能为驱动其近20年历史的Radeon GPU的驱动程序开发了一个补丁。" data-title="Nearly 20 years after launch, ancient AMD Radeon HD 2000 and 3000 GPUs finally get a Linux fix for corrupted video playback" data-date="11-14 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 19:00</span>
          <span class="news-item-title">在发布近20年后，老旧的AMD Radeon HD 2000和3000系列GPU终于获得了针对视频播放损坏问题的Linux补丁。</span>
          <span class="news-item-title-en">Nearly 20 years after launch, ancient AMD Radeon HD 2000 and 3000 GPUs finally get a Linux fix for corrupted video playback</span>
          <span class="news-value-point">💡 一位新的内核贡献者使用人工智能为驱动其近20年历史的Radeon GPU的驱动程序开发了一个补丁</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510297.html" target="_blank" rel="noopener" data-cat="keji" data-summary="马斯克也签名了" data-title="英伟达上演“奥特曼2.0”，员工集体请愿：让老黄回家！" data-date="11-14 18:08" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-14 18:08</span>
          <span class="news-item-title">英伟达上演“奥特曼2.0”，员工集体请愿：让老黄回家！</span>
          <span class="news-value-point">💡 马斯克也签名了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510232.html" target="_blank" rel="noopener" data-cat="keji" data-summary="斯坦福、哈佛、康奈尔……十余家顶尖团队齐坐一桌了" data-title="“史上最严”湿实验预测基准发布！推理拉满、算力翻5倍也白搭" data-date="11-14 17:58" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-14 17:58</span>
          <span class="news-item-title">“史上最严”湿实验预测基准发布！推理拉满、算力翻5倍也白搭</span>
          <span class="news-value-point">💡 斯坦福、哈佛、康奈尔……十余家顶尖团队齐坐一桌了</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/158.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，外媒 9to5Google 在拆解谷歌 Android Auto 18.2 测试版时发现，谷歌仍在继续开发 Android Auto 的浅色模式菜单界面。具体来看，官方在本次更新中悄悄调整了超过 100 项界面资源文件，主要涉及按钮等用户界面元素。res/drawable/ic_mr_button_connected_14_dark.xmlres/drawable/ic_mr_button_connected_15_dark.xml外媒表示，谷歌最近的每次更新都在不断完善浅色模式功能，至于相应功能确切上线时间，目前还不得而知。值得一提的是，过去几个月谷歌已经为 Android Auto 带来了不少更具实际价值的功能，其中较新的变化是 Gemini Intel" data-title="谷歌推送 Android Auto 18.2 测试版，代码显示官方正持续开发浅色模式菜单界面" data-date="11-14 15:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 15:44</span>
          <span class="news-item-title">谷歌推送 Android Auto 18.2 测试版，代码显示官方正持续开发浅色模式菜单界面</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，外媒 9to5Google 在拆解谷歌 Android Auto 18.2 测试版时发现，谷歌仍在继续开发 A…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510003.html" target="_blank" rel="noopener" data-cat="keji" data-summary="官方App功能均可自由组合调用" data-title="突发！DeepSeek开放全家桶API" data-date="11-14 10:39" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-14 10:39</span>
          <span class="news-item-title">突发！DeepSeek开放全家桶API</span>
          <span class="news-value-point">💡 官方App功能均可自由组合调用</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/13/us/politics/nvidia-alice-huang-spy-china.html" target="_blank" rel="noopener" data-cat="keji" data-summary="美国情报机构认为，与黄仁勋有染的一名女性是中国情报人员。但他们仍在评估她的角色，还有很多情况尚待厘清。" data-title="Nvidia Scandal Prompts Questions of What It Means to Be a Spy" data-date="11-14 09:22" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-14 09:22</span>
          <span class="news-item-title">英伟达丑闻引发人们对“什么是间谍”的疑问</span>
          <span class="news-item-title-en">Nvidia Scandal Prompts Questions of What It Means to Be a Spy</span>
          <span class="news-value-point">💡 美国情报机构认为，与黄仁勋有染的一名女性是中国情报人员</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/" target="_blank" rel="noopener" data-cat="keji" data-summary="在黄仁勋的领导下，英伟达向人工智能初创企业投入了数百亿美元。没有他掌舵，创始人与风险投资机构正准备迎接更少的投资和更低的估值。" data-title="Jensen Huang’s departure blasts big hole in AI startup funding, VCs and founders say" data-date="11-14 06:43" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-14 06:43</span>
          <span class="news-item-title">风险投资人和创始人表示，Jensen Huang的离职在人工智能初创企业的融资方面留下了巨大的缺口</span>
          <span class="news-item-title-en">Jensen Huang’s departure blasts big hole in AI startup funding, VCs and founders say</span>
          <span class="news-value-point">💡 在黄仁勋的领导下，英伟达向人工智能初创企业投入了数百亿美元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-board-reportedly-approached-arm-ceo-rene-haas-during-replacement-search-jensen-huangs-transgressions-leave-nvidia-scrambling-to-fill-a-massive-void" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达董事会在寻找首席执行官的过程中曾与Arm首席执行官、英伟达的资深老将Rene Haas接触。" data-title="Nvidia board reportedly approached Arm CEO Rene Haas during replacement search" data-date="11-14 05:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 05:00</span>
          <span class="news-item-title">据报道，在寻找继任者期间，Nvidia董事会曾与Arm首席执行官Rene Haas接触。</span>
          <span class="news-item-title-en">Nvidia board reportedly approached Arm CEO Rene Haas during replacement search</span>
          <span class="news-value-point">💡 据报道，英伟达董事会在寻找首席执行官的过程中曾与Arm首席执行官、英伟达的资深老将Rene Haas接触</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/chelsea-women-vs-manchester-city-women/live/575819" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WSL LIVE! Chelsea vs Man City under way, Man Utd lead Palace" data-title="WSL LIVE! Chelsea vs Man City under way, Man Utd lead Palace" data-date="11-14 19:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 19:15</span>
          <span class="news-item-title">英超女足联赛直播！切尔西对阵曼城比赛正在进行，曼联领先水晶宫</span>
          <span class="news-item-title-en">WSL LIVE! Chelsea vs Man City under way, Man Utd lead Palace</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611443/mauricio-pochettino-to-man-utd-what-does-a-pochettino-team-look-like-and-how-will-he-set-up-struggling-red-devils" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在迈克尔·卡里克被解雇后，毛里西奥·波切蒂诺被任命为曼联的新任主教练。那么，球迷们在球场上究竟可以期待什么呢？" data-title="What does a Pochettino team look like?" data-date="11-14 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 15:00</span>
          <span class="news-item-title">一支波切蒂诺的球队是什么样的？</span>
          <span class="news-item-title-en">What does a Pochettino team look like?</span>
          <span class="news-value-point">💡 在迈克尔·卡里克被解雇后，毛里西奥·波切蒂诺被任命为曼联的新任主教练</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c85y13pv69xwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联球迷可以对新任主教练毛里西奥·波切蒂诺抱有怎样的期望？BBC体育从托比·阿尔德韦雷尔德那里获得了独家见解，后者曾在热刺效力时由他执教。" data-title="Fitness obsessed &amp; &#39;control freak&#39; - what can Man Utd expect from Pochettino?" data-date="11-14 06:53" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-14 06:53</span>
          <span class="news-item-title">对体能的痴迷和“控制狂”——曼联可以对波切蒂诺抱有怎样的期望？</span>
          <span class="news-item-title-en">Fitness obsessed & 'control freak' - what can Man Utd expect from Pochettino?</span>
          <span class="news-value-point">💡 曼联球迷可以对新任主教练毛里西奥·波切蒂诺抱有怎样的期望</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmd61qne8352o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺在解释他为何离开美国去执教曼联时泪流满面。" data-title="Tearful Pochettino on &#39;difficult&#39; decision to leave USA for Man Utd" data-date="11-13 23:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 23:28</span>
          <span class="news-item-title">波切蒂诺含泪谈及离开美国队执教曼联的“艰难”决定</span>
          <span class="news-item-title-en">Tearful Pochettino on 'difficult' decision to leave USA for Man Utd</span>
          <span class="news-value-point">💡 情绪激动的毛里西奥·波切蒂诺在解释他为何离开美国去执教曼联时泪流满面</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611887/mauricio-pochettino-new-man-utd-head-coach-in-tears-as-he-labels-leaving-usmnt-toughest-decision-of-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会。" data-title="Tearful Pochettino admits he &#39;couldn&#39;t say no to Man Utd&#39;" data-date="11-13 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 23:00</span>
          <span class="news-item-title">泪流满面的波切蒂诺承认他“无法拒绝曼联”</span>
          <span class="news-item-title-en">Tearful Pochettino admits he 'couldn't say no to Man Utd'</span>
          <span class="news-value-point">💡 情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13611887/mauricio-pochettino-new-man-utd-head-coach-in-tears-as-he-labels-leaving-usmnt-toughest-decision-of-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="情绪激动的毛里西奥·波切蒂诺表示，离开美国队是他“职业生涯中最艰难的决定”，但他承认，他无法拒绝成为曼联主教练的机会。" data-title="Tearful Pochettino admits he &#39;couldn&#39;t say no to Man Utd&#39;" data-date="11-13 23:00" data-source="天空体育">
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/maker-stem/contractor-builds-ethernet-cable-untwisting-machine-after-facing-100-000-cat6-termination-job-modified-milwaukee-hackzall-straightens-cables-in-under-two-seconds" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这款以太网电缆解绞工具可以将安装 RJ45 连接器所需的时间缩短一半。" data-title="Contractor turns a Milwaukee Hackzall into a portable Ethernet untwister after facing job requiring 50,000 custom Cat6 cables" data-date="11-14 22:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 22:20</span>
          <span class="news-item-title">在面临一项需要 5 万根定制 Cat6 电缆的工程后，承包商将一台密尔沃基 Hackzall 改造成了一台便携式以太网电缆绞线分离器。</span>
          <span class="news-item-title-en">Contractor turns a Milwaukee Hackzall into a portable Ethernet untwister after facing job requiring 50,000 custom Cat6 cables</span>
          <span class="news-value-point">💡 这款以太网电缆解绞工具可以将安装 RJ45 连接器所需的时间缩短一半</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1033844/tesla-personal-cybercab-orders-299-subscription-fine-print" target="_blank" rel="noopener" data-cat="zonghe" data-summary="特斯拉向“特定客户”提供购买Cybercab用于“个人使用”的机会，这使其对自动驾驶未来的大胆宣称力度加倍，甚至可能翻了两番。但这款镀金的无方向盘双座车型“仅在支持的地区" data-title="Tesla is inviting some people to buy a Cybercab ‘for personal use’ — but read the fine print" data-date="11-14 22:18" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 22:18</span>
          <span class="news-item-title">特斯拉正在邀请一些人“自用”购买Cybercab——但请仔细阅读小字条款</span>
          <span class="news-item-title-en">Tesla is inviting some people to buy a Cybercab ‘for personal use’ — but read the fine print</span>
          <span class="news-value-point">💡 特斯拉向“特定客户”提供购买Cybercab用于“个人使用”的机会，这使其对自动驾驶未来的大胆宣称力度加倍，甚至可能翻了两番</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1013985/crkd-atom-plus-tmr-analog-thumbstick-controller-gamepad-switch-ios-android-hands-on" target="_blank" rel="noopener" data-cat="zonghe" data-summary="虽然我很欣赏任天堂 Switch 的 Joy-Con 巧妙的设计，但我和家人都受不了将它们作为独立的游戏手柄来使用。因此，当我们带着 Switch 2 旅行时，我们总是会带上至少一个全尺寸游戏手柄，外加几个 8BitDo。" data-title="This tiny gamepad with dual analog thumbsticks pushes the limits of portable controllers" data-date="11-14 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 22:00</span>
          <span class="news-item-title">这款小巧的双模拟摇杆游戏手柄突破了便携式手柄的极限</span>
          <span class="news-item-title-en">This tiny gamepad with dual analog thumbsticks pushes the limits of portable controllers</span>
          <span class="news-value-point">💡 虽然我很欣赏任天堂 Switch 的 Joy-Con 巧妙的设计，但我和家人都受不了将它们作为独立的游戏手柄来使用</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/live-blog/12040/13611918/dp-world-tour-championship-rory-mcilroy-eugenio-chacarra-set-for-final-day-battle-who-will-win-the-race-to-dubai" target="_blank" rel="noopener" data-cat="zonghe" data-summary="McIlroy backed for Race to Dubai &#39;reset&#39; - can he overcome Chacarra?" data-title="McIlroy backed for Race to Dubai &#39;reset&#39; - can he overcome Chacarra?" data-date="11-14 21:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 21:40</span>
          <span class="news-item-title">麦克罗伊支持“重启”迪拜争霸赛——他能战胜查卡拉吗？</span>
          <span class="news-item-title-en">McIlroy backed for Race to Dubai 'reset' - can he overcome Chacarra?</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/231.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 14 日消息，据央视新闻今天（14 日）晚间报道，荷兰皇家航空公司前首席执行官（CEO）卡米尔 · 厄尔林斯 9 月在该公司一架客机上违规使用充电宝引发火情，荷航日前已就此事向检方提请指控厄尔林斯。荷航 13 日在一份声明中说：“如果乘客严重违反安全规定，危及航班、乘客或机组人员安全，公司方面会提出指控，这是标准做法。”荷航没有公布当事人身份。消息人士称，受指控的是厄尔林斯。多方消息称，9 月 17 日，一架荷航客机从荷兰首都阿姆斯特丹飞往加勒比海的荷兰海外属地库拉索，途中客舱出现火情。当时，厄尔林斯违规使用充电宝，充电宝过热自燃，浓烟笼罩客舱，火焰把窗户遮阳板烧得焦黑。厄尔林斯本人在睡梦中受轻微伤。机组人员迅速用灭火器把火扑灭。飞机立即返航，安全返回阿姆斯特丹。IT之家" data-title="荷兰皇家航空前 CEO 被曝机上违规使用充电宝引发火情，公司提请指控" data-date="11-14 21:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 21:28</span>
          <span class="news-item-title">荷兰皇家航空前 CEO 被曝机上违规使用充电宝引发火情，公司提请指控</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，据央视新闻今天（14 日）晚间报道，荷兰皇家航空公司前首席执行官（CEO）卡米尔 · 厄尔林斯 9 月在该公司…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-14/10732179.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明11月14日电 (罗婕)近日，云南省人民政府印发《云南省文化和旅游发展“十五五”规划》(以下简称《规划》)，该省将加强保护传承，构建不可移动文物资源“一张图”，建立非遗资源总目录。" data-title="文物“一张图”非遗“一本账” 云南“十五五”将加强文化遗产保护传承" data-date="11-14 21:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 21:19</span>
          <span class="news-item-title">文物“一张图”非遗“一本账” 云南“十五五”将加强文化遗产保护传承</span>
          <span class="news-value-point">💡 中新网昆明11月14日电 (罗婕)近日，云南省人民政府印发《云南省文化和旅游发展“十五五”规划》(以下简称《规划》)，该省将加强保护传承，构建不…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-14/10732168.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海11月14日电 题：荷兰学者奥雷·伯曼：万里归来，“东游”未止" data-title="荷兰学者奥雷·伯曼：万里归来，“东游”未止" data-date="11-14 21:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 21:06</span>
          <span class="news-item-title">荷兰学者奥雷·伯曼：万里归来，“东游”未止</span>
          <span class="news-value-point">💡 中新网上海11月14日电 题：荷兰学者奥雷·伯曼：万里归来，“东游”未止</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-14/10732161.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原11月14日电 (记者 李庭耀)山西省公安厅14日集中公布6起涉嫌新型黑恶违法犯罪典型案例，共抓获犯罪嫌疑人22名。" data-title="山西公安公布一批涉嫌新型黑恶违法犯罪典型案例 22人落网" data-date="11-14 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 21:01</span>
          <span class="news-item-title">山西公安公布一批涉嫌新型黑恶违法犯罪典型案例 22人落网</span>
          <span class="news-value-point">💡 中新网太原11月14日电 (记者 李庭耀)山西省公安厅14日集中公布6起涉嫌新型黑恶违法犯罪典型案例，共抓获犯罪嫌疑人22名</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/save-up-to-usd800-on-an-ibuypower-gaming-pc-right-now-in-this-massive-black-friday-sale-coupon-code-knocks-up-to-usd200-extra-off-high-spec-pre-built-rigs-fitted-with-nvidia-and-amd-gpus" target="_blank" rel="noopener" data-cat="zonghe" data-summary="iBuyPower将于今年11月针对新款游戏电脑开展为期一个月的黑色星期五促销活动。" data-title="Save up to $800 on an iBuyPower gaming PC right now in this massive Black Friday sale" data-date="11-14 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 21:00</span>
          <span class="news-item-title">现在，在这次盛大的黑色星期五促销活动中，购买iBuyPower游戏电脑最高可节省800美元</span>
          <span class="news-item-title-en">Save up to $800 on an iBuyPower gaming PC right now in this massive Black Friday sale</span>
          <span class="news-value-point">💡 iBuyPower将于今年11月针对新款游戏电脑开展为期一个月的黑色星期五促销活动</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1033761/home-assistant-tk-tripod-tabletop-installer" target="_blank" rel="noopener" data-cat="zonghe" data-summary="大家好！欢迎来到Installer第152期，这里是您了解世界上最棒、最Verge的事物的指南。（如果您是新来的，欢迎您，感谢您抽空离开塞尔达来到这里，您还可以在Installer主页上阅读所有旧版。）" data-title="A gadget to make your dumb house smarter" data-date="11-14 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 21:00</span>
          <span class="news-item-title">让您的“傻瓜”房屋变得更智能的小工具</span>
          <span class="news-item-title-en">A gadget to make your dumb house smarter</span>
          <span class="news-value-point">💡 大家好</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/live-blog/12040/13612004/wales-vs-new-zealand-england-vs-japan-live-nations-championship-updates-latest-scores-team-news-commentary-from-cardiff-twickenham" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Wales vs New Zealand LIVE! Hosts stun All Blacks with two tries inside six minutes" data-title="Wales vs New Zealand LIVE! Hosts stun All Blacks with two tries inside six minutes" data-date="11-14 20:45" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 20:45</span>
          <span class="news-item-title">威尔士对阵新西兰直播！主队在6分钟内两次达阵，令全黑队措手不及</span>
          <span class="news-item-title-en">Wales vs New Zealand LIVE! Hosts stun All Blacks with two tries inside six minutes</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/live-blog/12040/13611907/grand-slam-of-darts-leg-by-leg-highlights-scores-from-wolverhampton-with-stephen-bunting-luke-littler-and-luke-humphries-in-action" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Grand Slam of Darts LIVE! Bunting, Aspinall headline opening Saturday" data-title="Grand Slam of Darts LIVE! Bunting, Aspinall headline opening Saturday" data-date="11-14 20:45" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 20:45</span>
          <span class="news-item-title">镖神大赛直播！邦廷、阿斯皮诺尔领衔周六揭幕战</span>
          <span class="news-item-title-en">Grand Slam of Darts LIVE! Bunting, Aspinall headline opening Saturday</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-14/10732158.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网绍兴11月14日电(项菁)王羲之、陆游、王阳明、鲁迅……浙江绍兴历代名士相关遗迹点，被一张手绘导览图串珠成链。“有了这张图，我对绍兴文化有了更深入的了解，也让这次研学体验更充实。”游客王朝受访时说。" data-title="串联陆游、鲁迅等名人古迹 浙江绍兴循图Citywalk引游人" data-date="11-14 20:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 20:41</span>
          <span class="news-item-title">串联陆游、鲁迅等名人古迹 浙江绍兴循图Citywalk引游人</span>
          <span class="news-value-point">💡 中新网绍兴11月14日电(项菁)王羲之、陆游、王阳明、鲁迅……浙江绍兴历代名士相关遗迹点，被一张手绘导览图串珠成链</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-14/10732155.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川11月14日电 (记者 李佩珊)由宁夏图书馆主办的“国风雅韵·阅见宁夏”文旅市集14日在银川一处商圈举办。作为“阅游宁夏”全民阅读文旅融合服务项目重要板块，活动将阅读推广、非遗体验、传统技艺引入商业综合体，为市民打造集阅读、手作、演艺、闯关打卡于一体的沉浸式国风文化体验现场。" data-title="“国风雅韵·阅见宁夏”文旅市集开集 市民沉浸式感受国风盛宴" data-date="11-14 20:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 20:40</span>
          <span class="news-item-title">“国风雅韵·阅见宁夏”文旅市集开集 市民沉浸式感受国风盛宴</span>
          <span class="news-value-point">💡 中新网银川11月14日电 (记者 李佩珊)由宁夏图书馆主办的“国风雅韵·阅见宁夏”文旅市集14日在银川一处商圈举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-14/10732154.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月14日电 (记者 应妮)“凝眸对望——中荷女性艺术家沙龙”日前在北京大学举行。两国女性艺术家们就东西方视角下的艺术观念与情感、女性身份对创作的影响及未来可能、AI时代艺术与艺术家的价值等话题展开深入交流。" data-title="中荷女性艺术家在“凝眸对望”中对话交流" data-date="11-14 20:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 20:39</span>
          <span class="news-item-title">中荷女性艺术家在“凝眸对望”中对话交流</span>
          <span class="news-value-point">💡 中新网北京11月14日电 (记者 应妮)“凝眸对望——中荷女性艺术家沙龙”日前在北京大学举行</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-14 22:24（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
