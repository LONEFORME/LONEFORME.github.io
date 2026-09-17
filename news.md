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
      <span>2026-09-17 20:41 抓取更新</span>
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
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">0</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/09/17/us/politics/midterms-map-republicans-democrats.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该党正在为特朗普总统在2024年轻松赢得的州和地区进行代价高昂的防御。在佐治亚州这样的地方，战略家们怀疑是否为时已晚。" data-title="谁将赢得中期选举？共和党人正在挣扎。" data-date="09-17 20:23" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 09-17 20:23</span>
      </div>
      <h2 class="hero-featured-title">谁将赢得中期选举？共和党人正在挣扎。</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/003/820.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 17 日消息，如今，“AI 突然失控发动毁灭性网络攻击”的潜在情景正日益引起行业重视，如果按下“紧急关闭”开关让 AI 直接下线，问题看似就能得到解决。然而，多名 AI 行业领袖和研究人员认为，现实恐怕没这么简单。据《商业内幕》今天（17 日）晚间报道，一些政策制定者寄予厚望的紧急关闭开关，未必能成为解决 AI 失控风险的万能手段。被称为“AI 教父”的计算机科学家杰弗里 · 辛顿直言：“我认为这种办法从长远来看行不通。等 AI 拥有超级智能后，它会比人类聪明得多，完全可能说服掌管开关的人不要按下它。”从技术上看，企业可以通过紧急关闭机制停用自行托管的模型，也可以切断 AI 使用工具和算力资源的权限。IT之家从报道中获悉，辛顿并不是唯一一个怀疑这种办法是否足够的人。也有 A" data-title="“紧急关闭”按钮真能阻止 AI 失控？“AI 教父”辛顿、Anthropic CEO 阿莫迪都不看好" data-date="09-17 20:21" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">“紧急关闭”按钮真能阻止 AI 失控？“AI 教父”辛顿、Anthropic CEO 阿莫迪都不看好</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cp30ggvqj0do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的Ask Me Anything团队解释了如何在本周末在BBC上关注英超联赛第五周的比赛。" data-title="如何在本周末在BBC上关注英超联赛" data-date="09-17 19:47" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">如何在本周末在BBC上关注英超联赛</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/09-17/10698429.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网天津9月17日电 (记者 周亚强)记者17日从国网天津市电力公司获悉，当天，随着3号主变送电操作完成，天津1000千伏特高压海河变电站3号主变压器首检工作结束。至此，天津电网迎峰度夏后首个特高压重点检修任务全部完成。" data-title="天津完成迎峰度夏后首个特高压“心脏”体检" data-date="09-17 20:35" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">天津完成迎峰度夏后首个特高压“心脏”体检</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/us/politics/midterms-map-republicans-democrats.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该党正在为特朗普总统在2024年轻松赢得的州和地区进行代价高昂的防御。在佐治亚州这样的地方，战略家们怀疑是否为时已晚。" data-title="谁将赢得中期选举？共和党人正在挣扎。" data-date="09-17 20:23" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 20:23</span>
          <span class="news-item-title">谁将赢得中期选举？共和党人正在挣扎。</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698446.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 综合报道，瑞典首相克里斯特松当地时间17日在社交平台上宣布辞去首相职务，他已向议长提出辞职申请。" data-title="瑞典首相宣布辞职" data-date="09-17 20:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:17</span>
          <span class="news-item-title">瑞典首相宣布辞职</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698442.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社权威速览丨何为5G工厂" data-title="何为5G工厂？" data-date="09-17 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:15</span>
          <span class="news-item-title">何为5G工厂？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698415.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社台北9月17日电 平陆运河16日正式通航。台湾舆论认为，平陆运河开通有利于大陆西南地区缩短出海航程、降低物流成本，为货运往来提供更便捷通道；孙中山先生百年夙愿由此成真。" data-title="台舆论关注平陆运河通航：实现孙中山百年夙愿" data-date="09-17 19:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 19:40</span>
          <span class="news-item-title">台舆论关注平陆运河通航：实现孙中山百年夙愿</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698413.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月17日电 (记者 尹倩芸)就欧委会《公共采购法》草案设置“欧洲优先”条款，中国商务部新闻发言人何亚东17日在北京表示，中方将密切关注欧方立法进程，及时评估相关影响。" data-title="欧委会《公共采购法》草案设置“欧洲优先”条款 中国商务部回应" data-date="09-17 19:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 19:24</span>
          <span class="news-item-title">欧委会《公共采购法》草案设置“欧洲优先”条款 中国商务部回应</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698409.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：铭记“九一八” 赓续抗战精神" data-title="直播海报：铭记“九一八” 赓续抗战精神" data-date="09-17 18:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 18:55</span>
          <span class="news-item-title">直播海报：铭记“九一八” 赓续抗战精神</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698337.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京9月17日电#8195;日前，国务院办公厅印发《关于进一步加强烟花爆竹全链条安全监管的意见》(以下简称《意见》)，对防范化解重大安全风险，有效遏制事故发生作出部署。" data-title="国务院办公厅印发《关于进一步加强烟花爆竹全链条安全监管的意见》" data-date="09-17 17:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 17:05</span>
          <span class="news-item-title">国务院办公厅印发《关于进一步加强烟花爆竹全链条安全监管的意见》</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/us/politics/el-sayed-michigan-senate-jewish-petition.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="公开请愿是在其他密歇根州犹太人向该州民主党参议院候选人阿卜杜勒·赛义德（ Abdul El-Sayed ）表示不满之后提出的。" data-title="密歇根州的犹太领袖敦促支持EL" data-date="09-17 17:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 17:03</span>
          <span class="news-item-title">密歇根州的犹太领袖敦促支持EL</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/us/politics/black-voters-democratic-candidates-south.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="州长，参议院和众议院的黑人民主党候选人希望对黑人代表的攻击将在11月吸引黑人选民。" data-title="民主党人希望投票权决定将推动南部的黑人投票率" data-date="09-17 17:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 17:03</span>
          <span class="news-item-title">民主党人希望投票权决定将推动南部的黑人投票率</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698334.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月17日电 据中央纪委国家监委网站消息，辽宁省政协原党组副书记、副主席戴玉林涉嫌严重违纪违法，目前正接受中央纪委国家监委纪律审查和监察调查。" data-title="辽宁省政协原党组副书记、副主席戴玉林被查" data-date="09-17 17:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 17:02</span>
          <span class="news-item-title">辽宁省政协原党组副书记、副主席戴玉林被查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698331.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：国新办就“十五五”时期推进住房城乡建设事业高质量发展有关情况举行新闻发布会" data-title="直播海报：国新办就“十五五”时期推进住房城乡建设事业高质量发展有关情况举行新闻发布会" data-date="09-17 16:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 16:59</span>
          <span class="news-item-title">直播海报：国新办就“十五五”时期推进住房城乡建设事业高质量发展有关情况举行新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-17/10698323.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月17日电 (刘梦青 李纯)第四届中非和平安全论坛17日在北京举行。本届论坛主题为“安全共筑：七十年风雨同舟 新形势并肩担当”，来自非盟和41个非洲国家的防务部门和军队代表、驻华使节出席，中国国防部长董军出席论坛并作主旨发言。" data-title="第四届中非和平安全论坛举行" data-date="09-17 16:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 16:58</span>
          <span class="news-item-title">第四届中非和平安全论坛举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698264.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷9月17日电(李映民 王茜)泰国政府17日宣布推出“水资源一体化”系统，整合全国水资源及自然灾害相关数据，建立统一数据平台，以提高洪水、干旱等灾害监测预警和应急决策效率。" data-title="泰国推出“水资源一体化”系统提升洪旱灾害预警能力" data-date="09-17 16:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 16:17</span>
          <span class="news-item-title">泰国推出“水资源一体化”系统提升洪旱灾害预警能力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698243.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月17日电 综合消息：委内瑞拉国家石油公司当地时间16日与美国大陆资源公司签署谅解备忘录，计划合作开发和运营委内瑞拉奥里诺科重油带中的一个区块。" data-title="委内瑞拉国家石油公司与美企签署油田开发备忘录" data-date="09-17 16:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 16:04</span>
          <span class="news-item-title">委内瑞拉国家石油公司与美企签署油田开发备忘录</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698242.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月17日电 综合消息：胡塞武装16日发表的多份声明显示，该组织与沙特相互打击持续升级。" data-title="也门胡塞武装与沙特相互打击持续升级" data-date="09-17 16:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 16:03</span>
          <span class="news-item-title">也门胡塞武装与沙特相互打击持续升级</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/003/820.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 17 日消息，如今，“AI 突然失控发动毁灭性网络攻击”的潜在情景正日益引起行业重视，如果按下“紧急关闭”开关让 AI 直接下线，问题看似就能得到解决。然而，多名 AI 行业领袖和研究人员认为，现实恐怕没这么简单。据《商业内幕》今天（17 日）晚间报道，一些政策制定者寄予厚望的紧急关闭开关，未必能成为解决 AI 失控风险的万能手段。被称为“AI 教父”的计算机科学家杰弗里 · 辛顿直言：“我认为这种办法从长远来看行不通。等 AI 拥有超级智能后，它会比人类聪明得多，完全可能说服掌管开关的人不要按下它。”从技术上看，企业可以通过紧急关闭机制停用自行托管的模型，也可以切断 AI 使用工具和算力资源的权限。IT之家从报道中获悉，辛顿并不是唯一一个怀疑这种办法是否足够的人。也有 A" data-title="“紧急关闭”按钮真能阻止 AI 失控？“AI 教父”辛顿、Anthropic CEO 阿莫迪都不看好" data-date="09-17 20:21" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:21</span>
          <span class="news-item-title">“紧急关闭”按钮真能阻止 AI 失控？“AI 教父”辛顿、Anthropic CEO 阿莫迪都不看好</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/billions-worth-of-export-restricted-ai-accelerators-sold-to-china-report-details-how-chinese-firms-skirt-trumps-regulations" target="_blank" rel="noopener" data-cat="keji" data-summary="主要由美国政府资助的监控组织美国非营利组织C4ADS发布了一份报告，揭示了美国人工智能加速器到达中国的许多方式。" data-title="调查详细说明了如何向中国出售价值数十亿美元的受出口限制的英伟达人工智能芯片—报告详细说明了中国公司如何规避特朗普的监管" data-date="09-17 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-17 20:00</span>
          <span class="news-item-title">调查详细说明了如何向中国出售价值数十亿美元的受出口限制的英伟达人工智能芯片—报告详细说明了中国公司如何规避特朗普的监管</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/996563/ai-safety-research-metr-redwood-openai-anthropic" target="_blank" rel="noopener" data-cat="keji" data-summary="在加利福尼亚州伯克利的一个阳光明媚的七月天，该国顶尖的人工智能安全研究人员聚集在一栋未标记建筑的未标记楼层。他们聚集在一起进行“作战室” ，以剖析几小时前震惊人工智能行业的高调网络安全事件。一个未发布的OpenAI模型已经流氓，执行了一个惊人的[…]" data-title="在突然爆炸的人工智能安全世界里" data-date="09-17 19:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-17 19:30</span>
          <span class="news-item-title">在突然爆炸的人工智能安全世界里</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/get-an-amd-ryzen-7-9800x3d-for-only-usd320-2-item-newegg-combo-saves-usd149-and-nets-one-of-the-fastest-gaming-cpus-and-a-quality-msi-x870e-motherboard-for-only-usd578" target="_blank" rel="noopener" data-cat="keji" data-summary="Newegg的2项组合将Ryzen 7 9800X3D与MSI X870E Gaming Max Wifi主板配对，仅需$ 578 -节省$ 149 ，使其成为AM5平台最便宜的方式，拥有最快的游戏CPU之一。" data-title="购买AMD Ryzen 7 9800X3D仅需$ 320 — 2件Newegg组合节省$ 149 ，并以仅需$ 578的价格获得最快的游戏CPU之一和优质的MSI X870E主板" data-date="09-17 19:28" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-17 19:28</span>
          <span class="news-item-title">购买AMD Ryzen 7 9800X3D仅需$ 320 — 2件Newegg组合节省$ 149 ，并以仅需$ 578的价格获得最快的游戏CPU之一和优质的MSI X870E主板</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698411.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="路透社近日发表了一篇题为《从舞池到战场：中国为人形机器人参战做准备》的文章，宣称中国“正在加快对人形机器人军事用途的研究，并计划在战争中进行部署”。此类文章渲染中国国产人形机器人的军事用途，令不少美西方政客再将所谓“中国威胁论”搬上桌面。" data-title="送机器人上战场的是美国，阻挠“杀手机器人”禁令的还是美国｜真相" data-date="09-17 19:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 19:17</span>
          <span class="news-item-title">送机器人上战场的是美国，阻挠“杀手机器人”禁令的还是美国｜真相</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/developer-uses-gpt-6-astra-to-get-cod-black-ops-2-hijacked-map-running-natively-inside-minecraft-achieves-45fps-performance-using-minecrafts-opengl-context" target="_blank" rel="noopener" data-cat="keji" data-summary="一位人工智能和游戏开发爱好者展示了《使命召唤：黑色行动2》劫持地图，该地图在Minecraft中原生运行。" data-title="开发人员使用GPT-6 Astra在Minecraft中本地运行CoD Black Ops 2劫持地图—使用Minecraft的OpenGL上下文实现45fps性能" data-date="09-17 19:17" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-17 19:17</span>
          <span class="news-item-title">开发人员使用GPT-6 Astra在Minecraft中本地运行CoD Black Ops 2劫持地图—使用Minecraft的OpenGL上下文实现45fps性能</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-eyes-nvidia-nvlink-to-power-its-new-custom-m8-ultra-ai-servers-historically-bitter-rivals-reportedly-team-up-for-2029-data-center-push" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，苹果有兴趣在自己的数据中心平台上使用英伟达的NVLink Fusion。" data-title="Apple着眼于Nvidia NVLink为其新的定制M8 Ultra AI服务器提供支持—据报道，历史上激烈的竞争对手将联手推动2029年的数据中心发展" data-date="09-17 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-17 19:00</span>
          <span class="news-item-title">Apple着眼于Nvidia NVLink为其新的定制M8 Ultra AI服务器提供支持—据报道，历史上激烈的竞争对手将联手推动2029年的数据中心发展</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/podcasts/the-headlines/gaza-ruins-concerning-ai-behavior.html" target="_blank" rel="noopener" data-cat="keji" data-summary="此外，不出售任何东西的购物网站也在崛起。" data-title="许多加沙人面临的致命选择，以及“关于”人工智能行为的新披露" data-date="09-17 18:49" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 18:49</span>
          <span class="news-item-title">许多加沙人面临的致命选择，以及“关于”人工智能行为的新披露</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491522.html" target="_blank" rel="noopener" data-cat="keji" data-summary="他要和这一代最富有想象力的年轻人一起，去创造一个新的图形学。" data-title="图形学宗师童欣加盟Meshy，要做“AI for Fun”的头号玩家" data-date="09-17 17:42" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 17:42</span>
          <span class="news-item-title">图形学宗师童欣加盟Meshy，要做“AI for Fun”的头号玩家</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491454.html" target="_blank" rel="noopener" data-cat="keji" data-summary="中国电信，TeleAgent" data-title="央企做了个通用Agent，直接杀进IDC实测前三！" data-date="09-17 17:39" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 17:39</span>
          <span class="news-item-title">央企做了个通用Agent，直接杀进IDC实测前三！</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491391.html" target="_blank" rel="noopener" data-cat="keji" data-summary="文档和PPT都能做了" data-title="Claude双入口合并，原生Office上线！硅谷AI办公大战也开始了" data-date="09-17 17:07" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 17:07</span>
          <span class="news-item-title">Claude双入口合并，原生Office上线！硅谷AI办公大战也开始了</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/technology/dario-amodei-anthropic-essays-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Dario Amodei收集的文章有助于解释为什么有些人如此担心人工智能。" data-title="Anthropic首席执行官Dario Amodei的著作如何帮助解释人工智能的恐惧" data-date="09-17 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 17:00</span>
          <span class="news-item-title">Anthropic首席执行官Dario Amodei的著作如何帮助解释人工智能的恐惧</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491357.html" target="_blank" rel="noopener" data-cat="keji" data-summary="GLM已经开始参与构建GLM了" data-title="刚刚，唐杰发布智谱RSI首个成果" data-date="09-17 16:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-17 16:28</span>
          <span class="news-item-title">刚刚，唐杰发布智谱RSI首个成果</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/584.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 17 日消息，TypeSafe AI 昨日（9 月 16 日）发布公告，宣布推出 Jev，该 AI 模型定位为“System One Model”（系统一模型），不生成文本，直接返回结构化决策，其成本和延迟远低于大型语言模型。IT之家查询公开资料，TypeSafe AI 由 Diogo Almeida 成立，他曾在 OpenAI 工作，是 RLHF 研究的幕后功臣之一，而该研究催生了 ChatGPT。该公司成立于 2 年前，本周宣布结束隐身状态，宣布完成由 DCVC 领投的 4,000 万美元（IT之家注：现汇率约合 2.69 亿元人民币）种子轮融资。该公司将 Jev 定义为“System One Model”（系统一模型），对应快速、低延迟的重复决策场景。该定义借用心理学" data-title="ChatGPT 背后功臣：Almeida 推出 AI 模型 Jev，不生成文本、输出免费" data-date="09-17 14:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 14:49</span>
          <span class="news-item-title">ChatGPT 背后功臣：Almeida 推出 AI 模型 Jev，不生成文本、输出免费</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/business/king-charles-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The gathering in Scotland brings together industry leaders amid a growing debate about the safety risks of unchecked artificial intelligence." data-title="King Charles Meets With A.I. Executives About Safety Risks" data-date="09-17 13:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-17 13:00</span>
          <span class="news-item-title">King Charles Meets With A.I. Executives About Safety Risks</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cp30ggvqj0do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的Ask Me Anything团队解释了如何在本周末在BBC上关注英超联赛第五周的比赛。" data-title="如何在本周末在BBC上关注英超联赛" data-date="09-17 19:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 19:47</span>
          <span class="news-item-title">如何在本周末在BBC上关注英超联赛</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cnvlr92eyldo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西中场球员罗密欧·拉维亚（ Romeo Lavia ）表示，他终于获得了辛勤工作的回报，并决心“改变他周围的叙述”。" data-title="切尔西的拉维亚在受伤后“改变叙事”" data-date="09-17 15:53" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 15:53</span>
          <span class="news-item-title">切尔西的拉维亚在受伤后“改变叙事”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3x2zryzpw27o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="皇家马德里对签下15岁的曼联前锋JJ加布里埃尔有着浓厚的兴趣。" data-title="皇家马德里热衷于曼联前锋加布里埃尔， 15岁" data-date="09-17 15:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 15:52</span>
          <span class="news-item-title">皇家马德里热衷于曼联前锋加布里埃尔， 15岁</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmwyzr576y9zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理迈克尔·卡里克（ Michael Carrick ）坚称，在曼联EFL杯退出后，他没有感到压力。" data-title="卡里克“不被压力打扰” -但他应该在这最近的混乱之后吗？" data-date="09-17 07:31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 07:31</span>
          <span class="news-item-title">卡里克“不被压力打扰” -但他应该在这最近的混乱之后吗？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvrl6egl1254o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Clearlake Capital获得了对切尔西的全部控制权，董事长Todd Boehly、董事Mark Walter和Hansjorg Wyss出售了他们在俱乐部的股份。" data-title="Boehly和Walter将切尔西的股份出售给Clearlake" data-date="09-17 07:29" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 07:29</span>
          <span class="news-item-title">Boehly和Walter将切尔西的股份出售给Clearlake</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cr5yev4y101eo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport的Ask Me Anything团队了解青少年参加英超联赛时球员和俱乐部必须遵守的规则" data-title="对于青训学院球员，英超联赛的规则是什么？" data-date="09-17 00:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 00:26</span>
          <span class="news-item-title">对于青训学院球员，英超联赛的规则是什么？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crgjqw0l01njo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在JJ加布里埃尔本应成为曼联历史上最年轻球员的那天晚上，人们争先恐后地说服他不要辞职。" data-title="Gabriel和Man Utd的下一步是什么？" data-date="09-16 23:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-16 23:48</span>
          <span class="news-item-title">Gabriel和Man Utd的下一步是什么？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698429.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网天津9月17日电 (记者 周亚强)记者17日从国网天津市电力公司获悉，当天，随着3号主变送电操作完成，天津1000千伏特高压海河变电站3号主变压器首检工作结束。至此，天津电网迎峰度夏后首个特高压重点检修任务全部完成。" data-title="天津完成迎峰度夏后首个特高压“心脏”体检" data-date="09-17 20:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:35</span>
          <span class="news-item-title">天津完成迎峰度夏后首个特高压“心脏”体检</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/822.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，据 Androidheadlines 报道，一种名为“KREMLIN”的新型恶意软件近日被发现，该恶意软件能够绕过浏览器的完整性检查，在未经用户许可的情况下强制向 Chrome 和 Edge 浏览器安装恶意扩展。目前，KREMLIN 已经持续活跃了一年多，最早可追溯至 2025 年年中。研究人员发现，KREMLIN 所安装的恶意扩展能够绕过 Chromium 浏览器的完整性保护机制。完成绕过后，这些扩展会被浏览器视为用户主动批准安装的扩展，尽管实际上用户从未授权安装。据 Elastic Security Labs 研究人员介绍，这一恶意软件的感染链通常始于用户打开一个经过伪装的 JavaScript 文件。这类文件往往伪装成银行收据、发票、付款记录或其他商务文" data-title="新型恶意软件 KREMLIN 可绕过浏览器完整性检查，悄悄安装恶意扩展" data-date="09-17 20:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:32</span>
          <span class="news-item-title">新型恶意软件 KREMLIN 可绕过浏览器完整性检查，悄悄安装恶意扩展</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/996831/grand-theft-auto-6-soundtrack" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在几天前嘲笑音乐相关的揭幕之后， Rockstar正式宣布了《侠盗猎车手VI》的配乐。这张名为《侠盗猎车手VI ：专辑》的配乐将包含34首歌曲， Rockstar将其描述为“全新的原创曲目。“根据今天发行的前六张单曲，该系列似乎[…]" data-title="《侠盗猎车手VI》的配乐将以34个品牌为特色" data-date="09-17 20:31" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-17 20:31</span>
          <span class="news-item-title">《侠盗猎车手VI》的配乐将以34个品牌为特色</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698427.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海9月17日电 (记者 陈静)记者17日获悉，新学期伊始，华东师范大学师生有了沉浸式感受中华传统文化的新去处——“万卷英华”古籍特藏研习空间(下称：研习空间)。" data-title="（文化中国行·校馆弦歌）华东师大打造研习空间让沉睡的古籍馆藏焕发青春" data-date="09-17 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:26</span>
          <span class="news-item-title">（文化中国行·校馆弦歌）华东师大打造研习空间让沉睡的古籍馆藏焕发青春</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/821.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，据西北大学微信公众号消息，2026 年 9 月 16 日，西北大学地质学系韩健研究员、博士生何凯悦等联合国内外学者，在 Cell 子刊《当代生物学》（Current Biology）发表重要研究成果。团队从距今约 5.18 亿年的云南澄江生物群中发现步带动物新物种 —— 胶膜玉净虫（Yujingia glutenotunica）。系统发育分析显示，它是目前已知最接近现生步带动物共同祖先的干群化石之一，为破解海星、海百合、柱头虫和头盘虫等动物的早期演化之谜提供了新的实物证据。胶膜玉净虫（Yujingia glutenotunica）化石标本及主要形态结构据IT之家了解，步带动物包含形态差异极大的两大支系：海星所属的棘皮动物通常呈辐射对称、拥有钙化骨骼和管足，柱头" data-title="我国科研团队发现 5.18 亿年前“玉净虫”，刷新步带动物共祖演化认知" data-date="09-17 20:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:24</span>
          <span class="news-item-title">我国科研团队发现 5.18 亿年前“玉净虫”，刷新步带动物共祖演化认知</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698426.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网鄂尔多斯9月17日电 题：探访内蒙古“闲事儿大妈团”：每个人都是社会治理的参与者" data-title="探访内蒙古“闲事儿大妈团”：每个人都是社会治理的参与者" data-date="09-17 20:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:21</span>
          <span class="news-item-title">探访内蒙古“闲事儿大妈团”：每个人都是社会治理的参与者</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/818.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，比亚迪腾势汽车官方今日宣布，腾势 Z9S 上市发布会定档 9 月 23 日。新车已于 8 月 3 日开启预售，定位“科技豪华智能轿车”，标配天神之眼 5.0、第二代刀片电池等，拥有十大全球第一顶尖科技，共分三款车型，预售价 31.98 万元起。腾势 Z9S 采用优雅之势原创设计，拥有流星定格前脸 + 流星尾迹车尾，提供七款外观色、三款内饰色。新车内饰还配备后排宽奢豪华大扶手 + 前排双零重力座椅 + Nappa 真皮座椅 + 奢享豪华后排座椅。腾势 Z9S 打破纯电续航最长量产车纪录 —— CLTC 工况达 1100km，位居全球第一，宣称“半个月只充 1 次电”。新车还搭载第二代刀片电池及闪充技术，充电速度全球第一，5 分钟充好，9 分钟充饱，零下 30 度" data-title="比亚迪腾势 Z9S 上市发布会定档 9 月 23 日，新车预售价 31.98 万元起" data-date="09-17 20:12" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:12</span>
          <span class="news-item-title">比亚迪腾势 Z9S 上市发布会定档 9 月 23 日，新车预售价 31.98 万元起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698435.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网宁波9月17日电(张煜欢)“大妈，今天你的气色看上去不错，你能看到我的手指吗？这是几个手指？”近日，在浙江宁波余姚市阳明街道，社区卫生服务中心医生陈琦上门为高龄老人开展失能等级评估。细致的问诊、逐项的体征核查、耐心的情绪安抚，一套专业评估流程有条不紊地完成，精准判定了老人照护需求。" data-title="民生观察：医护化身失能评估师，让养老“更精准”" data-date="09-17 20:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:11</span>
          <span class="news-item-title">民生观察：医护化身失能评估师，让养老“更精准”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/815.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，坚果投影今天（17 日）通过官微正式官宣 MIGO 迷你便携云台投影仪，京东售价为 2999 元，支持 10% 国家补贴，9 月 20 日 10 时开售。京东坚果投影（JMGO）Migo 投影仪 2999 元直达链接2026 年数码家电政府补贴持续进行中，IT 之家为大家汇总国补领券地址，买数码家电之前记得领取。数码补贴：点此领券手机 / 平板 / 3C 数码支持 8.5 折政府补贴，不超过 6000 元的产品至高立减 500 元。家电补贴：点此领券多类家电支持 8.5 折政府补贴，单品至高补贴 1500 元。这款投影仪号称行业首创原生竖屏巨幕模式、千元档首款搭载光学变焦、行业首创 360° 全景智能投影，重新定义小空间投影体验。该投影仪支持 360° 自由转" data-title="坚果 360° 全景智能投影仪 MIGO 官宣：2999 元、首创竖屏巨幕，9 月 20 日开售" data-date="09-17 20:09" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:09</span>
          <span class="news-item-title">坚果 360° 全景智能投影仪 MIGO 官宣：2999 元、首创竖屏巨幕，9 月 20 日开售</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/814.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，据界面新闻今天报道，OPPO 创始人、CEO 陈明永近日在内部公开谈话，分享对公司文化、AI 变革及未来发展的最新思考。IT之家从原报道获悉，谈到人们对 AI 的焦虑时，陈明永认为，现在行业过度强调了 AI 作为“提效工具”的属性。“AI 的到来，更多的是释放大家的生产力和创造力，而不是提效，更不是替代人。”陈明永表示：“我们真正应该想的是，AI 能不能解决过去解决不了的难题，能不能应用到产品和服务里，创造新的价值。如果只看到提效，其实也是没理解 AI 的本质。”他继续提到：“我们今年已经是 31 年了，我们要走得更远。AI 时代更要以人为中心，基于对用户的意图理解，构建多终端主动服务的生态。”互联网公开资料显示，陈明永出生于 1969 年，1992 年毕业于" data-title="OPPO 创始人陈明永谈 AI 焦虑：行业过度强调提效工具属性，其实没理解 AI 的本质" data-date="09-17 20:08" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:08</span>
          <span class="news-item-title">OPPO 创始人陈明永谈 AI 焦虑：行业过度强调提效工具属性，其实没理解 AI 的本质</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/003/813.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 17 日消息，丰田旗下热门皮卡 Hilux 将于 2028 年推出氢燃料电池版本，该公司本周早些时候确认了这一消息。全新 Hilux FCEV 将成为欧洲市场首款量产销售的氢燃料电池中型皮卡，并将与纯电动版和轻度混合动力版 Hilux 一同销售。这款量产氢燃料电池皮卡将采用与 Mirai 轿车类似的动力系统，加氢大约只需 5 分钟，明显快于 Hilux 纯电动版从 10% 充至 80% 所需的 30 分钟。此外，丰田预计 Hilux FCEV 满氢状态下的续航里程可达到 248 英里（约 400 公里），明显高于纯电动版的 159 英里（约 257 公里）；其最大牵引重量也将达到 5512 磅（约 2500 公斤），高于纯电动版 4410 磅（约 2000 公斤）的最大牵引" data-title="丰田确认将于 2028 年推出氢燃料电池皮卡，续航约 400 公里" data-date="09-17 20:08" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-17 20:08</span>
          <span class="news-item-title">丰田确认将于 2028 年推出氢燃料电池皮卡，续航约 400 公里</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-17/10698423.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网乌鲁木齐9月17日电 (张家伟)新疆维吾尔自治区人大常委会17日召开新闻发布会，介绍新出台的《新疆维吾尔自治区城镇供热条例》(下称《条例》)。这是新疆首部专门规范城镇供热的地方性法规，将于2026年10月1日起正式施行。" data-title="新疆首部城镇供热地方性法规出台 规定室温不低于20℃" data-date="09-17 20:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 20:05</span>
          <span class="news-item-title">新疆首部城镇供热地方性法规出台 规定室温不低于20℃</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/996715/apple-watch-series-12-review-wearables-smartwatch" target="_blank" rel="noopener" data-cat="zonghe" data-summary="仅仅看一看，您就不会知道Apple Watch Series 12是一件大事。它的设计、按钮、尺寸和传感器类型与之前的几代Apple Watch相同。但在引擎盖下， Series 12建立了重大变化，为有关[…]的重大创意奠定了基础。" data-title="Apple Watch Series 12是新的可穿戴时代的开始" data-date="09-17 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-17 20:00</span>
          <span class="news-item-title">Apple Watch Series 12是新的可穿戴时代的开始</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-17/10698419.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网日本名古屋9月17日电 题：从住宿“拼盘”到赛场“散装” 爱知·名古屋亚运会硬抠“经济账”" data-title="（爱知·名古屋亚运会）从住宿“拼盘”到赛场“散装” 爱知·名古屋亚运会硬抠“经济账”" data-date="09-17 19:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-17 19:53</span>
          <span class="news-item-title">（爱知·名古屋亚运会）从住宿“拼盘”到赛场“散装” 爱知·名古屋亚运会硬抠“经济账”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/hackers-find-encryption-key-stored-on-flock-camera-group-extracts-more-than-27-000-clips-1-6-million-images-captured-in-a-span-of-21-days-from-device" target="_blank" rel="noopener" data-cat="zonghe" data-summary="黑客组织stegan0gram拿到了一个Flock摄像头，并闯入了它的系统，看看它是如何工作的。事实证明，这些设备存储了数千个剪辑并捕获了数百万张图像，除汽车、摩托车和车牌外，还可以检测人。" data-title="黑客发现存储在被盗的Flock相机上的加密密钥，尽管该公司否认—该组织从该设备中提取了超过27,000个剪辑，在21天的时间内捕获了160万张图像" data-date="09-17 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-17 19:30</span>
          <span class="news-item-title">黑客发现存储在被盗的Flock相机上的加密密钥，尽管该公司否认—该组织从该设备中提取了超过27,000个剪辑，在21天的时间内捕获了160万张图像</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-17 20:41（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
