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
      <span>2026-09-14 22:19 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-14/10696440.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中共中央政治局委员、外交部长王毅14日应约同法国外长巴罗通电话。" data-title="王毅同法国外长巴罗通电话" data-date="09-14 21:59" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-14 21:59</span>
      </div>
      <h2 class="hero-featured-title">王毅同法国外长巴罗通电话</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/09/14/business/tech-stocks-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在科技领导者对“前沿”人工智能技术的安全性表示担忧后，亚洲、欧洲和美国处于人工智能前沿的公司出现下滑。" data-title="人工智能领导者呼吁行业放缓后，科技股暴跌" data-date="09-14 22:15" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">人工智能领导者呼吁行业放缓后，科技股暴跌</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/audio/2026/sep/14/football-weekly-podcast-manchester-derby-var-controversy-city-united-arsenal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Max Rushden is joined by Barry Glendenning, Barney Ronay and John Brewin to discuss the weekend’s Premier League actionOn the podcast today: Max Rushden is joined by Barry Glendenning, Barney Ronay, and John Brewin to round up the weekend’s Premier League action.Manchester City beat Manchester United at Old Trafford with a controversial Erling Haal" data-title="VAR争议决定曼彻斯特德比，因为曼城与阿森纳保持同步：足球周刊" data-date="09-14 20:55" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">VAR争议决定曼彻斯特德比，因为曼城与阿森纳保持同步：足球周刊</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/09-14/10696437.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社武汉9月14日电 (记者 武一力 刘大炜 余瑞冬)作为中国传统农业大省之一的湖北省，正大力推进农业科技创新。湖北省官员14日对媒体表示，该省已稳步迈入“精准设计、性状可控”的智能育种新时代。" data-title="（活力中国）湖北智能育种成果助中国种业核心技术攻关" data-date="09-14 22:07" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">（活力中国）湖北智能育种成果助中国种业核心技术攻关</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696440.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中共中央政治局委员、外交部长王毅14日应约同法国外长巴罗通电话。" data-title="王毅同法国外长巴罗通电话" data-date="09-14 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:59</span>
          <span class="news-item-title">王毅同法国外长巴罗通电话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696435.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="金砖国家领导人第十八次会晤新德里宣言" data-title="金砖国家领导人第十八次会晤新德里宣言（全文）" data-date="09-14 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:59</span>
          <span class="news-item-title">金砖国家领导人第十八次会晤新德里宣言（全文）</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-14/10696417.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷9月14日电(记者 李映民)由泰国第五电视台、泰国中华总商会、泰国潮州会馆联合主办的泰国首届电视中秋晚会13日晚上在泰国第五电视台剧场举办。中国驻泰国大使馆参赞倪洋出席了中秋晚会，与来自泰国政、商、文化界的嘉宾一起欣赏由泰中文化人联合会担纲演出的中秋晚会。" data-title="泰国首届电视中秋晚会在曼谷举办" data-date="09-14 21:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:58</span>
          <span class="news-item-title">泰国首届电视中秋晚会在曼谷举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696404.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="行进中国｜一粒种子的“长征”——中国超级稻的三十年" data-title="一粒种子的“长征”" data-date="09-14 21:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:26</span>
          <span class="news-item-title">一粒种子的“长征”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696384.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="老挝当地时间9月14日10时许，中老“和平列车-2026”人道主义医学救援联合演习完成各项预定演练课目，在老挝万象圆满落下帷幕。" data-title="中老“和平列车-2026”人道主义医学救援联合演习圆满落幕" data-date="09-14 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:09</span>
          <span class="news-item-title">中老“和平列车-2026”人道主义医学救援联合演习圆满落幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696377.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月14日电 中国国防部长董军14日在北京八一大楼同来访的老挝副总理兼国防部长坎良举行会谈。" data-title="董军同老挝副总理兼国防部长举行会谈" data-date="09-14 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:01</span>
          <span class="news-item-title">董军同老挝副总理兼国防部长举行会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696364.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="香港上市公司万隆控股集团前行政总裁周泓，涉嫌利用职务便利虚构交易、套取公司巨额资金购置名表私用，欺诈罪名成立，14日在香港高等法院获刑十年零八个月。法庭同时下令其赔偿公司5157万港元，并禁止其担任公司董事等职务十五年。" data-title="6017万公款买名表！香港上市公司前高层被判10年8个月" data-date="09-14 20:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 20:38</span>
          <span class="news-item-title">6017万公款买名表！香港上市公司前高层被判10年8个月</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696358.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网成都9月14日电 (记者 张浪)四川省纪委监委14日消息：日前，经四川省委批准，四川省纪委监委对绵阳市政府原党组成员、副市长吴明禹严重违纪违法问题进行了立案审查调查。" data-title="四川省绵阳市政府原党组成员、副市长吴明禹严重违纪违法被开除党籍和公职" data-date="09-14 20:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 20:34</span>
          <span class="news-item-title">四川省绵阳市政府原党组成员、副市长吴明禹严重违纪违法被开除党籍和公职</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/us/politics/hegseth-pentagon-turmoil.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着美国军方面临一系列战时问题，包括导弹拦截器的短缺，持续的干扰正在助长不信任的气氛。" data-title="在黑格塞斯的五角大楼，最高领导人与动荡作战" data-date="09-14 20:22" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 20:22</span>
          <span class="news-item-title">在黑格塞斯的五角大楼，最高领导人与动荡作战</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-14/10696336.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月14日电 据英国广播公司(BBC)报道，当地时间14日，英国威尔士、苏格兰和北爱尔兰三地政党领导人在威尔士首府卡迪夫会晤并举行新闻发布会。" data-title="英国三地政党领导人会晤：“威斯敏斯特的时代即将结束”" data-date="09-14 19:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 19:55</span>
          <span class="news-item-title">英国三地政党领导人会晤：“威斯敏斯特的时代即将结束”</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cr7dl0n178do/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="朝鲜（北韩）士兵于2024年底被平壤派遣，与俄罗斯部队并肩作战，试图击退乌克兰的一次攻势。乌克兰总统泽连斯基表示，俄罗斯沃罗涅日地区正进行准备，以接收新一批朝鲜部队。" data-title="俄乌战场为何或会迎来新一批朝鲜军人" data-date="09-14 19:25" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 19:25</span>
          <span class="news-item-title">俄乌战场为何或会迎来新一批朝鲜军人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-14/10696257.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月14日电 据法新社报道，当地时间9月14日，芬兰与法国发布联合声明称，芬兰已决定加入法国总统马克龙此前提出的“前沿威慑”核计划。" data-title="芬兰决定加入法国“前沿威慑”核计划 两国发布联合声明" data-date="09-14 17:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 17:21</span>
          <span class="news-item-title">芬兰决定加入法国“前沿威慑”核计划 两国发布联合声明</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-14/10696237.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网阿斯塔纳9月14日电 (记者 单璐)哈萨克斯坦内务部14日发布消息称，哈执法人员近日在该国江布尔州捣毁一处非法大麻种植园，查获438公斤大麻及50株大麻植株，抓获一名犯罪嫌疑人。" data-title="哈萨克斯坦警方捣毁一处非法大麻种植园 查获438公斤大麻" data-date="09-14 16:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 16:56</span>
          <span class="news-item-title">哈萨克斯坦警方捣毁一处非法大麻种植园 查获438公斤大麻</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-14/10696170.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月14日电 综合日媒报道，在13日举行的日本冲绳县知事选举中，受自民党等政党支持的冲绳首府那霸市前副市长古谢玄太确定当选。" data-title="日媒：高市政权被指介入冲绳知事选举 导致现任知事落败" data-date="09-14 16:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 16:40</span>
          <span class="news-item-title">日媒：高市政权被指介入冲绳知事选举 导致现任知事落败</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-14/10696232.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月14日，也门胡塞武装称袭击了位于沙特海米斯穆谢特的空军基地。" data-title="也门胡塞武装称袭击沙特一空军基地" data-date="09-14 16:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 16:37</span>
          <span class="news-item-title">也门胡塞武装称袭击沙特一空军基地</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/business/tech-stocks-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在科技领导者对“前沿”人工智能技术的安全性表示担忧后，亚洲、欧洲和美国处于人工智能前沿的公司出现下滑。" data-title="人工智能领导者呼吁行业放缓后，科技股暴跌" data-date="09-14 22:15" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 22:15</span>
          <span class="news-item-title">人工智能领导者呼吁行业放缓后，科技股暴跌</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696414.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社杭州9月14日电 (郭其钰)中国经济社会理事会和欧盟经济社会委员会第二十一次圆桌会议14日在浙江杭州召开。中欧代表围绕“解决贫困问题，促进社会包容”“推动中欧贸易投资提质增效”“以人为本的人工智能”等议题深入交流，共话中欧合作新机遇。" data-title="第二十一次中欧圆桌会议召开 共商拓展务实合作新空间" data-date="09-14 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 22:01</span>
          <span class="news-item-title">第二十一次中欧圆桌会议召开 共商拓展务实合作新空间</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/301.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 14 日消息，据路透社报道，德国数字事务部于当地时间周一回应顶尖 AI 开发者提出的、为能力持续增强的 AI 系统设置安全防护的呼吁，称欧洲不应选择停止 AI 研发这条路。该部门一名发言人表示：“我们认为，停止研发对欧洲而言并非可行方案。”他补充说，要巩固欧洲的数字主权，就必须持续推进 AI 领域的研发与创新。此番表态的背景是，Anthropic 首席执行官达里奥 · 阿莫代伊（Dario Amodei）上周末发布长文，呼吁 AI 企业放缓模型能力迭代速度，并提议建立更严格的安全防护机制，包括在 AI 企业内部派驻独立评估人员。德国数字事务部表示，正在密切跟踪全球 AI 发展动态，并重视顶尖 AI 研发人员发出的公开风险警示。但这位发言人同时提到，如果 AI 系统能够脱离测" data-title="德国称暂停 AI 开发对欧洲而言不可行，呼吁中美参与 AI 治理" data-date="09-14 21:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 21:46</span>
          <span class="news-item-title">德国称暂停 AI 开发对欧洲而言不可行，呼吁中美参与 AI 治理</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/297.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 14 日消息，随着各界对 AI 模型发展的安全担忧不断加剧，微软于今日发布了一份长达 37 页的“人文主义 AI 行为准则”。上周末，Anthropic 首席执行官达里奥 · 阿莫代伊（Dario Amodei）呼吁各方协同放缓 AI 研发进度。此前已有研究人员发出警示：AI 模型迭代速度，可能快于人类安全部署日趋复杂系统、核验并管控 AI 智能体行为的能力。微软这份 AI 行为准则明确提出，“人比 AI 更重要”；AI 模型并不具备意识，“不应被设计成模仿意识”。微软同时反对“赋予 AI 法人资格，或是认为模型应当享有福利、拥有权利”这类观点。IT之家注意到，这一表述直接针对 AI 福利研究与模型意识相关理论，而 Anthropic 近期一直在大力推动相关方向。阿莫代伊今" data-title="微软发布 37 页人文主义 AI 行为准则：强调“人比 AI 重要”，拒绝追逐无边界超级智能" data-date="09-14 21:29" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 21:29</span>
          <span class="news-item-title">微软发布 37 页人文主义 AI 行为准则：强调“人比 AI 重要”，拒绝追逐无边界超级智能</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/994566/microsoft-humanist-ai-code-of-conduct" target="_blank" rel="noopener" data-cat="keji" data-summary="微软今天发布了一份长达37页的“人文主义人工智能行为准则” ，人们对人工智能模型进展的安全担忧与日俱增。Anthropic首席执行官Dario Amodei呼吁在周末协调减缓人工智能的发展，此前研究人员最近警告说，人工智能模型的进展可能超过我们安全部署日益复杂的系统和验证的能力。" data-title="出于安全考虑，微软表示“人比人工智能更重要”" data-date="09-14 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-14 21:00</span>
          <span class="news-item-title">出于安全考虑，微软表示“人比人工智能更重要”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/world/asia/china-ai-security-risks-anthropic.html" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管北京敦促美国不要炒作人工智能的危险，但它自己的间谍头目却将这项技术说成是对共产党安全的威胁。" data-title="中国最高间谍负责人警告人工智能是对党统治的威胁" data-date="09-14 19:14" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 19:14</span>
          <span class="news-item-title">中国最高间谍负责人警告人工智能是对党统治的威胁</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/994414/cities-ditching-flock-cameras-controversy" target="_blank" rel="noopener" data-cat="keji" data-summary="从佛罗里达州到华盛顿州，全国各地的地方政府正在取消与Flock的合同， Flock是备受争议的人工智能车牌阅读器背后的公司，以回应公众的强烈抗议。但终止合同并不一定意味着摄像头会立即关闭，或者他们收集的信息很快就会被删除。[…]" data-title="在城镇de之后会发生什么" data-date="09-14 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-14 19:00</span>
          <span class="news-item-title">在城镇de之后会发生什么</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/podcasts/the-daily/the-ai-researcher-whose-rebellion-is-changing-everything.html" target="_blank" rel="noopener" data-cat="keji" data-summary="雅各布·考克森（ Jacob Coxon ）辞去了在人类公司的工作，讨论了他对人工智能风险的担忧。" data-title="叛乱正在改变一切的人工智能研究人员" data-date="09-14 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 18:00</span>
          <span class="news-item-title">叛乱正在改变一切的人工智能研究人员</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/podcasts/the-headlines/warnings-ai-deadly-street-drug.html" target="_blank" rel="noopener" data-cat="keji" data-summary="此外，还有那个曾经去过太空却再也不想回去的人。" data-title="关于人工智能的警告不断升级，以及致命的新街头毒品的崛起" data-date="09-14 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 18:00</span>
          <span class="news-item-title">关于人工智能的警告不断升级，以及致命的新街头毒品的崛起</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/488933.html" target="_blank" rel="noopener" data-cat="keji" data-summary="让模型和设备共同进化" data-title="端侧AI从“能跑”到“会进化”，元空智能跑进惠普预装" data-date="09-14 16:08" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-14 16:08</span>
          <span class="news-item-title">端侧AI从“能跑”到“会进化”，元空智能跑进惠普预装</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/488912.html" target="_blank" rel="noopener" data-cat="keji" data-summary="险资、券商与头部创投持续加码" data-title="一年连融三轮，这家金融AI公司又拿下超3亿B轮" data-date="09-14 15:55" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-14 15:55</span>
          <span class="news-item-title">一年连融三轮，这家金融AI公司又拿下超3亿B轮</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-14/10696148.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="2026年国家网络安全宣传周开幕式于9月14日在山东济南举行。《人工智能安全治理框架》3.0、《2026年人工智能技术赋能网络安全应用测试结果》、消费类网联摄像头网络安全标识备案产品等一系列网络安全领域重要成果在开幕式上发布。" data-title="2026年国家网络安全宣传周开幕" data-date="09-14 15:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 15:08</span>
          <span class="news-item-title">2026年国家网络安全宣传周开幕</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/091.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 14 日消息，小米集团合伙人、总裁卢伟冰今日发文谈到了米家品牌。他提到，2016 年小米创立米家品牌，正式进入家电行业。科技家电的未来是主动智能，这也是米家下一个十年，要走的路。未来，会有更多“懂事”的米家产品和大家见面。他表示，家电从能联网、能 App 控制，到能语音、能 AI 交互，“让家电听话”这件事，行业已经做到了极致。但说句实话，再听话，本质还是“遥控器”一-你说一句，它做一件。距离真正的主动智能，还有不小距离。今年上半年，小米研发投入超过 180 亿元。一批硬核技术，开始集中从实验室走进市场：Xiaomi MiMo 大模型累计调用突破一万亿词元，玄戒三芯齐发、撑起人车家全生态的算力底座，IoT 全球设备连接数突破 11 亿。模型、算力、生态，把地基打好了。也正是" data-title="小米卢伟冰：科技家电的未来是主动智能，也是米家下一个十年要走的路" data-date="09-14 15:03" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 15:03</span>
          <span class="news-item-title">小米卢伟冰：科技家电的未来是主动智能，也是米家下一个十年要走的路</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/090.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 14 日消息，OpenAI 首席执行官萨姆 · 奥尔特曼（Sam Altman）于当地时间上周日表态，支持对人工智能的发展采取“控速”思路，避免尖端模型的能力发展速度超出人类可控范围。奥尔特曼的表述与 Anthropic 首席执行官达里奥 · 阿莫迪（Dario Amodei）的观点相近。他称，将工作重心转向安全会付出一定代价，但此举有助于维持外界信心，证明美国企业在研发能力日益强大的人工智能时恪守责任，这份代价值得承担。“无论美国面临多大的竞争压力，都不能成为鲁莽行事的理由，也不能让模型能力的发展领先于对齐技术与监管监测。”这位 OpenAI 负责人在 X 平台发帖写道。他同时强调，保障安全并不等同于停止技术进步：“我们所说的‘控速’，并不是‘叫停’。”IT之家注意到，就" data-title="OpenAI CEO 奥尔特曼支持控制 AI 发展速度，强调并非停止技术进步" data-date="09-14 15:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 15:01</span>
          <span class="news-item-title">OpenAI CEO 奥尔特曼支持控制 AI 发展速度，强调并非停止技术进步</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/087.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 14 日消息，TrendForce（集邦）今日表示，NOR 闪存市场正经历近十年来最重要的供需结构转变。该领域在 2026 年下半年的按容量计产能增幅有限，高容量产品价格可能会再度翻倍成长。机构认为，尽管相关供应商皆已提高资本支出并扩产，但新增产能必须经过制程微缩、良率爬坡、产品验证以及纳入客户规格、设计导入等流程，无法立即转化为市场可用供给，因此，短期内中高容量市场的缺口仍无法获得满足。除传统的汽车 ADAS、数字座舱与工业控制外，人工智能与航天通信正成为新的 NOR 需求主力。AI 服务器的 NOR 需求显著高于传统服务器，大量重定时器 (Retimer) 都需要配套 NOR；另一方面，NOR 也非常适合航天通信产业对高可靠性存储介质的需求。▲ 图源：TrendForc" data-title="TrendForce 预测：NOR 闪存增产有限，高容量产品价格 2026H2 恐翻倍" data-date="09-14 14:59" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 14:59</span>
          <span class="news-item-title">TrendForce 预测：NOR 闪存增产有限，高容量产品价格 2026H2 恐翻倍</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/audio/2026/sep/14/football-weekly-podcast-manchester-derby-var-controversy-city-united-arsenal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Max Rushden is joined by Barry Glendenning, Barney Ronay and John Brewin to discuss the weekend’s Premier League actionOn the podcast today: Max Rushden is joined by Barry Glendenning, Barney Ronay, and John Brewin to round up the weekend’s Premier League action.Manchester City beat Manchester United at Old Trafford with a controversial Erling Haal" data-title="VAR争议决定曼彻斯特德比，因为曼城与阿森纳保持同步：足球周刊" data-date="09-14 20:55" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-14 20:55</span>
          <span class="news-item-title">VAR争议决定曼彻斯特德比，因为曼城与阿森纳保持同步：足球周刊</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmg49n3g7exlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳将就Ezri Konsa在周六击败桑德兰的比赛中承认点球的事件联系裁判机构职业裁判。" data-title="Arsenal将就Konsa罚款问题联系专业参考" data-date="09-14 19:31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 19:31</span>
          <span class="news-item-title">Arsenal将就Konsa罚款问题联系专业参考</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq6384g0pqyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当天比赛专家丹尼·墨菲（ Danny Murphy ）解释了曼城如何在老特拉福德击败曼联，尽管在比赛的大部分时间里只剩下10名男子。" data-title="马雷斯卡曼城的情报和复原力关键陈述胜利" data-date="09-14 06:20" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 06:20</span>
          <span class="news-item-title">马雷斯卡曼城的情报和复原力关键陈述胜利</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/13/mikel-arteta-arsenal-sunderland-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="由于阿森纳经理帮助创建的微观分析文化，裁判现在是一项不可能的工作。绅士绝不会无意中粗鲁，只有设计。没有人真正知道是谁先说的。但它可以很容易地从精英足球经理指南到新闻发布会（英超联赛版）。因为在这些空间中没有意外发生。在广告中覆盖的板子前面说的每一个字都是" data-title="Arteta拥抱完美风暴，在自己制作的游戏中扮演受害者| Barney Ronay" data-date="09-14 04:35" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-14 04:35</span>
          <span class="news-item-title">Arteta拥抱完美风暴，在自己制作的游戏中扮演受害者| Barney Ronay</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5ym9ky3rzxo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛裁判机构Pro Ref承认在授予Erling Haaland的曼彻斯特德比冠军时存在判断错误。" data-title="裁判机构承认对哈兰德德比冠军的判断错误" data-date="09-14 04:29" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 04:29</span>
          <span class="news-item-title">裁判机构承认对哈兰德德比冠军的判断错误</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c624d3g15e9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日的德比之前，曼联球迷在老特拉福德内外抗议，然后看到他们的球队输给了10人曼城" data-title="联合-自1992年以来最糟糕的开局和球迷抗议-曼联难忘的一天" data-date="09-14 03:54" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 03:54</span>
          <span class="news-item-title">联合-自1992年以来最糟糕的开局和球迷抗议-曼联难忘的一天</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c4g7pezw1mjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在连续第四次失利后，考文垂市重返英超联赛的梦想开始破灭-但弗兰克·兰帕德能扭转局面吗？" data-title="等待25年-考文垂的噩梦顶级航班回程" data-date="09-14 03:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 03:32</span>
          <span class="news-item-title">等待25年-考文垂的噩梦顶级航班回程</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/13/manchester-united-v-manchester-city-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Erling Haaland有争议的进球为曼城带来了巨大的胜利，在Phil Foden的早期红牌之后，他打得非常出色布莱顿的第四个进球是所有人中刘易斯·扣篮的尖叫声，促使史蒂夫·布拉德菲尔德发了这封电子邮件。布莱顿的第四个进球是本月进球的扣篮吗？继续阅读..." data-title="曼联0-1曼城：英超联赛–实际情况" data-date="09-14 02:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-14 02:16</span>
          <span class="news-item-title">曼联0-1曼城：英超联赛–实际情况</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/13/manchester-united-manchester-city-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“恩佐，恩佐，恩佐，在你的脑海中”是曼城球迷对恩佐·费尔南德斯（ Enzo Fernández ）的狂热追求，他在令人难忘的胜利中扮演明星角色后，立即获得了邪教英雄地位。第199场德比赛由Erling Haaland在比赛中的第九次罢工赢得，但游客的图腾是他们新的第17号。视频助理裁判在裁定费尔南德斯没有分散注意力时推翻了一个最初因越位而被排除在外的进球，他是其中的关键人物。" data-title="曼城从福登红牌中恢复过来，哈兰德在曼联赢得德比" data-date="09-14 01:32" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-14 01:32</span>
          <span class="news-item-title">曼城从福登红牌中恢复过来，哈兰德在曼联赢得德比</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c2kwpk5zy23o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和曼城球员在老特拉福德德比赛中的得分情况。" data-title="Foden看到Mainoo印象深刻的红色-曼彻斯特德比评级" data-date="09-14 01:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 01:27</span>
          <span class="news-item-title">Foden看到Mainoo印象深刻的红色-曼彻斯特德比评级</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/13/manchester-united-v-manchester-city-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽️ 曼彻斯特德比从英国夏令时下午4:30⚽️开始的更新帮助布莱顿击败考文垂|今天的分数布莱顿的第四个进球是所有人中刘易斯·扣篮的尖叫声，促使史蒂夫·布拉德菲尔德发来这封电子邮件。布莱顿的第四个进球是本月进球的扣篮吗？继续阅读..." data-title="曼联v曼城：英超联赛" data-date="09-14 00:31" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-14 00:31</span>
          <span class="news-item-title">曼联v曼城：英超联赛</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c624d3g15e9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日的德比之前，曼联球迷在老特拉福德内外抗议。" data-title="曼联在德比之前抗议所有权" data-date="09-14 00:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-14 00:16</span>
          <span class="news-item-title">曼联在德比之前抗议所有权</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/13/coventry-brighton-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="裸露的统计数据是黯淡的：考文垂城是英超历史上第二支在本赛季的前四场比赛中没有得分的球队。“然而……”将是弗兰克·兰帕德（ Frank Lampard ）的持久信息。然而，他们给反对派队伍带来了麻烦--即使在对阵布莱顿的比赛中只有10人。然而，他们已经面对过三支顶级欧洲队伍。然而，它们并没有发挥作用" data-title="Lewis Dunk的表演主角帮助五星级布莱顿击败了10人考文垂" data-date="09-13 23:10" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 23:10</span>
          <span class="news-item-title">Lewis Dunk的表演主角帮助五星级布莱顿击败了10人考文垂</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696437.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社武汉9月14日电 (记者 武一力 刘大炜 余瑞冬)作为中国传统农业大省之一的湖北省，正大力推进农业科技创新。湖北省官员14日对媒体表示，该省已稳步迈入“精准设计、性状可控”的智能育种新时代。" data-title="（活力中国）湖北智能育种成果助中国种业核心技术攻关" data-date="09-14 22:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 22:07</span>
          <span class="news-item-title">（活力中国）湖北智能育种成果助中国种业核心技术攻关</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696447.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网温州9月14日电(周健)“我们期待以此次培训为契机，推动风险管理更好地融入各国导助航规划布局和管理服务，为导助航事业安全、高效、可持续发展提供有力支撑。”9月14日，2026年国际海上导助航风险管理培训班在浙江温州开班，东海航海保障中心副主任吴宇晓在开班致辞时说。" data-title="全球业界人士浙江温州探讨导助航风险 提升航行安全性" data-date="09-14 22:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 22:06</span>
          <span class="news-item-title">全球业界人士浙江温州探讨导助航风险 提升航行安全性</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696432.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月14日电(张煜欢 孙杨洋)依托AI数字技术，抗美援朝老兵杨礼渊拥有了一份独一无二的“数字回忆录”。通过影像复原、数字人建模、场景复刻等方式，这位93岁老兵的峥嵘岁月被生动还原，尘封的军旅记忆得以鲜活留存，让老人深受触动。" data-title="AI重现烽火记忆 九旬老兵收获专属“数字回忆录”" data-date="09-14 22:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 22:06</span>
          <span class="news-item-title">AI重现烽火记忆 九旬老兵收获专属“数字回忆录”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696418.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月14日电 (记者 李京泽)“区域国别学·北京论坛2026”于9月13日在北京会议中心开幕。本届论坛由北京第二外国语学院(以下简称“二外”)主办。" data-title="“区域国别学·北京论坛2026”举办" data-date="09-14 22:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 22:06</span>
          <span class="news-item-title">“区域国别学·北京论坛2026”举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696416.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月14日电 “万象在经纬之间 WEAVE THE MIXC”日前在杭州万象城正式启幕。这是香港故宫文化博物馆与杭州万象城共同发起的城市文化项目。" data-title="文化遗产织入都市生活 文化项目“万象在经纬之间”启幕" data-date="09-14 22:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 22:05</span>
          <span class="news-item-title">文化遗产织入都市生活 文化项目“万象在经纬之间”启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696394.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海南保亭9月14日电 (文宏武)据海南保亭黎族苗族自治县防灾减灾救灾委员会14日消息，受热带低压与冷空气共同叠加影响，保亭出现持续性强降雨天气，降雨历时久、覆盖范围广、累积雨量大、局地强度极端，引发山体滑坡、道路损毁、河水漫溢、房屋积水等多重险情，全县防汛防地质灾害形势极为严峻。" data-title="持续强降雨侵袭海南保亭 引发山体滑坡等多重险情" data-date="09-14 21:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:55</span>
          <span class="news-item-title">持续强降雨侵袭海南保亭 引发山体滑坡等多重险情</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/14/a-vinyl-bar-in-shibuya-is-a-startup-offering-fun-music-apps-without-any-ai-prompting/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="前Spotify高管的公司发布了涉及音乐制作用户的实验性“单曲”。" data-title="涩谷的一家黑胶唱片酒吧是一家初创公司，在没有任何AI提示的情况下提供有趣的音乐应用程序" data-date="09-14 21:55" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-14 21:55</span>
          <span class="news-item-title">涩谷的一家黑胶唱片酒吧是一家初创公司，在没有任何AI提示的情况下提供有趣的音乐应用程序</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/303.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 14 日消息，小米官方今日透露，截至目前，小米澎程 N90 Max 探索版展车已进入全国 108 个城市的 291 个门店，并公布具体门店（附文末）。IT之家注意到，小米澎程系列于 9 月 7 日晚发布，4 分钟锁单突破 10,000 台。新车包含小米澎程 N70 Pro、N70 Max、N90 Max、N90 Max 探索版四款车型，小米澎程 N70 Pro 售价 20.99 万元；小米澎程 N70 Max 售价 23.99 万元；小米澎程 N90 Max 售价 26.99 万元；小米澎程 N90 Max 探索版售价 29.99 万元。小米澎程 N70 Pro 定位“中大型五座增程 SUV”，拥有经典豪华 SUV 车身比例：车长 4960mm、宽 1998mm、轴距 29" data-title="小米澎程 N90 Max 探索版展车已进入全国 108 个城市的门店" data-date="09-14 21:54" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 21:54</span>
          <span class="news-item-title">小米澎程 N90 Max 探索版展车已进入全国 108 个城市的门店</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696424.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川9月14日电 (记者 杨迪)9月14日，2026年宁夏药品安全宣传周活动暨法治大课堂在银川举行。" data-title="2026年宁夏药品安全宣传周活动启动" data-date="09-14 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:54</span>
          <span class="news-item-title">2026年宁夏药品安全宣传周活动启动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-14/10696422.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网固原9月14日电 (记者 李佩珊)秋雨初歇，六盘山山间薄雾氤氲，红色氛围浓厚。9月14日，宁夏固原市隆德县3000余名师生齐聚六盘山红军长征纪念馆前，集体诵读《清平乐·六盘山》。本次诵读活动作为第四届六盘山红色文化旅游节的配套预热活动，以沉浸式红色体验，提前点燃节会氛围。" data-title="（长征胜利90周年）宁夏隆德3000余名师生诵经典 赓续六盘山红色文脉" data-date="09-14 21:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-14 21:51</span>
          <span class="news-item-title">（长征胜利90周年）宁夏隆德3000余名师生诵经典 赓续六盘山红色文脉</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/994596/musk-documentary-review-tiff-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="马斯克是一部长片，这是有道理的。亚历克斯·吉布尼（ Alex Gibney ）曾执导过关于Theranos和史蒂夫·乔布斯（ Steve Jobs ）的纪录片，他的最新作品令人印象深刻地重述了埃隆·马斯克（ Elon Musk ）的故事，从他早期的互联网百万富翁到“带着木屑”到美国重要的政府部门。按顺序[…]" data-title="长达四个小时的伊隆·马斯克（ Elon Musk ）纪录片可能正在向合唱团讲道" data-date="09-14 21:50" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-14 21:50</span>
          <span class="news-item-title">长达四个小时的伊隆·马斯克（ Elon Musk ）纪录片可能正在向合唱团讲道</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/300.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 14 日消息，据三名被裁员员工以及一封发给 Business Insider 的邮件显示，甲骨文公司已经开启新一轮裁员。一名知情人士透露，本轮裁员定于当地时间周一开始。Business Insider 上月曾报道，甲骨文为筹措资金建设 AI 基础设施，背负了巨额债务，为此制定了新一轮裁员计划以缩减人力开支。一份内部文件显示，部分团队的裁员比例达到两位数。当地时间周一，领英、Reddit 以及职场匿名社区 Blind 上陆续出现帖子，发帖人称自己在本次裁员中受到波及。本轮裁员是甲骨文继今年早些时候裁员之后的又一轮缩减动作。最新提交的文件显示，在截至 5 月 31 日的 2026 财年，甲骨文员工总数减少 2.1 万人，降幅 13%。该公司称，本轮裁员前，员工数量约为 14.1" data-title="消息称甲骨文启动新一轮裁员，部分团队裁员比例达两位数" data-date="09-14 21:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 21:40</span>
          <span class="news-item-title">消息称甲骨文启动新一轮裁员，部分团队裁员比例达两位数</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/002/298.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 14 日消息，广汽昊铂埃安 BU 总裁张雄今日在社交媒体上公布了 2027 款埃安 i60 更多配置信息，9 月 15 日正式上市。2027 款埃安 i60 与在售车型基本保持一致，新车中控屏从现款车型的 14.6 英寸升级为 15.6 英寸 2.5k 中控屏，配备前备箱，搭载可承重铝合金行李架，纯电版搭载非晶电驱，CLTC 续航提升到 700 公里。据此前公布信息，这款汽车将搭载 192 线激光雷达，拥有 L4 同源一段式端到端算法，辅助驾驶能力相比现款型号进一步增强，车身尺寸为 4685×1854×1660mm，轴距 2775mm。该车号称是全球最长续航增程车，超级增程综合续航达 1738km，纯电续航达 350km。▲ 在售广汽埃安 AION i60IT之家注意到，在" data-title="全球最长续航增程车，2027 款广汽埃安 i60 更多信息公布" data-date="09-14 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-14 21:32</span>
          <span class="news-item-title">全球最长续航增程车，2027 款广汽埃安 i60 更多信息公布</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/science/ai-bioweapons.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="专家说，目前的聊天机器人不太可能帮助单个演员发明一种致命的病原体。但是，经过生物学训练的新模型可能需要更强的保护措施。" data-title="人工智能是否增加了生物战的可能性？" data-date="09-14 20:54" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 20:54</span>
          <span class="news-item-title">人工智能是否增加了生物战的可能性？</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/14/climate/global-warming-limit-paris-climate-agreement.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着全球气温上升超过1.5摄氏度，为实现《巴黎协定》目标而战的脆弱国家面临着一个残酷的新现实。" data-title="全球变暖将突破1.5摄氏度的极限。现在该怎么办？" data-date="09-14 20:26" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-14 20:26</span>
          <span class="news-item-title">全球变暖将突破1.5摄氏度的极限。现在该怎么办？</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-14 22:19（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
