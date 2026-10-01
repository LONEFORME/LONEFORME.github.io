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
      <span>2026-10-01 15:54 抓取更新</span>
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
        <span class="channel-count">55</span>
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
        <span class="channel-count">10</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-01/10706707.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月1日电 综合美联社、英国广播公司报道，美国田纳西州官员当地时间9月30日未能通过注射致命药物的方式执行死囚克丽丝塔·盖尔·派克的死刑。" data-title="美国一死刑犯两剂致命注射后仍存活，行刑失败送医" data-date="10-01 15:01" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-01 15:01</span>
      </div>
      <h2 class="hero-featured-title">美国一死刑犯两剂致命注射后仍存活，行刑失败送医</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/086.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 1 日消息，特朗普昨日签署行政令将“Super Intelligence”定义为原有法律中“Artificial Intelligence”所涵盖的技术和系统，用“SI”取代原先“AI”的定义及相关立法。详情可见IT之家昨日报道。当地时间 9 月 30 日，美国加利福尼亚州州长加文 · 纽森签署第 N-10-26 号行政令，要求所有受其管辖的州政府机构和部门，在官方事务中继续使用“人工智能”及其缩写“AI”指代相关技术，不受联邦政府采用其他称谓的影响。特朗普要求，在法律允许的最大范围内，美国联邦行政部门在官方通信、公共传播、网站、报告、政策文件等非法律文件中，以“超级智能”和“SI”取代“人工智能”和“AI”。纽森签署的行政令则明确规定，不管美国联邦政府采用何种术语，加州" data-title="一字不改：加州州长纽森反击特朗普将“人工智能”改为“超级智能”，州政府范围内继续叫“AI”" data-date="10-01 15:50" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">一字不改：加州州长纽森反击特朗普将“人工智能”改为“超级智能”，州政府范围内继续叫“AI”</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/news/audio/2026/oct/01/billionaire-sheiks-and-sham-contracts-the-manchester-city-scandal-podcast" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="乔纳森·刘（ Jonathan Liew ）解释了对曼城的指控，西蒙·哈滕斯通（ Simon Hattenstone ）解释了作为《卫报》的特写作家西蒙·哈滕斯通（ Simon Hattenstone ）作为曼城球迷50多年的感受。当他开始与父亲在家乡参加比赛时，他还很年轻，从童年时期几乎要死的疾病中恢复过来。很长一段时间，这是一段建立在偶尔的高潮和" data-title="亿万富翁酋长和“虚假”合同：曼城丑闻" data-date="10-01 10:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">亿万富翁酋长和“虚假”合同：曼城丑闻</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.com/zhongwen/articles/cxyvzvqp0z01o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这次加费是高市政府收紧移民政策的一环，目的是管理快速增长的外国人口。" data-title="日本收紧外国人居留条件，申请费用上调二十倍" data-date="10-01 15:38" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">日本收紧外国人居留条件，申请费用上调二十倍</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706707.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月1日电 综合美联社、英国广播公司报道，美国田纳西州官员当地时间9月30日未能通过注射致命药物的方式执行死囚克丽丝塔·盖尔·派克的死刑。" data-title="美国一死刑犯两剂致命注射后仍存活，行刑失败送医" data-date="10-01 15:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 15:01</span>
          <span class="news-item-title">美国一死刑犯两剂致命注射后仍存活，行刑失败送医</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706685.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月1日电 (记者 孙自法)刚刚过去的9月，2026年全国科普月为公众献上持续一个月的科普“盛宴”。作为全国科普月主场之一，中国科技馆推出一系列丰富多彩活动，融前沿科技、学风建设与人文关怀于一体，以“科学+艺术+联动+交流”的多元模式，带来可看、可感、可参与的沉浸式科普体验。" data-title="2026年全国科普月：中国科技馆主场多元模式打造沉浸式科普体验" data-date="10-01 14:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:09</span>
          <span class="news-item-title">2026年全国科普月：中国科技馆主场多元模式打造沉浸式科普体验</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706677.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="香港高等法院原讼法庭暂委法官周昭雯，于9月30日颁布裁决理由，就何超琼起诉陈芃余骚扰、恐吓民事诉讼一案，对陈芃余批出永久禁制令。" data-title="何超琼称遭骚扰恐吓，获批永久禁制令" data-date="10-01 13:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:51</span>
          <span class="news-item-title">何超琼称遭骚扰恐吓，获批永久禁制令</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706642.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿10月1日电(记者 陈孟统)美国国防部长赫格塞思9月30日宣布组建“自主作战司令部”，以提升美军规模化自主及机器人作战能力。" data-title="美防长宣布组建“自主作战司令部”" data-date="10-01 13:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:33</span>
          <span class="news-item-title">美防长宣布组建“自主作战司令部”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706640.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿9月30日电(记者 陈孟统)美国五角大楼发言人肖恩·帕内尔9月30日发表声明称，由美国主导的打击极端组织“伊斯兰国”国际联盟部队当天正式结束在伊拉克的任务。" data-title="美国宣布正式结束国际联盟部队在伊拉克军事任务" data-date="10-01 13:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:33</span>
          <span class="news-item-title">美国宣布正式结束国际联盟部队在伊拉克军事任务</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706639.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月1日电 综合消息：阿联酋迪拜航空公司当地时间9月30日发表声明，称在当日该公司一航班发生驾驶舱冲突事件后，决定暂停往返以色列的航班，等待有关方面对事件展开调查。" data-title="迪拜航空因驾驶舱冲突事件暂停往返以色列航班" data-date="10-01 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:32</span>
          <span class="news-item-title">迪拜航空因驾驶舱冲突事件暂停往返以色列航班</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706675.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿10月1日电 (记者 陈孟统)中国驻美大使谢锋9月30日在华盛顿表示，中美双方要加快把新定位的愿景转化为行动，朝着合作为主、竞争有度、分歧可控、和平可期的方向努力，跨越“修昔底德陷阱”，走出中美正确相处之道。" data-title="中国驻美大使谢锋：中美合作是双行道，永远在进行时" data-date="10-01 13:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:30</span>
          <span class="news-item-title">中国驻美大使谢锋：中美合作是双行道，永远在进行时</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706659.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月1日电 (记者 孙自法)记者10月1日从中国科学院理化技术研究所(理化所)获悉，该所低温科学与技术全国重点实验室最近首次提出以交流电替代传统直流电驱动直接电解海水制氢策略，实现海上发电就地制氢，从根源上破解了海水电解制氢的沉淀瓶颈难题。" data-title="实现海上发电就地制氢 中国团队首提交流电直接电解海水制氢新策略" data-date="10-01 13:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:17</span>
          <span class="news-item-title">实现海上发电就地制氢 中国团队首提交流电直接电解海水制氢新策略</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706633.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月1日电 据美国阿克西奥斯新闻网站9月30日报道，一名美国官员和另一位知情人士透露，在美伊双方谈判陷入僵局后，美国务卿鲁比奥9月28日曾要求伊朗外长阿拉格齐率领的代表团立即离开美国。" data-title="美媒：鲁比奥要求伊朗代表团立即离开美国" data-date="10-01 11:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 11:59</span>
          <span class="news-item-title">美媒：鲁比奥要求伊朗代表团立即离开美国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706614.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网开罗10月1日电 题：记者手记：从会场到街巷 在开罗感受中阿文明交流互鉴" data-title="记者手记：从会场到街巷 在开罗感受中阿文明交流互鉴" data-date="10-01 11:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 11:46</span>
          <span class="news-item-title">记者手记：从会场到街巷 在开罗感受中阿文明交流互鉴</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-01/10706629.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月1日电 综合英国广播公司、美国《华尔街日报》当地时间9月30日报道，英国首相安迪·伯纳姆表示，英国政府认为伊朗“参与了英国空军费尔福德基地发生的事情”。" data-title="英首相称有充分迹象表明伊朗参与英空军基地事件 伊方回应" data-date="10-01 11:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 11:15</span>
          <span class="news-item-title">英首相称有充分迹象表明伊朗参与英空军基地事件 伊方回应</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706621.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社哈尔滨10月1日电 10月1日0时起，中俄界江黑龙江、乌苏里江开启为期20天的秋季禁渔期，重点守护大马哈鱼跨境洄游繁殖。两条界江全年禁渔各55天，分为伏季、秋季两个阶段落实。" data-title="中俄两大界江进入20天秋季禁渔期 700余艘渔船撤离作业水域" data-date="10-01 11:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 11:09</span>
          <span class="news-item-title">中俄两大界江进入20天秋季禁渔期 700余艘渔船撤离作业水域</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706590.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月1日出版的《求是》杂志发表中共中央总书记、国家主席、中央军委主席习近平的重要文章《加强普惠性、基础性、兜底性民生建设》。这是习近平总书记2012年11月至2026年1月期间有关重要论述的节录。" data-title="习言道｜让老百姓过上更好的日子" data-date="10-01 08:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 08:47</span>
          <span class="news-item-title">习言道｜让老百姓过上更好的日子</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706593.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“77”的回答" data-title="庆祝祖国77周年华诞：“77”的回答" data-date="10-01 08:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 08:37</span>
          <span class="news-item-title">庆祝祖国77周年华诞：“77”的回答</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/30/us/hegseth-troops-address.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="In his “State of the Force” address, Defense Secretary Pete Hegseth focused on the culture war and accused reporters of “treason” over Iran war coverage." data-title="In Speech, Hegseth Targets Diversity, Transgender People, Reporters and Iran" data-date="10-01 07:25" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-01 07:25</span>
          <span class="news-item-title">In Speech, Hegseth Targets Diversity, Transgender People, Reporters and Iran</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/086.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 1 日消息，特朗普昨日签署行政令将“Super Intelligence”定义为原有法律中“Artificial Intelligence”所涵盖的技术和系统，用“SI”取代原先“AI”的定义及相关立法。详情可见IT之家昨日报道。当地时间 9 月 30 日，美国加利福尼亚州州长加文 · 纽森签署第 N-10-26 号行政令，要求所有受其管辖的州政府机构和部门，在官方事务中继续使用“人工智能”及其缩写“AI”指代相关技术，不受联邦政府采用其他称谓的影响。特朗普要求，在法律允许的最大范围内，美国联邦行政部门在官方通信、公共传播、网站、报告、政策文件等非法律文件中，以“超级智能”和“SI”取代“人工智能”和“AI”。纽森签署的行政令则明确规定，不管美国联邦政府采用何种术语，加州" data-title="一字不改：加州州长纽森反击特朗普将“人工智能”改为“超级智能”，州政府范围内继续叫“AI”" data-date="10-01 15:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 15:50</span>
          <span class="news-item-title">一字不改：加州州长纽森反击特朗普将“人工智能”改为“超级智能”，州政府范围内继续叫“AI”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/085.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 1 日消息，软银集团今日表示，公司已通过软银愿景基金 2 完成对 OpenAI 的第三笔投资，金额为 100 亿美元（IT之家注：现汇率约合 671.69 亿元人民币），这是软银对 OpenAI 的最后一笔投资。至此，软银此前承诺的 300 亿美元（现汇率约合 2,015.06 亿元人民币）投资全部到位。OpenAI 的估值正处于快速上升阶段。据彭博社报道，该人工智能实验室在寻求新一轮融资，至少 300 亿美元。软银完成此次投资后，预计将持有 OpenAI 约 13% 股份。此次投资的资金源于软银债券，路透社表示，这笔债券是全球迄今为止规模最大的企业高收益债券发行。对软银而言，这些资金既是机遇也是风险：一方面它为软银继续推进 AI 战略提供充足资金；另一方面也让公司更加依" data-title="软银完成对 OpenAI 最后一笔投资，300 亿美元承诺全部到位" data-date="10-01 15:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 15:43</span>
          <span class="news-item-title">软银完成对 OpenAI 最后一笔投资，300 亿美元承诺全部到位</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/083.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 1 日消息，日本计算机娱乐供应商协会（CESA）于本月上旬发布了一份有关游戏行业开发现状的初步调研摘要，完整报告将于 12 月正式对外公布。其中一组格外值得关注的数据显示：85.8% 的日本游戏开发者已经在日常工作当中积极使用生成式人工智能。据IT之家了解，该调研的数据采集自日本游戏开发者大会 CEDEC 开展的开发者问卷调查。作为对比，去年的数据仅有 51% 的开发者正在使用该项技术。开发者的使用场景既包含美术素材生成，也包括借助 ChatGPT、Copilot 这类工具处理一般性行政事务。在已经使用生成式 AI 的受访者当中，63% 表示自己每天都会使用；22.8% 只是偶尔使用。另有 8.6% 的受访者提到，所在企业已经出台针对这项技术的使用指引。本次调研一共回收了" data-title="调研显示：超 85% 的日本游戏开发者正使用生成式 AI" data-date="10-01 15:37" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 15:37</span>
          <span class="news-item-title">调研显示：超 85% 的日本游戏开发者正使用生成式 AI</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-01/10706680.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京10月1日电 (记者 孙自法)刚刚过去的2026年全国科普月期间，在国家科技传播中心举办的人工智能(AI)时代科普变革系列主题活动颇受关注。聚焦科普方法创新、AI技术冲击与场景变革，科普界、教育界及产业界多位专家学者代表，应邀共同探寻智能时代科普转型方向。" data-title="聚焦AI时代科普变革 2026年全国科普月系列主题活动共探科普转型" data-date="10-01 14:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:01</span>
          <span class="news-item-title">聚焦AI时代科普变革 2026年全国科普月系列主题活动共探科普转型</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1003068/elon-musk-grokipedia-v-0-3-spacexai" target="_blank" rel="noopener" data-cat="keji" data-summary="SpaceXAI的人工智能驱动的维基百科竞争对手Grokipedia最近再次开始合并编辑，今天，作为v0.3更新的一部分，它进行了一些设计调整，包括新徽标以及对其主页和实时编辑页面的刷新。SpaceXAI设计主管本吉·泰勒（ Benji Taylor ）称其为“新刷新的Grokipedia。“ Grokipedia的旧主页差不多[…]" data-title="伊隆·马斯克（ Elon Musk ）的《格罗基百科全书》（ Grokipedia ）采用“" data-date="10-01 08:23" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-01 08:23</span>
          <span class="news-item-title">伊隆·马斯克（ Elon Musk ）的《格罗基百科全书》（ Grokipedia ）采用“</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌发布了最新的双子座模型，将其作为编码和网络安全工作的主力进行营销。" data-title="谷歌发布Gemini 4 Argon ，被称为迄今为止最强大的型号" data-date="10-01 07:43" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-01 07:43</span>
          <span class="news-item-title">谷歌发布Gemini 4 Argon ，被称为迄今为止最强大的型号</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/30/valor-atreides-and-sequoia-back-ai-startup-flow-engineering-at-750m-valuation/" target="_blank" rel="noopener" data-cat="keji" data-summary="Flow Engineering将人工智能代理引入硬件设计，也让Roelof Botha成为天使投资人和董事会成员。" data-title="Valor、Atreides和Sequoia以7.5亿美元的估值支持人工智能初创公司Flow Engineering" data-date="10-01 05:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-01 05:07</span>
          <span class="news-item-title">Valor、Atreides和Sequoia以7.5亿美元的估值支持人工智能初创公司Flow Engineering</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1002980/google-gemini-4-argon" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌今天公布了它的下一个人工智能前沿模型，它被称为Gemini 4 Argon。根据首席人工智能架构师兼谷歌DeepMind高级副总裁Koray Kavukcuoglu的说法，新模型在现实世界的软件工程、法律和金融等企业知识工作以及网络安全防御等复杂工作流程中提供了“前沿性能”。但该公司正在限制[…]的访问权限" data-title="谷歌宣布推出Gemini 4 ，并表示它非常强大，目前只有“值得信赖的网络防御者”才能拥有它" data-date="10-01 04:41" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-01 04:41</span>
          <span class="news-item-title">谷歌宣布推出Gemini 4 ，并表示它非常强大，目前只有“值得信赖的网络防御者”才能拥有它</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/30/openais-jev-clone-could-help-the-frontier-lab-stop-its-swarming-agents/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI的“Decisions API”是一个JEV克隆，它证实了快速、廉价智能的重要性。" data-title="OpenAI的JEV克隆可以帮助前沿实验室阻止其集群特工" data-date="10-01 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-01 03:00</span>
          <span class="news-item-title">OpenAI的JEV克隆可以帮助前沿实验室阻止其集群特工</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/30/ai-voice-startup-elevenlabs-doubles-valuation-to-22b/" target="_blank" rel="noopener" data-cat="keji" data-summary="3亿美元的员工招标由惠灵顿和T. Rowe Price共同牵头。" data-title="人工智能语音初创公司ElevenLabs的估值翻番至220亿美元（ $ 220亿）" data-date="10-01 02:23" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-01 02:23</span>
          <span class="news-item-title">人工智能语音初创公司ElevenLabs的估值翻番至220亿美元（ $ 220亿）</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1002779/openai-dots-meta-muse-ai-agents-hardware-devices" target="_blank" rel="noopener" data-cat="keji" data-summary="虽然人工智能在人们的手机和电脑上取得了很大的进步，但在专用设备上基本上失败了。但在接下来的一年里，两家主要的人工智能公司Meta和OpenAI将试图改变这种状况。他们显然也在押注类似的道路：用他们可爱的软件代理测试对物理硬件的需求。“硬件是[…]" data-title="AI Tamagotchis即将到来" data-date="10-01 02:07" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-01 02:07</span>
          <span class="news-item-title">AI Tamagotchis即将到来</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/geekbench-7-results-suggest-openais-dots-agent-runs-on-nine-core-amd-epyc-vms-with-nearly-10gb-of-memory-newest-runs-score-about-six-times-meta-muse-in-multi-core" target="_blank" rel="noopener" data-cat="keji" data-summary="发布后的Geekbench 7运行显示Debian Linux而不是泄漏的Ubuntu。" data-title="Geekbench 7的结果表明OpenAI的点运行在9" data-date="10-01 02:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-01 02:00</span>
          <span class="news-item-title">Geekbench 7的结果表明OpenAI的点运行在9</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1002788/old-reddit-ai-scraping" target="_blank" rel="noopener" data-cat="keji" data-summary="Reddit进一步限制了谁可以使用“旧版Reddit”体验作为其打击抓取和自动化流量的努力的一部分。Reddit最近开始强制用户登录才能使用旧版Reddit ，但在“未来几个月”内，该公司表示您必须登录并[…]" data-title="Reddit表示，由于人工智能机器人，它必须削减对“旧Reddit”的访问权限" data-date="10-01 01:45" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-01 01:45</span>
          <span class="news-item-title">Reddit表示，由于人工智能机器人，它必须削减对“旧Reddit”的访问权限</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/" target="_blank" rel="noopener" data-cat="keji" data-summary="Reddit正在结束对RSS源的支持，因为该公司继续收紧对其大量用户生成内容的访问权限。" data-title="由于人工智能机器人， Reddit正在杀死RSS Feed并终止公共API访问" data-date="10-01 01:45" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-01 01:45</span>
          <span class="news-item-title">由于人工智能机器人， Reddit正在杀死RSS Feed并终止公共API访问</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/top-ai-tech-executives-promise-to-self-police-ai-development-nvidia-anthropic-openai-and-more-pledge-ai-labs-will-take-steps-to-build-a-positive-future" target="_blank" rel="noopener" data-cat="keji" data-summary="最大的人工智能实验室（ Google、Anthropic、Meta、OpenAI、SpaceXAI和Nvidia ）的负责人前往华盛顿，签署了“前沿责任联合承诺” ，承诺安全开发自己的模型。特朗普表示，这是推进人工智能的最佳方式，因为它可以平衡进步与安全。" data-title="顶级人工智能技术高管承诺“自我监管”人工智能开发" data-date="10-01 01:27" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-01 01:27</span>
          <span class="news-item-title">顶级人工智能技术高管承诺“自我监管”人工智能开发</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">10 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/news/audio/2026/oct/01/billionaire-sheiks-and-sham-contracts-the-manchester-city-scandal-podcast" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="乔纳森·刘（ Jonathan Liew ）解释了对曼城的指控，西蒙·哈滕斯通（ Simon Hattenstone ）解释了作为《卫报》的特写作家西蒙·哈滕斯通（ Simon Hattenstone ）作为曼城球迷50多年的感受。当他开始与父亲在家乡参加比赛时，他还很年轻，从童年时期几乎要死的疾病中恢复过来。很长一段时间，这是一段建立在偶尔的高潮和" data-title="亿万富翁酋长和“虚假”合同：曼城丑闻" data-date="10-01 10:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 10:00</span>
          <span class="news-item-title">亿万富翁酋长和“虚假”合同：曼城丑闻</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/30/etihad-airways-considering-legal-action-premier-league-manchester-city" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="航空公司“断然拒绝”委员会的有罪判决自2009年以来，埃蒂哈德一直是俱乐部的主要球衣赞助商曼城的主要赞助商阿提哈德航空公司（ Etihad Airways ）正在考虑对英超联赛采取法律行动，此前该公司公布了独立委员会对俱乐部违反财务规则的100多项调查结果的核心决定。阿提哈德在周三晚上发布的一份声明中表示，它“断然拒绝”这一罪行" data-title="城市赞助商阿提哈德航空考虑对英超采取法律行动" data-date="10-01 05:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 05:30</span>
          <span class="news-item-title">城市赞助商阿提哈德航空考虑对英超采取法律行动</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6vgyg3zv3kwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="高级足球人物告诉BBC Sport ，曼城对违反英超联赛规则的惩罚应该在本赛季结束前传下来。" data-title="其他俱乐部负责人说，本赛季惩罚曼城" data-date="10-01 04:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-01 04:38</span>
          <span class="news-item-title">其他俱乐部负责人说，本赛季惩罚曼城</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/30/manchester-city-whistleblower-rui-pinto-no-longer-protected-witness-premier-league-portuguese-police" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="工作提供了有关曼城财务的信息他称曼城的决定对英格兰足球来说是“历史性的”鲁伊·平托（ Rui Pinto ）的私人文件泄露有助于引发英超联赛对曼城金融事务的调查，他将不再作为证人受到葡萄牙当局的保护，这可以被揭露。根据卫队看到的文件，周三决定解除对举报人的保护" data-title="曼城举报人Rui Pinto在葡萄牙不再是受保护的证人" data-date="10-01 03:40" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 03:40</span>
          <span class="news-item-title">曼城举报人Rui Pinto在葡萄牙不再是受保护的证人</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/30/rival-clubs-feel-relegating-manchester-city-championship-not-enough-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛高管推动严厉惩罚曼城坚持认为他们是“无辜的指控”英超联赛将面临来自曼城竞争对手的压力，要求在俱乐部被判犯有100多项违反财务规则的指控后，要求长期缺席顶级联赛。许多英超联赛俱乐部的高管告诉《卫报》，扣分将降低" data-title="对手俱乐部认为将曼城降级为冠军是不够的" data-date="10-01 02:55" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 02:55</span>
          <span class="news-item-title">对手俱乐部认为将曼城降级为冠军是不够的</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/30/andy-burnham-manchester-city-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="俱乐部是建设现代曼彻斯特独立足球监管机构监控案件的巨大合作伙伴安迪·伯纳姆（ Andy Burnham ）表示，由于俱乐部被判犯有100多项违反英超联赛规则的罪行，他将“非常担心”失去曼城的所有者。在独立足球监管机构确认其有权调查阿布扎比联赛集团是否适合在英超联赛结束后拥有一家英格兰俱乐部" data-title="安迪·伯纳姆（ Andy Burnham ）承认，如果曼城在有罪判决后失去主人，他会“担心”" data-date="10-01 02:31" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 02:31</span>
          <span class="news-item-title">安迪·伯纳姆（ Andy Burnham ）承认，如果曼城在有罪判决后失去主人，他会“担心”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9y7zr4l6de1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育台（ BBC Sport ）审视了曼城（ Manchester City ）被判有罪判决后的关键问题。" data-title="刑事调查？降级还是驱逐？曼城的关键问题" data-date="09-30 21:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-30 21:17</span>
          <span class="news-item-title">刑事调查？降级还是驱逐？曼城的关键问题</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/30/manchester-city-premier-league-legal-costs" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="俱乐部被判犯有违反财务规则的罪行曼城否认有不当行为，称这是一个“阴谋论”曼城在被判犯有几乎所有针对他们的指控后，预计将欠英超联赛数千万英镑的法律费用。英超联赛周二宣布，一个独立委员会已确定该俱乐部在9个月内人为地将他们的收入增加了9亿英镑" data-title="曼城可能被迫向英超支付高达5000万英镑的法律费用" data-date="09-30 20:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-30 20:16</span>
          <span class="news-item-title">曼城可能被迫向英超支付高达5000万英镑的法律费用</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckrerg4n2v82o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前曼城老板瓜迪奥拉表示，在他们被判犯有财务指控后，他将“永远”支持俱乐部。" data-title="瓜迪奥拉在有罪判决后支持曼城" data-date="09-30 18:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-30 18:07</span>
          <span class="news-item-title">瓜迪奥拉在有罪判决后支持曼城</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/30/throw-your-medals-in-the-bin-roy-keane-tells-manchester-city-players" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前曼联队长罗伊·基恩（ Roy Keane ）表示，如果他是曼城球员，他将把“奖牌扔进垃圾桶” ，因为英超联赛周二确认俱乐部犯有与财务规则相关的所有指控，并在与商业部门安排“虚假合同”后将他们的收入增加了9亿多£" data-title="“把你的奖牌扔进垃圾桶，”罗伊·基恩告诉曼城球员" data-date="09-30 17:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-30 17:53</span>
          <span class="news-item-title">“把你的奖牌扔进垃圾桶，”罗伊·基恩告诉曼城球员</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cxyvzvqp0z01o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这次加费是高市政府收紧移民政策的一环，目的是管理快速增长的外国人口。" data-title="日本收紧外国人居留条件，申请费用上调二十倍" data-date="10-01 15:38" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-01 15:38</span>
          <span class="news-item-title">日本收紧外国人居留条件，申请费用上调二十倍</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/082.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 1 日消息，当地时间 9 月 29 日，据《财富》杂志报道，现如今，数据中心已然成为 AI 争议中的焦点之一。批评者担心，大规模建设数据中心会给社区带来耗水、用电和噪声等问题。但与此同时，数据中心也催生了庞大的用工需求，其中技术工种尤其缺人。谷歌俄亥俄州和印第安纳州数据中心运营区域负责人蒂姆 · 查德威克在博客中写道：“目前全美有数十万个技术工种岗位空缺，等着有人来填补。高级电工、管道安装领班、项目经理都在其中，这些职业需求增长快，也能提供长期稳定的收入。”仲量联行一份报告援引美国教育部估算称，到 2030 年，美国约有 210 万个技术工种岗位可能招不到人。对劳动者来说，这也意味着越来越多职业道路无需四年制大学学历，通过职业技术培训、学徒制和在岗实践，同样可以掌握专业技" data-title="数据中心催生庞大用工需求，谷歌高管称全美存在数十万个技术工种缺口" data-date="10-01 15:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 15:36</span>
          <span class="news-item-title">数据中心催生庞大用工需求，谷歌高管称全美存在数十万个技术工种缺口</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/081.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 1 日消息，世纪天成昨天在官网发布公告，宣布经典端游《跑跑卡丁车》计划于 2026 年 10 月 29 日正式升级为 64 位客户端。官方表示，《跑跑卡丁车》客户端完成升级后，游戏将不再支持 32 位 Windows 操作系统。请各位玩家确认自己的电脑是 64 位 Windows 系统，方可正常游玩本作。IT之家了解到，《跑跑卡丁车》将于 10 月 29 日通过 TCG 客户端完成 64 位新版本升级。本次补丁包容量较大，大小接近完整客户端重装体积，请预留充足磁盘空间，建议在网络条件良好的环境下进行更新下载。官方建议各位玩家提前下载安装 Visual C++ 2015‑2022 (x64)、DirectX End‑User Runtime 运行组件，以便更新后能够顺畅游玩" data-title="经典端游《跑跑卡丁车》本月末升级 64 位客户端，不再支持 32 位 Windows 系统" data-date="10-01 15:30" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 15:30</span>
          <span class="news-item-title">经典端游《跑跑卡丁车》本月末升级 64 位客户端，不再支持 32 位 Windows 系统</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/080.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 1 日消息，数码博主 @i冰宇宙 今天（10 月 1 日）发布微博，分享了一张图片，展示了 5 款适用于三星 Galaxy S27 Ultra 旗舰手机的保护膜，并称基本上和 Galaxy S26 Ultra 手机通用。IT之家附上微博内容如下：“Galaxy S27 Ultra 保护膜基本可以和 S26 Ultra 通用。居然有防窥膜，属实多此一举”。该博主在 X 平台上也同步发布推文，补充了更多信息：下图为三星 Galaxy S27 Ultra 的屏幕保护膜。S27 Ultra 和 S26 Ultra 之间的差异微乎其微。事实上，这可能是三星历史上两款连续 Ultra 旗舰机型在正面屏幕设计上变化最小的一次。根据我们目前所了解的情况来看，屏幕尺寸、形状和整体轮廓都非常" data-title="三星 Galaxy S27 Ultra 手机保护膜曝光，基本和 S26 Ultra 通用" data-date="10-01 15:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 15:28</span>
          <span class="news-item-title">三星 Galaxy S27 Ultra 手机保护膜曝光，基本和 S26 Ultra 通用</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706700.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月1日电 据“中国铁路”微信公众号消息，10月1日，全国铁路预计发送旅客2480万人次，客流保持高位运行，计划加开旅客列车2324列。9月30日，全国铁路发送旅客1954.2万人次，运输安全平稳有序。" data-title="10月1日全国铁路预计发送旅客2480万人次" data-date="10-01 14:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:31</span>
          <span class="news-item-title">10月1日全国铁路预计发送旅客2480万人次</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/30/us/christa-pike-stay-execution-tennessee.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="克里斯塔·派克（ Christa Pike ）于1995年因谋杀一名同学而被定罪。目前尚不清楚处决中出现了什么问题，也不清楚她目前的身体状况。" data-title="律师说，田纳西州死刑犯克里斯塔·派克在试图处决她后仍然活着" data-date="10-01 14:15" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-01 14:15</span>
          <span class="news-item-title">律师说，田纳西州死刑犯克里斯塔·派克在试图处决她后仍然活着</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706693.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长沙10月1日电 题：“扫帚诗人”黄新生：扫帚扫街巷，诗笔写人间" data-title="“扫帚诗人”黄新生：扫帚扫街巷，诗笔写人间" data-date="10-01 14:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:12</span>
          <span class="news-item-title">“扫帚诗人”黄新生：扫帚扫街巷，诗笔写人间</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706699.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="根据国铁集团消息，今天(1日)为客流高峰日，预计发送旅客2480万人次，预计加开列车2324列。目前，全国铁路的运行情况如何？有哪些出行新特点？" data-title="国庆假期第一天铁路迎客流最高峰 最新出行提示→" data-date="10-01 14:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:11</span>
          <span class="news-item-title">国庆假期第一天铁路迎客流最高峰 最新出行提示→</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706683.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口10月1日电 (高磊 吕东星)10月1日，国庆假期开启，琼州海峡、三亚陆岛水域迎来出行高峰。据海南海事局披露，假期琼州海峡预计运送旅客57.5万人次、车辆16万台次，三亚陆岛运输预计运送旅客30.4万人次。" data-title="国庆假期琼州海峡迎出行高峰 海事部门高效护航" data-date="10-01 14:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:11</span>
          <span class="news-item-title">国庆假期琼州海峡迎出行高峰 海事部门高效护航</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706689.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网牡丹江10月1日电 (记者 王琳)10月1日凌晨4时左右，位于龙江森工大海林林业局有限公司双峰林场的中国雪乡风景区降下今秋首场瑞雪，为秋色增添了一抹温柔又清冽的浪漫。" data-title="中国雪乡“十一”迎来今秋首场瑞雪" data-date="10-01 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:08</span>
          <span class="news-item-title">中国雪乡“十一”迎来今秋首场瑞雪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706691.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长春10月1日电 (高龙安 李彦国)长期握工具、搬重物，“05后”女孩何晓嫚的手比常人更显粗糙。这是记者在长春见到她的第一印象。" data-title="世界技能大赛“冠军中的冠军”：成功源于勤奋" data-date="10-01 14:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 14:07</span>
          <span class="news-item-title">世界技能大赛“冠军中的冠军”：成功源于勤奋</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq7702n27ynxo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="纽卡斯尔联队主教练马蒂亚斯·贾斯尔（ Matthias Jaissle ）一度无法移动他的脖子，但在开始在泰恩赛德（ Tyneside ）的教练生涯之前，他继续打球。" data-title="Jaissle在5岁肿瘤后学到了很多关于生活的知识" data-date="10-01 14:00" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-01 14:00</span>
          <span class="news-item-title">Jaissle在5岁肿瘤后学到了很多关于生活的知识</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706672.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社浙江温州10月1日电 题：一块浪板“撬动”新活力 浙江苍南小渔村“逐浪”新生" data-title="（走进中国乡村）一块浪板“撬动”新活力 浙江苍南小渔村“逐浪”新生" data-date="10-01 13:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:29</span>
          <span class="news-item-title">（走进中国乡村）一块浪板“撬动”新活力 浙江苍南小渔村“逐浪”新生</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-01/10706665.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月1日电 (钱晨菲 江林海)10月1日，浙江海警局发布消息称，日前浙江宁波海警局联合宁波市公安局、宁波边检站、宁波市海洋与渔业执法队在象山渔山海域成功查获一艘走私船舶，当场抓获犯罪嫌疑人4名，查获牛板筋等冻品150余吨，涉案金额1000余万元。" data-title="轨迹露出马脚 一艘“渔船”牵出千万元走私案" data-date="10-01 13:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-01 13:27</span>
          <span class="news-item-title">轨迹露出马脚 一艘“渔船”牵出千万元走私案</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/01/us/christa-pike-alive-tennessee-execution-halted.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="50岁的派克女士在田纳西州两次注射致命药物后幸存下来。她因1995年谋杀一名同学而被判处死刑。" data-title="关于克里斯塔·派克（ Christa Pike ）未遂死刑的须知事项" data-date="10-01 13:16" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-01 13:16</span>
          <span class="news-item-title">关于克里斯塔·派克（ Christa Pike ）未遂死刑的须知事项</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-01 15:54（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
