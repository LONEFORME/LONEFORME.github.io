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
      <span>2026-11-26 18:07 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · 天空体育×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-26/10738261.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中央纪委国家监委网站讯 经中共中央批准，中央纪委国家监委对中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法问题进行了立案审查调查。" data-title="中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法被开除党籍" data-date="11-26 18:01" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-26 18:01</span>
      </div>
      <h2 class="hero-featured-title">中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法被开除党籍</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.qbitai.com/2026/11/512942.html" target="_blank" rel="noopener" data-cat="keji" data-summary="12月6日，WAIC将携手第六届“海聚英才”全球创新创业峰会，把这场关于“人”的讨论带回现场。" data-title="报名最后2天｜AI浪潮之中，来认识创造未来的人" data-date="11-26 15:36" data-source="量子位">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🧠 量子位</span>
      </div>
      <p class="hero-sub-title">报名最后2天｜AI浪潮之中，来认识创造未来的人</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13615913/liam-delap-has-a-chance-to-show-chelsea-what-theyre-missing-when-they-travel-to-nottingham-forest" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="When Liam Delap joined Chelsea in the summer of 2025, he probably had ambitions of cementing himself as an elite Premier League No 9. Perhaps even positioning himself to be the heir to Harry Kane&#39;s throne for England." data-title="Delap&#39;s chance at redemption against toothless Chelsea" data-date="11-26 18:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Delap's chance at redemption against toothless Chelsea</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-26/10738247.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月26日电(记者 应妮)第七届“中国好家风”中华优秀传统文化全国入校公益项目启动仪式25日在京举行，这个已运行六年的公益项目全新升级，面向全国中小学征集家校协同育人优秀实践案例，发掘校园家风建设好样板。" data-title="第七届“中国好家风”公益项目面向全国征集家校育人优秀案例" data-date="11-26 17:58" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">第七届“中国好家风”公益项目面向全国征集家校育人优秀案例</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738261.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中央纪委国家监委网站讯 经中共中央批准，中央纪委国家监委对中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法问题进行了立案审查调查。" data-title="中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法被开除党籍" data-date="11-26 18:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 18:01</span>
          <span class="news-item-title">中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法被开除党籍</span>
          <span class="news-value-point">💡 中央纪委国家监委网站讯 经中共中央批准，中央纪委国家监委对中央宣传部原副部长，原国家新闻出版广电总局党组书记、局长蔡赴朝严重违纪违法问题进行了立…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738245.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月26日电 记者从北京外国语大学非洲学院获悉，当地时间11月24日至25日，“2026非洲语言文化研究国际研讨会”在埃塞俄比亚亚的斯亚贝巴大学举行。本次会议以“文明互鉴与新时代中非合作发展”为主题，来自中国、埃塞俄比亚、尼日利亚、肯尼亚、南非、阿联酋、贝宁、英国等国的高校和科研机构的专家学者齐聚一堂，共同探讨新时代中非文明交流互鉴与合作发展的新路径。" data-title="“2026非洲语言文化研究国际研讨会”在埃塞俄比亚举行" data-date="11-26 18:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 18:01</span>
          <span class="news-item-title">“2026非洲语言文化研究国际研讨会”在埃塞俄比亚举行</span>
          <span class="news-value-point">💡 中新网北京11月26日电 记者从北京外国语大学非洲学院获悉，当地时间11月24日至25日，“2026非洲语言文化研究国际研讨会”在埃塞俄比亚亚的…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738209.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月26日电 伊斯兰堡消息：当地时间11月26日，巴基斯坦三军新闻局证实，11月20日至23日，巴安全部队在俾路支省开展四次反恐行动，共击毙12名恐怖分子。" data-title="巴基斯坦在俾路支省开展反恐行动 击毙12名恐怖分子" data-date="11-26 17:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:59</span>
          <span class="news-item-title">巴基斯坦在俾路支省开展反恐行动 击毙12名恐怖分子</span>
          <span class="news-value-point">💡 中新社北京11月26日电 伊斯兰堡消息：当地时间11月26日，巴基斯坦三军新闻局证实，11月20日至23日，巴安全部队在俾路支省开展四次反恐行动…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738244.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月26日电 综合外媒报道，当地时间26日，泰国首都曼谷邦纳区政府称，当地一家炼油厂发生爆炸。" data-title="外媒：泰国曼谷一炼油厂发生爆炸 造成至少7人受伤" data-date="11-26 17:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:49</span>
          <span class="news-item-title">外媒：泰国曼谷一炼油厂发生爆炸 造成至少7人受伤</span>
          <span class="news-value-point">💡 中新网11月26日电 综合外媒报道，当地时间26日，泰国首都曼谷邦纳区政府称，当地一家炼油厂发生爆炸</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738236.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月26日电 (刘梦青 李纯)中国国防部26日在北京举行例行记者会，新闻发言人陈曦指出，有关域外国家应切实尊重中方在南海的主权和权益，停止插手介入南海问题。" data-title="中国国防部：有关域外国家应停止插手介入南海问题" data-date="11-26 17:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:44</span>
          <span class="news-item-title">中国国防部：有关域外国家应停止插手介入南海问题</span>
          <span class="news-value-point">💡 中新社北京11月26日电 (刘梦青 李纯)中国国防部26日在北京举行例行记者会，新闻发言人陈曦指出，有关域外国家应切实尊重中方在南海的主权和权益…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738235.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月26日电 (刘梦青 李纯)“若日方连当年侵略中国时遗留下的化武都不愿清理干净，又怎能彻底清算军国主义遗毒？”在26日的中国国防部例行记者会上，新闻发言人陈曦表示，中方督促日方早日彻底清除日遗化武毒害，还中国人民以净土。" data-title="中国国防部：督促日方早日彻底清除日遗化武毒害" data-date="11-26 17:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:40</span>
          <span class="news-item-title">中国国防部：督促日方早日彻底清除日遗化武毒害</span>
          <span class="news-value-point">💡 中新社北京11月26日电 (刘梦青 李纯)“若日方连当年侵略中国时遗留下的化武都不愿清理干净，又怎能彻底清算军国主义遗毒</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738221.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月26日电(燕新台)近日，中国国民党副主席萧旭岑在一档政论节目中重申，国民党坚定地走两岸和平的路线。" data-title="萧旭岑批赖清德“台独”主张，重申中国国民党坚定走两岸和平路线" data-date="11-26 17:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:27</span>
          <span class="news-item-title">萧旭岑批赖清德“台独”主张，重申中国国民党坚定走两岸和平路线</span>
          <span class="news-value-point">💡 中新网11月26日电(燕新台)近日，中国国民党副主席萧旭岑在一档政论节目中重申，国民党坚定地走两岸和平的路线</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738217.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社昆明11月26日电 (记者 缪超 陈静)中国共产党云南省第十二次代表大会26日在昆明开幕，中共云南省委书记莫高义代表省委作报告时立下“上游责任状”：强化六大水系“源头责任”“上游担当”，持续推进长江十年禁渔，确保“一江清水出云南”。" data-title="云南立下“上游责任状”，确保“一江清水出云南”" data-date="11-26 17:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:24</span>
          <span class="news-item-title">云南立下“上游责任状”，确保“一江清水出云南”</span>
          <span class="news-value-point">💡 中新社昆明11月26日电 (记者 缪超 陈静)中国共产党云南省第十二次代表大会26日在昆明开幕，中共云南省委书记莫高义代表省委作报告时立下“上游…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738212.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月26日电 据《以色列时报》26日报道，以色列总理内塔尼亚胡和国防部长卡茨证实，以军打死了巴勒斯坦伊斯兰抵抗运动(哈马斯)的经济和教育部门负责人哈立德·阿布·纳达。" data-title="内塔尼亚胡：以军打死哈马斯经济和教育部门负责人" data-date="11-26 17:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:10</span>
          <span class="news-item-title">内塔尼亚胡：以军打死哈马斯经济和教育部门负责人</span>
          <span class="news-value-point">💡 中新网11月26日电 据《以色列时报》26日报道，以色列总理内塔尼亚胡和国防部长卡茨证实，以军打死了巴勒斯坦伊斯兰抵抗运动(哈马斯)的经济和教育…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738202.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆11月26日电(陈媛)中国致公党重庆市委员会2026年对外联络工作能力建设会议暨海归青年创新创业交流活动26日在渝举行。来自重庆、四川、广西、江苏四地的中国致公党党员，围绕发挥海外优势搭建平台、做好对外联络工作、深化区域合作等议题展开讨论。" data-title="四地致公党党员齐聚山城 共话侨海资源转化新路径" data-date="11-26 17:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:08</span>
          <span class="news-item-title">四地致公党党员齐聚山城 共话侨海资源转化新路径</span>
          <span class="news-value-point">💡 中新网重庆11月26日电(陈媛)中国致公党重庆市委员会2026年对外联络工作能力建设会议暨海归青年创新创业交流活动26日在渝举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738167.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="全球媒体聚焦｜瑞典智库驳斥所谓“中国挤压”：那是近现代历史上前所未有的“共赢”！" data-title="瑞典智库驳斥所谓“中国挤压”：那是近现代历史上前所未有的“共赢”！" data-date="11-26 16:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 16:21</span>
          <span class="news-item-title">瑞典智库驳斥所谓“中国挤压”：那是近现代历史上前所未有的“共赢”！</span>
          <span class="news-value-point">💡 全球媒体聚焦｜瑞典智库驳斥所谓“中国挤压”：那是近现代历史上前所未有的“共赢”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738140.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月26日电 据路透社报道，美国联邦通信委员会25日表示，已批准埃隆·马斯克旗下太空探索技术公司部署最多由100万颗卫星组成的星座，用于建设太空数据中心。" data-title="美国批准马斯克旗下公司部署百万卫星 建太空数据中心" data-date="11-26 16:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 16:06</span>
          <span class="news-item-title">美国批准马斯克旗下公司部署百万卫星 建太空数据中心</span>
          <span class="news-value-point">💡 中新网11月26日电 据路透社报道，美国联邦通信委员会25日表示，已批准埃隆·马斯克旗下太空探索技术公司部署最多由100万颗卫星组成的星座，用于…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwlymzm5mnxyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介。" data-title="台湾“九合一”选举：六都市长候选人简介" data-date="11-26 12:29" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 12:29</span>
          <span class="news-item-title">台湾“九合一”选举：六都市长候选人简介</span>
          <span class="news-value-point">💡 这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/us/politics/van-hollen-schumer-israel-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="参议员克里斯·范·霍伦表示，他取代参议员查克·舒默担任党魁的举动与以色列无关，但他对犹太国家的尖锐批评立场已成为这场竞选中的主要分歧点。" data-title="Van Hollen’s Challenge to Schumer Highlights Democratic Rift on Israel" data-date="11-26 00:41" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 00:41</span>
          <span class="news-item-title">范·霍伦对舒默的挑战凸显了民主党内部在以色列问题上的分歧</span>
          <span class="news-item-title-en">Van Hollen’s Challenge to Schumer Highlights Democratic Rift on Israel</span>
          <span class="news-value-point">💡 参议员克里斯·范·霍伦表示，他取代参议员查克·舒默担任党魁的举动与以色列无关，但他对犹太国家的尖锐批评立场已成为这场竞选中的主要分歧点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10737857.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月26日电 (记者 孙自法)作为古人类演化、迁徙和扩散的关键地区之一，中国岭南是否生活过丹尼索瓦人？同期还有无其他古人类共存？这些议题一直因缺乏化石记录悬而未决，也备受关注。" data-title="中国岭南首次发现丹尼索瓦人和10.1万年前未知古人类" data-date="11-26 00:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 00:10</span>
          <span class="news-item-title">中国岭南首次发现丹尼索瓦人和10.1万年前未知古人类</span>
          <span class="news-value-point">💡 中新网北京11月26日电 (记者 孙自法)作为古人类演化、迁徙和扩散的关键地区之一，中国岭南是否生活过丹尼索瓦人</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512942.html" target="_blank" rel="noopener" data-cat="keji" data-summary="12月6日，WAIC将携手第六届“海聚英才”全球创新创业峰会，把这场关于“人”的讨论带回现场。" data-title="报名最后2天｜AI浪潮之中，来认识创造未来的人" data-date="11-26 15:36" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 15:36</span>
          <span class="news-item-title">报名最后2天｜AI浪潮之中，来认识创造未来的人</span>
          <span class="news-value-point">💡 12月6日，WAIC将携手第六届“海聚英才”全球创新创业峰会，把这场关于“人”的讨论带回现场</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512916.html" target="_blank" rel="noopener" data-cat="keji" data-summary="30秒一镜到底，可自动编排镜头" data-title="顶尖商用级AI视频每秒只要5毛！中国开源新势力拿下全球第一" data-date="11-26 14:41" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 14:41</span>
          <span class="news-item-title">顶尖商用级AI视频每秒只要5毛！中国开源新势力拿下全球第一</span>
          <span class="news-value-point">💡 30秒一镜到底，可自动编排镜头</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512897.html" target="_blank" rel="noopener" data-cat="keji" data-summary="李斌坦言：不做AI变革可能活不下去" data-title="任少卿带着世界模型3.0来了！蔚来智驾训练提效5倍，座舱也用上强化学习" data-date="11-26 11:23" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 11:23</span>
          <span class="news-item-title">任少卿带着世界模型3.0来了！蔚来智驾训练提效5倍，座舱也用上强化学习</span>
          <span class="news-value-point">💡 李斌坦言：不做AI变革可能活不下去</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512840.html" target="_blank" rel="noopener" data-cat="keji" data-summary="“灵巧手是人类最后的尊严”" data-title="沈向洋刚讲了好多AI非共识啊" data-date="11-26 11:13" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 11:13</span>
          <span class="news-item-title">沈向洋刚讲了好多AI非共识啊</span>
          <span class="news-value-point">💡 “灵巧手是人类最后的尊严”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512828.html" target="_blank" rel="noopener" data-cat="keji" data-summary="叠满海淀最强AI Buff。" data-title="AI影视高地正在北影海淀一带崛起，“一人制片厂”基建搭好了" data-date="11-26 10:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 10:53</span>
          <span class="news-item-title">AI影视高地正在北影海淀一带崛起，“一人制片厂”基建搭好了</span>
          <span class="news-value-point">💡 叠满海淀最强AI Buff</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/us/politics/trump-nvidia-stock-market.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The retreat of the stock market in recent days shows how President Trump’s push to reinstall the company’s chief executive has collided with the realities of his other policies." data-title="Trump Rejoiced in the Market’s Nvidia Surge. It Didn’t Last Long." data-date="11-26 09:53" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 09:53</span>
          <span class="news-item-title">Trump Rejoiced in the Market’s Nvidia Surge. It Didn’t Last Long.</span>
          <span class="news-value-point">💡 The retreat of the stock market in recent days shows how President Trump…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/sp-considers-nvidia-credit-downgrade-over-governance-and-key-man-risks/" target="_blank" rel="noopener" data-cat="keji" data-summary="The credit rating agency may lower Nvidia&#39;s credit rating to AA-, the fourth-highest rating." data-title="S&amp;P considers Nvidia credit downgrade over governance and ‘key man’ risks" data-date="11-26 06:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 06:44</span>
          <span class="news-item-title">S&P considers Nvidia credit downgrade over governance and ‘key man’ risks</span>
          <span class="news-value-point">💡 The credit rating agency may lower Nvidia's credit rating to AA-, the fo…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/business/nvidia-stock-insider-trading-rumor.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Three data providers say they have no evidence to support the online claim that insider trading generated a 9,000 percent return." data-title="A Rumored $300 Million Score on Nvidia’s Stock Surge Isn’t Backed by Trading Records" data-date="11-26 05:36" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:36</span>
          <span class="news-item-title">A Rumored $300 Million Score on Nvidia’s Stock Surge Isn’t Backed by Trading Records</span>
          <span class="news-value-point">💡 Three data providers say they have no evidence to support the online cla…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/business/stocks-sp500-nvidia-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达和其他科技公司股价下跌，原因是投资者权衡了全球贸易的发展和利率走势。" data-title="Stocks Slump Again as Investors Fret About A.I., Tariffs and Inflation" data-date="11-26 05:32" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:32</span>
          <span class="news-item-title">投资者对人工智能、关税和通胀感到担忧，股市再次暴跌</span>
          <span class="news-item-title-en">Stocks Slump Again as Investors Fret About A.I., Tariffs and Inflation</span>
          <span class="news-value-point">💡 英伟达和其他科技公司股价下跌，原因是投资者权衡了全球贸易的发展和利率走势</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/nyregion/mamdani-rent-freeze-legal-challenge-apartments.html" target="_blank" rel="noopener" data-cat="keji" data-summary="曼哈顿的一名法官驳回了房东就租金稳定公寓的租金冻结提起的诉讼，从而使市议员Zohran Mamdani胜诉。" data-title="Mamdani Wins Against Landlords in Rent Freeze Lawsuit" data-date="11-26 05:16" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:16</span>
          <span class="news-item-title">Mamdani在租金冻结诉讼中胜诉房东</span>
          <span class="news-item-title-en">Mamdani Wins Against Landlords in Rent Freeze Lawsuit</span>
          <span class="news-value-point">💡 曼哈顿的一名法官驳回了房东就租金稳定公寓的租金冻结提起的诉讼，从而使市议员Zohran Mamdani胜诉</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI 将在整个 ChatGPT 中引入一个统一的使用量仪表，因为它将聊天和工作体验结合在一起。" data-title="OpenAI says heavy ChatGPT users may hit limits sooner as it merges Chat and Work" data-date="11-26 04:03" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 04:03</span>
          <span class="news-item-title">OpenAI表示，随着ChatGPT将聊天和工作功能合并，重度用户可能更快达到使用上限。</span>
          <span class="news-item-title-en">OpenAI says heavy ChatGPT users may hit limits sooner as it merges Chat and Work</span>
          <span class="news-value-point">💡 OpenAI 将在整个 ChatGPT 中引入一个统一的使用量仪表，因为它将聊天和工作体验结合在一起</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/jensen-huang-broke-nvidias-code-of-conduct-and-his-employees-may-not-forget-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="大多数行为准则都反映了企业文化。就英伟达而言，这可能会产生后果。" data-title="Jensen Huang broke Nvidia’s code of conduct, and his employees may not forget it" data-date="11-26 03:54" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 03:54</span>
          <span class="news-item-title">黄仁勋违反了英伟达的行为准则，他的员工可能不会忘记这一点</span>
          <span class="news-item-title-en">Jensen Huang broke Nvidia’s code of conduct, and his employees may not forget it</span>
          <span class="news-value-point">💡 大多数行为准则都反映了企业文化</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管领先的人工智能公司正日益实现其自身研究和模型开发的自动化，但Anthropic首席执行官Dario Amodei仍对竞争对手的指责予以回击，后者指责他倾向于将人类的自主权拱手让与人工智能。" data-title="Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’" data-date="11-26 03:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 03:44</span>
          <span class="news-item-title">Anthropic的Dario Amodei称，将人类控制权拱手让给人工智能的指控“荒谬”</span>
          <span class="news-item-title-en">Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’</span>
          <span class="news-value-point">💡 尽管领先的人工智能公司正日益实现其自身研究和模型开发的自动化，但Anthropic首席执行官Dario Amodei仍对竞争对手的指责予以回击，…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/" target="_blank" rel="noopener" data-cat="keji" data-summary="纽约已禁止人工智能聊天机器人玩具五年，因为Common Sense Media的新研究揭示了令人担忧的安全缺陷，包括接触不当内容和对情绪发展的风险。" data-title="Want to buy your kid an AI toy this Christmas? Not in New York" data-date="11-26 02:11" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 02:11</span>
          <span class="news-item-title">想在这个圣诞节给孩子买一个人工智能玩具吗？在纽约不行</span>
          <span class="news-item-title-en">Want to buy your kid an AI toy this Christmas? Not in New York</span>
          <span class="news-value-point">💡 纽约已禁止人工智能聊天机器人玩具五年，因为Common Sense Media的新研究揭示了令人担忧的安全缺陷，包括接触不当内容和对情绪发展的风…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/save-usd2600-on-the-cheapest-rtx-5090-prebuilt-pc-weve-found-so-far-in-the-black-friday-rush-corsair-vengeance-i7600-features-ultra-9-285k-cpu-64gb-ram-and-the-ultimate-gaming-gpu" target="_blank" rel="noopener" data-cat="keji" data-summary="这款 Corsair Vengeance 预组装游戏电脑将 RTX 5090 与英特尔最强大的 Arrow Lake 处理器和 64GB 内存相结合，可满足最苛刻的工作或游戏需求。" data-title="Save $2600 on the cheapest RTX 5090 prebuilt PC we&#39;ve found so far in the Black Friday rush" data-date="11-26 01:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 01:45</span>
          <span class="news-item-title">在黑色星期五购物狂潮中，我们迄今为止发现的最便宜的RTX 5090预装电脑可节省2600美元</span>
          <span class="news-item-title-en">Save $2600 on the cheapest RTX 5090 prebuilt PC we've found so far in the Black Friday rush</span>
          <span class="news-value-point">💡 这款 Corsair Vengeance 预组装游戏电脑将 RTX 5090 与英特尔最强大的 Arrow Lake 处理器和 64GB 内存相…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13615913/liam-delap-has-a-chance-to-show-chelsea-what-theyre-missing-when-they-travel-to-nottingham-forest" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="When Liam Delap joined Chelsea in the summer of 2025, he probably had ambitions of cementing himself as an elite Premier League No 9. Perhaps even positioning himself to be the heir to Harry Kane&#39;s throne for England." data-title="Delap&#39;s chance at redemption against toothless Chelsea" data-date="11-26 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 18:00</span>
          <span class="news-item-title">Delap's chance at redemption against toothless Chelsea</span>
          <span class="news-value-point">💡 When Liam Delap joined Chelsea in the summer of 2025, he probably had am…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13612810/aaron-collins-exclusive-mk-dons-striker-discusses-electric-start-to-2026-27-and-first-senior-wales-call-up" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="On Friday November 6, Aaron Collins was notified by the FAW that he was on the standby list for Wales&#39; Nations League matches against Norway and Portugal." data-title="Collins: I got choked up before I came on for my Wales debut!" data-date="11-26 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 18:00</span>
          <span class="news-item-title">Collins: I got choked up before I came on for my Wales debut!</span>
          <span class="news-value-point">💡 On Friday November 6, Aaron Collins was notified by the FAW that he was …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea Q&amp;A! Submit your questions as club backs Alonso" data-title="Chelsea Q&amp;A! Submit your questions as club backs Alonso" data-date="11-26 15:29" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 15:29</span>
          <span class="news-item-title">Chelsea Q&A! Submit your questions as club backs Alonso</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq20x16zxxzeo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="For Premier League referees, the KMI Panel is more important than you might realise. It determines a significant portion of their salary." data-title="Why KMI Panel frustrates referees too - and impacts their salary" data-date="11-26 15:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 15:28</span>
          <span class="news-item-title">Why KMI Panel frustrates referees too - and impacts their salary</span>
          <span class="news-value-point">💡 For Premier League referees, the KMI Panel is more important than you mi…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616618/man-utd-goalkeeper-senne-lammens-criticised-for-howler-in-sporting-draw-by-jamie-carragher" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Jamie Carragher says Manchester United goalkeeper Senne Lammens&#39; confidence is a cause for concern after his howler cost Mauricio Pochettino a first win since taking charge." data-title="Carra: Lammens confidence worrying but Poch will feel Man Utd were robbed" data-date="11-26 07:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 07:10</span>
          <span class="news-item-title">Carra: Lammens confidence worrying but Poch will feel Man Utd were robbed</span>
          <span class="news-value-point">💡 Jamie Carragher says Manchester United goalkeeper Senne Lammens' confide…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616560/liverpool-transfer-news-sidy-barhama-ndiaye-agrees-deal-to-sign-for-reds-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周四报纸的热门报道和转移谣言..." data-title="Papers: Liverpool agree deal to sign Senegal teenager Ndiaye" data-date="11-26 05:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 05:40</span>
          <span class="news-item-title">Papers: Liverpool agree deal to sign Senegal teenager Ndiaye</span>
          <span class="news-value-point">💡 周四报纸的热门报道和转移谣言...</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c65y10z8k59jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰足球独立监管机构主席向议员表示，他“有胆量”对曼城采取潜在的行动。" data-title="Regulator chief &#39;has stomach&#39; to face Man City" data-date="11-26 05:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 05:27</span>
          <span class="news-item-title">监管机构负责人“有胆量”面对曼城</span>
          <span class="news-item-title-en">Regulator chief 'has stomach' to face Man City</span>
          <span class="news-value-point">💡 英格兰足球独立监管机构主席向议员表示，他“有胆量”对曼城采取潜在的行动</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616555/porting-lisbon-vs-manchester-united-clinton-morrison-reacts-to-bizarre-bruno-fernandes-goal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="克林顿·莫里森观看了曼联凭借布鲁诺·费尔南德斯的诡异进球以 2-1 战胜里斯本竞技的比赛。" data-title="Strangest goal ever?! Morrison reacts to BIZARRE Bruno goal!" data-date="11-26 05:14" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 05:14</span>
          <span class="news-item-title">有史以来最奇怪的进球？！莫里森对布鲁诺的离奇进球做出反应！</span>
          <span class="news-item-title-en">Strangest goal ever?! Morrison reacts to BIZARRE Bruno goal!</span>
          <span class="news-value-point">💡 克林顿·莫里森观看了曼联凭借布鲁诺·费尔南德斯的诡异进球以 2-1 战胜里斯本竞技的比赛</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616547/sporing-lisbon-vs-manchester-united-clinton-morrison-reacts-to-double-penalty-drama" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="克林顿·莫里森对曼联在欧冠与里斯本竞技的比赛中被判的两粒点球发表了看法。" data-title="&#39;Where&#39;s he going?!&#39; - Morrison reacts to Man Utd double penalty drama!" data-date="11-26 04:43" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 04:43</span>
          <span class="news-item-title">“他要去哪里？！“- 莫里森对曼联的两粒点球戏剧性事件做出反应！</span>
          <span class="news-item-title-en">'Where's he going?!' - Morrison reacts to Man Utd double penalty drama!</span>
          <span class="news-value-point">💡 克林顿·莫里森对曼联在欧冠与里斯本竞技的比赛中被判的两粒点球发表了看法</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13279286/bournemouth-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Bournemouth latest: Are Cherries the most underrated club in Europe?" data-title="Bournemouth latest: Are Cherries the most underrated club in Europe?" data-date="11-26 03:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 03:45</span>
          <span class="news-item-title">Bournemouth latest: Are Cherries the most underrated club in Europe?</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/burnley-vs-birmingham-city/live/560699" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Birmingham ease to victory at troubled Burnley LIVE!" data-title="Birmingham ease to victory at troubled Burnley LIVE!" data-date="11-26 03:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 03:15</span>
          <span class="news-item-title">伯明翰轻松战胜陷入困境的伯恩利，直播！</span>
          <span class="news-item-title-en">Birmingham ease to victory at troubled Burnley LIVE!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw20xr4d7x55o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语。" data-title="Glasner criticises Forest players yet to learn English" data-date="11-26 02:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 02:32</span>
          <span class="news-item-title">格拉斯纳批评诺丁汉森林球员尚未学会英语</span>
          <span class="news-item-title-en">Glasner criticises Forest players yet to learn English</span>
          <span class="news-value-point">💡 诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/club-brugge-vs-liverpool/live/577679" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Game over? Liverpool three up at Club Brugge LIVE!" data-title="Game over? Liverpool three up at Club Brugge LIVE!" data-date="11-26 01:58" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 01:58</span>
          <span class="news-item-title">比赛结束？利物浦在布鲁日俱乐部以三球领先！</span>
          <span class="news-item-title-en">Game over? Liverpool three up at Club Brugge LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616388/dominik-szoboszlai-free-kick-for-liverpool-vs-man-utd-reveals-grey-area-as-mauricio-pochettino-questions-decision" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联输给利物浦的比赛中，毛里西奥·波切蒂诺对勒尼·约罗被罚红牌感到愤怒，但也认为多米尼克·索博斯洛伊的开场进球不应被判有效——他说的对吗？" data-title="Why wasn&#39;t Szoboszlai&#39;s free-kick ruled out vs Man Utd?" data-date="11-25 23:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 23:15</span>
          <span class="news-item-title">为什么索博斯洛伊对曼联的任意球没有被判无效？</span>
          <span class="news-item-title-en">Why wasn't Szoboszlai's free-kick ruled out vs Man Utd?</span>
          <span class="news-value-point">💡 在曼联输给利物浦的比赛中，毛里西奥·波切蒂诺对勒尼·约罗被罚红牌感到愤怒，但也认为多米尼克·索博斯洛伊的开场进球不应被判有效——他说的对吗</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Merson accuses Gunners of second" data-title="Arsenal latest: Merson accuses Gunners of second" data-date="11-25 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 21:00</span>
          <span class="news-item-title">阿森纳最新消息：默森指责枪手屈居第二</span>
          <span class="news-item-title-en">Arsenal latest: Merson accuses Gunners of second</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738247.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月26日电(记者 应妮)第七届“中国好家风”中华优秀传统文化全国入校公益项目启动仪式25日在京举行，这个已运行六年的公益项目全新升级，面向全国中小学征集家校协同育人优秀实践案例，发掘校园家风建设好样板。" data-title="第七届“中国好家风”公益项目面向全国征集家校育人优秀案例" data-date="11-26 17:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:58</span>
          <span class="news-item-title">第七届“中国好家风”公益项目面向全国征集家校育人优秀案例</span>
          <span class="news-value-point">💡 中新网北京11月26日电(记者 应妮)第七届“中国好家风”中华优秀传统文化全国入校公益项目启动仪式25日在京举行，这个已运行六年的公益项目全新升…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/985.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 26 日消息，美国专利商标局于 11 月 12 日披露了微软一项手机屏幕专利 US 2026/0360990 A1，微软在该专利中提出“将天线阵列直接集成到屏幕玻璃内部”，有望在不增加机身厚度的情况下，为手机容纳下尺寸更大的天线阵列，以改善信号情况。众所周知，智能手机内部空间十分有限，厂商通常需要通过缩小天线尺寸、让不同无线通信功能共用天线，或者直接取消毫米波（mmWave）、超宽带（UWB）等功能来控制内部空间占用。微软此次提出的方案则尝试利用屏幕玻璃本身，为天线提供额外的安装位置。根据专利描述，该方案首先在屏幕玻璃背面加工出一处局部减薄区域，再将天线层安装在玻璃背面，使其至少部分嵌入减薄区域。由于玻璃正面仍保持平整，用户正常使用时不会看到明显凹陷，也不会感受到表面存在" data-title="微软新专利公布：将天线阵列集成到手机屏幕玻璃内部，或为 Surface Phone 铺路" data-date="11-26 17:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-26 17:56</span>
          <span class="news-item-title">微软新专利公布：将天线阵列集成到手机屏幕玻璃内部，或为 Surface Phone 铺路</span>
          <span class="news-value-point">💡 IT之家 11 月 26 日消息，美国专利商标局于 11 月 12 日披露了微软一项手机屏幕专利 US 2026/0360990 A1，微软在该…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/980.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 26 日消息，开发商 Lucid Games 旗下 PS5 平台车辆战斗游戏《毁灭全明星（Destruction AllStars）》于昨日正式关服，官方现已更新游戏界面，确认本作在关服后仍可游玩街机模式单人挑战，不过由于服务器关闭，部分功能可能会受到影响。公开信息显示，本作于 2021 年 2 月发售，至今运营约 5 年半。以车辆碰撞、夸张角色和多人混战为主要内容，车辆破坏具有一定乐趣。不过，其内容量不足以长期维持玩家参与，首发时的单人模式配置和微交易设计也影响了整体体验。随着玩家数量下滑以及更多新作推出，该作逐渐失去关注。" data-title="PS5 游戏《毁灭全明星》今日关服，官方确认玩家仍可游玩街机模式单人挑战" data-date="11-26 17:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-26 17:44</span>
          <span class="news-item-title">PS5 游戏《毁灭全明星》今日关服，官方确认玩家仍可游玩街机模式单人挑战</span>
          <span class="news-value-point">💡 IT之家 11 月 26 日消息，开发商 Lucid Games 旗下 PS5 平台车辆战斗游戏《毁灭全明星（Destruction AllSt…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/979.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 26 日消息，本月早些时候，华为官方宣布，HUAWEI WATCH GT 6 系列手表推出鸿蒙 HarmonyOS 7.0.0.108 SP8 版本升级，开始分批推送给 6.1.0.117 SP6 / 6.1.0.118 SP10 / 7.0.0.107 SP7 / 7.0.0.107 SP10 / 7.0.0.107 SP13 版本上的用户。在官方当时发布的更新日志中，新版本主要带来了手表支持微信来电接听和挂断、增强录音机同步能力，以及支持耳机与手表配对同步功能。IT之家注意到，目前新版本已开启陆续推送，最新的更新日志显示，该款手表还下放了“高血糖风险评估”功能。完整更新日志如下：新增1.配对 HarmonyOS 7.0.0.115 及以上版本的手机，手表支持微信来电接" data-title="版本推送时还有新功能：华为 WATCH GT 6 系列手表获“高血糖风险评估”下放" data-date="11-26 17:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-26 17:42</span>
          <span class="news-item-title">版本推送时还有新功能：华为 WATCH GT 6 系列手表获“高血糖风险评估”下放</span>
          <span class="news-value-point">💡 IT之家 11 月 26 日消息，本月早些时候，华为官方宣布，HUAWEI WATCH GT 6 系列手表推出鸿蒙 HarmonyOS 7.0.…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/978.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 26 日消息，微信鸿蒙版 App 在华为应用市场（App Gallery）发布了 8.0.24.33 (8394785) 版本邀测升级（需收到短信通知后点击链接跳转安装），测试时间为 2026/11/26-2026/12/26。和往常一样，本次更新的说明依旧为“修复了一些已知问题”。据博主 @伤心萨摩耶Ciuciu ，8.0.24 版本的微信新增了如下特性：设置＞朋友权限变更为通讯录权限；我＞收藏＞笔记点击右上角三点新增小图模式、大图模式切换；视频号＞发起直播＞更多＞互动与变现新增奖品；视频号评论区左上角新增问小微入口（逐步开放）；发现＞直播预览界面支持长按直播预览卡片快捷转发给朋友或分享到朋友圈；发现＞听一听＞搜索底部新增“按住问小微”，可按住提问、搜歌或搜音乐人（逐步" data-title="微信鸿蒙版 App 获 8.0.24.33 邀测升级" data-date="11-26 17:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-26 17:41</span>
          <span class="news-item-title">微信鸿蒙版 App 获 8.0.24.33 邀测升级</span>
          <span class="news-value-point">💡 IT之家 11 月 26 日消息，微信鸿蒙版 App 在华为应用市场（App Gallery）发布了 8.0.24.33 (8394785) 版…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cmx29vxzgj25o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="有学者指出，这并非“中国因素”消失，而是地方选举本质以市政民生为主，民进党也吸取去年大罢免的教训，战略性搁置了统独议题，以此拉拢中间选民。" data-title="台湾九合一选举：从“洋流”看民进党战略性搁置“抗中保台”牌" data-date="11-26 17:38" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 17:38</span>
          <span class="news-item-title">台湾九合一选举：从“洋流”看民进党战略性搁置“抗中保台”牌</span>
          <span class="news-value-point">💡 有学者指出，这并非“中国因素”消失，而是地方选举本质以市政民生为主，民进党也吸取去年大罢免的教训，战略性搁置了统独议题，以此拉拢中间选民</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738226.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网云南保山11月26日电 (李开平 侯云鹏)近日，上百只灰鹤飞抵云南省保山市龙陵县境内，在多处区域觅食、休憩、停歇补给。充足的食源与优良的生态环境，让这里成为候鸟理想的补给驿站。" data-title="云南龙陵：灰鹤连续六年赴约" data-date="11-26 17:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:36</span>
          <span class="news-item-title">云南龙陵：灰鹤连续六年赴约</span>
          <span class="news-value-point">💡 中新网云南保山11月26日电 (李开平 侯云鹏)近日，上百只灰鹤飞抵云南省保山市龙陵县境内，在多处区域觅食、休憩、停歇补给</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738211.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州11月26日电 题：从笔墨雅集到时尚视频 跨越太平洋的文化之约" data-title="从笔墨雅集到时尚视频 跨越太平洋的文化之约" data-date="11-26 17:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:21</span>
          <span class="news-item-title">从笔墨雅集到时尚视频 跨越太平洋的文化之约</span>
          <span class="news-value-point">💡 中新网广州11月26日电 题：从笔墨雅集到时尚视频 跨越太平洋的文化之约</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738218.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国天气网讯 最近我国气温反复横跳，有人吐槽：“最近的天气，好像把我们当剩饭了，冷了热，热了冷……”今天(11月26日)起，又有新冷空气上线，北方局地降温可达10℃以上，短暂降温后大回暖又来了，气温如坐过山车，如何穿对衣服成了难题。中国天气网推出全国花式穿衣地图，看看粽子式、洋葱式、橘子式哪种穿衣方法最适合你。" data-title="气温反复横跳！全国花式穿衣地图 看你适合粽子式还是洋葱式穿搭法" data-date="11-26 17:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 17:14</span>
          <span class="news-item-title">气温反复横跳！全国花式穿衣地图 看你适合粽子式还是洋葱式穿搭法</span>
          <span class="news-value-point">💡 中国天气网讯 最近我国气温反复横跳，有人吐槽：“最近的天气，好像把我们当剩饭了，冷了热，热了冷……”今天(11月26日)起，又有新冷空气上线，北…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cmewv0vkgwplo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="目前，近四成女性（38%）与超过四分之一男性（28%）表示从未有过性行为；在1990、2000与2010年的调查中，这一比例约为 五分之一。" data-title="英国性调查：年轻人中五成女性、九成男性观看色情片 三分之一未有性经验" data-date="11-26 17:11" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 17:11</span>
          <span class="news-item-title">英国性调查：年轻人中五成女性、九成男性观看色情片 三分之一未有性经验</span>
          <span class="news-value-point">💡 目前，近四成女性（38%）与超过四分之一男性（28%）表示从未有过性行为</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13610208/oliver-bearman-to-remain-with-haas-for-2027-f1-season-after-new-contract-finally-agreed-ahead-of-qatar-gp" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Haas have confirmed Oliver Bearman will stay at the team for the 2027 Formula 1 season, after protracted contract talks resulted in a one-year extension." data-title="Bearman confirmed to stay at Haas for 2027" data-date="11-26 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 17:00</span>
          <span class="news-item-title">Bearman confirmed to stay at Haas for 2027</span>
          <span class="news-value-point">💡 Haas have confirmed Oliver Bearman will stay at the team for the 2027 Fo…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738178.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="两个小孩发生争执，6岁半女孩拨通110" data-title="民警的一次出警，在孩子心中种下法治的种子" data-date="11-26 16:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 16:46</span>
          <span class="news-item-title">民警的一次出警，在孩子心中种下法治的种子</span>
          <span class="news-value-point">💡 两个小孩发生争执，6岁半女孩拨通110</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738189.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南昌11月26日电 (记者 李韵涵)“鄱湖鸟，知多少？飞时遮尽云和月，落时不见湖边草。”又是一年候鸟迁徙季，中国最大淡水湖鄱阳湖陆续迎来远方来客。" data-title="万鸟归来，鄱阳湖如何守好越冬家园？" data-date="11-26 16:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 16:44</span>
          <span class="news-item-title">万鸟归来，鄱阳湖如何守好越冬家园？</span>
          <span class="news-value-point">💡 中新网南昌11月26日电 (记者 李韵涵)“鄱湖鸟，知多少</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-26/10738185.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆11月26日电 (张旭)11月23日至26日，西南五省(自治区、直辖市)地质灾害防灾减灾救灾经验交流会在重庆召开。" data-title="西南五省区市在重庆交流地灾防治经验" data-date="11-26 16:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 16:39</span>
          <span class="news-item-title">西南五省区市在重庆交流地灾防治经验</span>
          <span class="news-value-point">💡 中新网重庆11月26日电 (张旭)11月23日至26日，西南五省(自治区、直辖市)地质灾害防灾减灾救灾经验交流会在重庆召开</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512952.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，IF 2027 全议程揭晓。" data-title="极客公园创新大会 2027 全议程公布！" data-date="11-26 16:19" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 16:19</span>
          <span class="news-item-title">极客公园创新大会 2027 全议程公布！</span>
          <span class="news-value-point">💡 今天，IF 2027 全议程揭晓</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-26 18:07（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
