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
      <span>2026-11-08 01:47 抓取更新</span>
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
        <span class="channel-count">56</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">13</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">13</span>
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
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×11 · 天空体育×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/06/us/politics/susie-wiles-chief-of-staff-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新任白宫办公厅主任负责特朗普总统第二任期内一些最具挑衅性的政策，以及对行政权力的激进态度。" data-title="In Elevating Stephen Miller, Trump Doubles Down on Hard" data-date="11-08 01:23" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-08 01:23</span>
      </div>
      <h2 class="hero-featured-title">在《提升斯蒂芬·米勒》中，特朗普加倍努力</h2>
      <div class="hero-featured-title-en">In Elevating Stephen Miller, Trump Doubles Down on Hard</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government" target="_blank" rel="noopener" data-cat="keji" data-summary="有人担心，在审查获准处理该公司H200人工智能芯片的中国公司时，商务部和英伟达都没有进行尽职调查。据《纽约时报》报道， New Matrix在" data-title="The US let Nvidia sell chips to an empty office in China" data-date="11-07 23:43" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">The US let Nvidia sell chips to an empty office in China</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/nov/07/nottingham-forest-v-manchester-city-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从格林尼治标准时间下午5点30分开始的⚽英超联赛⚽现场比分更新|完整表格|在TikTok上关注我们|邮件TomWe &#39;re off at the City Ground。在开球之前，我们将听到The Last Post。Remembrance Sunday is tomorrow.继续阅读..." data-title="Nottingham Forest v Manchester City: Premier League" data-date="11-08 01:47" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Nottingham Forest v Manchester City: Premier League</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/nov/07/fulham-newcastle-premier-league-match-report" target="_blank" rel="noopener" data-cat="zonghe" data-summary="罗德里戈·穆尼兹（ Rodrigo Muniz ）从替补席上下来，为富勒姆（ Fulham ）抢救一分，并在艰难的一周后否认马蒂亚斯·贾斯尔（ Mat在所有比赛的五场比赛中，纽卡斯尔在四场失利后表现有所改善，但他们无法" data-title="Muniz rescues late point for Fulham against Newcastle after Murphy stunner" data-date="11-08 01:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Muniz rescues late point for Fulham against Newcastle after Murphy stunner</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/us/politics/susie-wiles-chief-of-staff-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新任白宫办公厅主任负责特朗普总统第二任期内一些最具挑衅性的政策，以及对行政权力的激进态度。" data-title="In Elevating Stephen Miller, Trump Doubles Down on Hard" data-date="11-08 01:23" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 01:23</span>
          <span class="news-item-title">在《提升斯蒂芬·米勒》中，特朗普加倍努力</span>
          <span class="news-item-title-en">In Elevating Stephen Miller, Trump Doubles Down on Hard</span>
          <span class="news-value-point">💡 新任白宫办公厅主任负责特朗普总统第二任期内一些最具挑衅性的政策，以及对行政权力的激进态度</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-07/10728178.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉11月7日电 (记者 周璟)菲律宾统计局6日公布的数据显示，菲律宾9月失业人数升至286万，高于8月的277万和去年同期的196万。当月失业率为5.4%，高于8月的5.3%和去年同期的3.8%。" data-title="菲律宾9月失业人数升至286万 就业市场承压" data-date="11-07 23:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 23:04</span>
          <span class="news-item-title">菲律宾9月失业人数升至286万 就业市场承压</span>
          <span class="news-value-point">💡 中新社马尼拉11月7日电 (记者 周璟)菲律宾统计局6日公布的数据显示，菲律宾9月失业人数升至286万，高于8月的277万和去年同期的196万</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728184.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近日，我国完成全球首个千公里空芯光纤双向实时传输验证。这意味着我国在新一代通信网关键技术领域取得新的突破。" data-title="千公里仅3.43毫秒！我国新一代通信网技术取得新突破" data-date="11-07 22:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 22:51</span>
          <span class="news-item-title">千公里仅3.43毫秒！我国新一代通信网技术取得新突破</span>
          <span class="news-value-point">💡 近日，我国完成全球首个千公里空芯光纤双向实时传输验证</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728166.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="昨天(6日)，十四届全国人大常委会第二十五次会议表决通过《中华人民共和国检察公益诉讼法》，该法自2027年1月1日起施行。" data-title="原创性“中国方案”→国家法律制度 检察公益诉讼法明年起施行" data-date="11-07 21:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 21:45</span>
          <span class="news-item-title">原创性“中国方案”→国家法律制度 检察公益诉讼法明年起施行</span>
          <span class="news-value-point">💡 昨天(6日)，十四届全国人大常委会第二十五次会议表决通过《中华人民共和国检察公益诉讼法》，该法自2027年1月1日起施行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-07/10728150.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社金边11月7日电 据柬埔寨新闻社7日报道，柬埔寨国家打击网络诈骗委员会(CCOS)日前通报，该国过去16个月以来，累计对972个涉电诈地点采取行动，起诉并羁押犯罪嫌疑人5032名，遣返来自38个国家的2.3万余名外籍人员。" data-title="柬埔寨官方：过去16个月起诉并羁押电诈犯罪嫌疑人逾五千名" data-date="11-07 21:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 21:16</span>
          <span class="news-item-title">柬埔寨官方：过去16个月起诉并羁押电诈犯罪嫌疑人逾五千名</span>
          <span class="news-value-point">💡 中新社金边11月7日电 据柬埔寨新闻社7日报道，柬埔寨国家打击网络诈骗委员会(CCOS)日前通报，该国过去16个月以来，累计对972个涉电诈地点…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728101.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月7日电 (记者 张晓曦)记者节来临之际，中华全国新闻工作者协会(简称“中国记协”)6日至7日在北京举办港澳台侨媒体“共庆节日 携手前行”采访联谊活动，来自港澳台地区及海外的华文媒体及部分在京媒体40余名记者参加。" data-title="中国记协邀港澳台侨媒体采访联谊" data-date="11-07 21:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 21:05</span>
          <span class="news-item-title">中国记协邀港澳台侨媒体采访联谊</span>
          <span class="news-value-point">💡 中新网北京11月7日电 (记者 张晓曦)记者节来临之际，中华全国新闻工作者协会(简称“中国记协”)6日至7日在北京举办港澳台侨媒体“共庆节日 携…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-07/10728061.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网悉尼11月7日电 11月7日下午，中国驻墨尔本总领事房新文应约同维多利亚州州长卡罗尔紧急通话。" data-title="中国驻墨尔本总领事就领区一名中国公民不幸遇害案件同维州州长紧急通话" data-date="11-07 20:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 20:52</span>
          <span class="news-item-title">中国驻墨尔本总领事就领区一名中国公民不幸遇害案件同维州州长紧急通话</span>
          <span class="news-value-point">💡 中新网悉尼11月7日电 11月7日下午，中国驻墨尔本总领事房新文应约同维多利亚州州长卡罗尔紧急通话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728126.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社西宁11月7日电(记者柳泽兴)学习贯彻党的二十届五中全会精神中央宣讲团11月6日至7日在青海宣讲，中央宣讲团成员、中央社会工作部部长吴汉圣作宣讲报告。" data-title="学习贯彻党的二十届五中全会精神丨学习贯彻党的二十届五中全会精神中央宣讲团在青海宣讲" data-date="11-07 20:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 20:47</span>
          <span class="news-item-title">学习贯彻党的二十届五中全会精神丨学习贯彻党的二十届五中全会精神中央宣讲团在青海宣讲</span>
          <span class="news-value-point">💡 新华社西宁11月7日电(记者柳泽兴)学习贯彻党的二十届五中全会精神中央宣讲团11月6日至7日在青海宣讲，中央宣讲团成员、中央社会工作部部长吴汉圣…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728127.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：记者11月7日从海军航空大学获悉，海军首批舰载机女飞行学员全部通过结业考核赴一线部队。这标志着海军航空兵人才梯队建设再添新生力量，海军舰载机飞行人才培养取得突破性进展。" data-title="海军首批舰载机女飞行学员结业赴一线部队" data-date="11-07 20:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 20:42</span>
          <span class="news-item-title">海军首批舰载机女飞行学员结业赴一线部队</span>
          <span class="news-value-point">💡 新华社快讯：记者11月7日从海军航空大学获悉，海军首批舰载机女飞行学员全部通过结业考核赴一线部队</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728105.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="党的新闻舆论工作是党的一项重要工作，是治国理政、定国安邦的大事。习近平总书记始终高度重视党的新闻舆论工作，关心关爱广大新闻工作者。11月8日中国记者节之际，一起重温总书记对新闻工作者的殷殷嘱托，牢记使命，永远向前。" data-title="学习新语｜习近平总书记殷切寄语新闻工作者" data-date="11-07 20:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 20:32</span>
          <span class="news-item-title">学习新语｜习近平总书记殷切寄语新闻工作者</span>
          <span class="news-value-point">💡 党的新闻舆论工作是党的一项重要工作，是治国理政、定国安邦的大事</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10728104.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月6日是北京市区和乡镇两级人大代表换届选举投票日。习近平总书记在西城区中南海选区怀仁堂投票站参加区人大代表的选举投票。" data-title="第一观察｜总书记投下庄严一票，率先垂范践行民主" data-date="11-07 20:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 20:20</span>
          <span class="news-item-title">第一观察｜总书记投下庄严一票，率先垂范践行民主</span>
          <span class="news-value-point">💡 11月6日是北京市区和乡镇两级人大代表换届选举投票日</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/us/politics/stephen-miller-white-house-chief-staff.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="米勒是特朗普总统大规模驱逐运动的设计师，一直是特朗普许多移民政策的公众形象。" data-title="What to Know About Stephen Miller, Trump’s New Chief of Staff" data-date="11-07 10:56" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 10:56</span>
          <span class="news-item-title">关于特朗普新任幕僚长斯蒂芬·米勒（ Stephen Miller ）的须知</span>
          <span class="news-item-title-en">What to Know About Stephen Miller, Trump’s New Chief of Staff</span>
          <span class="news-value-point">💡 米勒是特朗普总统大规模驱逐运动的设计师，一直是特朗普许多移民政策的公众形象</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/us/politics/susie-wiles-trump-women.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="过去一年，一波高级别女性离开了特朗普政府。许多人被男人取代。" data-title="Susie Wiles Is the Latest Powerful Woman to Exit the Trump Administration" data-date="11-07 07:53" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 07:53</span>
          <span class="news-item-title">苏茜·怀尔斯（ Susie Wiles ）是退出特朗普政府的最新强大女性</span>
          <span class="news-item-title-en">Susie Wiles Is the Latest Powerful Woman to Exit the Trump Administration</span>
          <span class="news-value-point">💡 过去一年，一波高级别女性离开了特朗普政府</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government" target="_blank" rel="noopener" data-cat="keji" data-summary="有人担心，在审查获准处理该公司H200人工智能芯片的中国公司时，商务部和英伟达都没有进行尽职调查。据《纽约时报》报道， New Matrix在" data-title="The US let Nvidia sell chips to an empty office in China" data-date="11-07 23:43" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 23:43</span>
          <span class="news-item-title">美国允许英伟达向中国一间空置办公室出售芯片</span>
          <span class="news-item-title-en">The US let Nvidia sell chips to an empty office in China</span>
          <span class="news-value-point">💡 有人担心，在审查获准处理该公司H200人工智能芯片的中国公司时，商务部和英伟达都没有进行尽职调查</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos" target="_blank" rel="noopener" data-cat="keji" data-summary="今天，我正在与Cognition首席安全官兼长期网络安全专家Alex Stamos谈论网络安全目前的混乱局面。本集是关于现实生活中的人工智能的特别系列的一部分。我一直很喜欢聊天" data-title="AI broke the cybersecurity world. What’s next?" data-date="11-07 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 23:00</span>
          <span class="news-item-title">人工智能打破了网络安全的世界。下一步是什么？</span>
          <span class="news-item-title-en">AI broke the cybersecurity world. What’s next?</span>
          <span class="news-value-point">💡 今天，我正在与Cognition首席安全官兼长期网络安全专家Alex Stamos谈论网络安全目前的混乱局面</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/824.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 7 日消息，美国联邦治安法官谢文辉（Alex Tse）裁定，Anthropic 必须继续应对 Claude Max 套餐使用额度涉嫌误导消费者的主要指控。据 Courthouse News 报道，谢文辉周五驳回了案件中的其他几项诉求。Anthropic 宣传称，月费 100 美元（IT之家注：现汇率约合 668.6 元人民币）和 200 美元（现汇率约合 1,337 元人民币）的 Max 套餐，使用额度分别是 Pro 套餐的 5 倍和 20 倍。但今年 6 月提起诉讼的消费者指控，如果按整周计算，实际额度远远达不到宣传中的倍数。两名原告卡尔 · 卡恩和所罗门 · 史密斯计算发现，以 Claude 的一款模型为例，200 美元（现汇率约合 1,337 元人民币）套餐的每周额" data-title="Claude Max 订阅套餐使用额度被指“虚标”，Anthropic 辩词未获法官采纳" data-date="11-07 22:57" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 22:57</span>
          <span class="news-item-title">Claude Max 订阅套餐使用额度被指“虚标”，Anthropic 辩词未获法官采纳</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，美国联邦治安法官谢文辉（Alex Tse）裁定，Anthropic 必须继续应对 Claude Max 套餐使用…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/823.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 7 日消息，当地时间 11 月 5 日，GitHub 发布博文，称上周在 GitHub Universe 大会上，正式公布了全新的 Git 存储架构，代号“Rubicon”。官方表示，该架构不仅具备每秒处理数千次写入的能力，还能实现读取按需水平扩展。经内部压力测试验证，新架构能够在保持极低读取延迟的同时，支持单个代码仓库容纳 5000 个智能体（Agent）并发协作，并承受每秒高达 7200 次的代码推送。IT之家获悉，该架构目前已经开启小范围定向内测（limited private preview），并计划于明年初逐步扩大开放范围。据介绍，如今 GitHub 上最繁忙的代码仓库，其单秒写入峰值最多也不过数十次，且往往呈现短暂脉冲式的突发状态。然而，随着越来越多的研发工作" data-title="GitHub 推出新 Git 存储架构：内部测试单个代码仓库支持 5000 个智能体同时协作，每秒处理 7200 次推送" data-date="11-07 22:57" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 22:57</span>
          <span class="news-item-title">GitHub 推出新 Git 存储架构：内部测试单个代码仓库支持 5000 个智能体同时协作，每秒处理 7200 次推送</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，当地时间 11 月 5 日，GitHub 发布博文，称上周在 GitHub Universe 大会上，正式公布了…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/822.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 7 日消息，据 RT今日俄罗斯报道，当地时间 11 月 6 日，特斯拉 CEO 埃隆 · 马斯克接受投资者罗恩 · 巴伦采访时表示，他热爱中国，并高度评价中国汽车工业的竞争力。“中国令人惊叹。顺便说一句，我爱中国。去那里旅行令人深受鼓舞，”马斯克在采访中说。他同时指出，在上海生产的特斯拉 Model Y 是中国最畅销的电动汽车，但强调实现这一成绩“并不容易”。马斯克特别补充道：“中国汽车公司非常厉害。”据IT之家此前报道，今年 9 月，马斯克接受了央视财经专访。当谈及 AI，他表示中国的 AI 大模型整体而言非常出色，单位算力产出的性能几乎全球顶尖。他认为，中国解决算力问题的速度会比大多数人预想更快。粗略估计，大概两到三年内，中国就能依靠光刻技术与芯片制造补齐算力缺口。图" data-title="马斯克再次表白中国，称赞中国汽车工业水平高" data-date="11-07 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 22:51</span>
          <span class="news-item-title">马斯克再次表白中国，称赞中国汽车工业水平高</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，据 RT今日俄罗斯报道，当地时间 11 月 6 日，特斯拉 CEO 埃隆 · 马斯克接受投资者罗恩 · 巴伦采访…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips" target="_blank" rel="noopener" data-cat="keji" data-summary="美国情报人士表示， Nvidia首席执行官黄延森(Jensen Huang)在涉及Megaspeed高管黄爱丽丝(Alice Huang)的“蜜罐”行动中成为中国情报部门的目标。" data-title="US intelligence believes Jensen Huang had affair with Chinese spy in honeypot operation" data-date="11-07 22:47" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-07 22:47</span>
          <span class="news-item-title">美国情报部门认为Jensen Huang在蜜罐操作中与中国间谍有染</span>
          <span class="news-item-title-en">US intelligence believes Jensen Huang had affair with Chinese spy in honeypot operation</span>
          <span class="news-value-point">💡 美国情报人士表示， Nvidia首席执行官黄延森(Jensen Huang)在涉及Megaspeed高管黄爱丽丝(Alice Huang)的“蜜…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security" target="_blank" rel="noopener" data-cat="keji" data-summary="由于有关中国阴谋的报道，英伟达的Jensen Huang正式致电国会—官员们提到对国家安全的担忧日益增加" data-title="Nvidia&#39;s Jensen Huang officially called to Congress due to reports of a Chinese spy plot" data-date="11-07 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-07 21:30</span>
          <span class="news-item-title">由于有关中国间谍阴谋的报道，英伟达的Jensen Huang正式被召集到国会</span>
          <span class="news-item-title-en">Nvidia's Jensen Huang officially called to Congress due to reports of a Chinese spy plot</span>
          <span class="news-value-point">💡 由于有关中国阴谋的报道，英伟达的Jensen Huang正式致电国会—官员们提到对国家安全的担忧日益增加</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达要求台积电生产“3D DRAM”来解决内存短缺问题。" data-title="TSMC denies exploring 3D DRAM at Nvidia&#39;s request" data-date="11-07 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-07 21:00</span>
          <span class="news-item-title">台积电否认应英伟达要求探索3D DRAM</span>
          <span class="news-item-title-en">TSMC denies exploring 3D DRAM at Nvidia's request</span>
          <span class="news-value-point">💡 据报道，英伟达要求台积电生产“3D DRAM”来解决内存短缺问题</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508264.html" target="_blank" rel="noopener" data-cat="keji" data-summary="苦单Session久矣，两大Agent玩家不谋而合。" data-title="抢跑DeepSeek！硅谷华人把下一代Agent Harness造出来了！？" data-date="11-07 13:01" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-07 13:01</span>
          <span class="news-item-title">抢跑DeepSeek！硅谷华人把下一代Agent Harness造出来了！？</span>
          <span class="news-value-point">💡 苦单Session久矣，两大Agent玩家不谋而合</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508244.html" target="_blank" rel="noopener" data-cat="keji" data-summary="全新的电脑病毒" data-title="AGENTS.MD，危险危险危险！！！" data-date="11-07 11:43" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-07 11:43</span>
          <span class="news-item-title">AGENTS.MD，危险危险危险！！！</span>
          <span class="news-value-point">💡 全新的电脑病毒</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/06/crusoe-sells-troubled-wyoming-data-center-project-to-google/" target="_blank" rel="noopener" data-cat="keji" data-summary="这笔交易凸显了开发大规模人工智能数据中心的挑战。" data-title="Crusoe sells troubled Wyoming data center project to Google" data-date="11-07 09:40" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 09:40</span>
          <span class="news-item-title">Crusoe将陷入困境的怀俄明州数据中心项目出售给谷歌</span>
          <span class="news-item-title-en">Crusoe sells troubled Wyoming data center project to Google</span>
          <span class="news-value-point">💡 这笔交易凸显了开发大规模人工智能数据中心的挑战</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，作为一轮融资的一部分， OpenAI又筹集了110亿美元，这轮融资尚未结束，但预计将在未来几周内完成。" data-title="OpenAI reportedly raises an additional $11 billion at a $1.25 trillion valuation" data-date="11-07 06:53" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 06:53</span>
          <span class="news-item-title">据报道， OpenAI以1.25万亿美元的估值额外筹集了110亿美元</span>
          <span class="news-item-title-en">OpenAI reportedly raises an additional $11 billion at a $1.25 trillion valuation</span>
          <span class="news-value-point">💡 据报道，作为一轮融资的一部分， OpenAI又筹集了110亿美元，这轮融资尚未结束，但预计将在未来几周内完成</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta的Muse代理继续获得新功能和集成。Spaces有望成为与人工智能助手互动的新方式。" data-title="Meta introduces Spaces, a new way to collaborate with your Muse agent" data-date="11-07 02:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 02:44</span>
          <span class="news-item-title">Meta引入了Spaces ，这是一种与Muse代理进行协作的新方法</span>
          <span class="news-item-title-en">Meta introduces Spaces, a new way to collaborate with your Muse agent</span>
          <span class="news-value-point">💡 Meta的Muse代理继续获得新功能和集成</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/07/nottingham-forest-v-manchester-city-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从格林尼治标准时间下午5点30分开始的⚽英超联赛⚽现场比分更新|完整表格|在TikTok上关注我们|邮件TomWe &#39;re off at the City Ground。在开球之前，我们将听到The Last Post。Remembrance Sunday is tomorrow.继续阅读..." data-title="Nottingham Forest v Manchester City: Premier League" data-date="11-08 01:47" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 01:47</span>
          <span class="news-item-title">诺丁汉森林v曼城：英超联赛</span>
          <span class="news-item-title-en">Nottingham Forest v Manchester City: Premier League</span>
          <span class="news-value-point">💡 从格林尼治标准时间下午5点30分开始的⚽英超联赛⚽现场比分更新|完整表格|在TikTok上关注我们|邮件TomWe 're off at the…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609399/arsenal-1-0-hull-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：阿森纳与赫尔在英超联赛中的比赛亮点。" data-title="Odegaard earns Arsenal narrow win over Hull to extend gap at the top" data-date="11-08 01:16" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:16</span>
          <span class="news-item-title">奥德加尔赢得了阿森纳对赫尔的狭隘胜利，以扩大顶部的差距</span>
          <span class="news-item-title-en">Odegaard earns Arsenal narrow win over Hull to extend gap at the top</span>
          <span class="news-value-point">💡 免费观看：阿森纳与赫尔在英超联赛中的比赛亮点</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609257/leeds-1-0-tottenham-hotspur-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：利兹队在英超联赛中对阵托特纳姆热刺队的比赛亮点。" data-title="Leeds end Spurs’ winning run in VAR controversy filled match" data-date="11-08 01:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:15</span>
          <span class="news-item-title">利兹结束马刺队在VAR争议充满比赛中的胜利</span>
          <span class="news-item-title-en">Leeds end Spurs’ winning run in VAR controversy filled match</span>
          <span class="news-value-point">💡 免费观看：利兹队在英超联赛中对阵托特纳姆热刺队的比赛亮点</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609384/fulham-1-1-newcastle-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：富勒姆和纽卡斯尔联队之间英超比赛的亮点。" data-title="Late goals as Fulham draw with Newcastle" data-date="11-08 01:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:10</span>
          <span class="news-item-title">与纽卡斯尔队一起打进富勒姆队的近期进球</span>
          <span class="news-item-title-en">Late goals as Fulham draw with Newcastle</span>
          <span class="news-value-point">💡 免费观看：富勒姆和纽卡斯尔联队之间英超比赛的亮点</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/07/arsenal-hull-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="正如大多数阿森纳球迷会作证的那样，耐心是一种美德。在22年的等待中，他们需要很多才能加冕英超冠军， Mikel Arteta的球队当然必须保持镇静，因为他们试图击败一个顽强的Hul" data-title="Martin Ødegaard extends Arsenal lead at top with winner to break Hull resistance" data-date="11-08 01:02" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 01:02</span>
          <span class="news-item-title">Martin Ødegaard以冠军延长阿森纳的领先优势，以打破船体阻力</span>
          <span class="news-item-title-en">Martin Ødegaard extends Arsenal lead at top with winner to break Hull resistance</span>
          <span class="news-value-point">💡 正如大多数阿森纳球迷会作证的那样，耐心是一种美德</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq62yp4lg831o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳和赫尔城的球员在阿联酋体育场的英超比赛后如何评分。" data-title="Goal caps eye-catching Odegaard display - player ratings for Arsenal v Hull" data-date="11-08 01:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 01:00</span>
          <span class="news-item-title">进球帽引人注目的Odegaard展示- Arsenal v Hull的球员评分</span>
          <span class="news-item-title-en">Goal caps eye-catching Odegaard display - player ratings for Arsenal v Hull</span>
          <span class="news-value-point">💡 阿森纳和赫尔城的球员在阿联酋体育场的英超比赛后如何评分</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/arsenal-vs-hull-city/report/559534" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马丁·奥德加德（ Martin Odegaard ）的进球以1比0战胜赫尔（ Hull ） ，让阿森纳在英超联赛中获得6分。" data-title="Odegaard clinches Arsenal win over stubborn Hull" data-date="11-08 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:00</span>
          <span class="news-item-title">奥德高击败阿森纳战胜顽固的船体</span>
          <span class="news-item-title-en">Odegaard clinches Arsenal win over stubborn Hull</span>
          <span class="news-value-point">💡 马丁·奥德加德（ Martin Odegaard ）的进球以1比0战胜赫尔（ Hull ） ，让阿森纳在英超联赛中获得6分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-08 00:52" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 00:52</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c39wz9llg255o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺将提交一份正式投诉，内容涉及在利兹失利期间不因Jayden Bogle对Mathys Tel的挑战而将其解雇的决定。" data-title="Tottenham set to complain to Pro Ref - but should Bogle have seen red?" data-date="11-08 00:35" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 00:35</span>
          <span class="news-item-title">托特纳姆热刺将向职业裁判投诉-但博格尔是否应该看到红色？</span>
          <span class="news-item-title-en">Tottenham set to complain to Pro Ref - but should Bogle have seen red?</span>
          <span class="news-value-point">💡 托特纳姆热刺将提交一份正式投诉，内容涉及在利兹失利期间不因Jayden Bogle对Mathys Tel的挑战而将其解雇的决定</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/nottingham-forest-vs-manchester-city/live/559542" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Cunha gives Forest early lead vs Man City LIVE! &amp; highlights" data-title="Cunha gives Forest early lead vs Man City LIVE! &amp; highlights" data-date="11-07 23:49" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 23:49</span>
          <span class="news-item-title">Cunha现场直播森林与曼城的早期领先优势！和亮点</span>
          <span class="news-item-title-en">Cunha gives Forest early lead vs Man City LIVE! & highlights</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/07/leeds-united-v-tottenham-hotspur-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺亚·奥卡福（ Noah Okafor ）抓住了埃兰路（ Elland Road ）激烈战斗的唯一目标，因为杰登·博格尔（ Jayden Bogle ）很好地逃脱了红色。对普通人来说，不同的大张旗鼓–最后一篇文章–听起来很尖锐。对堕落者的沉默而庄严的回忆。之后，托特纳姆热刺H" data-title="Leeds United 1-0 Tottenham Hotspur: Premier League – as it happened" data-date="11-07 23:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-07 23:03</span>
          <span class="news-item-title">利兹联队1-0托特纳姆热刺：英超联赛–事实如此</span>
          <span class="news-item-title-en">Leeds United 1-0 Tottenham Hotspur: Premier League – as it happened</span>
          <span class="news-value-point">💡 诺亚·奥卡福（ Noah Okafor ）抓住了埃兰路（ Elland Road ）激烈战斗的唯一目标，因为杰登·博格尔（ Jayden Bog…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/07/leeds-tottenham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="差不多一年后，利兹经理丹尼尔·法克（ Daniel Farke ）进行了战术大修，许多观察家认为这挽救了他的工作。那天，当利兹在曼城2-0落后时，法克放弃了他信任的4-3-3 ，尽管他们输了" data-title="Okafor’s Leeds winner adds insult to Tel’s injury for Tottenham as Bogle escapes red" data-date="11-07 22:34" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-07 22:34</span>
          <span class="news-item-title">奥卡福（ Okafor ）的利兹（ Leeds ）冠军侮辱了Tel对托特纳姆（ Tottenham ）的伤害，因为博格尔（ Bogle ）逃</span>
          <span class="news-item-title-en">Okafor’s Leeds winner adds insult to Tel’s injury for Tottenham as Bogle escapes red</span>
          <span class="news-value-point">💡 差不多一年后，利兹经理丹尼尔·法克（ Daniel Farke ）进行了战术大修，许多观察家认为这挽救了他的工作</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/leeds-united-vs-tottenham-hotspur/report/559540" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在白人后卫杰登·博格尔（ Jayden Bogle ）有争议的上半场红牌后，替补诺亚·奥卡福（ Noah Okafor ）的已故冠军让利兹（ Leeds ）以1比0主场战胜托特纳姆（ Tottenham" data-title="Leeds deservedly beat Spurs after Bogle escapes red card" data-date="11-07 22:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 22:30</span>
          <span class="news-item-title">博格尔逃出红牌后，利兹当之无愧地击败了马刺队</span>
          <span class="news-item-title-en">Leeds deservedly beat Spurs after Bogle escapes red card</span>
          <span class="news-value-point">💡 在白人后卫杰登·博格尔（ Jayden Bogle ）有争议的上半场红牌后，替补诺亚·奥卡福（ Noah Okafor ）的已故冠军让利兹（ L…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckly00wq495zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="詹姆斯·特拉福德表示，上赛季没有为曼城效力是“可怕的” ，让他别无选择，只能离开俱乐部，在夏天加盟利兹联队。" data-title="I left Man City for my mental wellbeing" data-date="11-07 15:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-07 15:16</span>
          <span class="news-item-title">我离开曼城是为了心理健康</span>
          <span class="news-item-title-en">I left Man City for my mental wellbeing</span>
          <span class="news-value-point">💡 詹姆斯·特拉福德表示，上赛季没有为曼城效力是“可怕的” ，让他别无选择，只能离开俱乐部，在夏天加盟利兹联队</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/06/premier-league-news-manchester-united-baleba-manchester-city-donnarumma-arsenal-arteta-rice" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳经理说“我们真的在照顾”中场球员，而Andoni Iraola则支持门将Alisson继续阅读..." data-title="Premier League news: Arteta insists Rice isn’t playing too many games" data-date="11-07 07:09" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-07 07:09</span>
          <span class="news-item-title">英超新闻：阿尔特塔坚持认为赖斯没有打太多比赛</span>
          <span class="news-item-title-en">Premier League news: Arteta insists Rice isn’t playing too many games</span>
          <span class="news-value-point">💡 阿森纳经理说“我们真的在照顾”中场球员，而Andoni Iraola则支持门将Alisson继续阅读...</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/07/fulham-newcastle-premier-league-match-report" target="_blank" rel="noopener" data-cat="zonghe" data-summary="罗德里戈·穆尼兹（ Rodrigo Muniz ）从替补席上下来，为富勒姆（ Fulham ）抢救一分，并在艰难的一周后否认马蒂亚斯·贾斯尔（ Mat在所有比赛的五场比赛中，纽卡斯尔在四场失利后表现有所改善，但他们无法" data-title="Muniz rescues late point for Fulham against Newcastle after Murphy stunner" data-date="11-08 01:00" data-source="卫报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 01:00</span>
          <span class="news-item-title">在Murphy Stunner之后， Muniz在富勒姆对阵纽卡斯尔的比赛中拯救了后期点</span>
          <span class="news-item-title-en">Muniz rescues late point for Fulham against Newcastle after Murphy stunner</span>
          <span class="news-value-point">💡 罗德里戈·穆尼兹（ Rodrigo Muniz ）从替补席上下来，为富勒姆（ Fulham ）抢救一分，并在艰难的一周后否认马蒂亚斯·贾斯尔（ …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1023230/the90-gem-necklace-hands-on-impressions" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着洛杉矶的气温上升到90年代，当我在8月份参加亲戚的户外派对时，避开炎热并不是一种选择。所以我坐在露台的雨伞下，旁边有一个强大的风扇，以为我受到保护，不受阳光照射，" data-title="The UV-tracking Gem made me rethink how sunlight affects my health, not just my appearance" data-date="11-08 01:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-08 01:00</span>
          <span class="news-item-title">紫外线追踪宝石让我重新思考阳光如何影响我的健康，而不仅仅是我的外表</span>
          <span class="news-item-title-en">The UV-tracking Gem made me rethink how sunlight affects my health, not just my appearance</span>
          <span class="news-value-point">💡 随着洛杉矶的气温上升到90年代，当我在8月份参加亲戚的户外派对时，避开炎热并不是一种选择</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/live-blog/12040/13608633/f1-sao-paulo-gp-qualifying-and-final-practice-updates-results-stream-and-highlights-from-brazil-formula-1-race-weekend-at-interlagos" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Sao Paulo GP: Rain arrives ahead of 6pm qualifying LIVE!" data-title="Sao Paulo GP: Rain arrives ahead of 6pm qualifying LIVE!" data-date="11-08 00:48" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 00:48</span>
          <span class="news-item-title">圣保罗大奖赛：在下午6点预选赛现场直播前降雨！</span>
          <span class="news-item-title-en">Sao Paulo GP: Rain arrives ahead of 6pm qualifying LIVE!</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/07/us/politics/schumer-election-democrats-senate.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这位民主党领导人仍然面临队伍中的怀疑论者和一些活动家的敌意，但助手们表示，他有足够的支持承诺，可以当选为多数党领袖。" data-title="Schumer Lifts His Senate Standing With an Election Blowout" data-date="11-08 00:22" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 00:22</span>
          <span class="news-item-title">舒默通过选举井喷提升参议院议席</span>
          <span class="news-item-title-en">Schumer Lifts His Senate Standing With an Election Blowout</span>
          <span class="news-value-point">💡 这位民主党领导人仍然面临队伍中的怀疑论者和一些活动家的敌意，但助手们表示，他有足够的支持承诺，可以当选为多数党领袖</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13609314/taurus-bay-dents-some-lofty-reputations-in-rising-stars" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在Taurus Bay在Aintree的Boodles Rising Stars新手Chase中首次亮相获胜后， Harry Redknapp可能会有另一个顶级前景。" data-title="Taurus Bay dents some lofty reputations in Rising Stars" data-date="11-08 00:04" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 00:04</span>
          <span class="news-item-title">金牛座湾在冉冉升起的新星中凹陷了一些崇高的声誉</span>
          <span class="news-item-title-en">Taurus Bay dents some lofty reputations in Rising Stars</span>
          <span class="news-value-point">💡 在Taurus Bay在Aintree的Boodles Rising Stars新手Chase中首次亮相获胜后， Harry Redknapp可…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/829.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，安卓阵营首款阔直板手机，也是酷派首款阔直板手机 Cool X Wide 今日正式开售。其中，8GB+128GB 版本 999 元，8GB+256GB 版本 1199 元，12GB+256GB 版本 1399 元。这款新机搭载 6.38 英寸 16:10 屏幕，仅 720x1158 分辨率，还支持 90Hz 刷新率；有鎏白、岩黑、嫣红三种配色可选，机身尺寸为 150.3×94.5×8.95mm，后置 5000 万像素摄像头。这款手机采用联发科曦力 G99 处理器，搭配 LPDDR4X 内存与 UFS 2.2 闪存，至高 12GB+256GB 存储，此外支持最大 256GB TF 卡扩展；电池容量 4600mAh。IT之家附参数如下：京东酷派 COOL X Wid" data-title="安卓阵营首款阔直板手机酷派 COOL X Wide 今日开售：999~1399 元，搭载联发科曦力 G99 芯片 + 720p 屏幕" data-date="11-08 00:00" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 00:00</span>
          <span class="news-item-title">安卓阵营首款阔直板手机酷派 COOL X Wide 今日开售：999~1399 元，搭载联发科曦力 G99 芯片 + 720p 屏幕</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，安卓阵营首款阔直板手机，也是酷派首款阔直板手机 Cool X Wide 今日正式开售</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1028917/legend-of-zelda-ocarina-of-time-remake-switch-2-costco-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="虽然一些零售商在重新制作的《塞尔达传说：时间之笛》上提供预购折扣，但如果您错过了，现在还不算太晚。Costco会员目前可以在线获得$ 5的数字版优惠，将价格降至" data-title="Costco members can get $5 off the reimagined Ocarina of Time" data-date="11-08 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-08 00:00</span>
          <span class="news-item-title">Costco会员可享受$ 5的时间之笛折扣</span>
          <span class="news-item-title-en">Costco members can get $5 off the reimagined Ocarina of Time</span>
          <span class="news-value-point">💡 虽然一些零售商在重新制作的《塞尔达传说：时间之笛》上提供预购折扣，但如果您错过了，现在还不算太晚</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1029474/discogs-kevin-lewandowski-aeropress-interview" target="_blank" rel="noopener" data-cat="zonghe" data-summary="二十五年前，凯文·莱万多夫斯基（ Kevin Lewandowski ）创立了Discogs ，可以说是各种黑胶唱片收藏家和音乐书呆子的网上目的地。显然，这是一个买卖唱片的市场，但它也变得更加重要。" data-title="Discogs’ Kevin Lewandowski can’t live without his AeroPress" data-date="11-08 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-08 00:00</span>
          <span class="news-item-title">Discogs的Kevin Lewandowski离不开他的AeroPress</span>
          <span class="news-item-title-en">Discogs’ Kevin Lewandowski can’t live without his AeroPress</span>
          <span class="news-value-point">💡 二十五年前，凯文·莱万多夫斯基（ Kevin Lewandowski ）创立了Discogs ，可以说是各种黑胶唱片收藏家和音乐书呆子的网上目的…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1029489/nyt-cooking-ai-assistant-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="每个工作日晚上7点左右，我发现自己站在冰箱前，试图选择一些不会让我丈夫抱怨的晚餐， “又是鸡？“是的，我应该多做一些饮食计划，但我没有，所以这就是我所在的地方，每晚一只蝙蝠" data-title="NYT Cooking’s AI assistant saved my weeknight chicken, but almost ruined my cake" data-date="11-07 23:50" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 23:50</span>
          <span class="news-item-title">纽约时报烹饪的AI助手拯救了我的工作夜鸡，但几乎毁了我的蛋糕</span>
          <span class="news-item-title-en">NYT Cooking’s AI assistant saved my weeknight chicken, but almost ruined my cake</span>
          <span class="news-value-point">💡 每个工作日晚上7点左右，我发现自己站在冰箱前，试图选择一些不会让我丈夫抱怨的晚餐， “又是鸡</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13609194/sao-paulo-gp-max-verstappen-fastest-in-final-practice-but-faces-grid-penalties-with-ferraris-lewis-hamilton-and-charles-leclerc" target="_blank" rel="noopener" data-cat="zonghe" data-summary="红牛的Max Verstappen在圣保罗大奖赛的最后练习中跑得最快，但将与法拉利的刘易斯·汉密尔顿和查尔斯·勒克莱尔一起进行罚球。" data-title="Verstappen fastest in final practice but faces grid penalties with Ferraris" data-date="11-07 23:44" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 23:44</span>
          <span class="news-item-title">Verstappen在最终练习中速度最快，但面临法拉利车队的罚款</span>
          <span class="news-item-title-en">Verstappen fastest in final practice but faces grid penalties with Ferraris</span>
          <span class="news-value-point">💡 红牛的Max Verstappen在圣保罗大奖赛的最后练习中跑得最快，但将与法拉利的刘易斯·汉密尔顿和查尔斯·勒克莱尔一起进行罚球</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/828.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 7 日消息，B站网友 @0x535A 发布视频，分享了自己的最新刷机成果 —— 为一台苹果 MacBook Pro 成功刷入了鸿蒙 HarmonyOS 6 系统，实现在 Mac 物理机上把鸿蒙系统跑了起来。视频画面显示，这台苹果 MacBook Pro 刷入的是鸿蒙 HarmonyOS 6 系统，机型显示为华为擎云 L410，应用小窗、全屏等功能正常。网友表示，还有很多问题没有解决，但嫁接 Linux 内核是非常好做法。据IT之家此前报道，今年 10 月，陆续有网友为第三方设备刷入了华为鸿蒙 HarmonyOS 系统，包括一台一加 Ace 5 和一台小米平板 6S Pro。此外，本月初，还有网友成功将华为二合一平板电脑 —— MateBook E Go 2023 刷入了" data-title="又一梦幻组合实现：网友成功将苹果 MacBook Pro 刷入华为鸿蒙 HarmonyOS 6 系统" data-date="11-07 23:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 23:40</span>
          <span class="news-item-title">又一梦幻组合实现：网友成功将苹果 MacBook Pro 刷入华为鸿蒙 HarmonyOS 6 系统</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，B站网友 @0x535A 发布视频，分享了自己的最新刷机成果 —— 为一台苹果 MacBook Pro 成功刷入…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-07/10728190.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者从消防、公安等多部门了解到，11月7日下午，沪武高速安徽潜山段发生一起多车追尾事故。沪武高速岳西往桐城南方向，一辆载有电池的货车发生自燃，后方多车追尾。目前事故伤亡情况还在了解中，记者从当地有关部门了解到，有人被送到医院治疗。" data-title="沪武高速潜山段发生多车追尾事故" data-date="11-07 23:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 23:40</span>
          <span class="news-item-title">沪武高速潜山段发生多车追尾事故</span>
          <span class="news-value-point">💡 记者从消防、公安等多部门了解到，11月7日下午，沪武高速安徽潜山段发生一起多车追尾事故</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609284/sao-paulo-gp-max-verstappen-goes-fastest-in-final-practice" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Max Verstappen在圣保罗大奖赛决赛练习中跑得最快。" data-title="Verstappen goes fastest in Sao Paulo GP final practice!" data-date="11-07 23:28" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 23:28</span>
          <span class="news-item-title">Verstappen在圣保罗GP决赛练习中跑得最快！</span>
          <span class="news-item-title-en">Verstappen goes fastest in Sao Paulo GP final practice!</span>
          <span class="news-value-point">💡 Max Verstappen在圣保罗大奖赛决赛练习中跑得最快</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13353569/leeds-united-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Leeds latest: Farke says &#39;butterfly&#39; Bogle is &#39;softest player&#39; in PL" data-title="Leeds latest: Farke says &#39;butterfly&#39; Bogle is &#39;softest player&#39; in PL" data-date="11-07 23:24" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 23:24</span>
          <span class="news-item-title">利兹最新消息：法克说“蝴蝶”博格尔在PL中是“最软的球员”</span>
          <span class="news-item-title-en">Leeds latest: Farke says 'butterfly' Bogle is 'softest player' in PL</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/827.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 7 日现场消息，今晚，在阿布扎比，比亚迪旗下超豪华行政旗舰轿车 —— 仰望鼎曜迎来全球首秀。随后，官方公布了鼎曜行政版的具体配置信息。IT之家从活动现场获悉，新车长宽高分别为 5600/2030/1590mm，轴距更是达到了 3500mm。新车拥有鼎形前脸和鼎形钻切大灯，点阵式格栅内部 137 颗宝石随光影流转，甲骨文车标更是由 24K 真金打造，号称“鼎立东方，气韵自成”。新车拥有首尾延展的 4.8 米贯穿式双腰线，并配备“中轴对开门”，前门开合角 80°，后门开合角 90°。内饰部分，新车座舱采用“中轴对称布局”，配备一块贯穿式全景巨幕屏，辅以真木材质点缀。材质上，车内采用金属按键、60 切面钻切宝石，全车多处采用软质包覆，座椅的材质则是半苯胺全粒面真皮。座舱布局上，" data-title="比亚迪超豪华行政旗舰轿车登场！仰望鼎曜行政版车长 5.6 米、续航破千公里" data-date="11-07 23:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 23:19</span>
          <span class="news-item-title">比亚迪超豪华行政旗舰轿车登场！仰望鼎曜行政版车长 5.6 米、续航破千公里</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日现场消息，今晚，在阿布扎比，比亚迪旗下超豪华行政旗舰轿车 —— 仰望鼎曜迎来全球首秀</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-08 01:47（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
