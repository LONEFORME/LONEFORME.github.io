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
      <span>2026-09-10 14:44 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar" style="margin: 12px 0 8px; display: flex; align-items: center; gap: 8px; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.2); border-radius: 8px; padding: 7px 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity: 0.65;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)" style="flex: 1; background: transparent; border: none; outline: none; color: inherit; font-size: 13px;">
    <span id="news-search-count" style="font-size: 12px; opacity: 0.7; font-weight: 500;"></span>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">47</span>
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
        <span class="channel-count">2</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-10/10693926.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月10日电 题：中国式现代化对中拉人权合作有何启示？" data-title="东西问丨巴西学者：中国式现代化对中拉人权合作有何启示？" data-date="09-10 14:30" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-10 14:30</span>
      </div>
      <h2 class="hero-featured-title">东西问丨巴西学者：中国式现代化对中拉人权合作有何启示？</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/000/732.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，据中国汽车工业协会分析，8 月，多地汽车消费补贴持续升级，车企促销活动活跃，汽车产销环比增长、同比小幅下降。其中，国内市场继续承压，月度销量同比降幅连续 5 个月超过 20%；出口保持高速增长，月度出口量连续 3 个月超过 100 万辆，成为稳定行业大盘的关键增量；新能源汽车主导地位持续巩固，月度销量占比再创新高。中汽协数据显示，8 月汽车国内销量完成 170.1 万辆，环比增长 10.4%，同比下降 24.2%。其中，传统燃料汽车国内销量 58.4 万辆，环比增长 9.4%，同比下降 45.7%。我国新能源汽车主导地位持续巩固，成为稳定行业大盘的关键增量。数据显示，新能源汽车月度销量占比再创新高，8 月份，新能源汽车产销量分别完成 165.3 万辆和 164" data-title="中汽协：8 月汽车国内销量环比增长 10.4%，同比下降 24.2%" data-date="09-10 14:41" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">中汽协：8 月汽车国内销量环比增长 10.4%，同比下降 24.2%</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c3v4379d4ylo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚历克西斯·麦克·阿利斯特(Alexis Mac Allister)对他在利物浦的合同的公开评论存在分歧，球迷和BBC体育评论员帕特·内文(Pat Nevin)分享了意见。" data-title="“说得很精彩”，但利物浦球迷对麦克·阿利斯特的合同评论感到不满" data-date="09-09 23:07" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">“说得很精彩”，但利物浦球迷对麦克·阿利斯特的合同评论感到不满</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/09-10/10693945.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如今，徒步、登山等户外休闲活动备受追捧，社交媒体上不少标注“宝藏”的网红徒步攻略热度很高，但这样的攻略背后往往暗藏安全隐患。前不久，北京一名女子就依照一条网红徒步攻略出行，不料遭遇意外。" data-title="女子按网红徒步攻略出行遭意外 户外出游遇险谁担责？" data-date="09-10 14:38" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">女子按网红徒步攻略出行遭意外 户外出游遇险谁担责？</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-10/10693926.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月10日电 题：中国式现代化对中拉人权合作有何启示？" data-title="东西问丨巴西学者：中国式现代化对中拉人权合作有何启示？" data-date="09-10 14:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 14:30</span>
          <span class="news-item-title">东西问丨巴西学者：中国式现代化对中拉人权合作有何启示？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-10/10693935.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网桂林9月10日电 题：影片出品人荣斌：将湘江战役的历史重新带回观众面前" data-title="（长征胜利90周年）影片出品人荣斌：将湘江战役的历史重新带回观众面前" data-date="09-10 14:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 14:27</span>
          <span class="news-item-title">（长征胜利90周年）影片出品人荣斌：将湘江战役的历史重新带回观众面前</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693870.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月10日电 德黑兰消息：当地时间9日，伊朗多名官员发文批评国际原子能机构理事会当天表决通过的伊朗核问题决议，该决议主张将相关伊核问题提交至联合国安理会。" data-title="伊朗驳斥国际原子能机构理事会通过的伊核决议" data-date="09-10 14:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 14:15</span>
          <span class="news-item-title">伊朗驳斥国际原子能机构理事会通过的伊核决议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-10/10693907.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="广西壮族自治区主席韦韬赴京“带货”：吃“三碗粉”才算优秀；现场切开168斤合浦大月饼，“祝大家中秋快乐”" data-title="广西壮族自治区主席韦韬赴京“带货”：吃“三碗粉”才算优秀" data-date="09-10 13:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 13:40</span>
          <span class="news-item-title">广西壮族自治区主席韦韬赴京“带货”：吃“三碗粉”才算优秀</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/10/us/politics/trump-dividend-5000-dollar-checks.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统在大会演讲中提出，如果共和党继续控制国会，将为每个成年美国人提供 5,000 美元的“特朗普红利”。与许多其他想法一样，这个想法可能不会实现。" data-title="如果共和党赢得中期选举，特朗普将发放 5,000 美元的“特朗普股息”支票" data-date="09-10 13:35" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 13:35</span>
          <span class="news-item-title">如果共和党赢得中期选举，特朗普将发放 5,000 美元的“特朗普股息”支票</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/10/us/politics/trump-republican-convention-speech-takeaways.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一场史无前例的中期大会上，特朗普总统大多表示了重述和自我祝贺。然后，他提出如果共和党继续掌权，将向美国人每人支付 5,000 美元。" data-title="“假装我正在竞选”：共和党的 7 个要点中期大会" data-date="09-10 13:22" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 13:22</span>
          <span class="news-item-title">“假装我正在竞选”：共和党的 7 个要点中期大会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-10/10693864.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月10日电 据“市说新语”微信公众号消息，9月10日上午，由市场监管总局与世界知识产权组织共同主办的第二届知识产权执法国际交流大会在湖南省长沙市开幕。市场监管总局副局长白清元、世界知识产权组织助理总干事爱德华·夸夸、湖南省副省长蒋涤非出席会议并致辞。" data-title="第二届知识产权执法国际交流大会在长沙开幕" data-date="09-10 12:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 12:24</span>
          <span class="news-item-title">第二届知识产权执法国际交流大会在长沙开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-10/10693868.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="全国首个外籍人员入境综合保险保障产品今天(10日)在北京发布，这个保险产品聚焦外籍人员短期入境的实际需求，一次投保可享受多种保障服务。" data-title="全国首个外籍人员入境综合保险保障产品在北京发布" data-date="09-10 12:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 12:24</span>
          <span class="news-item-title">全国首个外籍人员入境综合保险保障产品在北京发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693846.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月10日电 综合外媒报道，当地时间9日，美国总统特朗普承诺，如果共和党在2026年11月的中期选举中成功保住对国会的控制权，将向每位美国成年人发布5000美元的“红利”。" data-title="特朗普：若共和党赢得中期选举，将向每位美国成年人发5000美元“红利”" data-date="09-10 11:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 11:55</span>
          <span class="news-item-title">特朗普：若共和党赢得中期选举，将向每位美国成年人发5000美元“红利”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693819.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月10日电(记者 刁炜)近日，胡塞武装发射导弹连续袭击了受沙特支持的也门政府军目标，摧毁对手多辆装甲车及货运卡车。" data-title="无人机“现场直播”，胡塞武装发射导弹精准打击对手" data-date="09-10 11:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 11:13</span>
          <span class="news-item-title">无人机“现场直播”，胡塞武装发射导弹精准打击对手</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693780.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月10日电 大马士革消息：当地时间9日，叙利亚西北部伊德利卜省一处存放武器和战争遗留物的临时仓库发生爆炸，造成至少14人死亡。" data-title="叙利亚一武器仓库爆炸 至少14人死亡" data-date="09-10 11:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 11:11</span>
          <span class="news-item-title">叙利亚一武器仓库爆炸 至少14人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693756.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网柏林9月10日电 (记者 马秀秀)德国总理、基督教民主联盟主席弗里德里希·默茨9日在联邦议院表示，德国选择党虽然在萨克森-安哈尔特州议会选举中获胜，但未能取得绝对多数。凭借现有政策，选择党在德国任何地方都不可能获得绝对多数支持。" data-title="德国总理默茨：选择党不可能获得绝对多数支持" data-date="09-10 11:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 11:00</span>
          <span class="news-item-title">德国总理默茨：选择党不可能获得绝对多数支持</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/09/us/politics/john-fetterman-trump-republican-convention.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="与自己的政党关系疏远的参议员约翰·费特曼出现在钢铁厂前拍摄的一段短片中，称他“永远会拒绝社会主义的极端”。" data-title="费特曼在特朗普大会上出人意料地客串" data-date="09-10 09:48" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 09:48</span>
          <span class="news-item-title">费特曼在特朗普大会上出人意料地客串</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/09/us/politics/election-officials-confusion-mail-ballots.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当他们等待特朗普政府的新选票系统是否可以推进的消息时，当地官员表示他们已经没有时间了。" data-title="最高法院考虑邮寄投票计划，选举官员努力应对不确定性" data-date="09-10 09:29" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 09:29</span>
          <span class="news-item-title">最高法院考虑邮寄投票计划，选举官员努力应对不确定性</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/09/us/politics/trump-census-immigrants-race.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2030 年的提案是重大变化之一，这些变化将颠覆帮助分配国会席位和制定解决不平等问题的政策的程序。" data-title="特朗普的人口普查改革将排除一些移民并消除种族问题" data-date="09-10 08:21" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 08:21</span>
          <span class="news-item-title">特朗普的人口普查改革将排除一些移民并消除种族问题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/000/732.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，据中国汽车工业协会分析，8 月，多地汽车消费补贴持续升级，车企促销活动活跃，汽车产销环比增长、同比小幅下降。其中，国内市场继续承压，月度销量同比降幅连续 5 个月超过 20%；出口保持高速增长，月度出口量连续 3 个月超过 100 万辆，成为稳定行业大盘的关键增量；新能源汽车主导地位持续巩固，月度销量占比再创新高。中汽协数据显示，8 月汽车国内销量完成 170.1 万辆，环比增长 10.4%，同比下降 24.2%。其中，传统燃料汽车国内销量 58.4 万辆，环比增长 9.4%，同比下降 45.7%。我国新能源汽车主导地位持续巩固，成为稳定行业大盘的关键增量。数据显示，新能源汽车月度销量占比再创新高，8 月份，新能源汽车产销量分别完成 165.3 万辆和 164" data-title="中汽协：8 月汽车国内销量环比增长 10.4%，同比下降 24.2%" data-date="09-10 14:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:41</span>
          <span class="news-item-title">中汽协：8 月汽车国内销量环比增长 10.4%，同比下降 24.2%</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/731.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，据外媒 Nintendo Life 今天报道，任天堂现已为 Switch 2 游戏机推送 23.0.0 固件更新。本次更新最大的变化是为主机模式增加 VRR（IT之家注：可变刷新率）支持。据报道，本次更新让 Switch 2 能够支持电视模式的 VRR 输出。当游戏软件和电视 / 显示器支持 VRR 时，画面将以游戏相匹配的帧率显示。若要启用该功能，用户需更新 Switch 2 底座。同时，本次更新还在显示设置内新增了视频输出信息，用户可查看电视机支持的分辨率、刷新率。Mii 编辑界面新增背景音乐，掌机模式增强现可在快速设置菜单中一键启动。此外，本次更新还能让两台 Switch 2 主机之间进行完整数据传输，用户可将存档、截图等所有数据，从旧 Switch 2" data-title="任天堂 Switch 2 游戏机获 23.0.0 固件更新，解锁主机模式 VRR" data-date="09-10 14:40" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:40</span>
          <span class="news-item-title">任天堂 Switch 2 游戏机获 23.0.0 固件更新，解锁主机模式 VRR</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/730.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，新华社今日发文报道了小米玄戒三芯、小米澎程系列新车的发布，称底层技术自研打开科技创新空间。小米创办人、董事长兼 CEO 雷军随后发文回应：感谢认可！技术为本，这是小米永不更改的铁律。在硬核科技上，我们会持续加大研发投入。未来 5 年，我们计划投入 2000 亿元研发费用。据IT之家此前报道，在 8 月 24 日的小米玄戒芯片技术沟通会上，新一代玄戒芯片“三芯齐发”，包括：玄戒 O3，AI 旗舰 SoC，安兔兔首破 500 万玄戒 O100，1.22TB/s 高带宽 AI 加速芯片玄戒 D100，国内首款 3nm 智驾高算力 AI 芯片雷军透露，SoC 和基带双线突破的背后，是小米死磕底层技术的决心。小米重启大芯片研发，已经五年多的时间了，累计投入的研发经费超过" data-title="雷军回应新华社报道小米“底层技术自研打开科技创新空间”：未来 5 年，计划投入 2000 亿元研发费用" data-date="09-10 14:35" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:35</span>
          <span class="news-item-title">雷军回应新华社报道小米“底层技术自研打开科技创新空间”：未来 5 年，计划投入 2000 亿元研发费用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/726.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，一张启境 GX7 媒体群的群聊截图最近在网络平台传播。图片显示，昵称为“小助手”的工作人员在群聊中发布了“小米澎程攻防”相关内容。随后，该群聊被解散。启境汽车官方刚刚针对此事发布说明，IT之家附原文如下：关于媒体群误发信息的说明大家好！这两天，一条内部工作信息被误发到媒体群，引发了不少讨论。对此，我们不回避：相关工作人员操作失误，发现后又因处置仓促解散了群。关注市场、了解行业信息是新品上市前的常规工作，截图中的“攻防”，是内部对同期产品进行信息监测、差异梳理和事实核验的工作用语，并非策划攻击、拉踩友商。但这个词用得不妥，误发和解散群的处理也不专业。给大家添麻烦了，跟各位说声抱歉。我们会认真复盘，改进管理。该说明的，我们不回避；该做好的，还是产品。9 月 4 日" data-title="启境汽车回应媒体群误发“小米澎程攻防”相关内容：并非策划攻击、拉踩友商" data-date="09-10 14:18" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:18</span>
          <span class="news-item-title">启境汽车回应媒体群误发“小米澎程攻防”相关内容：并非策划攻击、拉踩友商</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/725.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，科技媒体 cultofmac 今天（9 月 10 日）发布博文，报道称苹果公司面向符合条件的 iPhone 14 系列、iPhone 15 系列以及 iPhone 16 系列用户，再次延长免费卫星服务 1 年，是自 2023 年 9 月在 iPhone 14 Pro 上推出该功能以来，苹果第三次扩展免费卫星连接功能。截取自苹果美国官网信息，无白色背景IT之家附上苹果官方更新内容如下：在蜂窝网络和 Wi-Fi 覆盖范围之外，Apple 的突破性卫星功能可帮助 iPhone 18 Pro 和 iPhone 18 Pro Max 用户保持连接，并在最需要的时候获得帮助。Apple 将为现有的 iPhone 14、iPhone 15 和 iPhone 16 用户免费延" data-title="第三次拓展：美版苹果 iPhone 14 系列等免费卫星访问服务再延长 1 年" data-date="09-10 14:15" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:15</span>
          <span class="news-item-title">第三次拓展：美版苹果 iPhone 14 系列等免费卫星访问服务再延长 1 年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693927.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="总台记者获悉，挪威首相当地时间9月9日表示，一架无人机差点击中乌克兰总统泽连斯基所乘坐的从摩尔多瓦前往挪威奥斯陆的飞机。挪威首相没有透露该信息的来源，也没有说明无人机距离飞机有多近。" data-title="挪威首相称泽连斯基所乘飞机“差点被无人机击中”" data-date="09-10 14:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 14:15</span>
          <span class="news-item-title">挪威首相称泽连斯基所乘飞机“差点被无人机击中”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/723.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，有网友今日拍摄到北京新浪总部大楼附近发生火情，现场冒出滚滚浓烟，引发关注。对此，微博 CEO 王高飞回应称：隔壁一个什么厂房着火了，新浪行政水军去帮消防灭火去了，已经灭了。IT之家注意到，北京海淀消防今日发布警情通报，2026 年 9 月 10 日 11 时 53 分，119 指挥中心接到报警，海淀区马连洼街道一废弃平房内杂物起火。指挥中心迅速调派附近消防救援力量到场处置。12 时 05 分，火灾扑灭，无人员被困伤亡。" data-title="微博 CEO 王高飞辟谣“总部着火”：隔壁一个厂房起火" data-date="09-10 14:08" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:08</span>
          <span class="news-item-title">微博 CEO 王高飞辟谣“总部着火”：隔壁一个厂房起火</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/722.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 10 日消息，苹果 iPhone 18 Pro Max（对应 iPhone19,2 和 iPhone19,3）已经出现在了 Geekbench 基准测试数据库中，A20 Pro 性能可见一斑（IT之家提醒：样本太少，不具备可比性）。苹果 A20 Pro 采用六核 CPU 设计，频率可达 4.93GHz。这款新机配备 12GB 内存，在 Geekbench 6.7.0 上单核得分 4719 分，多核得分 12677 分，Metal 图形测试得分 64069 分。据苹果官方介绍，A20 Pro 芯片采用新一代 2nm 制程工艺打造，具备 6 核 CPU，其中 2 个性能核心较上一代强 20%，另有 4 个能效核心；新 GPU 为 7 核设计，相比 A19 Pro 提升最高达 4" data-title="A20 Pro 跑分首曝：苹果 iPhone 18 Pro Max 现身 Geekbench，搭载 12GB 内存" data-date="09-10 14:07" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:07</span>
          <span class="news-item-title">A20 Pro 跑分首曝：苹果 iPhone 18 Pro Max 现身 Geekbench，搭载 12GB 内存</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwyzp5561n2o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="新款iPhone采用书本式的折叠设计，命名为Duo，是历来最大尺寸的版本，也是最贵的型号。" data-title="苹果折叠式iPhone：新任掌舵人的豪赌，能转化为实质销量吗？" data-date="09-10 13:37" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 13:37</span>
          <span class="news-item-title">苹果折叠式iPhone：新任掌舵人的豪赌，能转化为实质销量吗？</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/486625.html" target="_blank" rel="noopener" data-cat="keji" data-summary="模型可以开源，部署经验不能" data-title="一周连发6个模型！这家公司把具身智能的闭环跑通了" data-date="09-10 12:55" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-10 12:55</span>
          <span class="news-item-title">一周连发6个模型！这家公司把具身智能的闭环跑通了</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-10/10693746.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社北京9月10日电 据乌克兰媒体报道，当地时间9日晚，乌克兰东北部苏梅市一处购物娱乐中心遭到无人机袭击，已造成2人死亡、20人受伤。" data-title="乌克兰苏梅市一购物中心遇袭致2死20伤" data-date="09-10 10:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 10:58</span>
          <span class="news-item-title">乌克兰苏梅市一购物中心遇袭致2死20伤</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/486436.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月9日，以“JoyAI · 跃迁物理世界”为主题的JDDiscovery-2026京东全球科技探索者大会在北京举行" data-title="打造10万卡国产算力集群推出JoyAI世界模型，京东发布物理AI建设最新成果" data-date="09-10 09:39" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-10 09:39</span>
          <span class="news-item-title">打造10万卡国产算力集群推出JoyAI世界模型，京东发布物理AI建设最新成果</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/486350.html" target="_blank" rel="noopener" data-cat="keji" data-summary="赶上了API限时五折" data-title="实测星火X2.5：手搓粒子月亮、拆完61页财报……还顺手揪出了我的Bug" data-date="09-10 08:42" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-10 08:42</span>
          <span class="news-item-title">实测星火X2.5：手搓粒子月亮、拆完61页财报……还顺手揪出了我的Bug</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cn74d8mr640o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="经典的“好太太”系列广告以“好丈夫”的形象重出江湖：镜头前穿着清凉的不再是女性,而是男性。" data-title="AI“性转”视频风靡中国网络：一场“ 新文化运动”的觉醒与局限" data-date="09-10 08:14" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 08:14</span>
          <span class="news-item-title">AI“性转”视频风靡中国网络：一场“ 新文化运动”的觉醒与局限</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/09/ai-research-startup-listen-labs-scrubbed-a-1-5b-funding-round-for-salesforce-talks/" target="_blank" rel="noopener" data-cat="keji" data-summary="消息人士称， Listen Labs放弃了Menlo Ventures签署的C系列条款表。" data-title="人工智能研究初创公司Listen Labs为Salesforce会谈筹集了15亿美元资金" data-date="09-10 08:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-10 08:00</span>
          <span class="news-item-title">人工智能研究初创公司Listen Labs为Salesforce会谈筹集了15亿美元资金</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">2 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3v4379d4ylo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚历克西斯·麦克·阿利斯特(Alexis Mac Allister)对他在利物浦的合同的公开评论存在分歧，球迷和BBC体育评论员帕特·内文(Pat Nevin)分享了意见。" data-title="“说得很精彩”，但利物浦球迷对麦克·阿利斯特的合同评论感到不满" data-date="09-09 23:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-09 23:07</span>
          <span class="news-item-title">“说得很精彩”，但利物浦球迷对麦克·阿利斯特的合同评论感到不满</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm2mlk4p4x5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃斯特沃·威廉在对阵阿森纳的客串比赛中表现出色，让我们看看他本赛季可以在切尔西队中扮演什么角色。" data-title="埃斯特沃融入切尔西的一切" data-date="09-09 15:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-09 15:00</span>
          <span class="news-item-title">埃斯特沃融入切尔西的一切</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-10/10693945.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如今，徒步、登山等户外休闲活动备受追捧，社交媒体上不少标注“宝藏”的网红徒步攻略热度很高，但这样的攻略背后往往暗藏安全隐患。前不久，北京一名女子就依照一条网红徒步攻略出行，不料遭遇意外。" data-title="女子按网红徒步攻略出行遭意外 户外出游遇险谁担责？" data-date="09-10 14:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 14:38</span>
          <span class="news-item-title">女子按网红徒步攻略出行遭意外 户外出游遇险谁担责？</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/728.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 10 日消息，科幻射击新作《流浪地球：望日》今日发布首个预告片，由《边境》开发团队柳叶刀工作室制作，刘慈欣本人担任监制，是一款线性剧情任务驱动的第三人称科幻射击游戏。玩家将扮演一名工程师，在最后的“望日窗口”结束前赶赴月球，执行关乎人类存亡的关键任务。玩家将深入月球与太空战场，借助宇航服、外骨骼等特殊装备，探索更多不同于传统射击游戏的战场体验。《流浪地球：望日》现已上架 Steam 商店，具体发售日期待定。柳叶刀工作室的太空射击游戏《边境》是一款近未来太空题材的第一人称射击游戏，形形色色的太空操作员在近轨道相遇，在零重力环境下进行射击对战。该游戏于 2023 年 4 月 13 日以“抢先体验”形式在 Steam 平台提前开服。2024 年 6 月 20 日，柳叶刀工作室发布" data-title="科幻射击单机游戏《流浪地球：望日》上架 Steam：刘慈欣监制，《边境》开发团队制作" data-date="09-10 14:22" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-10 14:22</span>
          <span class="news-item-title">科幻射击单机游戏《流浪地球：望日》上架 Steam：刘慈欣监制，《边境》开发团队制作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-10/10693917.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="平日里不少宝爸宝妈会带孩子去商场玩，常乘坐自动扶梯。出于好奇，有的孩子把自动扶梯当成大玩具，由此引发的意外事故近期频繁出现，一些事故甚至发生在家长的眼皮底下，值得警惕。" data-title="别再让孩子这样玩扶梯！这些地方尤其危险→" data-date="09-10 13:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 13:55</span>
          <span class="news-item-title">别再让孩子这样玩扶梯！这些地方尤其危险→</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-10/10693880.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京9月10日电 (记者 陈杭)北京拟鼓励各区依托世界遗产、历史建筑、革命史迹、传统村落、历史街巷、民俗文化等，整合分散文博资源，推动连片活化利用，构建开放式博物馆展示方式，建设“没有围墙的博物馆”。" data-title="北京拟立法鼓励建设“没有围墙的博物馆”" data-date="09-10 13:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 13:13</span>
          <span class="news-item-title">北京拟立法鼓励建设“没有围墙的博物馆”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-10/10693879.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社海南东方9月10日电 题：海南黎村“花样”蝶变 多元业态引客来" data-title="（走进中国乡村）海南黎村“花样”蝶变　多元业态引客来" data-date="09-10 13:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 13:12</span>
          <span class="news-item-title">（走进中国乡村）海南黎村“花样”蝶变　多元业态引客来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-10/10693881.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近日" data-title="巡查人员多看一眼救了216人！这些异常可能是泥石流发生前兆" data-date="09-10 13:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-10 13:06</span>
          <span class="news-item-title">巡查人员多看一眼救了216人！这些异常可能是泥石流发生前兆</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ced7g3qpyyjo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2001年的袭击造成数千名美国人丧生，并对全球产生了深远影响。" data-title="911事件25周年：震惊世界的袭击如何发生，造成多少人死亡？" data-date="09-10 08:14" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 08:14</span>
          <span class="news-item-title">911事件25周年：震惊世界的袭击如何发生，造成多少人死亡？</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/09/business/saudi-arabia-houthis-red-sea-oil-shipping.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="由于安全运输石油的好选择很少，沙特阿拉伯的出口已跌至 13 年来的最低点。" data-title="由于战争蔓延导致航线关闭，沙特石油出口暴跌" data-date="09-10 00:42" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 00:42</span>
          <span class="news-item-title">由于战争蔓延导致航线关闭，沙特石油出口暴跌</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/09/us/cesar-chavez-lawsuit.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这是自今年针对工会领导人的丑闻曝光以来的首起此类诉讼，指控两个基金会未能阻止“虐待、流氓和不当”行为。" data-title="新原告起诉与塞萨尔·查韦斯有联系的基金会" data-date="09-10 00:36" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-10 00:36</span>
          <span class="news-item-title">新原告起诉与塞萨尔·查韦斯有联系的基金会</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/991893/google-search-gets-better-at-live-nfl-football" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Google 推出了新的实时比赛动态，让您在常规赛季今晚开始时了解 NFL 比赛的最新动态。寻找红色的“直播”图标，您将看到正在进行的比赛的回顾、逐个比赛的更新、社交热门评论、视频亮点和“人工智能驱动的见解”。现在可以在手机上使用英语，[...]" data-title="谷歌搜索包含 NFL 橄榄球直播" data-date="09-10 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-10 00:00</span>
          <span class="news-item-title">谷歌搜索包含 NFL 橄榄球直播</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/487.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 9 日消息，弹幕射击游戏《东方红魔乡：新典 ～ the Embodiment of Scarlet Devil.》现已正式发售，登陆 PS5、Switch 2、PC 平台，支持中文。IT之家获悉，《东方红魔乡：新典》是 2002 年推出的《东方红魔乡》时隔 24 年首次推出的重制版本，玩家将操控博丽灵梦与雾雨魔理沙，在漫天飞舞的弹幕之间穿梭，调查笼罩幻想乡的神秘红雾异变。价格方面，以 Steam 国区为例，本作标准版定价为 69 元（收录原版《东方红魔乡 Classic》游戏），豪华版定价为 97.75 元，额外收录游戏音乐原声带，IT之家附游戏商品页（https://store.steampowered.com/app/4659620/__the_Embodiment_o" data-title="经典弹幕游戏重制《东方红魔乡：新典》发售，Steam 国区 69 元起" data-date="09-09 23:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-09 23:52</span>
          <span class="news-item-title">经典弹幕游戏重制《东方红魔乡：新典》发售，Steam 国区 69 元起</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/000/485.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 9 日消息，发行商 Deep Silver 今天在任天堂新一期直面会宣布，《天国：拯救 2 皇家版》将登陆 Switch 2 平台，预计 2027 年发售。据介绍，本作将包含所有 DLC，包含高级剧情扩展包、专属装备和额外任务线。玩家可在游戏中体验第一人称中世纪冒险，感受广阔开放世界、宏大的电影级剧情以及爽快战斗。IT之家了解到，《天国：拯救 2》发售于去年 2 月 4 日，主打历史题材第一人称开放世界动作角色扮演，过去一年里官方陆续推出了多次免费更新以及三款付费 DLC，其中最后一款资料片《教会的奥秘》表现尤为亮眼，Embracer Group 认为本 DLC 帮助游戏表现“远超”预期。" data-title="《天国：拯救 2 皇家版》游戏官宣登陆任天堂 Switch 2，预计 2027 年发售" data-date="09-09 23:23" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-09 23:23</span>
          <span class="news-item-title">《天国：拯救 2 皇家版》游戏官宣登陆任天堂 Switch 2，预计 2027 年发售</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-09/10693650.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近日，青岛一男子花15元买了两斤蛤蜊，吃着吃着突然咬到硬物，吐出来一看，竟是3颗珍珠。无独有偶，当地崂山区的王先生此前食用蛤蜊时，也曾吃出一颗高粱米大小的乳白色珍珠。相关话题引发热议。" data-title="15元买两斤蛤蜊吃出3颗珍珠！专家：正常现象 不耽误食用" data-date="09-09 23:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-09 23:23</span>
          <span class="news-item-title">15元买两斤蛤蜊吃出3颗珍珠！专家：正常现象 不耽误食用</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-09/10693645.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月9日电 (记者 孙自法)中国科学院青藏高原研究所陈发虎院士领衔的古生态与人类适应团队联合中外合作者，最近通过对云南鹤庆蝙蝠洞遗址开展多学科综合研究，首次系统揭示中国南方丹尼索瓦人(丹人)的体质形态、技术行为与生存策略，重建出这一神秘人群在青藏高原东南缘的生存全景图，包括石器技术保持长期稳定、生存适应高度务实等。" data-title="考古首次揭示中国南方丹尼索瓦人生存图景：长期稳定高度务实" data-date="09-09 23:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-09 23:05</span>
          <span class="news-item-title">考古首次揭示中国南方丹尼索瓦人生存图景：长期稳定高度务实</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/992053/the-switch-2-is-getting-a-2d-metroid-called-ravenous" target="_blank" rel="noopener" data-cat="zonghe" data-summary="任天堂刚刚宣布在 Switch 2 上推出一款银河战士系列新 2D 作品，名为《银河战士：贪婪》。它将于 2027 年 1 月 28 日推出。这款新游戏看起来像是《银河战士恐惧》的进化版。虽然它仍然是一款 2D 游戏，但它具有 3D 图形、大量电影动作镜头、招架敌人以及 Samus 四处滚动 [...]" data-title="Switch 2 将迎来一款名为 Ravenous 的 2D 银河战士" data-date="09-09 22:46" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-09 22:46</span>
          <span class="news-item-title">Switch 2 将迎来一款名为 Ravenous 的 2D 银河战士</span>
        </a>
  </div>
</div>

<script>
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
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'flex' : 'block') : 'none';
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


---

<p class="news-updated">🕐 抓取更新于 2026-09-10 14:44（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
