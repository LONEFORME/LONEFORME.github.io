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
      <span>2026-09-01 今日更新</span>
    </div>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">13</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">6</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 科技 & AI</span>
        <span class="channel-count">1</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">6</span>
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
  <a class="hero-featured-card" href="https://www.bbc.co.uk/sport/football/articles/ckgvrlme148o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城与切尔西就签下阿根廷中场恩佐·费尔南德斯展开谈判。" data-title="曼城与切尔西就费尔南德斯转会事宜展开谈判" data-date="08-31" data-source="BBC">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
        <span class="hero-featured-date">08-31</span>
      </div>
      <h2 class="hero-featured-title">曼城与切尔西就费尔南德斯转会事宜展开谈判</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cpwlxkynjvno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="枪手 1-0 获胜后阿斯顿维拉和阿森纳球员的评价。" data-title="比赛获胜者萨卡表现如何？阿斯顿维拉 v 阿森纳 评分" data-date="08-31" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">🔥 焦点</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">比赛获胜者萨卡表现如何？阿斯顿维拉 v 阿森纳 评分</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c74em1dx0pjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本赛季每轮英超比赛结束后，特洛伊·迪尼都会向我们推荐他的本周最佳球队。你同意他的选择吗？" data-title="谁入选了特洛伊本周英超最佳球队？" data-date="08-31" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">🔥 焦点</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">谁入选了特洛伊本周英超最佳球队？</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/crm97epp2l4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城提议以 8000 万英镑收购利物浦前锋科迪·加克波的提议接近失败。" data-title="曼城8000万英镑收购Gakpo的交易接近失败" data-date="08-31" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">🔥 焦点</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">曼城8000万英镑收购Gakpo的交易接近失败</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">6 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckgvrlme148o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城与切尔西就签下阿根廷中场恩佐·费尔南德斯展开谈判。" data-title="曼城与切尔西就费尔南德斯转会事宜展开谈判" data-date="08-31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-31</span>
          <span class="news-item-title">曼城与切尔西就费尔南德斯转会事宜展开谈判</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cpwlxkynjvno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="枪手 1-0 获胜后阿斯顿维拉和阿森纳球员的评价。" data-title="比赛获胜者萨卡表现如何？阿斯顿维拉 v 阿森纳 评分" data-date="08-31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-31</span>
          <span class="news-item-title">比赛获胜者萨卡表现如何？阿斯顿维拉 v 阿森纳 评分</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c74em1dx0pjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本赛季每轮英超比赛结束后，特洛伊·迪尼都会向我们推荐他的本周最佳球队。你同意他的选择吗？" data-title="谁入选了特洛伊本周英超最佳球队？" data-date="08-31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-31</span>
          <span class="news-item-title">谁入选了特洛伊本周英超最佳球队？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crm97epp2l4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城提议以 8000 万英镑收购利物浦前锋科迪·加克波的提议接近失败。" data-title="曼城8000万英镑收购Gakpo的交易接近失败" data-date="08-31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-31</span>
          <span class="news-item-title">曼城8000万英镑收购Gakpo的交易接近失败</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c80453nj9gno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城同意以至少 6000 万英镑的价格从埃弗顿签下伊利曼·恩迪亚耶。" data-title="曼城同意以 6500 万英镑收购埃弗顿球员恩迪亚耶" data-date="08-31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-31</span>
          <span class="news-item-title">曼城同意以 6500 万英镑收购埃弗顿球员恩迪亚耶</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c4gj341p8ypo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西接受托特纳姆热刺队对边锋米哈伊洛·穆德里克和后卫托辛·阿达拉比奥约的报价，以及意大利俱乐部科莫对门将罗伯特·桑切斯的报价。" data-title="穆德里克转会热刺，切尔西桑切斯前往科莫" data-date="08-31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-31</span>
          <span class="news-item-title">穆德里克转会热刺，切尔西桑切斯前往科莫</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">科技创新 & AI 算力</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx2zp5q4gnjo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="卫星对比图像曝光尼泊尔洪灾的严峻灾情。许多村庄、桥梁和西藏边境的重要过境点被毁灭性的洪水冲毁。" data-title="卫星图像揭示村庄灾情的严重程度" data-date="08-30" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 科技前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">08-30</span>
          <span class="news-item-title">卫星图像揭示村庄灾情的严重程度</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (时政国际 · 文化社会 · 环保教育)</span>
      <span class="news-category-count">6 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/tp/2026/09-01/10687687.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="9月1日，家长在华东师范大学附属天山学校门口，帮助学生整理书包。近日，上海市教育委员会发布《上海市中小学2026学年校历》。上海市各区中小学统一于2026年9月1日开学，2027年1月22日结束，全学期共21周。中新社记者 殷立勤 摄 9月1日，学生进入华东师范大学附属天山学校。近日，上海市教育委员会发布《上海市中小学2026学年校历》。上海市各区中小学统一于2026年9月1日开学，2027年1月22日结束，全学期共21周。中新社记者 殷立勤 摄 9月1日，家长在华东师范大学附属天山学校门口，帮助学生整理书包。近日，上海市教育委员会发布《上海市中小学2026学年校历》。上海市各区中小学统一于2026年9月1日开学，2027年1月22日结束，全学期共21周。中新社记者 殷立勤 摄 9月1日，上" data-title="上海市各区中小学开启秋季新学期" data-date="09-01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-01</span>
          <span class="news-item-title">上海市各区中小学开启秋季新学期</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-01/10687751.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网青海西宁9月1日电 (记者 孙晨慧 赵凛松)澜沧江发源于青海，出中国境后称湄公河，流经缅甸、老挝、泰国、柬埔寨、越南，最终汇入南海。" data-title="从澜沧江源头出发 奔赴下一个“金色十年”" data-date="09-01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-01</span>
          <span class="news-item-title">从澜沧江源头出发 奔赴下一个“金色十年”</span>
        </a>
        <a class="news-item" href="http://www.chinanews.com.cn/tp/hd2011/2026/09-01/1202737.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国“9·11”国家纪念博物馆推出“9·11”事件25周年特展" data-title="美国“9·11”国家纪念博物馆推出“9·11”事件25周年特展" data-date="09-01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-01</span>
          <span class="news-item-title">美国“9·11”国家纪念博物馆推出“9·11”事件25周年特展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-01/10687752.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网阿坝9月1日电 题：雪山脚下的传承：四代人接力守护芦花会议会址九十载" data-title="（长征胜利90周年）雪山脚下的传承：四代人接力守护芦花会议会址九十载" data-date="09-01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-01</span>
          <span class="news-item-title">（长征胜利90周年）雪山脚下的传承：四代人接力守护芦花会议会址九十载</span>
        </a>
        <a class="news-item" href="http://www.chinanews.com.cn/tp/hd2011/2026/09-01/1202734.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="智神星一号运载火箭首飞成功" data-title="智神星一号运载火箭首飞成功" data-date="09-01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-01</span>
          <span class="news-item-title">智神星一号运载火箭首飞成功</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-01/10687748.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近期，菲律宾武装部队联合美国印太司令部下属部队及澳大利亚国防军在中国南海相关海域完成了第19次“多边海上合作活动”(MMCA)。自2024年4月该机制由双边升级为多边以来，短短两年零四个月内已经高频举办19次演习，仅2026年前八个月就开展了10次，互动频率远超传统盟国年度例行演习的常规标准。" data-title="警惕菲方以“多边合作”之名行军事挑衅之实" data-date="09-01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-01</span>
          <span class="news-item-title">警惕菲方以“多边合作”之名行军事挑衅之实</span>
        </a>
  </div>
</div>


---

<p class="news-updated">🕐 更新于 2026-09-01</p>
