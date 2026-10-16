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
      <span>2026-10-16 20:38 抓取更新</span>
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
        <span class="channel-count">57</span>
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
  <div class="ov-item"><span class="ov-num">57</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-16/10715941.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="工业和信息化部 财政部 国家发展改革委关于同意京津冀等5个城市群开展氢能综合应用试点工作的通知" data-title="京津冀等5个城市群将开展氢能综合应用试点工作" data-date="10-16 20:34" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-16 20:34</span>
      </div>
      <h2 class="hero-featured-title">京津冀等5个城市群将开展氢能综合应用试点工作</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-16/10715939.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社江西樟树10月16日电 (记者 姜涛)2026中国药都·樟树第57届全国药材药品交易会16日在江西樟树市岐黄小镇会展中心开幕。展区一台同步展出搭载AI药材检测大模型的中药材智能检测设备，吸引医药行业同仁观摩交流。" data-title="中国药都樟树办“药交会” 发布中药材AI检测大模型" data-date="10-16 20:30" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">中国药都樟树办“药交会” 发布中药材AI检测大模型</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/16/martinez-sorry-outburst-european-reaction-premier-league-latest-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进入周末⚽的所有最新足球新闻⚽十件需要注意的事情|足球日报|电子邮件LukeSky报道说，切尔西今天早上确认接受小膝盖手术的里斯·詹姆斯预计将缺席三次" data-title="James has knee surgery; Martínez sorry; Watford sacking reports ‘fake news’: football" data-date="10-16 20:36" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">James has knee surgery; Martínez sorry; Watford sacking reports ‘fake news’: football</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/014/152.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，理想汽车今日发布新一期答网友问，公布了关于 2026 款理想 i6 智能座舱的几大升级。IT之家从官方介绍获悉，2026 款理想 i6 支持 Apple CarPlay、HUAWEI HiCar 和 ICCOA Carlink。手机连上车机后，原车的车辆控制、驾驶信息、空调、座椅调节等功能照常可用，车机 App 和手机 App 之间也可以丝滑切换。2026 款理想 i6 的 29 英寸 6K 全景屏，不只是把屏幕做得更大、更清楚，也重新考虑了主驾、副驾和停车休息时，大家各自最常用的体验。开车时，信息看得更清楚：大卡片式桌面让常用信息一目了然；副驾无人或暂不使用屏幕时，更多显示空间会留给主驾。打开地图后，显示宽度增加近 1.5 倍，让导航视野更加开阔。副驾看视" data-title="2026 款理想 i6 智能座舱升级：支持苹果 CarPlay、华为 HiCar，更新 29 英寸 6K 全景屏" data-date="10-16 20:30" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">2026 款理想 i6 智能座舱升级：支持苹果 CarPlay、华为 HiCar，更新 29 英寸 6K 全景屏</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715941.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="工业和信息化部 财政部 国家发展改革委关于同意京津冀等5个城市群开展氢能综合应用试点工作的通知" data-title="京津冀等5个城市群将开展氢能综合应用试点工作" data-date="10-16 20:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:34</span>
          <span class="news-item-title">京津冀等5个城市群将开展氢能综合应用试点工作</span>
          <span class="news-value-point">💡 工业和信息化部 财政部 国家发展改革委关于同意京津冀等5个城市群开展氢能综合应用试点工作的通知</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715932.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网石家庄10月16日电 (李玉素 韩晓欧)16日，“我的赶考行”西柏坡主题红色研学活动在河北省石家庄市平山县西柏坡纪念馆正式启动。" data-title="“我的赶考行”西柏坡主题红色研学活动在河北平山启动" data-date="10-16 20:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:28</span>
          <span class="news-item-title">“我的赶考行”西柏坡主题红色研学活动在河北平山启动</span>
          <span class="news-value-point">💡 中新网石家庄10月16日电 (李玉素 韩晓欧)16日，“我的赶考行”西柏坡主题红色研学活动在河北省石家庄市平山县西柏坡纪念馆正式启动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715923.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网新疆五家渠10月16日电 (记者 戚亚平)“十五五”时期，新疆生产建设兵团第六师五家渠市将深入推进城乡更新与乡村全面振兴，加快构建城乡融合发展新格局。" data-title="新疆兵团第六师五家渠市构建城乡融合发展新格局" data-date="10-16 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:26</span>
          <span class="news-item-title">新疆兵团第六师五家渠市构建城乡融合发展新格局</span>
          <span class="news-value-point">💡 中新网新疆五家渠10月16日电 (记者 戚亚平)“十五五”时期，新疆生产建设兵团第六师五家渠市将深入推进城乡更新与乡村全面振兴，加快构建城乡融合…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715903.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网天津10月16日电 (记者 江莹)天津市第二中级人民法院近日发布公告，该院已于9月28日立案受理天津市人民检察院第二分院申请没收犯罪嫌疑人钱志敏违法所得一案，该案系涉案403亿余元的蓝天格锐集资诈骗案追赃重要程序。" data-title="天津二中院受理蓝天格锐案没收违法所得申请 涉案金额超403亿元" data-date="10-16 20:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:22</span>
          <span class="news-item-title">天津二中院受理蓝天格锐案没收违法所得申请 涉案金额超403亿元</span>
          <span class="news-value-point">💡 中新网天津10月16日电 (记者 江莹)天津市第二中级人民法院近日发布公告，该院已于9月28日立案受理天津市人民检察院第二分院申请没收犯罪嫌疑人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715899.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网德州10月16日电 (刘驰原)2026海峡两岸(德州)大禹文化交流活动10月16日在德州开幕。来自海峡两岸的专家学者、青年学子及宗亲代表齐聚一堂，围绕大禹文化的交流与传承开展学术研讨，共叙文化根脉，增进彼此认同。" data-title="2026海峡两岸（德州）大禹文化交流活动在山东德州开幕" data-date="10-16 20:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:22</span>
          <span class="news-item-title">2026海峡两岸（德州）大禹文化交流活动在山东德州开幕</span>
          <span class="news-value-point">💡 中新网德州10月16日电 (刘驰原)2026海峡两岸(德州)大禹文化交流活动10月16日在德州开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715918.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="李强主持召开国务院常务会议" data-title="李强主持召开国务院常务会议" data-date="10-16 20:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:04</span>
          <span class="news-item-title">李强主持召开国务院常务会议</span>
          <span class="news-value-point">💡 李强主持召开国务院常务会议</span>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715620.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网阿斯塔纳10月16日电 哈通社16日援引哈国家统计局数据显示，截至今年10月1日，该国登记机动车总量达611.46万辆，其中乘用车占83.9%。" data-title="哈萨克斯坦登记机动车超610万辆" data-date="10-16 14:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 14:04</span>
          <span class="news-item-title">哈萨克斯坦登记机动车超610万辆</span>
          <span class="news-value-point">💡 中新网阿斯塔纳10月16日电 哈通社16日援引哈国家统计局数据显示，截至今年10月1日，该国登记机动车总量达611.46万辆，其中乘用车占83.…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715618.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆10月16日电 (梁钦卿)走进沙坪坝区丰文街道三河村，青山和绿水相映成趣，绿树掩映的农家院落干净整洁。近年来，三河村全域整治农村人居环境，对道路、农房、庭院、沟渠、水体等实施微改造、精提升，乡村环境风貌显著提升。" data-title="山清水秀入画来，重庆美丽乡村背后的“生态密码”" data-date="10-16 14:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 14:03</span>
          <span class="news-item-title">山清水秀入画来，重庆美丽乡村背后的“生态密码”</span>
          <span class="news-value-point">💡 中新网重庆10月16日电 (梁钦卿)走进沙坪坝区丰文街道三河村，青山和绿水相映成趣，绿树掩映的农家院落干净整洁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-16/10715604.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月16日电 据加拿大城市新闻网站报道，加拿大艾伯塔省卡尔加里市当地时间15日下午发生一起多车连环相撞事故，造成3人死亡、19人受伤。" data-title="加拿大卡尔加里多车相撞起火致3死19伤" data-date="10-16 14:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 14:03</span>
          <span class="news-item-title">加拿大卡尔加里多车相撞起火致3死19伤</span>
          <span class="news-value-point">💡 中新网北京10月16日电 据加拿大城市新闻网站报道，加拿大艾伯塔省卡尔加里市当地时间15日下午发生一起多车连环相撞事故，造成3人死亡、19人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715588.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月16日电 应急管理部16日举行季度例行新闻发布会，有记者问，四季度是烟花爆竹生产经营旺季。应急管理部将采取哪些措施加强安全监管，防范遏制这方面的事故发生？" data-title="应急管理部：严打烟花爆竹线上销售线下寄递等非法违法行为" data-date="10-16 13:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 13:40</span>
          <span class="news-item-title">应急管理部：严打烟花爆竹线上销售线下寄递等非法违法行为</span>
          <span class="news-value-point">💡 中新网10月16日电 应急管理部16日举行季度例行新闻发布会，有记者问，四季度是烟花爆竹生产经营旺季</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-16/10715579.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月16日电 (记者 周昕)中国人民外交学会16日在北京宣布，2026全球治理论坛(雄安)将于10月23日至25日在河北雄安新区举行。" data-title="2026全球治理论坛（雄安）将于10月23日至25日举行" data-date="10-16 13:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 13:25</span>
          <span class="news-item-title">2026全球治理论坛（雄安）将于10月23日至25日举行</span>
          <span class="news-value-point">💡 中新社北京10月16日电 (记者 周昕)中国人民外交学会16日在北京宣布，2026全球治理论坛(雄安)将于10月23日至25日在河北雄安新区举行</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715939.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社江西樟树10月16日电 (记者 姜涛)2026中国药都·樟树第57届全国药材药品交易会16日在江西樟树市岐黄小镇会展中心开幕。展区一台同步展出搭载AI药材检测大模型的中药材智能检测设备，吸引医药行业同仁观摩交流。" data-title="中国药都樟树办“药交会” 发布中药材AI检测大模型" data-date="10-16 20:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:30</span>
          <span class="news-item-title">中国药都樟树办“药交会” 发布中药材AI检测大模型</span>
          <span class="news-value-point">💡 中新社江西樟树10月16日电 (记者 姜涛)2026中国药都·樟树第57届全国药材药品交易会16日在江西樟树市岐黄小镇会展中心开幕</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/taiwan-raising-usd4-billion-to-build-industrial-park-in-texas-to-support-us-chipmaking-supply-chain-project-to-support-countless-small-manufacturers-crucial-to-tsmc-foxconn-supply-chain" target="_blank" rel="noopener" data-cat="keji" data-summary="这个耗资40亿美元的工业园区将使那些无力在美国建造自己工厂的小型台湾公司更容易扩张并效仿台积电和富士康等台湾主要制造商。" data-title="Taiwan raising $4 billion to build industrial park in Texas to support US chipmaking supply chain" data-date="10-16 19:57" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-16 19:57</span>
          <span class="news-item-title">台湾筹集40亿美元在德克萨斯州建设工业园区，以支持美国芯片制造供应链</span>
          <span class="news-item-title-en">Taiwan raising $4 billion to build industrial park in Texas to support US chipmaking supply chain</span>
          <span class="news-value-point">💡 这个耗资40亿美元的工业园区将使那些无力在美国建造自己工厂的小型台湾公司更容易扩张并效仿台积电和富士康等台湾主要制造商</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself" target="_blank" rel="noopener" data-cat="keji" data-summary="Linus Torvalds将他的第一个LLM辅助补丁发布到Linux内核—在发布明确的亲AI指令后，老板本人使用了AI工具" data-title="Linus Torvalds posts his first AI-assisted patch to the Linux kernel, synthetic test clocks 23x performance leap" data-date="10-16 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-16 18:30</span>
          <span class="news-item-title">Linus Torvalds在Linux内核上发布了他的第一个AI辅助补丁，合成测试时钟性能提升了23倍</span>
          <span class="news-item-title-en">Linus Torvalds posts his first AI-assisted patch to the Linux kernel, synthetic test clocks 23x performance leap</span>
          <span class="news-value-point">💡 Linus Torvalds将他的第一个LLM辅助补丁发布到Linux内核—在发布明确的亲AI指令后，老板本人使用了AI工具</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/894.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 16 日消息，AI 公司 PrismML 昨日（10 月 15 日）发布博文，宣布推出 Ternary Bonsai 2 系列模型，共有 2B、4B 和 9B 三种规模，目标在手机、PC 以及可穿戴设备上本地运行 AI 智能体，执行推理、识图、调用工具等能力。Ternary Bonsai 2 系列模型基于阿里的 Qwen 3.5 基座构建，采用“三元”权重表示法，即仅用 -1、0、+1 三种数值编码模型参数。官方称，2B、4B、9B 模型的存储占用分别约为 0.43GB、0.95GB 和 2GB。在能力上，Bonsai 2 系列强调本地智能体的实用性：遵循指令、完成日常任务、在移动设备上调用工具、避免重复输出等。官方在 19 项基准上测试了智能工具调用、数学、指令遵循、编" data-title="Ternary Bonsai 2 系列 AI 模型登场：苹果 iPhone 18 Pro Max 上本地吞吐最高每秒 120 个词元" data-date="10-16 13:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 13:50</span>
          <span class="news-item-title">Ternary Bonsai 2 系列 AI 模型登场：苹果 iPhone 18 Pro Max 上本地吞吐最高每秒 120 个词元</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，AI 公司 PrismML 昨日（10 月 15 日）发布博文，宣布推出 Ternary Bonsai 2 系…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1012510/openai-chatgpt-google-chrome-tabs" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI的ChatGPT Atlas浏览器已不复存在，但现在ChatGPT的Google Chrome扩展正在进行一些升级，允许它使用您已经打开的浏览器选项卡。安装扩展后， OpenAI表示ChatGPT现在可以查看您的浏览器选项卡" data-title="ChatGPT can peek at your Chrome tabs now" data-date="10-16 06:43" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 06:43</span>
          <span class="news-item-title">ChatGPT现在可以查看您的Chrome标签页</span>
          <span class="news-item-title-en">ChatGPT can peek at your Chrome tabs now</span>
          <span class="news-value-point">💡 OpenAI的ChatGPT Atlas浏览器已不复存在，但现在ChatGPT的Google Chrome扩展正在进行一些升级，允许它使用您已经…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1012512/sega-total-war-shogun-2-remaster-pulled" target="_blank" rel="noopener" data-cat="keji" data-summary="在一次灾难性的发布之后，世嘉正在从店面中删除全面战争：幕府将军2 -完整版，用户抱怨诸如错误和升级等问题似乎是由人工智能完成的。完整版， 2011年策略的重制版" data-title="Sega pulls Total War: Shogun 2 remaster from sale following disastrous launch" data-date="10-16 06:35" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 06:35</span>
          <span class="news-item-title">世嘉在灾难性发布后从销售中撤出《全面战争：幕府将军2》重制版</span>
          <span class="news-item-title-en">Sega pulls Total War: Shogun 2 remaster from sale following disastrous launch</span>
          <span class="news-value-point">💡 在一次灾难性的发布之后，世嘉正在从店面中删除全面战争：幕府将军2 -完整版，用户抱怨诸如错误和升级等问题似乎是由人工智能完成的</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1012445/donald-trump-ai-photo-white-house-rennovation-column" target="_blank" rel="noopener" data-cat="keji" data-summary="唐纳德·特朗普（ Donald Trump ）总统在“真相社交” （ Truth Social ）上发布了一系列照片，展示了白宫的翻修工作，但其中一张似乎被人工智能修改了。这张照片将旧的白宫专栏与“修复的”专栏进行了比较，" data-title="Trump posts AI-edited photo to brag about White House restoration work" data-date="10-16 05:09" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 05:09</span>
          <span class="news-item-title">特朗普发布AI编辑照片吹嘘白宫修复工作</span>
          <span class="news-item-title-en">Trump posts AI-edited photo to brag about White House restoration work</span>
          <span class="news-value-point">💡 唐纳德·特朗普（ Donald Trump ）总统在“真相社交” （ Truth Social ）上发布了一系列照片，展示了白宫的翻修工作，但其…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta和苹果已经联手推出了这家社交媒体巨头的最新型号Muse Spark Open ，它将在苹果芯片上本地运行。" data-title="Meta launches an open-weight AI model that runs on Macs" data-date="10-16 04:04" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 04:04</span>
          <span class="news-item-title">Meta推出在Mac上运行的开放式权重AI模型</span>
          <span class="news-item-title-en">Meta launches an open-weight AI model that runs on Macs</span>
          <span class="news-value-point">💡 Meta和苹果已经联手推出了这家社交媒体巨头的最新型号Muse Spark Open ，它将在苹果芯片上本地运行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-sees-a-future-where-ai-devices-replace-the-need-to-use-apps/" target="_blank" rel="noopener" data-cat="keji" data-summary="在TechCrunch Disrupt上，亚马逊设备主管帕诺斯·帕奈（ Panos Panay ）描述了未来环境人工智能设备在后台工作，预测用户的需求，而不是等待命令。" data-title="Amazon devices chief Panos Panay sees a future where AI devices replace the need to use apps" data-date="10-16 03:55" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 03:55</span>
          <span class="news-item-title">亚马逊设备主管Panos Panay认为，未来人工智能设备将取代使用应用程序的需求</span>
          <span class="news-item-title-en">Amazon devices chief Panos Panay sees a future where AI devices replace the need to use apps</span>
          <span class="news-value-point">💡 在TechCrunch Disrupt上，亚马逊设备主管帕诺斯·帕奈（ Panos Panay ）描述了未来环境人工智能设备在后台工作，预测用户…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/15/anthropic-is-letting-metr-researchers-look-under-the-hood-with-employee-level-access/" target="_blank" rel="noopener" data-cat="keji" data-summary="METR将发布自己对Anthropic的风险、事件和实践的评估，前沿AI模型制造商已放弃阻止这些风险、事件和实践的权利。" data-title="Anthropic is letting METR researchers look under the hood with employee" data-date="10-16 03:14" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-16 03:14</span>
          <span class="news-item-title">Anthropic让METR研究人员与员工一起查看引擎盖下</span>
          <span class="news-item-title-en">Anthropic is letting METR researchers look under the hood with employee</span>
          <span class="news-value-point">💡 METR将发布自己对Anthropic的风险、事件和实践的评估，前沿AI模型制造商已放弃阻止这些风险、事件和实践的权利</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/sk-hynix-reportedly-playing-hardball-with-trump-admin-over-3d-nand-fab-company-demands-increased-chipmaking-equipment-exports-to-china-in-exchange-for-us-fab" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， SK海力士要求在美国建造新的Solidigm 3D NAND晶圆厂，并将设备出口到中国大连的Solidigm晶圆厂。" data-title="SK hynix reportedly playing hardball with Trump admin over 3D NAND fab" data-date="10-16 01:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-16 01:40</span>
          <span class="news-item-title">据报道， SK海力士与特朗普管理员在3D NAND晶圆厂打硬球</span>
          <span class="news-item-title-en">SK hynix reportedly playing hardball with Trump admin over 3D NAND fab</span>
          <span class="news-value-point">💡 据报道， SK海力士要求在美国建造新的Solidigm 3D NAND晶圆厂，并将设备出口到中国大连的Solidigm晶圆厂</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/15/business/russia-ukraine-data-centers-war.html" target="_blank" rel="noopener" data-cat="keji" data-summary="军队试图破坏为在线服务和人工智能系统提供动力的计算中心。" data-title="Data Centers Become Targets in Wars in Ukraine, Russia and the Middle East" data-date="10-16 00:22" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-16 00:22</span>
          <span class="news-item-title">数据中心成为乌克兰、俄罗斯和中东战争的目标</span>
          <span class="news-item-title-en">Data Centers Become Targets in Wars in Ukraine, Russia and the Middle East</span>
          <span class="news-value-point">💡 军队试图破坏为在线服务和人工智能系统提供动力的计算中心</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1011938/muse-ai-data-friends-consent" target="_blank" rel="noopener" data-cat="keji" data-summary="消费科技领域有一个日益增长的趋势：设计用于监视您周围的一切和每个人的小工具，无论其他人是否实际同意。现在，随着Meta的Muse等“人工智能个人助理”的出现，" data-title="Friends don’t let friends feed their data to AI agents" data-date="10-16 00:21" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 00:21</span>
          <span class="news-item-title">好友不会让好友将他们的数据馈送给人工智能代理</span>
          <span class="news-item-title-en">Friends don’t let friends feed their data to AI agents</span>
          <span class="news-value-point">💡 消费科技领域有一个日益增长的趋势：设计用于监视您周围的一切和每个人的小工具，无论其他人是否实际同意</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/683.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 16 日消息，除了苹果 CEO 约翰・特努斯（John Ternus）之外，《时代》今日还采访到了苹果全球营销高级副总裁格雷格・乔斯维亚克（Greg Joswiak）。当谈及 OpenAI 的硬件计划时，他表示，苹果并不担心 OpenAI 进军硬件领域带来的竞争。“我们并未感受到威胁。我们能够实现这样的软硬件整合，这意味着我们可以创造比其他任何人都更好的体验。”乔斯维亚克还谈到了苹果对人工智能产品的定位。他表示，苹果并不是专门为那些执着于追求超级智能的 AI 爱好者开发产品。“我们欢迎他们使用我们的产品，但他们不是我们的目标用户。我们的目标是让普通人的日常生活变得更好。”《时代》指出，苹果虽然正在训练自有 AI 模型，但在前沿 AI 技术方面仍与行业领先者存在差距。苹果高" data-title="苹果营销主管谈 OpenAI 硬件：我们没感到有威胁，相比追逐 AGI 更重视用户隐私与日常使用体验" data-date="10-16 00:02" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 00:02</span>
          <span class="news-item-title">苹果营销主管谈 OpenAI 硬件：我们没感到有威胁，相比追逐 AGI 更重视用户隐私与日常使用体验</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，除了苹果 CEO 约翰・特努斯（John Ternus）之外，《时代》今日还采访到了苹果全球营销高级副总裁格雷…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1011705/nvidia-rtx-spark-everything-runs-on-arm" target="_blank" rel="noopener" data-cat="keji" data-summary="十四年前的这个月，微软发布了一款基于Nvidia的Windows PC ，它将成为现代历史上最伟大的技术失败者之一。最初的微软Surface ，在Nvidia Tegra芯片上运行精简版的Windows ， b" data-title="The best reason to care about Nvidia’s RTX Spark: ‘everything’ will run on Arm" data-date="10-16 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 00:00</span>
          <span class="news-item-title">关注英伟达RTX Spark的最佳理由： “一切”将在Arm上运行</span>
          <span class="news-item-title-en">The best reason to care about Nvidia’s RTX Spark: ‘everything’ will run on Arm</span>
          <span class="news-value-point">💡 十四年前的这个月，微软发布了一款基于Nvidia的Windows PC ，它将成为现代历史上最伟大的技术失败者之一</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/16/martinez-sorry-outburst-european-reaction-premier-league-latest-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="进入周末⚽的所有最新足球新闻⚽十件需要注意的事情|足球日报|电子邮件LukeSky报道说，切尔西今天早上确认接受小膝盖手术的里斯·詹姆斯预计将缺席三次" data-title="James has knee surgery; Martínez sorry; Watford sacking reports ‘fake news’: football" data-date="10-16 20:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-16 20:36</span>
          <span class="news-item-title">詹姆斯接受了膝盖手术；马丁内斯很抱歉；沃特福德解雇报告了“假新闻” ：足球</span>
          <span class="news-item-title-en">James has knee surgery; Martínez sorry; Watford sacking reports ‘fake news’: football</span>
          <span class="news-value-point">💡 进入周末⚽的所有最新足球新闻⚽十件需要注意的事情|足球日报|电子邮件LukeSky报道说，切尔西今天早上确认接受小膝盖手术的里斯·詹姆斯预计将缺…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/144.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 16 日消息，三星宣布联合深度伪造检测公司 Reality Defender 合作，开发面向企业用户的端侧 AI 深度伪造检测方案。该方案将直接在三星 Galaxy 设备上运行，帮助企业识别 AI 生成的虚假语音、视频和图像，降低冒充诈骗及其他相关风险，计划率先落地新加坡市场。IT之家获悉，Reality Defender 专注于企业级深度伪造检测，利用多种 AI 模型实时分析语音、视频和图像内容。例如，该技术能够在实时通话中识别冒充他人的合成语音，也可用于客户身份识别和新用户注册审核，帮助企业发现可疑的虚假内容。Reality Defender 表示，随着生成式 AI 技术的发展，利用合成语音和视频实施诈骗的情况日益受到关注。有调查显示，2024 年新加坡有 56% 的" data-title="三星携手 Reality Defender，面向新加坡企业用户开发端侧 AI 深度伪造检测方案" data-date="10-16 19:58" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 19:58</span>
          <span class="news-item-title">三星携手 Reality Defender，面向新加坡企业用户开发端侧 AI 深度伪造检测方案</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，三星宣布联合深度伪造检测公司 Reality Defender 合作，开发面向企业用户的端侧 AI 深度伪造检…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c615jw414vypo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="富勒姆主教练阿尔瓦罗·阿贝洛亚（ Alvaro Arbeloa ）表示，重点不应放在他身上，因为他本周末正在寻找本赛季对阵赫尔城的第一场英超联赛胜利。" data-title="&#39;Not about me&#39; - Arbeloa dismisses future questions" data-date="10-16 18:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 18:24</span>
          <span class="news-item-title">“不是关于我” - Arbeloa驳斥了未来的问题</span>
          <span class="news-item-title-en">'Not about me' - Arbeloa dismisses future questions</span>
          <span class="news-value-point">💡 富勒姆主教练阿尔瓦罗·阿贝洛亚（ Alvaro Arbeloa ）表示，重点不应放在他身上，因为他本周末正在寻找本赛季对阵赫尔城的第一场英超联赛…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cp30ggvqj0do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的Ask Me Anything团队解释了如何在本周末在BBC上关注英超联赛第七周的比赛。" data-title="How to follow the Premier League on the BBC this weekend" data-date="10-16 17:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 17:52</span>
          <span class="news-item-title">如何在本周末在BBC上关注英超联赛</span>
          <span class="news-item-title-en">How to follow the Premier League on the BBC this weekend</span>
          <span class="news-value-point">💡 我们的Ask Me Anything团队解释了如何在本周末在BBC上关注英超联赛第七周的比赛</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq073d9l0ly9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西队长里斯·詹姆斯在接受膝盖手术后将缺席三个月的比赛。" data-title="Chelsea&#39;s James out for three months after knee surgery" data-date="10-16 17:02" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 17:02</span>
          <span class="news-item-title">切尔西的詹姆斯在膝盖手术后出局三个月</span>
          <span class="news-item-title-en">Chelsea's James out for three months after knee surgery</span>
          <span class="news-value-point">💡 切尔西队长里斯·詹姆斯在接受膝盖手术后将缺席三个月的比赛</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/16/premier-league-teams-run-more-win-matches-distance-opta" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="权威人士经常批评团队跑得不够，但距离和结果之间是否存在联系？ Opta Analyst的《It was like clockwork》。曼联在对阵托特纳姆热刺的比赛中失分，批评者很快质疑他们的努力" data-title="Do Premier League teams really need to run more to win matches?" data-date="10-16 15:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-16 15:30</span>
          <span class="news-item-title">英超球队真的需要跑得更多才能赢得比赛吗？</span>
          <span class="news-item-title-en">Do Premier League teams really need to run more to win matches?</span>
          <span class="news-value-point">💡 权威人士经常批评团队跑得不够，但距离和结果之间是否存在联系</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqy7l51e80p0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）的FPL专家詹尼·巴蒂斯（ Gianni Buttice ）研究了幻想英超联赛（ Fantasy Premier League ）经理们进入第七周游戏周面临的一些最大困境。" data-title="Are De Cuyper and Gross essential? FPL gameweek seven dilemmas" data-date="10-16 15:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-16 15:28</span>
          <span class="news-item-title">De Cuyper和Gross是必不可少的吗？ FPL游戏周七难题</span>
          <span class="news-item-title-en">Are De Cuyper and Gross essential? FPL gameweek seven dilemmas</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）的FPL专家詹尼·巴蒂斯（ Gianni Buttice ）研究了幻想英超联赛（ Fantasy …</span>
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
        <a class="news-item" href="https://www.theguardian.com/football/who-scored-blog/2026/oct/15/chelsea-premier-league-fun-team-sustainable-xabi-alonso-europe" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="哈比·阿隆索的球队以惊人的速度得分和让步。这对中立者来说很棒，但不一定是获得欧洲资格的最佳方式。通过WhoScoredWatching切尔西本赛季应该附带健康警告。目标的到来是丰富的，" data-title="Chelsea are the Premier League’s most fun team but is it sustainable?" data-date="10-15 23:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-15 23:30</span>
          <span class="news-item-title">切尔西是英超最有趣的球队，但它是可持续的吗？</span>
          <span class="news-item-title-en">Chelsea are the Premier League’s most fun team but is it sustainable?</span>
          <span class="news-value-point">💡 哈比·阿隆索的球队以惊人的速度得分和让步</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/014/152.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，理想汽车今日发布新一期答网友问，公布了关于 2026 款理想 i6 智能座舱的几大升级。IT之家从官方介绍获悉，2026 款理想 i6 支持 Apple CarPlay、HUAWEI HiCar 和 ICCOA Carlink。手机连上车机后，原车的车辆控制、驾驶信息、空调、座椅调节等功能照常可用，车机 App 和手机 App 之间也可以丝滑切换。2026 款理想 i6 的 29 英寸 6K 全景屏，不只是把屏幕做得更大、更清楚，也重新考虑了主驾、副驾和停车休息时，大家各自最常用的体验。开车时，信息看得更清楚：大卡片式桌面让常用信息一目了然；副驾无人或暂不使用屏幕时，更多显示空间会留给主驾。打开地图后，显示宽度增加近 1.5 倍，让导航视野更加开阔。副驾看视" data-title="2026 款理想 i6 智能座舱升级：支持苹果 CarPlay、华为 HiCar，更新 29 英寸 6K 全景屏" data-date="10-16 20:30" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 20:30</span>
          <span class="news-item-title">2026 款理想 i6 智能座舱升级：支持苹果 CarPlay、华为 HiCar，更新 29 英寸 6K 全景屏</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，理想汽车今日发布新一期答网友问，公布了关于 2026 款理想 i6 智能座舱的几大升级</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/googlebooks-are-as-poorly-timed-as-valves-steam-machine-and-may-suffer-a-similar-fate" target="_blank" rel="noopener" data-cat="zonghe" data-summary="谷歌试图通过Googlebooks升级其Chromebook平台。但时机不可能更糟。推出时的手机支持非常有限，大多数人使用安卓手机和Chromebook ，因为它们很便宜。" data-title="Googlebooks are as poorly timed as Valve’s Steam Machine, and may suffer a similar fate" data-date="10-16 20:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-16 20:30</span>
          <span class="news-item-title">Googlebooks的时机与Valve的Steam机器一样糟糕，可能会遭遇类似的命运</span>
          <span class="news-item-title-en">Googlebooks are as poorly timed as Valve’s Steam Machine, and may suffer a similar fate</span>
          <span class="news-value-point">💡 谷歌试图通过Googlebooks升级其Chromebook平台</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715929.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆10月16日电 (记者 钟旖)职引未来·“渝”见Offer——2026年全国城市联合招聘高校毕业生(重庆)秋季专场活动16日在重庆工商大学举行。" data-title="重庆办专场招聘活动拓青年就业渠道" data-date="10-16 20:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:28</span>
          <span class="news-item-title">重庆办专场招聘活动拓青年就业渠道</span>
          <span class="news-value-point">💡 中新网重庆10月16日电 (记者 钟旖)职引未来·“渝”见Offer——2026年全国城市联合招聘高校毕业生(重庆)秋季专场活动16日在重庆工商…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/150.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，懂车帝刚刚发布声明，针对近期网络上流传的“懂车帝删视频”相关谣言进行澄清。声明指出，部分网络内容通过拼接不同账号、不同时间的数据截图，制造“懂车帝大规模删除测试视频”的假象，相关说法均属谣言。IT之家附官方截图如下：懂车帝举例说明，部分自媒体所描述内容不实，除刹车踏板支架相关视频外，懂车帝实测账号近期未更新过其他内容，“7 月后视频都删了”属于谣言。此外，还有人将懂车帝原创账号在不同时间、不同系统版本下显示的作品数量 —— 四舍五入后的“1.5 万”与精确数字“14639”—— 拼接在一起，得出的“删视频”结论同样属于谣言。另外，直接将两个不同账号的发布作品数据进行拼接，声称的“删视频”亦属于谣言。懂车帝在声明中表示，近期已有多条谣言在未与公司核实的情况下，" data-title="懂车帝否认“7 月后视频都删了”：系恶意拼图，呼吁网友注意甄别" data-date="10-16 20:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 20:25</span>
          <span class="news-item-title">懂车帝否认“7 月后视频都删了”：系恶意拼图，呼吁网友注意甄别</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，懂车帝刚刚发布声明，针对近期网络上流传的“懂车帝删视频”相关谣言进行澄清</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715908.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网双鸭山10月16日电 (张晓玲 田德雨)连日来，受降温、降水天气叠加影响，黑龙江双鸭山友谊县秋收工作进入攻坚阶段。全县水稻进入成熟收获期，为有效应对深秋霜冻、降雨天气带来的不利影响，友谊县抢抓短暂晴好窗口期，组织农户、农机力量昼夜抢收，全力防范水稻倒伏、霉变、烂田风险。" data-title="黑龙江友谊县：抢晴战雨保秋收" data-date="10-16 20:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:23</span>
          <span class="news-item-title">黑龙江友谊县：抢晴战雨保秋收</span>
          <span class="news-value-point">💡 中新网双鸭山10月16日电 (张晓玲 田德雨)连日来，受降温、降水天气叠加影响，黑龙江双鸭山友谊县秋收工作进入攻坚阶段</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715906.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨10月16日电 (李雪莹 田德雨)金秋十月，礼赞耕耘。10月16日，龙江丰收文化节在哈尔滨西城红场拉开帷幕。来自黑龙江各地的展商与广大市民、游客齐聚一堂，共赏黑土丰收盛景，共品黑龙江物产之美。" data-title="黑龙江哈尔滨：2000余款“龙江好物”亮相丰收文化节" data-date="10-16 20:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:23</span>
          <span class="news-item-title">黑龙江哈尔滨：2000余款“龙江好物”亮相丰收文化节</span>
          <span class="news-value-point">💡 中新网哈尔滨10月16日电 (李雪莹 田德雨)金秋十月，礼赞耕耘</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715897.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月16日电(郭其钰)10月16日，首届全球具身智能应用创新挑战赛暨2026中国机器人大赛在浙江杭州举办。本届大赛设置22个赛道、60个赛项及3个企业独立赛项。经层层选拔，来自300余所高校的2000余支队伍、近5000名选手角逐总决赛。" data-title="“文武双全”亮绝技 300余所高校组队竞逐机器人赛场" data-date="10-16 20:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:22</span>
          <span class="news-item-title">“文武双全”亮绝技 300余所高校组队竞逐机器人赛场</span>
          <span class="news-value-point">💡 中新网杭州10月16日电(郭其钰)10月16日，首届全球具身智能应用创新挑战赛暨2026中国机器人大赛在浙江杭州举办</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/149.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，CDPR 联合首席执行官 Michał Nowakowski 于 10 月 15 日在接受波兰媒体 PAP Biznes 的采访表示，《赛博朋克 2077》真人电影不会照搬游戏剧情，而是计划在同一世界观下讲述全新的故事。该项目由 CD Projekt 与派拉蒙合作推进，制片人 Lorenzo di Bonaventura 曾参与真人版《变形金刚》系列电影。Nowakowski 表示，制作团队希望讲述发生在《赛博朋克》世界中的原创故事，而不是将游戏剧情一比一搬上银幕。这意味着影片将采用原创叙事，而非直接复刻游戏主角 V 的经历。路透社 10 月 9 日报道称，派拉蒙影业正与 CD Projekt RED 合作开发这部真人电影，Lorenzo di Bonave" data-title="CDPR 确认《赛博朋克 2077》真人电影不会照搬游戏剧情，与动画一样讲述原创故事" data-date="10-16 20:17" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 20:17</span>
          <span class="news-item-title">CDPR 确认《赛博朋克 2077》真人电影不会照搬游戏剧情，与动画一样讲述原创故事</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，CDPR 联合首席执行官 Michał Nowakowski 于 10 月 15 日在接受波兰媒体 PAP B…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715894.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南昌10月16日电 (记者 李韵涵)10月16日，“黄庭坚杯”江西省中小学生书画大赛优秀作品展开幕式在江西省美术馆举行，本次展览共展出114件书画作品，充分展现新时代江西少年儿童的审美情趣与家国情怀。" data-title="展审美情趣与家国情怀 百余件江西省中小学生书画作品集中亮相" data-date="10-16 20:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:03</span>
          <span class="news-item-title">展审美情趣与家国情怀 百余件江西省中小学生书画作品集中亮相</span>
          <span class="news-value-point">💡 中新网南昌10月16日电 (记者 李韵涵)10月16日，“黄庭坚杯”江西省中小学生书画大赛优秀作品展开幕式在江西省美术馆举行，本次展览共展出11…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-16/10715893.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网双鸭山10月16日电 (韩雪 刘海建)眼下正值乌苏里江秋季禁渔期，为落实中俄界江禁渔相关规定，防范非法捕捞、越界作业风险，15日，黑龙江出入境边防检查总站双鸭山边境管理支队在辖区沿江一线强化管控，维护界江秩序与边境稳定。" data-title="乌苏里江禁渔期管控推进 黑龙江双鸭山边境警方守界江平安" data-date="10-16 20:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-16 20:03</span>
          <span class="news-item-title">乌苏里江禁渔期管控推进 黑龙江双鸭山边境警方守界江平安</span>
          <span class="news-value-point">💡 中新网双鸭山10月16日电 (韩雪 刘海建)眼下正值乌苏里江秋季禁渔期，为落实中俄界江禁渔相关规定，防范非法捕捞、越界作业风险，15日，黑龙江出…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/146.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，中国联通今日宣布，面向 2009 年通过联通渠道购得正版 iPhone 的老用户，开放 iPhone Duo 最高优先级购机资格。相关用户可通过联通官网（IT之家附地址：https://go.10010.com:32001/apple-booking/）核验身份，结果显示为“尊享挚友”后，可前往就近的联通苹果授权门店优先购机。2009 年 10 月 30 日晚，中国联通在北京世贸天阶举行 iPhone 入华首销仪式，现场连续销售并为购机用户颁发印有编号的证书。当天到场的大多是办理 186 号段 3G 套餐的用户，这批人也成为中国大陆正品 iPhone 的首批使用者。根据苹果官方新闻稿，iPhone Duo 是苹果首款可折叠机型，该机展开后为 7.6 英寸超视" data-title="中国联通回馈 2009 年首批 iPhone 用户，开放 iPhone Duo 最高优先级购机资格" data-date="10-16 20:00" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 20:00</span>
          <span class="news-item-title">中国联通回馈 2009 年首批 iPhone 用户，开放 iPhone Duo 最高优先级购机资格</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，中国联通今日宣布，面向 2009 年通过联通渠道购得正版 iPhone 的老用户，开放 iPhone Duo …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tablets/microsoft-surface/microsoft-surface-laptop-ultra-rtx-spark-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="微软的Surface Laptop Ultra是有史以来最漂亮的笔记本电脑，但在其上使用Windows与以往一样。只有人工智能爱好者才能充分利用RTX Spark。" data-title="Microsoft Surface Laptop Ultra review: RTX Spark in a straight-up beautiful Windows PC" data-date="10-16 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-16 20:00</span>
          <span class="news-item-title">微软Surface笔记本电脑Ultra评测：在漂亮的Windows PC上使用RTX Spark</span>
          <span class="news-item-title-en">Microsoft Surface Laptop Ultra review: RTX Spark in a straight-up beautiful Windows PC</span>
          <span class="news-value-point">💡 微软的Surface Laptop Ultra是有史以来最漂亮的笔记本电脑，但在其上使用Windows与以往一样</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/988582/apple-iphone-duo-preorder-buy-foldable" target="_blank" rel="noopener" data-cat="zonghe" data-summary="很少有手机比可折叠iPhone更令人期待，但它终于来了。iPhone Duo在Apple的“Surprise and shine”活动中与iPhone 18 Pro以及Apple Watch Series 12和Ultra 4型号一同亮相。苹果的第一个FOL" data-title="The iPhone Duo is now available to preorder at $1,999" data-date="10-16 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 20:00</span>
          <span class="news-item-title">IPhone Duo现在可以以$ 1,999的价格预订</span>
          <span class="news-item-title-en">The iPhone Duo is now available to preorder at $1,999</span>
          <span class="news-value-point">💡 很少有手机比可折叠iPhone更令人期待，但它终于来了</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1012628/microsoft-surface-laptop-ultra-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在设置了微软的Surface Laptop Ultra之后，我花了五分钟盯着它看。我对其类似MacBook Pro的设计并不感到惊讶，也没有被其明亮的显示屏所震撼。我试图弄清楚我用一台$ 5,900的笔记本电脑实际上会做什么。" data-title="Surface Laptop Ultra review: a different kind of MacBook Pro" data-date="10-16 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-16 20:00</span>
          <span class="news-item-title">Surface Laptop Ultra回顾：不同类型的MacBook Pro</span>
          <span class="news-item-title-en">Surface Laptop Ultra review: a different kind of MacBook Pro</span>
          <span class="news-value-point">💡 在设置了微软的Surface Laptop Ultra之后，我花了五分钟盯着它看</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/143.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 16 日消息，作为微星 40 周年推出的特别之作，神影 16 魔龙姬限定款把二次元 IP“魔龙姬”融进了传统的游戏本里，用一抹星云白取代常见的黑色机身，让这台高性能机器多了一份清爽与个性。目前IT之家已经拿到了这款特别的游戏本新品 —— 神影 16 魔龙姬星际套装 2026。值得一提的是，本次IT之家拿到的并不只有笔记本本体，还包括同主题耳机、鼠标和鼠标垫。从机身到外设，整套装备都融入了魔龙姬的设计元素，视觉风格保持统一。设计上，微星神影 16 魔龙姬限定款采用了星云白配色，并将微星旗下的二次元 IP“魔龙姬”融入整体设计。机身 A 面采用白色盖板，右侧布置了微星龙盾 Logo。表面的幻彩珠光涂层会随着光线和观察角度的变化，呈现出细微的色泽差异，让纯白机身多了几分层次感。" data-title="【IT之家开箱】微星神影 16 魔龙姬星际套装图赏：星云白 + 魔龙姬，这套装备有点特别" data-date="10-16 19:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-16 19:56</span>
          <span class="news-item-title">【IT之家开箱】微星神影 16 魔龙姬星际套装图赏：星云白 + 魔龙姬，这套装备有点特别</span>
          <span class="news-value-point">💡 IT之家 10 月 16 日消息，作为微星 40 周年推出的特别之作，神影 16 魔龙姬限定款把二次元 IP“魔龙姬”融进了传统的游戏本里，用一…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-16 20:38（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
