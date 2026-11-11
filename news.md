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
      <span>2026-11-11 23:30 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×17 · 天空体育×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-11/10730564.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月11日电#8195;中共中央政治局委员、外交部长王毅11日同美国国务卿鲁比奥通电话。双方就中美关系及两国元首互动深入交换意见，通话是积极和建设性的。" data-title="王毅同美国国务卿鲁比奥通电话" data-date="11-11 23:09" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-11 23:09</span>
      </div>
      <h2 class="hero-featured-title">王毅同美国国务卿鲁比奥通电话</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/11/us/politics/jim-himes-cia-house-intelligence-oversight.html" target="_blank" rel="noopener" data-cat="keji" data-summary="众议员吉姆·希梅斯（Jim Himes）将在新一届国会中领导影响力巨大的情报委员会，他表示，他也计划仔细审查承包商对特朗普总统建筑项目的捐款。" data-title="Incoming House Intelligence Chairman Vows Oversight of CIA’s Use of Covert Action" data-date="11-11 23:27" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Incoming House Intelligence Chairman Vows Oversight of CIA’s Use of Covert Action</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/watch/video/13611018/manchester-utd-latest-five-things-mauricio-pochettino-will-need-to-sort-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的尼克·赖特（Nick Wright）分析了毛里西奥·波切蒂诺（Mauricio Pochettino）如果并一旦接替迈克尔·卡里克（Michael Carrick）担任曼联主教练，将需要解决的五个问题。" data-title="FIVE things Pochettino will need to sort out at Man Utd" data-date="11-11 21:30" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">FIVE things Pochettino will need to sort out at Man Utd</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1031301/sharge-140w-gan-charger-lenovo-yoga-mini-desktop-pc-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="正在寻找一款既时尚又实用的MacBook和设备充电器吗？亚马逊和 Sharge 都在销售 Pixel 140W GaN 充电器，售价分别为 69.88 美元和 69.90 美元，比原价优惠 24 美元。如果您不需要那么大的功率" data-title="Sharge’s eye-catching MacBook charger is over 25 percent off" data-date="11-11 23:30" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Sharge’s eye-catching MacBook charger is over 25 percent off</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730564.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月11日电#8195;中共中央政治局委员、外交部长王毅11日同美国国务卿鲁比奥通电话。双方就中美关系及两国元首互动深入交换意见，通话是积极和建设性的。" data-title="王毅同美国国务卿鲁比奥通电话" data-date="11-11 23:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 23:09</span>
          <span class="news-item-title">王毅同美国国务卿鲁比奥通电话</span>
          <span class="news-value-point">💡 新华社北京11月11日电#8195;中共中央政治局委员、外交部长王毅11日同美国国务卿鲁比奥通电话</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/us/elections/trump-voters-democrats-priorities.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党在政治中间派中取得的成功是否预示着该国将出现广泛的政治重组？还是说这只是暂时远离一位不受欢迎的总统？" data-title="The Moderates Who Chose Democrats. For Now." data-date="11-11 22:27" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-11 22:27</span>
          <span class="news-item-title">选择民主党的温和派。目前是这样。</span>
          <span class="news-item-title-en">The Moderates Who Chose Democrats. For Now.</span>
          <span class="news-value-point">💡 民主党在政治中间派中取得的成功是否预示着该国将出现广泛的政治重组</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730556.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月11日电 (记者 蔡敏婕)2026年亚太经合组织(APEC)领导人会议周新闻中心11日在广东深圳启用，工作区域总面积1.5万平方米的新闻中心将为近5000名中外注册记者提供新闻服务保障。" data-title="（深圳APEC）2026年APEC领导人会议周新闻中心启用" data-date="11-11 22:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 22:05</span>
          <span class="news-item-title">（深圳APEC）2026年APEC领导人会议周新闻中心启用</span>
          <span class="news-value-point">💡 中新社深圳11月11日电 (记者 蔡敏婕)2026年亚太经合组织(APEC)领导人会议周新闻中心11日在广东深圳启用，工作区域总面积1.5万平方…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730554.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科11月11日电 俄罗斯、美国、乌克兰三方会谈代表11日在阿拉伯联合酋长国首都阿布扎比结束会谈。俄罗斯总统助理、俄方代表团团长梅金斯基在会谈结束后对媒体表示，欧洲安全体系是本次会谈的核心议题，各方在某些方面达成了共识。俄乌就新一轮大规模换俘达成一致。" data-title="俄美乌三方会谈结束 俄乌就大规模换俘达成一致" data-date="11-11 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 22:03</span>
          <span class="news-item-title">俄美乌三方会谈结束 俄乌就大规模换俘达成一致</span>
          <span class="news-value-point">💡 中新社莫斯科11月11日电 俄罗斯、美国、乌克兰三方会谈代表11日在阿拉伯联合酋长国首都阿布扎比结束会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730551.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月11日电 题：两岸民众在北京碧云寺追思中山先生" data-title="两岸民众在北京碧云寺追思中山先生" data-date="11-11 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 22:01</span>
          <span class="news-item-title">两岸民众在北京碧云寺追思中山先生</span>
          <span class="news-value-point">💡 中新社北京11月11日电 题：两岸民众在北京碧云寺追思中山先生</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730549.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月11日电 中共中央政治局常委、全国政协主席王沪宁11日在北京会见古巴党和政府特使、古共中央政治局委员、外交部长罗德里格斯。" data-title="王沪宁会见古巴党和政府特使、古共中央政治局委员、外交部长罗德里格斯" data-date="11-11 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 22:00</span>
          <span class="news-item-title">王沪宁会见古巴党和政府特使、古共中央政治局委员、外交部长罗德里格斯</span>
          <span class="news-value-point">💡 中新社北京11月11日电 中共中央政治局常委、全国政协主席王沪宁11日在北京会见古巴党和政府特使、古共中央政治局委员、外交部长罗德里格斯</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730550.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月11日电 中国自然资源部中国地质调查局11日消息，国际地质科学联合会近日公布了第三批100个世界地质遗产地名录，中国有三处“上榜”，分别是鲜水河断裂、云阳中侏罗世恐龙化石群和大别山三叠纪超高压变质带。" data-title="中国新增三处世界地质遗产地" data-date="11-11 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 21:59</span>
          <span class="news-item-title">中国新增三处世界地质遗产地</span>
          <span class="news-value-point">💡 中新社北京11月11日电 中国自然资源部中国地质调查局11日消息，国际地质科学联合会近日公布了第三批100个世界地质遗产地名录，中国有三处“上榜…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730548.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月11日电 (记者 马帅莎)据中国航天科技集团消息，北京时间11月11日19时41分，中国在酒泉卫星发射中心使用长征二号丁运载火箭，将探源计划探路者卫星发射升空，卫星顺利进入预定轨道，发射任务取得圆满成功。" data-title="中国发射探源计划探路者卫星" data-date="11-11 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 21:59</span>
          <span class="news-item-title">中国发射探源计划探路者卫星</span>
          <span class="news-value-point">💡 中新社北京11月11日电 (记者 马帅莎)据中国航天科技集团消息，北京时间11月11日19时41分，中国在酒泉卫星发射中心使用长征二号丁运载火箭…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730538.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月11日电 学习贯彻党的二十届五中全会精神中央宣讲团报告会11月11日在中宣部举行。中央宣讲团成员、中共中央政治局委员、中宣部部长李书磊作宣讲报告。" data-title="学习贯彻党的二十届五中全会精神中央宣讲团在中宣部宣讲" data-date="11-11 21:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 21:44</span>
          <span class="news-item-title">学习贯彻党的二十届五中全会精神中央宣讲团在中宣部宣讲</span>
          <span class="news-value-point">💡 新华社北京11月11日电 学习贯彻党的二十届五中全会精神中央宣讲团报告会11月11日在中宣部举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-11/10730536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月11日电 据重庆市纪委监委消息：经重庆市委批准，重庆市纪委监委对重庆市永川区人大常委会原党组成员、副主任王寒峰严重违纪违法问题进行了立案审查调查。" data-title="重庆市永川区人大常委会原副主任王寒峰被“双开”" data-date="11-11 21:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 21:34</span>
          <span class="news-item-title">重庆市永川区人大常委会原副主任王寒峰被“双开”</span>
          <span class="news-value-point">💡 中新网11月11日电 据重庆市纪委监委消息：经重庆市委批准，重庆市纪委监委对重庆市永川区人大常委会原党组成员、副主任王寒峰严重违纪违法问题进行了…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730408.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达11月11日电 题：从苏加诺到当地华侨：孙中山与印尼的百年联系" data-title="从苏加诺到当地华侨：孙中山与印尼的百年联系" data-date="11-11 20:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 20:27</span>
          <span class="news-item-title">从苏加诺到当地华侨：孙中山与印尼的百年联系</span>
          <span class="news-value-point">💡 中新社雅加达11月11日电 题：从苏加诺到当地华侨：孙中山与印尼的百年联系</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730405.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月11日电 综合俄罗斯媒体报道，率俄罗斯代表团在阿联酋阿布扎比参加俄美乌三方会谈的俄总统助理梅金斯基11日公布了本轮俄美乌三方会谈的部分成果。" data-title="俄罗斯公布本轮俄美乌三方会谈部分成果" data-date="11-11 20:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 20:04</span>
          <span class="news-item-title">俄罗斯公布本轮俄美乌三方会谈部分成果</span>
          <span class="news-value-point">💡 中新网11月11日电 综合俄罗斯媒体报道，率俄罗斯代表团在阿联酋阿布扎比参加俄美乌三方会谈的俄总统助理梅金斯基11日公布了本轮俄美乌三方会谈的部…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730403.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月11日电 综合伊朗媒体报道，针对美国国务院宣布将对提供有关伊朗核计划情报者提供最高2000万美元奖励一事，伊朗外交部长阿拉格齐10日致信联合国秘书长、联合国安理会主席以及国际原子能机构总干事，呼吁相关方面对美国此举予以谴责。" data-title="伊朗外长致信联合国：要求谴责美国悬赏征集伊核情报" data-date="11-11 20:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 20:03</span>
          <span class="news-item-title">伊朗外长致信联合国：要求谴责美国悬赏征集伊核情报</span>
          <span class="news-value-point">💡 中新网11月11日电 综合伊朗媒体报道，针对美国国务院宣布将对提供有关伊朗核计划情报者提供最高2000万美元奖励一事，伊朗外交部长阿拉格齐10日…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730400.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月11日，俄谈判代表团团长、俄总统助理梅金斯基公布了本轮俄美乌三方会谈的部分成果。" data-title="俄方公布本轮俄美乌三方会谈成果" data-date="11-11 19:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 19:33</span>
          <span class="news-item-title">俄方公布本轮俄美乌三方会谈成果</span>
          <span class="news-value-point">💡 当地时间11月11日，俄谈判代表团团长、俄总统助理梅金斯基公布了本轮俄美乌三方会谈的部分成果</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730378.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社安塔利亚11月11日电(记者 陈溯)《联合国气候变化框架公约》第三十一次缔约方大会(COP31)正在土耳其安塔利亚举行。《联合国气候变化框架公约》秘书处执行秘书西蒙·斯蒂尔在大会开幕致辞中表示，全球气候行动已进入“落实阶段”，COP31除了继续释放信号，还必须把全球目标和国家计划分解为具体步骤，推出可落地的方案。" data-title="《联合国气候变化框架公约》秘书处执行秘书：须推出可落地方案" data-date="11-11 19:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 19:15</span>
          <span class="news-item-title">《联合国气候变化框架公约》秘书处执行秘书：须推出可落地方案</span>
          <span class="news-value-point">💡 中新社安塔利亚11月11日电(记者 陈溯)《联合国气候变化框架公约》第三十一次缔约方大会(COP31)正在土耳其安塔利亚举行</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/us/politics/jim-himes-cia-house-intelligence-oversight.html" target="_blank" rel="noopener" data-cat="keji" data-summary="众议员吉姆·希梅斯（Jim Himes）将在新一届国会中领导影响力巨大的情报委员会，他表示，他也计划仔细审查承包商对特朗普总统建筑项目的捐款。" data-title="Incoming House Intelligence Chairman Vows Oversight of CIA’s Use of Covert Action" data-date="11-11 23:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-11 23:27</span>
          <span class="news-item-title">即将上任的众议院情报委员会主席誓言监督中央情报局的秘密行动</span>
          <span class="news-item-title-en">Incoming House Intelligence Chairman Vows Oversight of CIA’s Use of Covert Action</span>
          <span class="news-value-point">💡 众议员吉姆·希梅斯（Jim Himes）将在新一届国会中领导影响力巨大的情报委员会，他表示，他也计划仔细审查承包商对特朗普总统建筑项目的捐款</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， SpaceX正在开发一种采用72个Nvidia Rubin GPU的“Kessel”机架式系统设计，该系统依赖于一个巨大的84层PCB中板。" data-title="SpaceX develops its own ‘Kessel’ rack-scale system featuring 72 Nvidia Rubin GPUs for data centers in space, report claims" data-date="11-11 23:03" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 23:03</span>
          <span class="news-item-title">报告称， SpaceX为太空数据中心开发了自己的“Kessel”机架式系统，配备72个Nvidia Rubin GPU</span>
          <span class="news-item-title-en">SpaceX develops its own ‘Kessel’ rack-scale system featuring 72 Nvidia Rubin GPUs for data centers in space, report claims</span>
          <span class="news-value-point">💡 据报道， SpaceX正在开发一种采用72个Nvidia Rubin GPU的“Kessel”机架式系统设计，该系统依赖于一个巨大的84层PCB…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/821.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 11 日消息，数据挖掘者最近一直在研究 Xbox 版《GTA 6》的预载文件，而近期发现的两项线索，让这款游戏的运行表现有了更多值得期待的地方。IT之家注意到，在数据挖掘者 Tex2 分享的文件包中，出现了两个库文件，分别名为 amd_fidelityfx_loader_xbox.dll 和 amd_fidelityfx_upscaler_xbox.dll。这两个文件的名称与微软上周发布的 FSR 4.1 Xbox GDK 示例项目中的相关术语一致。当然，这并不意味着 AMD 的 FSR 4.1 技术一定会在《GTA 6》发售时，或者在游戏推出后加入其中。不过，至少可以确认，游戏存在采用最新超分辨率技术的可能性。FSR 4 是 AMD 超分辨率技术的一次重大升级，将此前以" data-title="Xbox 版《GTA 6》预载文件出现 AMD FSR 4.1 线索，首发未必支持" data-date="11-11 23:02" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 23:02</span>
          <span class="news-item-title">Xbox 版《GTA 6》预载文件出现 AMD FSR 4.1 线索，首发未必支持</span>
          <span class="news-value-point">💡 IT之家 11 月 11 日消息，数据挖掘者最近一直在研究 Xbox 版《GTA 6》的预载文件，而近期发现的两项线索，让这款游戏的运行表现有了…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/" target="_blank" rel="noopener" data-cat="keji" data-summary="在12,000名员工中， AI Ghodsi是第一个承认他不可能认识每个人的人，他们也不太可能向他坦白出错的事情。但他不需要他们。为此，他使用了Databricks新修订的精灵特工。" data-title="Databricks’ new AI agent tells CEO Ali Ghodsi the unvarnished truth" data-date="11-11 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-11 23:00</span>
          <span class="news-item-title">Databricks的新人工智能代理告诉首席执行官Ali Ghodsi毫不掩饰的真相</span>
          <span class="news-item-title-en">Databricks’ new AI agent tells CEO Ali Ghodsi the unvarnished truth</span>
          <span class="news-value-point">💡 在12,000名员工中， AI Ghodsi是第一个承认他不可能认识每个人的人，他们也不太可能向他坦白出错的事情</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌DeepMind的研究人员发布了一种新型人工智能模型，旨在揭示DNA的变化如何影响不同的细胞，为科学家们提供了一个更详细的视角，来观察一个众所周知的难题，该难题可能为各种疾病的病因提供重要线索。" data-title="Google’s AlphaGenome 2 zooms in on the cellular roots of disease" data-date="11-11 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-11 23:00</span>
          <span class="news-item-title">谷歌的AlphaGenome 2聚焦于疾病的细胞根源</span>
          <span class="news-item-title-en">Google’s AlphaGenome 2 zooms in on the cellular roots of disease</span>
          <span class="news-value-point">💡 谷歌DeepMind的研究人员发布了一种新型人工智能模型，旨在揭示DNA的变化如何影响不同的细胞，为科学家们提供了一个更详细的视角，来观察一个众…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/world/asia/china-us-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="美国怀疑英伟达的掌门人是中国间谍的目标，这凸显了两大强国之间深层次的不信任，即使两国领导人正努力稳定双边关系。" data-title="Behind the Trump-Xi Bonhomie, a Fierce Spy War Rages" data-date="11-11 22:57" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-11 22:57</span>
          <span class="news-item-title">在特朗普与习近平的友好关系背后，一场激烈的间谍战正在上演</span>
          <span class="news-item-title-en">Behind the Trump-Xi Bonhomie, a Fierce Spy War Rages</span>
          <span class="news-value-point">💡 美国怀疑英伟达的掌门人是中国间谍的目标，这凸显了两大强国之间深层次的不信任，即使两国领导人正努力稳定双边关系</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/technology/jensen-huang-affair-lori-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Lori Huang与英伟达首席执行官结婚已超过40年，她在科技巨头的配偶中显得与众不同，因为她一直非常低调。" data-title="Nvidia Scandal Puts Lori Huang, Jensen Huang’s Wife, In the Spotlight" data-date="11-11 22:46" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-11 22:46</span>
          <span class="news-item-title">英伟达丑闻将黄仁勋的妻子Lori Huang推上风口浪尖</span>
          <span class="news-item-title-en">Nvidia Scandal Puts Lori Huang, Jensen Huang’s Wife, In the Spotlight</span>
          <span class="news-value-point">💡 Lori Huang与英伟达首席执行官结婚已超过40年，她在科技巨头的配偶中显得与众不同，因为她一直非常低调</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/softbank-loses-usd3-7-billion-on-canceled-ai-data-center-gas-turbine-orders-days-after-denying-elon-musks-claim-it-was-defaulting-company-kills-reserved-13-gigawatts-of-power-more-than-six-hoover-dams-worth-of-capacity" target="_blank" rel="noopener" data-cat="keji" data-summary="软银可能没有在大量燃气轮机订单上违约，但在高估了在人工智能数据中心建设热潮中可以使用多少后，它已经退出了不需要的动力装置的交易。" data-title="Softbank loses $3.7 billion on canceled AI data center gas turbine orders days after denying Elon Musk’s claim it was defaulting" data-date="11-11 22:29" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 22:29</span>
          <span class="news-item-title">软银因取消人工智能数据中心燃气轮机订单损失37亿美元（ $ 3.7 billion ） ，此前几天，软银否认了埃隆·马斯克（ Elon Musk ）声称其违约</span>
          <span class="news-item-title-en">Softbank loses $3.7 billion on canceled AI data center gas turbine orders days after denying Elon Musk’s claim it was defaulting</span>
          <span class="news-value-point">💡 软银可能没有在大量燃气轮机订单上违约，但在高估了在人工智能数据中心建设热潮中可以使用多少后，它已经退出了不需要的动力装置的交易</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/" target="_blank" rel="noopener" data-cat="keji" data-summary="就像为驾驶汽车而训练的端到端模型一样，人工智能代理是在不可预测的环境中运行的概率系统。" data-title="Plurai wants to help AI agents work better using the same approach that helped get self-driving cars to roads" data-date="11-11 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-11 22:00</span>
          <span class="news-item-title">Plurai希望使用帮助自动驾驶汽车上路的相同方法，帮助人工智能代理更好地工作</span>
          <span class="news-item-title-en">Plurai wants to help AI agents work better using the same approach that helped get self-driving cars to roads</span>
          <span class="news-value-point">💡 就像为驾驶汽车而训练的端到端模型一样，人工智能代理是在不可预测的环境中运行的概率系统</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/nintendo/nintendo-unleashes-dmca-takedown-wave-against-open-source-switch-modchip-firmware-144-tools-disabled-picofly-sx-core-and-hwfly-among-casualties-following-criminal-trial-victory" target="_blank" rel="noopener" data-cat="keji" data-summary="任天堂正在追查任天堂Switch硬件改版芯片背后的开源固件" data-title="Nintendo unleashes DMCA takedown wave against open-source Switch modchip firmware, 144 tools disabled" data-date="11-11 21:42" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 21:42</span>
          <span class="news-item-title">任天堂发起针对开源Switch改版芯片固件的DMCA下架浪潮，144款工具被禁用</span>
          <span class="news-item-title-en">Nintendo unleashes DMCA takedown wave against open-source Switch modchip firmware, 144 tools disabled</span>
          <span class="news-value-point">💡 任天堂正在追查任天堂Switch硬件改版芯片背后的开源固件</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/cognichip-reveals-how-its-new-ai-assisted-program-can-slash-chip-design-times-from-months-to-days-automating-labor-intensive-tasks-cuts-design-time-down-chief-product-officer-explains" target="_blank" rel="noopener" data-cat="keji" data-summary="Cognichip声称，其人工智能可以将芯片设计时间从数月缩短至数天，但前提是设计必须非常简单。" data-title="Cognichip reveals how its new AI-assisted program can slash chip design times from months to days — automating labor-intensive tasks cuts design time down, Chief Product Officer explains" data-date="11-11 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 21:30</span>
          <span class="news-item-title">Cognichip揭示了其全新AI辅助程序如何将芯片设计时间从数月缩短至数天——首席产品官解释说，自动化劳动密集型任务可缩短设计时间。</span>
          <span class="news-item-title-en">Cognichip reveals how its new AI-assisted program can slash chip design times from months to days — automating labor-intensive tasks cuts design time down, Chief Product Officer explains</span>
          <span class="news-value-point">💡 Cognichip声称，其人工智能可以将芯片设计时间从数月缩短至数天，但前提是设计必须非常简单</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/congress-could-issue-subpoena-to-nvidia-ceo-jensen-huang-if-he-doesnt-respond-by-today-to-request-for-a-joint-closed-door-briefing-us-representatives-want-to-discuss-companys-security-protocols-against-foreign-adversary-espionage" target="_blank" rel="noopener" data-cat="keji" data-summary="三位委员会主席希望就Jensen Huang的公司“针对外国敌对势力间谍活动的安保协议”对其进行质询，因为一位前中情局特工表示，作为一家万亿美元公司的领导者，Jensen Huang被盯上了。" data-title="Congress could issue subpoena to Nvidia CEO Jensen Huang if he doesn’t respond by today to request for a ‘joint, closed" data-date="11-11 21:04" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 21:04</span>
          <span class="news-item-title">如果英伟达首席执行官黄仁勋未能在今天之前对“联合闭门”的请求作出回应，国会可能会向他发出传票。</span>
          <span class="news-item-title-en">Congress could issue subpoena to Nvidia CEO Jensen Huang if he doesn’t respond by today to request for a ‘joint, closed</span>
          <span class="news-value-point">💡 三位委员会主席希望就Jensen Huang的公司“针对外国敌对势力间谍活动的安保协议”对其进行质询，因为一位前中情局特工表示，作为一家万亿美元…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/linux/cyanogen-co-founder-unveils-kora-a-linux-os-that-splits-ai-models-across-the-cpu-gpu-and-npu-snapdragon-x2-elite-and-hexagon-npu-get-full-support-first" target="_blank" rel="noopener" data-cat="keji" data-summary="Kora 是一款内置 AI 模型和用于本地代理工作的代理的 Linux 桌面操作系统，将于 2027 年登陆 PC，包括搭载 Snapdragon X2 Elite 的设备。" data-title="Cyanogen co-founder unveils Kora, a Linux OS that splits AI models across the CPU, GPU, and NPU" data-date="11-11 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 21:00</span>
          <span class="news-item-title">Cyanogen联合创始人发布Kora，这是一款将AI模型分散到CPU、GPU和NPU的Linux操作系统</span>
          <span class="news-item-title-en">Cyanogen co-founder unveils Kora, a Linux OS that splits AI models across the CPU, GPU, and NPU</span>
          <span class="news-value-point">💡 Kora 是一款内置 AI 模型和用于本地代理工作的代理的 Linux 桌面操作系统，将于 2027 年登陆 PC，包括搭载 Snapdrago…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-11/10730432.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网首尔11月11日电(记者 金旭)韩国关税厅当地时间11日公布数据显示，11月1日至10日，韩国出口额为335亿美元(约合人民币2234.7亿元)，同比增长111.9%，创历年11月同期最高水平。" data-title="韩国半导体出口持续增长 全年出口额有望首次突破1万亿美元" data-date="11-11 20:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 20:28</span>
          <span class="news-item-title">韩国半导体出口持续增长 全年出口额有望首次突破1万亿美元</span>
          <span class="news-value-point">💡 中新网首尔11月11日电(记者 金旭)韩国关税厅当地时间11日公布数据显示，11月1日至10日，韩国出口额为335亿美元(约合人民币2234.7…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/business/nvidia-megaspeed-christian-lamarco.html" target="_blank" rel="noopener" data-cat="keji" data-summary="31岁的卖空者兼交易员克里斯蒂安·拉马科（Christian Lamarco）在5月份就曾警告过英伟达的财务和人事问题。" data-title="This Trader Raised Alarm About Nvidia’s China Entanglements Months Ago" data-date="11-11 18:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-11 18:03</span>
          <span class="news-item-title">这位交易员几个月前就对英伟达的中国纠葛提出了警告</span>
          <span class="news-item-title-en">This Trader Raised Alarm About Nvidia’s China Entanglements Months Ago</span>
          <span class="news-value-point">💡 31岁的卖空者兼交易员克里斯蒂安·拉马科（Christian Lamarco）在5月份就曾警告过英伟达的财务和人事问题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/watch/video/13611018/manchester-utd-latest-five-things-mauricio-pochettino-will-need-to-sort-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的尼克·赖特（Nick Wright）分析了毛里西奥·波切蒂诺（Mauricio Pochettino）如果并一旦接替迈克尔·卡里克（Michael Carrick）担任曼联主教练，将需要解决的五个问题。" data-title="FIVE things Pochettino will need to sort out at Man Utd" data-date="11-11 21:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 21:30</span>
          <span class="news-item-title">波切蒂诺在曼联需要解决的五个问题</span>
          <span class="news-item-title-en">FIVE things Pochettino will need to sort out at Man Utd</span>
          <span class="news-value-point">💡 天空体育的尼克·赖特（Nick Wright）分析了毛里西奥·波切蒂诺（Mauricio Pochettino）如果并一旦接替迈克尔·卡里克（M…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwzd9pvjy426o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球撰稿人菲尔·麦克纳尔蒂（Phil McNulty）表示，毛里西奥·波切蒂诺（Mauricio Pochettino）似乎即将把与曼联长达十年的“暧昧”关系发展为正式的“恋爱”关系。" data-title="Pochettino a decade in Man Utd&#39;s making - but Carrick deserves better" data-date="11-11 20:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-11 20:58</span>
          <span class="news-item-title">波切蒂诺在曼联的十年——但卡里克理应得到更好的待遇</span>
          <span class="news-item-title-en">Pochettino a decade in Man Utd's making - but Carrick deserves better</span>
          <span class="news-value-point">💡 首席足球撰稿人菲尔·麦克纳尔蒂（Phil McNulty）表示，毛里西奥·波切蒂诺（Mauricio Pochettino）似乎即将把与曼联长达…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611004/mauricio-pochettino-manchester-uniteds-approach-for-former-tottenham-and-chelsea-boss-questioned" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻的卡韦·索尔赫科尔对曼联追求毛里西奥·波切蒂诺的做法提出质疑，认为还有更好的选择。" data-title="Is Pochettino a short-term fix? Man Utd pursuit of Carrick replacement questioned" data-date="11-11 20:44" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 20:44</span>
          <span class="news-item-title">波切蒂诺是短期解决方案吗？曼联寻求卡里克替代者受到质疑</span>
          <span class="news-item-title-en">Is Pochettino a short-term fix? Man Utd pursuit of Carrick replacement questioned</span>
          <span class="news-value-point">💡 天空体育新闻的卡韦·索尔赫科尔对曼联追求毛里西奥·波切蒂诺的做法提出质疑，认为还有更好的选择</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13610871/sandpapergate-nasser-hussain-calls-australia-ball-tampering-scandal-a-complete-mess-after-usman-khawaja-claims" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的纳瑟·侯赛因（Nasser Hussain）将澳大利亚的“砂纸门”事件及其随后引发的轩然大波称为“一团糟”。" data-title="Hussain calls &#39;Sandpapergate&#39; affair a &#39;complete mess&#39;" data-date="11-11 20:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 20:15</span>
          <span class="news-item-title">侯赛因称“砂纸门”事件是一团糟</span>
          <span class="news-item-title-en">Hussain calls 'Sandpapergate' affair a 'complete mess'</span>
          <span class="news-value-point">💡 天空体育的纳瑟·侯赛因（Nasser Hussain）将澳大利亚的“砂纸门”事件及其随后引发的轩然大波称为“一团糟”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610949/mauricio-pochettino-man-utd-strike-agreement-with-michael-carricks-potential-successor" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）原则上达成协议，如果迈克尔·卡里克（Michael Carrick）被解雇，波切蒂诺将接任主教练一职。" data-title="Man Utd strike Pochettino agreement as Carrick takes training" data-date="11-11 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 20:00</span>
          <span class="news-item-title">曼联与波切蒂诺达成协议，卡里克接管球队训练</span>
          <span class="news-item-title-en">Man Utd strike Pochettino agreement as Carrick takes training</span>
          <span class="news-value-point">💡 曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）原则上达成协议，如果迈克尔·卡里克（Michael Carrick）被解雇，…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610949/mauricio-pochettino-man-utd-strike-agreement-with-michael-carricks-potential-successor" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）原则上达成协议，如果迈克尔·卡里克（Michael Carrick）被解雇，波切蒂诺将接任主教练一职。" data-title="Man Utd strike Pochettino agreement as Carrick takes training" data-date="11-11 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 20:00</span>
          <span class="news-item-title">曼联与波切蒂诺达成协议，卡里克接管球队训练</span>
          <span class="news-item-title-en">Man Utd strike Pochettino agreement as Carrick takes training</span>
          <span class="news-value-point">💡 曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）原则上达成协议，如果迈克尔·卡里克（Michael Carrick）被解雇，…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw30e0yz0p04o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="正在进行的国际比赛日让主教练恩佐·马雷斯卡有了亟需的时间来解决曼城队日益增多的问题。" data-title="Assessing the reasons for Man City&#39;s decline in form under Maresca" data-date="11-11 19:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-11 19:47</span>
          <span class="news-item-title">评估马雷斯卡执教下曼城状态下滑的原因</span>
          <span class="news-item-title-en">Assessing the reasons for Man City's decline in form under Maresca</span>
          <span class="news-value-point">💡 正在进行的国际比赛日让主教练恩佐·马雷斯卡有了亟需的时间来解决曼城队日益增多的问题</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Van Dijk &#39;not panicking&#39; over new deal" data-title="Liverpool latest: Van Dijk &#39;not panicking&#39; over new deal" data-date="11-11 18:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 18:40</span>
          <span class="news-item-title">利物浦最新消息：范迪克对新合同“并不慌张”</span>
          <span class="news-item-title-en">Liverpool latest: Van Dijk 'not panicking' over new deal</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqvg25pj36mvo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺已准备好接受曼联的邀约，成为球队的下一任主教练。" data-title="Pochettino ready to accept Man Utd offer to replace Carrick" data-date="11-11 18:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-11 18:34</span>
          <span class="news-item-title">波切蒂诺准备接受曼联的邀约，接替卡里克</span>
          <span class="news-item-title-en">Pochettino ready to accept Man Utd offer to replace Carrick</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺已准备好接受曼联的邀约，成为球队的下一任主教练</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610916/liverpool-incorrectly-denied-penalty-for-jurrien-timber-pull-on-alexander-isak-vs-arsenal-rules-independent-panel" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一个独立小组裁定，在阿森纳在安菲尔德球场获胜的比赛中，当尤里恩·廷伯拉扯亚历山大·伊萨克的球衣时，利物浦本应获得一个点球。" data-title="Liverpool incorrectly denied pen vs Arsenal says independent panel" data-date="11-11 18:33" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 18:33</span>
          <span class="news-item-title">独立小组称利物浦对阵阿森纳时被错误地判罚点球无效</span>
          <span class="news-item-title-en">Liverpool incorrectly denied pen vs Arsenal says independent panel</span>
          <span class="news-value-point">💡 一个独立小组裁定，在阿森纳在安菲尔德球场获胜的比赛中，当尤里恩·廷伯拉扯亚历山大·伊萨克的球衣时，利物浦本应获得一个点球</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6n8d8kl125vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛小组表示，尤里恩·廷伯（Jurrien Timber）拉拽亚历山大·伊萨克（Alexander Isak）的球衣，利物浦本应获得对阿森纳的点球。" data-title="Shirt pull on Isak should have been penalty" data-date="11-11 18:23" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-11 18:23</span>
          <span class="news-item-title">拉拽伊萨克的球衣应该判罚点球</span>
          <span class="news-item-title-en">Shirt pull on Isak should have been penalty</span>
          <span class="news-value-point">💡 英超联赛小组表示，尤里恩·廷伯（Jurrien Timber）拉拽亚历山大·伊萨克（Alexander Isak）的球衣，利物浦本应获得对阿森纳…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13594403/jordan-hadaway-interview-meet-the-25-year-old-llandudno-boss-the-youngest-top-flight-manager-in-europe" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着足球的发展，进入足球管理层的途径也随之演变。" data-title="Meet the youngest top-flight manager in Europe" data-date="11-11 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 18:00</span>
          <span class="news-item-title">认识欧洲最年轻的顶级联赛主教练</span>
          <span class="news-item-title-en">Meet the youngest top-flight manager in Europe</span>
          <span class="news-value-point">💡 随着足球的发展，进入足球管理层的途径也随之演变</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13576948/andoni-iraola-was-sacked-from-his-first-job-at-aek-larnaca-in-cyprus-liverpool-managers-difficult-career-start-explained" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="并非每个成功的职业生涯都能有一个漂亮的开端，但安多尼·伊拉奥拉通往利物浦的道路将充满坎坷。七年前，他在执教塞浦路斯甲级联赛球队拉纳卡AEK期间遭遇连败，从而失去了他的第一份教练工作。" data-title="From the sack in Cyprus to Liverpool: Iraola&#39;s first job explained" data-date="11-11 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 18:00</span>
          <span class="news-item-title">从在塞浦路斯被解雇到利物浦：伊拉奥拉的第一份工作解析</span>
          <span class="news-item-title-en">From the sack in Cyprus to Liverpool: Iraola's first job explained</span>
          <span class="news-value-point">💡 并非每个成功的职业生涯都能有一个漂亮的开端，但安多尼·伊拉奥拉通往利物浦的道路将充满坎坷</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610578/manchester-united-and-mauricio-pochettino-would-argentine-be-the-perfect-fit-or-just-another-manager-to-fall-foul-of-old-trafford-chaos" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺与曼联有着悠久的历史渊源。他们的轨迹可能早在很久以前就曾多次交汇，但不知为何，始终未能真正走到一起。" data-title="Man Utd&#39;s Pochettino pursuit comes full circle" data-date="11-11 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 17:00</span>
          <span class="news-item-title">曼联对波切蒂诺的追求终于尘埃落定</span>
          <span class="news-item-title-en">Man Utd's Pochettino pursuit comes full circle</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺与曼联有着悠久的历史渊源</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/11/is-no-10-still-the-best-or-no-41-the-myths-and-maths-of-premier-league-shirt-numbers" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="虽然9号球员仍然进球最多， 1号球员试图阻止他们，但自20世纪90年代初引入球队号码以来，趋势已经发生了变化。球衣号码值多少钱？如果您想在阿森纳2026-赛季后面添加两个数字，则需要花费£ 8" data-title="Is No 10 still the best, or No 41? The myths and maths of Premier League shirt numbers" data-date="11-11 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-11 16:00</span>
          <span class="news-item-title">10号仍然是最好的，还是41号？英超球衣号码的神话和数学</span>
          <span class="news-item-title-en">Is No 10 still the best, or No 41? The myths and maths of Premier League shirt numbers</span>
          <span class="news-value-point">💡 虽然9号球员仍然进球最多， 1号球员试图阻止他们，但自20世纪90年代初引入球队号码以来，趋势已经发生了变化</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1031301/sharge-140w-gan-charger-lenovo-yoga-mini-desktop-pc-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="正在寻找一款既时尚又实用的MacBook和设备充电器吗？亚马逊和 Sharge 都在销售 Pixel 140W GaN 充电器，售价分别为 69.88 美元和 69.90 美元，比原价优惠 24 美元。如果您不需要那么大的功率" data-title="Sharge’s eye-catching MacBook charger is over 25 percent off" data-date="11-11 23:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-11 23:30</span>
          <span class="news-item-title">Sharge的这款引人注目的MacBook充电器现享七五折优惠</span>
          <span class="news-item-title-en">Sharge’s eye-catching MacBook charger is over 25 percent off</span>
          <span class="news-value-point">💡 正在寻找一款既时尚又实用的MacBook和设备充电器吗</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/822.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 11 日消息，谷歌 DeepMind 发布新一代 DNA 序列模型 AlphaGenome 2，可预测 DNA 序列及其变异对特定人体细胞类型的影响，为科研人员挖掘疾病的细胞驱动因素提供全新工具。人体每个细胞携带相同的 DNA 蓝图，但不同细胞类型会通过开关不同基因完成特定功能。全球的人类细胞图谱项目已对数百万细胞的基因表达进行绘制，但预测细微 DNA 变异如何影响细胞基因表达，仍是尚未解决的难题。此前谷歌已推出初代 AlphaGenome，可预测 DNA 变异对宽泛组织的分子活性影响，并推出了覆盖人类基因组全部 90 亿种单字母变异预测的 AlphaGenome Atlas，助力罕见病、复杂性状与基础生物学研究。AlphaGenome 2 从宽泛组织平均水平缩小至单个细" data-title="谷歌 DeepMind 发布 AlphaGenome 2 基因序列模型：识别致病变异能力提升近一倍" data-date="11-11 23:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 23:19</span>
          <span class="news-item-title">谷歌 DeepMind 发布 AlphaGenome 2 基因序列模型：识别致病变异能力提升近一倍</span>
          <span class="news-value-point">💡 IT之家 11 月 11 日消息，谷歌 DeepMind 发布新一代 DNA 序列模型 AlphaGenome 2，可预测 DNA 序列及其变异…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/820.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 11 日消息，据彭博社今天（11 日）晚间报道，保时捷 CEO 骆明楷（Michael Leiters）批评特斯拉 Roadster 发布会过于追求噱头，并指出特斯拉展示的飞行汽车与保时捷 Mission S 概念车面向不同的消费群体。骆明楷在柏林出席一场会议时直言：“我们不想搞任何特效或表演。”同时，他强调，保时捷希望通过新车展示真正的技术创新。特斯拉与保时捷都在当地时间 10 月 15 日（IT之家注：北京时间均为 16 日上午）发布新车，但两场活动的风格截然不同。特斯拉主打炫目的展示效果，配备压缩空气推进器的 Roadster 从斜坡腾空跃起，在空中翻转后稳稳落地。骆明楷称，全新的中置发动机超跑 Mission S 发布以来获得了客户“极其热烈”的反响。作为保时捷进" data-title="保时捷 CEO 骆明楷批评特斯拉 Roadster 发布会：我们不想搞任何特效或表演" data-date="11-11 23:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 23:01</span>
          <span class="news-item-title">保时捷 CEO 骆明楷批评特斯拉 Roadster 发布会：我们不想搞任何特效或表演</span>
          <span class="news-value-point">💡 IT之家 11 月 11 日消息，据彭博社今天（11 日）晚间报道，保时捷 CEO 骆明楷（Michael Leiters）批评特斯拉 Road…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1031321/the-legend-of-zelda-ocarina-of-time-notes-app-gold-skulltula" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我从来都不喜欢在《塞尔达传说：时之笛》中寻找金色骷髅蛛。这款游戏中藏有100个金魂蛛，它们散布在海拉鲁的各个角落。即使我在成长过程中花了许多时间玩这款N64经典游戏，我也不记得自己是否真的找到过所有金魂蛛，或者" data-title="Ocarina of Time is even better if you use a smartphone app" data-date="11-11 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-11 23:00</span>
          <span class="news-item-title">如果使用智能手机应用程序，《时之笛》的体验会更好</span>
          <span class="news-item-title-en">Ocarina of Time is even better if you use a smartphone app</span>
          <span class="news-value-point">💡 我从来都不喜欢在《塞尔达传说：时之笛》中寻找金色骷髅蛛</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/819.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡萨帝 · 揽光 GLD 热泵洗烘一体机 10kg，型号 CE AB10LWUGLDU1。日常售价 10498 元，今日叠加 PLUS 立减 + 15% 国补后仅需 6104.2 元：领 8.5 折洗衣机券：点此查看售价下方可选“家电组合购”任选 1 件家电一起加购下单下单时选择“以旧换新 → 个护健康 → 普通牙刷（无需回收）”洗衣机实付 5900 元，今日下单官方返 300 元红包。参与家电家居多买多返（售价下方可见活动标签），再返 100 元 E 卡。折合仅需 5500 元：京东卡萨帝 揽光 热泵洗烘一体机 10kg 组合购 5900 元直达链接京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。关于尺寸官方简介京东卡萨帝 揽光 热泵洗烘一体机 1" data-title="553mm 超薄机身：卡萨帝热泵洗烘一体机 10498 → 5500 元破冰新低" data-date="11-11 22:55" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 22:55</span>
          <span class="news-item-title">553mm 超薄机身：卡萨帝热泵洗烘一体机 10498 → 5500 元破冰新低</span>
          <span class="news-value-point">💡 卡萨帝 · 揽光 GLD 热泵洗烘一体机 10kg，型号 CE AB10LWUGLDU1</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/818.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【京东活动可能随时变更，需以实付款为准】小米 · 米家智能净烟机 3 Pro 开售于 2026 年 8 月，官方定价 3999 元。京东 11.11 大促期间，按下方步骤下单，叠加 PLUS 立减 + 15% 国补后仅需 2291 元：领 8.7 折券：点此查看。下单时选择“以旧换新 → 个护健康 → 普通牙刷（无需回收）”补贴 200 元。参与“多买多返”活动返 30 元 E 卡，晒单返 50 元京豆，社交平台种草返 50 元京豆（详询客服）京东小米 米家智能净烟机 3 ProMJ06A 以旧换新后 2291 元直达链接京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。米家智能净烟机 3 Pro 主打三重净烟专利，可净吸油烟气味、PM2.5，包含防逸" data-title="以旧换新 3999 → 2291 元：小米米家智能净烟机 3 Pro 国补直降，7 级大风力" data-date="11-11 22:49" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 22:49</span>
          <span class="news-item-title">以旧换新 3999 → 2291 元：小米米家智能净烟机 3 Pro 国补直降，7 级大风力</span>
          <span class="news-value-point">💡 【京东活动可能随时变更，需以实付款为准】小米 · 米家智能净烟机 3 Pro 开售于 2026 年 8 月，官方定价 3999 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/816.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="12kg 洗 + 8kg 烘海信 · 大薄荷 E3S 热泵洗烘一体机灰白双色可选，日常大促价 6199 元。今日 11.11 下单仅需 3668 元，11 月 11 日下单返 400 元 E 卡，折合仅需 3268 元。京东家电“多买多返”返 30 元 E 卡（售价下方可见活动标签），折合仅需 3238 元官方好价：下单时需选择“以旧换新” → 家庭小电 → 普通餐具：京东海信 热泵洗烘一体机大薄荷 2.0 E3S 灰白两色可选以旧换新 3668 元领 9 折券13kg 洗涤 + 9kg 烘海信 E8Q 热泵洗烘一体机灰白双色可选，日常大促价 7999 元。今日 11.11 下单仅需 4302 元，11 月 11 日下单返 300 元 E 卡，折合仅需 4002 元。京东家电“多买多返”返" data-title="热泵洗烘一体机破冰新低：海信 12kg 洗 +8kg 烘 6199 → 3238 元限 1 小时" data-date="11-11 22:46" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 22:46</span>
          <span class="news-item-title">热泵洗烘一体机破冰新低：海信 12kg 洗 +8kg 烘 6199 → 3238 元限 1 小时</span>
          <span class="news-value-point">💡 12kg 洗 + 8kg 烘海信 · 大薄荷 E3S 热泵洗烘一体机灰白双色可选，日常大促价 6199 元</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13611064/harry-kane-applauded-by-journalists-as-he-enters-england-press-conference" target="_blank" rel="noopener" data-cat="zonghe" data-summary="英格兰队长哈里·凯恩（Harry Kane）在周三的新闻发布会上亮相，为对阵克罗地亚的欧国联比赛做准备。他因荣膺金球奖而受到媒体的赞誉。" data-title="Kane applauded by journalists as he enters England press conference" data-date="11-11 22:41" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 22:41</span>
          <span class="news-item-title">凯恩在进入英格兰队新闻发布会时受到记者鼓掌欢迎</span>
          <span class="news-item-title-en">Kane applauded by journalists as he enters England press conference</span>
          <span class="news-value-point">💡 英格兰队长哈里·凯恩（Harry Kane）在周三的新闻发布会上亮相，为对阵克罗地亚的欧国联比赛做准备</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/815.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 11 日消息，每年举办的 Adobe MAX 大会上，Adobe 展示的最令人印象深刻的技术之一，往往是那些仍处于实验阶段、尚未正式推出的创新功能。今天，该公司公布了最新一批实验项目：它们能够将普通图片转换为可探索的 3D 场景，通过与 AI 角色对话来设计角色形象，还能让照片编辑变成简单的复制粘贴操作。首先是非常奇特的 Project Screen Test 项目，其旨在让用户更轻松地创建 AI 生成角色，并将其应用于视频内容。IT之家注意到，与传统方式不同，用户不再只是通过文字提示词描述角色应该如何说话、如何表现，而是可以直接与角色对话，在类似演员试镜的环境中对其进行指导。使用时，用户首先需要描述角色的一些基本性格特征，例如“焦虑、害羞、笨拙”等，并为角色设置声音。声" data-title="Adobe 公布四项 AI 实验项目：照片秒变 3D 场景，还能通过聊天设计 AI 角色" data-date="11-11 22:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-11 22:32</span>
          <span class="news-item-title">Adobe 公布四项 AI 实验项目：照片秒变 3D 场景，还能通过聊天设计 AI 角色</span>
          <span class="news-value-point">💡 IT之家 11 月 11 日消息，每年举办的 Adobe MAX 大会上，Adobe 展示的最令人印象深刻的技术之一，往往是那些仍处于实验阶段、…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/asrock-attempts-to-correct-botched-radeon-rx-7000-firmware-release-with-new-version-revised-release-should-work-ok-but-company-provides-no-explanation-for-bricked-cards" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在有报道称 Radeon RX 7900 XT 和 XTX 显卡在安装上一版固件后无法启动之后，华擎推出了 VBIOS 1.0.6 更新。" data-title="ASRock quietly rolls out new firmware after disastrous previous update killed Radeon RX 7900" data-date="11-11 22:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 22:20</span>
          <span class="news-item-title">在灾难性的先前更新杀死了Radeon RX 7900之后， ASRock悄然推出了新固件</span>
          <span class="news-item-title-en">ASRock quietly rolls out new firmware after disastrous previous update killed Radeon RX 7900</span>
          <span class="news-value-point">💡 在有报道称 Radeon RX 7900 XT 和 XTX 显卡在安装上一版固件后无法启动之后，华擎推出了 VBIOS 1.0.6 更新</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/pc-cases/montech-king-95-3d-pro-case-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新款 Montech King 95 3D 机箱提供 3 面全景内部视图，内部空间宽敞，可容纳各种组件和散热装置，Pro 版本配备七个 RGB 风扇。" data-title="Montech King 95 3D Pro case review: The King has returned" data-date="11-11 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-11 22:00</span>
          <span class="news-item-title">Montech King 95 3D Pro case review: The King has returned</span>
          <span class="news-value-point">💡 新款 Montech King 95 3D 机箱提供 3 面全景内部视图，内部空间宽敞，可容纳各种组件和散热装置，Pro 版本配备七个 RGB …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1031291/sony-playstation-pulse-wireless-gaming-headset-hands-on" target="_blank" rel="noopener" data-cat="zonghe" data-summary="人们很容易被一款功能齐全的无线游戏耳机吸引，它具备降噪功能、出色的音质、多平台连接、可更换电池等各种特性。但如果您只是希望基本功能做得好，那么索尼新款 99.99 美元的 PlaySta" data-title="Sony’s latest Pulse wireless headset packs planar magnetic drivers at a good price" data-date="11-11 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-11 22:00</span>
          <span class="news-item-title">索尼最新款Pulse无线耳机配备平面磁性驱动单元，价格实惠</span>
          <span class="news-item-title-en">Sony’s latest Pulse wireless headset packs planar magnetic drivers at a good price</span>
          <span class="news-value-point">💡 人们很容易被一款功能齐全的无线游戏耳机吸引，它具备降噪功能、出色的音质、多平台连接、可更换电池等各种特性</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1031505/adobe-max-2026-sneaks-experiments-ai" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Adobe每年在其年度Max大会上展示的一些最令人印象深刻的技术是其正在开发的实验性功能，而其中最新的工具将于今天发布：它们可以将图像转换为可探索的3D场景，" data-title="Adobe’s AI experiments let you walk around in photos and interview your characters" data-date="11-11 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-11 22:00</span>
          <span class="news-item-title">Adobe 的人工智能实验让您可以在照片中走动，并采访照片中的人物</span>
          <span class="news-item-title-en">Adobe’s AI experiments let you walk around in photos and interview your characters</span>
          <span class="news-value-point">💡 Adobe每年在其年度Max大会上展示的一些最令人印象深刻的技术是其正在开发的实验性功能，而其中最新的工具将于今天发布：它们可以将图像转换为可探…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-11/10730545.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原11月11日电 (刘小红 杨静)11日，在中共山西省委宣传部、山西省人民政府新闻办公室举行的“开局起步‘十五五’”系列主题新闻发布会上，针对山西老龄工作相关问题，山西省民政厅党组书记、厅长李建红表示，目前山西省老年人口突破800万，“十五五”时期是当地积极应对人口老龄化的重要窗口期。" data-title="山西老年人口突破800万  围绕五大重点谋划“十五五”老龄工作布局" data-date="11-11 21:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 21:57</span>
          <span class="news-item-title">山西老年人口突破800万  围绕五大重点谋划“十五五”老龄工作布局</span>
          <span class="news-value-point">💡 中新网太原11月11日电 (刘小红 杨静)11日，在中共山西省委宣传部、山西省人民政府新闻办公室举行的“开局起步‘十五五’”系列主题新闻发布会上…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-11/10730543.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原11月11日电 (刘小红 杨静)11日，在中共山西省委宣传部、山西省人民政府新闻办公室举行的“开局起步‘十五五’”系列主题新闻发布会上，山西省民政厅党组书记、厅长李建红介绍了全省民政事业发展情况。“十四五”期间，山西持续推进普惠性、基础性、兜底性民生建设，低保、特困、孤儿、残疾人等保障标准稳步提高，惠及困难民众184万人。发布会同步解读《山西省“十五五”民政事业发展规划》，明确五个重点发力方向，统筹推进养老服务、社会救助、特殊群体福利、社会事务、社会治理各项民政工作。" data-title="山西民政收官“十四五”惠及184万民众  五大方向布局“十五五”民生工作" data-date="11-11 21:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-11 21:57</span>
          <span class="news-item-title">山西民政收官“十四五”惠及184万民众  五大方向布局“十五五”民生工作</span>
          <span class="news-value-point">💡 中新网太原11月11日电 (刘小红 杨静)11日，在中共山西省委宣传部、山西省人民政府新闻办公室举行的“开局起步‘十五五’”系列主题新闻发布会上…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-11 23:30（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
