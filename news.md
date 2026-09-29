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
      <span>2026-09-29 22:14 抓取更新</span>
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
        <span class="channel-count">54</span>
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
        <span class="channel-count">9</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-29/10705921.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月29日电 (记者 张杨彬)为纪念孙中山先生诞辰160周年，由民革中央主办的孙中山与华侨华人学术研讨会29日在北京举行。" data-title="孙中山与华侨华人学术研讨会在北京举行" data-date="09-29 21:50" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-29 21:50</span>
      </div>
      <h2 class="hero-featured-title">孙中山与华侨华人学术研讨会在北京举行</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/1001886/meta-muse-ai-facebook-marketplace-security-concerns" target="_blank" rel="noopener" data-cat="keji" data-summary="Tech YouTuber Matt Robb表示， Muse在授权机器人处理他的Facebook Marketplace帐户后，于本周末向一个完全陌生的人透露了他的家庭住址。尽管Meta在本月早些时候推出个人AI代理时非常重视Muse的安全功能，因为它试图抓住[…]" data-title="Meta的Muse AI向陌生人发送了YouTuber的地址" data-date="09-29 22:08" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Meta的Muse AI向陌生人发送了YouTuber的地址</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/commentisfree/2026/sep/29/manchester-city-global-mega-rich-impunity" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当跨国联盟几乎没有减弱时，据称俱乐部的运营方式提供了一个由蛮力和财富驱动的世界的黯淡愿景。Der Spiegel于2018年发布了最终导致曼城陷入危机的泄露电子邮件和文件的缓存，而俱乐部沟通的基调往往与其内容一样令人震惊。市主席Khaldoon al-Mubarak" data-title="曼城的案例向我们展示了全球超级富豪现在如何期望不受惩罚地运营| Jonathan Liew" data-date="09-29 21:30" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">曼城的案例向我们展示了全球超级富豪现在如何期望不受惩罚地运营| Jonathan Liew</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1001905/amazon-leak-basic-entry-level-kindle-colors-design-power-button" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊通常在假日购物季节前几个月推出新的Kindle机型，今年看起来将包括比2024年推出的更大的入门级Kindle更新。Kindle基本型号的最新升级仅限于更亮的背光、新的深色模式和[…]" data-title="泄露的图像揭示了亚马逊下一个条目的新颜色" data-date="09-29 22:10" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">泄露的图像揭示了亚马逊下一个条目的新颜色</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705921.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月29日电 (记者 张杨彬)为纪念孙中山先生诞辰160周年，由民革中央主办的孙中山与华侨华人学术研讨会29日在北京举行。" data-title="孙中山与华侨华人学术研讨会在北京举行" data-date="09-29 21:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:50</span>
          <span class="news-item-title">孙中山与华侨华人学术研讨会在北京举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705914.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网沈阳9月29日电 (记者 李𬀪)“情系桑梓 赋能振兴——辽宁籍文化人才回乡行动”9月28日在沈阳启动。单霁翔、刘兰芳、冯巩、于魁智、李梓萌等50余位辽宁籍文化人才回乡，畅谈对家乡的深厚情感，分享各自创作历程中的辽宁印记。" data-title="单霁翔、刘兰芳等50余位辽籍文化人才回乡共讲辽宁故事" data-date="09-29 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:42</span>
          <span class="news-item-title">单霁翔、刘兰芳等50余位辽籍文化人才回乡共讲辽宁故事</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705908.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月29日电 (记者 余湛奕)9月29日晚，全总文工团、北京市总工会在京联合举办“为劳动者放歌”慰问首都职工文艺演出。首都劳模工匠、新就业形态劳动者和一线职工代表1000余人现场观看。" data-title="“为劳动者放歌”慰问首都职工文艺演出在京举办" data-date="09-29 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:41</span>
          <span class="news-item-title">“为劳动者放歌”慰问首都职工文艺演出在京举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705896.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆9月29日电 (记者 钟旖)穿越时光，中国近代爱国实业家卢作孚的爱国精神如何照亮新时代青年的前行路？29日，在卢作孚的故乡——重庆市合川区，“作孚爱国精神与新时代青年担当”青年主题对话沙龙活动举行，40余位专家学者、青年代表“面对面”交流，在传承、弘扬作孚爱国精神中凝聚青年担当。" data-title="青年如何传承卢作孚爱国精神？重庆合川举办青年主题对话沙龙" data-date="09-29 21:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:39</span>
          <span class="news-item-title">青年如何传承卢作孚爱国精神？重庆合川举办青年主题对话沙龙</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705876.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网山东曲阜9月29日电(周艺伟 孙婷婷)为期两天的2026尼山世界文明论坛(简称“尼山论坛”)29日在孔子诞生地山东曲阜落下帷幕。" data-title="从尼山出发 以文明对话求索秩序与公理" data-date="09-29 21:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:36</span>
          <span class="news-item-title">从尼山出发 以文明对话求索秩序与公理</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705887.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宁德9月29日电 (记者 叶茂)周宁县“极地科普馆”开馆仪式29日在福建省宁德市周宁县举行。“极地科普馆”的落成，是周宁县以科普促创新、以创新驱动发展的又一成果，将成为传播科学精神、激发创新热情的重要平台。" data-title="福建首个“极地科学”主题科普馆在周宁开馆" data-date="09-29 21:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:35</span>
          <span class="news-item-title">福建首个“极地科学”主题科普馆在周宁开馆</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-29/10705788.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月29日电(记者 刁炜)近期在也门战场上，胡塞武装大量投放包括第一视角无人机(FPV)在内的小型旋翼无人机，用于侦察敌情和打击对手的人员装备，取得一系列战果。" data-title="无人机300米高度投弹，胡塞武装飞手肉眼瞄准炸坦克" data-date="09-29 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 20:26</span>
          <span class="news-item-title">无人机300米高度投弹，胡塞武装飞手肉眼瞄准炸坦克</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-29/10705640.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆9月29日电 (梁钦卿)重庆市委宣传部29日对外公布，“陆海讲读堂”西班牙站活动于当地时间9月28日在马德里举办。本次活动以《绯色盛宴：葡萄酒的全球史》为主题，吸引约200名中西文化、出版、教育、媒体领域从业者及读者代表参与。" data-title="“陆海讲读堂”走进马德里：讲述一杯酒里的中西文明对话" data-date="09-29 17:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 17:14</span>
          <span class="news-item-title">“陆海讲读堂”走进马德里：讲述一杯酒里的中西文明对话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-29/10705579.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月29日电 布宜诺斯艾利斯消息：阿根廷总统府当地时间28日发表声明说，阿根廷总统米莱已指示外交部和政府法律团队启动《联合国海洋法公约》附件七规定的仲裁程序，以阻止英国在马尔维纳斯群岛(简称马岛，英称福克兰群岛)附近通过海狮油田项目开发油气资源。" data-title="阿根廷称将就马岛海狮油田项目启动国际仲裁" data-date="09-29 17:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 17:14</span>
          <span class="news-item-title">阿根廷称将就马岛海狮油田项目启动国际仲裁</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/29/us/politics/ad-watch-nebraska-senate-race.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一个支持内布拉斯加州独立参议员候选人丹·奥斯本（ Dan Osborn ）的团体正在播放一则广告，攻击共和党参议员皮特·里基茨（ Pete Ricketts ）赦免一名被判犯有性侵犯罪的男子。" data-title="一则强硬的广告提醒内布拉斯加州选民注意残酷的犯罪和赦免" data-date="09-29 17:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-29 17:03</span>
          <span class="news-item-title">一则强硬的广告提醒内布拉斯加州选民注意残酷的犯罪和赦免</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-29/10705585.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月29日电 据俄罗斯卫星通讯社28日报道，俄罗斯副外长鲁坚科表示，俄罗斯不相信日本有关在联合军演结束后撤走美国“堤丰”中程导弹系统的承诺，俄方将准备回应措施。" data-title="俄罗斯警告日本：不相信日方承诺 将准备回应措施" data-date="09-29 15:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 15:59</span>
          <span class="news-item-title">俄罗斯警告日本：不相信日方承诺 将准备回应措施</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705562.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月29日电 (记者 曾玥 郭超凯)中国外交部发言人郭嘉昆29日主持例行记者会。" data-title="中方回应菲律宾发布所谓新版“海图”：严重侵犯中国领土主权，是非法、无效的" data-date="09-29 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 15:30</span>
          <span class="news-item-title">中方回应菲律宾发布所谓新版“海图”：严重侵犯中国领土主权，是非法、无效的</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705561.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月29日电 (记者 曾玥)中国外交部发言人郭嘉昆29日主持例行记者会。" data-title="《中日联合声明》发表54周年 中方再次敦促日本当政者切实反思纠错" data-date="09-29 15:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 15:29</span>
          <span class="news-item-title">《中日联合声明》发表54周年 中方再次敦促日本当政者切实反思纠错</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705560.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="9月29日，外交部发言人郭嘉昆主持例行记者会。总台央视记者问：今天是《中日联合声明》发表54周年纪念日。当前中日关系面临严重困难，请问中方如何看待《中日联合声明》等四个政治文件的历史和现实意义？" data-title="外交部：只有真正恪守中日四个政治文件精神 两国关系才能不偏航、不脱轨" data-date="09-29 15:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 15:29</span>
          <span class="news-item-title">外交部：只有真正恪守中日四个政治文件精神 两国关系才能不偏航、不脱轨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月29日电 据“中国海警”微信公众号消息，中国海警局新闻发言人姜略表示，9月29日，中国海警朱家尖舰编队位中国台湾岛以东海域依法开展常态化执法巡查。9月以来，朱家尖舰编队持续加强相关海域管控，有力保障正常航行和作业秩序，切实维护包括台湾同胞在内的中国民众合法正当权益和生命财产安全。中国海警将持续加强在中国管辖海域执法巡查，坚决维护国家领土主权和海洋权益。" data-title="中国海警位中国台湾岛以东海域依法开展常态化执法巡查" data-date="09-29 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 15:26</span>
          <span class="news-item-title">中国海警位中国台湾岛以东海域依法开展常态化执法巡查</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1001886/meta-muse-ai-facebook-marketplace-security-concerns" target="_blank" rel="noopener" data-cat="keji" data-summary="Tech YouTuber Matt Robb表示， Muse在授权机器人处理他的Facebook Marketplace帐户后，于本周末向一个完全陌生的人透露了他的家庭住址。尽管Meta在本月早些时候推出个人AI代理时非常重视Muse的安全功能，因为它试图抓住[…]" data-title="Meta的Muse AI向陌生人发送了YouTuber的地址" data-date="09-29 22:08" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-29 22:08</span>
          <span class="news-item-title">Meta的Muse AI向陌生人发送了YouTuber的地址</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-29/10705927.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="世界互联网大会今天(29日)召开新闻发布会，记者从发布会上了解到，2026年世界互联网大会乌镇峰会将于11月2日至5日在浙江省乌镇举行。本次乌镇峰会以“开源开放 共建共享——携手构建网络空间命运共同体”为主题，将邀请来自全球的政府、国际组织、企业、专家学者代表，围绕人工智能开源开放发展的理念与实践，从创新发展、安全治理、文明交流、国际合作等多个维度展开深入交流，共同探索在人工智能快速发展的新阶段，如何进一步推动技术开放、创新协作和成果共享。" data-title="2026年世界互联网大会乌镇峰会将于11月2日至5日举行" data-date="09-29 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 22:00</span>
          <span class="news-item-title">2026年世界互联网大会乌镇峰会将于11月2日至5日举行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/29/with-dazzle-marissa-mayer-bets-your-camera-roll-has-more-info-on-your-life-than-your-inbox/" target="_blank" rel="noopener" data-cat="keji" data-summary="这位前雅虎首席执行官将完全基于您的照片推出一款新的人工智能个人助理。" data-title="通过Dazzle ， Marissa Mayer打赌您的相机胶卷比您的收件箱有更多关于您生活的信息" data-date="09-29 21:53" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-29 21:53</span>
          <span class="news-item-title">通过Dazzle ， Marissa Mayer打赌您的相机胶卷比您的收件箱有更多关于您生活的信息</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/29/meta-is-expanding-its-ai-agent-muse-to-small-businesses/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家科技巨头表示，该代理可以帮助业主经营业务并寻找新客户。" data-title="Meta正在将其人工智能代理Muse扩展到小企业" data-date="09-29 21:47" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-29 21:47</span>
          <span class="news-item-title">Meta正在将其人工智能代理Muse扩展到小企业</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705913.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网陕西渭南9月29日电 (记者 阿琳娜)9月29日，在第四届气象旅游发展大会上，全国文旅气象服务智能体基座建设示范计划正式启动。该计划由中国气象局公共气象服务中心(以下简称：公共服务中心)发起，旨在推动人工智能与气象、文化和旅游深度融合，打造统一的文旅气象服务智能体基座和工具能力平台，以国家级集约建设、地方按需组装模式，提升文旅气象服务能力。" data-title="全国文旅气象服务智能体基座建设示范计划启动" data-date="09-29 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:42</span>
          <span class="news-item-title">全国文旅气象服务智能体基座建设示范计划启动</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-lists-existential-risks-to-humanity-as-one-of-its-risk-factors-in-ipo-prospectus-80-pages-of-risk-factors-dwarf-business-description-as-firm-eyes-usd2-trillion-debut" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic在其IPO招股说明书中发出了可怕的警告，称流氓模式可能导致人类的终结，从而导致其业务的终结。尽管如此，投资者仍然希望公司上市后估值达到2万$。" data-title="Anthropic在IPO招股说明书中将“人类生存风险”列为其风险因素之一" data-date="09-29 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-29 21:30</span>
          <span class="news-item-title">Anthropic在IPO招股说明书中将“人类生存风险”列为其风险因素之一</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/29/openai-apologizes-to-australia-after-its-ai-agents-breached-government-sites/" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司还详细说明了其中一些违规行为是如何发生的，并概述了其正在采取的其他措施，以评估事件的影响。" data-title="OpenAI在人工智能特工入侵政府网站后向澳大利亚道歉" data-date="09-29 20:45" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-29 20:45</span>
          <span class="news-item-title">OpenAI在人工智能特工入侵政府网站后向澳大利亚道歉</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/silicon-is-starting-to-design-silicon-how-ai-is-being-used-in-chipmaking-from-eda-tools-to-openais-jalapeno-and-beyond" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能与设计其运行的相同芯片有多接近？我们探讨了人工智能如何在当今的现代芯片设计中使用。" data-title="Silicon开始设计硅--人工智能在芯片制造中的应用，从EDA工具到OpenAI的Jalapeño等等" data-date="09-29 20:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-29 20:40</span>
          <span class="news-item-title">Silicon开始设计硅--人工智能在芯片制造中的应用，从EDA工具到OpenAI的Jalapeño等等</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/" target="_blank" rel="noopener" data-cat="keji" data-summary="该轮融资是在2月份筹集3000万美元的基础上进行的，使该公司的总融资额达到1.4亿美元。" data-title="随着人工智能代理安全初创公司挤进市场， Reco筹集了5500万$" data-date="09-29 20:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-29 20:30</span>
          <span class="news-item-title">随着人工智能代理安全初创公司挤进市场， Reco筹集了5500万$</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intels-nova-lake-platforms-pass-compliance-at-pci-sig-usb-if-as-launch-looms" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔正在为Core Ultra 400系列“Nova Lake”平台的发布做准备，因为CPU和芯片组通过了与PCI-SIG和USB-IF的互操作性和合规性测试。" data-title="随着发布的临近，英特尔的下一代Nova Lake平台通过USB和PCIe标准机构的合规性认证" data-date="09-29 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-29 20:00</span>
          <span class="news-item-title">随着发布的临近，英特尔的下一代Nova Lake平台通过USB和PCIe标准机构的合规性认证</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1001767/khanna-ai-safety-china-treaty" target="_blank" rel="noopener" data-cat="keji" data-summary="当唐纳德·特朗普总统准备在华盛顿会见科技和人工智能首席执行官时，众议员Ro Khanna （ D-CA ）呼吁美国和中国之间达成一项条约，以防止人工智能对世界造成严重破坏。但是，与两国领导人争吵以采取行动可能是一个漫长的过程。在信件中，仅与[…]共享" data-title="中国人工智能公司会放缓吗？众议院民主党高层希望得到答案" data-date="09-29 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-29 20:00</span>
          <span class="news-item-title">中国人工智能公司会放缓吗？众议院民主党高层希望得到答案</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/amd-drops-an-epyc-usd15-000-256-core-bomb-epyc-9006-zen-6-venice-cpus-get-full-spec-and-pricing-treatment-from-usd700-up-to-usd14-904" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD已分享其第六代EPYC 9006 （代号为威尼斯）系列的完整SKU列表，定价为1Ku。" data-title="AMD放弃EPYC $ 15,000, 256" data-date="09-29 19:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-29 19:20</span>
          <span class="news-item-title">AMD放弃EPYC $ 15,000, 256</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/499239.html" target="_blank" rel="noopener" data-cat="keji" data-summary="推动公司具身模型、本体、软件等全栈能力进入更多真实场景" data-title="正行创新联合创始人杨宇欣正式亮相：出任总裁，负责全球业务拓展" data-date="09-29 18:56" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-29 18:56</span>
          <span class="news-item-title">正行创新联合创始人杨宇欣正式亮相：出任总裁，负责全球业务拓展</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/499140.html" target="_blank" rel="noopener" data-cat="keji" data-summary="AGI计划暂停。" data-title="OpenAI因新模型太强叫停发布" data-date="09-29 15:49" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-29 15:49</span>
          <span class="news-item-title">OpenAI因新模型太强叫停发布</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/008/310.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 29 日消息，世界互联网大会官方今日召开新闻发布会，宣布 2026 年世界互联网大会乌镇峰会将于 11 月 2 日至 5 日在浙江省乌镇举行。本次峰会主题为“开源开放共建共享 —— 携手构建网络空间命运共同体”。本届峰会将邀请全球政府、国际组织、企业、专家学者代表，围绕人工智能开源开放发展的理念与实践，从创新发展、安全治理、文明交流、国际合作等多个维度展开交流。IT之家从官方获悉，今年乌镇峰会将设置 27 个分论坛，围绕全球治理倡议网络空间合作、数智时代的理论与政策、机器人与具身智能等话题展开讨论。主论坛将设置“人工智能乌镇对话”环节，邀请全球领军科技企业、知名开源大模型企业负责人以及人工智能科学家同台对话，围绕全球人工智能开源生态构建等议题展开交流。“携手构建网络空间命运" data-title="2026 年世界互联网大会乌镇峰会 11 月 2 日至 5 日举行：设 27 个分论坛，聚焦人工智能开源开放" data-date="09-29 15:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-29 15:27</span>
          <span class="news-item-title">2026 年世界互联网大会乌镇峰会 11 月 2 日至 5 日举行：设 27 个分论坛，聚焦人工智能开源开放</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/commentisfree/2026/sep/29/manchester-city-global-mega-rich-impunity" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当跨国联盟几乎没有减弱时，据称俱乐部的运营方式提供了一个由蛮力和财富驱动的世界的黯淡愿景。Der Spiegel于2018年发布了最终导致曼城陷入危机的泄露电子邮件和文件的缓存，而俱乐部沟通的基调往往与其内容一样令人震惊。市主席Khaldoon al-Mubarak" data-title="曼城的案例向我们展示了全球超级富豪现在如何期望不受惩罚地运营| Jonathan Liew" data-date="09-29 21:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-29 21:30</span>
          <span class="news-item-title">曼城的案例向我们展示了全球超级富豪现在如何期望不受惩罚地运营| Jonathan Liew</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/29/premier-league-fast-start-teams-manchester-city" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城以连续五场胜利拉开了比赛的序幕，但冠军争夺战是一场马拉松而不是短跑Opta Analyst第一个国际窗口让我们有时间进行评估，并了解英超赛季前几周发生的事情。曼城是唯一一支赢得所有五场比赛的球队。他们在瓜迪奥拉之后以最好的方式在球场上开始生活，开了一个三分球" data-title="对于追逐英超冠军的球队来说，快速起步有多重要？" data-date="09-29 20:41" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-29 20:41</span>
          <span class="news-item-title">对于追逐英超冠军的球队来说，快速起步有多重要？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6e3077kkde3o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦在寻找全球青年人才方面变得越来越积极主动。英国广播公司体育频道（ BBC Sport ）近距离观看。" data-title="利物浦日益增加的全球青年投资" data-date="09-29 15:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-29 15:19</span>
          <span class="news-item-title">利物浦日益增加的全球青年投资</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/extra/x3s96hvhqb/the-story-of-manchester-city-and-115-charges?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是英超历史上最大的纪律处分案件。在这里，我们将曼城的现场努力与他们所谓的不法行为拼凑在一起。" data-title="曼城的故事和115项指控" data-date="09-29 08:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-29 08:00</span>
          <span class="news-item-title">曼城的故事和115项指控</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/28/manchester-city-chief-executive-ferran-soriano-premier-league-rivals-urge-commission-publish-verdict" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="费兰·索里亚诺（ Ferran Soriano ）告诉欧洲俱乐部曼城将与判决作斗争英超联赛俱乐部抱怨时间表“无效”一些英超联赛俱乐部正在推动尽快公布曼城的判决，俱乐部正在进行长期的斗争，以清除他们的名字。曼城首席执行官费兰·索里亚诺（ Ferran Soriano ）周一在欧洲足球俱乐部董事会会议上表示，他们将努力证明自己是无辜的。" data-title="曼城酋长坚持认为俱乐部是无辜的，因为竞争对手正在推动公布判决" data-date="09-29 04:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-29 04:30</span>
          <span class="news-item-title">曼城酋长坚持认为俱乐部是无辜的，因为竞争对手正在推动公布判决</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/28/manchester-city-punishment-premier-league-charges" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Khaldoon al-Mubarak已经出来战斗，但英超联赛未能完全规范他的俱乐部什么都没有结束，什么也没做。或者至少不是从勇气来判断，曼城主席Khaldoon al-Mubarak的信心，他仍然相信过去三天的鞭笞只是大揭露之前的鼓声，这是一些有力证据的前奏，这些证据将冲走P最初的内疚发现" data-title="城市的惩罚规模是唯一的故事，但英超联赛必须承担一些责任| Barney Ronay" data-date="09-29 03:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-29 03:30</span>
          <span class="news-item-title">城市的惩罚规模是唯一的故事，但英超联赛必须承担一些责任| Barney Ronay</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckz7zxzdwl7lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport获悉，曼城首席执行官Ferran Soriano向其他球队的高管发出了一个挑衅的信息，即该俱乐部被判犯有大部分英超联赛指控。" data-title="曼城首席执行官对英超联赛指控的反抗" data-date="09-29 02:53" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-29 02:53</span>
          <span class="news-item-title">曼城首席执行官对英超联赛指控的反抗</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/28/roberto-mancini-double-contract-manchester-city" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据称教练因咨询工作而获得报酬城市的索里亚诺说，俱乐部将努力证明无辜罗伯托·曼奇尼似乎承认在管理曼城时有“双重合同” ，但坚称俱乐部在被发现违反英超联赛财务规则后无罪。曼奇尼在曼彻斯特的四年时间里带领曼城在2012年获得了他们的第一个英超联赛冠军。现在他负责意大利国家队，" data-title="曼奇尼提到“双重”曼城合同，并说“这不是我的问题”" data-date="09-29 01:52" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-29 01:52</span>
          <span class="news-item-title">曼奇尼提到“双重”曼城合同，并说“这不是我的问题”</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/28/how-the-manchester-city-scandal-could-play-out" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="读者对足球俱乐部违反英超金融公平竞争规则的有罪判决作出回应三十六年前，我支持的斯温顿镇球队因财务违规行为而受到严厉惩罚，与曼城的违规行为相比相形见绌（曼城因违反英超金融公平竞争规则而被判有罪， 9月25日）。我们最初被判降级为两个师，但是，" data-title="曼城丑闻可能如何演变|来信" data-date="09-29 00:54" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-29 00:54</span>
          <span class="news-item-title">曼城丑闻可能如何演变|来信</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1001905/amazon-leak-basic-entry-level-kindle-colors-design-power-button" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊通常在假日购物季节前几个月推出新的Kindle机型，今年看起来将包括比2024年推出的更大的入门级Kindle更新。Kindle基本型号的最新升级仅限于更亮的背光、新的深色模式和[…]" data-title="泄露的图像揭示了亚马逊下一个条目的新颜色" data-date="09-29 22:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-29 22:10</span>
          <span class="news-item-title">泄露的图像揭示了亚马逊下一个条目的新颜色</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705929.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社黑龙江佳木斯9月29日电 (记者 王妮娜)“稻田一眼望不到边，看不到人，只有无人驾驶收割机在自动收割水稻，很震撼。”新加坡《海峡时报》记者游润恬29日在黑龙江佳木斯富锦市万亩水稻科技示范园参观时说。" data-title="“外媒看中国”活动走进黑龙江 见证农业“智”变" data-date="09-29 22:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 22:10</span>
          <span class="news-item-title">“外媒看中国”活动走进黑龙江 见证农业“智”变</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/blockchain-assisted-cyberattacks-surge-fivefold-driven-by-iranian-and-north-korean-state-actors-russia-linked-groups-open-weight-llms-are-linked-to-an-increase-in-attacks" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一份新的报告称，区块链的死掉攻击增加了440% ，与国家相关的犯罪集团使用交易、智能合约，甚至是虚拟钱包来隐藏公共区块链上的恶意软件有效负载和C2基础设施。" data-title="在伊朗和朝鲜国家行为体以及与俄罗斯有关的团体的推动下，区块链辅助网络攻击激增了五倍" data-date="09-29 22:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-29 22:10</span>
          <span class="news-item-title">在伊朗和朝鲜国家行为体以及与俄罗斯有关的团体的推动下，区块链辅助网络攻击激增了五倍</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/008/497.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 29 日消息，据科技媒体 neowin 今天报道，微软正在改进使用 Win11 系统的 WoA 设备初次开机流程，让 OOBE 可以只更新关键驱动和固件。据报道，微软现已告知硬件合作伙伴，称 OOBE 现可提供特定版本的系统清单（System Manifest）。据IT之家了解，系统清单用于协调 WoA（Windows on ARM）设备的驱动程序和固件更新。如今厂商可选择在 OOBE 阶段只更新关键驱动或固件，将非必要的更新延后。这种改动将可以显著降低用户在 OOBE 的停留时间，带来更好的使用体验。对于其他轻微修复和改进，厂商应继续采用现有 Windows Update 机制。" data-title="微软将优化 Win11 ARM 设备初次开机 OOBE 流程，厂商可延后非关键驱动和固件更新" data-date="09-29 22:04" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-29 22:04</span>
          <span class="news-item-title">微软将优化 Win11 ARM 设备初次开机 OOBE 流程，厂商可延后非关键驱动和固件更新</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/008/496.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 29 日消息，冠捷新上架了一款 27 英寸办公显示器，型号为 AOC Q27V6X，京东售价 1299 元。该产品属于 AOC V6 黑曜系列，配备 27 英寸 2K IPS 面板，刷新率 180Hz。京东 AOC 27 英寸 2K 180Hz 硬件低蓝光 不闪屏护眼 HDR 升降旋转 节能认证 电竞办公显示器 Q27V6X1299 元直达链接核心参数方面，该显示器分辨率 2560×1440，刷新率 180Hz，响应时间 0.5ms MPRT / 4ms GtG；支持 MBR Sync 插黑帧同步技术；覆盖 100% sRGB（CIE 1931）、90% DCI-P3（CIE 1976）、91% Adobe RGB（CIE 1936）色域，经过出厂校色，平均 ΔE＜2；支持" data-title="AOC 推出 27 英寸 2K 180Hz 显示器 Q27V6X，1299 元" data-date="09-29 22:04" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-29 22:04</span>
          <span class="news-item-title">AOC 推出 27 英寸 2K 180Hz 显示器 Q27V6X，1299 元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october" target="_blank" rel="noopener" data-cat="zonghe" data-summary="现在还不到10月，亚马逊已经在自己的硬件上提供一些Prime Big Deal Day折扣，以及许多其他受欢迎的产品。这一切都是为了宣传10月黄金日，从10月6日美国东部时间凌晨3点开始，如果你在东部，则持续到8日美国东部时间凌晨3点[…]" data-title="目前最优惠的10月初黄金日优惠" data-date="09-29 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-29 22:00</span>
          <span class="news-item-title">目前最优惠的10月初黄金日优惠</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1000245/steelseries-rival-sensei-pro-uwb-swappable-batteries-specs-price" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新款符合人体工程学的Rival Pro和Sensei Pro无线游戏鼠标是该公司多年来最有趣的型号。它们是熟悉的设计，感觉非常轻便（黑色每件53克，白色每件1克） ，并且在其他产品类别中配备了两个标志性的SteelSeries功能： […]" data-title="SteelSeries的新鼠标超轻，配备超宽带和可更换电池" data-date="09-29 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-29 22:00</span>
          <span class="news-item-title">SteelSeries的新鼠标超轻，配备超宽带和可更换电池</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/008/495.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 29 日消息，据外媒 Push Square 今天报道，CDPR 今天推出《巫师 3：狂猎 — 重制版》游戏，本作的 PS5 版本支持 MOD 模组，但启用后将无法获取新奖杯。IT之家从原报道获悉，本作发售时提供超 40 款 MOD 供玩家下载。其中很多 Mod 只有轻微玩法调整，例如移除坠落伤害，或者让玩家在昆特牌游戏中自动获胜。有的则可以让杰洛特换上更好看的眉毛，或是让装备外观看起来更符合原著描述。目前 PS5 版《巫师 3》重制版还没有什么比较惊艳的 MOD，相信官方将会持续提供新模组。玩家可以打开主菜单，然后选择 MOD 浏览这些模组。" data-title="《巫师 3：狂猎 — 重制版》PS5 首发支持超 40 款 MOD，启用后无法获取奖杯" data-date="09-29 21:54" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-29 21:54</span>
          <span class="news-item-title">《巫师 3：狂猎 — 重制版》PS5 首发支持超 40 款 MOD，启用后无法获取奖杯</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/008/494.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 29 日消息，据新华社今日报道，记者从海南国际商业航天发射有限公司获悉，海南商业航天发射场二期项目主体工程完工并启动合练，经过后续合练和测试，两个发射工位计划年内形成发射能力。据悉，海南商业航天发射场二期项目于 2025 年 1 月 25 日正式启动建设，占地 1100 余亩，于今日正式具备合练能力。该项目建有两个通用型中型液体发射工位，可为长征十二号乙等 5 米直径以下两级构型火箭提供发射服务。随着海南商业航天发射场二期项目、测控系统及回收系统的全面建成，海南商业航天发射场将具备每年超 60 次的综合发射能力，形成“发射-测控-回收”的能力闭环。IT之家查询获悉，二期项目发射区主要建设三号、四号两个液体火箭发射工位及水塔等设施。双工位均借鉴二号发射工位进行统型设计，采用“" data-title="海南商业航天发射场二期项目开展合练，具备每年超 60 次的综合发射能力" data-date="09-29 21:54" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-29 21:54</span>
          <span class="news-item-title">海南商业航天发射场二期项目开展合练，具备每年超 60 次的综合发射能力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705923.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海9月29日电 (记者 姜煜)2026年“上海环球美食汇·风味无界”活动29日下午在青浦区蟠龙古镇启动。启动仪式由上海市商务委员会、青浦区人民政府主办，青浦区商务委员会、上海市商业联合会承办。" data-title="2026年“上海环球美食汇·风味无界”活动启动 7大环球美食地标发布" data-date="09-29 21:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:52</span>
          <span class="news-item-title">2026年“上海环球美食汇·风味无界”活动启动 7大环球美食地标发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705890.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月29日电 (记者 张素)秋冬时节被称为膏方进补调养的“窗口期”。29日在北京举行的一场中医药文化惠民活动上，中医医师介绍特色膏方，建言如何摆脱亚健康困扰。" data-title="膏方养生文化节启幕 中医建言摆脱亚健康困扰" data-date="09-29 21:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:43</span>
          <span class="news-item-title">膏方养生文化节启幕 中医建言摆脱亚健康困扰</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705912.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆9月29日电(记者 肖江川)29日，随着红荷岭右线1号拼宽桥最后一片T梁精准平稳落位，重庆武隆至两江新区高速公路(平桥至大顺段)平桥南枢纽互通439片T梁全部架设完成。作为武两高速的“起点门户”，这一节点的完成，标志着重庆高速路网向渝东南片区延伸的又一关键环节被打通。" data-title="武两高速“起点门户”打通 平桥南枢纽互通T梁架设完成" data-date="09-29 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:42</span>
          <span class="news-item-title">武两高速“起点门户”打通 平桥南枢纽互通T梁架设完成</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705894.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口9月29日电 题：新西兰少年的海南“友谊礼”：竹竿跃，锡刻韵，青春之约" data-title="新西兰少年的海南“友谊礼”：竹竿跃，锡刻韵，青春之约" data-date="09-29 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:41</span>
          <span class="news-item-title">新西兰少年的海南“友谊礼”：竹竿跃，锡刻韵，青春之约</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705899.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州9月29日电 (记者 蔡敏婕)广东省交通运输厅29日发布消息称，2026年国庆假期(10月1日至7日，共计7天)，预计高速公路车流整体保持高位运行，以景区间串联漫游、跨区域长途流转为主，同时会出现一定规模的长途自驾返乡探亲出行。" data-title="广东预计国庆假期高速公路车流整体保持高位运行" data-date="09-29 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:41</span>
          <span class="news-item-title">广东预计国庆假期高速公路车流整体保持高位运行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-29/10705904.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月29日电 (记者 陈杭)记者29日从北京市密云区获悉，北京鳌游美术馆正式开门迎客。户外广场上30余个动物装置变身“涂鸦雕塑”，近300平方米的挡墙粉刷一新化作“露天画布”，孩子们手持画笔认真涂色，描绘着自己喜爱的图案。" data-title="北京鳌游美术馆开门迎客 密云增添艺术新地标" data-date="09-29 21:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-29 21:41</span>
          <span class="news-item-title">北京鳌游美术馆开门迎客 密云增添艺术新地标</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-29 22:14（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
