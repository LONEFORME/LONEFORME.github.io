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
      <span>2026-11-06 04:08 抓取更新</span>
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
        <span class="channel-count">58</span>
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
        <span class="channel-count">13</span>
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
  <div class="ov-item"><span class="ov-num">58</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×11 · 天空体育×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/05/us/california-death-row-newsom-commutation.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="预计将竞选总统的加文·纽森（ Gavin Newsom ）州长称，死刑在道德上令人反感。尽管加利福尼亚州已有20年没有处决过任何人，但这约占全国死刑判决的四分之一。" data-title="Newsom Commutes the Sentences of California’s 548 Death Row Inmates" data-date="11-06 03:57" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-06 03:57</span>
      </div>
      <h2 class="hero-featured-title">纽瑟姆对加州548名死刑犯减刑</h2>
      <div class="hero-featured-title-en">Newsom Commutes the Sentences of California’s 548 Death Row Inmates</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/05/metas-warns-that-election-backlash-against-data-centers-could-make-ai-expansion-harder/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta警告说，随着社区对大规模基础设施项目的抵制，对数据中心的政治反对可能会威胁到未来的人工智能投资。" data-title="Meta warns that election backlash against data centers could make AI expansion harder" data-date="11-06 03:12" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Meta warns that election backlash against data centers could make AI expansion harder</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ck5ynzry64p2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领电脑游戏《足球经理27》（ Football Manager 27 ） ，以及英国广播公司的读者和人工智能，对本周末的英超赛事进行了预测。" data-title="Sutton&#39;s predictions v Football Manager, the game" data-date="11-06 02:02" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Sutton's predictions v Football Manager, the game</p>
    </a>
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/05/meta-says-us-users-can-now-video-chat-with-their-muse-ai-avatar/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Meta的AI代理现在可以在推出旨在让Muse栩栩如生的类似Tamagotchi的可穿戴设备之前，将呼叫作为可定制的动画头像。" data-title="Meta says US users can now video chat with their Muse AI avatar" data-date="11-06 03:48" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Meta says US users can now video chat with their Muse AI avatar</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/california-death-row-newsom-commutation.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="预计将竞选总统的加文·纽森（ Gavin Newsom ）州长称，死刑在道德上令人反感。尽管加利福尼亚州已有20年没有处决过任何人，但这约占全国死刑判决的四分之一。" data-title="Newsom Commutes the Sentences of California’s 548 Death Row Inmates" data-date="11-06 03:57" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 03:57</span>
          <span class="news-item-title">纽瑟姆对加州548名死刑犯减刑</span>
          <span class="news-item-title-en">Newsom Commutes the Sentences of California’s 548 Death Row Inmates</span>
          <span class="news-value-point">💡 预计将竞选总统的加文·纽森（ Gavin Newsom ）州长称，死刑在道德上令人反感</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/politics/harmeet-dhillon-resigns-doj-civil-rights-unit.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="知情人士称，此举发生在与司法部领导人的冲突之后，包括在中期选举中对法律策略的分歧。" data-title="Harmeet Dhillon, Leader of Justice Department’s Civil Rights Unit, Resigns" data-date="11-06 03:38" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 03:38</span>
          <span class="news-item-title">司法部民权部门负责人Harmeet Dhillon辞职</span>
          <span class="news-item-title-en">Harmeet Dhillon, Leader of Justice Department’s Civil Rights Unit, Resigns</span>
          <span class="news-value-point">💡 知情人士称，此举发生在与司法部领导人的冲突之后，包括在中期选举中对法律策略的分歧</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/politics/supreme-court-trump-abortion-leak-dobbs.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="调查人员利用传票和其他执法权力，正在加快调查，让特朗普政府深入了解法院的内部运作。" data-title="DOJ Steps Up Leak Investigation on Supreme Court Decision Overturning Roe v. Wade" data-date="11-06 03:32" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 03:32</span>
          <span class="news-item-title">美国司法部加强对最高法院推翻Roe诉Wade案的裁决的泄密调查</span>
          <span class="news-item-title-en">DOJ Steps Up Leak Investigation on Supreme Court Decision Overturning Roe v. Wade</span>
          <span class="news-value-point">💡 调查人员利用传票和其他执法权力，正在加快调查，让特朗普政府深入了解法院的内部运作</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/politics/mississippi-senate-race-democrat-colom-hyde-smith.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党人斯科特·科洛姆（ Scott Colom ）在特朗普集会上发布了一则病毒式广告，并吸引了共和党人，然后赢得了与共和党参议员辛迪·海德-史密斯（ Cindy Hyde-Smith ）几乎相同的选票。" data-title="How Colom Changed a Long Shot in Mississippi Into a Race Too Close to Call" data-date="11-06 02:34" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 02:34</span>
          <span class="news-item-title">Colom如何将密西西比州的远射变成一场太接近通话的竞赛</span>
          <span class="news-item-title-en">How Colom Changed a Long Shot in Mississippi Into a Race Too Close to Call</span>
          <span class="news-value-point">💡 民主党人斯科特·科洛姆（ Scott Colom ）在特朗普集会上发布了一则病毒式广告，并吸引了共和党人，然后赢得了与共和党参议员辛迪·海德-史…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/politics/midterms-southern-democrats.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="他们在北卡罗来纳州、南卡罗来纳州和佐治亚州赢得了参议院的比赛，密西西比州的比赛仍然太接近了。他们的胜利也提升了下选票的候选人。" data-title="How Democrats Won Across the South" data-date="11-06 02:18" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 02:18</span>
          <span class="news-item-title">民主党如何在南方获胜</span>
          <span class="news-item-title-en">How Democrats Won Across the South</span>
          <span class="news-value-point">💡 他们在北卡罗来纳州、南卡罗来纳州和佐治亚州赢得了参议院的比赛，密西西比州的比赛仍然太接近了</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/technology/tech-billionaires-democrats-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="许多人向特朗普总统的支持事业捐款，并成为他的盟友。现在，政治结盟可能是一种负担。" data-title="Tech Billionaires Face Tricky Political Waters After Democratic Midterm Sweep" data-date="11-06 01:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 01:02</span>
          <span class="news-item-title">民主党中期选举后，科技亿万富翁面临棘手的政治水域</span>
          <span class="news-item-title-en">Tech Billionaires Face Tricky Political Waters After Democratic Midterm Sweep</span>
          <span class="news-value-point">💡 许多人向特朗普总统的支持事业捐款，并成为他的盟友</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10726975.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月5日电 (马帅莎 崔婉莹)北京时间11月5日23时58分，我国在西昌卫星发射中心使用长征二号丙运载火箭，成功将遥感五十一号07-09星发射升空，卫星顺利进入预定轨道，发射任务取得圆满成功。该卫星主要用于科学试验、电磁环境探测等领域。" data-title="我国成功发射遥感五十一号07" data-date="11-06 00:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 00:38</span>
          <span class="news-item-title">我国成功发射遥感五十一号07</span>
          <span class="news-value-point">💡 中新网北京11月5日电 (马帅莎 崔婉莹)北京时间11月5日23时58分，我国在西昌卫星发射中心使用长征二号丙运载火箭，成功将遥感五十一号07-…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-05/10726954.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网贵阳11月5日电 (记者 周燕玲)贵州省知识产权局近日会同贵州省教育厅等12部门，联合印发《贵州省高价值专利培育工程实施方案(2026—2030年)》(以下简称《方案》)，系统部署高价值专利培育和转化运用全链条工作，夯实知识产权强省建设根基，服务贵州高质量发展。" data-title="贵州12部门联合印发高价值专利培育工程实施方案" data-date="11-05 23:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 23:23</span>
          <span class="news-item-title">贵州12部门联合印发高价值专利培育工程实施方案</span>
          <span class="news-value-point">💡 中新网贵阳11月5日电 (记者 周燕玲)贵州省知识产权局近日会同贵州省教育厅等12部门，联合印发《贵州省高价值专利培育工程实施方案(2026—2…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-05/10726956.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社厦门11月5日电 (记者 阮煜琳 林永传)《〈海洋生物多样性协定〉地位、作用、前景与中国角色》报告中英文版5日在厦门发布。报告指出，中国正以实际行动提升全球南方蓝色实力。" data-title="报告：中国以实际行动提升全球南方蓝色实力" data-date="11-05 23:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 23:22</span>
          <span class="news-item-title">报告：中国以实际行动提升全球南方蓝色实力</span>
          <span class="news-value-point">💡 中新社厦门11月5日电 (记者 阮煜琳 林永传)《〈海洋生物多样性协定〉地位、作用、前景与中国角色》报告中英文版5日在厦门发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-05/10726951.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆11月5日电 (梁钦卿)“外籍人士进政协”暨“中外艺术家看重庆”展览5日在重庆市政协文史馆开幕。意大利、越南、西班牙、白俄罗斯、墨西哥、澳大利亚、匈牙利等多国驻渝蓉领事机构官员、外国商协会负责人、在渝留学生代表等约60人参加活动，近距离感受重庆人文底蕴与传统文化魅力。" data-title="“外籍人士进政协”暨“中外艺术家看重庆”展览在渝开展" data-date="11-05 23:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 23:18</span>
          <span class="news-item-title">“外籍人士进政协”暨“中外艺术家看重庆”展览在渝开展</span>
          <span class="news-value-point">💡 中新网重庆11月5日电 (梁钦卿)“外籍人士进政协”暨“中外艺术家看重庆”展览5日在重庆市政协文史馆开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-05/10726955.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔11月5日电 (记者 金旭)韩国国防部当地时间5日表示，计划向国会提交一份延长清海部队派遣期限的修订同意案，内容包括将部队任务区域扩大至阿曼南部海域，同时增派军事装备和兵力。" data-title="韩国拟扩大清海部队任务区域至霍尔木兹海峡附近海域" data-date="11-05 23:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 23:17</span>
          <span class="news-item-title">韩国拟扩大清海部队任务区域至霍尔木兹海峡附近海域</span>
          <span class="news-value-point">💡 中新社首尔11月5日电 (记者 金旭)韩国国防部当地时间5日表示，计划向国会提交一份延长清海部队派遣期限的修订同意案，内容包括将部队任务区域扩大…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-05/10726950.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安11月5日电 (阿琳娜 魏梦鸽 张学冰)从一篇篇论文到一件件产品，从埋头攻关的实验室到“开疆拓土”的生产线，从一片普通的荷叶到超疏自洁的涂层……西北大学化工学院教授胡军带领团队研发出防黏附纳米功能涂层，让“出淤泥而不染”从一片荷叶走进工厂、油田和航天器。" data-title="潜心科研聚力转化 西大团队让超疏自洁涂层“走出”实验室" data-date="11-05 23:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 23:17</span>
          <span class="news-item-title">潜心科研聚力转化 西大团队让超疏自洁涂层“走出”实验室</span>
          <span class="news-value-point">💡 中新网西安11月5日电 (阿琳娜 魏梦鸽 张学冰)从一篇篇论文到一件件产品，从埋头攻关的实验室到“开疆拓土”的生产线，从一片普通的荷叶到超疏自洁…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-05/10726944.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网黑河11月5日电 (胡心玥 张志国)11月5日，黑龙江省首个中俄跨境综合办事大厅——黑河市中俄跨境综合服务大厅，在黑河自贸片区正式揭牌运营。大厅归集416项对俄跨境服务事项，由此从“分散办理”迈入“一厅集成”新阶段。" data-title="黑龙江省首个中俄跨境综合办事大厅正式运营" data-date="11-05 23:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 23:06</span>
          <span class="news-item-title">黑龙江省首个中俄跨境综合办事大厅正式运营</span>
          <span class="news-value-point">💡 中新网黑河11月5日电 (胡心玥 张志国)11月5日，黑龙江省首个中俄跨境综合办事大厅——黑河市中俄跨境综合服务大厅，在黑河自贸片区正式揭牌运营</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-05/10726924.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社南宁11月5日电 (陈秋霞)广西壮族自治区人民政府与加纳阿散蒂省5日在南宁签署建立友好区省关系意向书。广西壮族自治区主席韦韬会见阿散蒂省省长弗兰克·阿莫阿科辛，并共同签署意向书。" data-title="广西与加纳阿散蒂省签署建立友好区省关系意向书" data-date="11-05 22:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 22:36</span>
          <span class="news-item-title">广西与加纳阿散蒂省签署建立友好区省关系意向书</span>
          <span class="news-value-point">💡 中新社南宁11月5日电 (陈秋霞)广西壮族自治区人民政府与加纳阿散蒂省5日在南宁签署建立友好区省关系意向书</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-05/10726848.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网悉尼11月5日电 (记者 薄雯雯)2026深圳全球招商大会悉尼分会场活动4日在澳大利亚悉尼举办，中澳政商界近百名代表出席。" data-title="2026深圳全球招商大会悉尼分会场活动举行" data-date="11-05 20:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 20:46</span>
          <span class="news-item-title">2026深圳全球招商大会悉尼分会场活动举行</span>
          <span class="news-value-point">💡 中新网悉尼11月5日电 (记者 薄雯雯)2026深圳全球招商大会悉尼分会场活动4日在澳大利亚悉尼举办，中澳政商界近百名代表出席</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/metas-warns-that-election-backlash-against-data-centers-could-make-ai-expansion-harder/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta警告说，随着社区对大规模基础设施项目的抵制，对数据中心的政治反对可能会威胁到未来的人工智能投资。" data-title="Meta warns that election backlash against data centers could make AI expansion harder" data-date="11-06 03:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 03:12</span>
          <span class="news-item-title">Meta警告称，选举对数据中心的强烈反对可能会使人工智能扩张变得更加困难</span>
          <span class="news-item-title-en">Meta warns that election backlash against data centers could make AI expansion harder</span>
          <span class="news-value-point">💡 Meta警告说，随着社区对大规模基础设施项目的抵制，对数据中心的政治反对可能会威胁到未来的人工智能投资</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/" target="_blank" rel="noopener" data-cat="keji" data-summary="随着人工智能实验室面临对其保护数字基础设施工作的审查， OpenAI最新的网络安全模型应运而生。" data-title="OpenAI released a new cybersecurity model. Is that enough?" data-date="11-06 03:06" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 03:06</span>
          <span class="news-item-title">OpenAI发布了新的网络安全模型。够了吗？</span>
          <span class="news-item-title-en">OpenAI released a new cybersecurity model. Is that enough?</span>
          <span class="news-value-point">💡 随着人工智能实验室面临对其保护数字基础设施工作的审查， OpenAI最新的网络安全模型应运而生</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/business/stocks-midterms-artificial-intelligence.html" target="_blank" rel="noopener" data-cat="keji" data-summary="标准普尔500指数跌至一年多以来的最大单日跌幅，受科技行业拖累，投资者担心人工智能扩张的持久性。" data-title="Stocks Erase Post-Midterm Elections Rally, Dragged Down by Tech" data-date="11-06 02:57" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 02:57</span>
          <span class="news-item-title">股市抹去中期选举后的反弹，被科技拖累</span>
          <span class="news-item-title-en">Stocks Erase Post-Midterm Elections Rally, Dragged Down by Tech</span>
          <span class="news-value-point">💡 标准普尔500指数跌至一年多以来的最大单日跌幅，受科技行业拖累，投资者担心人工智能扩张的持久性</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/openai-president-greg-brockman-says-company-could-be-ipo-ready-in-2027/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI总裁格雷格·布罗克曼（ Greg Brockman ）表示，该公司可能已准备好在2027年上市，这表明企业收入将加速增长，业务也将出现转机。" data-title="OpenAI president Greg Brockman says company could be IPO ready in 2027" data-date="11-06 02:02" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 02:02</span>
          <span class="news-item-title">OpenAI总裁Greg Brockman表示，该公司可能在2027年首次公开募股</span>
          <span class="news-item-title-en">OpenAI president Greg Brockman says company could be IPO ready in 2027</span>
          <span class="news-value-point">💡 OpenAI总裁格雷格·布罗克曼（ Greg Brockman ）表示，该公司可能已准备好在2027年上市，这表明企业收入将加速增长，业务也将出…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/" target="_blank" rel="noopener" data-cat="keji" data-summary="借助Claude的个人理财服务，用户可以通过Plaid连接其银行账户和信用卡账户，并询问有关其财务状况的问题。" data-title="Claude can now analyze your spending with its new Personal Finance tool" data-date="11-06 02:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 02:00</span>
          <span class="news-item-title">Claude现在可以使用其新的个人理财工具来分析您的支出</span>
          <span class="news-item-title-en">Claude can now analyze your spending with its new Personal Finance tool</span>
          <span class="news-value-point">💡 借助Claude的个人理财服务，用户可以通过Plaid连接其银行账户和信用卡账户，并询问有关其财务状况的问题</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry" target="_blank" rel="noopener" data-cat="keji" data-summary="MeitY秘书S. Krishnan表示，印度计划根据半导体任务2.0开发自己的GPU ，目标是大约两年。该国还希望将其SHAKTI和VEGA RISC-V处理器商业化，扩大国内服务器" data-title="India targets creating homegrown GPUs within 2 years and plans to commercialize indigenous SHAKTI and VEGA processors" data-date="11-06 02:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 02:00</span>
          <span class="news-item-title">印度的目标是在2年内创建本土GPU ，并计划将本土SHAKTI和VEGA处理器商业化</span>
          <span class="news-item-title-en">India targets creating homegrown GPUs within 2 years and plans to commercialize indigenous SHAKTI and VEGA processors</span>
          <span class="news-value-point">💡 MeitY秘书S. Krishnan表示，印度计划根据半导体任务2.0开发自己的GPU ，目标是大约两年</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic为管理您的个人财务提出了一个新的策略：让Claude来代替，使用新的个人财务功能，通过Plaid银行桥接平台将其连接到您的银行和信用卡账户。你可以问聊天机器人“我的m在哪里" data-title="Claude AI can plug directly into your bank account" data-date="11-06 02:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 02:00</span>
          <span class="news-item-title">Claude AI可以直接插入您的银行账户</span>
          <span class="news-item-title-en">Claude AI can plug directly into your bank account</span>
          <span class="news-value-point">💡 Anthropic为管理您的个人财务提出了一个新的策略：让Claude来代替，使用新的个人财务功能，通过Plaid银行桥接平台将其连接到您的银行…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1026927/total-repudiation-the-blue-wave-is-about-to-hit-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="周二晚上，民主党人控制了众议院和参议院，创造了历史，一股蓝色的浪潮席卷了传统的红色和摇摆州-全国第一位黑人女州长在格鲁吉亚当选，这是该国第一位原住民" data-title="‘Total repudiation’: The blue wave is about to hit AI" data-date="11-06 01:51" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 01:51</span>
          <span class="news-item-title">“彻底否定” ：蓝色浪潮即将击中AI</span>
          <span class="news-item-title-en">‘Total repudiation’: The blue wave is about to hit AI</span>
          <span class="news-value-point">💡 周二晚上，民主党人控制了众议院和参议院，创造了历史，一股蓝色的浪潮席卷了传统的红色和摇摆州-全国第一位黑人女州长在格鲁吉亚当选，这是该国第一位原…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/chinese-ai-lab-moonshot-reportedly-looked-at-european-data-centers-to-access-nvidia-chips-report-claims-kimi-maker-primarily-interested-in-inferencing-capacity-but-also-asked-about-training-clusters" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，该实验室有兴趣租用至少8,000个Nvidia Blackwell GPU。" data-title="Chinese AI lab Moonshot reportedly looked at European data centers to access Nvidia chips, report claims" data-date="11-06 00:48" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 00:48</span>
          <span class="news-item-title">据报道，中国人工智能实验室Moonshot研究了欧洲数据中心以访问Nvidia芯片</span>
          <span class="news-item-title-en">Chinese AI lab Moonshot reportedly looked at European data centers to access Nvidia chips, report claims</span>
          <span class="news-value-point">💡 据报道，该实验室有兴趣租用至少8,000个Nvidia Blackwell GPU</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/axiom-math-wants-to-keep-ai-slop-out-of-mathematics/" target="_blank" rel="noopener" data-cat="keji" data-summary="随着人工智能用未经检查的证明充斥数学，公理数学押注于验证。这家初创公司的人工智能代理刚刚正式验证了Stacks项目，这是该领域最大的库之一。" data-title="Axiom Math wants to keep AI slop out of mathematics" data-date="11-06 00:16" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 00:16</span>
          <span class="news-item-title">Axiom Math希望将AI SLOP排除在数学之外</span>
          <span class="news-item-title-en">Axiom Math wants to keep AI slop out of mathematics</span>
          <span class="news-value-point">💡 随着人工智能用未经检查的证明充斥数学，公理数学押注于验证</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/020.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 6 日消息，苹果首款触控屏 MacBook Pro（配备 PROLED XDR 显示屏的 MacBook Pro）今日正式开售，定价 22999 元起。基础配置为 M5 Pro 芯片（15 核 CPU/16 核 GPU）、24GB 内存、1TB 硬盘，支持在购买时按需升级配置。京东 Apple MacBook Pro (PROLED XDR 显示屏) 22999 元直达链接IT之家了解到，这款笔记本提供 14 英寸与 16 英寸两种机型，搭载双层串联 OLED 技术，具有最高达 2,000 尼特的峰值 HDR 和 SDR 亮度，对比度 10,000,000:1，支持 120Hz 可变刷新率，覆盖 P3 和 Adobe RGB 广色域。这款全新 MacBook Pro 还首" data-title="22999 元起：苹果首款触屏 MacBook Pro 正式开售，可选 M5 Pro/M5 Max 芯片" data-date="11-06 00:00" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 00:00</span>
          <span class="news-item-title">22999 元起：苹果首款触屏 MacBook Pro 正式开售，可选 M5 Pro/M5 Max 芯片</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，苹果首款触控屏 MacBook Pro（配备 PROLED XDR 显示屏的 MacBook Pro）今日正式开…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/019.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 5 日消息，博主 @WHYLAB 今日分享了荣耀 700 系列手机的盲盒周边。从盲盒可以看出，荣耀 700 系列手机将采用小矩阵背屏设计。博主透露，背屏尺寸为 1.72 英寸。该博主还透露，荣耀 700 标准版采用骁龙 8s Gen4 处理器，Pro 则搭载骁龙 8 Gen5 处理器。据IT之家今日早些时候报道，博主 @数码闲聊站 今日爆料，荣耀 700 系列手机采用同档唯一双 8 芯片，拥有更强性能 + 更大电池 + 潜望镜 + 旗舰影像 + 自拍背屏。荣耀全球首席营销官关海涛于 11 月 3 日发文，正式官宣了数字 700 系列手机。他表示，系列新机方向很明确：继承旗舰级影像能力、探索 AI 时代年轻人的新鲜玩法，并守住荣耀一直以来的优势长板。" data-title="荣耀 700 系列手机盲盒周边曝光：背屏设计确认，消息称标准版搭载骁龙 8s Gen4 处理器" data-date="11-05 23:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-05 23:46</span>
          <span class="news-item-title">荣耀 700 系列手机盲盒周边曝光：背屏设计确认，消息称标准版搭载骁龙 8s Gen4 处理器</span>
          <span class="news-value-point">💡 IT之家 11 月 5 日消息，博主 @WHYLAB 今日分享了荣耀 700 系列手机的盲盒周边</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/017.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 5 日消息，英伟达官方今日庆祝 GeForce 8800 GTX 显卡诞生 20 周年，同步推出一款 Steam 演示游戏，带领 PC 玩家回到 2006 年，一睹这款经典显卡的外貌。据IT之家了解，GeForce 8800 GTX 诞生于 2006 年 11 月 8 日，是首款支持 CUDA 的 NVIDIA 显卡，为图形渲染以外的 GPU 计算奠定了基础，并推动形成了加速计算平台。GeForce 8800 GTX 是 06 年的 NVIDIA 旗舰显卡，建议零售价 599 美元（IT之家注：现汇率约合 4,005 元人民币），采用 Tesla GPU 架构，基于 G80 芯片打造，制程工艺为 90nm，带有 128 个核心。而 CUDA 最初作为并行计算平台和 API" data-title="英伟达庆祝首款支持 CUDA 显卡 GeForce 8800 GTX 诞生 20 周年，同步推出纪念游戏带 PC 玩家重返 2006 年" data-date="11-05 23:23" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-05 23:23</span>
          <span class="news-item-title">英伟达庆祝首款支持 CUDA 显卡 GeForce 8800 GTX 诞生 20 周年，同步推出纪念游戏带 PC 玩家重返 2006 年</span>
          <span class="news-value-point">💡 IT之家 11 月 5 日消息，英伟达官方今日庆祝 GeForce 8800 GTX 显卡诞生 20 周年，同步推出一款 Steam 演示游戏，…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/dropbox-acquires-tigris-data-for-350m-to-bolster-its-ai-iinfrastructure/" target="_blank" rel="noopener" data-cat="keji" data-summary="这笔交易预计将支持DBX Agent Cloud的开发，这是一个新的存储平台，旨在帮助开发人员构建人工智能模型和代理。" data-title="Dropbox acquires Tigris Data for $350M to bolster its AI infrastructure" data-date="11-05 23:19" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-05 23:19</span>
          <span class="news-item-title">Dropbox以3.5亿美元收购Tigris Data ，以加强其人工智能基础设施</span>
          <span class="news-item-title-en">Dropbox acquires Tigris Data for $350M to bolster its AI infrastructure</span>
          <span class="news-value-point">💡 这笔交易预计将支持DBX Agent Cloud的开发，这是一个新的存储平台，旨在帮助开发人员构建人工智能模型和代理</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-leaker-claims-nova-lake-desktop-chips-have-5-1-ghz-clock-limit-beyond-90-c-high-clock-speeds-could-demand-significant-cooling-for-next-gen-chips" target="_blank" rel="noopener" data-cat="keji" data-summary="一位知名的英特尔泄密者声称，如果CPU核心温度不低于90°C ，英特尔的下一代处理器将达到5.1 GHz。" data-title="Intel leaker claims Nova Lake desktop chips have 5.1 GHz clock limit beyond 90°C" data-date="11-05 22:57" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-05 22:57</span>
          <span class="news-item-title">英特尔泄密者声称Nova Lake台式机芯片具有超过90°C的5.1 GHz时钟限制</span>
          <span class="news-item-title-en">Intel leaker claims Nova Lake desktop chips have 5.1 GHz clock limit beyond 90°C</span>
          <span class="news-value-point">💡 一位知名的英特尔泄密者声称，如果CPU核心温度不低于90°C ，英特尔的下一代处理器将达到5.1 GHz</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck5ynzry64p2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领电脑游戏《足球经理27》（ Football Manager 27 ） ，以及英国广播公司的读者和人工智能，对本周末的英超赛事进行了预测。" data-title="Sutton&#39;s predictions v Football Manager, the game" data-date="11-06 02:02" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 02:02</span>
          <span class="news-item-title">萨顿的预测v足球经理，比赛</span>
          <span class="news-item-title-en">Sutton's predictions v Football Manager, the game</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领电脑游戏《足球经理27》（ Football Manager 27 ） …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13608535/jesus-de-miguel-funeral-family-friends-and-tenerife-players-gather-to-remember-striker-who-died-following-on-field-collision" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="特内里费岛前锋耶稣·德米格尔（ Jesus de Miguel ）的葬礼是在这位足球运动员在场上碰撞后去世后举行的。" data-title="Family, friends and Tenerife players gather for De Miguel&#39;s funeral" data-date="11-06 01:54" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:54</span>
          <span class="news-item-title">家人、朋友和特内里费岛球员聚集在一起参加德米格尔的葬礼</span>
          <span class="news-item-title-en">Family, friends and Tenerife players gather for De Miguel's funeral</span>
          <span class="news-value-point">💡 特内里费岛前锋耶稣·德米格尔（ Jesus de Miguel ）的葬礼是在这位足球运动员在场上碰撞后去世后举行的</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13608505/is-adil-rashid-still-englands-no-1-spinner-in-one-day-international-cricket" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在过去十年左右的英格兰白球板球的起伏中，其中一个常数是阿迪尔·拉希德（ Adil Rashid ）。" data-title="Is Rashid still England&#39;s No 1 spinner in ODI cricket?" data-date="11-06 01:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:45</span>
          <span class="news-item-title">拉希德仍然是英格兰ODI板球的头号旋转者吗？</span>
          <span class="news-item-title-en">Is Rashid still England's No 1 spinner in ODI cricket?</span>
          <span class="news-value-point">💡 在过去十年左右的英格兰白球板球的起伏中，其中一个常数是阿迪尔·拉希德（ Adil Rashid ）</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13607998/premier-league-predictions-jones-knows-best-bets-nottingham-forest-vs-man-city-man-utd-vs-aston-villa-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩" data-title="PL Predictions: How will your team fare this weekend?" data-date="11-06 01:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:40</span>
          <span class="news-item-title">PL预测：您的团队本周末的表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your team fare this weekend?</span>
          <span class="news-value-point">💡 我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607998/premier-league-predictions-jones-knows-best-bets-nottingham-forest-vs-man-city-man-utd-vs-aston-villa-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩" data-title="PL Predictions: How will your team fare this weekend?" data-date="11-06 01:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:40</span>
          <span class="news-item-title">PL预测：您的团队本周末的表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your team fare this weekend?</span>
          <span class="news-value-point">💡 我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw99zde82nmno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉经理Unai Emery即将同意与俱乐部续约。" data-title="Emery close to agreeing new Aston Villa contract" data-date="11-05 23:45" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-05 23:45</span>
          <span class="news-item-title">Emery即将同意新的阿斯顿维拉合同</span>
          <span class="news-item-title-en">Emery close to agreeing new Aston Villa contract</span>
          <span class="news-value-point">💡 阿斯顿维拉经理Unai Emery即将同意与俱乐部续约</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm93zvzzl33zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="菲尔·麦克纳尔蒂（ Phil McNulty ）写道，哈里·凯恩（ Harry Kane ）在拜仁慕尼黑（ Bayern Munich ）的新合同可能会结束他的英超联赛生涯，但他可以带领" data-title="What new Kane deal means for England and the Premier League record" data-date="11-05 22:44" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-05 22:44</span>
          <span class="news-item-title">新的凯恩交易对英格兰和英超联赛纪录意味着什么</span>
          <span class="news-item-title-en">What new Kane deal means for England and the Premier League record</span>
          <span class="news-value-point">💡 菲尔·麦克纳尔蒂（ Phil McNulty ）写道，哈里·凯恩（ Harry Kane ）在拜仁慕尼黑（ Bayern Munich ）的新合…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/05/the-international-break-is-almost-here-so-wave-goodbye-to-your-players-and-maybe-your-manager" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="过去是重置的时候，现在是重新雇佣的时候了，迈克尔·卡里克并不是唯一一个看着他肩上的英超经理。也许曼联复出对阵罗马的最有说服力的时刻是在终场哨响。" data-title="The international break is almost here: so wave goodbye to your players, and maybe your manager | Max Rushden" data-date="11-05 21:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-05 21:00</span>
          <span class="news-item-title">国际比赛即将到来：所以向你的球员，也许还有你的经理挥手告别| Max Rushden</span>
          <span class="news-item-title-en">The international break is almost here: so wave goodbye to your players, and maybe your manager | Max Rushden</span>
          <span class="news-value-point">💡 过去是重置的时候，现在是重新雇佣的时候了，迈克尔·卡里克并不是唯一一个看着他肩上的英超经理</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607957/man-utd-paul-merson-says-michael-carrick-needs-bruno-fernandes-on-side-and-matheus-cunha-to-be-consistent" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="保罗·梅森（ Paul Merson ）表示，迈克尔·卡里克（ Michael Carrick ）需要布鲁诺·费尔南德斯（ Bruno Fernandes ）的支持，并在曼联以3-2戏剧性地复出战胜罗马后，向马修斯·库尼亚（ Matheus Cunha" data-title="&#39;Carrick needs Bruno – but Villa could expose United&#39;" data-date="11-05 19:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 19:45</span>
          <span class="news-item-title">“卡里克需要布鲁诺–但维拉可能会暴露曼联”</span>
          <span class="news-item-title-en">'Carrick needs Bruno – but Villa could expose United'</span>
          <span class="news-value-point">💡 保罗·梅森（ Paul Merson ）表示，迈克尔·卡里克（ Michael Carrick ）需要布鲁诺·费尔南德斯（ Bruno Fern…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-05/10726787.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网11月5日电 据路透社报道，当地时间5日，葡萄牙球星克里斯蒂亚诺·罗纳尔多通过社交媒体宣布，他正式从葡萄牙国家足球队退役，结束多年的国家队生涯。" data-title="C罗宣布从葡萄牙国家足球队退役：“葡萄牙，永在我心”" data-date="11-05 18:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 18:54</span>
          <span class="news-item-title">C罗宣布从葡萄牙国家足球队退役：“葡萄牙，永在我心”</span>
          <span class="news-value-point">💡 中新网11月5日电 据路透社报道，当地时间5日，葡萄牙球星克里斯蒂亚诺·罗纳尔多通过社交媒体宣布，他正式从葡萄牙国家足球队退役，结束多年的国家队…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13608290/manchester-united-manager-latest-no-interim-planned-should-club-decide-to-sack-michael-carrick" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻被告知，如果他们决定在未来几周内取代迈克尔·卡里克，曼联不太可能任命另一位临时主教练。" data-title="Man Utd unlikely to appoint interim should they sack Carrick" data-date="11-05 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 18:00</span>
          <span class="news-item-title">如果他们解雇卡里克，曼联不太可能任命临时</span>
          <span class="news-item-title-en">Man Utd unlikely to appoint interim should they sack Carrick</span>
          <span class="news-value-point">💡 天空体育新闻被告知，如果他们决定在未来几周内取代迈克尔·卡里克，曼联不太可能任命另一位临时主教练</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13608280/liverpool-trey-nyoni-and-rio-ngumoha-starring-shows-reds-havent-spent-money-well-enough-says-jamie-carragher" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="杰米·卡拉格（ Jamie Carragher ）在欧洲冠军联赛中以3比2击败费内巴切（ Fenerbahce ）后，对利物浦的招募提出" data-title="Carra: Young guns starring shows Liverpool haven&#39;t spent money well enough" data-date="11-05 17:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 17:45</span>
          <span class="news-item-title">卡拉：主演的年轻枪手表明利物浦花的钱不够多</span>
          <span class="news-item-title-en">Carra: Young guns starring shows Liverpool haven't spent money well enough</span>
          <span class="news-value-point">💡 杰米·卡拉格（ Jamie Carragher ）在欧洲冠军联赛中以3比2击败费内巴切（ Fenerbahce ）后，对利物浦的招募提出</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw62ym8r113vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛的五个人将在曼城的命运中发挥关键作用。" data-title="Meet the people set for key role in deciding Man City fate" data-date="11-05 14:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-05 14:26</span>
          <span class="news-item-title">认识在决定曼城命运中扮演关键角色的人</span>
          <span class="news-item-title-en">Meet the people set for key role in deciding Man City fate</span>
          <span class="news-value-point">💡 英超联赛的五个人将在曼城的命运中发挥关键作用</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/meta-says-us-users-can-now-video-chat-with-their-muse-ai-avatar/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Meta的AI代理现在可以在推出旨在让Muse栩栩如生的类似Tamagotchi的可穿戴设备之前，将呼叫作为可定制的动画头像。" data-title="Meta says US users can now video chat with their Muse AI avatar" data-date="11-06 03:48" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 03:48</span>
          <span class="news-item-title">Meta表示，美国用户现在可以与他们的Muse AI头像进行视频聊天</span>
          <span class="news-item-title-en">Meta says US users can now video chat with their Muse AI avatar</span>
          <span class="news-value-point">💡 Meta的AI代理现在可以在推出旨在让Muse栩栩如生的类似Tamagotchi的可穿戴设备之前，将呼叫作为可定制的动画头像</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13574263/liv-golf-league-timeline-key-moments-from-breakaway-circuits-history-rivalry-with-the-pga-tour-and-what-happens-next" target="_blank" rel="noopener" data-cat="zonghe" data-summary="LIV高尔夫联盟在宣布进入清算五年后似乎已经结束。" data-title="LIV Golf: Timeline from big beginnings to liquidation" data-date="11-06 03:35" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 03:35</span>
          <span class="news-item-title">LIV高尔夫：从大起点到清算的时间表</span>
          <span class="news-item-title-en">LIV Golf: Timeline from big beginnings to liquidation</span>
          <span class="news-value-point">💡 LIV高尔夫联盟在宣布进入清算五年后似乎已经结束</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13608523/raymond-van-barneveld-secures-world-darts-championship-spot-as-tommy-morris-stuns-luke-humphries-in-players-championship-34" target="_blank" rel="noopener" data-cat="zonghe" data-summary="五届世界冠军雷蒙德·范·巴内费尔德（ Raymond van Barneveld ）在今年的世界飞镖锦标赛中获得了一席之地，而非巡回赛卡持有人汤米·莫里斯（ Tommy Morris ）让卢克·汉弗莱斯（ Luke Humphries ）惊呆了，赢得了最后的球员" data-title="Van Barneveld secures World Championship spot as Evans forced to qualify" data-date="11-06 03:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 03:30</span>
          <span class="news-item-title">Van Barneveld获得世界锦标赛席位， Evans被迫获得资格</span>
          <span class="news-item-title-en">Van Barneveld secures World Championship spot as Evans forced to qualify</span>
          <span class="news-value-point">💡 五届世界冠军雷蒙德·范·巴内费尔德（ Raymond van Barneveld ）在今年的世界飞镖锦标赛中获得了一席之地，而非巡回赛卡持有人汤…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1027659/samsung-galaxy-z-fold-8-beats-pill-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="安卓粉丝对iPhone Duo有点羡慕，请注意：三星Galaxy Z Fold 8在亚马逊和百思买都打折至1,599.99美元，比平时低300美元，只比我们见过的最低价高50美元。考虑到开发人员" data-title="Samsung’s Galaxy Z Fold 8 is $300 off ahead of Black Friday" data-date="11-06 03:12" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 03:12</span>
          <span class="news-item-title">三星Galaxy Z Fold 8在黑色星期五前立减$ 300</span>
          <span class="news-item-title-en">Samsung’s Galaxy Z Fold 8 is $300 off ahead of Black Friday</span>
          <span class="news-value-point">💡 安卓粉丝对iPhone Duo有点羡慕，请注意：三星Galaxy Z Fold 8在亚马逊和百思买都打折至1,599.99美元，比平时低300美…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028015/meta-muse-ai-voice-mode-expressive-avatar" target="_blank" rel="noopener" data-cat="zonghe" data-summary="首席执行官马克·扎克伯格（ Mark Zuckerberg ）今天宣布， Meta现在可以让您与Muse AI代理进行实时语音对话。该功能已向我推出，我在撰写本文时在iOS应用程序上进行了演示。当您与您的Muse ag聊天时" data-title="Muse has a voice mode now" data-date="11-06 03:03" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 03:03</span>
          <span class="news-item-title">Muse现在有语音模式</span>
          <span class="news-item-title-en">Muse has a voice mode now</span>
          <span class="news-value-point">💡 首席执行官马克·扎克伯格（ Mark Zuckerberg ）今天宣布， Meta现在可以让您与Muse AI代理进行实时语音对话</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/028.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 6 日消息，据央视新闻报道，11 月 5 日 23 时 58 分，长征二号丙运载火箭在西昌卫星发射中心点火升空，随后成功将遥感五十一号 07-09 星送入预定轨道，发射任务取得圆满成功。长二丙火箭由中国航天科技集团有限公司一院抓总研制，为两级常温液体运载火箭，具备一箭一星、一箭多星发射及星座部署能力。IT之家查询获悉，该卫星主要用于科学试验、电磁环境探测等领域。另外，本次发射是长征系列运载火箭的第 675 次发射。" data-title="我国成功发射遥感五十一号 07-09 星，主要用于科学试验、电磁环境探测等领域" data-date="11-06 02:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 02:39</span>
          <span class="news-item-title">我国成功发射遥感五十一号 07-09 星，主要用于科学试验、电磁环境探测等领域</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，据央视新闻报道，11 月 5 日 23 时 58 分，长征二号丙运载火箭在西昌卫星发射中心点火升空，随后成功将遥…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1023553/ea-classic-pc-games-steam-anniversary-edition" target="_blank" rel="noopener" data-cat="zonghe" data-summary="艺电将在Steam上推出25款经典游戏，包括摩托车赛车手Road Rash的“周年纪念版”和六款Wing Commander游戏。这些周年纪念版保留了“游戏的原创外观、感觉和创意意图” bu" data-title="EA is bringing 25 classic PC games to Steam" data-date="11-06 02:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 02:30</span>
          <span class="news-item-title">EA将为Steam带来25款经典PC游戏</span>
          <span class="news-item-title-en">EA is bringing 25 classic PC games to Steam</span>
          <span class="news-value-point">💡 艺电将在Steam上推出25款经典游戏，包括摩托车赛车手Road Rash的“周年纪念版”和六款Wing Commander游戏</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13608312/kimi-antonelli-new-f1-world-champion-reveals-details-of-title-celebrations-and-special-messages-received-from-fellow-sports-stars" target="_blank" rel="noopener" data-cat="zonghe" data-summary="基米·安东内利（ Kimi Antonelli ）在加冕F1世界冠军后透露了他的庆祝活动的细节，以及他在历史性胜利后收到的一些信息。" data-title="&#39;I went full out!&#39; - Antonelli reveals title celebrations" data-date="11-06 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 02:30</span>
          <span class="news-item-title">（我全力以赴了！ '- Antonelli揭示了冠军庆祝活动</span>
          <span class="news-item-title-en">'I went full out!' - Antonelli reveals title celebrations</span>
          <span class="news-value-point">💡 基米·安东内利（ Kimi Antonelli ）在加冕F1世界冠军后透露了他的庆祝活动的细节，以及他在历史性胜利后收到的一些信息</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately" target="_blank" rel="noopener" data-cat="zonghe" data-summary="结合OpenSSH和musl-libc漏洞，任何人都可以通过键入超过256个字符的密码进入Alpine Linux和其他发行版" data-title="Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and other distros by typing anything over 256 characters as a password" data-date="11-06 02:14" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 02:14</span>
          <span class="news-item-title">结合OpenSSH和musl-libc漏洞，任何人都可以通过键入超过256个字符的密码进入Alpine Linux和其他发行版</span>
          <span class="news-item-title-en">Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and other distros by typing anything over 256 characters as a password</span>
          <span class="news-value-point">💡 结合OpenSSH和musl-libc漏洞，任何人都可以通过键入超过256个字符的密码进入Alpine Linux和其他发行版</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1027689/ember-cup-6-ounce-woot-kitchen-sale-deal" target="_blank" rel="noopener" data-cat="zonghe" data-summary="多年来，我们一直是Ember温控杯的粉丝，尽管考虑到价格标签，我们承认它们有点奢侈。值得庆幸的是，如果您一直在寻找更实惠的选择， Woot正在出售黑色的Ember Cup" data-title="Ember’s smallest self-heating mug is on sale for just $33" data-date="11-06 01:34" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 01:34</span>
          <span class="news-item-title">Ember最小的自热杯仅售$ 33</span>
          <span class="news-item-title-en">Ember’s smallest self-heating mug is on sale for just $33</span>
          <span class="news-value-point">💡 多年来，我们一直是Ember温控杯的粉丝，尽管考虑到价格标签，我们承认它们有点奢侈</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279298/crystal-palace-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Crystal Palace latest: Sage gives cryptic response over Disasi absence vs Hoffenheim" data-title="Crystal Palace latest: Sage gives cryptic response over Disasi absence vs Hoffenheim" data-date="11-06 01:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:30</span>
          <span class="news-item-title">水晶宫最新消息： Sage对Disasi缺席vs Hoffenheim给出了神秘的回应</span>
          <span class="news-item-title-en">Crystal Palace latest: Sage gives cryptic response over Disasi absence vs Hoffenheim</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1027772/tiktok-shop-app" target="_blank" rel="noopener" data-cat="zonghe" data-summary="正如社交媒体顾问马特·纳瓦拉（ Matt Navarra ）所发现的那样， TikTok已在几个国家发布了一款适用于TikTok商店的独立应用程序。根据其App Store列表， TikTok Shop应用程序提供： -受您的兴趣启发的个性化精选-直播" data-title="TikTok launched a dedicated TikTok Shop app" data-date="11-06 01:27" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 01:27</span>
          <span class="news-item-title">TikTok推出专用TikTok商店应用程序</span>
          <span class="news-item-title-en">TikTok launched a dedicated TikTok Shop app</span>
          <span class="news-value-point">💡 正如社交媒体顾问马特·纳瓦拉（ Matt Navarra ）所发现的那样， TikTok已在几个国家发布了一款适用于TikTok商店的独立应用程…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c8y56z50k95xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="纽卡斯尔联队主教练马蒂亚斯·贾斯尔（ Matthias Jaissle ）表示，他“从俱乐部内部获得了更多的感觉” ，即在他的球队挣扎的情况下，他们对他的“承诺”。" data-title="Good to feel club are committed to me" data-date="11-06 01:25" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 01:25</span>
          <span class="news-item-title">感觉很好，俱乐部对我很忠诚</span>
          <span class="news-item-title-en">Good to feel club are committed to me</span>
          <span class="news-value-point">💡 纽卡斯尔联队主教练马蒂亚斯·贾斯尔（ Matthias Jaissle ）表示，他“从俱乐部内部获得了更多的感觉” ，即在他的球队挣扎的情况下，…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1027757/nintendo-switch-2-price-hike-plans-ram" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据路透社报道，任天堂总裁古川俊太郎在公司最新的财报电话会议上表示， “不考虑对Switch 2的价格进行额外调整”。今年早些时候， Switch 2的价格上涨了50 $ ，带来了起步价" data-title="Nintendo says it’s not planning another Switch 2 price hike" data-date="11-06 01:24" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 01:24</span>
          <span class="news-item-title">任天堂表示不会计划再次提高Switch 2的价格</span>
          <span class="news-item-title-en">Nintendo says it’s not planning another Switch 2 price hike</span>
          <span class="news-value-point">💡 据路透社报道，任天堂总裁古川俊太郎在公司最新的财报电话会议上表示， “不考虑对Switch 2的价格进行额外调整”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10726977.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国地震台网正式测定：11月06日00时56分在新疆和田地区和康县(北纬35.64度，东经78.14度)发生4.8级地震，震源深度60千米。" data-title="新疆和田地区和康县发生4.8级地震 震源深度60千米" data-date="11-06 01:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 01:20</span>
          <span class="news-item-title">新疆和田地区和康县发生4.8级地震 震源深度60千米</span>
          <span class="news-value-point">💡 中国地震台网正式测定：11月06日00时56分在新疆和田地区和康县(北纬35.64度，东经78.14度)发生4.8级地震，震源深度60千米</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-06 04:08（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
