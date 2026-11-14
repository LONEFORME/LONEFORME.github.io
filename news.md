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
      <span>2026-11-15 02:21 抓取更新</span>
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
        <span class="channel-count">49</span>
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
        <span class="channel-count">4</span>
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
  <div class="ov-item"><span class="ov-num">49</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-14/10732210.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社金边11月14日电 题：在柬埔寨金边“法语国家文化村”感受多元文化魅力" data-title="在柬埔寨金边“法语国家文化村”感受多元文化魅力" data-date="11-14 23:43" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-14 23:43</span>
      </div>
      <h2 class="hero-featured-title">在柬埔寨金边“法语国家文化村”感受多元文化魅力</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目。" data-title="The AI graveyard: a running list of projects and startups that didn’t make it" data-date="11-15 01:30" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">The AI graveyard: a running list of projects and startups that didn’t make it</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/boxing/news/12040/13612036/aaron-mckenna-to-defend-ibf-middleweight-world-title-against-jevgenijs-aleksejevs-live-on-sky-sports-on-december-4" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿伦·麦肯纳将于12月4日（星期五）捍卫他的中量级世界冠军头衔，比赛将在天空体育频道（Sky Sports）现场直播。" data-title="McKenna to defend world title live on Sky Sports on December 4" data-date="11-15 00:50" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">McKenna to defend world title live on Sky Sports on December 4</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/14/us/faa-groundstop-flights-restarting.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="由于数百架飞机不在位，机组人员也已下班，因此重启该国的飞行系统并非易事。" data-title="Here’s Why It Could Take Days for Flights to Return to Normal" data-date="11-15 01:46" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Here’s Why It Could Take Days for Flights to Return to Normal</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732210.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社金边11月14日电 题：在柬埔寨金边“法语国家文化村”感受多元文化魅力" data-title="在柬埔寨金边“法语国家文化村”感受多元文化魅力" data-date="11-14 23:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 23:43</span>
          <span class="news-item-title">在柬埔寨金边“法语国家文化村”感受多元文化魅力</span>
          <span class="news-value-point">💡 中新社金边11月14日电 题：在柬埔寨金边“法语国家文化村”感受多元文化魅力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732206.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月14日电 (记者 欧阳开宇)英国苏格兰格拉斯哥一栋公寓楼13日发生人为纵火引发的火灾，共计15名居民送医接受治疗。当地警方已将此次火情定性为蓄意案件并启动专项调查。" data-title="英国格拉斯哥公寓楼发生蓄意纵火案 15人送医" data-date="11-14 22:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 22:56</span>
          <span class="news-item-title">英国格拉斯哥公寓楼发生蓄意纵火案 15人送医</span>
          <span class="news-value-point">💡 中新社伦敦11月14日电 (记者 欧阳开宇)英国苏格兰格拉斯哥一栋公寓楼13日发生人为纵火引发的火灾，共计15名居民送医接受治疗</span>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-14/10732056.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月14日电 综合消息：伊朗伊斯兰革命卫队14日通报称，几小时内，至少有4艘油轮在霍尔木兹海峡触雷起火。联合国方面13日通报称，霍尔木兹海峡及更广泛的中东海域已发生134起商船袭击事件，造成25名海员死亡。" data-title="伊朗通报4艘油轮触雷起火 联合国通报134起商船袭击事件" data-date="11-14 17:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-14 17:13</span>
          <span class="news-item-title">伊朗通报4艘油轮触雷起火 联合国通报134起商船袭击事件</span>
          <span class="news-value-point">💡 中新社北京11月14日电 综合消息：伊朗伊斯兰革命卫队14日通报称，几小时内，至少有4艘油轮在霍尔木兹海峡触雷起火</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目。" data-title="The AI graveyard: a running list of projects and startups that didn’t make it" data-date="11-15 01:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-15 01:30</span>
          <span class="news-item-title">人工智能墓地：未成功完成的项目和初创公司的运行列表</span>
          <span class="news-item-title-en">The AI graveyard: a running list of projects and startups that didn’t make it</span>
          <span class="news-value-point">💡 从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/" target="_blank" rel="noopener" data-cat="keji" data-summary="一些政府已采取行动，确认芯片供应承诺，而另一些政府则在监测对本地项目的影响或处理正在进行的调查。" data-title="Asian governments react to Nvidia CEO Jensen Huang’s exit" data-date="11-15 00:34" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-15 00:34</span>
          <span class="news-item-title">亚洲各国政府对英伟达首席执行官黄仁勋离职一事作出回应</span>
          <span class="news-item-title-en">Asian governments react to Nvidia CEO Jensen Huang’s exit</span>
          <span class="news-value-point">💡 一些政府已采取行动，确认芯片供应承诺，而另一些政府则在监测对本地项目的影响或处理正在进行的调查</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-november-14-2026-mac-studio-versus-dgx-spark-amds-mext-cuts-dram-requirements-in-half-and-the-huang-saga-reaches-critical-mass" target="_blank" rel="noopener" data-cat="keji" data-summary="通过我们的订阅服务Tom&#39;s Hardware Premium，了解我们本周发布的所有内容，包括独家采访、本地人工智能深度解析等。" data-title="This week in Tom&#39;s Hardware Premium: November 14, 2026 — Mac Studio versus DGX Spark, AMD&#39;s MEXT cuts DRAM requirements in half, and the Huang saga reaches critical mass" data-date="11-15 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 00:00</span>
          <span class="news-item-title">本周《Tom's Hardware Premium》：2026年11月14日——Mac Studio与DGX Spark的对决，AMD的MEXT将DRAM要求减半，黄仁勋的传奇故事达到临界点</span>
          <span class="news-item-title-en">This week in Tom's Hardware Premium: November 14, 2026 — Mac Studio versus DGX Spark, AMD's MEXT cuts DRAM requirements in half, and the Huang saga reaches critical mass</span>
          <span class="news-value-point">💡 通过我们的订阅服务Tom's Hardware Premium，了解我们本周发布的所有内容，包括独家采访、本地人工智能深度解析等</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/u-s-treasury-secretary-questions-whether-nvidia-knowingly-sold-ai-gpus-to-shell-companies-says-company-itself-is-responsible-i-think-it-is-important-that-anyone-at-the-company-there-be-held-accountable-for-that" target="_blank" rel="noopener" data-cat="keji" data-summary="斯科特·贝森特（Scott Bessent）想知道英伟达的管理层是否知晓向空壳公司出售受限硬件一事，但他并未直接指责黄仁勋（Jensen Huang）。" data-title="U.S. Treasury Secretary questions whether Nvidia knowingly sold AI GPUs to shell companies, says company itself is responsible" data-date="11-14 23:35" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 23:35</span>
          <span class="news-item-title">美国财政部长质疑英伟达是否明知故犯地向空壳公司出售人工智能GPU，并表示公司本身应承担责任</span>
          <span class="news-item-title-en">U.S. Treasury Secretary questions whether Nvidia knowingly sold AI GPUs to shell companies, says company itself is responsible</span>
          <span class="news-value-point">💡 斯科特·贝森特（Scott Bessent）想知道英伟达的管理层是否知晓向空壳公司出售受限硬件一事，但他并未直接指责黄仁勋（Jensen Hua…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/247.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，今天（14 日）晚间，马斯克在 X 平台发文称，随着黄仁勋离任 CEO，英伟达将失去一些至关重要的商业合作。马斯克称赞黄仁勋在供应链管理方面表现出色，指出英伟达许多交易都是靠黄仁勋与合作方握手达成的，并没有签署书面合同。紧接着，马斯克又补充说：“如果黄仁勋答应向我交付算力，或者我要求加快零部件供应，他每次都能说到做到。当然，我们之后还是会补上采购订单，但我从来没有怀疑过他会兑现承诺。”据IT之家了解，就在昨天，马斯克发文回应网友关于“约 1600 名英伟达员工呼吁黄仁勋回归”的推文：一项要求让黄仁勋复职的请愿正在进行，我也会签署。相关阅读：《马斯克声援黄仁勋：将签署请愿，支持其重返英伟达 CEO 岗位》《马斯克谈黄仁勋结束 33 年掌舵英伟达生涯：创始人很难" data-title="马斯克再度力挺黄仁勋：没有他，英伟达将失去部分关键合作" data-date="11-14 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 23:28</span>
          <span class="news-item-title">马斯克再度力挺黄仁勋：没有他，英伟达将失去部分关键合作</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，今天（14 日）晚间，马斯克在 X 平台发文称，随着黄仁勋离任 CEO，英伟达将失去一些至关重要的商业合作</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/malaysia-plans-new-law-using-data-center-power-consumption-to-catch-ai-gpu-smugglers-but-real-world-tdp-variance-and-lack-of-physical-audits-could-undermine-it-new-law-also-forces-operators-to-pay-for-unused-electricity-capacity" target="_blank" rel="noopener" data-cat="keji" data-summary="马来西亚计划跟踪人工智能GPU进口和数据中心能耗，以打击芯片走私。但它能做到吗？" data-title="Malaysia plans new law using data center power consumption to catch AI GPU smugglers" data-date="11-14 23:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 23:10</span>
          <span class="news-item-title">马来西亚计划出台新法律，利用数据中心耗电量来抓捕人工智能GPU走私者</span>
          <span class="news-item-title-en">Malaysia plans new law using data center power consumption to catch AI GPU smugglers</span>
          <span class="news-value-point">💡 马来西亚计划跟踪人工智能GPU进口和数据中心能耗，以打击芯片走私</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/amds-fastest-gaming-cpu-and-the-radeon-rx-9070-just-hit-a-massive-usd550-discount-32gb-ddr5-ram-and-1tb-ssd-round-off-usd1-749-99-gaming-rig" target="_blank" rel="noopener" data-cat="keji" data-summary="除了Ryzen 7 9800X3D和Radeon RX 9070之外，购买者还将获得一个360mm AIO一体式水冷散热器、850W电源、32GB DDR5-5600内存和1TB固态硬盘，所有这些都装在一个配备RGB灯光的优质中塔式机箱内。" data-title="AMD&#39;s fastest gaming CPU and the Radeon RX 9070 just hit a massive $550 discount" data-date="11-14 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 23:00</span>
          <span class="news-item-title">AMD 最快的游戏 CPU 和 Radeon RX 9070 刚刚获得了高达 550 美元的巨额折扣</span>
          <span class="news-item-title-en">AMD's fastest gaming CPU and the Radeon RX 9070 just hit a massive $550 discount</span>
          <span class="news-value-point">💡 除了Ryzen 7 9800X3D和Radeon RX 9070之外，购买者还将获得一个360mm AIO一体式水冷散热器、850W电源、32G…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1032907/helen-toner-openai-cset-ai-safety-policy-interview" target="_blank" rel="noopener" data-cat="keji" data-summary="今天，我将与乔治敦大学安全与新兴技术中心的执行主任Helen Toner进行对话。本期节目是我们“人工智能在现实生活中的应用”系列的第二期。Helen是人工智能安全和政策领域的知名人士。" data-title="The OpenAI board member who fired Sam Altman says we still can’t trust AI CEOs" data-date="11-14 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 23:00</span>
          <span class="news-item-title">解雇萨姆·阿尔特曼的OpenAI董事会成员表示，我们仍然不能信任人工智能公司的首席执行官</span>
          <span class="news-item-title-en">The OpenAI board member who fired Sam Altman says we still can’t trust AI CEOs</span>
          <span class="news-value-point">💡 今天，我将与乔治敦大学安全与新兴技术中心的执行主任Helen Toner进行对话</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/245.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，根据 Intel（英特尔）官网页面，此前悄然上市的酷睿 Ultra 7 处理器 260K 实际上早在 2026 年第 3 季度就已发行。而从规格上来看，其大致相当于 Ultra 7 265K 的降频版。英特尔酷睿 Ultra 7 处理器 260K 的最大睿频频率为 5.4GHz、性能核最大睿频频率为 5.3GHz、能效核最大睿频频率为 4.5GHz，这三项数据均比 Ultra 7 265K 低 0.1GHz，但性能核与能效核的基本频率保持不变。同时，该处理器的内存支持为 DDR5 6400MT/s，暗示其并非 &quot;Arrow Lake Refresh&quot; 的一员，仍属于初代 &quot;Arrow Lake&quot;，晶粒间频率应该也会相对较低。此外，英特尔酷睿 Ultra 7" data-title="英特尔官网确认酷睿 Ultra 7 处理器 260K 规格，最大睿频频率 5.4GHz" data-date="11-14 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 22:51</span>
          <span class="news-item-title">英特尔官网确认酷睿 Ultra 7 处理器 260K 规格，最大睿频频率 5.4GHz</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，根据 Intel（英特尔）官网页面，此前悄然上市的酷睿 Ultra 7 处理器 260K 实际上早在 2026…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-allege-deepseek-kimi-and-other-chinese-ai-models-were-trained-on-export-controlled-nvidia-blackwell-chips-statistical-analysis-on-model-weights-reveals-high-correlation-to-nvidia-hardware" target="_blank" rel="noopener" data-cat="keji" data-summary="研究人员指出，DeepSeek、Kimi和其他中国人工智能模型是在受出口管制的Nvidia Blackwell芯片上训练的——对模型权重的统计分析显示，它们与Nvidia硬件具有高度相关性。" data-title="Researchers allege DeepSeek, Kimi, and other Chinese AI models were trained using banned Nvidia Blackwell GPUs" data-date="11-14 22:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 22:50</span>
          <span class="news-item-title">研究人员称，DeepSeek、Kimi和其他中国人工智能模型是在使用被禁用的Nvidia Blackwell GPU进行训练的。</span>
          <span class="news-item-title-en">Researchers allege DeepSeek, Kimi, and other Chinese AI models were trained using banned Nvidia Blackwell GPUs</span>
          <span class="news-value-point">💡 研究人员指出，DeepSeek、Kimi和其他中国人工智能模型是在受出口管制的Nvidia Blackwell芯片上训练的——对模型权重的统计分…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/244.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 14 日消息，过去几十年里，不想花钱买 Mac、却又希望使用 macOS 的用户，可以通过组装“黑苹果”电脑实现。不过，自从苹果改用自研 Arm 芯片后，黑苹果的安装难度大幅提高。据外媒 TechSpot 今天（14 日）晚间报道，近期出现的至少两个新项目，则试图让 macOS 登陆骁龙和 x86 平台。其中一个项目开发了 Arm 转 x86 指令翻译层，计划让大多数较新的英特尔和 AMD 处理器能够运行 macOS，早期版本现已开放试用。另一个项目则在搭载骁龙处理器的华硕 Zenbook 笔记本上成功启动 macOS，部分基本功能也能正常使用。黑苹果的历史可以追溯到 20 世纪 80 年代，但在非苹果设备上运行 macOS 直到 21 世纪初才逐渐流行。2006 年，苹" data-title="“黑苹果”有望卷土重来，新项目探索将 macOS 搬上骁龙和 x86 架构电脑" data-date="11-14 22:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 22:49</span>
          <span class="news-item-title">“黑苹果”有望卷土重来，新项目探索将 macOS 搬上骁龙和 x86 架构电脑</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，过去几十年里，不想花钱买 Mac、却又希望使用 macOS 的用户，可以通过组装“黑苹果”电脑实现</span>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">4 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13612036/aaron-mckenna-to-defend-ibf-middleweight-world-title-against-jevgenijs-aleksejevs-live-on-sky-sports-on-december-4" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿伦·麦肯纳将于12月4日（星期五）捍卫他的中量级世界冠军头衔，比赛将在天空体育频道（Sky Sports）现场直播。" data-title="McKenna to defend world title live on Sky Sports on December 4" data-date="11-15 00:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 00:50</span>
          <span class="news-item-title">麦肯纳将于 12 月 4 日在 Sky Sports 直播中捍卫世界冠军头衔</span>
          <span class="news-item-title-en">McKenna to defend world title live on Sky Sports on December 4</span>
          <span class="news-value-point">💡 阿伦·麦肯纳将于12月4日（星期五）捍卫他的中量级世界冠军头衔，比赛将在天空体育频道（Sky Sports）现场直播</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-united-women-vs-crystal-palace-women/report/575822" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联以 2-0 的压倒性优势战胜水晶宫，升至英超女足联赛第四名，玛雅·勒·蒂西耶在她的第 150 场俱乐部出场中以一记精彩的射门庆祝。" data-title="Le Tissier hits stunner to mark milestone in Man Utd win" data-date="11-14 18:54" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 18:54</span>
          <span class="news-item-title">勒·蒂西耶踢进精彩进球，为曼联的胜利立下里程碑</span>
          <span class="news-item-title-en">Le Tissier hits stunner to mark milestone in Man Utd win</span>
          <span class="news-value-point">💡 曼联以 2-0 的压倒性优势战胜水晶宫，升至英超女足联赛第四名，玛雅·勒·蒂西耶在她的第 150 场俱乐部出场中以一记精彩的射门庆祝</span>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/14/us/faa-groundstop-flights-restarting.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="由于数百架飞机不在位，机组人员也已下班，因此重启该国的飞行系统并非易事。" data-title="Here’s Why It Could Take Days for Flights to Return to Normal" data-date="11-15 01:46" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-15 01:46</span>
          <span class="news-item-title">以下是航班恢复正常可能需要数天的原因</span>
          <span class="news-item-title-en">Here’s Why It Could Take Days for Flights to Return to Normal</span>
          <span class="news-value-point">💡 由于数百架飞机不在位，机组人员也已下班，因此重启该国的飞行系统并非易事</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1033898/faa-ground-stop-sean-duffy-faa-copper-wire" target="_blank" rel="noopener" data-cat="zonghe" data-summary="交通部长肖恩·达菲（Sean Duffy）在今天的新闻发布会上表示，周五美国联邦航空管理局（FAA）下令的全国性地面停飞与一项工程有关，该工程是在“FAA的一个偏远设施”将老旧的铜线更换为光纤线路。部长表示，" data-title="Work to replace old copper wire led to the FAA’s ground stop" data-date="11-15 01:44" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-15 01:44</span>
          <span class="news-item-title">更换旧铜线的工程导致美国联邦航空管理局（FAA）下达地面停飞令</span>
          <span class="news-item-title-en">Work to replace old copper wire led to the FAA’s ground stop</span>
          <span class="news-value-point">💡 交通部长肖恩·达菲（Sean Duffy）在今天的新闻发布会上表示，周五美国联邦航空管理局（FAA）下令的全国性地面停飞与一项工程有关，该工程是…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/14/us/politics/ground-stop-air-traffic-faa.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近几个月来，美国联邦航空管理局的老化空中交通管制基础设施发生了数次造成中断的故障，而官员们一直在努力进行升级。" data-title="Ground Stop Highlights Chronic Vulnerabilities in Air Traffic System" data-date="11-15 00:36" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-15 00:36</span>
          <span class="news-item-title">停飞事件凸显航空交通系统的长期性脆弱性</span>
          <span class="news-item-title-en">Ground Stop Highlights Chronic Vulnerabilities in Air Traffic System</span>
          <span class="news-value-point">💡 近几个月来，美国联邦航空管理局的老化空中交通管制基础设施发生了数次造成中断的故障，而官员们一直在努力进行升级</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/samsungs-1tb-990-ssd-drops-to-19-cents-per-gb-amid-the-memory-crisis-grab-it-for-usd40-off" target="_blank" rel="noopener" data-cat="zonghe" data-summary="无论您是正在组装新电脑、扩展游戏库，还是更换旧的SATA硬盘，三星990都能让您轻松地为系统添加高速PCIe 4.0存储。" data-title="Samsung&#39;s 1TB 990 SSD drops to 19 cents per GB amid the memory crisis" data-date="11-15 00:32" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 00:32</span>
          <span class="news-item-title">在存储器危机之际，三星1TB 990 SSD的价格降至每GB 19美分</span>
          <span class="news-item-title-en">Samsung's 1TB 990 SSD drops to 19 cents per GB amid the memory crisis</span>
          <span class="news-value-point">💡 无论您是正在组装新电脑、扩展游戏库，还是更换旧的SATA硬盘，三星990都能让您轻松地为系统添加高速PCIe 4.0存储</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13612236/meetmebythesea-gives-mcmanus-a-first-paddy-power-gold-cup" target="_blank" rel="noopener" data-cat="zonghe" data-summary="本·保林（Ben Pauling）的Meetmebythesea再次展现出对切尔滕纳姆赛场的喜爱，并为马主JP·麦克马纳斯（JP McManus）赢得了在久负盛名的帕迪·鲍尔金杯赛（Paddy Power Gold Cup）上的首场胜利。" data-title="Meetmebythesea gives McManus a first Paddy Power Gold Cup" data-date="11-15 00:03" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 00:03</span>
          <span class="news-item-title">Meetmebythesea为麦克马纳斯赢得首个Paddy Power金杯</span>
          <span class="news-item-title-en">Meetmebythesea gives McManus a first Paddy Power Gold Cup</span>
          <span class="news-value-point">💡 本·保林（Ben Pauling）的Meetmebythesea再次展现出对切尔滕纳姆赛场的喜爱，并为马主JP·麦克马纳斯（JP McManus…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13612238/spain-vs-england-james-trafford-set-to-replace-jordan-pickford-as-goalkeeper-and-how-does-thomas-tuchel-stop-lamine-yamal" target="_blank" rel="noopener" data-cat="zonghe" data-summary="面对世界上最出色的球队，托马斯·图赫尔的防守决策将是关键。而他需要做出很多决定。" data-title="A new No 1? How to stop Lamine Yamal? Tuchel&#39;s selection issues" data-date="11-15 00:02" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 00:02</span>
          <span class="news-item-title">新的头号球星？如何阻止拉明·亚马尔？图赫尔的选人问题</span>
          <span class="news-item-title-en">A new No 1? How to stop Lamine Yamal? Tuchel's selection issues</span>
          <span class="news-value-point">💡 面对世界上最出色的球队，托马斯·图赫尔的防守决策将是关键</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/we-tested-the-ram-saving-storage-tech-in-gears-of-war-e-day-up-to-3-7-gb-s-of-ssd-streaming-speed-saves-several-gigabytes-of-system-ram-usage" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，我们将重点关注一项鲜有讨论的技术，它在将这个视觉效果丰富、细节密集的虚拟世界带到硬件资源更为有限的系统方面发挥着同样重要的作用：旨在减少 RAM 使用量的存储技术。" data-title="We tested the RAM-saving storage tech in Gears of War: E-Day" data-date="11-14 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-14 23:30</span>
          <span class="news-item-title">我们在《战争机器：E日》中测试了节省内存的存储技术</span>
          <span class="news-item-title-en">We tested the RAM-saving storage tech in Gears of War: E-Day</span>
          <span class="news-value-point">💡 今天，我们将重点关注一项鲜有讨论的技术，它在将这个视觉效果丰富、细节密集的虚拟世界带到硬件资源更为有限的系统方面发挥着同样重要的作用：旨在减少 …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/norway-vs-wales/live/554107" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Nusa breaks Wales&#39; resistance in Oslo LIVE!" data-title="Nusa breaks Wales&#39; resistance in Oslo LIVE!" data-date="11-14 23:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 23:30</span>
          <span class="news-item-title">努萨在奥斯陆打破威尔士的防线，直播中！</span>
          <span class="news-item-title-en">Nusa breaks Wales' resistance in Oslo LIVE!</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/246.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 14 日消息，美国 CBS 电视台交通记者克里斯 · 范 · 克利夫在 X 平台发文称，收到一位美国政府高级官员的消息：导致全美航班地面停飞的故障设备已被查明并隔离。克利夫援引官员的话说，美国联邦航空管理局（FAA）认为，故障仅涉及一种“特定型号”的 20 年历史老路由器。“（系统）基本上是被负载压垮了，不过具体原因尚不清楚。”初步信息显示，路由器过载后开始传输不同步的数据，造成空管人员的语音通信线路出现杂音，还可能导致显示屏闪烁或黑屏，与 2025 年纽瓦克自由国际机场发生的故障类似。据IT之家此前报道，当地时间 14 日，航班追踪网站 FlightAware 的数据显示，在 13 日空管系统出现通信故障、导致全美所有飞机停飞后，14 日，美国境内及往返美国的航班已有超" data-title="导致全美航班停飞的“罪魁祸首”找到了？FAA 调查指向 20 年历史路由器" data-date="11-14 23:06" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 23:06</span>
          <span class="news-item-title">导致全美航班停飞的“罪魁祸首”找到了？FAA 调查指向 20 年历史路由器</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，美国 CBS 电视台交通记者克里斯 · 范 · 克利夫在 X 平台发文称，收到一位美国政府高级官员的消息：导致…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1032500/best-deals-rei-holiday-sale-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="黑色星期五已经成为一个独立的购物季，零售商再次在真正的购物节到来之前就提前提供折扣。我们已经整理了一些我们发现的最佳黑色星期五提前优惠，但如果您正在寻找" data-title="Here are our favorite deals from REI’s giant Holiday Sale" data-date="11-14 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-14 23:00</span>
          <span class="news-item-title">以下是我们最喜爱的REI大型假日促销优惠</span>
          <span class="news-item-title-en">Here are our favorite deals from REI’s giant Holiday Sale</span>
          <span class="news-value-point">💡 黑色星期五已经成为一个独立的购物季，零售商再次在真正的购物节到来之前就提前提供折扣</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/243.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 14 日消息，OPPO 官方微博发文，展示了 OPPO Reno17 系列手机提供的洛天依定制主题，相应主题仅限 Reno17 系列机型使用，包含 4 款专属锁屏 + 壁纸，提供洛天依三色全新造型及 Q 版形象锁屏。除此之外，相应主题包括时间、待办、步数等多种趣味组件及跟手粒子、下雪动效、充电动画等专属交互动效。IT之家注意到，先前相应手机规格已曝光，具体参数如下：OPPO Reno176.56 英寸 1.5K LTPS 直屏骁龙 7 Gen4 处理器前置 50Mp 镜头，后置 50Mp 主摄 +50Mp 超广角 +50Mp 3.5X 潜望长焦8000mAh 电池 +80W 快充金属中框，光学指纹OPPO Reno17 Pro6.32 英寸 1.5K LTPS 直屏天玑" data-title="OPPO 展示 Reno17 系列手机洛天依联动定制主题，11 月 16 日发布" data-date="11-14 22:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 22:43</span>
          <span class="news-item-title">OPPO 展示 Reno17 系列手机洛天依联动定制主题，11 月 16 日发布</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，OPPO 官方微博发文，展示了 OPPO Reno17 系列手机提供的洛天依定制主题，相应主题仅限 Reno1…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/242.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 14 日消息，华硕 (ASUS) 今日公布了鼠标新品 ROG 龙鳞 (Harpe) 2 Ace Mini。这一型号由华硕与《无畏契约》世界冠军选手 Max &quot;Demon1&quot; Mazanov 共同打造，结合最新硬件和面向抓握与指握用户的紧凑型半对称模具。龙鳞 2 Ace Mini 三维 118.2 × 61.3 × 40.2 (mm)，质量 47g；配备 ROG AimPoint Pro 65K 传感器、ROG 100M 光学微动开关；支持三模连接，搭载第二代 ROG SpeedNova 8K 无线技术；可选暗夜黑、月耀白、晴空蓝、熔岩红 4 种常规配色。除常规版本外，华硕还带来了 &quot;Demon1&quot; 联名款的龙鳞 2 Ace Mini。其拥有渐变淡紫色涂装、&quot;Demon1&quot;" data-title="华硕 ROG 带来龙鳞 2 Ace Mini 鼠标，&quot;Demon1&quot; 联名款同步亮相" data-date="11-14 22:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 22:40</span>
          <span class="news-item-title">华硕 ROG 带来龙鳞 2 Ace Mini 鼠标，"Demon1" 联名款同步亮相</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，华硕 (ASUS) 今日公布了鼠标新品 ROG 龙鳞 (Harpe) 2 Ace Mini</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13612201/dp-world-tour-championship-eugenio-chacarra-edges-back-ahead-of-rory-mcilroy-in-race-to-dubai-battle-ahead-of-final-day" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在第三轮比赛中表现出色后，尤金尼奥·查卡拉（Eugenio Chacarra）不仅希望在DP世界巡回锦标赛上阻止罗里·麦克罗伊（Rory McIlroy）赢得迪拜争霸赛的胜利，而且还希望取得更多成就。" data-title="Chacarra reveals plan for &#39;dream&#39; win over McIlroy and &#39;Dubai double&#39;" data-date="11-14 22:35" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 22:35</span>
          <span class="news-item-title">查卡拉透露了战胜麦克罗伊和“迪拜双冠”的“梦想”计划</span>
          <span class="news-item-title-en">Chacarra reveals plan for 'dream' win over McIlroy and 'Dubai double'</span>
          <span class="news-value-point">💡 在第三轮比赛中表现出色后，尤金尼奥·查卡拉（Eugenio Chacarra）不仅希望在DP世界巡回锦标赛上阻止罗里·麦克罗伊（Rory McI…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/241.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 14 日消息，据央视新闻报道，当地时间 11 月 14 日，航班追踪网站 FlightAware 的数据显示，在 13 日空管系统出现通信故障、导致全美所有飞机停飞后，14 日，美国境内及往返美国的航班已有超过 3300 架次被取消。截至美国东部时间 14 日 6 时 15 分（IT之家注：北京时间 14 日 19 时 15 分），达美航空已取消当日计划航班的 19%，联合航空取消了 16%，美国航空则取消了 14%。美国联邦航空管理局 13 日发布全美地面停飞令，暂停国内机场航班起飞超过 4 个小时，导致上万架次航班延误或取消。美官方表示，航班大规模停飞的原因仍在调查中，但可能由设备老旧带来的通信故障引发。相关阅读：《美国突发全国性航班停飞，欧洲航空安全组织暂停成员国赴" data-title="受空管系统故障影响，11 月 14 日美国仍有超 3300 架次航班被取消" data-date="11-14 22:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 22:25</span>
          <span class="news-item-title">受空管系统故障影响，11 月 14 日美国仍有超 3300 架次航班被取消</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，据央视新闻报道，当地时间 11 月 14 日，航班追踪网站 FlightAware 的数据显示，在 13 日空…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/240.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 14 日消息，当地时间 11 月 5 日，意媒 Quattroruote 援引不具名知情人士消息称，小米与 HWA 或在秘密合作开发一款超高性能汽车，部分知名零部件供应商也有望参与其中。IT之家注：HWA 由 AMG 创始人汉斯 · 维尔纳 · 奥夫雷希特创办，脱胎于 AMG，长期负责奔驰的赛车项目，这其中就包括德国房车大师赛（DTM）。双方据称希望打造一款性能前所未有、足以载入汽车史册的车型。新车的具体形式仍未确定，既有可能是全新的旗舰车型，也有可能是小米现有两款车型（SU7/YU7）的极致性能版。▲ 现款小米 SU7 Ultra过去几周，多辆采用更激进设计的 SU7 Ultra 测试车现身纽博格林赛道。该媒体分析称，不排除小米已在开发更侧重赛道性能的 SU7 Ultr" data-title="曝小米与“AMG 之父”创办的 HWA 秘密合作，希望打造“载入史册”新车" data-date="11-14 22:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-14 22:20</span>
          <span class="news-item-title">曝小米与“AMG 之父”创办的 HWA 秘密合作，希望打造“载入史册”新车</span>
          <span class="news-value-point">💡 IT之家 11 月 14 日消息，当地时间 11 月 5 日，意媒 Quattroruote 援引不具名知情人士消息称，小米与 HWA 或在秘密…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-15 02:21（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
