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
      <span>2026-10-09 22:30 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · BBC×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.theverge.com/policy/1008677/trump-super-intelligence-ai-rebranding" target="_blank" rel="noopener" data-cat="shizheng" data-summary="唐纳德·特朗普总统善于用言语对付他的敌人。他第一次成功的总统竞选建立在“小马可”和“歪曲的希拉里”等绰号的基础上；他将“假新闻”从描述欺诈性媒体的短语改为" data-title="Trump’s attempt to rename AI is looking awfully artificial" data-date="10-09 22:25" data-source="The Verge">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
        <span class="hero-featured-date">🕒 10-09 22:25</span>
      </div>
      <h2 class="hero-featured-title">特朗普重命名人工智能的尝试看起来非常人为</h2>
      <div class="hero-featured-title-en">Trump’s attempt to rename AI is looking awfully artificial</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/142.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 9 日消息，中共中央 国务院今日发布《关于发展新质生产力的意见》，提出 19 条重大发展改革任务，坚持“创新主导、改革为要、因地制宜、先立后破”4 条原则。《意见》将“大力推进科技创新”作为 5 大任务之首，提出加强原创性颠覆性科技创新、加快突破关键核心技术、统筹国家战略科技力量建设、强化企业科技创新主体地位、加速科技成果向现实生产力转化。在培育壮大新兴产业方面，《意见》提出着力打造新兴支柱产业。加快新一代信息技术、新能源、新材料、智能网联新能源汽车、机器人、生物医药、高端装备、航空航天等战略性新兴产业发展，因地制宜建设各具特色、优势互补的战略性新兴产业集群，推动资源集聚、主体集中、成果集成、分工合作。深化产业内、产品内专业分工，促进跨行业跨区域融合，避免“内卷式”竞争。" data-title="国务院发布《关于发展新质生产力的意见》：加快推进智能网联新能源汽车、人工智能手机和电脑、人形机器人等新一代智能终端场景应用" data-date="10-09 22:10" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">国务院发布《关于发展新质生产力的意见》：加快推进智能网联新能源汽车、人工智能手机和电脑、人形机器人等新一代智能终端场景应用</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/09/premier-league-resumes-manchester-city-in-spotlight-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进入周末⚽的所有最新足球新闻⚽十件事|马雷斯卡对未来的羞怯|邮件比利足球周刊：您可以观看/收听播音员阵容讨论周日在利物浦和曼城之间的冲突，以及更多，在最新" data-title="Maresca says Manchester City titles not tainted; Liverpool’s Isak and Gakpo injured" data-date="10-09 22:28" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Maresca says Manchester City titles not tainted; Liverpool’s Isak and Gakpo injured</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/10-09/10709952.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社北京10月9日电 国务委员谌贻琴9日在京会见载誉归来的第20届亚运会中国体育代表团，向全体运动员、教练员及工作人员转达党中央、国务院的热烈祝贺和亲切慰问，强调要牢记习近平总书记嘱托，戒骄戒躁、再接再厉，扎实推进洛杉矶奥运会备战工作。" data-title="谌贻琴在会见第20届亚运会中国体育代表团时强调 戒骄戒躁 再接再厉 扎实推进洛杉矶奥运会备战工作" data-date="10-09 22:26" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">谌贻琴在会见第20届亚运会中国体育代表团时强调 戒骄戒躁 再接再厉 扎实推进洛杉矶奥运会备战工作</p>
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
        <a class="news-item" href="https://www.theverge.com/policy/1008677/trump-super-intelligence-ai-rebranding" target="_blank" rel="noopener" data-cat="shizheng" data-summary="唐纳德·特朗普总统善于用言语对付他的敌人。他第一次成功的总统竞选建立在“小马可”和“歪曲的希拉里”等绰号的基础上；他将“假新闻”从描述欺诈性媒体的短语改为" data-title="Trump’s attempt to rename AI is looking awfully artificial" data-date="10-09 22:25" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 22:25</span>
          <span class="news-item-title">特朗普重命名人工智能的尝试看起来非常人为</span>
          <span class="news-item-title-en">Trump’s attempt to rename AI is looking awfully artificial</span>
          <span class="news-value-point">💡 唐纳德·特朗普总统善于用言语对付他的敌人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709948.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网长沙10月9日电(向一鹏)湖南省住房和城乡建设厅9日透露，目前湖南已搭建起相对完整的城市更新政策框架，省级先后出台16份相关文件，系统推进存量土地盘活，推动存量建筑活化利用，促进城市高质量发展。" data-title="湖南系统推进城市更新 推动存量建筑活化利用" data-date="10-09 22:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:15</span>
          <span class="news-item-title">湖南系统推进城市更新 推动存量建筑活化利用</span>
          <span class="news-value-point">💡 中新网长沙10月9日电(向一鹏)湖南省住房和城乡建设厅9日透露，目前湖南已搭建起相对完整的城市更新政策框架，省级先后出台16份相关文件，系统推进…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709928.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦10月9日电 当地时间10月9日，中国驻英国使馆发言人就英方制裁中国实体问题答记者问。" data-title="中国驻英国使馆敦促英方立即撤销对有关中国实体的制裁" data-date="10-09 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:01</span>
          <span class="news-item-title">中国驻英国使馆敦促英方立即撤销对有关中国实体的制裁</span>
          <span class="news-value-point">💡 中新社伦敦10月9日电 当地时间10月9日，中国驻英国使馆发言人就英方制裁中国实体问题答记者问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709938.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社东京10月9日电(记者梁晨#8195;李子越#8195;陈泽安)日本冲绳县议会9日就驻日美军士兵涉嫌抢劫杀人案通过抗议决议和意见书，向美方提出抗议，并向日本政府提出交涉，要求采取有效措施防止类似案件发生，以及从根本上修订日美地位协定。" data-title="国际观察｜冲绳命案凸显日本倚美恶果" data-date="10-09 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:01</span>
          <span class="news-item-title">国际观察｜冲绳命案凸显日本倚美恶果</span>
          <span class="news-value-point">💡 新华社东京10月9日电(记者梁晨#8195;李子越#8195;陈泽安)日本冲绳县议会9日就驻日美军士兵涉嫌抢劫杀人案通过抗议决议和意见书，向美方…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709905.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦10月9日电 (记者 欧阳开宇)英国环境署10月9日宣布约克郡正式进入干旱状态，当地水库与河流水位偏低，近期降雨尚不足以弥补春夏降水短缺造成的水资源缺口。" data-title="英国约克郡正式进入干旱状态" data-date="10-09 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:01</span>
          <span class="news-item-title">英国约克郡正式进入干旱状态</span>
          <span class="news-value-point">💡 中新网伦敦10月9日电 (记者 欧阳开宇)英国环境署10月9日宣布约克郡正式进入干旱状态，当地水库与河流水位偏低，近期降雨尚不足以弥补春夏降水短…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709814.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦10月9日电 (记者 欧阳开宇)英国教育部9日发布民调显示，绝大多数青少年支持政府推进职业教育改革，希望获得更多实操学习机会，社会长期存在的职业教育偏见仍未完全消除。" data-title="英国推职业教育改革 多数青少年支持实操学习路径" data-date="10-09 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:59</span>
          <span class="news-item-title">英国推职业教育改革 多数青少年支持实操学习路径</span>
          <span class="news-value-point">💡 中新网伦敦10月9日电 (记者 欧阳开宇)英国教育部9日发布民调显示，绝大多数青少年支持政府推进职业教育改革，希望获得更多实操学习机会，社会长期…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709932.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社墨尔本10月9日电#8195;通讯｜不断升温的澳大利亚“赴华热”" data-title="通讯｜不断升温的澳大利亚“赴华热”" data-date="10-09 21:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:58</span>
          <span class="news-item-title">通讯｜不断升温的澳大利亚“赴华热”</span>
          <span class="news-value-point">💡 新华社墨尔本10月9日电#8195;通讯｜不断升温的澳大利亚“赴华热”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709931.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月9日电 据伊朗塔斯尼姆通讯社当地时间9日报道，伊朗革命卫队称将打击区域内所有“违规”船只，范围不限于霍尔木兹海峡。" data-title="伊朗革命卫队：将打击区域内所有“违规”船只，范围不限于霍尔木兹海峡" data-date="10-09 21:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:57</span>
          <span class="news-item-title">伊朗革命卫队：将打击区域内所有“违规”船只，范围不限于霍尔木兹海峡</span>
          <span class="news-value-point">💡 中新网10月9日电 据伊朗塔斯尼姆通讯社当地时间9日报道，伊朗革命卫队称将打击区域内所有“违规”船只，范围不限于霍尔木兹海峡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709923.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月9日电 据“外交部驻香港特派员公署”微信公众号消息，针对美国国务院发布所谓《2026年人口贩运报告》，罔顾事实，恶意诋毁香港特区打击人口贩运的努力和成效，歪曲抹黑香港国安法和《维护国家安全条例》，外交部驻港公署发言人表示强烈不满和坚决反对。" data-title="外交部驻港公署发言人：人口贩运的“锅”香港不背" data-date="10-09 21:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:55</span>
          <span class="news-item-title">外交部驻港公署发言人：人口贩运的“锅”香港不背</span>
          <span class="news-value-point">💡 中新网10月9日电 据“外交部驻香港特派员公署”微信公众号消息，针对美国国务院发布所谓《2026年人口贩运报告》，罔顾事实，恶意诋毁香港特区打击…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/us/politics/fort-hood-execution-streamed-public.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="如果执行，定于12月3日由行刑队公开处决Nidal Malik Hasan少校将是美国现代历史上的第一次。" data-title="Fort Hood Shooter’s Execution Will Be Public and Streamed Live, Pentagon Says" data-date="10-09 21:29" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 21:29</span>
          <span class="news-item-title">五角大楼表示，胡德堡射手的处决将公开并直播</span>
          <span class="news-item-title-en">Fort Hood Shooter’s Execution Will Be Public and Streamed Live, Pentagon Says</span>
          <span class="news-value-point">💡 如果执行，定于12月3日由行刑队公开处决Nidal Malik Hasan少校将是美国现代历史上的第一次</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/world/europe/putin-russia-ukraine-war-europe-nato.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="莫斯科利用恐惧和模棱两可的策略试图分裂北约并限制对乌克兰的支持。但欧洲应该如何报复？有多难？" data-title="As Putin Wages Shadow War, Europe Looks for a Way to Hit Back" data-date="10-09 21:09" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 21:09</span>
          <span class="news-item-title">随着普京发动影子战争，欧洲寻找回击的方法</span>
          <span class="news-item-title-en">As Putin Wages Shadow War, Europe Looks for a Way to Hit Back</span>
          <span class="news-value-point">💡 莫斯科利用恐惧和模棱两可的策略试图分裂北约并限制对乌克兰的支持</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/podcasts/the-headlines/nobel-peace-prize-livestream-execution.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="此外，还有周五的新闻测验。" data-title="The 2026 Nobel Peace Prize Winner, and the Pentagon’s Plan to Livestream an Execution" data-date="10-09 19:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 19:00</span>
          <span class="news-item-title">2026年诺贝尔和平奖获得者，以及五角大楼直播处决的计划</span>
          <span class="news-item-title-en">The 2026 Nobel Peace Prize Winner, and the Pentagon’s Plan to Livestream an Execution</span>
          <span class="news-value-point">💡 此外，还有周五的新闻测验</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/us/midterm-election-democratic-wave.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党在2006年和2018年对抗不受欢迎的共和党总统的最后两次中期选举。他们的结果明显不同。" data-title="Why This Election Could Be More Complicated for Democrats Than Polls Suggest" data-date="10-09 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 17:02</span>
          <span class="news-item-title">为什么这次选举对民主党人来说可能比民意调查所暗示的更复杂</span>
          <span class="news-item-title-en">Why This Election Could Be More Complicated for Democrats Than Polls Suggest</span>
          <span class="news-value-point">💡 民主党在2006年和2018年对抗不受欢迎的共和党总统的最后两次中期选举</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/us/politics/trump-grand-conspiracy.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统的盟友试图通过司法部庞大的调查来证明“大阴谋”。在人员配置调整、内部纠纷和难以找到证据的情况下，它已经屈服了。" data-title="How Trump’s Revenge Campaign Descended Into Turmoil" data-date="10-09 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 17:00</span>
          <span class="news-item-title">特朗普的复仇运动如何陷入动荡</span>
          <span class="news-item-title-en">How Trump’s Revenge Campaign Descended Into Turmoil</span>
          <span class="news-value-point">💡 总统的盟友试图通过司法部庞大的调查来证明“大阴谋”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/us/senate-debate-maine-michigan-georgia.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="可能决定参议院控制权的三场比赛的候选人进行了激烈的人身攻击。" data-title="Fiery Senate Debates in Maine, Michigan and Georgia: Five Takeaways" data-date="10-09 16:38" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 16:38</span>
          <span class="news-item-title">缅因州、密歇根州和佐治亚州参议院激烈辩论：五大要点</span>
          <span class="news-item-title-en">Fiery Senate Debates in Maine, Michigan and Georgia: Five Takeaways</span>
          <span class="news-value-point">💡 可能决定参议院控制权的三场比赛的候选人进行了激烈的人身攻击</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/142.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 9 日消息，中共中央 国务院今日发布《关于发展新质生产力的意见》，提出 19 条重大发展改革任务，坚持“创新主导、改革为要、因地制宜、先立后破”4 条原则。《意见》将“大力推进科技创新”作为 5 大任务之首，提出加强原创性颠覆性科技创新、加快突破关键核心技术、统筹国家战略科技力量建设、强化企业科技创新主体地位、加速科技成果向现实生产力转化。在培育壮大新兴产业方面，《意见》提出着力打造新兴支柱产业。加快新一代信息技术、新能源、新材料、智能网联新能源汽车、机器人、生物医药、高端装备、航空航天等战略性新兴产业发展，因地制宜建设各具特色、优势互补的战略性新兴产业集群，推动资源集聚、主体集中、成果集成、分工合作。深化产业内、产品内专业分工，促进跨行业跨区域融合，避免“内卷式”竞争。" data-title="国务院发布《关于发展新质生产力的意见》：加快推进智能网联新能源汽车、人工智能手机和电脑、人形机器人等新一代智能终端场景应用" data-date="10-09 22:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 22:10</span>
          <span class="news-item-title">国务院发布《关于发展新质生产力的意见》：加快推进智能网联新能源汽车、人工智能手机和电脑、人形机器人等新一代智能终端场景应用</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，中共中央 国务院今日发布《关于发展新质生产力的意见》，提出 19 条重大发展改革任务，坚持“创新主导、改革为要、…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1008254/instinct-agent-ai-hands-on-muse-dots" target="_blank" rel="noopener" data-cat="keji" data-summary="在有可爱的小家伙之前，就有本能。今年8月，这家初创公司将其人工智能代理推向市场，推出了一本不同寻常的剧本：仅限受邀者，没有营销，几乎没有网站。然而，本能很快成为人工智能中最嗡嗡作响的东西，" data-title="Instinct was the buzziest AI agent around — can it survive Muse?" data-date="10-09 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 22:00</span>
          <span class="news-item-title">本能是周围最嗡嗡作响的人工智能特工—它能否在Muse中生存</span>
          <span class="news-item-title-en">Instinct was the buzziest AI agent around — can it survive Muse?</span>
          <span class="news-value-point">💡 在有可爱的小家伙之前，就有本能</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709901.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网哈尔滨10月9日电(记者 刘璐)9日，黑龙江省人民政府新闻办公室举行《黑龙江省第九个五年法治宣传教育工作行动计划(2026—2030年)》介绍和解读新闻发布会。据悉，该行动计划由省司法厅会同省委宣传部等部门编制，全面承接国家“九五”普法规划，立足黑龙江实际，细化形成24个方面89项任务清单，旨在提升公民法治素养、繁荣发展社会主义法治文化，加快构建精准高效“大普法”格局。" data-title="黑龙江省推进“人工智能+普法”应用 推动法治精神浸润生活日常" data-date="10-09 21:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:49</span>
          <span class="news-item-title">黑龙江省推进“人工智能+普法”应用 推动法治精神浸润生活日常</span>
          <span class="news-value-point">💡 中新网哈尔滨10月9日电(记者 刘璐)9日，黑龙江省人民政府新闻办公室举行《黑龙江省第九个五年法治宣传教育工作行动计划(2026—2030年)》…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/gigabytes-latest-bios-update-hints-at-intels-raptor-lake-next-launch-in-2027-new-cpus-may-support-both-ddr4-and-ddr5-memory" target="_blank" rel="noopener" data-cat="keji" data-summary="技嘉确认B760和H610主板上即将推出的英特尔LGA 1700处理器支持BIOS ，传闻中的Raptor Lake Next阵容预计将于2027年初同时支持DDR4和DDR5内存。" data-title="Gigabyte&#39;s latest BIOS update hints at Intel&#39;s Raptor Lake Next Launch in 2027" data-date="10-09 21:43" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-09 21:43</span>
          <span class="news-item-title">Gigabyte的最新BIOS更新暗示了英特尔将于2027年推出的Raptor Lake</span>
          <span class="news-item-title-en">Gigabyte's latest BIOS update hints at Intel's Raptor Lake Next Launch in 2027</span>
          <span class="news-value-point">💡 技嘉确认B760和H610主板上即将推出的英特尔LGA 1700处理器支持BIOS ，传闻中的Raptor Lake Next阵容预计将于202…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/pc-shipments-tumble-over-20-percent-in-3q26-as-chip-shortages-bite-top-three-pc-vendors-ship-11-6-million-fewer-units-year-over-year" target="_blank" rel="noopener" data-cat="keji" data-summary="2026年第三季度PC出货量下降了1580万台，其中联想、惠普和戴尔受到的打击最大。内存芯片制造商估计，这种情况要到2028年或2029年才会改善，即使宏碁认为PC价格" data-title="PC shipments tumble over 20% in 3Q26 as chip shortages bite" data-date="10-09 19:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-09 19:10</span>
          <span class="news-item-title">由于芯片短缺， PC出货量在26年第三季度下滑超过20 ％</span>
          <span class="news-item-title-en">PC shipments tumble over 20% in 3Q26 as chip shortages bite</span>
          <span class="news-value-point">💡 2026年第三季度PC出货量下降了1580万台，其中联想、惠普和戴尔受到的打击最大</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/independent-tests-rank-mistrals-new-trillion-parameter-large-4-the-best-ai-model-outside-the-u-s-and-china-but-chinese-open-weights-still-overcome-europes-best-efforts" target="_blank" rel="noopener" data-cat="keji" data-summary="人工分析将Mistral的新款Large 4评为38分，落后于小米、Z.ai、Moonshot和DeepSeek的开放模型。" data-title="Mistral’s new Large 4 trails some Chinese open models in independent tests" data-date="10-09 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-09 19:00</span>
          <span class="news-item-title">Mistral的新款Large 4在独立测试中追踪了一些中国开放模型</span>
          <span class="news-item-title-en">Mistral’s new Large 4 trails some Chinese open models in independent tests</span>
          <span class="news-value-point">💡 人工分析将Mistral的新款Large 4评为38分，落后于小米、Z.ai、Moonshot和DeepSeek的开放模型</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1008604/openai-defends-decision-fire-safety-researchers" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI坚定地决定解雇三名安全研究人员，此前调查发现他们“严重违反信任”。“在周五的X帖子中，该公司表示Jasmine Wang ， Tomek Korbak和Mikita Balesni被解雇" data-title="OpenAI doubles down on decision to fire three AI safety researchers" data-date="10-09 17:48" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 17:48</span>
          <span class="news-item-title">OpenAI加倍决定解雇三名人工智能安全研究人员</span>
          <span class="news-item-title-en">OpenAI doubles down on decision to fire three AI safety researchers</span>
          <span class="news-value-point">💡 OpenAI坚定地决定解雇三名安全研究人员，此前调查发现他们“严重违反信任”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502422.html" target="_blank" rel="noopener" data-cat="keji" data-summary="联想天禧AI自主研发的专业代码智能体框架TianxiCode 以71%的问题解决率登顶全球第一名" data-title="联想天禧自研代码智能体TianxiCode斩获SWE" data-date="10-09 16:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 16:53</span>
          <span class="news-item-title">联想天禧自研代码智能体TianxiCode斩获SWE</span>
          <span class="news-value-point">💡 联想天禧AI自主研发的专业代码智能体框架TianxiCode 以71%的问题解决率登顶全球第一名</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502411.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这是一台机器人正在关闭微波炉门时，因人手突然插进来而紧急悬停的时间" data-title="0.2秒急停、秒级重规划！因果智能走进真实世界" data-date="10-09 16:47" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 16:47</span>
          <span class="news-item-title">0.2秒急停、秒级重规划！因果智能走进真实世界</span>
          <span class="news-value-point">💡 这是一台机器人正在关闭微波炉门时，因人手突然插进来而紧急悬停的时间</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709655.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京10月9日电 (记者 黄钰钦 曾玥)中国外交部发言人毛宁9日主持例行记者会。" data-title="日本右翼势力持续向国际主流大模型提供经过篡改的二战历史语料 中方驳斥" data-date="10-09 15:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:34</span>
          <span class="news-item-title">日本右翼势力持续向国际主流大模型提供经过篡改的二战历史语料 中方驳斥</span>
          <span class="news-value-point">💡 中新网北京10月9日电 (记者 黄钰钦 曾玥)中国外交部发言人毛宁9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709646.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="10月9日，外交部发言人毛宁主持例行记者会。有记者会问，据披露，日本右翼势力持续向国际主流大模型提供经过篡改的二战历史语料，一些大模型在对话中输出带有明显错误史观的回答，例如将七七事变称为“日中军事冲突”，将南京大屠杀淡化为“南京陷落”，将日本侵略东南亚美化为“对南方资源的关心”等。发言人对此有何评论?" data-title="外交部批日本数据“投毒”歪曲侵略历史" data-date="10-09 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:30</span>
          <span class="news-item-title">外交部批日本数据“投毒”歪曲侵略历史</span>
          <span class="news-value-point">💡 10月9日，外交部发言人毛宁主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502364.html" target="_blank" rel="noopener" data-cat="keji" data-summary="答不答得对，得看Token站位" data-title="字节找到了DeepSeek时强时弱的原因" data-date="10-09 15:11" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 15:11</span>
          <span class="news-item-title">字节找到了DeepSeek时强时弱的原因</span>
          <span class="news-value-point">💡 答不答得对，得看Token站位</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/nyregion/ice-shooting-nyc-bronx.html" target="_blank" rel="noopener" data-cat="keji" data-summary="当局说，这名男子在一辆汽车里，一名5岁的孩子坐在后座上，当时他被枪击并受伤。市长Zohran Mamdani表示，特朗普政府正在“恐吓我们的城市”。" data-title="ICE Agent Shoots Man During Arrest Attempt in New York Neighborhood" data-date="10-09 15:06" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 15:06</span>
          <span class="news-item-title">ICE特工在纽约街区逮捕未遂时枪杀了一名男子</span>
          <span class="news-item-title-en">ICE Agent Shoots Man During Arrest Attempt in New York Neighborhood</span>
          <span class="news-value-point">💡 当局说，这名男子在一辆汽车里，一名5岁的孩子坐在后座上，当时他被枪击并受伤</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502359.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Google 研究成果首次登上《柳叶刀》主刊" data-title="《柳叶刀》研究表明：AI 有望改善医患关系" data-date="10-09 14:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 14:28</span>
          <span class="news-item-title">《柳叶刀》研究表明：AI 有望改善医患关系</span>
          <span class="news-value-point">💡 Google 研究成果首次登上《柳叶刀》主刊</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502330.html" target="_blank" rel="noopener" data-cat="keji" data-summary="机器人摆脱展会、舞台Demo，产生真实商业价值，究竟需要哪些东西？" data-title="灵巧操作头号玩家：Sharpa把指尖“触觉”进化到全面“体感”" data-date="10-09 12:15" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 12:15</span>
          <span class="news-item-title">灵巧操作头号玩家：Sharpa把指尖“触觉”进化到全面“体感”</span>
          <span class="news-value-point">💡 机器人摆脱展会、舞台Demo，产生真实商业价值，究竟需要哪些东西</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/09/premier-league-resumes-manchester-city-in-spotlight-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进入周末⚽的所有最新足球新闻⚽十件事|马雷斯卡对未来的羞怯|邮件比利足球周刊：您可以观看/收听播音员阵容讨论周日在利物浦和曼城之间的冲突，以及更多，在最新" data-title="Maresca says Manchester City titles not tainted; Liverpool’s Isak and Gakpo injured" data-date="10-09 22:28" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-09 22:28</span>
          <span class="news-item-title">马雷斯卡说曼城冠军没有受到影响；利物浦的伊萨克和Gakpo受伤</span>
          <span class="news-item-title-en">Maresca says Manchester City titles not tainted; Liverpool’s Isak and Gakpo injured</span>
          <span class="news-value-point">💡 进入周末⚽的所有最新足球新闻⚽十件事|马雷斯卡对未来的羞怯|邮件比利足球周刊：您可以观看/收听播音员阵容讨论周日在利物浦和曼城之间的冲突，以及更…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmzxjdvv784xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，俱乐部的冠军头衔在英超联赛对他们提出的115项指控中被判有罪后， “绝对没有”受到污染。" data-title="Man City titles &#39;absolutely not&#39; tainted" data-date="10-09 22:08" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 22:08</span>
          <span class="news-item-title">曼城冠军头衔“绝对没有”被污染</span>
          <span class="news-item-title-en">Man City titles 'absolutely not' tainted</span>
          <span class="news-value-point">💡 曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，俱乐部的冠军头衔在英超联赛对他们提出的115项指控中被判有罪后， “绝对没有”受到…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjkgey07lq15o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="巴士欢迎，横幅和旗帜预计曼城前往利物浦周日他们的第一场比赛，因为他们被判犯有违反英超联赛规则。" data-title="What reception awaits Man City at Anfield?" data-date="10-09 22:02" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 22:02</span>
          <span class="news-item-title">安菲尔德的曼城有什么招待会？</span>
          <span class="news-item-title-en">What reception awaits Man City at Anfield?</span>
          <span class="news-value-point">💡 巴士欢迎，横幅和旗帜预计曼城前往利物浦周日他们的第一场比赛，因为他们被判犯有违反英超联赛规则</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm040l634249o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="由于曼城被判犯有针对他们的115项指控中的大多数，他们的球迷感觉如何？" data-title="From doomscrolling to defiance - how do Man City fans feel?" data-date="10-09 17:02" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 17:02</span>
          <span class="news-item-title">从末日卷轴到反抗-曼城球迷的感受如何？</span>
          <span class="news-item-title-en">From doomscrolling to defiance - how do Man City fans feel?</span>
          <span class="news-value-point">💡 由于曼城被判犯有针对他们的115项指控中的大多数，他们的球迷感觉如何</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/09/zavier-gozo-crystal-palace-usmnt-interview" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在搬到伦敦之前，水晶宫的美国进口商除了犹他州以外从未居住过任何地方。现在，他的目标是更多的英超比赛分钟自5月以来，扎维尔·戈佐的生活发生了很大变化。那时，戈佐距离得知他" data-title="Zavier Gozo: ‘You have to be uncomfortable to get to the highest levels’" data-date="10-09 17:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-09 17:00</span>
          <span class="news-item-title">Zavier Gozo ： “你必须感到不舒服才能达到最高水平”</span>
          <span class="news-item-title-en">Zavier Gozo: ‘You have to be uncomfortable to get to the highest levels’</span>
          <span class="news-value-point">💡 在搬到伦敦之前，水晶宫的美国进口商除了犹他州以外从未居住过任何地方</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/09/carlos-baleba-manchester-united-debut" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛的回归，我们潜入签约谁可以提升曼联的中场–或进一步混淆事情卡洛斯·巴莱巴花了曼联$ 8870万（ £ 6500万）加上$ 680万（ £ 500万）的附加费，当他们在8月份从布莱顿签下他时。他可能b" data-title="Will Carlos Baleba fix Manchester United? Three big questions ahead of potential debut" data-date="10-09 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-09 16:00</span>
          <span class="news-item-title">卡洛斯·巴莱巴（ Carlos Baleba ）会修复曼联吗？在可能首次亮相之前的三大问题</span>
          <span class="news-item-title-en">Will Carlos Baleba fix Manchester United? Three big questions ahead of potential debut</span>
          <span class="news-value-point">💡 随着英超联赛的回归，我们潜入签约谁可以提升曼联的中场–或进一步混淆事情卡洛斯·巴莱巴花了曼联$ 8870万（ £ 6500万）加上$ 680万（…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck054p2lyeplo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联7000万英镑的夏季签约球员卡洛斯·巴莱巴（ Carlos Baleba ）预计将在老特拉福德（ Old Trafford ）对阵托特纳姆热刺（ Tottenham Hotspur" data-title="Is £70m Baleba ready for his Man Utd exam?" data-date="10-09 15:57" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 15:57</span>
          <span class="news-item-title">£ 7000万Baleba准备好参加曼联考试了吗？</span>
          <span class="news-item-title-en">Is £70m Baleba ready for his Man Utd exam?</span>
          <span class="news-value-point">💡 曼联7000万英镑的夏季签约球员卡洛斯·巴莱巴（ Carlos Baleba ）预计将在老特拉福德（ Old Trafford ）对阵托特纳姆热…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crn8wg221lnvo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Mikel Arteta本赛季对风险的胃口有所增加，但由于阿森纳希望保持领先地位，未能重塑将是一场更大的赌博。" data-title="How Arteta&#39;s response to Brighton loss may shape Arsenal&#39;s next chapter" data-date="10-09 14:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 14:41</span>
          <span class="news-item-title">Arteta对布莱顿损失的反应如何塑造阿森纳的下一个篇章</span>
          <span class="news-item-title-en">How Arteta's response to Brighton loss may shape Arsenal's next chapter</span>
          <span class="news-value-point">💡 Mikel Arteta本赛季对风险的胃口有所增加，但由于阿森纳希望保持领先地位，未能重塑将是一场更大的赌博</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq4g1pk9w8y0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家普拉斯（ FPL Pras ）回答了经理们在第六周比赛中面临的一些最大困境。" data-title="What to do with Joao Pedro? FPL gameweek six dilemmas" data-date="10-09 14:18" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 14:18</span>
          <span class="news-item-title">Joao Pedro怎么办？ FPL游戏周六难题</span>
          <span class="news-item-title-en">What to do with Joao Pedro? FPL gameweek six dilemmas</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家普拉斯（ FPL Pras …</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmy4x3908kpqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么曼城球员在周日前往安菲尔德时有很大的机会表现出团结和团结。" data-title="Maresca will be demanding a siege mentality from Man City" data-date="10-09 13:25" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 13:25</span>
          <span class="news-item-title">马雷斯卡将要求曼城采取围攻心态</span>
          <span class="news-item-title-en">Maresca will be demanding a siege mentality from Man City</span>
          <span class="news-value-point">💡 英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么曼城球员在周日前往安菲尔德时有很大的机会表现出团结和团结</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/09/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）对“托特纳姆热刺博士”保持警惕，奥利弗·格拉斯纳（ Oliver Glasner ）回到塞尔赫斯特公园（ Selhurst Park ） ，曼城会在安菲尔德（ Anfield ）召唤英超联赛最佳射手|查看联赛积分榜德克兰·赖斯在英格兰中场的未来角色是问题" data-title="Premier League: 10 things to look out for this weekend" data-date="10-09 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-09 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）对“托特纳姆热刺博士”保持警惕，奥利弗·格拉斯纳（ Oliver Glasner ）回到塞尔…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckpqg9388e7wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺的哈维·西蒙斯（ Xavi Simons ）在着名的美国大学哈佛（ Harvard ）就读，继续从长期受伤中恢复过来。" data-title="Spurs&#39; Simons enrols at iconic university Harvard" data-date="10-09 06:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 06:21</span>
          <span class="news-item-title">马刺队的西蒙斯入读标志性的哈佛大学</span>
          <span class="news-item-title-en">Spurs' Simons enrols at iconic university Harvard</span>
          <span class="news-value-point">💡 托特纳姆热刺的哈维·西蒙斯（ Xavi Simons ）在着名的美国大学哈佛（ Harvard ）就读，继续从长期受伤中恢复过来</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5zjx92v1mero?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）与明星水手主唱詹姆斯·沃尔什（ James Walsh ）以及英国广播公司的读者和人工智能进行了对本周末英超联赛的预测。" data-title="Sutton&#39;s predictions v Starsailor frontman James Walsh" data-date="10-09 04:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 04:46</span>
          <span class="news-item-title">Sutton对Starsailor主唱James Walsh的预测</span>
          <span class="news-item-title-en">Sutton's predictions v Starsailor frontman James Walsh</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）与明星水手主唱詹姆斯·沃尔什（ James Walsh ）以及英国广播公司的…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6n4ex2lgg2ko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="恩佐·马雷斯卡（ Enzo Maresca ）表示，他的球员“不太关心”曼城周围的115项英超指控的噪音。" data-title="Maresca says &#39;feeling is fantastic&#39; among Man City squad" data-date="10-09 04:40" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 04:40</span>
          <span class="news-item-title">马雷斯卡说曼城队的“感觉棒极了”</span>
          <span class="news-item-title-en">Maresca says 'feeling is fantastic' among Man City squad</span>
          <span class="news-value-point">💡 恩佐·马雷斯卡（ Enzo Maresca ）表示，他的球员“不太关心”曼城周围的115项英超指控的噪音</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/sport/live/2026/oct/08/football-qa-ask-ed-aarons-your-questions-as-the-premier-league-returns" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛在周六的回归，足球作家Ed Aarons回答了你关于曼城判决意味着什么，裁判是否会更严格，以及不要回头看愤怒是否是预言性的问题。Fearandloathingpart2问道：" data-title="‘Is the greatness of the Premier League a myth?’: Ed Aarons answered your football questions" data-date="10-08 23:48" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 23:48</span>
          <span class="news-item-title">“英超联赛的伟大是一个神话吗？ ’： Ed Aarons回答了你的足球问题</span>
          <span class="news-item-title-en">‘Is the greatness of the Premier League a myth?’: Ed Aarons answered your football questions</span>
          <span class="news-value-point">💡 随着英超联赛在周六的回归，足球作家Ed Aarons回答了你关于曼城判决意味着什么，裁判是否会更严格，以及不要回头看愤怒是否是预言性的问题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709952.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社北京10月9日电 国务委员谌贻琴9日在京会见载誉归来的第20届亚运会中国体育代表团，向全体运动员、教练员及工作人员转达党中央、国务院的热烈祝贺和亲切慰问，强调要牢记习近平总书记嘱托，戒骄戒躁、再接再厉，扎实推进洛杉矶奥运会备战工作。" data-title="谌贻琴在会见第20届亚运会中国体育代表团时强调 戒骄戒躁 再接再厉 扎实推进洛杉矶奥运会备战工作" data-date="10-09 22:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:26</span>
          <span class="news-item-title">谌贻琴在会见第20届亚运会中国体育代表团时强调 戒骄戒躁 再接再厉 扎实推进洛杉矶奥运会备战工作</span>
          <span class="news-value-point">💡 新华社北京10月9日电 国务委员谌贻琴9日在京会见载誉归来的第20届亚运会中国体育代表团，向全体运动员、教练员及工作人员转达党中央、国务院的热烈…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/144.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，据央视新闻今日报道，国际标准化组织（ISO）近日发布《船舶与海洋技术压载水管理系统（BWMS）电解法压载水管理系统的调试和测试程序》国际标准。该标准由中国牵头，美国、德国、加拿大、瑞士、挪威、丹麦等国专家参与制定。报道称，船舶压载水携带的外来生物是海洋生物入侵的重要途径之一，严重威胁海洋生态安全。压载水管理系统是杀灭这些入侵生物的关键设备，其杀灭效果取决于产品本身设计性能及安装后现场调试水平。IT之家从报道获悉，该标准规范了电解法压载水管理系统调试测试技术要求，规定系统运行时长不少于 60 分钟、排放采样体积不少于 1 立方米，并对大于等于 50 微米和 10 微米至 50 微米两类生物进行达标验证，确保满足国际公约排放标准，为全球船东、船厂、设备制造商和行业" data-title="遏制有害水生物传播，我国牵头制定的船舶压载水管理系统调试测试国际标准发布" data-date="10-09 22:22" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 22:22</span>
          <span class="news-item-title">遏制有害水生物传播，我国牵头制定的船舶压载水管理系统调试测试国际标准发布</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，据央视新闻今日报道，国际标准化组织（ISO）近日发布《船舶与海洋技术压载水管理系统（BWMS）电解法压载水管理系…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709946.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南宁10月9日电(记者 黄艳梅)广西壮族自治区卫生健康委员会9日介绍，该部门统筹推进食品安全标准体系建设、风险监测评估、营养健康科普、食品安全与营养创新平台建设等重点工作，不断提升食品安全治理能力，民众“舌尖上的安全”得到有效保障。" data-title="广西推进食品安全治理 建立地方特色食药物质目录制度" data-date="10-09 22:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:18</span>
          <span class="news-item-title">广西推进食品安全治理 建立地方特色食药物质目录制度</span>
          <span class="news-value-point">💡 中新网南宁10月9日电(记者 黄艳梅)广西壮族自治区卫生健康委员会9日介绍，该部门统筹推进食品安全标准体系建设、风险监测评估、营养健康科普、食品…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709926.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福州10月9日电 题：畲族服饰传承人的针线人生 一针一线绣“凤凰”" data-title="（八闽千姿）畲族服饰传承人的针线人生　一针一线绣“凤凰”" data-date="10-09 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:03</span>
          <span class="news-item-title">（八闽千姿）畲族服饰传承人的针线人生　一针一线绣“凤凰”</span>
          <span class="news-value-point">💡 中新社福州10月9日电 题：畲族服饰传承人的针线人生 一针一线绣“凤凰”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709841.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网伦敦10月9日电 (记者 欧阳开宇)英国环境、食品和农村事务部9日发布消息，随着野鸭、大雁等野生水禽迁徙至英国越冬，该国禽流感传入风险走高，官方呼吁各类鸟类饲养者完善防疫举措。" data-title="英国政府警示禽流感风险上升 呼吁养禽者强化生物安全" data-date="10-09 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 22:00</span>
          <span class="news-item-title">英国政府警示禽流感风险上升 呼吁养禽者强化生物安全</span>
          <span class="news-value-point">💡 中新网伦敦10月9日电 (记者 欧阳开宇)英国环境、食品和农村事务部9日发布消息，随着野鸭、大雁等野生水禽迁徙至英国越冬，该国禽流感传入风险走高…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/world/europe/mussolini-corpse-photo.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="经历了一次穿越阿尔卑斯山暴风雪的危险之旅，向世界展示了这位独裁者已经死了。" data-title="A Photo of Mussolini’s Corpse Led Page 1. How It Got There Is a Tale." data-date="10-09 21:57" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 21:57</span>
          <span class="news-item-title">墨索里尼的尸体主导的照片第1页。它是如何到达那里的，这是一个故事。</span>
          <span class="news-item-title-en">A Photo of Mussolini’s Corpse Led Page 1. How It Got There Is a Tale.</span>
          <span class="news-value-point">💡 经历了一次穿越阿尔卑斯山暴风雪的危险之旅，向世界展示了这位独裁者已经死了</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709924.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天(9日)白天" data-title="海南多地发布暴雨红色预警 局地出现大暴雨" data-date="10-09 21:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:52</span>
          <span class="news-item-title">海南多地发布暴雨红色预警 局地出现大暴雨</span>
          <span class="news-value-point">💡 今天(9日)白天</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709902.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网成都10月9日电 (刘忠俊 冉露茜)10月9日，新建的四川自贡至重庆永川高速公路四川段(以下简称“自永高速四川段”)首段路面功能层顺利摊铺，项目正式进入路面工程施工阶段，建设取得重要进展。" data-title="四川自贡至重庆永川高速公路四川段进入路面工程施工阶段" data-date="10-09 21:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:50</span>
          <span class="news-item-title">四川自贡至重庆永川高速公路四川段进入路面工程施工阶段</span>
          <span class="news-value-point">💡 中新网成都10月9日电 (刘忠俊 冉露茜)10月9日，新建的四川自贡至重庆永川高速公路四川段(以下简称“自永高速四川段”)首段路面功能层顺利摊铺…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709921.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="极目新闻记者 张屏 李碗容" data-title="开局之年看中国・潮涌荆楚｜他们是最值得追的星" data-date="10-09 21:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 21:39</span>
          <span class="news-item-title">开局之年看中国・潮涌荆楚｜他们是最值得追的星</span>
          <span class="news-value-point">💡 极目新闻记者 张屏 李碗容</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1008563/googlebook-software-impressions-thoughts-roundtable" target="_blank" rel="noopener" data-cat="zonghe" data-summary="谷歌的新操作系统开始步履维艰。新推出的五款Googlebook笔记本电脑的硬件从优秀到卓越不等，但当前状态下的软件是薄弱环节。The Verge的员工有四个人，" data-title="A week with Googlebooks: four notes from our testing so far" data-date="10-09 21:36" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 21:36</span>
          <span class="news-item-title">Googlebooks的一周：迄今为止我们测试的四个注意事项</span>
          <span class="news-item-title-en">A week with Googlebooks: four notes from our testing so far</span>
          <span class="news-value-point">💡 谷歌的新操作系统开始步履维艰</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/131.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，市场研究机构 Counterpoint Research 发文，认为苹果触控屏 MacBook Pro 预计将推动 OLED 笔记本电脑面板市场增长。预计 2026 年 OLED 笔记本面板出货量将同比增长 50%，2027 年还将进一步增长 24%。在高端笔记本显示面板市场中，Counterpoint 预计 OLED 面板相对于 Mini LED 面板将进一步扩大领先优势。预计 OLED 面板在该市场的出货占比将从 2025 年的 56% 升至 2026 年的 75%，Mini LED 面板的占比则将从 44% 降至 25%。除苹果产品换代外，高端 AI PC 需求持续增长，以及 OLED 面板技术和制造工艺的进步，也进一步推动 OLED 面板市场扩张。展望" data-title="Counterpoint：苹果全新 MacBook Pro 将推动 OLED 笔记本面板市场增长，预计今年市场出货量同比增长 50%" data-date="10-09 21:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 21:25</span>
          <span class="news-item-title">Counterpoint：苹果全新 MacBook Pro 将推动 OLED 笔记本面板市场增长，预计今年市场出货量同比增长 50%</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，市场研究机构 Counterpoint Research 发文，认为苹果触控屏 MacBook Pro 预计将推…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/130.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，酷比魔方掌玩 mini 4 Pro 今日发布，8.8 英寸黄金小尺寸，整机仅 295g、厚度 6.95mm，定位“千元便携小平板”。IT之家注意到，新品搭载天玑 7400 八核处理器，搭配 8.8 英寸 2.5K 分辨率 LCD 全贴合大屏，120Hz 智能高刷，支持 DC 护眼调光。后置镜头模组自带 RGB 炫彩灯环，可自定义灯效，兼具科技氛围感与消息呼吸提醒功能。这款小平板最大亮点是支持 4G 全网通双卡双待，内置 6500mAh 大容量电池，支持 20W PD 快充与旁路供电。BOX 音腔超线性对称双扬声器搭配 AST 音效，立体声饱满。原生干净安卓 16 系统，支持 TF 卡扩容。" data-title="酷比魔方掌玩 mini 4 Pro 发布：千元便携小平板，天玑 7400 八核处理器" data-date="10-09 21:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 21:25</span>
          <span class="news-item-title">酷比魔方掌玩 mini 4 Pro 发布：千元便携小平板，天玑 7400 八核处理器</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，酷比魔方掌玩 mini 4 Pro 今日发布，8.8 英寸黄金小尺寸，整机仅 295g、厚度 6.95mm，定位…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/127.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，由 SpaceRocket Games 开发、Toplitz Productions 发行的剧情驱动末日生存沙盒游戏《永冻纪元》（Permafrost）今日正式登陆 Steam 开启抢先体验，国区首发享 20% 折扣，折后价为 ¥ 95.20，优惠截止至 10 月 23 日。游戏支持简体中文界面与完整中文音频，目前尚无玩家评价。IT之家附游戏商品页（https://store.steampowered.com/app/2254990/Permafrost/）。《永冻纪元》背景设定在不远的未来，一系列灾难导致月球破碎，地球陷入永无止境的寒冬。玩家将扮演拥有重建能力的工程师“Rook”，凭借一段失联好友的无线电信号踏入这片冰封末日，在严酷环境中挣扎求生。官方介绍如" data-title="剧情驱动末日生存沙盒《永冻纪元》登陆 Steam：国区首发价 ¥95.20，支持简中配音" data-date="10-09 21:13" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 21:13</span>
          <span class="news-item-title">剧情驱动末日生存沙盒《永冻纪元》登陆 Steam：国区首发价 ¥95.20，支持简中配音</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，由 SpaceRocket Games 开发、Toplitz Productions 发行的剧情驱动末日生存沙盒…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1008658/meta-tiktok-bytedance-ads-ban" target="_blank" rel="noopener" data-cat="zonghe" data-summary="正如彭博早些时候报道的那样，由于主要社交媒体运营商之间的竞争加剧， Meta已禁止TikTok的中国母公司ByteDance在美国和其他几个国家投放广告。该禁令于周四生效" data-title="Meta is banning TikTok ads across its platforms" data-date="10-09 21:12" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 21:12</span>
          <span class="news-item-title">Meta正在其平台上禁止TikTok广告</span>
          <span class="news-item-title-en">Meta is banning TikTok ads across its platforms</span>
          <span class="news-value-point">💡 正如彭博早些时候报道的那样，由于主要社交媒体运营商之间的竞争加剧， Meta已禁止TikTok的中国母公司ByteDance在美国和其他几个国家…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/this-rtx-5070-gaming-laptop-is-still-the-absolute-best-usd1-299-you-can-spend-rtx-5060-and-5050-models-also-see-up-to-usd450-off" target="_blank" rel="noopener" data-cat="zonghe" data-summary="立即查看使用GeForce RTX 5070、RTX 5060和RTX 5050的游戏笔记本电脑的最佳优惠，价格低于$ 1,300。" data-title="This RTX 5070 gaming laptop is still the absolute best $1,299 you can spend — RTX 5060 and 5050 models also see up to $450 off" data-date="10-09 21:07" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-09 21:07</span>
          <span class="news-item-title">这款RTX 5070游戏笔记本电脑仍然是您可以花费的绝对最佳$ 1,299 — RTX 5060和5050型号也可享受高达$ 450的折扣</span>
          <span class="news-item-title-en">This RTX 5070 gaming laptop is still the absolute best $1,299 you can spend — RTX 5060 and 5050 models also see up to $450 off</span>
          <span class="news-value-point">💡 立即查看使用GeForce RTX 5070、RTX 5060和RTX 5050的游戏笔记本电脑的最佳优惠，价格低于$ 1,300</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-09 22:30（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
