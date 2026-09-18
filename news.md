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
      <span>2026-09-18 20:18 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/09-18/10699160.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宋卡9月18日电(记者 李映民)中国驻宋卡总领事馆17日举办庆祝中华人民共和国成立77周年招待会。领区各府府尹、宗教人士、华侨华人、媒体、中资机构、留学生代表等900余人应邀出席。" data-title="中国驻宋卡总领馆举办国庆招待会" data-date="09-18 20:07" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-18 20:07</span>
      </div>
      <h2 class="hero-featured-title">中国驻宋卡总领馆举办国庆招待会</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/004/312.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 18 日消息，过去两年，甲骨文花费数十亿美元帮助其他企业运行 AI。然而相比之下，自家公司全面引入 AI 的时间却晚得多。据《商业内幕》今天（18 日）晚间报道，甲骨文联合 CEO 克莱 · 马古尔克在内部员工大会上坦言，直到去年，公司还没有找到让生成式 AI 在整个员工队伍中真正发挥作用的方法。ChatGPT 和 Codex 投入使用后，甲骨文员工编写代码的速度大幅提升，同时也把原本隐藏在其他环节的瓶颈暴露了出来。马古尔克说：“回想一年前的情况，我觉得当时我们还没弄明白，怎样才能真正让 AI 对我们自己这么有用。”去年，甲骨文尝试把 AI 用于客户支持，但开发、财务和销售等部门还没有大范围应用。甲骨文首席信息官杰伊 · 埃文斯告诉员工，转折出现在今年 4 月和 5 月，公" data-title="甲骨文烧数十亿美元帮其他企业运行 AI，公司内部推广 AI 却并不顺利" data-date="09-18 20:06" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">甲骨文烧数十亿美元帮其他企业运行 AI，公司内部推广 AI 却并不顺利</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/sep/18/england-squad-to-be-announced-premier-league-latest-european-reaction-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 周五的团队新闻、新闻发布会和分析⚽The Knowledge ：第一批复制品套件是什么时候？联系我们⚽！发送电子邮件给Dom ，提供任何想法Alexander-Arnold、Alex Scott、Cole Palmer和Rio Ngumoha都会参与进来。菲尔·福登（ Phil Foden ）无处可去。所有小队都在下面。继续阅读..." data-title="图切尔解释了亚历山大-阿诺德和帕尔默英格兰的回忆；西班牙队在休达透露：足球新闻–现场" data-date="09-18 20:15" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">图切尔解释了亚历山大-阿诺德和帕尔默英格兰的回忆；西班牙队在休达透露：足球新闻–现场</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/004/315.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 18 日消息，据央视新闻报道，车辆年检、尾气检测是守护空气质量的重要关口。为堵住机动车尾气检测弄虚作假、检测不规范等问题，生态环境部、市场监管总局近日联合印发《关于推进机动车排放检验机构监管改革提升排放检验质量的意见》，今后，严重弄虚作假机构将被坚决清出市场。IT之家获悉，《意见》要求聚焦机动车排放检验机构设备管理、检验操作、日常运维、人员技能等薄弱环节，建立健全权责清晰、运行规范、全程可溯、常态监管的全过程管理体系。要坚持源头严管，指导机动车排放检验机构按照《生态环境法典》要求落实主体责任，提升检验数据质量和检验合规水平。在机构准入和退出管理上，《意见》要求，加强资质认定专家评审，确保排放检验设备和人员符合条件要求，对违法机构和人员依法处罚惩戒，严重弄虚作假机构要被坚决清" data-title="两部门整治机动车排放检验乱象：将严重弄虚作假机构清出市场" data-date="09-18 20:19" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">两部门整治机动车排放检验乱象：将严重弄虚作假机构清出市场</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699160.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宋卡9月18日电(记者 李映民)中国驻宋卡总领事馆17日举办庆祝中华人民共和国成立77周年招待会。领区各府府尹、宗教人士、华侨华人、媒体、中资机构、留学生代表等900余人应邀出席。" data-title="中国驻宋卡总领馆举办国庆招待会" data-date="09-18 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 20:07</span>
          <span class="news-item-title">中国驻宋卡总领馆举办国庆招待会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699154.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社银川9月18日电(记者 李佩珊)“制作漆扇的经历令我十分难忘，这不只是一件手工艺品，更是我要带回祖国的一份中国文化印记。”在第十届“一带一路”青少年创客营与教师研讨活动(中国-阿拉伯国家青少年创客营)18日闭营的现场，印度学生哈娜(Ravikumar Mythili Harsini)如是谈及她的感受。" data-title="丝路青年以AI短视频记录“中国文化印记”" data-date="09-18 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 20:07</span>
          <span class="news-item-title">丝路青年以AI短视频记录“中国文化印记”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699128.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月18日电 据国家市场监督管理总局网站消息，18日，国务院食安办发布《国务院食安办关于做好2026年中秋、国庆期间食品安全工作的通知》，要求各地食(药)安办要高度重视，坚持底线思维，加强问题导向，督促相关部门切实提高风险防控意识，采取积极措施，着力消除问题隐患，确保人民群众度过欢乐祥和的节日假期。" data-title="国务院食安办部署中秋、国庆期间食品安全工作" data-date="09-18 19:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:49</span>
          <span class="news-item-title">国务院食安办部署中秋、国庆期间食品安全工作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-18/10699103.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆9月18日电 (记者 刘相琳)记者18日从重庆市发展改革委获悉，该委近日正式批复重庆玉滩大型灌区工程可行性研究报告，标志着项目建设取得关键性突破，进入全面推进实施阶段。" data-title="重庆首个新建大型灌区工程可行性研究报告获批 新增灌溉面积30万亩" data-date="09-18 19:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:48</span>
          <span class="news-item-title">重庆首个新建大型灌区工程可行性研究报告获批 新增灌溉面积30万亩</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-18/10699112.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月18日电 据中央纪委国家监委驻中国银行纪检监察组、天津市纪委监委消息：日前，中央纪委国家监委驻中国银行纪检监察组、天津市监委对中国银行浙江省分行原党委书记、行长程军严重违纪违法问题进行了立案审查调查。" data-title="中国银行浙江省分行原党委书记、行长程军被“双开”" data-date="09-18 19:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:48</span>
          <span class="news-item-title">中国银行浙江省分行原党委书记、行长程军被“双开”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699129.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="莫桑比克南部伊尼扬巴内省当地时间17日晚发生一起交通事故，造成至少17人死亡、2人受伤，其中1人伤势严重。" data-title="莫桑比克南部交通事故致至少17人死亡" data-date="09-18 19:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:23</span>
          <span class="news-item-title">莫桑比克南部交通事故致至少17人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699122.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社吉隆坡9月18日电(记者 刘育英)马来西亚最高元首易卜拉欣18日批准对前总理纳吉布给予有条件特赦，准许其以居家监禁方式服完剩余刑期，刑期至2028年8月23日。" data-title="马来西亚前总理纳吉布获准居家服完剩余刑期" data-date="09-18 19:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:19</span>
          <span class="news-item-title">马来西亚前总理纳吉布获准居家服完剩余刑期</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699123.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月18日，马来西亚特赦局宣布，允许马前总理纳吉布以居家监禁的方式服役完剩余刑期，至2028年8月。" data-title="马来西亚前总理纳吉布将以居家监禁形式继续服刑" data-date="09-18 19:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:09</span>
          <span class="news-item-title">马来西亚前总理纳吉布将以居家监禁形式继续服刑</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699107.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间18日，巴基斯坦西北部开伯尔-普什图省一座清真寺附近发生爆炸。当地警方称，袭击已导致16人死亡。" data-title="巴基斯坦西北部爆炸事故已致16人死亡" data-date="09-18 18:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 18:01</span>
          <span class="news-item-title">巴基斯坦西北部爆炸事故已致16人死亡</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/18/podcasts/the-headlines/russia-election-results-rfk-jr-vaccines.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="此外，还有周五的新闻测验。" data-title="克里姆林宫如何获得它想要的选举结果， R.F.K. Jr.集会疫苗怀疑论者" data-date="09-18 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-18 18:00</span>
          <span class="news-item-title">克里姆林宫如何获得它想要的选举结果， R.F.K. Jr.集会疫苗怀疑论者</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/18/world/europe/putin-russia-election-ideas.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="俄罗斯正在举行一场几乎对任何人都不重要的选举--除了弗拉基米尔· V ·普京总统及其核心圈子。" data-title="为什么独裁者关心人们的想法" data-date="09-18 17:47" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-18 17:47</span>
          <span class="news-item-title">为什么独裁者关心人们的想法</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-18/10699065.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月18日电 据中央纪委国家监委驻中国石化纪检监察组、宁波市纪委监委消息：中石化宁波工程有限公司原党委书记、执行董事许一君涉嫌严重违纪违法，目前正接受中央纪委国家监委驻中国石化纪检监察组纪律审查和浙江省宁波市监察委员会监察调查。" data-title="中石化宁波工程有限公司原党委书记许一君接受审查调查" data-date="09-18 17:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 17:13</span>
          <span class="news-item-title">中石化宁波工程有限公司原党委书记许一君接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/18/us/politics/alexandria-ocasio-cortez-donation-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="The news has reignited speculation about whether the progressive representative from the Bronx is considering a run for senator or president." data-title="Ocasio-Cortez Donates to N.Y. Democrats, Will Barnstorm State Ahead of Midterms" data-date="09-18 17:04" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-18 17:04</span>
          <span class="news-item-title">Ocasio-Cortez Donates to N.Y. Democrats, Will Barnstorm State Ahead of Midterms</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/18/us/politics/ashley-hinson-trump-iowa-senate-race.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Representative Ashley Hinson is hoping to keep a crucial Senate seat red in Iowa, where the president has created major headwinds for her party." data-title="Ashley Hinson, a Republican ‘Minivan-Driving Mom,’ Steers Away From Trump in Midterm Elections" data-date="09-18 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-18 17:02</span>
          <span class="news-item-title">Ashley Hinson, a Republican ‘Minivan-Driving Mom,’ Steers Away From Trump in Midterm Elections</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-18/10699058.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="九一八事变是日本蓄谋已久、精心策划的侵略战争行为，但日本民众从日本媒体上看到的却是日本关东军捏造的“中国军队炸毁南满铁路”，以及将日军侵略行为粉饰为“自卫”的虚假报道。" data-title="九一八事变爆发95周年 日本“自卫”谎言还要骗多久" data-date="09-18 16:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 16:56</span>
          <span class="news-item-title">九一八事变爆发95周年 日本“自卫”谎言还要骗多久</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/004/312.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 18 日消息，过去两年，甲骨文花费数十亿美元帮助其他企业运行 AI。然而相比之下，自家公司全面引入 AI 的时间却晚得多。据《商业内幕》今天（18 日）晚间报道，甲骨文联合 CEO 克莱 · 马古尔克在内部员工大会上坦言，直到去年，公司还没有找到让生成式 AI 在整个员工队伍中真正发挥作用的方法。ChatGPT 和 Codex 投入使用后，甲骨文员工编写代码的速度大幅提升，同时也把原本隐藏在其他环节的瓶颈暴露了出来。马古尔克说：“回想一年前的情况，我觉得当时我们还没弄明白，怎样才能真正让 AI 对我们自己这么有用。”去年，甲骨文尝试把 AI 用于客户支持，但开发、财务和销售等部门还没有大范围应用。甲骨文首席信息官杰伊 · 埃文斯告诉员工，转折出现在今年 4 月和 5 月，公" data-title="甲骨文烧数十亿美元帮其他企业运行 AI，公司内部推广 AI 却并不顺利" data-date="09-18 20:06" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-18 20:06</span>
          <span class="news-item-title">甲骨文烧数十亿美元帮其他企业运行 AI，公司内部推广 AI 却并不顺利</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-in-a-web-browser-using-webgpu-147mb-browser-port-runs-on-non-nvidia-gpus-and-macos-but-takes-two-seconds-per-render" target="_blank" rel="noopener" data-cat="keji" data-summary="开发人员的实时WebGPU演示在Web浏览器中运行Nvidia的DLSS 5神经渲染，但显然也在macOS上运行。" data-title="Modder让Nvidia的DLSS 5在使用WebGPU的Web浏览器中工作— 147MB浏览器端口在非Nvidia GPU和macOS上运行，但每次渲染需要两秒钟" data-date="09-18 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 20:00</span>
          <span class="news-item-title">Modder让Nvidia的DLSS 5在使用WebGPU的Web浏览器中工作— 147MB浏览器端口在非Nvidia GPU和macOS上运行，但每次渲染需要两秒钟</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/004/310.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 18 日消息，针对社区中有关代码库数据上传的讨论，智谱旗下编程产品 ZCode 今天（18 日）通过智谱官方群组向受影响用户致歉，并发布回应称已第一时间完成自查，相关问题目前已经修复。IT之家从官方的回应获悉，此次问题源于 ZCode 的“代码库索引”功能，该功能旨在帮助用户在本地生成仓库索引，以支持包括历史版本在内的会话检查点恢复、历史版本回退及 Repo Wiki（代码仓库知识库）等功能。Repo Wiki 功能在生成 Wiki 页面（知识库页面）时，可能会触发仓库数据上传。Wiki 页面在云端生成后，相关上传数据会立即销毁，不会保存。由于该功能在上线初期默认开启，导致部分用户受到影响。针对外界对数据安全及产品信任的关注，官方宣布近期将开源 ZCode 代码库，并邀请第" data-title="智谱 ZCode 被质疑“偷传代码”：官方回应称问题已修复，将开源代码库、引入第三方审查" data-date="09-18 19:48" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-18 19:48</span>
          <span class="news-item-title">智谱 ZCode 被质疑“偷传代码”：官方回应称问题已修复，将开源代码库、引入第三方审查</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/us-chip-manufacturers-are-in-dire-need-of-engineers-and-technicians-experts-suggest-a-shortage-of-up-to-157-000-semiconductor-workers-by-2030" target="_blank" rel="noopener" data-cat="keji" data-summary="随着20世纪30年代及以后许多半导体工厂和设施上线，一家全球咨询公司表示，这些工厂将需要成千上万的工程师和技术人员，而美国将很难填补。" data-title="美国芯片制造厂面临15.7万名工人的巨大短缺，只有3%的美国工程毕业生进入芯片制造业--尽管薪资高达六位数，但美国芯片制造商迫切需要工程师和技术人员" data-date="09-18 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 19:30</span>
          <span class="news-item-title">美国芯片制造厂面临15.7万名工人的巨大短缺，只有3%的美国工程毕业生进入芯片制造业--尽管薪资高达六位数，但美国芯片制造商迫切需要工程师和技术人员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699124.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京9月18日电 雅思官方模考系统近日上线。该系统由雅思全科模考、雅思口语模考和雅思写作模考组成，由英国文化教育协会中国团队主导研发。模考面向中国雅思考生和英语教育机构，以诊断式测评为入口，围绕考前摸底、能力诊断、学习反馈和教学支持，帮助学习者认识自身能力表现和提升方向，也为教师和教育机构提供更具参考价值的学情数据。" data-title="雅思官方模考系统中国上线 人工智能赋能诊断式测评" data-date="09-18 19:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:21</span>
          <span class="news-item-title">雅思官方模考系统中国上线 人工智能赋能诊断式测评</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/asml-snubs-elon-musk-backed-particle-accelerator-chipmaking-tech-firm-doubles-down-on-1-000w-laser-produced-plasma-systems-for-chipmaking-tools" target="_blank" rel="noopener" data-cat="keji" data-summary="随着ASML在扫描仪的LPP EUV光源方面取得的进展，该公司对采用基于粒子加速器的FEL光源几乎没有兴趣。" data-title="ASML冷落埃隆·马斯克（ Elon Musk ）支持的粒子加速器芯片制造技术—该公司将用于芯片制造工具的1,000W激光生产等离子系统加倍" data-date="09-18 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 19:00</span>
          <span class="news-item-title">ASML冷落埃隆·马斯克（ Elon Musk ）支持的粒子加速器芯片制造技术—该公司将用于芯片制造工具的1,000W激光生产等离子系统加倍</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-4k-gaming-pc-with-a-9800x3d-and-rtx-5070-ti-now-usd2-599-powerhouse-abs-stratos-ii-rig-ships-with-32gb-ddr5-and-a-2tb-ssd" target="_blank" rel="noopener" data-cat="keji" data-summary="ABS的4K游戏机，配备强大的RTX 5070 Ti、AMD Ryzen 7 9800X3D、32GB DDR5和2TB SSD ，均售价$ 2,599.99。" data-title="这款4K游戏PC节省300 $ ，配备9800X3D和RTX 5070 Ti ，现在为2,599 $ —强大的ABS Stratos II钻机配备32GB DDR5和2TB SSD" data-date="09-18 18:56" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 18:56</span>
          <span class="news-item-title">这款4K游戏PC节省300 $ ，配备9800X3D和RTX 5070 Ti ，现在为2,599 $ —强大的ABS Stratos II钻机配备32GB DDR5和2TB SSD</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-details-ai-accelerator-roadmap-pulls-in-next-generation-ascend-npus-by-quarters-fp4-performance-of-the-ascend-960pr-doubles-expectations" target="_blank" rel="noopener" data-cat="keji" data-summary="华为模仿英伟达对人工智能工厂的态度，公布了有关下一代Ascend NPU、Kunpeng CPU、横向扩展和横向扩展连接解决方案的详细信息。" data-title="华为详细介绍了人工智能加速器路线图，将下一代Ascend NPU提升了几个季度— Ascend 960PR的FP4性能使预期翻了一番" data-date="09-18 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 18:30</span>
          <span class="news-item-title">华为详细介绍了人工智能加速器路线图，将下一代Ascend NPU提升了几个季度— Ascend 960PR的FP4性能使预期翻了一番</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/004/087.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 18 日消息，据 36 氪从多位产业人士处获悉，今年以来，理想汽车已经开启了多项核心技术的对外供应计划；而伴随业务拆分，部分业务也有引入外部资金的计划。典型启动外供的业务有自研马赫芯片、碳化硅模组公司斯科半导体及增程器等。目前，马赫芯片、碳化硅模组等都已经成立独立的公司实体，寻求更多外部客户，斯科半导体也准备引入更多外部资金。而其他的动力技术，如增程系统也向外释放出接纳外部客户的信息。但自研电池尚无计划，行业人士表示，“电池的定制化程度很高，外供难度太大。”据悉，理想高层也已经决议批准芯片业务分拆，与此同时，业务拓展等动作也在同步进行。消息人士透露，已经有具身智能公司与理想高层洽谈过，“后者明确推销了马赫芯片”，最终这些具身公司是否使用马赫芯片，可能取决于算法迁移难度。据I" data-title="消息称理想汽车开始卖技术：马赫芯片、碳化硅、增程器启动外供" data-date="09-18 14:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-18 14:45</span>
          <span class="news-item-title">消息称理想汽车开始卖技术：马赫芯片、碳化硅、增程器启动外供</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/004/085.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 18 日消息，继型号 M154FF 和 M1544F 两款小米手机跑分曝光后，型号 M610BB 手机也现身 GeekBench 跑分平台，7.0.0 版本单核成绩为 2,831 分、多核成绩 8,843 分。型号方面，科技媒体 GSMArena 认为该机上市后关联小米 18 Pro，由于是工程样机，内存容量、软件调校、温控状态和测试版本都会显著影响跑分成绩，因此相关跑分目前仅供参考。芯片方面，页面信息显示该机配备高通第六代骁龙 8 至尊版（SM8950，英文名称 Snapdragon 8 Elite Gen6），采用 2+3+3 集群方案，相关时钟频率为高通第六代骁龙 8 超级至尊版（SM8975，英文名称 Snapdragon 8 Elite Extreme Gen6）" data-title="M610BB 手机曝光：高通第六代骁龙 8 至尊版芯片，预估为小米 18 Pro" data-date="09-18 14:34" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-18 14:34</span>
          <span class="news-item-title">M610BB 手机曝光：高通第六代骁龙 8 至尊版芯片，预估为小米 18 Pro</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491875.html" target="_blank" rel="noopener" data-cat="keji" data-summary="用通用AI去啃最硬的骨头，这条路走得通" data-title="AGI最难一战，竟在医院！中国AI登上Science，医生不怕失业还催着上线" data-date="09-18 14:11" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-18 14:11</span>
          <span class="news-item-title">AGI最难一战，竟在医院！中国AI登上Science，医生不怕失业还催着上线</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/17/us/politics/trump-f35-jet-saudi-arabia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="U.S. intelligence agencies have warned in internal reports that China could acquire or steal U.S. warplane technology if F-35 jets are sent to Saudi Arabia." data-title="Trump Moves Ahead With F-35 Jet Sales to Saudi Arabia Despite Intelligence Concerns" data-date="09-18 10:32" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-18 10:32</span>
          <span class="news-item-title">Trump Moves Ahead With F-35 Jet Sales to Saudi Arabia Despite Intelligence Concerns</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c8y5z7y521eeo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="随着人工智能以惊人的速度发展，一些业内最杰出的领导者已经警告了它可能带来的潜在风险。然而，世界两大人工智能超级大国——中美之间的激烈竞争，可能会让应对这项威胁的努力变得更加复杂。" data-title="美国科技巨头呼吁放缓AI发展速度" data-date="09-18 09:08" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 09:08</span>
          <span class="news-item-title">美国科技巨头呼吁放缓AI发展速度</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491764.html" target="_blank" rel="noopener" data-cat="keji" data-summary="作价40亿美元推进新融资" data-title="Manus重生第17天，估值居然就翻倍了" data-date="09-18 08:37" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-18 08:37</span>
          <span class="news-item-title">Manus重生第17天，估值居然就翻倍了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/491711.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Git白学了？？？" data-title="刚刚，Claude Code大重构！内部3万Agent管理技术免费开放" data-date="09-18 08:34" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-18 08:34</span>
          <span class="news-item-title">刚刚，Claude Code大重构！内部3万Agent管理技术免费开放</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/18/england-squad-to-be-announced-premier-league-latest-european-reaction-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 周五的团队新闻、新闻发布会和分析⚽The Knowledge ：第一批复制品套件是什么时候？联系我们⚽！发送电子邮件给Dom ，提供任何想法Alexander-Arnold、Alex Scott、Cole Palmer和Rio Ngumoha都会参与进来。菲尔·福登（ Phil Foden ）无处可去。所有小队都在下面。继续阅读..." data-title="图切尔解释了亚历山大-阿诺德和帕尔默英格兰的回忆；西班牙队在休达透露：足球新闻–现场" data-date="09-18 20:15" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-18 20:15</span>
          <span class="news-item-title">图切尔解释了亚历山大-阿诺德和帕尔默英格兰的回忆；西班牙队在休达透露：足球新闻–现场</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/articles/cmn07zv95le8o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃克塞特老板罗布·巴克斯特说，英超俱乐部一直在与英超球队伯恩茅斯分享知识。" data-title="埃克塞特酋长和伯恩茅斯在收购后分享专业知识" data-date="09-18 16:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 16:47</span>
          <span class="news-item-title">埃克塞特酋长和伯恩茅斯在收购后分享专业知识</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/18/todd-boehly-leaves-chelsea-clearlake-capital-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这位亿万富翁的离职对俱乐部的日常生活影响不大，但对俱乐部的体育场计划可能意义重大。自从托德·博利（ Todd Boehly ）注定要进军棘手的转会市场以来，他对切尔西的日常生活没有任何真正的影响。四年后，这位美国人与他的投资伙伴马克·沃尔特（ Mark Walter ）一起退出足球界，首先要说的是，斯坦福桥董事会会议室几乎没有什么变化。" data-title="托德·博赫利（ Todd Boehly ）在手指被烧伤后退出切尔西" data-date="09-18 15:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-18 15:00</span>
          <span class="news-item-title">托德·博赫利（ Todd Boehly ）在手指被烧伤后退出切尔西</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c69qr50nynqdo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heisenberg ）回答了经理们在游戏第五周面临的一些最大困境。" data-title="保留或出售Cherki ？ FPL游戏周五难题" data-date="09-18 14:44" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 14:44</span>
          <span class="news-item-title">保留或出售Cherki ？ FPL游戏周五难题</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmx2zyv3x5rpo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="罗伯托·德·泽比（ Roberto De Zerbi ）的托特纳姆热刺（ Tottenham ）本赛季还没有打进英超联赛的进球，他们如何" data-title="De Zerbi如何解决马刺队的得分问题？" data-date="09-18 13:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 13:16</span>
          <span class="news-item-title">De Zerbi如何解决马刺队的得分问题？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckvgypz42n36o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前锋亚历山大·伊萨克（ Alexander Isak ）表示，利物浦签下他的雄心壮志和决心是他加入俱乐部的重要原因。" data-title="轻松决定从纽卡斯尔搬到利物浦" data-date="09-18 13:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 13:12</span>
          <span class="news-item-title">轻松决定从纽卡斯尔搬到利物浦</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/18/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺和别墅在绝望的德比中相遇， Andoni Iraola面临着对南海岸回归的考验英超联赛最佳射手：查看最新积分榜切尔西自布伦特福德首个英超联赛赛季以来从未赢得过这场西伦敦德比。自2021年10月1-0获胜以来，每次访问，得分手Ben Chilwell都是平局。本赛季延续了俱乐部各自方法之间的分歧，相比之下，布伦特福德的稳固性和连续性" data-title="英超联赛：本周末需要注意的10件事" data-date="09-18 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-18 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/who-scored-blog/2026/sep/17/hull-city-championship-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="赫尔去年几乎被降级到一级联赛。现在他们在英超联赛中排名第四十六个月前，赫尔城避免了因进球差异而降级到联赛一。四个月前，他们需要奥利·麦克伯尼（ Oli McBurnie ）在温布利（ Wembley ）的最后一分钟进球，才能赢得总冠军季后赛决赛。三周前，当季前预测公布时，他们被认为会威胁到德比郡有史以来最糟糕的积分记录" data-title="赫尔城从冠军挣扎者崛起为英超联赛传单" data-date="09-18 00:06" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-18 00:06</span>
          <span class="news-item-title">赫尔城从冠军挣扎者崛起为英超联赛传单</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c62j06np0gpo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）与传奇吉他手和曼城球迷约翰尼·马尔（ Johnny Marr ）以及英国广播公司的读者和人工智能公司（ AI ）一起对本周末的英超联赛进行了预测。" data-title="萨顿的预言v传奇吉他手约翰尼·马尔" data-date="09-17 23:10" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-17 23:10</span>
          <span class="news-item-title">萨顿的预言v传奇吉他手约翰尼·马尔</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/004/315.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 18 日消息，据央视新闻报道，车辆年检、尾气检测是守护空气质量的重要关口。为堵住机动车尾气检测弄虚作假、检测不规范等问题，生态环境部、市场监管总局近日联合印发《关于推进机动车排放检验机构监管改革提升排放检验质量的意见》，今后，严重弄虚作假机构将被坚决清出市场。IT之家获悉，《意见》要求聚焦机动车排放检验机构设备管理、检验操作、日常运维、人员技能等薄弱环节，建立健全权责清晰、运行规范、全程可溯、常态监管的全过程管理体系。要坚持源头严管，指导机动车排放检验机构按照《生态环境法典》要求落实主体责任，提升检验数据质量和检验合规水平。在机构准入和退出管理上，《意见》要求，加强资质认定专家评审，确保排放检验设备和人员符合条件要求，对违法机构和人员依法处罚惩戒，严重弄虚作假机构要被坚决清" data-title="两部门整治机动车排放检验乱象：将严重弄虚作假机构清出市场" data-date="09-18 20:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-18 20:19</span>
          <span class="news-item-title">两部门整治机动车排放检验乱象：将严重弄虚作假机构清出市场</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/004/314.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 18 日消息，据汽车之家消息，领克 20 将于 9 月 28 日正式上市。9 月 8 日，领克汽车宣布全新领克 20 代言人为吴谨言，同时宣布新车开启“先享预订”，下订用户即可获赠价值 3999 元的充电桩。新车定位精致驾趣纯电 SUV，属于领克 Z20 的改款换代产品，基于 SEA 浩瀚架构打造，车长 4495mm、轴距 2755mm。此次“去 Z 回归”的更名，也标志着产品定位和配置的全面跃升，主要卖点包括：动力与补能：全系标配全域 800V 高压平台与 6C 超高充电倍率，最大充电功率可达 460kW，电量从 10% 充至 80% 仅需约 12 分钟。车辆提供 545km 和 630km 两种 CLTC 续航版本。智能驾驶：全系标配激光雷达，由 28 颗高精度智能感知" data-title="全新领克 20 将于 9 月 28 日上市，全系标配激光雷达、800V 高压平台" data-date="09-18 20:11" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-18 20:11</span>
          <span class="news-item-title">全新领克 20 将于 9 月 28 日上市，全系标配激光雷达、800V 高压平台</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699173.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长沙9月18日电(刘思妮 丁向)18日，第九届发展中国家儿童健康论坛暨国家儿童区域医疗中心高质量发展交流会在长沙开幕，国内外知名儿科专家、医疗机构代表等近600人参会。" data-title="第九届发展中国家儿童健康论坛在长沙开幕" data-date="09-18 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 20:07</span>
          <span class="news-item-title">第九届发展中国家儿童健康论坛在长沙开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699101.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川9月18日电 (记者 于晶)9月18日，记者从宁夏回族自治区人力资源和社会保障厅获悉，该单位印发《宁夏回族自治区深化产教评技能生态链建设工作方案》，启动首批遴选申报工作，宁夏产教评技能生态链建设正式全面实施。" data-title="宁夏启动首批产教评技能生态链建设" data-date="09-18 19:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:47</span>
          <span class="news-item-title">宁夏启动首批产教评技能生态链建设</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699136.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网忻州9月18日电 题：海外华文媒体走进山西神池 探访千年非遗“神池月饼”的产业新生" data-title="海外华文媒体走进山西神池 探访千年非遗“神池月饼”的产业新生" data-date="09-18 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:35</span>
          <span class="news-item-title">海外华文媒体走进山西神池 探访千年非遗“神池月饼”的产业新生</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699138.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海9月18日电 (陈静 曹乃文)第48届世界技能大赛开幕在即，来自世界各地的参赛选手、技术专家及其他代表团成员陆续抵沪。" data-title="第48届世界技能大赛涉赛人员自上海口岸集中入境" data-date="09-18 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:34</span>
          <span class="news-item-title">第48届世界技能大赛涉赛人员自上海口岸集中入境</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-18/10699100.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川9月18日电(于晶 何佳欣)9月18日，记者从宁夏回族自治区体育局获悉，中秋、国庆假期，宁夏统筹谋划59项体育赛事活动，涵盖专业竞技、群众参与、休闲娱乐多个类型，兼顾本地市民与外地游客运动体验需求，以体育赋能假日文旅消费。" data-title="宁夏“双节”推出59项体育赛事 体育+文旅激活假日活力" data-date="09-18 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 19:28</span>
          <span class="news-item-title">宁夏“双节”推出59项体育赛事 体育+文旅激活假日活力</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/997083/flash-flood-warning-tacls-satellite-machine-learning" target="_blank" rel="noopener" data-cat="zonghe" data-summary="6月9日上午， Laura Lin在距离肯塔基州边境约15英里的印第安纳州南部乡村小镇Lanesville的家中工作。她正在打Zoom电话，不知道外面的大雨开始淹没她的院子。“我看着那边的谷仓， […]" data-title="山洪暴发可能在没有预警的情况下发生—这项新技术可能会改变" data-date="09-18 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-18 19:00</span>
          <span class="news-item-title">山洪暴发可能在没有预警的情况下发生—这项新技术可能会改变</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-18/10699114.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月18日电 综合日本共同社、韩国《东亚日报》报道，在18日举行的韩国队出场的爱知·名古屋亚运会男子曲棍球比赛时，出现了误将朝鲜国歌作为韩国国歌播放的问题。赛事相关人员透露了此事。" data-title="大乌龙！外媒曝亚运会韩国队比赛误播朝鲜国歌" data-date="09-18 18:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-18 18:44</span>
          <span class="news-item-title">大乌龙！外媒曝亚运会韩国队比赛误播朝鲜国歌</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cryptocurrency/hacker-turns-25-cents-into-46-billion-fake-bitcoins-to-steal-usd770-000-symbiosis-defi-exchange-bit-by-lack-of-basic-bounds-checking-in-smart-contract" target="_blank" rel="noopener" data-cat="zonghe" data-summary="共生DeFi网络因智能合约中缺乏基本边界检查而被黑客入侵，至少价值$ 770,000比特币— DeFi交易所位" data-title="黑客将25美分变成460亿个假比特币，窃取$ 770,000 —由于缺乏基本的智能合约检查，共生DeFi交换位" data-date="09-18 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 18:30</span>
          <span class="news-item-title">黑客将25美分变成460亿个假比特币，窃取$ 770,000 —由于缺乏基本的智能合约检查，共生DeFi交换位</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/florida-man-arrested-for-selling-usd50-3d-printed-machine-gun-conversion-kits-to-undercover-cops-glock-switches-turn-pistols-into-fully-automatic-weapons" target="_blank" rel="noopener" data-cat="zonghe" data-summary="佛罗里达州杰克逊维尔的Emani Rey Justavino因销售50多台“格洛克开关”转换器而被捕，这些转换器为手枪提供了全自动功能。嫌疑人声称，他在一夜之间3D打印了整个批次，并以折扣价将其全部提供给了一名卧底ATF特工。" data-title="一名男子因向卧底警察出售50 $ 3D打印机枪转换套件而被捕— “格洛克开关”将手枪变成全自动武器" data-date="09-18 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-18 18:00</span>
          <span class="news-item-title">一名男子因向卧底警察出售50 $ 3D打印机枪转换套件而被捕— “格洛克开关”将手枪变成全自动武器</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckwyzg2v80elo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚运选手将入住木制货柜屋或一艘意大利邮轮。韩国代表团批评，货柜屋宿舍水管漏水，且床铺太小，运动员甚至无法伸直双腿睡觉。" data-title="“运动员无法伸直双腿睡觉”：日本亚运为何爆发住宿争议？" data-date="09-18 17:24" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 17:24</span>
          <span class="news-item-title">“运动员无法伸直双腿睡觉”：日本亚运为何爆发住宿争议？</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/492015.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="那些数以亿万计的，仍在等待被市场看见的小农户们。" data-title="白天务农晚上码农，这个斐济农民跨越一万公里来拼多多取经" data-date="09-18 17:19" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-18 17:19</span>
          <span class="news-item-title">白天务农晚上码农，这个斐济农民跨越一万公里来拼多多取经</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/18/us/politics/abortion-rights-activists-in-idaho-find-their-pitch-bring-back-the-doctors.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Organizers of a referendum to repeal an abortion ban in deep-red Idaho are far more focused on how the ban has broadly affected health care in the state." data-title="爱达荷州的堕胎权利活动家找到自己的主张：让医生回来" data-date="09-18 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-18 17:02</span>
          <span class="news-item-title">爱达荷州的堕胎权利活动家找到自己的主张：让医生回来</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq3d7zld42m0o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Hyrox已更新赛例，明文规定若参赛者的“血液、呕吐物、尿液或粪便”构成健康风险，可被要求退赛。" data-title="Hyrox失禁风波：澳洲选手道歉、主办方承诺退款" data-date="09-18 16:46" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-18 16:46</span>
          <span class="news-item-title">Hyrox失禁风波：澳洲选手道歉、主办方承诺退款</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-18 20:18（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
