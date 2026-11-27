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
      <span>2026-11-28 01:35 抓取更新</span>
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
        <span class="channel-count">55</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">14</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">14</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">55</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · BBC×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.bbc.com/zhongwen/articles/cwlymzm5mnxyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介。" data-title="台湾“九合一”选举：六都市长候选人简介" data-date="11-28 00:04" data-source="BBC">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
        <span class="hero-featured-date">🕒 11-28 00:04</span>
      </div>
      <h2 class="hero-featured-title">台湾“九合一”选举：六都市长候选人简介</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/desktops/gaming-pcs/ibuypowers-black-friday-offers-net-you-usd650-off-powerful-rtx-5080-prebuilt-pc-stackable-offer-code-can-net-you-a-bargain-bundle-with-a-free-monitor-and-peripherals" target="_blank" rel="noopener" data-cat="keji" data-summary="Prebuilt PC extraordinaires iBuyPower is having a huge Black Friday sale across a whole range of products, including a powerful bundle on an all-AMD Ryzen 9 7800X3D / RX 9070 XT build, which will also net you free bundled extras, including a set of Asus peripherals and a 144Hz FHD MSI gaming monitor, and a total of $650 off an RTX 5080 gaming PC" data-title="iBuyPower’s Black Friday offers net you $650 off powerful RTX 5080 prebuilt PC" data-date="11-28 01:30" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">iBuyPower’s Black Friday offers net you $650 off powerful RTX 5080 prebuilt PC</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/12040/13208899/wsl-news-transfers-rumours-gossip-and-womens-football-latest" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="VOTE: Were Arsenal right to sack Slegers?" data-title="VOTE: Were Arsenal right to sack Slegers?" data-date="11-28 00:35" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">VOTE: Were Arsenal right to sack Slegers?</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1039645/black-friday-best-cheap-tech-deals-under-30-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="What can you get for $30 these days? When it comes to tech, you might be surprised. Even as gadgets get more expensive, $30 can still go a long way, especially on Black Friday. For just $8, for instance, TP-Link’s Tapo smart plug will let you control the Christmas tree lights from your phone. You […]" data-title="Here are the best Black Friday deals you can grab for $30 or less" data-date="11-28 01:30" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Here are the best Black Friday deals you can grab for $30 or less</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwlymzm5mnxyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介。" data-title="台湾“九合一”选举：六都市长候选人简介" data-date="11-28 00:04" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-28 00:04</span>
          <span class="news-item-title">台湾“九合一”选举：六都市长候选人简介</span>
          <span class="news-value-point">💡 这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/27/us/politics/trump-congressional-investigations-contractors.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="The incoming Democratic majorities have begun targeting businesses and other outsiders in their planned inquiries, but the president has threatened to fire them if they comply without his permission." data-title="In Democrats vs. Trump, the Loser May Be Federal Contractors" data-date="11-27 23:47" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-27 23:47</span>
          <span class="news-item-title">In Democrats vs. Trump, the Loser May Be Federal Contractors</span>
          <span class="news-value-point">💡 The incoming Democratic majorities have begun targeting businesses and o…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10739090.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国共产党江苏省第十五届委员会第一次全体会议11月27日选举信长星为省委书记，刘小涛、范波为省委副书记，当选为省委常委的还有周红波、张文兵、胡立杰(女)、边学文、李耀光、陈忠伟、马士光、沈剑荣、敬健、吴庆文。" data-title="信长星当选中共江苏省委书记" data-date="11-27 22:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 22:48</span>
          <span class="news-item-title">信长星当选中共江苏省委书记</span>
          <span class="news-value-point">💡 中国共产党江苏省第十五届委员会第一次全体会议11月27日选举信长星为省委书记，刘小涛、范波为省委副书记，当选为省委常委的还有周红波、张文兵、胡立…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10739085.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月27日电 (记者 马帅莎)据中国航天科技集团消息，北京时间11月27日21时05分，中国在太原卫星发射中心使用长征六号改运载火箭，将遥感五十号04星发射升空，卫星顺利进入预定轨道，发射任务取得圆满成功。" data-title="中国成功发射遥感五十号04星" data-date="11-27 22:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 22:33</span>
          <span class="news-item-title">中国成功发射遥感五十号04星</span>
          <span class="news-value-point">💡 中新社北京11月27日电 (记者 马帅莎)据中国航天科技集团消息，北京时间11月27日21时05分，中国在太原卫星发射中心使用长征六号改运载火箭…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/27/us/politics/2028-presidential-race-questions.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Will JD Vance and Marco Rubio run? What about Kamala Harris and Alexandria Ocasio-Cortez? And, of course, what role will President Trump play?" data-title="Five Big Questions for the 2028 Presidential Race" data-date="11-27 22:33" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-27 22:33</span>
          <span class="news-item-title">Five Big Questions for the 2028 Presidential Race</span>
          <span class="news-value-point">💡 Will JD Vance and Marco Rubio run? What about Kamala Harris and Alexandr…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10739073.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网吉隆坡11月27日电 中国驻马来西亚使馆27日举办“读懂中国之治——中国共产党二十届五中全会精神专题座谈会”。中国驻马来西亚大使姚文出席并作主旨发言，马国会议员、民主行动党顾问陈国伟，巫统最高理事洛克曼，人民公正党副总秘书艾迪，马中友好协会会长马吉德，亚太“一带一路”共策会会长翁诗杰等政党、智库学者及友好团体代表参加。" data-title="中国驻马来西亚使馆举办“读懂中国之治——中国共产党二十届五中全会精神专题座谈会”" data-date="11-27 21:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 21:56</span>
          <span class="news-item-title">中国驻马来西亚使馆举办“读懂中国之治——中国共产党二十届五中全会精神专题座谈会”</span>
          <span class="news-value-point">💡 中新网吉隆坡11月27日电 中国驻马来西亚使馆27日举办“读懂中国之治——中国共产党二十届五中全会精神专题座谈会”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738991.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉11月27日电 (记者 周璟)菲律宾副总统莎拉·杜特尔特27日表示，即使面临弹劾审判，她也绝不会主动辞去副总统职务。" data-title="菲律宾副总统莎拉称绝不会因弹劾审判辞职" data-date="11-27 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 20:26</span>
          <span class="news-item-title">菲律宾副总统莎拉称绝不会因弹劾审判辞职</span>
          <span class="news-value-point">💡 中新社马尼拉11月27日电 (记者 周璟)菲律宾副总统莎拉·杜特尔特27日表示，即使面临弹劾审判，她也绝不会主动辞去副总统职务</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738967.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月27日电 渥太华消息：当地时间26日，呼吁加拿大政府驱逐美国驻加大使皮特·胡克斯特拉的请愿书被提交至加拿大国会众议院。该请愿书由近30万加拿大民众实名联署。" data-title="加拿大近30万民众联名请愿要求驱逐美国大使" data-date="11-27 20:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 20:24</span>
          <span class="news-item-title">加拿大近30万民众联名请愿要求驱逐美国大使</span>
          <span class="news-value-point">💡 中新社北京11月27日电 渥太华消息：当地时间26日，呼吁加拿大政府驱逐美国驻加大使皮特·胡克斯特拉的请愿书被提交至加拿大国会众议院</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738996.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月27日电 据日本广播协会(NHK)27日报道，日本冲绳县警方以涉嫌非法侵入住宅为由，逮捕了一名驻日美军人员。" data-title="日媒：涉嫌非法侵入住宅，一名驻日美军人员被捕" data-date="11-27 20:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 20:13</span>
          <span class="news-item-title">日媒：涉嫌非法侵入住宅，一名驻日美军人员被捕</span>
          <span class="news-value-point">💡 中新网11月27日电 据日本广播协会(NHK)27日报道，日本冲绳县警方以涉嫌非法侵入住宅为由，逮捕了一名驻日美军人员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738962.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据伊朗方面27日消息，伊朗海军司令沙赫拉姆·伊拉尼当天说，伊朗海军突击队夺回两艘此前被美军劫持的油轮。" data-title="伊朗海军司令称夺回两艘被美军劫持的油轮" data-date="11-27 19:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 19:18</span>
          <span class="news-item-title">伊朗海军司令称夺回两艘被美军劫持的油轮</span>
          <span class="news-value-point">💡 据伊朗方面27日消息，伊朗海军司令沙赫拉姆·伊拉尼当天说，伊朗海军突击队夺回两艘此前被美军劫持的油轮</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738947.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月27日电 据朝中社报道，朝鲜劳动党总书记、国务委员长金正恩11月26日观看了在东平壤大剧院进行的俄罗斯艺术家纪念演出。" data-title="俄艺术家赴朝访问演出 金正恩到场观看并祝贺演出成功" data-date="11-27 18:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 18:54</span>
          <span class="news-item-title">俄艺术家赴朝访问演出 金正恩到场观看并祝贺演出成功</span>
          <span class="news-value-point">💡 中新网11月27日电 据朝中社报道，朝鲜劳动党总书记、国务委员长金正恩11月26日观看了在东平壤大剧院进行的俄罗斯艺术家纪念演出</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738910.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷11月27日电 (王茜 梁峻祥 李映民)泰国正大管理学院27日与泰国中华文化促进会签约，该校授权泰国中华文化促进会在中国开展招生工作。根据合作安排，该协会可联动中国各地相关协会，在不同地区为正大管理学院开展招生。" data-title="泰国文促会携手高校开展教育领域合作" data-date="11-27 18:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 18:34</span>
          <span class="news-item-title">泰国文促会携手高校开展教育领域合作</span>
          <span class="news-value-point">💡 中新网曼谷11月27日电 (王茜 梁峻祥 李映民)泰国正大管理学院27日与泰国中华文化促进会签约，该校授权泰国中华文化促进会在中国开展招生工作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738860.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社悉尼11月27日电 (记者 薄雯雯)2026第七届悉尼茶博会27日在澳大利亚悉尼开幕。展会现场，绿茶、红茶、乌龙茶等多种中国传统茶叶受到当地民众欢迎。" data-title="第七届悉尼茶博会开幕 中国茶受青睐" data-date="11-27 17:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 17:29</span>
          <span class="news-item-title">第七届悉尼茶博会开幕 中国茶受青睐</span>
          <span class="news-value-point">💡 中新社悉尼11月27日电 (记者 薄雯雯)2026第七届悉尼茶博会27日在澳大利亚悉尼开幕</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx053e8yr348o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="台湾选举传统中，素有“决战中台湾”一称。江启臣若当选，卢路线将得到选民加持，其在国民党内的声望也有望进一步升高。" data-title="台中市选战：江启臣对决何欣纯，卢秀燕问鼎总统前哨战" data-date="11-27 13:47" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 13:47</span>
          <span class="news-item-title">台中市选战：江启臣对决何欣纯，卢秀燕问鼎总统前哨战</span>
          <span class="news-value-point">💡 台湾选举传统中，素有“决战中台湾”一称</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/ibuypowers-black-friday-offers-net-you-usd650-off-powerful-rtx-5080-prebuilt-pc-stackable-offer-code-can-net-you-a-bargain-bundle-with-a-free-monitor-and-peripherals" target="_blank" rel="noopener" data-cat="keji" data-summary="Prebuilt PC extraordinaires iBuyPower is having a huge Black Friday sale across a whole range of products, including a powerful bundle on an all-AMD Ryzen 9 7800X3D / RX 9070 XT build, which will also net you free bundled extras, including a set of Asus peripherals and a 144Hz FHD MSI gaming monitor, and a total of $650 off an RTX 5080 gaming PC" data-title="iBuyPower’s Black Friday offers net you $650 off powerful RTX 5080 prebuilt PC" data-date="11-28 01:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 01:30</span>
          <span class="news-item-title">iBuyPower’s Black Friday offers net you $650 off powerful RTX 5080 prebuilt PC</span>
          <span class="news-value-point">💡 Prebuilt PC extraordinaires iBuyPower is having a huge Black Friday sale…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/manufacturing/chinas-ai-hardware-push-is-moving-beyond-gpus-to-the-pcbs-underneath-them-beijing-races-to-corner-the-market-on-copper-foil-and-micro-drill-bits-as-board-complexity-explodes" target="_blank" rel="noopener" data-cat="keji" data-summary="AI hardware bottlenecks are expanding beyond GPUs to the PCBs underneath them. As AI servers like Rubin Ultra push PCB layers toward 78 layers using denser laminates, drill bits are wearing out 10 times faster than normal, while high-speed signalling stretches the demand for smooth copper foil." data-title="China’s AI hardware push is moving beyond GPUs to the PCBs underneath them — Beijing races to corner the market on copper foil and micro-drill bits as board complexity explodes" data-date="11-28 01:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 01:00</span>
          <span class="news-item-title">China’s AI hardware push is moving beyond GPUs to the PCBs underneath them — Beijing races to corner the market on copper foil and micro-drill bits as board complexity explodes</span>
          <span class="news-value-point">💡 AI hardware bottlenecks are expanding beyond GPUs to the PCBs underneath…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/this-usd619-powercolor-radeon-rx-9070-gre-is-the-cheapest-around-this-black-friday-grab-a-great-1080p-or-1440p-gaming-upgrade-for-a-great-price" target="_blank" rel="noopener" data-cat="keji" data-summary="PowerColor&#39;s Radeon RX 9070 GRE is just $619 at Amazon this Black Friday — a rare midrange gaming GPU deal in today&#39;s tough market." data-title="This $619 PowerColor Radeon RX 9070 GRE is the cheapest around this Black Friday" data-date="11-28 00:41" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 00:41</span>
          <span class="news-item-title">This $619 PowerColor Radeon RX 9070 GRE is the cheapest around this Black Friday</span>
          <span class="news-value-point">💡 PowerColor's Radeon RX 9070 GRE is just $619 at Amazon this Black Friday…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10739084.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社福州11月27日电 (叶秋云)于27日在福州市举行的第七届海峡两岸(福州)职工创新创业创造大赛主题日活动上，面向两岸职工的职工创新项目辅导及创新成果转化AI大模型正式上线。" data-title="两岸职工福州同场竞技 项目辅导及成果转化AI大模型上线" data-date="11-27 22:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 22:32</span>
          <span class="news-item-title">两岸职工福州同场竞技 项目辅导及成果转化AI大模型上线</span>
          <span class="news-value-point">💡 中新社福州11月27日电 (叶秋云)于27日在福州市举行的第七届海峡两岸(福州)职工创新创业创造大赛主题日活动上，面向两岸职工的职工创新项目辅导…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513352.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一支团队在真机上验证的成果，可以成为下一支团队继续开发的起点。" data-title="人形机器人开发者集合！众擎开放大小脑，10亿产业级生态支持计划也来了" data-date="11-27 22:07" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 22:07</span>
          <span class="news-item-title">人形机器人开发者集合！众擎开放大小脑，10亿产业级生态支持计划也来了</span>
          <span class="news-value-point">💡 一支团队在真机上验证的成果，可以成为下一支团队继续开发的起点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-27/10739083.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社北京11月27日电 (记者 陈杭)2026太空数据中心建设工作推进大会27日在北京举办。会上宣布，太空数据中心在轨技术试验平台上线运行，将面向全国商业航天和人工智能领域，提供模型训练推理、载荷在轨验证等试验机会，为更多创新主体开展太空算力应用提供公共基础设施。" data-title="从在轨测试到开放服务 北京太空算力“朋友圈”扩容" data-date="11-27 21:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 21:57</span>
          <span class="news-item-title">从在轨测试到开放服务 北京太空算力“朋友圈”扩容</span>
          <span class="news-value-point">💡 中新社北京11月27日电 (记者 陈杭)2026太空数据中心建设工作推进大会27日在北京举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-27/10738926.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网11月27日电 据美国福克斯新闻网27日报道，美国总统特朗普表示，黄仁勋重返英伟达对美国和世界来说都是一件“好事”。" data-title="特朗普：黄仁勋重返英伟达是件“好事”，他本人也很高兴回归" data-date="11-27 18:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-27 18:43</span>
          <span class="news-item-title">特朗普：黄仁勋重返英伟达是件“好事”，他本人也很高兴回归</span>
          <span class="news-value-point">💡 中新网11月27日电 据美国福克斯新闻网27日报道，美国总统特朗普表示，黄仁勋重返英伟达对美国和世界来说都是一件“好事”</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq62p0n4er0wo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋戏剧性地重返英伟达执行长职位，引发亚洲股市剧烈波动，也暴露出区内经济体高度依赖AI产业及英伟达所带来的风险。" data-title="押注英伟达发展AI，亚洲在黄仁勋复职后前景如何？" data-date="11-27 15:40" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 15:40</span>
          <span class="news-item-title">押注英伟达发展AI，亚洲在黄仁勋复职后前景如何？</span>
          <span class="news-value-point">💡 黄仁勋戏剧性地重返英伟达执行长职位，引发亚洲股市剧烈波动，也暴露出区内经济体高度依赖AI产业及英伟达所带来的风险</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513305.html" target="_blank" rel="noopener" data-cat="keji" data-summary="网页App双端亮出聊天账单" data-title="DeepSeek APP突然更新账单，网友：要收费了？" data-date="11-27 15:29" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 15:29</span>
          <span class="news-item-title">DeepSeek APP突然更新账单，网友：要收费了？</span>
          <span class="news-value-point">💡 网页App双端亮出聊天账单</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513227.html" target="_blank" rel="noopener" data-cat="keji" data-summary="地图能随时修，记忆能跨任务用" data-title="刚刚，首个带跨任务空间记忆的原生基模开源！机器人端侧就能跑" data-date="11-27 15:01" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 15:01</span>
          <span class="news-item-title">刚刚，首个带跨任务空间记忆的原生基模开源！机器人端侧就能跑</span>
          <span class="news-value-point">💡 地图能随时修，记忆能跨任务用</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513194.html" target="_blank" rel="noopener" data-cat="keji" data-summary="企业需要有用的 AI" data-title="钛动科技 × 腾讯云达成战略合作，用AI打开企业全球增长新空间" data-date="11-27 12:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 12:05</span>
          <span class="news-item-title">钛动科技 × 腾讯云达成战略合作，用AI打开企业全球增长新空间</span>
          <span class="news-value-point">💡 企业需要有用的 AI</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513211.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11 月 27 日，蚂蚁灵波科技发布流式三维重建模型 LingBot-Map 2.0" data-title="蚂蚁灵波发布LingBot-Map 2.0，模型自己修正“空间记忆”，把地图画更准" data-date="11-27 12:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 12:05</span>
          <span class="news-item-title">蚂蚁灵波发布LingBot-Map 2.0，模型自己修正“空间记忆”，把地图画更准</span>
          <span class="news-value-point">💡 11 月 27 日，蚂蚁灵波科技发布流式三维重建模型 LingBot-Map 2.0</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513163.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Quickwit查询总耗时降31%，最高降87%" data-title="20个AI Agents组队，4天狂跑350次实验，超越ClickBench最佳公开成绩" data-date="11-27 11:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-27 11:53</span>
          <span class="news-item-title">20个AI Agents组队，4天狂跑350次实验，超越ClickBench最佳公开成绩</span>
          <span class="news-value-point">💡 Quickwit查询总耗时降31%，最高降87%</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia has told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand and Indonesia as the U.S. tightens its push to keep AI chips out of China." data-title="Nvidia hits pause on chip shipments to Southeast Asia" data-date="11-27 04:03" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-27 04:03</span>
          <span class="news-item-title">Nvidia hits pause on chip shipments to Southeast Asia</span>
          <span class="news-value-point">💡 Nvidia has told manufacturing partners to pause server shipments to Mala…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13208899/wsl-news-transfers-rumours-gossip-and-womens-football-latest" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="VOTE: Were Arsenal right to sack Slegers?" data-title="VOTE: Were Arsenal right to sack Slegers?" data-date="11-28 00:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-28 00:35</span>
          <span class="news-item-title">VOTE: Were Arsenal right to sack Slegers?</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw4gnm4p3zxlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Tottenham winger Savio will miss the club&#39;s Christmas fixtures with injury and could be out for up to 80 days, manager Roberto de Zerbi confirms." data-title="Spurs&#39; Savio to miss festive fixtures after injury setback" data-date="11-28 00:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-28 00:05</span>
          <span class="news-item-title">Spurs' Savio to miss festive fixtures after injury setback</span>
          <span class="news-value-point">💡 Tottenham winger Savio will miss the club's Christmas fixtures with inju…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6d91j5geepqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester United activate an option on captain Bruno Fernandes&#39; contract, extending it until 2028." data-title="Man Utd trigger Fernandes&#39; one-year contract extension" data-date="11-27 23:08" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 23:08</span>
          <span class="news-item-title">Man Utd trigger Fernandes' one-year contract extension</span>
          <span class="news-value-point">💡 Manchester United activate an option on captain Bruno Fernandes' contrac…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13617231/arsenal-vs-man-city-enzo-maresca-says-two-teams-cannot-be-compared-due-to-being-in-different-stages-of-project" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Enzo Maresca said Premier League title rivals Manchester City and Arsenal couldn’t be compared after his side&#39;s early-season form raised expectations." data-title="Maresca: You can&#39;t compare Man City and Arsenal" data-date="11-27 22:47" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 22:47</span>
          <span class="news-item-title">Maresca: You can't compare Man City and Arsenal</span>
          <span class="news-value-point">💡 Enzo Maresca said Premier League title rivals Manchester City and Arsena…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cknv47dee54zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester City&#39;s leaky defence faces one of the most difficult games of the season with a trip to watertight Arsenal, aiming to put right their patchy recent form." data-title="&#39;I am not a magician&#39; - what can Maresca&#39;s Man City learn from watertight Arsenal?" data-date="11-27 22:37" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 22:37</span>
          <span class="news-item-title">'I am not a magician' - what can Maresca's Man City learn from watertight Arsenal?</span>
          <span class="news-value-point">💡 Manchester City's leaky defence faces one of the most difficult games of…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13617215/bruno-fernandes-man-utd-activate-captains-12-month-option-to-extend-contract-which-now-ends-in-2028" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester United have triggered their 12-month option to extend captain Bruno Fernandes&#39; contract." data-title="Man Utd activate Fernandes contract extension clause" data-date="11-27 22:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 22:10</span>
          <span class="news-item-title">Man Utd activate Fernandes contract extension clause</span>
          <span class="news-value-point">💡 Manchester United have triggered their 12-month option to extend captain…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025499/man-city-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City latest: &#39;It&#39;s completely normal&#39; - Maresca not panicking over form" data-title="Man City latest: &#39;It&#39;s completely normal&#39; - Maresca not panicking over form" data-date="11-27 21:11" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 21:11</span>
          <span class="news-item-title">Man City latest: 'It's completely normal' - Maresca not panicking over form</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Pochettino hits back at criticism" data-title="Man Utd latest: Pochettino hits back at criticism" data-date="11-27 20:03" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 20:03</span>
          <span class="news-item-title">Man Utd latest: Pochettino hits back at criticism</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/news/articles/c6wy43d3ry12o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="The Newcastle United defender was given a six-month ban at Newcastle Magistrates&#39; Court." data-title="Botman banned from driving for using phone at wheel" data-date="11-27 18:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 18:34</span>
          <span class="news-item-title">Botman banned from driving for using phone at wheel</span>
          <span class="news-value-point">💡 The Newcastle United defender was given a six-month ban at Newcastle Mag…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616882/man-utd-being-relegated-would-be-the-biggest-shock-in-history-but-it-wont-happen-says-paul-merson" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="In his latest Sky Sports column, Paul Merson previews a big weekend for Manchester United, before Arsenal take on Manchester City in a huge game live this Sunday." data-title="&#39;Man Utd being relegated would be biggest shock in history... but it won&#39;t happen&#39;" data-date="11-27 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 17:00</span>
          <span class="news-item-title">'Man Utd being relegated would be biggest shock in history... but it won't happen'</span>
          <span class="news-value-point">💡 In his latest Sky Sports column, Paul Merson previews a big weekend for …</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwp809d7yp4go?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester City&#39;s owners must be forced to sell the club as punishment for breaking financial rules, senior figures at some Premier League clubs tell BBC Sport." data-title="Man City owners should be forced to sell, say clubs" data-date="11-27 14:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 14:38</span>
          <span class="news-item-title">Man City owners should be forced to sell, say clubs</span>
          <span class="news-value-point">💡 Manchester City's owners must be forced to sell the club as punishment f…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx62pnz1evv4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="England international Dominic Calvert-Lewin signs a new contract to stay with Leeds United until 2029." data-title="Calvert-Lewin signs new Leeds deal until 2029" data-date="11-27 02:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 02:00</span>
          <span class="news-item-title">Calvert-Lewin signs new Leeds deal until 2029</span>
          <span class="news-value-point">💡 England international Dominic Calvert-Lewin signs a new contract to stay…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1039645/black-friday-best-cheap-tech-deals-under-30-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="What can you get for $30 these days? When it comes to tech, you might be surprised. Even as gadgets get more expensive, $30 can still go a long way, especially on Black Friday. For just $8, for instance, TP-Link’s Tapo smart plug will let you control the Christmas tree lights from your phone. You […]" data-title="Here are the best Black Friday deals you can grab for $30 or less" data-date="11-28 01:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-28 01:30</span>
          <span class="news-item-title">Here are the best Black Friday deals you can grab for $30 or less</span>
          <span class="news-value-point">💡 What can you get for $30 these days? When it comes to tech, you might be…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/the-hyperx-omen-max-16-gaming-laptop-with-a-rtx-5090-and-a-core-i9-ultra-can-be-yours-for-an-amazing-usd1-200-off-highest-end-gear-for-26-percent-off-less-than-a-comparable-desktop-pc" target="_blank" rel="noopener" data-cat="zonghe" data-summary="The HyperX Omen Max 16 laptop with a RTX 5090 and a Core i9 Ultra can be yours for just $3,799 — highest-end gear for less price than a comparable desktop" data-title="The HyperX Omen Max 16 laptop with a RTX 5090 and a Core i9 Ultra can be yours for amazing $1,200 off" data-date="11-28 01:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 01:20</span>
          <span class="news-item-title">The HyperX Omen Max 16 laptop with a RTX 5090 and a Core i9 Ultra can be yours for amazing $1,200 off</span>
          <span class="news-value-point">💡 The HyperX Omen Max 16 laptop with a RTX 5090 and a Core i9 Ultra can be…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1039190/best-black-friday-2026-deals-tech-gadgets-gift-ideas" target="_blank" rel="noopener" data-cat="zonghe" data-summary="This year’s Black Friday deals have launched in waves over the past several weeks, but now the floodgates have officially opened. You can now take advantage of the lowest prices we’ve seen in-store and online for video games, wireless earbuds, TVs, e-readers, robot vacuums, and so much more. We can’t guarantee a deal you’ve had […]" data-title="The absolute best Black Friday deals we’ve found (so far)" data-date="11-28 01:07" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-28 01:07</span>
          <span class="news-item-title">The absolute best Black Friday deals we’ve found (so far)</span>
          <span class="news-value-point">💡 This year’s Black Friday deals have launched in waves over the past seve…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/monitors/gaming-monitors/best-gaming-monitor-deals-oled" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Save big with one of these great Black Friday monitor deals. We’re hard at work updating this list with the best deals across all your favorite big tech retailers." data-title="Best Black Friday gaming monitor deals 2026" data-date="11-28 00:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 00:59</span>
          <span class="news-item-title">Best Black Friday gaming monitor deals 2026</span>
          <span class="news-value-point">💡 Save big with one of these great Black Friday monitor deals. We’re hard …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-mice/these-are-the-best-black-friday-gaming-mouse-deals-weve-found-so-far-even-the-newer-generations-are-on-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="We&#39;ve rounded up the best Black Friday deals on gaming mice for every type of gamer — whether you&#39;re looking for ultra-lightweight, tons of buttons, or even modular mice, we&#39;ve got you covered." data-title="These are the best Black Friday gaming mouse deals we&#39;ve found so far" data-date="11-28 00:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 00:40</span>
          <span class="news-item-title">These are the best Black Friday gaming mouse deals we've found so far</span>
          <span class="news-value-point">💡 We've rounded up the best Black Friday deals on gaming mice for every ty…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/live-blog/12040/13617151/f1-qatar-gp-live-friday-practice-updates-results-stream-highlights-from-formula-1-race-weekend-at-lusail-international-circuit" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Qatar GP: Antonelli fastest from Russell in second practice LIVE!" data-title="Qatar GP: Antonelli fastest from Russell in second practice LIVE!" data-date="11-28 00:37" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-28 00:37</span>
          <span class="news-item-title">Qatar GP: Antonelli fastest from Russell in second practice LIVE!</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1043935/best-black-friday-apple-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Black Friday is one of the best times of the year to save some cash on a new pair of AirPods or the latest Apple Watch. After all, the holiday savings can help offset the unfortunate price hikes from earlier this year, when Apple raised the cost of some of its most popular gear. Some […]" data-title="The best Black Friday deals on AirPods, MacBooks, and other Apple gear" data-date="11-28 00:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-28 00:30</span>
          <span class="news-item-title">The best Black Friday deals on AirPods, MacBooks, and other Apple gear</span>
          <span class="news-value-point">💡 Black Friday is one of the best times of the year to save some cash on a…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13617264/let-andalucia-costa-del-sol-open-de-espana-day-two-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Highlights from day two of the Andalucia Costa del Sol Open de Espana in Malaga, Spain." data-title="Spain&#39;s Davalos shines on debut as Huang leads the way in Malaga" data-date="11-28 00:27" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-28 00:27</span>
          <span class="news-item-title">Spain's Davalos shines on debut as Huang leads the way in Malaga</span>
          <span class="news-value-point">💡 Highlights from day two of the Andalucia Costa del Sol Open de Espana in…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13617253/saturday-tips-kap-vert-fancied-to-lift-coral-gold-cup-crown-at-newbury" target="_blank" rel="noopener" data-cat="zonghe" data-summary="With a hugely exciting renewal of the Coral Gold Cup on Saturday, Kate Tracey, Declan Rix and Sam Boswell headed to Newbury for a very special episode of Weekend Winners." data-title="Saturday tips: Kap Vert fancied to lift Coral Gold Cup crown at Newbury" data-date="11-28 00:15" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-28 00:15</span>
          <span class="news-item-title">Saturday tips: Kap Vert fancied to lift Coral Gold Cup crown at Newbury</span>
          <span class="news-value-point">💡 With a hugely exciting renewal of the Coral Gold Cup on Saturday, Kate T…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/these-are-the-best-gaming-laptop-deals-weve-found-this-black-friday-to-suit-all-budgets-save-up-to-usd1-200-off-a-range-of-portable-powerhouses" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Looking to grab yourself a gaming laptop this Black Friday? These are the best deals that we&#39;ve found so far, and you can net up to $1200 off MSRP on a range of systems across all reasonable budgets." data-title="These are the best gaming laptop deals we&#39;ve found this Black Friday to suit all budgets" data-date="11-28 00:12" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 00:12</span>
          <span class="news-item-title">These are the best gaming laptop deals we've found this Black Friday to suit all budgets</span>
          <span class="news-value-point">💡 Looking to grab yourself a gaming laptop this Black Friday? These are th…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/27/us/thanksgiving-weather-east-coast-storm.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="The storm brought heavy rain and strong winds from Virginia to New York, disrupting travel during the holiday season. Conditions were expected to gradually improve on Friday." data-title="Thanksgiving Storm Leaves Half a Million Without Power on the East Coast" data-date="11-28 00:04" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-28 00:04</span>
          <span class="news-item-title">Thanksgiving Storm Leaves Half a Million Without Power on the East Coast</span>
          <span class="news-value-point">💡 The storm brought heavy rain and strong winds from Virginia to New York,…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-chairs/grab-a-new-secretlab-gaming-chair-or-desk-to-upgrade-your-setup-in-its-black-friday-sale-with-up-to-usd537-off-individual-discounts-and-big-bundle-deals-mean-you-can-score-huge-savings-on-top-models-including-the-titan-evo-and-magnus-pro" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Grab a new gaming chair or desk in this Secretlab Black Friday sale." data-title="Grab a new Secretlab gaming chair or desk to upgrade your setup in its Black Friday sale with up to $537 off" data-date="11-28 00:02" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-28 00:02</span>
          <span class="news-item-title">Grab a new Secretlab gaming chair or desk to upgrade your setup in its Black Friday sale with up to $537 off</span>
          <span class="news-value-point">💡 Grab a new gaming chair or desk in this Secretlab Black Friday sale.</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/27/us/supreme-court-rulings-cheered-by-republicans-wound-up-hurting-them.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Decisions on voting rights, immigration and corruption generated a backlash that helped spur turnout that drove the Democratic sweep of Congress." data-title="Supreme Court Rulings Cheered by Republicans Wound Up Hurting Them" data-date="11-27 23:47" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-27 23:47</span>
          <span class="news-item-title">Supreme Court Rulings Cheered by Republicans Wound Up Hurting Them</span>
          <span class="news-value-point">💡 Decisions on voting rights, immigration and corruption generated a backl…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1043272/zepath-rechargeable-aa-batteries-black-friday-2026-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="If you’re picking up any gifts that require AA batteries, it’s not a bad idea to buy a set you can keep using long after the holidays. Thankfully, you can currently get a 12-pack of Zepath’s rechargeable 3,000mWh AAs on Amazon with a charger for $23.99 ($8 off) for Black Friday, which is a new […]" data-title="You can grab a 12-pack of Zepath’s rechargeable AA batteries for just $24" data-date="11-27 23:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 23:30</span>
          <span class="news-item-title">You can grab a 12-pack of Zepath’s rechargeable AA batteries for just $24</span>
          <span class="news-value-point">💡 If you’re picking up any gifts that require AA batteries, it’s not a bad…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1039978/airpods-pro-3-apple-earbuds-black-friday-2026-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="The AirPods Pro 3 are cheaper than ever. Despite receiving an early discount last week, Apple’s latest flagship wireless earbuds are still on sale for just $149 at Amazon, Best Buy, and Walmart. They originally sold for $249, but are commonly available for $199 outside major deal events. The best price that we’ve previously seen […]" data-title="Apple’s AirPods Pro 3 are a whopping $100 off for Black Friday" data-date="11-27 23:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 23:15</span>
          <span class="news-item-title">Apple’s AirPods Pro 3 are a whopping $100 off for Black Friday</span>
          <span class="news-value-point">💡 The AirPods Pro 3 are cheaper than ever. Despite receiving an early disc…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-28 01:35（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
