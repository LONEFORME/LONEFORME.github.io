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
      <span>2026-10-30 15:49 抓取更新</span>
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
        <span class="channel-count">61</span>
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
        <span class="channel-count">1</span>
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
  <div class="ov-item"><span class="ov-num">61</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-30/10723365.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会。" data-title="外交部：人类命运共同体理念连续第10年写入联大外空决议" data-date="10-30 15:39" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-30 15:39</span>
      </div>
      <h2 class="hero-featured-title">外交部：人类命运共同体理念连续第10年写入联大外空决议</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/020/154.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，今日有大量开发者在 DeepSeek 官网的前端代码中发现了一组与“Cyber”模型相关的申请入口与接口逻辑。从流出的代码信息来看，申请页面的路由指向 /usage/ model-application，并设置了 feature gate 开关，未获得权限的账号访问时会被重定向回用量页面。代码中还出现了与 Cyber Key 创建、额度管理相关的接口，以及企业版与个人版两套不同的申请模板。代码中出现的模型标识有两个，分别为 cyber-personal-v3 和 cyber-enterprise-v4。前者面向个人安全从业者，申请条件包括提供身份证信息并完成人脸核验；后者面向企业主体，除实名材料外还需提交营业执照与授权书。根据流出的申请须知，两类渠道的共同门" data-title="DeepSeek 官网代码曝光 Cyber 独立模型：分企业版与个人版，小范围灰度中" data-date="10-30 15:50" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">DeepSeek 官网代码曝光 Cyber 独立模型：分企业版与个人版，小范围灰度中</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cqy0r31kwne0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么文森特·康帕尼（ Vincent Kompany ）的健康恐慌提醒我们，管理层会造成身心损失" data-title="Why managers must put their own fitness first" data-date="10-30 15:41" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Why managers must put their own fitness first</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/020/148.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 30 日消息，熊猫现已在京东上架“F32U4”31.5 英寸显示器，该机主打 4K 120Hz，定价为 1249 元，部分地区国补后低至 1124 元。京东熊猫“F32U4”显示器 1249 元点此访问该机配备一块 3840x2160 分辨率 120Hz 面板，对比度 1000:1，显示器响应速度 1ms，支持 8-Bit 色彩，覆盖 138% sRGB 色域容积和 102% DCI-P3 色域容积。该机支架支持升降 / 倾斜 / 旋转，显示器本体内置双扬声器，支持 VESA 100x100mm 壁挂，提供 2 个 HDMI 2.0、2 个 DP 1.4、1 个 3.5mm 音频接口。IT之家附显示器参数：京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3" data-title="熊猫推出“F32U4”31.5 英寸显示器：4K 120Hz、双扬声器，1249 元" data-date="10-30 15:39" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">熊猫推出“F32U4”31.5 英寸显示器：4K 120Hz、双扬声器，1249 元</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723365.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会。" data-title="外交部：人类命运共同体理念连续第10年写入联大外空决议" data-date="10-30 15:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:39</span>
          <span class="news-item-title">外交部：人类命运共同体理念连续第10年写入联大外空决议</span>
          <span class="news-value-point">💡 中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723364.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月30日电 据“中国海警”微信公众号消息，10月30日，中国海警位中国黄岩岛领海及周边区域开展执法巡查，这是对菲方侵权挑衅行径的必要反制。10月份以来，中国海警持续加强黄岩岛领海及周边区域执法巡查，依法依规处置非法侵权船只，进一步强化有关海域管控，坚决维护国家领土主权和海洋权益。" data-title="中国海警位中国黄岩岛领海及周边区域执法巡查" data-date="10-30 15:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:39</span>
          <span class="news-item-title">中国海警位中国黄岩岛领海及周边区域执法巡查</span>
          <span class="news-value-point">💡 中新网10月30日电 据“中国海警”微信公众号消息，10月30日，中国海警位中国黄岩岛领海及周边区域开展执法巡查，这是对菲方侵权挑衅行径的必要反…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723361.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 (记者 谢雁冰 张素)检察公益诉讼法草案三次审议稿将提请十四届全国人大常委会第二十五次会议审议。全国人大常委会法工委发言人黄海华30日在记者会上表示，草案三审稿拟完善管辖和审判程序，与有关诉讼法做好衔接。" data-title="检察公益诉讼法草案将三审 拟完善管辖和审判程序" data-date="10-30 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:35</span>
          <span class="news-item-title">检察公益诉讼法草案将三审 拟完善管辖和审判程序</span>
          <span class="news-value-point">💡 中新网北京10月30日电 (记者 谢雁冰 张素)检察公益诉讼法草案三次审议稿将提请十四届全国人大常委会第二十五次会议审议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723356.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会。" data-title="南非未受邀参加二十国集团外长会 中方：支持南非继续参与框架内相关活动" data-date="10-30 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:30</span>
          <span class="news-item-title">南非未受邀参加二十国集团外长会 中方：支持南非继续参与框架内相关活动</span>
          <span class="news-value-point">💡 中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723354.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月30日电 据南部战区微信公众号消息，10月30日，中国人民解放军南部战区组织海空兵力位中国黄岩岛领海领空及周边海空域开展战备警巡，这是对菲方侵权挑衅行径的必要反制。黄岩岛是中国固有领土。10月份以来，战区部队组织海空兵力持续加强黄岩岛领海周边海空域巡逻警戒，进一步强化有关海空域管控力度，有力有效应对各类侵权挑衅行径，坚决捍卫国家主权安全，坚定维护南海地区和平稳定。" data-title="中国人民解放军南部战区位中国黄岩岛领海领空及周边区域组织战备警巡" data-date="10-30 15:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:29</span>
          <span class="news-item-title">中国人民解放军南部战区位中国黄岩岛领海领空及周边区域组织战备警巡</span>
          <span class="news-value-point">💡 中新网10月30日电 据南部战区微信公众号消息，10月30日，中国人民解放军南部战区组织海空兵力位中国黄岩岛领海领空及周边海空域开展战备警巡，这…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723344.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：征求对中共中央关于持之以恒推进全面从严治党若干重大问题的决定的意见" data-title="中共中央召开党外人士座谈会 习近平主持并发表重要讲话" data-date="10-30 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:26</span>
          <span class="news-item-title">中共中央召开党外人士座谈会 习近平主持并发表重要讲话</span>
          <span class="news-value-point">💡 原标题：征求对中共中央关于持之以恒推进全面从严治党若干重大问题的决定的意见</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-30/10723352.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会。" data-title="美媒称黄仁勋成为涉华情报人员接触目标 中方：纯属对华污蔑抹黑" data-date="10-30 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:26</span>
          <span class="news-item-title">美媒称黄仁勋成为涉华情报人员接触目标 中方：纯属对华污蔑抹黑</span>
          <span class="news-value-point">💡 中新网北京10月30日电 (记者 张蔚然)中国外交部发言人郭嘉昆30日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723293.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月30日电 圣萨尔瓦多消息：据萨尔瓦多《世界报》等媒体报道，萨尔瓦多前总统安东尼奥·萨卡当地时间29日服刑期满获释，于当天下午前往首都圣萨尔瓦多一家法院报告获释情况。他此前曾因侵吞公款和洗钱被判处十年监禁。" data-title="萨尔瓦多前总统萨卡刑满释放 曾因贪污3亿美元公款入狱" data-date="10-30 15:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:02</span>
          <span class="news-item-title">萨尔瓦多前总统萨卡刑满释放 曾因贪污3亿美元公款入狱</span>
          <span class="news-value-point">💡 中新网北京10月30日电 圣萨尔瓦多消息：据萨尔瓦多《世界报》等媒体报道，萨尔瓦多前总统安东尼奥·萨卡当地时间29日服刑期满获释，于当天下午前往…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723286.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网首尔10月30日电 据中国驻韩国大使馆30日消息，近期，中国驻韩国大使馆委托韩国权威民调机构盖洛普实施《韩民众对华认知民调》。10月1日至7日，盖洛普面向韩国1000名受访者开展民意调查，调查对象涵盖不同年龄、性别、地区及政治倾向的群体。现发布结果如下：" data-title="最新民调显示支持对华合作是韩国社会的共识" data-date="10-30 15:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:02</span>
          <span class="news-item-title">最新民调显示支持对华合作是韩国社会的共识</span>
          <span class="news-value-point">💡 中新网首尔10月30日电 据中国驻韩国大使馆30日消息，近期，中国驻韩国大使馆委托韩国权威民调机构盖洛普实施《韩民众对华认知民调》</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723323.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月30日电 据路透社30日报道，知情人士透露，五角大楼官员最近几周要求几个北约国家缓和有关俄罗斯的言论，理由是欧洲领导人和官员的一些声明破坏了欧洲大陆的安全。" data-title="消息人士：五角大楼官员要求欧洲缓和对俄言辞" data-date="10-30 14:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 14:59</span>
          <span class="news-item-title">消息人士：五角大楼官员要求欧洲缓和对俄言辞</span>
          <span class="news-value-point">💡 中新网10月30日电 据路透社30日报道，知情人士透露，五角大楼官员最近几周要求几个北约国家缓和有关俄罗斯的言论，理由是欧洲领导人和官员的一些声…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/29/world/middleeast/israel-voter-data-takeaways.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一些团体支持本雅明·内塔尼亚胡总理的政党，但支持率有所下降。投票率也是选举中的一个突出因素。" data-title="What Israeli Election Results Reveal About the Electorate" data-date="10-30 14:31" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 14:31</span>
          <span class="news-item-title">以色列选举结果揭示了选民的哪些方面</span>
          <span class="news-item-title-en">What Israeli Election Results Reveal About the Electorate</span>
          <span class="news-value-point">💡 一些团体支持本雅明·内塔尼亚胡总理的政党，但支持率有所下降</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723283.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月30日电 据美联社报道，美国俄勒冈州亚姆希尔县警方29日表示，当天该州发生两架直升机相撞事故，造成3人死亡。有关部门表示，事故还导致一条公路关闭。" data-title="美国突发直升机相撞事故 致3人死亡" data-date="10-30 13:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 13:58</span>
          <span class="news-item-title">美国突发直升机相撞事故 致3人死亡</span>
          <span class="news-value-point">💡 中新网10月30日电 据美联社报道，美国俄勒冈州亚姆希尔县警方29日表示，当天该州发生两架直升机相撞事故，造成3人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723253.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社悉尼10月30日电(记者 薄雯雯 贾靖峰 张子扬 张蔚然 安英昭)从杭州到天津，约5小时的高铁旅程，让澳大利亚人皮特·怀泽尔想起半个多世纪前的首次中国行。“1975年我第一次来中国时，同样的路程花了20多个小时。”他在纪行中写道，如今的旅程平稳而舒适，令人赞叹。" data-title="悉尼中国文化中心：从文化相遇开始，让相知跨越山海" data-date="10-30 13:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 13:28</span>
          <span class="news-item-title">悉尼中国文化中心：从文化相遇开始，让相知跨越山海</span>
          <span class="news-value-point">💡 中新社悉尼10月30日电(记者 薄雯雯 贾靖峰 张子扬 张蔚然 安英昭)从杭州到天津，约5小时的高铁旅程，让澳大利亚人皮特·怀泽尔想起半个多世纪…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723243.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月30日电 据美国《华尔街日报》当地时间10月29日报道，知情人士透露，在美国总统特朗普数周的施压动摇了基辅对来自美国支持的信心后，乌克兰军方已暂停对俄罗斯炼油厂的打击。" data-title="美媒曝：特朗普施压下，乌克兰已暂停袭击俄罗斯炼油厂" data-date="10-30 12:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 12:54</span>
          <span class="news-item-title">美媒曝：特朗普施压下，乌克兰已暂停袭击俄罗斯炼油厂</span>
          <span class="news-value-point">💡 中新网10月30日电 据美国《华尔街日报》当地时间10月29日报道，知情人士透露，在美国总统特朗普数周的施压动摇了基辅对来自美国支持的信心后，乌…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-30/10723164.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近期，日本政府加力推动“产军学合作”，推动学术界进入军事防卫领域。日本民间和平组织负责人小野政美认为，这一危险动向将使学术研究再次被战争利用，给日本带来危机。" data-title="日本有识之士：日政府推动“产军学合作”将带来危机" data-date="10-30 10:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 10:19</span>
          <span class="news-item-title">日本有识之士：日政府推动“产军学合作”将带来危机</span>
          <span class="news-value-point">💡 近期，日本政府加力推动“产军学合作”，推动学术界进入军事防卫领域</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/020/154.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，今日有大量开发者在 DeepSeek 官网的前端代码中发现了一组与“Cyber”模型相关的申请入口与接口逻辑。从流出的代码信息来看，申请页面的路由指向 /usage/ model-application，并设置了 feature gate 开关，未获得权限的账号访问时会被重定向回用量页面。代码中还出现了与 Cyber Key 创建、额度管理相关的接口，以及企业版与个人版两套不同的申请模板。代码中出现的模型标识有两个，分别为 cyber-personal-v3 和 cyber-enterprise-v4。前者面向个人安全从业者，申请条件包括提供身份证信息并完成人脸核验；后者面向企业主体，除实名材料外还需提交营业执照与授权书。根据流出的申请须知，两类渠道的共同门" data-title="DeepSeek 官网代码曝光 Cyber 独立模型：分企业版与个人版，小范围灰度中" data-date="10-30 15:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:50</span>
          <span class="news-item-title">DeepSeek 官网代码曝光 Cyber 独立模型：分企业版与个人版，小范围灰度中</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，今日有大量开发者在 DeepSeek 官网的前端代码中发现了一组与“Cyber”模型相关的申请入口与接口逻辑</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/152.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，今天（30 日）上午，据彭博社援引知情人士消息称，印度 AI 基础设施企业 AM Intelligence 计划融资最多 30 亿美元（IT之家注：现汇率约合 200.31 亿元人民币），用于购买此前宣布采购的英伟达下一代芯片。AI 热潮带动的企业举债规模持续扩大。AM Intelligence 由印度可再生能源企业 Greenko 集团的创始人创办。知情人士透露，公司考虑通过发行债券、银行贷款等方式筹资。各种融资方式的占比尚未确定，公司还预计从潜在客户获得 3 亿美元（现汇率约合 20.03 亿元人民币）预付款。据悉，融资谈判仍处于初期阶段，具体条款可能调整。随着亚洲及其他地区加紧建设 AI 基础设施，企业为采购最新一代处理器动辄需要筹集数十亿美元，融资方" data-title="曝印度 AI 企业 AM Intelligence 寻求 30 亿美元融资，用于订购英伟达芯片" data-date="10-30 15:48" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:48</span>
          <span class="news-item-title">曝印度 AI 企业 AM Intelligence 寻求 30 亿美元融资，用于订购英伟达芯片</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，今天（30 日）上午，据彭博社援引知情人士消息称，印度 AI 基础设施企业 AM Intelligence 计…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/151.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，联发科今日发布 2026 财年（2026 年 1 月～2026 年 12 月）第三财季（2026 年 7 月～2026 年 9 月）报告： 营业总收入：1680.57 亿新台币（IT之家注：现汇率约合 345.69 亿元人民币），同比增长 18.27%，环比增长 10.43% 毛利润：778.5 亿新台币（现汇率约合 160.14 亿元人民币） 毛利率：46.32% 归母净利润：282 亿新台币（现汇率约合 58.01 亿元人民币） 基本每股收益：17.5 新台币（现汇率约合 3.6 元人民币） AI 解读 联发科 2026 年第三季度合并营收 1680.57 亿新台币（现汇率约合 345.69 亿元人民币） 百万元，大幅超出公司先前指引区间上限，同时净利润" data-title="联发科 2026 财年第三财季归母净利润 282 亿新台币" data-date="10-30 15:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:44</span>
          <span class="news-item-title">联发科 2026 财年第三财季归母净利润 282 亿新台币</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，联发科今日发布 2026 财年（2026 年 1 月～2026 年 12 月）第三财季（2026 年 7 月～…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/150.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 30 日消息，小米 REDMI 红米手机官方微博今日发布了“K100 答网友问”专栏文章，针对 K100 为什么用骁龙 8 至尊版、REDMI Clip Neo 为什么是双 MIC 设计等问题进行了解答。▲ IT之家开箱：小米 REDMI K100 黑色版图赏IT之家附小米 REDMI 红米手机本期答网友问重点内容如下：K100 为什么用骁龙 8 至尊版？这不是两年前发的芯片吗？正所谓“XXX 老了还是 XXX”，骁龙 8 至尊版的确不是当代最新平台，但它依然是同档领先的性能基座。对于大多数用户而言，骁龙 8 至尊版在全新小米澎湃 OS 4 加持下日常使用流畅稳定，性能表现也能胜任主流游戏畅玩，体验稳、能效好。甚至在部分三方媒体的测试数据中，一些游戏有着不输当代旗舰平台第" data-title="小米 REDMI 回应 K100 选用骁龙 8 至尊版：的确非最新平台，但三方测试部分游戏表现不输“8EE6”" data-date="10-30 15:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:43</span>
          <span class="news-item-title">小米 REDMI 回应 K100 选用骁龙 8 至尊版：的确非最新平台，但三方测试部分游戏表现不输“8EE6”</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，小米 REDMI 红米手机官方微博今日发布了“K100 答网友问”专栏文章，针对 K100 为什么用骁龙 8 …</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506686.html" target="_blank" rel="noopener" data-cat="keji" data-summary="解析一切" data-title="RSI立大功！国产开源登顶全球第一，1.3B OXR重塑OCR" data-date="10-30 13:52" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-30 13:52</span>
          <span class="news-item-title">RSI立大功！国产开源登顶全球第一，1.3B OXR重塑OCR</span>
          <span class="news-value-point">💡 解析一切</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506674.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Claude新模型曝光：新Fable，新Opus…" data-title="Claude新模型曝光：新Fable，新Opus…" data-date="10-30 13:50" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-30 13:50</span>
          <span class="news-item-title">Claude新模型曝光：新Fable，新Opus…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506662.html" target="_blank" rel="noopener" data-cat="keji" data-summary="让机器人成为彼此的“老师”" data-title="从学习人类到学习机器人同伴，清华大学联合无问芯穹、智元提出具身智能规模化落地新路径" data-date="10-30 11:48" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-30 11:48</span>
          <span class="news-item-title">从学习人类到学习机器人同伴，清华大学联合无问芯穹、智元提出具身智能规模化落地新路径</span>
          <span class="news-value-point">💡 让机器人成为彼此的“老师”</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/you-dont-need-to-believe-in-a-god-to-get-a-religious-exemption-from-using-ai-at-work/" target="_blank" rel="noopener" data-cat="keji" data-summary="肯塔基大学管理员大卫·杜尔曼（ David Durman ）最近获得了在工作场所使用人工智能的宗教豁免。" data-title="You don’t need to believe in a god to get a religious exemption from using AI at work" data-date="10-30 09:20" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 09:20</span>
          <span class="news-item-title">你不需要相信上帝就能获得在工作中使用人工智能的宗教豁免</span>
          <span class="news-item-title-en">You don’t need to believe in a god to get a religious exemption from using AI at work</span>
          <span class="news-value-point">💡 肯塔基大学管理员大卫·杜尔曼（ David Durman ）最近获得了在工作场所使用人工智能的宗教豁免</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506569.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Momenta世界模型上车" data-title="买车送终身AI？智己LS8纯电版25万起！全系线控底盘宁德时代标配" data-date="10-30 08:19" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-30 08:19</span>
          <span class="news-item-title">买车送终身AI？智己LS8纯电版25万起！全系线控底盘宁德时代标配</span>
          <span class="news-value-point">💡 Momenta世界模型上车</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/aws-will-be-a-1t-business-jassy-says-but-first-it-will-spend-big/" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊希望成为人工智能云计算之王，并成为首个营收达1万$的业务。但其首席执行官周四表示，要做到这一点，它将不得不继续其资本支出狂潮。" data-title="AWS will be a $1T business, Jassy says — but first, it will spend big" data-date="10-30 07:42" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 07:42</span>
          <span class="news-item-title">Jassy说， AWS将是一个$ 1T的业务—但首先，它将花费大量</span>
          <span class="news-item-title-en">AWS will be a $1T business, Jassy says — but first, it will spend big</span>
          <span class="news-value-point">💡 亚马逊希望成为人工智能云计算之王，并成为首个营收达1万$的业务</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022911/intel-wildcat-lake-sold-out-ram-shortage" target="_blank" rel="noopener" data-cat="keji" data-summary="在英特尔最新的财报电话会议上，首席执行官Lip-Bu Tan表示，对其以预算为重点的Wildcat Lake芯片的需求“超过了供应。“根据首席财务官David Zinsner的说法，这些芯片现已售罄。Zinsner表示，英特尔“看到了Wi的显着增长，" data-title="Intel says it’s selling every affordable laptop chip it can make" data-date="10-30 07:42" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 07:42</span>
          <span class="news-item-title">英特尔表示，它正在销售它可以制造的每个价格合理的笔记本电脑芯片</span>
          <span class="news-item-title-en">Intel says it’s selling every affordable laptop chip it can make</span>
          <span class="news-value-point">💡 在英特尔最新的财报电话会议上，首席执行官Lip-Bu Tan表示，对其以预算为重点的Wildcat Lake芯片的需求“超过了供应</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022848/reddit-ceo-google-ai-mode-traffic" target="_blank" rel="noopener" data-cat="keji" data-summary="Reddit首席执行官史蒂夫·霍夫曼（ Steve Huffman ）在今天的财报电话会议上表示，谷歌的人工智能搜索模式无助于该平台的流量，与其他网站和发布商面临的问题相呼应。作为2026年第三季度收益的一部分， Reddit透露，" data-title="Reddit’s CEO says Google’s AI Mode ‘does not drive traffic’" data-date="10-30 06:19" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 06:19</span>
          <span class="news-item-title">Reddit首席执行官表示，谷歌的AI模式“不会带来流量”</span>
          <span class="news-item-title-en">Reddit’s CEO says Google’s AI Mode ‘does not drive traffic’</span>
          <span class="news-value-point">💡 Reddit首席执行官史蒂夫·霍夫曼（ Steve Huffman ）在今天的财报电话会议上表示，谷歌的人工智能搜索模式无助于该平台的流量，与其…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-confirms-nova-lake-will-use-advanced-18a-p-node-more-details-at-ces-company-says-its-taking-panther-lake-capacity-offline-to-build-more-granite-rapids-data-center-cpus" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔首席执行官Lip-Bu Tan在公司2026年第三季度财报电话会议上证实，英特尔的下一代Nova Lake台式机处理器将成为首款使用英特尔增强型18A-P节点的客户端产品。" data-title="Intel confirms Nova Lake CPUs will use advanced 18A-P node, more details at CES — company says it&#39;s taking Panther Lake capacity offline to build more Granite Rapids data center CPUs" data-date="10-30 05:55" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-30 05:55</span>
          <span class="news-item-title">英特尔确认Nova Lake CPU将使用先进的18A-P节点， CES上有更多细节—该公司表示将使Panther Lake容量离线，以构建更多的Granite Rapids数据中心CPU</span>
          <span class="news-item-title-en">Intel confirms Nova Lake CPUs will use advanced 18A-P node, more details at CES — company says it's taking Panther Lake capacity offline to build more Granite Rapids data center CPUs</span>
          <span class="news-value-point">💡 英特尔首席执行官Lip-Bu Tan在公司2026年第三季度财报电话会议上证实，英特尔的下一代Nova Lake台式机处理器将成为首款使用英特尔…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/as-search-traffic-dries-up-reddit-announces-its-shifting-to-a-logged-in-experience/" target="_blank" rel="noopener" data-cat="keji" data-summary="随着人工智能改变人们在网上查找信息的方式， Reddit正在重新思考其开放网络根源，以保护其受众和业务。" data-title="As search traffic dries up, Reddit announces it’s shifting to a logged" data-date="10-30 04:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 04:08</span>
          <span class="news-item-title">随着搜索流量的枯竭， Reddit宣布它将转向</span>
          <span class="news-item-title-en">As search traffic dries up, Reddit announces it’s shifting to a logged</span>
          <span class="news-value-point">💡 随着人工智能改变人们在网上查找信息的方式， Reddit正在重新思考其开放网络根源，以保护其受众和业务</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/openai-backed-thrive-holdings-acquires-adt/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI支持的Thrive Holdings将以153亿美元的价格收购ADT ，并计划将AI引入家庭安全业务。" data-title="OpenAI-backed Thrive Holdings acquires ADT" data-date="10-30 03:56" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 03:56</span>
          <span class="news-item-title">OpenAI支持的Thrive Holdings收购ADT</span>
          <span class="news-item-title-en">OpenAI-backed Thrive Holdings acquires ADT</span>
          <span class="news-value-point">💡 OpenAI支持的Thrive Holdings将以153亿美元的价格收购ADT ，并计划将AI引入家庭安全业务</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqy0r31kwne0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么文森特·康帕尼（ Vincent Kompany ）的健康恐慌提醒我们，管理层会造成身心损失" data-title="Why managers must put their own fitness first" data-date="10-30 15:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 15:41</span>
          <span class="news-item-title">为什么经理必须把自己的健身放在第一位</span>
          <span class="news-item-title-en">Why managers must put their own fitness first</span>
          <span class="news-value-point">💡 英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么文森特·康帕尼（ Vincent Kompany ）的健康恐慌提醒我…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjn5v3pl0159o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联的挣扎比以往任何时候都更加深刻-尤其是前球员。" data-title="How talking about Man Utd&#39;s cycle of doom became an industry" data-date="10-30 14:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 14:14</span>
          <span class="news-item-title">谈论曼联的厄运循环如何成为一个行业</span>
          <span class="news-item-title-en">How talking about Man Utd's cycle of doom became an industry</span>
          <span class="news-value-point">💡 曼联的挣扎比以往任何时候都更加深刻-尤其是前球员</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/30/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布鲁诺·费尔南德斯（ Bruno Fernandes ）欠曼联一场演出，马蒂斯·泰尔（ Mathys Tel ）已抵达马刺队，利物浦正在改善英超联赛最佳射手迈克尔·卡里克（ Michael Carrick ）和布鲁诺·费尔南德斯（ Bruno Fernandes ）本周举行费尔南德斯是一个未使用的替代品" data-title="Premier League: 10 things to look out for this weekend" data-date="10-30 08:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 08:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 布鲁诺·费尔南德斯（ Bruno Fernandes ）欠曼联一场演出，马蒂斯·泰尔（ Mathys Tel ）已抵达马刺队，利物浦正在改善英超…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq1m4j79x50jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）以他对本周末英超联赛赛事的预测，扮演了办公室糟糕的一天明星约翰·汉纳（ John Hannah ） ，以及BBC读者和人工智能。" data-title="Sutton&#39;s predictions v Bad Day At The Office star John Hannah" data-date="10-30 03:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 03:55</span>
          <span class="news-item-title">Sutton的预测v办公室糟糕的一天明星John Hannah</span>
          <span class="news-item-title-en">Sutton's predictions v Bad Day At The Office star John Hannah</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）以他对本周末英超联赛赛事的预测，扮演了办公室糟糕的一天明星约翰·汉纳（ Jo…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Arteta sweating on fitness of duo after Dowman appeal rejected" data-title="Arsenal latest: Arteta sweating on fitness of duo after Dowman appeal rejected" data-date="10-30 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 02:00</span>
          <span class="news-item-title">阿森纳最新消息：在Dowman上诉被驳回后， Arteta在二人组的健身上出汗</span>
          <span class="news-item-title-en">Arsenal latest: Arteta sweating on fitness of duo after Dowman appeal rejected</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/29/chelseas-fine-finishing-has-them-flying-high-but-how-long-can-it-last" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="根据Opta的预期积分模型，尽管处于桌子的两端，但切尔西的表现比周六的对手曼联更糟糕迈克尔·卡里克（ Michael Carrick ）将在周六抵达斯坦福桥（ Stamford Bridge ） ，带着一个死人走路的空气" data-title="Chelsea’s fine finishing has them flying high – but how long can it last?" data-date="10-30 01:21" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-30 01:21</span>
          <span class="news-item-title">切尔西的精美装饰让他们飞得很高–但它能持续多久？</span>
          <span class="news-item-title-en">Chelsea’s fine finishing has them flying high – but how long can it last?</span>
          <span class="news-value-point">💡 根据Opta的预期积分模型，尽管处于桌子的两端，但切尔西的表现比周六的对手曼联更糟糕迈克尔·卡里克（ Michael Carrick ）将在周六…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605317/tottenham-vs-crystal-palace-have-spurs-genuinely-turned-a-corner-in-the-premier-league-under-roberto-de-zerbi" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="到周六结束时，托特纳姆热刺上次在反弹中赢得三场英超比赛已经有616天了。自从上次取得这一壮举以来，已经有三位不同的经理人来来去去，没有人能够将马刺队带到一个连胜的早晨" data-title="It&#39;s been 616 days: Can Spurs finally win three in a row?" data-date="10-29 23:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 23:30</span>
          <span class="news-item-title">已经616天了：马刺队终于可以连续赢得三场比赛吗？</span>
          <span class="news-item-title-en">It's been 616 days: Can Spurs finally win three in a row?</span>
          <span class="news-value-point">💡 到周六结束时，托特纳姆热刺上次在反弹中赢得三场英超比赛已经有616天了</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605389/arsenals-kai-havertz-in-goal-drought-so-should-mikel-arteta-keep-faith-in-him-ahead-of-viktor-gyokeres-against-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal striker dilemma: Should Arteta keep faith in Havertz?" data-title="Arsenal striker dilemma: Should Arteta keep faith in Havertz?" data-date="10-29 23:13" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 23:13</span>
          <span class="news-item-title">阿森纳前锋困境： Arteta是否应该对Havertz保持信心？</span>
          <span class="news-item-title-en">Arsenal striker dilemma: Should Arteta keep faith in Havertz?</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605382/max-dowman-arsenals-appeal-against-teenagers-red-card-in-fleetwood-town-defeat-rejected" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉。" data-title="Arsenal fail with appeal against Dowman&#39;s red card" data-date="10-29 22:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:50</span>
          <span class="news-item-title">阿森纳对道曼的红牌上诉失败</span>
          <span class="news-item-title-en">Arsenal fail with appeal against Dowman's red card</span>
          <span class="news-value-point">💡 阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13605382/max-dowman-arsenals-appeal-against-teenagers-red-card-in-fleetwood-town-defeat-rejected" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉。" data-title="Arsenal fail with appeal against Dowman&#39;s red card" data-date="10-29 22:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:50</span>
          <span class="news-item-title">阿森纳对道曼的红牌上诉失败</span>
          <span class="news-item-title-en">Arsenal fail with appeal against Dowman's red card</span>
          <span class="news-value-point">💡 阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckz7x8z1e9y9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克（ Michael Carrick ）确认布鲁诺·费尔南德斯（ Bruno Fernandes ）将继续担任队长，并在周六前往切尔西之前谈论自己的未来。" data-title="&#39;Fully committed&#39; Fernandes to remain Man Utd captain" data-date="10-29 22:31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 22:31</span>
          <span class="news-item-title">“全力以赴”费尔南德斯继续担任曼联队长</span>
          <span class="news-item-title-en">'Fully committed' Fernandes to remain Man Utd captain</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克（ Michael Carrick ）确认布鲁诺·费尔南德斯（ Bruno Fernandes ）将继续担任队长，并在周…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">卡里克准备与费尔南德斯一起“前进”</span>
          <span class="news-item-title-en">Carrick ready to 'move forward' with Fernandes as captain</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">卡里克准备与费尔南德斯一起“前进”</span>
          <span class="news-item-title-en">Carrick ready to 'move forward' with Fernandes as captain</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cv2d6ze63gk2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="背靠背降级到英格兰足球第三梯队变得越来越普遍，本赛季伯恩利可能会在卢顿镇和莱斯特之后成为帽子戏法。" data-title="Is the double drop from the Premier League becoming more common?" data-date="10-29 21:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 21:19</span>
          <span class="news-item-title">英超联赛的双降是否变得越来越普遍？</span>
          <span class="news-item-title-en">Is the double drop from the Premier League becoming more common?</span>
          <span class="news-value-point">💡 背靠背降级到英格兰足球第三梯队变得越来越普遍，本赛季伯恩利可能会在卢顿镇和莱斯特之后成为帽子戏法</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604412/premier-league-predictions-jones-knows-best-bets-liverpool-vs-arsenal-crystal-palace-vs-tottenham-and-much-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，为英超联赛忙碌的周末提供了他的分析和博彩洞" data-title="PL Predictions: Man Utd to deliver a reaction for Carrick at Chelsea" data-date="10-29 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 21:00</span>
          <span class="news-item-title">PL预测：曼联将在切尔西为卡里克做出反应</span>
          <span class="news-item-title-en">PL Predictions: Man Utd to deliver a reaction for Carrick at Chelsea</span>
          <span class="news-value-point">💡 我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，为英超联赛忙碌的周末提供了他的分析和…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/020/148.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 30 日消息，熊猫现已在京东上架“F32U4”31.5 英寸显示器，该机主打 4K 120Hz，定价为 1249 元，部分地区国补后低至 1124 元。京东熊猫“F32U4”显示器 1249 元点此访问该机配备一块 3840x2160 分辨率 120Hz 面板，对比度 1000:1，显示器响应速度 1ms，支持 8-Bit 色彩，覆盖 138% sRGB 色域容积和 102% DCI-P3 色域容积。该机支架支持升降 / 倾斜 / 旋转，显示器本体内置双扬声器，支持 VESA 100x100mm 壁挂，提供 2 个 HDMI 2.0、2 个 DP 1.4、1 个 3.5mm 音频接口。IT之家附显示器参数：京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3" data-title="熊猫推出“F32U4”31.5 英寸显示器：4K 120Hz、双扬声器，1249 元" data-date="10-30 15:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:39</span>
          <span class="news-item-title">熊猫推出“F32U4”31.5 英寸显示器：4K 120Hz、双扬声器，1249 元</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，熊猫现已在京东上架“F32U4”31.5 英寸显示器，该机主打 4K 120Hz，定价为 1249 元，部分地…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723362.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者今天了解到，强制性国家标准《儿童呵护用品 通用安全要求》，以及配套推荐性国家标准《儿童呵护用品安全 儿童推车》《儿童呵护用品安全 婴儿学步车》《儿童呵护用品安全 婴幼儿安全护栏》将自2026年11月1日起实施。该系列标准从通用安全和特定专项要求两个维度，为儿童呵护用品设计、生产、检验、监管提供统一技术支撑，规范市场产品质量，保障婴幼儿日常活动安全。" data-title="事关婴幼儿日常安全 这4项强制性国家标准11月起实施" data-date="10-30 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 15:35</span>
          <span class="news-item-title">事关婴幼儿日常安全 这4项强制性国家标准11月起实施</span>
          <span class="news-value-point">💡 记者今天了解到，强制性国家标准《儿童呵护用品 通用安全要求》，以及配套推荐性国家标准《儿童呵护用品安全 儿童推车》《儿童呵护用品安全 婴儿学步车…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/144.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 30 日消息，ID-COOLING（酷凛）近日在其官网上线了 SE-206-XT SLK 处理器风冷散热器。该型号三维 123×110×156 (mm)，总质量 870g。SE-206-XT SLK 采用双塔结构，配备 6 根 6mm 热管，底部为 3+3 并管直触，同时热管倾斜以避让内存模组。其配备 2 颗 HDB 液压轴承风扇。前置的是 15mm 薄扇 AM-120 SLIM V2，最大转速 2500 RPM、最大风量 59.6 CFM、最大静压 2.7 mmAq、最大噪声 31.0 dB(A)；中置标准厚度的 XF-125，最大转速 2500 RPM、最大风量 75.17 CFM、最大静压 3.19 mmAq，最大噪声 35.89 dB(A)。" data-title="ID-COOLING 推出双塔风冷 SE-206-XT SLK：6 热管直触，一厚一薄风扇" data-date="10-30 15:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:33</span>
          <span class="news-item-title">ID-COOLING 推出双塔风冷 SE-206-XT SLK：6 热管直触，一厚一薄风扇</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，ID-COOLING（酷凛）近日在其官网上线了 SE-206-XT SLK 处理器风冷散热器</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/143.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 30 日消息，博主 @数码闲聊站 刚刚发文透露，某厂 6.35 英寸阔直板产品线，明年首款新机属于高端旗舰线，后续考虑下放轻薄拍照机。根据评论区讨论及博主的暗示符号来看，该厂指代的是 OPPO。据IT之家此前报道，该博主还曾透露，OPPO 阔直板手机是标准 16:9 比例，工程机测试天玑旗舰芯、3D 超声波指纹，屏幕分辨率为 2560*1440p，采用 LIPO 极窄四等边设计，目测边框 1mm±，看标准视频会铺满整块屏幕，机身宽度大概是 81mm。他表示，安卓阵营的阔直板手机，O（预计指 OPPO）大概率第一个上，h（预计指荣耀）第二个上。他表示，剩下几家进度较缓慢，目前排期是 2027 年底至 2028 年上半年。目前立项阶段有影像阔直板手机、中端阔直板手机、性能阔直" data-title="曝 OPPO 旗下 6.35 英寸阔直板明年首款新机属高端旗舰线，后续考虑下放轻薄拍照机" data-date="10-30 15:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:33</span>
          <span class="news-item-title">曝 OPPO 旗下 6.35 英寸阔直板明年首款新机属高端旗舰线，后续考虑下放轻薄拍照机</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，博主 @数码闲聊站 刚刚发文透露，某厂 6.35 英寸阔直板产品线，明年首款新机属于高端旗舰线，后续考虑下放轻…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/142.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 30 日消息，JBL 旗下 Wave Beam 3 现已在京东发售，该产品配备 8mm 动圈，定价为 443 元，部分地区国补后低至 398 元。京东 JBLWave Beam3443 元直达链接该耳机本体具备 IP54 级别的防水防尘，提供熔岩黑、珍珠白、清新绿、活力橙、青黛紫和晴空蓝六种配色。机身采用圆润磨砂质感处理，充电盒配有便携挂绳孔设计，整体重量为 39.1g。该耳机内置 8mm 定制调校动圈单元，支持主动降噪功能与智能环境声切换，配备 4Mic 麦克风系统。耳机搭载了蓝牙 6.0 技术，支持 LE Audio 及 Auracast™ 广播音频接收，并可同时连接两台设备。该耳机搭配充电盒的综合续航时间可达 40 小时，设备支持快充，充电 10 分钟即可使用 3" data-title="JBL Wave Beam 3 耳机发售：8mm 动圈、40 小时续航，443 元" data-date="10-30 15:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 15:28</span>
          <span class="news-item-title">JBL Wave Beam 3 耳机发售：8mm 动圈、40 小时续航，443 元</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，JBL 旗下 Wave Beam 3 现已在京东发售，该产品配备 8mm 动圈，定价为 443 元，部分地区国…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13605662/pan-pacific-open-elena-rybakina-withdraws-from-pan-pacific-open-with-injury-just-one-day-after-securing-year-end-no-1-ranking" target="_blank" rel="noopener" data-cat="zonghe" data-summary="世界排名第一的埃琳娜·雷巴基纳（ Elena Rybakina ）在泛太平洋公开赛上撤回了对阵莱拉·费尔南德斯（ Leylah Fernandez ）的伤病，在四分之一决赛阶段退" data-title="Rybakina withdraws from Pan Pacific Open with injury" data-date="10-30 15:10" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 15:10</span>
          <span class="news-item-title">Rybakina因伤退出泛太平洋公开赛</span>
          <span class="news-item-title-en">Rybakina withdraws from Pan Pacific Open with injury</span>
          <span class="news-value-point">💡 世界排名第一的埃琳娜·雷巴基纳（ Elena Rybakina ）在泛太平洋公开赛上撤回了对阵莱拉·费尔南德斯（ Leylah Fernande…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13605629/mexico-open-karl-vilips-shoots-62-to-take-the-first-round-lead-with-marco-penge-two-shots-back" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡尔·维利普斯（ Karl Vilips ）周四在墨西哥公开赛上使用了两个长小鸟连胜，取得了第一轮领先，这是该国连续两场美巡赛赛事中的第一场。" data-title="Vilips takes first-round lead at Mexico Open" data-date="10-30 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 15:00</span>
          <span class="news-item-title">维利普斯在墨西哥公开赛首轮比赛中领先</span>
          <span class="news-item-title-en">Vilips takes first-round lead at Mexico Open</span>
          <span class="news-value-point">💡 卡尔·维利普斯（ Karl Vilips ）周四在墨西哥公开赛上使用了两个长小鸟连胜，取得了第一轮领先，这是该国连续两场美巡赛赛事中的第一场</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-league/live-blog/12040/13599564/rugby-league-world-cup-2026-reports-news-scores-fixtures-from-across-the-mens-womens-and-wheelchair-tournaments" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Hawkins scores 11 tries as England hammer Wales in World Cup opener" data-title="Hawkins scores 11 tries as England hammer Wales in World Cup opener" data-date="10-30 14:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 14:40</span>
          <span class="news-item-title">霍金斯在世界杯揭幕战中作为英格兰锤击威尔士得分11次</span>
          <span class="news-item-title-en">Hawkins scores 11 tries as England hammer Wales in World Cup opener</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723312.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南昌10月30日电 题：江西南昌：碧水之畔，何以藏着豫章文化记忆？" data-title="江西南昌：碧水之畔，何以藏着豫章文化记忆？" data-date="10-30 14:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 14:37</span>
          <span class="news-item-title">江西南昌：碧水之畔，何以藏着豫章文化记忆？</span>
          <span class="news-value-point">💡 中新网南昌10月30日电 题：江西南昌：碧水之畔，何以藏着豫章文化记忆</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13605642/carolina-panthers-19-27-green-bay-packers-jordan-love-throws-three-touchdown-passes-in-vital-win" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乔丹·洛夫投掷了三次达阵传球，乔什·雅各布斯得分两次，绿湾包装工队经历了三次失误，卡罗莱纳黑豹队在兰博球场以27胜19负的复出尝试。" data-title="Love leads Packers past Panthers in vital win" data-date="10-30 14:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 14:30</span>
          <span class="news-item-title">爱带领包装工队走过黑豹队取得重大胜利</span>
          <span class="news-item-title-en">Love leads Packers past Panthers in vital win</span>
          <span class="news-value-point">💡 乔丹·洛夫投掷了三次达阵传球，乔什·雅各布斯得分两次，绿湾包装工队经历了三次失误，卡罗莱纳黑豹队在兰博球场以27胜19负的复出尝试</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723296.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网齐齐哈尔10月30日电 题：松嫩平原玉米归仓记：秋粮入囤 种养循环" data-title="（乡村行·看振兴）松嫩平原玉米归仓记：秋粮入囤 种养循环" data-date="10-30 14:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 14:27</span>
          <span class="news-item-title">（乡村行·看振兴）松嫩平原玉米归仓记：秋粮入囤 种养循环</span>
          <span class="news-value-point">💡 中新网齐齐哈尔10月30日电 题：松嫩平原玉米归仓记：秋粮入囤 种养循环</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723297.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州10月30日电 (记者 殷春永)外地访客以前到广东阳江，提到“万亩红树林”就会想到阳西县程村镇。如今，这里却“蚝”出了名堂。" data-title="当一个传统蚝村把“蚝”从产品变成场景" data-date="10-30 14:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 14:21</span>
          <span class="news-item-title">当一个传统蚝村把“蚝”从产品变成场景</span>
          <span class="news-value-point">💡 中新网广州10月30日电 (记者 殷春永)外地访客以前到广东阳江，提到“万亩红树林”就会想到阳西县程村镇</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723282.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月30日电 据长沙民政职业技术学院医学院网站消息，10月29日，长沙民政职业技术学院医学院发布情况通报：" data-title="一新生摆拍大体老师头骨标本发朋友圈 校方通报" data-date="10-30 14:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 14:19</span>
          <span class="news-item-title">一新生摆拍大体老师头骨标本发朋友圈 校方通报</span>
          <span class="news-value-point">💡 中新网10月30日电 据长沙民政职业技术学院医学院网站消息，10月29日，长沙民政职业技术学院医学院发布情况通报：</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-30/10723300.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网邯郸10月30日电 题：从古人“朋友圈”到今人“生活圈”：磁州窑凭啥“接地气”千年？" data-title="（乡村行·看振兴）从古人“朋友圈”到今人“生活圈”：磁州窑凭啥“接地气”千年？" data-date="10-30 14:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-30 14:19</span>
          <span class="news-item-title">（乡村行·看振兴）从古人“朋友圈”到今人“生活圈”：磁州窑凭啥“接地气”千年？</span>
          <span class="news-value-point">💡 中新网邯郸10月30日电 题：从古人“朋友圈”到今人“生活圈”：磁州窑凭啥“接地气”千年</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cmy932qe3wx3o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这位澳洲运动员承认责任，但表示舆论反弹令她“创伤”。" data-title="“我不希望它成为我的身份”：Hyrox失禁选手复出比赛前接受BBC专访" data-date="10-30 13:40" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 13:40</span>
          <span class="news-item-title">“我不希望它成为我的身份”：Hyrox失禁选手复出比赛前接受BBC专访</span>
          <span class="news-value-point">💡 这位澳洲运动员承认责任，但表示舆论反弹令她“创伤”</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ck4g18ql0vj9o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="姆巴佩有关一名“中国领导人”的言论引发众怒，但网络审查令许多人仍不清楚事件究竟是怎么回事。" data-title="中国施压下姆巴佩道歉，但许多人仍不知道他究竟说了什么" data-date="10-30 08:23" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 08:23</span>
          <span class="news-item-title">中国施压下姆巴佩道歉，但许多人仍不知道他究竟说了什么</span>
          <span class="news-value-point">💡 姆巴佩有关一名“中国领导人”的言论引发众怒，但网络审查令许多人仍不清楚事件究竟是怎么回事</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-30 15:49（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
