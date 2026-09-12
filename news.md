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
      <span>2026-09-12 23:39 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/09/12/world/europe/trump-ireland-unification-remarks.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在1998年达成和平协议之前，这个问题一直是北爱尔兰数十年暴力的根源，美国在这个问题上正式保持中立。" data-title="特朗普表示，爱尔兰的统一将是“奇妙的” ，打破了先例" data-date="09-12 23:27" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 09-12 23:27</span>
      </div>
      <h2 class="hero-featured-title">特朗普表示，爱尔兰的统一将是“奇妙的” ，打破了先例</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/001/656.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 12 日消息，据央视财经今日报道，今年服贸会首次推出“金融 + 科创”的联展模式，让金融机构联合他们所赋能的科创企业同台参展。展台上除了金融产品，还有智能机械臂、运载火箭模型、人形机器人等硬科技，背后是算力贷、算力保、投贷联动等新型金融工具的支持。针对 AI 企业的“算力词元贷”自 8 月落地后，正加速向全国推广。服贸会上，多家银行发布相关产品。中国工商银行公司金融业务部副总经理胡贤文介绍，“算力基建贷”支持算力机房建设、GPU 服务器集群采购等新型算力基础设施建设，“算力研发贷”解决企业研发投入大、转化周期长的痛点。中邮金融资产投资有限公司投资业务一部副总经理闫冉介绍，公司今年 3 月份正式成立后，已在新一代信息技术、人工智能等国家重点支持的领域投资了十几个项目，总投资金" data-title="算力词元贷加速全国推广，支持机房建设、GPU 服务器集群采购" data-date="09-12 23:10" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">算力词元贷加速全国推广，支持机房建设、GPU 服务器集群采购</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/sep/12/liverpool-fulham-chelsea-hull-and-more-football-clockwatch-live-scores-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽️ News and updates from all of Saturday’s football action⚽️ Live scores | Tables | Top scorers | And email BarryChampionship: Standing on the opposition goalline, Birmingham City’s South Korean midfielder Paik Seung-Ho can’t miss as he heads his side in front at Pride Park from a wonderful Liam Millar inswinger of a corner. The visitors lead Derby" data-title="利物浦v富勒姆、切尔西v赫尔城等：足球钟表" data-date="09-12 23:38" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">利物浦v富勒姆、切尔西v赫尔城等：足球钟表</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/001/659.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，本周早些时候，Gamers Nexus、Level1Techs 和多名独立安全研究人员称，LG 电视会记录并上传用户数据。北京时间 12 日（今天），LG 出面再次反驳这些指控。LG 通过声明回应称，近期部分媒体报道可能让外界对 LG 智能电视的工作方式产生了误解，旗下电视不会持续记录或传输用户的对话，唤醒词识别也全部在设备本地完成。然而，Gamers Nexus 的测试显示，即使在人们通常认为 AI 助手早就停止监听之后，一台 LG 电视仍保存了大量环境对话日志。LG 还称，自动内容识别（ACR）、语音识别和基于兴趣的广告等功能均可由用户选择启用，且默认情况下不会开启。“ACR 使用电视内部音频处理器，而非扬声器，通过音频指纹技术识别内容，不会从电视收集屏幕" data-title="LG 再次回应“电视待机状态会录音”：不会持续记录或传输用户对话" data-date="09-12 23:38" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">LG 再次回应“电视待机状态会录音”：不会持续记录或传输用户对话</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/world/europe/trump-ireland-unification-remarks.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在1998年达成和平协议之前，这个问题一直是北爱尔兰数十年暴力的根源，美国在这个问题上正式保持中立。" data-title="特朗普表示，爱尔兰的统一将是“奇妙的” ，打破了先例" data-date="09-12 23:27" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 23:27</span>
          <span class="news-item-title">特朗普表示，爱尔兰的统一将是“奇妙的” ，打破了先例</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/iran-and-houthi-rebels-used-anthropics-claude-ai-to-target-us-warships-and-build-hypersonic-missiles-houthi-rebels-also-used-the-bot-to-code-ballistic-missile-guidance-systems" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“大撒旦”的人工智能派上用场。" data-title="伊朗和胡塞叛乱分子使用Anthropic的Claude AI瞄准美国军舰并制造高超音速导弹—胡塞叛乱分子还使用机器人对弹道导弹制导系统进行编码" data-date="09-12 23:03" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 23:03</span>
          <span class="news-item-title">伊朗和胡塞叛乱分子使用Anthropic的Claude AI瞄准美国军舰并制造高超音速导弹—胡塞叛乱分子还使用机器人对弹道导弹制导系统进行编码</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/us/politics/paxton-republican-pac-spending-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="与参议院共和党领导人结盟的一个组织已经预订了超过$ 5100万的广告。现在，肯·帕克斯顿（ Ken Paxton ）在数月被民主党竞争对手超越后，拥有了财务优势。" data-title="共和党团体在观望后急于在德克萨斯州获得帕克斯顿的援助" data-date="09-12 22:59" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 22:59</span>
          <span class="news-item-title">共和党团体在观望后急于在德克萨斯州获得帕克斯顿的援助</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695490.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社新德里9月12日电(记者郝薇薇#8195;刘锴)当地时间9月12日下午，国家主席习近平在印度新德里出席金砖国家领导人第十八次会晤期间会见印度总理莫迪。两国领导人坦诚深入交换意见，就中印要做伙伴达成重要共识。" data-title="习近平会见印度总理莫迪" data-date="09-12 22:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 22:49</span>
          <span class="news-item-title">习近平会见印度总理莫迪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695481.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社新德里9月12日电 (记者 郭金超 黄钰钦)当地时间9月12日下午，中国国家主席习近平在新德里出席金砖国家领导人第十八次会晤第一阶段会议。" data-title="详讯：习近平出席金砖国家领导人第十八次会晤第一阶段会议并发表重要讲话" data-date="09-12 22:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 22:17</span>
          <span class="news-item-title">详讯：习近平出席金砖国家领导人第十八次会晤第一阶段会议并发表重要讲话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695480.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月12日，国家主席习近平在印度新德里出席金砖国家领导人第十八次会晤第一阶段会议，发表题为《共担时代责任 勇做先锋力量》的重要讲话。习近平指出——" data-title="习言道｜开启金砖合作第三个“金色十年”" data-date="09-12 22:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 22:09</span>
          <span class="news-item-title">习言道｜开启金砖合作第三个“金色十年”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695479.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社新德里9月12日电(记者孙承斌 杨依军)当地时间9月12日下午，国家主席习近平在新德里出席金砖国家领导人第十八次会晤第一阶段会议。" data-title="习近平出席金砖国家领导人第十八次会晤第一阶段会议并发表重要讲话" data-date="09-12 21:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 21:46</span>
          <span class="news-item-title">习近平出席金砖国家领导人第十八次会晤第一阶段会议并发表重要讲话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695444.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社黑龙江漠河9月12日电 (记者 田德雨)黑龙江漠河气温日渐走低，当地供热部门于9月12日正式开栓供暖，比计划时间提前13天，保障当地市民和中外游客取暖需求。" data-title="“中国北极”漠河：提前13天开栓供暖　开启超长供暖季" data-date="09-12 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 21:22</span>
          <span class="news-item-title">“中国北极”漠河：提前13天开栓供暖　开启超长供暖季</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695438.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海9月12日电(范宇斌)“海上论道·觉群论坛”暨第三届“人间佛教的理论与实践”论坛12日在上海玉佛禅寺举行，探索佛教如何在奉法守规、礼仪戒律、日常行持、道德建设等方面同中华优秀传统文化相融合、与社会主义社会相适应。论坛现场发布新一辑《觉群佛学译丛》。" data-title="宗教界及学界在沪共探我国佛教中国化新实践" data-date="09-12 21:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 21:20</span>
          <span class="news-item-title">宗教界及学界在沪共探我国佛教中国化新实践</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695466.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月12日电 综合报道，据菲律宾海岸警卫队消息，9月12日，有关部门在巴拉望省附近海域起火船只上再次清点出多具遇难者遗体，这使得该事故的遇难人数上升至76人，目前仍有13人失踪。" data-title="菲律宾客船起火事故已致76人死亡" data-date="09-12 21:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 21:08</span>
          <span class="news-item-title">菲律宾客船起火事故已致76人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695381.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社浙江义乌9月12日电 题：印度商人尼罗斯：我也曾是“来中国试一下”的年轻人" data-title="印度商人尼罗斯：我也曾是“来中国试一下”的年轻人" data-date="09-12 19:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:59</span>
          <span class="news-item-title">印度商人尼罗斯：我也曾是“来中国试一下”的年轻人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695378.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社加德满都9月12日电(记者 崔楠)第三场“加德满都对话会”12日在尼泊尔首都加德满都举行。" data-title="“加德满都对话会”聚焦中尼防灾减灾合作" data-date="09-12 19:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:59</span>
          <span class="news-item-title">“加德满都对话会”聚焦中尼防灾减灾合作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695326.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网兴安盟9月12日电 (记者 张玮)记者12日从兴安盟袁隆平院士工作站获悉，2026年耐盐碱水稻测产活动在内蒙古自治区兴安盟科右中旗举行。经专家团现场实收测定，耐盐碱水稻平均亩产达552.67公斤，再创历史新高。" data-title="兴安盟袁隆平院士工作站耐盐碱水稻亩产超552公斤" data-date="09-12 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:35</span>
          <span class="news-item-title">兴安盟袁隆平院士工作站耐盐碱水稻亩产超552公斤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695325.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海9月12日电 (记者 孙自法 郑莹莹)2026浦江创新论坛开幕式9月12日在上海举行，国家自然科学基金长三角基础研究联合基金重大专项正式启动。" data-title="2026浦江创新论坛开幕 长三角基础研究联合基金重大专项正式启动" data-date="09-12 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:35</span>
          <span class="news-item-title">2026浦江创新论坛开幕 长三角基础研究联合基金重大专项正式启动</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗可能会对被俘的美国海军Anduril Dive-LD水下无人机进行逆向工程，因为德黑兰嘲笑损失，而华盛顿则淡化其军事价值。" data-title="伊朗可能对捕获的美国水下无人机进行逆向工程—几个伊朗大使馆嘲笑美国捕获，海军声称丢失的Anduril车辆有缺陷且未分类" data-date="09-12 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 19:30</span>
          <span class="news-item-title">伊朗可能对捕获的美国水下无人机进行逆向工程—几个伊朗大使馆嘲笑美国捕获，海军声称丢失的Anduril车辆有缺陷且未分类</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/001/656.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 12 日消息，据央视财经今日报道，今年服贸会首次推出“金融 + 科创”的联展模式，让金融机构联合他们所赋能的科创企业同台参展。展台上除了金融产品，还有智能机械臂、运载火箭模型、人形机器人等硬科技，背后是算力贷、算力保、投贷联动等新型金融工具的支持。针对 AI 企业的“算力词元贷”自 8 月落地后，正加速向全国推广。服贸会上，多家银行发布相关产品。中国工商银行公司金融业务部副总经理胡贤文介绍，“算力基建贷”支持算力机房建设、GPU 服务器集群采购等新型算力基础设施建设，“算力研发贷”解决企业研发投入大、转化周期长的痛点。中邮金融资产投资有限公司投资业务一部副总经理闫冉介绍，公司今年 3 月份正式成立后，已在新一代信息技术、人工智能等国家重点支持的领域投资了十几个项目，总投资金" data-title="算力词元贷加速全国推广，支持机房建设、GPU 服务器集群采购" data-date="09-12 23:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 23:10</span>
          <span class="news-item-title">算力词元贷加速全国推广，支持机房建设、GPU 服务器集群采购</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/652.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 12 日消息，9 月 11 日，2026 浦江创新论坛成果发布会在上海张江科学会堂举行。中国聚变能源有限公司（以下简称“中国聚变”）总工程师钟武律作为青年科学家代表出席并演讲。钟武律指出，当前全球聚变研究加速迈向“燃烧”阶段，实现氘氚聚变燃烧等离子体运行，与实现高增益持续燃烧的聚变等离子体之间，仍有根本性的科学门槛需要跨越：要依靠聚变产生的 α 粒子把等离子体维持在上亿度，进入长期自维持、稳定可控的“燃烧”状态。“只有把科学问题搞清楚，工程上才知道往哪走。”中国聚变正全力推进全球首个高温超导强场稳态燃烧实验平台 —— 中国环流四号研发，为解答这一科学之问提供关键支撑。“从一个好问题出发，向科学最深处走去”，中国聚变将把握高温超导与人工智能两大技术机遇，沿着“实验堆-示范堆-" data-title="中国聚变：正全力推进全球首个高温超导强场稳态燃烧实验平台研发" data-date="09-12 22:52" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 22:52</span>
          <span class="news-item-title">中国聚变：正全力推进全球首个高温超导强场稳态燃烧实验平台研发</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/994112/ai-data-center-pollution-health-epa" target="_blank" rel="noopener" data-cat="keji" data-summary="一群前美国环保署官员本周在一份简报和新报告中表示，唐纳德·特朗普总统正在以加快人工智能数据中心建设的名义削弱环境法规，增加了美国人的健康风险。他们敦促--也许是徒劳的--总统采取“数据中心健康保护[…]" data-title="特朗普正在向数据中心提供污染通行证" data-date="09-12 22:41" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 22:41</span>
          <span class="news-item-title">特朗普正在向数据中心提供污染通行证</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works" target="_blank" rel="noopener" data-cat="keji" data-summary="我们在腾讯通40系列GPU上测试了DLSS多帧生成。" data-title="我们在腾讯通40系列显卡上测试了非官方的DLSS多帧生成支持—新的MOD为旧显卡带来了腾讯通50系列独有的功能，它确实有效" data-date="09-12 22:08" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 22:08</span>
          <span class="news-item-title">我们在腾讯通40系列显卡上测试了非官方的DLSS多帧生成支持—新的MOD为旧显卡带来了腾讯通50系列独有的功能，它确实有效</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-12-2026-benchmarking-qwen-3-8-the-splintered-compute-economy-and-ai-breakthroughs" target="_blank" rel="noopener" data-cat="keji" data-summary="本周在Tom&#39;s Hardware Premium上，我们在一系列不同的硬件上对Qwen 3.8进行了基准测试，在从IFA 2026回归后对现代计算的状态进行了反思，并打破了一切" data-title="本周Tom&#39;s Hardware Premium ： 2026年9月12日—对标Qwen 3.8、分裂的计算经济和人工智能突破" data-date="09-12 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 20:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium ： 2026年9月12日—对标Qwen 3.8、分裂的计算经济和人工智能突破</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/988337/iphone-18-pro-max-preorder-buy" target="_blank" rel="noopener" data-cat="keji" data-summary="IPhone 18 Pro和18 Pro Max即将推出。这两款升级后的手机在2026年9月的苹果“Sunrise and shine”活动上与iPhone Duo和其他新装备一起发布，配备了更快的A20 Pro处理器，具有更强的GPU能力以及用于AI相关任务的更多神经核心，以及一些受欢迎的改进[…]" data-title="在哪里预订iPhone 18 Pro和Pro Max" data-date="09-12 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 20:00</span>
          <span class="news-item-title">在哪里预订iPhone 18 Pro和Pro Max</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487860.html" target="_blank" rel="noopener" data-cat="keji" data-summary="太初（杭州）集成电路有限公司新一代超智融合计算系统元碁Hypertintellix入选“算力中国·年度卓越成就”。" data-title="“算力中国·年度卓越成就”发布 太初元碁超智融合计算系统入选" data-date="09-12 19:38" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 19:38</span>
          <span class="news-item-title">“算力中国·年度卓越成就”发布 太初元碁超智融合计算系统入选</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI在过去几年中一直在日益困难的数学领域种植旗帜。本周，它获得了迄今为止最大的奖项之一：解决传奇的千年奖问题。在正常情况下，这被认为是一项历史性的成就。相反，许多数学家已经看到了OpenAI在[…]方面的不懈进步。" data-title="OpenAI只想赢" data-date="09-12 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 19:00</span>
          <span class="news-item-title">OpenAI只想赢</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487796.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Claude越界攻击真实系统，并非只是测试系统的设置问题，模型本身的安全问题也出了问题。" data-title="A社承认Claude安全对齐存在缺陷，但“尚无解决方案”" data-date="09-12 16:49" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 16:49</span>
          <span class="news-item-title">A社承认Claude安全对齐存在缺陷，但“尚无解决方案”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487752.html" target="_blank" rel="noopener" data-cat="keji" data-summary="触觉、记忆、Ego数据、自进化……这个世界模型全都有" data-title="探索RSI，生数新世界模型让机器人开始自我进化" data-date="09-12 16:15" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 16:15</span>
          <span class="news-item-title">探索RSI，生数新世界模型让机器人开始自我进化</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487701.html" target="_blank" rel="noopener" data-cat="keji" data-summary="FrontierMath Tier 4，饱和了" data-title="AI数学的最后一道高墙，塌了！GPT-6 Astra刷穿FrontierMath Tier 4" data-date="09-12 15:33" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 15:33</span>
          <span class="news-item-title">AI数学的最后一道高墙，塌了！GPT-6 Astra刷穿FrontierMath Tier 4</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487688.html" target="_blank" rel="noopener" data-cat="keji" data-summary="冲刺港股IPO" data-title="Kimi突发K2.8：性能逼近K3，百万上下文全员开放" data-date="09-12 13:58" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 13:58</span>
          <span class="news-item-title">Kimi突发K2.8：性能逼近K3，百万上下文全员开放</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/562.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 12 日消息，阿里宣布旗下企业级通用 Agent 智能体产品千问办公已上架麒麟软件商店，即日起，银河麒麟操作系统用户在软件商店搜索千问办公，即可一键下载安装体验。目前，千问办公已全面支持 Windows、macOS、HarmonyOS、银河麒麟、统信 UOS 等全部主流操作系统。阿里表示，千问办公和麒麟软件团队此前进行了联合攻坚，在系统登录联动、设备互联、技能调用等核心链路展开了深度协作，并针对办公全场景适配优化，实现了千问办公在银河麒麟操作系统上的原生级运行效果，可为用户提供稳定、流畅的 AI 办公体验。例如，银河麒麟操作系统用户不仅可以体验通用办公 Agent 的能力，还可以使用千问办公发送钉钉消息、总结群聊内容、生成周报、预定日程会议、总结会议纪要、创建钉钉文档和 A" data-title="阿里千问办公上架麒麟软件商店，已原生适配全部主流操作系统" data-date="09-12 13:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 13:47</span>
          <span class="news-item-title">阿里千问办公上架麒麟软件商店，已原生适配全部主流操作系统</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487653.html" target="_blank" rel="noopener" data-cat="keji" data-summary="25位菲尔兹奖得主联名吹哨" data-title="陶哲轩邓煜究竟在反对什么：AI暴力解题摧毁人类数学精神" data-date="09-12 12:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 12:53</span>
          <span class="news-item-title">陶哲轩邓煜究竟在反对什么：AI暴力解题摧毁人类数学精神</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家成立两年的初创公司的融资是在Mecka宣布其A轮融资的几个月后进行的。" data-title="在急于获取机器人训练数据之际， Mecka AI对红杉领导的交易的估值接近5亿美元" data-date="09-12 06:58" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 06:58</span>
          <span class="news-item-title">在急于获取机器人训练数据之际， Mecka AI对红杉领导的交易的估值接近5亿美元</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/12/liverpool-fulham-chelsea-hull-and-more-football-clockwatch-live-scores-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽️ News and updates from all of Saturday’s football action⚽️ Live scores | Tables | Top scorers | And email BarryChampionship: Standing on the opposition goalline, Birmingham City’s South Korean midfielder Paik Seung-Ho can’t miss as he heads his side in front at Pride Park from a wonderful Liam Millar inswinger of a corner. The visitors lead Derby" data-title="利物浦v富勒姆、切尔西v赫尔城等：足球钟表" data-date="09-12 23:38" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 23:38</span>
          <span class="news-item-title">利物浦v富勒姆、切尔西v赫尔城等：足球钟表</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-sunderland-arsenal-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰和阿森纳今天的票价如何？以下是需要了解的信息，包括开球时间、电视频道和直播选项阿森纳可以在周六在光明体育场取得胜利，继续他们本赛季的强劲开局。然而，桑德兰在本场比赛中表现不佳，上赛季他们以2-2战平枪手。米克尔·阿尔特塔（ Mikel Arteta ）的卫冕冠军在他们的力量巅峰时表现出色。阿森纳赢得了所有五场比赛" data-title="今日英超联赛：如何观看桑德兰对阿森纳、电视频道和直播" data-date="09-12 22:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 22:00</span>
          <span class="news-item-title">今日英超联赛：如何观看桑德兰对阿森纳、电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-spurs-everton-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺队和埃弗顿队今天的表现如何？以下是需要了解的信息，包括开球时间、电视频道和直播选项热刺在经历了一个几乎被英超联赛淘汰的赛季之后的复苏尚未实现。事实上，罗伯托·德·泽比的球队仍在寻找他们在联赛赛季的第一场胜利，对周六的比赛给予一定的重视。任何低于马刺的胜利都可能改变气氛" data-title="今日英超联赛：如何观看马刺对埃弗顿，电视频道和直播" data-date="09-12 19:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 19:30</span>
          <span class="news-item-title">今日英超联赛：如何观看马刺对埃弗顿，电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-spurs-everton-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺队和埃弗顿队今天的表现如何？以下是需要了解的信息，包括开球时间、电视频道和直播选项热刺在经历了一个几乎被英超联赛淘汰的赛季之后的复苏尚未实现。事实上，罗伯托·德·泽比的球队仍在寻找他们在联赛赛季的第一场胜利，对周六的比赛给予一定的重视。任何低于马刺的胜利都可能改变气氛" data-title="今日英超联赛：如何观看热刺对阵埃弗顿的比赛、电视频道和直播" data-date="09-12 19:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 19:30</span>
          <span class="news-item-title">今日英超联赛：如何观看热刺对阵埃弗顿的比赛、电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695391.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网9月12日 据英国《卫报》当地时间12日报道，本周早些时候导致英国数千趟航班停飞的空中交通管制系统故障，据称是由一架军用飞机向系统输入虚假飞行数据所引发的。" data-title="英国超2000架次航班突然被取消 英媒：一军机输入虚假飞行数据所致" data-date="09-12 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:29</span>
          <span class="news-item-title">英国超2000架次航班突然被取消 英媒：一军机输入虚假飞行数据所致</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj9x7e40gr2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="摩纳哥和塞内加尔中场球员拉明·卡马拉（ Lamine Camara ）表示，他正在从失败的4710万英镑转会切尔西。" data-title="“我已经翻开了一页” -卡马拉对切尔西的交易崩溃" data-date="09-12 18:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 18:07</span>
          <span class="news-item-title">“我已经翻开了一页” -卡马拉对切尔西的交易崩溃</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-liverpool-fulham-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和富勒姆今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项2026-27赛季英超联赛的积分榜已经开始成形，利物浦的目标是在上个赛季的压倒性竞选之后更接近积分榜榜首，安菲尔德队获得了第五名。对于富勒姆来说，本赛季可能是关于生存的。山寨队已经失去了他们的三个开场赛程，" data-title="今日英超联赛：如何观看利物浦对富勒姆、电视频道和直播" data-date="09-12 17:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 17:00</span>
          <span class="news-item-title">今日英超联赛：如何观看利物浦对富勒姆、电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy5zp9llp3ro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="新任队长鲁本·迪亚斯（ Ruben Dias ）表示，曼城带来了“渴望获胜”的夏季签约球员，整个球队正在“接受”新任经理恩佐·马雷斯卡（ Enzo Maresca ）的“想法”。" data-title="新曼城签约迫切希望获胜" data-date="09-12 13:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 13:24</span>
          <span class="news-item-title">新曼城签约迫切希望获胜</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy5zp9llp3ro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="新任队长鲁本·迪亚斯（ Ruben Dias ）表示，曼城带来了“渴望获胜”的夏季签约球员，整个球队正在“接受”新任经理恩佐·马雷斯卡（ Enzo Maresca ）的“想法”。" data-title="曼城新援渴望胜利" data-date="09-12 13:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 13:24</span>
          <span class="news-item-title">曼城新援渴望胜利</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c1j4z1ry29jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西主教练哈比·阿隆索表示，前锋若昂·佩德罗在风格上与他的前皇家马德里队友卡里姆·本泽马相似，与曼城的埃尔林·哈兰德相当。" data-title="像本泽马和哈兰德一样好-阿隆索和若昂·佩德罗" data-date="09-12 05:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 05:30</span>
          <span class="news-item-title">像本泽马和哈兰德一样好-阿隆索和若昂·佩德罗</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c1j4z1ry29jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西主教练哈比·阿隆索表示，前锋若昂·佩德罗在风格上与他的前皇家马德里队友卡里姆·本泽马相似，与曼城的埃尔林·哈兰德相当。" data-title="像本泽马和哈兰德一样出色 - 阿隆索对若昂·佩德罗" data-date="09-12 05:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 05:30</span>
          <span class="news-item-title">像本泽马和哈兰德一样出色 - 阿隆索对若昂·佩德罗</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/premier-league-news-iraola-values-wirtzs-work-ethic-moyes-backs-senior-citizen-grealish" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦主教练坚持认为，中场球员应该以他的影响力而不是数字来评判。继续阅读……" data-title="英超新闻： Iraola重视Wirtz的职业道德； Moyes支持“老年人” Grealish" data-date="09-12 05:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 05:30</span>
          <span class="news-item-title">英超新闻： Iraola重视Wirtz的职业道德； Moyes支持“老年人” Grealish</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cr50q58vqggo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺前锋理查利森提议搬到瓦斯科达伽马，但在巴西未来的不确定性中失败了。" data-title="Richarlison搬到Vasco da Gama" data-date="09-12 04:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 04:49</span>
          <span class="news-item-title">Richarlison搬到Vasco da Gama</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/ballon-dor-shortlist-shows-up-premier-leagues-attacking-failings-but-tide-could-be-turning" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="English top flight’s forwards are not well represented on the list, reflecting a season of set-piece grapple, but 2026-27 already looks brighterPremier League representation is low when it comes to the 16 attacking players on this year’s Ballon d’Or shortlist. Manchester United’s Bruno Fernandes and Manchester City’s Erling Haaland are there but Co" data-title="Ballon d &#39;Or入围名单显示了英超联赛的进攻失败–但潮流可能正在转变" data-date="09-12 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 03:00</span>
          <span class="news-item-title">Ballon d 'Or入围名单显示了英超联赛的进攻失败–但潮流可能正在转变</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日，在桑德兰主办阿森纳之后，曼城前往曼联参加一场有趣的德比比赛周六下午3点场地别墅公园继续阅读..." data-title="英超球队新闻：周末动作的预测阵容" data-date="09-12 01:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 01:16</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/001/659.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，本周早些时候，Gamers Nexus、Level1Techs 和多名独立安全研究人员称，LG 电视会记录并上传用户数据。北京时间 12 日（今天），LG 出面再次反驳这些指控。LG 通过声明回应称，近期部分媒体报道可能让外界对 LG 智能电视的工作方式产生了误解，旗下电视不会持续记录或传输用户的对话，唤醒词识别也全部在设备本地完成。然而，Gamers Nexus 的测试显示，即使在人们通常认为 AI 助手早就停止监听之后，一台 LG 电视仍保存了大量环境对话日志。LG 还称，自动内容识别（ACR）、语音识别和基于兴趣的广告等功能均可由用户选择启用，且默认情况下不会开启。“ACR 使用电视内部音频处理器，而非扬声器，通过音频指纹技术识别内容，不会从电视收集屏幕" data-title="LG 再次回应“电视待机状态会录音”：不会持续记录或传输用户对话" data-date="09-12 23:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 23:38</span>
          <span class="news-item-title">LG 再次回应“电视待机状态会录音”：不会持续记录或传输用户对话</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/658.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，惠普星 Desk Mini 迷你主机现已上架电商平台，将于 9 月 16 日 0:00 开售，售价 9599 元起：Ultra 5 325、16GB+1TB：9599 元，国补到手价 8159.15 元Ultra 7 356H、16GB+1TB：10499 元，国补到手价 8999 元这款新品搭载英特尔酷睿 Ultra 5 325（8 核 8 线程、55W）或 Ultra 7 356H（16 核 16 线程、65W）处理器，板载 16GB DDR5 内存，双 PCIe SSD 插槽，支持 Wi-Fi 7 和蓝牙 6.0。这款迷你主机重约 475g，尺寸为 130×130×48 mm，体积约 0.8L，电源线采用隐藏式走线。IT之家附这款新品接口如下：正面：雷电" data-title="惠普星 Desk Mini 迷你主机上架：Ultra 5 325/7 356H，9599 元起" data-date="09-12 23:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 23:27</span>
          <span class="news-item-title">惠普星 Desk Mini 迷你主机上架：Ultra 5 325/7 356H，9599 元起</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/994333/lg-responds-to-tv-spying-allegations" target="_blank" rel="noopener" data-cat="zonghe" data-summary="本周早些时候，游戏玩家Nexus、Level1Techs和独立安全研究人员详细介绍了有关LG电视如何记录和上传用户数据的一些令人担忧的发现。现在，该公司正在反驳这些指控，称“最近的一些媒体报道可能导致了对LG智能电视工作原理的误解。“ LG发布了一款[…]" data-title="LG回应电视间谍指控" data-date="09-12 23:19" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 23:19</span>
          <span class="news-item-title">LG回应电视间谍指控</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/657.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，荣耀今日公布 SmallRig 专业视频拓展套件，适配荣耀 Magic9 Pro Max，将于 9 月 28 日发布。据官方介绍，荣耀 Magic9 Pro Max 支持阿莱电影模式，拥有阿莱 LogC3 视频管线、电影级枪麦收音、峰值对焦、伪色监看。搭配专业视频拓展套件，轻松应对复杂场景。超清双两亿，掌中电影机。荣耀 Magic9 Pro Max 预计将搭载“双 2 亿”影像方案，其中主摄采用 200MP 1/1.28 英寸传感器，潜望长焦采用 200MP 1/1.4 英寸传感器，并配备专业影像手柄以及 G200（200mm）、G500（500mm）两款增距镜配件。影像方面，荣耀 Magic9 Pro Max 将联合百年电影品牌 ARRI，引入专业电影色彩科" data-title="荣耀公布 SmallRig 专业视频拓展套件：适配 Magic9 Pro Max，9 月 28 日发布" data-date="09-12 23:17" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 23:17</span>
          <span class="news-item-title">荣耀公布 SmallRig 专业视频拓展套件：适配 Magic9 Pro Max，9 月 28 日发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695488.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月12日电(记者 高萌)当开学典礼遇上大雨，作为校长是选择念完准备好的发言稿，还是让同学们先避雨？" data-title="中新网评宁大校长雨中三句话致辞：比仪式更重要的是体谅" data-date="09-12 22:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 22:31</span>
          <span class="news-item-title">中新网评宁大校长雨中三句话致辞：比仪式更重要的是体谅</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695483.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社广州9月12日电 (记者 蔡敏婕)粤港澳大湾区核心枢纽工程——狮子洋通道跨西樵水道钢桁梁桥12日完成11个节段拼装，实现精准合龙。" data-title="中国内地单跨跨径最大的双层钢桁梁桥实现合龙" data-date="09-12 22:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 22:16</span>
          <span class="news-item-title">中国内地单跨跨径最大的双层钢桁梁桥实现合龙</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/ikea-releases-new-skyrim-mod-that-adds-gloriously-mundane-kallax-shelving-unit-as-your-newest-companion-free-collab-provides-a-drab-flatpack-answer-to-your-loot-woes" target="_blank" rel="noopener" data-cat="zonghe" data-summary="宜家宣布为PC或Xbox上的The Elder Scrolls V ： Skyrim特别版玩家推出Kallax Storageborn配套产品。" data-title="宜家推出全新Skyrim mod ，为您的最新伴侣添加了光彩夺目的Kallax货架单元--免费合作为您的战利品困境提供了单调的平装答案" data-date="09-12 21:31" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 21:31</span>
          <span class="news-item-title">宜家推出全新Skyrim mod ，为您的最新伴侣添加了光彩夺目的Kallax货架单元--免费合作为您的战利品困境提供了单调的平装答案</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695443.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社浙江嘉兴9月12日电 (黄彦君)“之前就来过平湖参赛，这次再来有全新感受。徐家埭村的乡村棒球场按照国际专业标准打造，配套设施完善，平整的草皮、规范的场地，跑动和竞技体验都特别好。”9月12日，在浙江省嘉兴市平湖市徐家埭村，台湾慢速垒球选手庄佳钧说。" data-title="嘉兴平湖办浙台棒垒球交流 选手大半是台青" data-date="09-12 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 21:22</span>
          <span class="news-item-title">嘉兴平湖办浙台棒垒球交流 选手大半是台青</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/994314/tiff-2026-wildwood-stuffed-julian" target="_blank" rel="noopener" data-cat="zonghe" data-summary="由于日程安排上的不便，我在多伦多国际电影节的第二天只能观看两部电影，但我确实设法提前了解了今年最受期待的电影之一的一些迷人细节。即使你不知道这个名字[…]" data-title="莱卡定格幻想怀尔德伍德看上去好光滑" data-date="09-12 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 21:00</span>
          <span class="news-item-title">莱卡定格幻想怀尔德伍德看上去好光滑</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695429.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北海9月12日电(翟李强 罗虹莉 林启波)9月12日，2026年合浦县中秋国庆非遗系列活动在广西合浦月饼小镇启动。活动以非遗月饼为核心纽带，串联千年海丝文脉、本土民俗风情与文旅特色产业，为民众打造一场沉浸式、多样化的非遗盛宴，系列活动将持续开展至10月3日。" data-title="广西合浦中秋国庆非遗系列活动启幕 168斤的大月饼免费吃" data-date="09-12 20:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 20:58</span>
          <span class="news-item-title">广西合浦中秋国庆非遗系列活动启幕 168斤的大月饼免费吃</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695427.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网青岛9月12日电 (王禹)印度辣椒加工厂里，一台蓝白相间的“箱子”正快速输出去柄后的辣椒。这台由胶州市胶莱街道农民李志敏研发的辣椒除柄机，在当地被亲切地称作“中国的宝马”。" data-title="从单机突围到集群拓局 上合示范区小农机耕拓印度大市场" data-date="09-12 20:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 20:51</span>
          <span class="news-item-title">从单机突围到集群拓局 上合示范区小农机耕拓印度大市场</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695424.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网天津9月12日电 (薛淳月)京津冀残疾人艺术作品展11日在天津图书馆文化中心馆举行，经专家评审后甄选166件作品入展，涵盖书法、绘画、摄影等类别，集中展现京津冀三地残疾人创作者的艺术实践。" data-title="京津冀残疾人艺术作品展在津举行 166件作品集中亮相" data-date="09-12 20:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 20:50</span>
          <span class="news-item-title">京津冀残疾人艺术作品展在津举行 166件作品集中亮相</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695413.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网黄山9月12日电 (任俊翔)第八届全国茶业职业技能竞赛安徽分赛区茶叶加工(精制)项目12日在黄山市屯溪区开赛，19名制茶能手同台竞技。" data-title="制茶能手齐聚黄山 比拼茶叶精制加工技艺" data-date="09-12 20:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 20:31</span>
          <span class="news-item-title">制茶能手齐聚黄山 比拼茶叶精制加工技艺</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695384.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川9月12日电 (记者 李佩珊)9月12日，2026年全国“和美乡村 ‘村钓’展示交流活动”在银川市贺兰县常信乡开赛，300名垂钓爱好者齐聚现场，开启一场乡土气息浓厚的垂钓盛会。" data-title="中国“村钓”开赛 钓友相聚宁夏贺兰竞逐渔乐" data-date="09-12 20:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 20:02</span>
          <span class="news-item-title">中国“村钓”开赛 钓友相聚宁夏贺兰竞逐渔乐</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695373.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北海9月12日电 (黄令妍 李荣霞)9月11日，2026年广西野生动植物保护宣传月主题宣传活动在北海市启动。活动主题为“拒绝野味消费，共护八桂生灵”，聚焦抵制滥食野生动物陋习，从消费源头遏制野生动植物非法交易链条。" data-title="广西多举措保护野生动植物 遏制非法交易" data-date="09-12 19:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:57</span>
          <span class="news-item-title">广西多举措保护野生动植物 遏制非法交易</span>
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


---

<p class="news-updated">🕐 抓取更新于 2026-09-12 23:39（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
