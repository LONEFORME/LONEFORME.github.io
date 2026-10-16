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
      <span>2026-10-17 00:48 抓取更新</span>
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
        <span class="channel-count">53</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">11</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">53</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×15 · BBC×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-17/10716043.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月17日电(记者 李京统)中央机关及其直属机构2027年度考试录用公务员报名自14日8时开始，已经进行了三天。具体岗位报考方面，已有岗位出现超千人竞争一岗的现象。" data-title="国考报名三天，热门岗位竞争已超1400:1" data-date="10-17 00:29" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-17 00:29</span>
      </div>
      <h2 class="hero-featured-title">国考报名三天，热门岗位竞争已超1400:1</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-17/10716044.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社杭州10月16日电 (钱晨菲)16日在杭州举办的国际电信联盟具身智能标准焦点组2026年第三次会议及具身智能标准高级研修班上，中国信息通信研究院人工智能研究所联合清华大学电子工程系、具身智能测试实验室，共同发布《具身智能发展报告(2026年)》(英文版)，系统梳理当前具身智能产业发展情况。" data-title="报告指上半年全球人形机器人出货量超2.2万台" data-date="10-17 00:43" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">报告指上半年全球人形机器人出货量超2.2万台</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/16/martinez-sorry-outburst-european-reaction-premier-league-latest-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进入周末⚽的所有最新足球新闻⚽十件需要注意的事情|足球日报|电子邮件LukeSky报道说，切尔西今天早上确认接受小膝盖手术的里斯·詹姆斯预计将缺席三次" data-title="Carrick includes Martínez in squad; Madrid call for Tebas to quit over Goebbels comparisons: football" data-date="10-17 00:36" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Carrick includes Martínez in squad; Madrid call for Tebas to quit over Goebbels comparisons: football</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/10-17/10716023.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社东京10月16日电 (记者 朱晨曦)针对16日中午错误推测发生9.9级地震并发出相应警报一事，日本气象厅当日下午两度召开记者会致歉。日本气象厅表示，此次误发预警可能是震源位置推定错误所致。" data-title="错估震级9.9级 日本气象厅两度召开记者会致歉" data-date="10-17 00:45" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">错估震级9.9级 日本气象厅两度召开记者会致歉</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716043.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月17日电(记者 李京统)中央机关及其直属机构2027年度考试录用公务员报名自14日8时开始，已经进行了三天。具体岗位报考方面，已有岗位出现超千人竞争一岗的现象。" data-title="国考报名三天，热门岗位竞争已超1400:1" data-date="10-17 00:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 00:29</span>
          <span class="news-item-title">国考报名三天，热门岗位竞争已超1400:1</span>
          <span class="news-value-point">💡 中新网北京10月17日电(记者 李京统)中央机关及其直属机构2027年度考试录用公务员报名自14日8时开始，已经进行了三天</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/16/world/europe/trump-zelensky-ukraine-war.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="两位总统的口水战将在哪里结束，这是任何人的猜测。但如果这种情况继续下去，它可能会威胁到乌克兰仍然从美国获得的关键作战援助。" data-title="The Rupturing Trump-Zelensky Relationship Stands to Hurt Ukraine and Its European Allies" data-date="10-16 23:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-16 23:02</span>
          <span class="news-item-title">特朗普-泽伦斯基关系破裂将伤害乌克兰及其欧洲盟友</span>
          <span class="news-item-title-en">The Rupturing Trump-Zelensky Relationship Stands to Hurt Ukraine and Its European Allies</span>
          <span class="news-value-point">💡 两位总统的口水战将在哪里结束，这是任何人的猜测</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715984.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社浙江金华10月16日电 (董易鑫)2026中非影视交流合作活动新闻通气会16日在浙江金华举行。会上透露，北京时间10月15日起，金华官方面向非洲38个国家展播《流浪地球》《唐人街探案》等中国优秀影视作品，以影视为媒，推动中非文化交流。" data-title="浙江金华面向非洲38国展播中国优秀影视作品" data-date="10-16 22:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 22:20</span>
          <span class="news-item-title">浙江金华面向非洲38国展播中国优秀影视作品</span>
          <span class="news-value-point">💡 中新社浙江金华10月16日电 (董易鑫)2026中非影视交流合作活动新闻通气会16日在浙江金华举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10716003.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州10月16日电 1934年10月，中央红军从江西于都出发，走向一场改变中国命运的二万五千里长征。从10月25日进入广东南雄，到11月14日离开乐昌，红军在广东境内的粤北群山间跋涉了21天，突破国民党军设置的第二、第三道封锁线，为长征初期打开了西进通道。" data-title="五集历史纪录片《突围21天》揭秘一段鲜为人知的长征史" data-date="10-16 21:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 21:56</span>
          <span class="news-item-title">五集历史纪录片《突围21天》揭秘一段鲜为人知的长征史</span>
          <span class="news-value-point">💡 中新网广州10月16日电 1934年10月，中央红军从江西于都出发，走向一场改变中国命运的二万五千里长征</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715960.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网东京10月16日电 (记者 朱晨曦)《“每日熊猫”的15年》写真集出版纪念会暨摄影展开幕式15日在东京多元文化会馆举行。" data-title="高氏贵博《“每日熊猫”的15年》写真集出版纪念会在东京举行" data-date="10-16 21:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 21:05</span>
          <span class="news-item-title">高氏贵博《“每日熊猫”的15年》写真集出版纪念会在东京举行</span>
          <span class="news-value-point">💡 中新网东京10月16日电 (记者 朱晨曦)《“每日熊猫”的15年》写真集出版纪念会暨摄影展开幕式15日在东京多元文化会馆举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715843.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月16日电 (记者 金旭)当地时间16日，韩国负责调查紧急戒严事件的特检组就“制造平壤上空无人机入侵事件”在二审中要求对韩国前总统尹锡悦处以30年有期徒刑，维持一审判决。" data-title="韩国检方要求尹锡悦涉无人机案二审维持30年刑期" data-date="10-16 18:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 18:24</span>
          <span class="news-item-title">韩国检方要求尹锡悦涉无人机案二审维持30年刑期</span>
          <span class="news-value-point">💡 中新社首尔10月16日电 (记者 金旭)当地时间16日，韩国负责调查紧急戒严事件的特检组就“制造平壤上空无人机入侵事件”在二审中要求对韩国前总统…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/16/us/avalanche-of-gop-cash-keeps-the-party-competitive-despite-its-problems.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="共和党参议院和众议院候选人被民主党的竞争对手击败，但该党得到了与埃隆·马斯克(Elon Musk)和特朗普总统有关的团体的巨大推动。" data-title="Avalanche of G.O.P. Cash Keeps the Party Competitive Despite Its Problems" data-date="10-16 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-16 17:02</span>
          <span class="news-item-title">尽管存在问题，但G.O.P. Cash的雪崩仍保持了党的竞争力</span>
          <span class="news-item-title-en">Avalanche of G.O.P. Cash Keeps the Party Competitive Despite Its Problems</span>
          <span class="news-value-point">💡 共和党参议院和众议院候选人被民主党的竞争对手击败，但该党得到了与埃隆·马斯克(Elon Musk)和特朗普总统有关的团体的巨大推动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715762.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="本报记者 李嘉宝" data-title="日本图谋删除“敌国条款”是痴人说梦（环球热点）" data-date="10-16 16:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 16:43</span>
          <span class="news-item-title">日本图谋删除“敌国条款”是痴人说梦（环球热点）</span>
          <span class="news-value-point">💡 本报记者 李嘉宝</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crz65gxl2jxlo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="法国总理暗示学生的愤怒情绪正被武器化，因为工会和其他抗议者也准备走上街头。法国是否濒临崩溃？" data-title="法国总统大选前，学生抗议活动是否被人为操纵？" data-date="10-16 14:21" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 14:21</span>
          <span class="news-item-title">法国总统大选前，学生抗议活动是否被人为操纵？</span>
          <span class="news-value-point">💡 法国总理暗示学生的愤怒情绪正被武器化，因为工会和其他抗议者也准备走上街头</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/15/us/politics/alina-habba-mildon-richard-grenell-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普的两个盟友--阿丽娜·哈巴·米尔登(Alina Habba Mildon)和理查德·格雷内尔(Richard Grenell) --陷入了一场激烈的争端，其根源在于争夺委内瑞拉的一部分战利品。" data-title="A Bitter White House Feud, Even by Trump-Era Standards: Alina Mildon and Richard Grenell" data-date="10-16 08:52" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-16 08:52</span>
          <span class="news-item-title">白宫的激烈争斗，即使是特朗普时代的标准： Alina Mildon和Richard Grenell</span>
          <span class="news-item-title-en">A Bitter White House Feud, Even by Trump-Era Standards: Alina Mildon and Richard Grenell</span>
          <span class="news-value-point">💡 特朗普的两个盟友--阿丽娜·哈巴·米尔登(Alina Habba Mildon)和理查德·格雷内尔(Richard Grenell) --陷入了…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/15/us/politics/trump-russia-srpska-elections-wiles.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统办公室主任的女儿与斯普斯卡共和国的一名美国商人一起勘探天然气管道。最近，六名现任和前任竞选顾问前往那里参加选举。" data-title="More Trump Allies Aided Pro-Russian Balkan Government" data-date="10-16 04:53" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-16 04:53</span>
          <span class="news-item-title">更多特朗普盟友援助亲俄巴尔干政府</span>
          <span class="news-item-title-en">More Trump Allies Aided Pro-Russian Balkan Government</span>
          <span class="news-value-point">💡 总统办公室主任的女儿与斯普斯卡共和国的一名美国商人一起勘探天然气管道</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-17/10716044.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社杭州10月16日电 (钱晨菲)16日在杭州举办的国际电信联盟具身智能标准焦点组2026年第三次会议及具身智能标准高级研修班上，中国信息通信研究院人工智能研究所联合清华大学电子工程系、具身智能测试实验室，共同发布《具身智能发展报告(2026年)》(英文版)，系统梳理当前具身智能产业发展情况。" data-title="报告指上半年全球人形机器人出货量超2.2万台" data-date="10-17 00:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 00:43</span>
          <span class="news-item-title">报告指上半年全球人形机器人出货量超2.2万台</span>
          <span class="news-value-point">💡 中新社杭州10月16日电 (钱晨菲)16日在杭州举办的国际电信联盟具身智能标准焦点组2026年第三次会议及具身智能标准高级研修班上，中国信息通信…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/video/a-nvidia-insider-turned-vc-on-why-robotics-hasnt-hit-its-chatgpt-moment-yet/" target="_blank" rel="noopener" data-cat="keji" data-summary="Amulya Vishwanath在NVIDIA机器人平台的产品营销方面花了七年的时间，她说机器人技术目前正处于“乐高时代” ，执行器、机器人手、软件和安全标准等基本构件仍在" data-title="A Nvidia insider-turned-VC on why robotics hasn’t hit its ChatGPT moment, yet" data-date="10-17 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-17 00:30</span>
          <span class="news-item-title">英伟达内部人士转向VC ，解释为什么机器人技术还没有达到其ChatGPT时刻</span>
          <span class="news-item-title-en">A Nvidia insider-turned-VC on why robotics hasn’t hit its ChatGPT moment, yet</span>
          <span class="news-value-point">💡 Amulya Vishwanath在NVIDIA机器人平台的产品营销方面花了七年的时间，她说机器人技术目前正处于“乐高时代” ，执行器、机器人手…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/podcast/physical-ai-is-more-than-robots-says-the-nvidia-veteran-now-investing-in-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="Amulya Vishwanath在NVIDIA机器人平台的产品营销方面花了七年的时间，她说机器人技术目前正处于“乐高时代” ，执行器、机器人手、软件和安全标准等基本构件仍在" data-title="Physical AI is more than robots, says the Nvidia veteran now investing in it" data-date="10-17 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-17 00:30</span>
          <span class="news-item-title">物理人工智能不仅仅是机器人，这位英伟达的资深人士现在投资于它</span>
          <span class="news-item-title-en">Physical AI is more than robots, says the Nvidia veteran now investing in it</span>
          <span class="news-value-point">💡 Amulya Vishwanath在NVIDIA机器人平台的产品营销方面花了七年的时间，她说机器人技术目前正处于“乐高时代” ，执行器、机器人手…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability" target="_blank" rel="noopener" data-cat="keji" data-summary="中国初创公司Langdao Silex在贸易展上展示了其激光生产的等离子体EUV源，但该技术可能需要多年时间才能达到体面的EUV功率水平。即使是这样，中国也需要更多的进步来建立一个" data-title="China startup demoes prototype EUV light source" data-date="10-17 00:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 00:30</span>
          <span class="news-item-title">中国初创企业演示EUV光源原型</span>
          <span class="news-item-title-en">China startup demoes prototype EUV light source</span>
          <span class="news-value-point">💡 中国初创公司Langdao Silex在贸易展上展示了其激光生产的等离子体EUV源，但该技术可能需要多年时间才能达到体面的EUV功率水平</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/gun-rights-activist-unveils-worlds-first-ai-made-3d-printed-firearm-22-caliber-handgun-created-by-an-ai-that-can-generate-guns-called-gatgpt" target="_blank" rel="noopener" data-cat="keji" data-summary="一名枪支权利活动家推出了世界上第一款人工智能3D打印枪支。" data-title="Gun-rights activist unveils world&#39;s first &#39;AI-made&#39; 3D-printed firearm — .22 caliber handgun created by an &#39;AI that can generate guns&#39; called GatGPT" data-date="10-17 00:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 00:20</span>
          <span class="news-item-title">枪支权利活动家推出世界上第一支“人工智能制造”的3D打印枪支—由名为GatGPT的“可以生成枪支的人工智能”创造的.22口径手枪</span>
          <span class="news-item-title-en">Gun-rights activist unveils world's first 'AI-made' 3D-printed firearm — .22 caliber handgun created by an 'AI that can generate guns' called GatGPT</span>
          <span class="news-value-point">💡 一名枪支权利活动家推出了世界上第一款人工智能3D打印枪支</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/" target="_blank" rel="noopener" data-cat="keji" data-summary="根据Elorian的评估， Glimpse在科学图表推理和短视频字幕方面的表现甚至优于GPT-6 Astra ，在其他视觉推理任务上取得了有竞争力的结果。" data-title="Elorian’s first AI model wants to reason with images, not just about them" data-date="10-17 00:01" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-17 00:01</span>
          <span class="news-item-title">Elorian的第一个人工智能模型想要用图像进行推理，而不仅仅是关于它们</span>
          <span class="news-item-title-en">Elorian’s first AI model wants to reason with images, not just about them</span>
          <span class="news-value-point">💡 根据Elorian的评估， Glimpse在科学图表推理和短视频字幕方面的表现甚至优于GPT-6 Astra ，在其他视觉推理任务上取得了有竞争…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models" target="_blank" rel="noopener" data-cat="keji" data-summary="订单在Nvidia RTX Spark笔记本电脑上有效，包括Microsoft Surface Laptop Ultra以及惠普、联想、华硕和戴尔的设备。" data-title="Orders are live on Nvidia RTX Spark devices, secure the Surface Laptop Ultra or other RTX Spark laptops here" data-date="10-16 23:38" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-16 23:38</span>
          <span class="news-item-title">订单在Nvidia RTX Spark设备上有效，在此处保护Surface Laptop Ultra或其他RTX Spark笔记本电脑</span>
          <span class="news-item-title-en">Orders are live on Nvidia RTX Spark devices, secure the Surface Laptop Ultra or other RTX Spark laptops here</span>
          <span class="news-value-point">💡 订单在Nvidia RTX Spark笔记本电脑上有效，包括Microsoft Surface Laptop Ultra以及惠普、联想、华硕和戴…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/16/jev-is-vercels-fastest-adopted-ai-model-ever/" target="_blank" rel="noopener" data-cat="keji" data-summary="数据来自Vercel的AI网关，这是一种类似于OpenRouter的统一API服务。" data-title="Jev is Vercel’s fastest-adopted AI model ever" data-date="10-16 23:33" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 23:33</span>
          <span class="news-item-title">Jev是Vercel有史以来采用最快的人工智能模型</span>
          <span class="news-item-title-en">Jev is Vercel’s fastest-adopted AI model ever</span>
          <span class="news-value-point">💡 数据来自Vercel的AI网关，这是一种类似于OpenRouter的统一API服务</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/184.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 16 日消息，硬件诊断监控软件 HWiNFO 近日在其版本历史记录页面更新了即将到来的变化，包括“新增 Panter Lake-H 080”“增强对 Nova Lake-E 和 Razor Lake-S 的支持”。IT之家注：&quot;Panter Lake&quot; 很明显是一个误输入，指的应该是 &quot;Panther Lake&quot;。消息人士 @jaykihn0 今日对上述 &quot;Panther Lake-H 080&quot; 和 &quot;Nova Lake-E&quot; 进行了解释：&quot;Panther Lake-H 080&quot; 是一款采用 0P + 8P + 0LP-E + 4Xe 设计的 &quot;Panter Lake&quot; 处理器，隶属于锐炫 Arc G 系列。其定位显然低于现有的 Arc G3 Extreme 和 Arc" data-title="曝英特尔将推 8E + 4Xe 版 &quot;Panther Lake&quot; 锐炫 G 掌机处理器" data-date="10-16 23:05" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 23:05</span>
          <span class="news-item-title">曝英特尔将推 8E + 4Xe 版 "Panther Lake" 锐炫 G 掌机处理器</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，硬件诊断监控软件 HWiNFO 近日在其版本历史记录页面更新了即将到来的变化，包括“新增 Panter Lak…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达的RTX Spark N1X处理器终于问世了，我们一直在共同测试价值一小笔的强大笔记本电脑，这些笔记本电脑配备了这款新的“超级芯片”。“RTX Spark旨在成为适用于笔记本电脑和小型台式机的高性能基于Arm的SoC ，" data-title="A week with RTX Spark: everything we’ve learned using Nvidia’s new laptops" data-date="10-16 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 23:00</span>
          <span class="news-item-title">RTX Spark一周体验：我们使用Nvidia新款笔记本电脑所学到的一切</span>
          <span class="news-item-title-en">A week with RTX Spark: everything we’ve learned using Nvidia’s new laptops</span>
          <span class="news-value-point">💡 英伟达的RTX Spark N1X处理器终于问世了，我们一直在共同测试价值一小笔的强大笔记本电脑，这些笔记本电脑配备了这款新的“超级芯片”</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/16/veritas-is-building-a-chip-to-verify-luxury-goods/" target="_blank" rel="noopener" data-cat="keji" data-summary="造假者越来越擅长复制品牌标志，并将被称为“超级假货”的骗局作为正品。一家名为Veritas的初创公司希望用自己的芯片来验证商品来解决这个问题。" data-title="Veritas expands its anti-counterfeit chip to jewelry, trophies, and fragrance bottles" data-date="10-16 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 22:00</span>
          <span class="news-item-title">Veritas将其防伪芯片扩展到珠宝、奖杯和香水瓶</span>
          <span class="news-item-title-en">Veritas expands its anti-counterfeit chip to jewelry, trophies, and fragrance bottles</span>
          <span class="news-value-point">💡 造假者越来越擅长复制品牌标志，并将被称为“超级假货”的骗局作为正品</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715946.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="10月16日，中共中央总书记、国家主席、中央军委主席习近平在内蒙古自治区乌兰察布市考察，习近平总书记指出——" data-title="习言道｜积极推动绿色算力产业发展" data-date="10-16 21:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 21:30</span>
          <span class="news-item-title">习言道｜积极推动绿色算力产业发展</span>
          <span class="news-value-point">💡 10月16日，中共中央总书记、国家主席、中央军委主席习近平在内蒙古自治区乌兰察布市考察，习近平总书记指出——</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715967.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京10月16日电 (记者 孙自法)记者10月16日从中国科协获悉，中国科协生态环境产学联合体当天发布了世界生态环境十大科技进展，人工智能(AI)重塑天气与地球系统预报等10项入选。" data-title="中国科技社团发布世界生态环境十大科技进展 AI重塑天地预报等入选" data-date="10-16 21:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 21:25</span>
          <span class="news-item-title">中国科技社团发布世界生态环境十大科技进展 AI重塑天地预报等入选</span>
          <span class="news-value-point">💡 中新网北京10月16日电 (记者 孙自法)记者10月16日从中国科协获悉，中国科协生态环境产学联合体当天发布了世界生态环境十大科技进展，人工智能…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715965.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社吉隆坡10月16日电 (记者 刘育英)马来西亚16日发布六款本土研发的半导体芯片及相关技术创新成果，预计合计销售潜力约3亿林吉特(约合4.9亿元人民币)，旨在推动本国半导体产业在封装、测试等传统优势基础上，加强本土芯片设计与研发能力，进一步向产业价值链上游拓展。" data-title="马来西亚推出六款本土研发芯片及相关成果" data-date="10-16 21:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 21:05</span>
          <span class="news-item-title">马来西亚推出六款本土研发芯片及相关成果</span>
          <span class="news-value-point">💡 中新社吉隆坡10月16日电 (记者 刘育英)马来西亚16日发布六款本土研发的半导体芯片及相关技术创新成果，预计合计销售潜力约3亿林吉特(约合4.…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/16/replits-ceo-says-the-future-of-work-is-the-self-driving-company/" target="_blank" rel="noopener" data-cat="keji" data-summary="Replit首席执行官Amjad Masad设想了“自动驾驶公司”的未来，人工智能代理处理日常任务，人们专注于更高层次的决策。" data-title="Replit’s CEO says the future of work is the ‘self" data-date="10-16 20:55" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 20:55</span>
          <span class="news-item-title">Replit的首席执行官表示，工作的未来是“自我”</span>
          <span class="news-item-title-en">Replit’s CEO says the future of work is the ‘self</span>
          <span class="news-value-point">💡 Replit首席执行官Amjad Masad设想了“自动驾驶公司”的未来，人工智能代理处理日常任务，人们专注于更高层次的决策</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/16/martinez-sorry-outburst-european-reaction-premier-league-latest-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进入周末⚽的所有最新足球新闻⚽十件需要注意的事情|足球日报|电子邮件LukeSky报道说，切尔西今天早上确认接受小膝盖手术的里斯·詹姆斯预计将缺席三次" data-title="Carrick includes Martínez in squad; Madrid call for Tebas to quit over Goebbels comparisons: football" data-date="10-17 00:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 00:36</span>
          <span class="news-item-title">卡里克在球队中包括马丁内斯；马德里呼吁特巴斯退出戈培尔的比较：足球</span>
          <span class="news-item-title-en">Carrick includes Martínez in squad; Madrid call for Tebas to quit over Goebbels comparisons: football</span>
          <span class="news-value-point">💡 进入周末⚽的所有最新足球新闻⚽十件需要注意的事情|足球日报|电子邮件LukeSky报道说，切尔西今天早上确认接受小膝盖手术的里斯·詹姆斯预计将缺…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6je5lwxk5l0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”。" data-title="Do Manchester City have any grounds to win their appeal?" data-date="10-17 00:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 00:17</span>
          <span class="news-item-title">曼城是否有任何理由赢得他们的上诉？</span>
          <span class="news-item-title-en">Do Manchester City have any grounds to win their appeal?</span>
          <span class="news-value-point">💡 一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwy7l5e4376no?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="刘易斯·库马斯（ Lewis Koumas ）谈到打破史蒂文·杰拉德（ Steven Gerrard ）的纪录，抓住他在安东尼·伊拉奥拉（ Andoni Iraola ）手下的机会，以及他在曼城" data-title="Feel-good Koumas story something for Liverpool to smile about" data-date="10-17 00:06" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 00:06</span>
          <span class="news-item-title">Koumas的美好故事，让利物浦人一笑置之</span>
          <span class="news-item-title-en">Feel-good Koumas story something for Liverpool to smile about</span>
          <span class="news-value-point">💡 刘易斯·库马斯（ Lewis Koumas ）谈到打破史蒂文·杰拉德（ Steven Gerrard ）的纪录，抓住他在安东尼·伊拉奥拉（ An…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cr3wv4xd2l6yo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳老板米克尔·阿尔特塔（ Mikel Arteta ）说，他被告知俱乐部裁员60人的决定是为了“实现我们想要创造的成功”。" data-title="Arteta told Arsenal job cuts will help create success" data-date="10-16 23:31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 23:31</span>
          <span class="news-item-title">Arteta告诉阿森纳裁员将有助于创造成功</span>
          <span class="news-item-title-en">Arteta told Arsenal job cuts will help create success</span>
          <span class="news-value-point">💡 阿森纳老板米克尔·阿尔特塔（ Mikel Arteta ）说，他被告知俱乐部裁员60人的决定是为了“实现我们想要创造的成功”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm4g189leelno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联老板迈克尔·卡里克（ Michael Carrick ）说，他从利桑德罗·马丁内斯（ Lisandro Martinez ）爆炸性的赛后采访中讲述了俱乐部的真相。" data-title="&#39;I am telling you the truth&#39; - Carrick on Martinez fallout" data-date="10-16 21:59" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 21:59</span>
          <span class="news-item-title">“我告诉你们真相” -卡里克谈论马丁内斯的影响</span>
          <span class="news-item-title-en">'I am telling you the truth' - Carrick on Martinez fallout</span>
          <span class="news-value-point">💡 曼联老板迈克尔·卡里克（ Michael Carrick ）说，他从利桑德罗·马丁内斯（ Lisandro Martinez ）爆炸性的赛后采访…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq073d9l0ly9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西队长里斯·詹姆斯在接受膝盖手术后将缺席三个月的比赛。" data-title="Chelsea&#39;s James out for three months after knee surgery" data-date="10-16 21:36" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 21:36</span>
          <span class="news-item-title">切尔西的詹姆斯在膝盖手术后出局三个月</span>
          <span class="news-item-title-en">Chelsea's James out for three months after knee surgery</span>
          <span class="news-value-point">💡 切尔西队长里斯·詹姆斯在接受膝盖手术后将缺席三个月的比赛</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c615jw414vypo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="富勒姆主教练阿尔瓦罗·阿贝洛亚（ Alvaro Arbeloa ）表示，重点不应放在他身上，因为他本周末正在寻找本赛季对阵赫尔城的第一场英超联赛胜利。" data-title="&#39;Not about me&#39; - Arbeloa dismisses future questions" data-date="10-16 18:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 18:24</span>
          <span class="news-item-title">“不是关于我” - Arbeloa驳斥了未来的问题</span>
          <span class="news-item-title-en">'Not about me' - Arbeloa dismisses future questions</span>
          <span class="news-value-point">💡 富勒姆主教练阿尔瓦罗·阿贝洛亚（ Alvaro Arbeloa ）表示，重点不应放在他身上，因为他本周末正在寻找本赛季对阵赫尔城的第一场英超联赛…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/16/premier-league-teams-run-more-win-matches-distance-opta" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="权威人士经常批评团队跑得不够，但距离和结果之间是否存在联系？ Opta Analyst的《It was like clockwork》。曼联在对阵托特纳姆热刺的比赛中失分，批评者很快质疑他们的努力" data-title="Do Premier League teams really need to run more to win matches?" data-date="10-16 15:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-16 15:30</span>
          <span class="news-item-title">英超球队真的需要跑得更多才能赢得比赛吗？</span>
          <span class="news-item-title-en">Do Premier League teams really need to run more to win matches?</span>
          <span class="news-value-point">💡 权威人士经常批评团队跑得不够，但距离和结果之间是否存在联系</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/world/2026/oct/16/friday-briefing-how-manchester-citys-financial-scandal-could-upend-the-whole-football-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在今天的时事通讯中：曼城的耻辱远远超出了体育范畴，不仅暴露了足球危机，还引发了对外国拥有的英国机构的质疑早上好。这是一场规模庞大的体育丑闻，" data-title="Friday briefing: How Manchester City’s ​financial scandal could upend the whole football league" data-date="10-16 13:44" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-16 13:44</span>
          <span class="news-item-title">周五简报：曼城的财务丑闻如何颠覆整个足球联盟</span>
          <span class="news-item-title-en">Friday briefing: How Manchester City’s ​financial scandal could upend the whole football league</span>
          <span class="news-value-point">💡 在今天的时事通讯中：曼城的耻辱远远超出了体育范畴，不仅暴露了足球危机，还引发了对外国拥有的英国机构的质疑早上好</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/16/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亨德森回到默西塞德郡，法克威胁要为卡里克和森林带来更多痛苦，这对阿森纳顶级联赛的顶级得分手构成威胁|在TikTok上关注我们前利物浦中场球员乔丹·亨德森和哈比·阿隆索在前夜的热烈接待" data-title="Premier League: 10 things to look out for this weekend" data-date="10-16 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-16 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 亨德森回到默西塞德郡，法克威胁要为卡里克和森林带来更多痛苦，这对阿森纳顶级联赛的顶级得分手构成威胁|在TikTok上关注我们前利物浦中场球员乔丹…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crgqwvnnyv30o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）与拳击手和伊普斯维奇球迷法比奥·沃德利（ Fabio Wardley ）以及英国广播公司（ BBC ）的读者和人工智能（ AI ）进行了对本周末英超" data-title="Sutton&#39;s predictions v boxer &amp; Ipswich fan Fabio Wardley" data-date="10-16 03:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 03:26</span>
          <span class="news-item-title">Sutton对拳击手和伊普斯维奇球迷Fabio Wardley的预测</span>
          <span class="news-item-title-en">Sutton's predictions v boxer & Ipswich fan Fabio Wardley</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）与拳击手和伊普斯维奇球迷法比奥·沃德利（ Fabio Wardley ）以及…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw77p152jz64o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联后卫利桑德罗·马丁内斯（ Lisandro Martinez ）在批评俱乐部等级制度的争议性言论后发表道歉。" data-title="Martinez apologises for outburst and fined by Man Utd" data-date="10-16 02:03" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 02:03</span>
          <span class="news-item-title">马丁内斯为爆发道歉并被曼联罚款</span>
          <span class="news-item-title-en">Martinez apologises for outburst and fined by Man Utd</span>
          <span class="news-value-point">💡 曼联后卫利桑德罗·马丁内斯（ Lisandro Martinez ）在批评俱乐部等级制度的争议性言论后发表道歉</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-17/10716023.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社东京10月16日电 (记者 朱晨曦)针对16日中午错误推测发生9.9级地震并发出相应警报一事，日本气象厅当日下午两度召开记者会致歉。日本气象厅表示，此次误发预警可能是震源位置推定错误所致。" data-title="错估震级9.9级 日本气象厅两度召开记者会致歉" data-date="10-17 00:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 00:45</span>
          <span class="news-item-title">错估震级9.9级 日本气象厅两度召开记者会致歉</span>
          <span class="news-value-point">💡 中新社东京10月16日电 (记者 朱晨曦)针对16日中午错误推测发生9.9级地震并发出相应警报一事，日本气象厅当日下午两度召开记者会致歉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-17/10716042.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“爷爷，再来一遍！”" data-title="七旬大爷大明湖畔演奏萨克斯火爆全网，网友从全国各地赶来捧场，称其“法拉利老了，依旧是法拉利”" data-date="10-17 00:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 00:27</span>
          <span class="news-item-title">七旬大爷大明湖畔演奏萨克斯火爆全网，网友从全国各地赶来捧场，称其“法拉利老了，依旧是法拉利”</span>
          <span class="news-value-point">💡 “爷爷，再来一遍</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1012962/apple-tv-4k-fourth-generation-fanttik-s1-pro-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="本周早些时候，苹果宣布推出新的Apple TV 4K ，其价格几乎是2022年型号推出时的两倍。亚马逊现在为即将推出的流媒体盒（将于11月13日推出）提供第一个折扣，就在Discou" data-title="The new Apple TV 4K just got its first (very small) discount" data-date="10-17 00:02" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 00:02</span>
          <span class="news-item-title">新款Apple TV 4K刚刚获得了第一个（非常小的）折扣</span>
          <span class="news-item-title-en">The new Apple TV 4K just got its first (very small) discount</span>
          <span class="news-value-point">💡 本周早些时候，苹果宣布推出新的Apple TV 4K ，其价格几乎是2022年型号推出时的两倍</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/188.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，暴雪《暗黑破坏神》系列新作《暗黑破坏神 V》的过场动画拍摄工作已经启动。游戏系列电影导演尼尔 · 大卫 · 卡特（Neil David Carter）昨日在 X 上发布了一张摄影棚照片，并配文“First shoot #Diablo5”，透露该项目已开始进行首轮拍摄。此次拍摄进展指向游戏中的动画向内容的制作，并不代表游戏整体开发已经进入后期阶段。参考IT之家此前报道，暴雪已在 2026 年暴雪嘉年华（BlizzCon 2026）正式公布《暗黑破坏神 V》，并确认游戏正在开发中，计划于 2029 年春季推出。根据暴雪官方公告，新作将呈现一个已经沦陷的庇护之地：迪亚波罗取得胜利，原有英雄已被击败。官方目前公布的信息主要集中在故事基调和发售窗口，尚未披露完整玩法细" data-title="暴雪《暗黑破坏神 V》开启首轮动画拍摄，游戏计划于 2029 年春季发售" data-date="10-16 23:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 23:44</span>
          <span class="news-item-title">暴雪《暗黑破坏神 V》开启首轮动画拍摄，游戏计划于 2029 年春季发售</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，暴雪《暗黑破坏神》系列新作《暗黑破坏神 V》的过场动画拍摄工作已经启动</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1012911/apple-homeview-apps-carplay-vergecast" target="_blank" rel="noopener" data-cat="zonghe" data-summary="自苹果发布大型智能家居公告以来，已经过去几天了，我们有关于Apple HomeView的更多信息和一系列新问题。该设备具有充足的计算能力，始终连接到电源，看起来像" data-title="Apple’s HomeView has an app problem" data-date="10-16 23:38" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 23:38</span>
          <span class="news-item-title">Apple的HomeView出现应用程序问题</span>
          <span class="news-item-title-en">Apple’s HomeView has an app problem</span>
          <span class="news-value-point">💡 自苹果发布大型智能家居公告以来，已经过去几天了，我们有关于Apple HomeView的更多信息和一系列新问题</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1012901/analogue-retro-console-supern-nt-plus-nintendo-sega-genesis-mega-plus" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Analogue今天宣布推出新版本的Super Nt和Mega Sg复古控制台，采用“重新设计的工业设计” ，并为控制器和配件内置无线连接。与原始版本一样，新的Super Nt Plus和Mega Sg Plu" data-title="Analogue is re-releasing its SNES and Genesis consoles with some nice upgrades" data-date="10-16 23:08" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 23:08</span>
          <span class="news-item-title">Analogue正在重新发布其SNES和Genesis游戏机，并进行了一些不错的升级</span>
          <span class="news-item-title-en">Analogue is re-releasing its SNES and Genesis consoles with some nice upgrades</span>
          <span class="news-value-point">💡 Analogue今天宣布推出新版本的Super Nt和Mega Sg复古控制台，采用“重新设计的工业设计” ，并为控制器和配件内置无线连接</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/185.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，在索尼 SIE 宣布于 2028 年 1 月起取消新游戏的实体光盘后，近期有越来越多的开发者将 PlayStation 独占游戏以“数字游戏”的形式搬上 PC 平台。据 Wccftech 今日报道，虽然索尼至今未将《GT 赛车》系列移植到 PC 平台，但这一局面已被第三方开发者打破。名为“mlgprorektm8”的开发者在 GitHub 上发布了《GT 赛车 Sport》PC 移植版。这意味着，继《血源诅咒》和《战神 3 重制版》之后又一款 PlayStation 非官方移植游戏首次登陆 PC 平台。值得一提的是，该 PC 移植版不包含任何游戏资源，玩家需要自备正版游戏的 ISO 镜像文件才能运行。另外，该项目加入了 AMD FSR 3.1 帧生成技术，并" data-title="索尼拒将《GT 赛车》上架 Steam：第三方开发者将《GT Sport》移植到 PC，支持 FSR 3.1 与着色器预编译" data-date="10-16 23:06" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 23:06</span>
          <span class="news-item-title">索尼拒将《GT 赛车》上架 Steam：第三方开发者将《GT Sport》移植到 PC，支持 FSR 3.1 与着色器预编译</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，在索尼 SIE 宣布于 2028 年 1 月起取消新游戏的实体光盘后，近期有越来越多的开发者将 PlaySta…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1012918/google-play-store-fake-whatsapp-android" target="_blank" rel="noopener" data-cat="zonghe" data-summary="本周早些时候，在Play商店中发现了一个Chrome克隆后， Reddit上的一名用户表示，他们在真实版本上方的“赞助”插槽中看到了一个虚假版本的WhatsApp。正如Android Authority早些时候报道的那样， WhatsApp的DUPE" data-title="A fake WhatsApp clone is showing up before the real version on the Play Store" data-date="10-16 23:02" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 23:02</span>
          <span class="news-item-title">假的WhatsApp克隆出现在Play商店的真实版本之前</span>
          <span class="news-item-title-en">A fake WhatsApp clone is showing up before the real version on the Play Store</span>
          <span class="news-value-point">💡 本周早些时候，在Play商店中发现了一个Chrome克隆后， Reddit上的一名用户表示，他们在真实版本上方的“赞助”插槽中看到了一个虚假版本…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/183.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，苹果董事会执行主席、前 CEO 蒂姆 · 库克今日发文告别本次中国之行，并分享记录视频。值得一提的是，这也是库克卸任苹果 CEO 后首次中国之行。IT之家附库克原文如下：感谢中国的每一位朋友，让这次旅程再次充满难忘的回忆。期待下次再见！Many thanks to everyone in China for another unforgettable visit. Until next time!IT之家注意到，库克于 10 月 10 日开启中国之行，首站落地广东广州，现场观看使用苹果 iPhone 18 Pro 手机拍摄非遗咏春作品，记录传统文化。随后，他到访了北京、上海等城市，接受了商务部部长王文涛会见。此外，他还现身爱奇艺总部，由爱奇艺 CEO 龚宇亲" data-title="库克卸任苹果 CEO 后首次中国之行结束：期待下次再见" data-date="10-16 22:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 22:56</span>
          <span class="news-item-title">库克卸任苹果 CEO 后首次中国之行结束：期待下次再见</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，苹果董事会执行主席、前 CEO 蒂姆 · 库克今日发文告别本次中国之行，并分享记录视频</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10716030.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网云南西双版纳10月16日电 (肖弼钰)“茶好喝，才吸引游客，我们从不愁客源。”南糯山村丫口新寨，哈尼族民宿老板散三的院子里，采茶制茶、茶山徒步、非遗体验等项目一应俱全。说起生意，这位从茶山起步的汉子语气笃定。" data-title="从过路客到留量客 社科专家为西双版纳勐海茶文旅康融合“开方”" data-date="10-16 22:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 22:56</span>
          <span class="news-item-title">从过路客到留量客 社科专家为西双版纳勐海茶文旅康融合“开方”</span>
          <span class="news-value-point">💡 中新网云南西双版纳10月16日电 (肖弼钰)“茶好喝，才吸引游客，我们从不愁客源</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/181.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，多年前曾有爆料称，育碧与腾讯旗下天美工作室群曾合作开发一款以中国古代为背景的《刺客信条》系列新作《刺客信条：命运》，但该项目目前已被取消。昨日，游戏媒体 MP1st 根据参与开发人员的作品集披露了早期玩法视频和截图，展示了潜行刺杀、信仰之跃，以及一款类似天机伞的旋转武器。这款作品原计划面向 PC 和主机平台，故事设定在公元前 206 年的秦朝。曝光素材大多来自 2025 年 2 月制作的原型，尚未达到完整游戏的开发阶段。曝光视频展示了一段任务流程：一名女性刺客需要进入一座遭历史人物项羽及其军队围困的宫殿，寻找一件神秘物品。片段还短暂展示了与项羽交战的首领战早期版本。这款游戏保留了《刺客信条》系列常见的潜行暗杀、跑酷和信仰之跃等玩法。其中一段画面展示了主角使用" data-title="中国秦朝背景《刺客信条：命运》早期实机视频曝光：腾讯天美工作室群主导，起步阶段即被取消" data-date="10-16 22:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 22:44</span>
          <span class="news-item-title">中国秦朝背景《刺客信条：命运》早期实机视频曝光：腾讯天美工作室群主导，起步阶段即被取消</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，多年前曾有爆料称，育碧与腾讯旗下天美工作室群曾合作开发一款以中国古代为背景的《刺客信条》系列新作《刺客信条：命…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/180.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，AOC 现已在京东上架“AGP277QKM”27 英寸显示器，该机主打 2K 425Hz，定价为 3254 元，部分地区国补后低至 2928.6 元。京东 AOC“AGP277QKM”显示器 3254 元直达链接该机配备一块 2560x1440 分辨率 425Hz 刷新率 1152 分区 QD-Mini LED 背光 Fast IPS 面板，峰值亮度 1200 尼特，对比度 1300:1，响应速度 0.3ms。该机支架支持升降 / 倾斜 / 旋转，显示器本体支持 VESA 100x100mm 壁挂，提供 2 个 HDMI 2.1、1 个 DP 2.1、3 个 USB-A 5Gbps 接口，采用内置电源。京东 11.11 无门槛红包 面额至高 26888 元，" data-title="AOC 上架“AGP277QKM”27 英寸显示器：2K 425Hz QD-Mini LED、内置电源，3254 元" data-date="10-16 22:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 22:41</span>
          <span class="news-item-title">AOC 上架“AGP277QKM”27 英寸显示器：2K 425Hz QD-Mini LED、内置电源，3254 元</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，AOC 现已在京东上架“AGP277QKM”27 英寸显示器，该机主打 2K 425Hz，定价为 3254 元…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/16/mark-wahlberg-on-using-ai-in-film-the-right-way-and-being-open-to-an-ai-clone-carrying-on-his-legacy/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="演员兼天使投资人马克·沃尔伯格（ Mark Wahlberg ）表示，他可以在电影制作中使用人工智能，前提是它被用来“增强你正在做的事情”。" data-title="Mark Wahlberg on using AI in film ‘the right way’ and being open to an AI clone carrying on his legacy" data-date="10-16 22:26" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 22:26</span>
          <span class="news-item-title">马克·沃尔伯格（ Mark Wahlberg ）在电影中“以正确的方式”使用人工智能，并对继承其遗产的人工智能克隆持开放态度</span>
          <span class="news-item-title-en">Mark Wahlberg on using AI in film ‘the right way’ and being open to an AI clone carrying on his legacy</span>
          <span class="news-value-point">💡 演员兼天使投资人马克·沃尔伯格（ Mark Wahlberg ）表示，他可以在电影制作中使用人工智能，前提是它被用来“增强你正在做的事情”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10716009.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网雅安10月16日电 (韩金雨)“茶田非常壮观，第一次感受到这么美的地方。”16日，在四川省雅安市名山区千里江山图景区，连云港日报记者姚新媛站在层层叠叠的茶垄间感叹道，“除了茶田外，一路上各种景点都打造得非常美。”" data-title="全国主流媒体走进雅安摄影采风 循茶香寻访茶乡新图景" data-date="10-16 22:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 22:26</span>
          <span class="news-item-title">全国主流媒体走进雅安摄影采风 循茶香寻访茶乡新图景</span>
          <span class="news-value-point">💡 中新网雅安10月16日电 (韩金雨)“茶田非常壮观，第一次感受到这么美的地方</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10716008.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网西宁10月16日电 (记者 潘雨洁)16日，青海省多部门联合召开新闻发布会，聚焦非法进入三江源国家公园突出风险，介绍源头预防、协同打击等相关治理情况。" data-title="青海多部门协同打击非法进入三江源国家公园行为" data-date="10-16 22:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 22:23</span>
          <span class="news-item-title">青海多部门协同打击非法进入三江源国家公园行为</span>
          <span class="news-value-point">💡 中新网西宁10月16日电 (记者 潘雨洁)16日，青海省多部门联合召开新闻发布会，聚焦非法进入三江源国家公园突出风险，介绍源头预防、协同打击等相…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-17 00:48（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
