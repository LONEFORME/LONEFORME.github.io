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
      <span>2026-10-30 02:34 抓取更新</span>
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
        <span class="channel-count">59</span>
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
        <span class="channel-count">14</span>
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
  <div class="ov-item"><span class="ov-num">59</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×14 · 天空体育×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/29/upshot/midterm-elections-senate-house-scenarios.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党人的期望正在达到顶峰，似乎有可能出现某种浪潮，但很大程度上取决于参议院的几场激烈竞选。" data-title="Four Scenarios for How the Midterms Could Go" data-date="10-30 01:48" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-30 01:48</span>
      </div>
      <h2 class="hero-featured-title">期中考试如何进行的四个场景</h2>
      <div class="hero-featured-title-en">Four Scenarios for How the Midterms Could Go</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/10/29/granola-crunches-up-a-dictation-feature-to-compete-with-wispr/" target="_blank" rel="noopener" data-cat="keji" data-summary="UNO REVERSE ！在Wispr向其听写应用程序添加会议笔记后， Granola正在向其会议笔记员添加听写。语音人工智能战争变得越来越有趣。" data-title="Granola crunches up a dictation feature to compete with Wispr" data-date="10-30 01:54" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Granola crunches up a dictation feature to compete with Wispr</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Arteta sweating on fitness of duo after Dowman appeal rejected" data-title="Arsenal latest: Arteta sweating on fitness of duo after Dowman appeal rejected" data-date="10-30 02:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Arsenal latest: Arteta sweating on fitness of duo after Dowman appeal rejected</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1022440/ikea-varmblixt-smart-lamp-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凭借其俏皮的设计、多功能性和相对实惠的价格，宜家Varmblixt在4月份测试时迅速成为我的同事Jennifer Pattison Tuohy最喜欢的智能灯产品之一。现在，甜甜圈形状的灯在SAL上" data-title="Ikea’s colorful donut-shaped smart lamp is $20 off" data-date="10-30 02:18" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Ikea’s colorful donut-shaped smart lamp is $20 off</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/29/upshot/midterm-elections-senate-house-scenarios.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党人的期望正在达到顶峰，似乎有可能出现某种浪潮，但很大程度上取决于参议院的几场激烈竞选。" data-title="Four Scenarios for How the Midterms Could Go" data-date="10-30 01:48" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 01:48</span>
          <span class="news-item-title">期中考试如何进行的四个场景</span>
          <span class="news-item-title-en">Four Scenarios for How the Midterms Could Go</span>
          <span class="news-value-point">💡 民主党人的期望正在达到顶峰，似乎有可能出现某种浪潮，但很大程度上取决于参议院的几场激烈竞选</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx5ynjr6q6gzo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位参议员离开巴西后，被拍到在美国走下飞机。他在巴西因涉嫌洗钱而接受调查。" data-title="巴西前总统博索纳罗之子败给卢拉后，为何飞往美国？" data-date="10-30 00:19" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-30 00:19</span>
          <span class="news-item-title">巴西前总统博索纳罗之子败给卢拉后，为何飞往美国？</span>
          <span class="news-value-point">💡 这位参议员离开巴西后，被拍到在美国走下飞机</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723080.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网南昌10月29日电 (记者 李韵涵)29日，江西省高级人民法院召开新闻发布会通报江西法院司法救助工作情况。记者从会上了解到，2023年以来，江西法院共办理司法救助案件11319件。" data-title="2023年以来江西法院共办理司法救助案件1.1万余件" data-date="10-29 23:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:51</span>
          <span class="news-item-title">2023年以来江西法院共办理司法救助案件1.1万余件</span>
          <span class="news-value-point">💡 中新网南昌10月29日电 (记者 李韵涵)29日，江西省高级人民法院召开新闻发布会通报江西法院司法救助工作情况</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723076.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月29日电 (记者 阮煜琳)中国自然资源部29日消息，当日，在亚美尼亚埃里温举办的《生物多样性公约》第十七次缔约方大会(COP17)“恢复日”活动上，联合国环境规划署正式宣布，因中国在海洋生态保护修复方面取得的突出成效，“中国蓝色海湾整治行动”获评2026年联合国“世界生态恢复旗舰项目”。" data-title="“中国蓝色海湾整治行动”获评2026年联合国“世界生态恢复旗舰项目”" data-date="10-29 23:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:43</span>
          <span class="news-item-title">“中国蓝色海湾整治行动”获评2026年联合国“世界生态恢复旗舰项目”</span>
          <span class="news-value-point">💡 中新社北京10月29日电 (记者 阮煜琳)中国自然资源部29日消息，当日，在亚美尼亚埃里温举办的《生物多样性公约》第十七次缔约方大会(COP17…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723069.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网天津10月29日电 (记者 江莹)28日，由天津市委市级机关工委、市妇联联合主办的2026年天津市巾帼宣讲员风采展示暨示范宣讲活动举行，活动以“巾帼津声理润津沽 凝心筑梦奋进新程”为主题，充分展现新时代天津女性担当风采。" data-title="天津开展巾帼宣讲员风采展示活动 讲好巾帼建功奋斗故事" data-date="10-29 23:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:34</span>
          <span class="news-item-title">天津开展巾帼宣讲员风采展示活动 讲好巾帼建功奋斗故事</span>
          <span class="news-value-point">💡 中新网天津10月29日电 (记者 江莹)28日，由天津市委市级机关工委、市妇联联合主办的2026年天津市巾帼宣讲员风采展示暨示范宣讲活动举行，活…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723067.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月29日电 10月29日，中共中央政治局委员、外交部长王毅在北京同冰岛外长贡纳尔斯多蒂尔举行会谈。" data-title="王毅同冰岛外长贡纳尔斯多蒂尔会谈" data-date="10-29 23:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:33</span>
          <span class="news-item-title">王毅同冰岛外长贡纳尔斯多蒂尔会谈</span>
          <span class="news-value-point">💡 中新社北京10月29日电 10月29日，中共中央政治局委员、外交部长王毅在北京同冰岛外长贡纳尔斯多蒂尔举行会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723066.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆10月29日电 (记者 钟旖)重庆“益企向善·社区慈善联合行动”推进会暨2026年社区阳光基金推进会29日在当地召开。" data-title="重庆已有1164支社区阳光基金 基层慈善网络加快形成" data-date="10-29 23:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:23</span>
          <span class="news-item-title">重庆已有1164支社区阳光基金 基层慈善网络加快形成</span>
          <span class="news-value-point">💡 中新网重庆10月29日电 (记者 钟旖)重庆“益企向善·社区慈善联合行动”推进会暨2026年社区阳光基金推进会29日在当地召开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723065.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西宁10月29日电 (记者 潘雨洁)从纪念馆里的“一口铜锅”到校园内的“一片青砖”，29日，青海省果洛州班玛县亚尔堂乡王柔村党支部书记门卓、海东市循化县西路红军小学校长史可英讲述了红军精神在高原落地生根、代代传承的故事。" data-title="青海：“一口铜锅、一片青砖”讲述九十载长征精神的高原传承" data-date="10-29 23:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:23</span>
          <span class="news-item-title">青海：“一口铜锅、一片青砖”讲述九十载长征精神的高原传承</span>
          <span class="news-value-point">💡 中新网西宁10月29日电 (记者 潘雨洁)从纪念馆里的“一口铜锅”到校园内的“一片青砖”，29日，青海省果洛州班玛县亚尔堂乡王柔村党支部书记门卓…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10723054.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 据伊朗伊斯兰共和国通讯社报道，伊朗伊斯兰革命卫队29日称，他们在霍尔木兹海峡以西捕获了一架美国间谍无人机。" data-title="伊朗称捕获一架美国间谍无人机" data-date="10-29 23:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:14</span>
          <span class="news-item-title">伊朗称捕获一架美国间谍无人机</span>
          <span class="news-value-point">💡 中新网北京10月29日电 据伊朗伊斯兰共和国通讯社报道，伊朗伊斯兰革命卫队29日称，他们在霍尔木兹海峡以西捕获了一架美国间谍无人机</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/video/us/elections/100000011223984/the-red-states-that-could-decide-the-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党人需要翻转四个共和党参议院席位才能重新获得多数席位，但他们的一些目标在2024年特朗普总统以两位数获胜的州。我们的选举数据记者埃文·雷诺兹（ Evan Reynolds ）解释了这可能有多么困难。" data-title="The Red States That Could Decide the Senate" data-date="10-29 22:58" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 22:58</span>
          <span class="news-item-title">可以决定参议院的红州</span>
          <span class="news-item-title-en">The Red States That Could Decide the Senate</span>
          <span class="news-value-point">💡 民主党人需要翻转四个共和党参议院席位才能重新获得多数席位，但他们的一些目标在2024年特朗普总统以两位数获胜的州</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10723035.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月29日电 (记者 金旭)当地时间29日，韩国负责调查紧急戒严事件的特别检察组以涉嫌带头发动内乱为由，请求二审法庭判处韩国前总统尹锡悦死刑。" data-title="韩国前总统尹锡悦涉“内乱案”二审被求死刑" data-date="10-29 22:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 22:47</span>
          <span class="news-item-title">韩国前总统尹锡悦涉“内乱案”二审被求死刑</span>
          <span class="news-value-point">💡 中新社首尔10月29日电 (记者 金旭)当地时间29日，韩国负责调查紧急戒严事件的特别检察组以涉嫌带头发动内乱为由，请求二审法庭判处韩国前总统尹…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722989.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 据美联社报道，保加利亚海事部门29日表示，一艘悬挂利比里亚国旗的船只在保加利亚黑海沿岸被无人机击中后沉没。" data-title="一艘商船在保加利亚黑海沿岸被无人机击中后沉没" data-date="10-29 21:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:16</span>
          <span class="news-item-title">一艘商船在保加利亚黑海沿岸被无人机击中后沉没</span>
          <span class="news-value-point">💡 中新网北京10月29日电 据美联社报道，保加利亚海事部门29日表示，一艘悬挂利比里亚国旗的船只在保加利亚黑海沿岸被无人机击中后沉没</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722936.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 综合消息：欧盟-加拿大峰会定于当地时间29日至30日在加拿大蒙特利尔举行。加拿大媒体称，双方预计30日发表的联合声明将删除给予加拿大欧盟“联席成员”身份的表述，改为呼吁建立“更紧密的联系”。" data-title="加媒称加拿大和欧盟联合声明将删去“联席成员”表述" data-date="10-29 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 20:15</span>
          <span class="news-item-title">加媒称加拿大和欧盟联合声明将删去“联席成员”表述</span>
          <span class="news-value-point">💡 中新网北京10月29日电 综合消息：欧盟-加拿大峰会定于当地时间29日至30日在加拿大蒙特利尔举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722963.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月29日电 据伊朗媒体报道，伊朗伊斯兰革命卫队当地时间29日发布声明称，在霍尔木兹海峡以西地区开展了一次进攻性电子战行动，成功控制一架美军间谍无人机，并使其安全降落。" data-title="伊朗伊斯兰革命卫队称捕获一架美军间谍无人机" data-date="10-29 20:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 20:13</span>
          <span class="news-item-title">伊朗伊斯兰革命卫队称捕获一架美军间谍无人机</span>
          <span class="news-value-point">💡 中新网10月29日电 据伊朗媒体报道，伊朗伊斯兰革命卫队当地时间29日发布声明称，在霍尔木兹海峡以西地区开展了一次进攻性电子战行动，成功控制一架…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722934.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间28日，以色列中央选举委员会公布了议会选举的初步计票结果。目前，以总理内塔尼亚胡领导的右翼阵营领先于前国防军总参谋长埃森科特领衔的反对派阵营，但双方均未达到议会多数席位。" data-title="以色列两大阵营均未获多数议席 不同组阁结果影响几何" data-date="10-29 19:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 19:44</span>
          <span class="news-item-title">以色列两大阵营均未获多数议席 不同组阁结果影响几何</span>
          <span class="news-value-point">💡 当地时间28日，以色列中央选举委员会公布了议会选举的初步计票结果</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/granola-crunches-up-a-dictation-feature-to-compete-with-wispr/" target="_blank" rel="noopener" data-cat="keji" data-summary="UNO REVERSE ！在Wispr向其听写应用程序添加会议笔记后， Granola正在向其会议笔记员添加听写。语音人工智能战争变得越来越有趣。" data-title="Granola crunches up a dictation feature to compete with Wispr" data-date="10-30 01:54" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 01:54</span>
          <span class="news-item-title">Granola推出听写功能，与Wispr展开竞争</span>
          <span class="news-item-title-en">Granola crunches up a dictation feature to compete with Wispr</span>
          <span class="news-value-point">💡 UNO REVERSE</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/" target="_blank" rel="noopener" data-cat="keji" data-summary="Mistral表示，其新模型可以让组织对其网络防御进行某种控制，而封闭模型无法做到这一点。" data-title="Mistral releases weights for its trillion-parameter AI model, targeting cybersecurity" data-date="10-30 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 01:00</span>
          <span class="news-item-title">Mistral发布针对网络安全的万亿参数AI模型的权重</span>
          <span class="news-item-title-en">Mistral releases weights for its trillion-parameter AI model, targeting cybersecurity</span>
          <span class="news-value-point">💡 Mistral表示，其新模型可以让组织对其网络防御进行某种控制，而封闭模型无法做到这一点</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/u-s-investigated-chinese-spy-plot-aimed-at-nvidia-ceo/" target="_blank" rel="noopener" data-cat="keji" data-summary="消息人士告诉《纽约时报》，一家被指控向中国非法出售英伟达芯片的新加坡人工智能云公司的高管也可能是中国间谍。" data-title="US investigated Chinese spy plot aimed at Nvidia CEO" data-date="10-30 00:42" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 00:42</span>
          <span class="news-item-title">美国调查了针对英伟达首席执行官的中国间谍阴谋</span>
          <span class="news-item-title-en">US investigated Chinese spy plot aimed at Nvidia CEO</span>
          <span class="news-value-point">💡 消息人士告诉《纽约时报》，一家被指控向中国非法出售英伟达芯片的新加坡人工智能云公司的高管也可能是中国间谍</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/ex-palantir-execs-launch-dream-with-17m-from-a16z-to-build-ai-world-models-for-construction/" target="_blank" rel="noopener" data-cat="keji" data-summary="DREAM以真实的物理和建筑标准为基础。正如法学硕士从文本中学习一样， Dream的世界模型是根据从美国各地的许可证档案中收集的超过1亿平方英尺的建筑数据进行培训的。" data-title="Ex-Palantir execs launch Dream with $17M from a16z to build AI world models for construction" data-date="10-30 00:21" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-30 00:21</span>
          <span class="news-item-title">Palantir前高管以a16z的1700万美元推出Dream ，用于构建建筑AI世界模型</span>
          <span class="news-item-title-en">Ex-Palantir execs launch Dream with $17M from a16z to build AI world models for construction</span>
          <span class="news-value-point">💡 DREAM以真实的物理和建筑标准为基础</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022023/microsoft-exit-offer-layoffs-notepad" target="_blank" rel="noopener" data-cat="keji" data-summary="对于任何密切关注微软首席执行官萨蒂亚·纳德拉（ Satya Nadella ）过去几年所说的话的人来说，本周似乎是人工智能即将从根本上改变微软员工规模的最明显迹象。微软现在是OFFE" data-title="Microsoft’s AI future has fewer jobs" data-date="10-30 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 00:00</span>
          <span class="news-item-title">微软的人工智能未来工作岗位减少</span>
          <span class="news-item-title-en">Microsoft’s AI future has fewer jobs</span>
          <span class="news-value-point">💡 对于任何密切关注微软首席执行官萨蒂亚·纳德拉（ Satya Nadella ）过去几年所说的话的人来说，本周似乎是人工智能即将从根本上改变微软员…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/796.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，《星闪 SLE3.0 技术标准演进蓝皮书》已在国际星闪联盟官网正式上线。蓝皮书中详细介绍了星闪 SLE 标准演进三阶段。IT之家从蓝皮书了解到，2025 年以来星闪 SLE 2.0 技术迈入技术成熟与商业落地双爆发阶段。芯片领域，卓胜微、恒玄、泰凌微、创耀、华为海思等厂商已发布 20+ 款芯片，支持高清音频、高精测距等星闪 SLE 2.0 核心功能。数字车钥匙领域，2025 年 3 月问界新 M9 上市，首批星闪数字钥匙实现量产上车；随后问界 M8、享界 S9 增程版、东风猛士 M817、广汽丰田铂智 7 等产品陆续搭载。2025 年全年搭载星闪数字钥匙车型总量达 80 余万台，覆盖 10 余家车企；后续还可以探索支持车内及车辆周边 IoT 设备组网管理，如" data-title="星闪 SLE 2.0 核心升级高清音频、高精测距功能，恒玄、华为海思等厂商发布 20+ 款芯片" data-date="10-29 23:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 23:45</span>
          <span class="news-item-title">星闪 SLE 2.0 核心升级高清音频、高精测距功能，恒玄、华为海思等厂商发布 20+ 款芯片</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，《星闪 SLE3.0 技术标准演进蓝皮书》已在国际星闪联盟官网正式上线</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ai-demand-triggers-massive-pcb-shortage-for-pc-makers-as-order-books-full-until-2030-lead-times-stretch-to-30-months-as-material-costs-surge-12x" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能行业继续吞噬曾经致力于为PC、智能设备和小工具制造商提供服务的制造资源。PCB行业不可避免地开始感受到它的影响。" data-title="AI demand triggers massive PCB shortage for PC makers as order books full until 2030 — lead times stretch to 30 months as material costs surge 12x" data-date="10-29 23:25" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 23:25</span>
          <span class="news-item-title">随着订单满载到2030年，人工智能需求引发了PC制造商的大规模PCB短缺—随着材料成本飙升12倍，交货时间延长至30个月</span>
          <span class="news-item-title-en">AI demand triggers massive PCB shortage for PC makers as order books full until 2030 — lead times stretch to 30 months as material costs surge 12x</span>
          <span class="news-value-point">💡 人工智能行业继续吞噬曾经致力于为PC、智能设备和小工具制造商提供服务的制造资源</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/791.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，《星闪 SLE3.0 技术标准演进蓝皮书》已在国际星闪联盟官网正式上线。据蓝皮书介绍，星闪 SLE 1.0 标准于 2022 年 11 月正式发布，SLE 1.0 芯片累计发货量 7000 万。模组：润和、汉枫、爱联、为思润华、亿佰特、问沧智能等模组厂商已发布超过 40 款基于星闪 SLE 1.0 的模组产品，可支持白色家电、小家电、照明、电工 IoT、传感器、运动健康、户外出行、家庭安防、照明、工业互联网等应用场景。终端产品：2023 年 9 月份华为发布首批支持星闪技术的商用终端产品，如 Mate 60 系列、MatePad Pro 13.2 英寸平板、华为第三代 M-Pencil 手写笔等，随后产业快速跟进，ATK、哈尔斯、雷柏、小豚当家、达尔优、北通" data-title="星闪 SLE 1.0 芯片累计发货量 7000 万，华为 2023 年实现首批商用终端产品落地" data-date="10-29 23:09" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 23:09</span>
          <span class="news-item-title">星闪 SLE 1.0 芯片累计发货量 7000 万，华为 2023 年实现首批商用终端产品落地</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，《星闪 SLE3.0 技术标准演进蓝皮书》已在国际星闪联盟官网正式上线</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1022193/nyt-cooking-app-ai-recipe-modification-tool" target="_blank" rel="noopener" data-cat="keji" data-summary="《纽约时报》正在为其烹饪应用程序测试一项新的人工智能功能，该功能可帮助用户修改食谱，并在用户中引发了一些戏剧性事件。上周五，《纽约时报》烹饪资深编辑Genevieve Ko宣布了该功能，可用于推荐" data-title="The NYT Cooking app is testing AI recipe modifications" data-date="10-29 22:39" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 22:39</span>
          <span class="news-item-title">纽约时报烹饪应用程序正在测试AI食谱修改</span>
          <span class="news-item-title-en">The NYT Cooking app is testing AI recipe modifications</span>
          <span class="news-value-point">💡 《纽约时报》正在为其烹饪应用程序测试一项新的人工智能功能，该功能可帮助用户修改食谱，并在用户中引发了一些戏剧性事件</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/wabi-the-ai-agent-that-builds-mini-apps-now-valued-at-1-25b-after-latest-round/" target="_blank" rel="noopener" data-cat="keji" data-summary="周四，人工智能应用程序Wabi现在将自己描述为“个人经纪人” ，并表示已以12.5亿美元的估值筹集了5500万美元。" data-title="Wabi, the AI agent that builds mini apps, now valued at $1.25B after latest round" data-date="10-29 22:35" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-29 22:35</span>
          <span class="news-item-title">构建迷你应用程序的人工智能代理Wabi ，经过最新一轮融资，现在估值为12.5亿美元$</span>
          <span class="news-item-title-en">Wabi, the AI agent that builds mini apps, now valued at $1.25B after latest round</span>
          <span class="news-value-point">💡 周四，人工智能应用程序Wabi现在将自己描述为“个人经纪人” ，并表示已以12.5亿美元的估值筹集了5500万美元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-geforce-rtx-5080-prices-hit-usd2-000-costing-more-than-the-rtx-5090-did-at-launch-and-with-limited-stock-available-original-usd999-msrp-long-forgotten-with-prices-now-2-3x-higher" target="_blank" rel="noopener" data-cat="keji" data-summary="现在购买Nvidia GeForce RTX 5080的成本与RTX 5090的发布价格一样高，现在这款高规格GPU的价格至少高出两倍。" data-title="Nvidia GeForce RTX 5080 prices hit $2,000, costing more than the RTX 5090 did at launch and with limited stock available — original $999 MSRP long forgotten, with prices now 2-3x higher" data-date="10-29 22:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 22:21</span>
          <span class="news-item-title">Nvidia GeForce RTX 5080价格达到2,000 $ ，比RTX 5090推出时的价格更高，库存有限—原价999 $的建议零售价早已被遗忘，现在价格高出2-3倍</span>
          <span class="news-item-title-en">Nvidia GeForce RTX 5080 prices hit $2,000, costing more than the RTX 5090 did at launch and with limited stock available — original $999 MSRP long forgotten, with prices now 2-3x higher</span>
          <span class="news-value-point">💡 现在购买Nvidia GeForce RTX 5080的成本与RTX 5090的发布价格一样高，现在这款高规格GPU的价格至少高出两倍</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/nvidia-ceo-jensen-huang-may-have-been-the-target-of-a-spy-plot-through-chinese-intelligence-asset-report-claims-exec-from-firm-under-investigation-for-smuggling-banned-ai-chips-to-china-accused-of-being-a-spy-was-also-feeding-information-to-beijing" target="_blank" rel="noopener" data-cat="keji" data-summary="消息人士称， Nvidia云合作伙伴的高管Alice Huang与Jensen Huang关系密切，涉嫌向北京传递信息。" data-title="Nvidia CEO Jensen Huang may have been the target of a spy plot through &#39;Chinese intelligence asset,&#39; report claims" data-date="10-29 21:04" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 21:04</span>
          <span class="news-item-title">报告称，英伟达首席执行官黄延森可能是“中国情报资产”间谍阴谋的目标</span>
          <span class="news-item-title-en">Nvidia CEO Jensen Huang may have been the target of a spy plot through 'Chinese intelligence asset,' report claims</span>
          <span class="news-value-point">💡 消息人士称， Nvidia云合作伙伴的高管Alice Huang与Jensen Huang关系密切，涉嫌向北京传递信息</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/dept-of-justice-reportedly-probes-nvidia-over-usd13-billion-hugging-face-ai-platform-acquisition-concerns-raised-over-competition-in-ai-and-pressure-on-customers" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达(Nvidia)以近130亿美元收购Hugging Face的交易因担心这将影响人工智能领域的竞争而受到密切关注。" data-title="Dept of Justice reportedly probes Nvidia over $13 billion Hugging Face AI platform acquisition" data-date="10-29 20:49" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 20:49</span>
          <span class="news-item-title">据报道，司法部调查英伟达逾130亿美元收购Hugging Face AI平台</span>
          <span class="news-item-title-en">Dept of Justice reportedly probes Nvidia over $13 billion Hugging Face AI platform acquisition</span>
          <span class="news-value-point">💡 英伟达(Nvidia)以近130亿美元收购Hugging Face的交易因担心这将影响人工智能领域的竞争而受到密切关注</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/29/us/politics/nvidia-china-jensen-huang-trump.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一名与Jensen Huang关系密切的中国女商人被发现正在向北京传递情报。特朗普总统听取了简报，但没有采取任何行动。" data-title="Nvidia Chief, Jensen Huang, Is Seen as Target of Chinese Spy Plot" data-date="10-29 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 17:01</span>
          <span class="news-item-title">英伟达首席执行官Jensen Huang被视为中国间谍阴谋的目标</span>
          <span class="news-item-title-en">Nvidia Chief, Jensen Huang, Is Seen as Target of Chinese Spy Plot</span>
          <span class="news-value-point">💡 一名与Jensen Huang关系密切的中国女商人被发现正在向北京传递情报</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506281.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月29日，文远知行披露旗下子公司景烁科技首次融资进展" data-title="文远知行001号员工带队，景烁科技首轮融资数千万美元" data-date="10-29 11:27" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-29 11:27</span>
          <span class="news-item-title">文远知行001号员工带队，景烁科技首轮融资数千万美元</span>
          <span class="news-value-point">💡 10月29日，文远知行披露旗下子公司景烁科技首次融资进展</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">14 条</span>
    </div>
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
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13605382/max-dowman-arsenals-appeal-against-teenagers-red-card-in-fleetwood-town-defeat-rejected" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉。" data-title="Arsenal fail with appeal against Dowman&#39;s red card" data-date="10-29 22:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:50</span>
          <span class="news-item-title">阿森纳对道曼的红牌上诉失败</span>
          <span class="news-item-title-en">Arsenal fail with appeal against Dowman's red card</span>
          <span class="news-value-point">💡 阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605382/max-dowman-arsenals-appeal-against-teenagers-red-card-in-fleetwood-town-defeat-rejected" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳在击败第二联盟弗利特伍德城时，未能对马克斯·道曼的红牌提出上诉。" data-title="Arsenal fail with appeal against Dowman&#39;s red card" data-date="10-29 22:50" data-source="天空体育">
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
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">卡里克准备与费尔南德斯一起“前进”</span>
          <span class="news-item-title-en">Carrick ready to 'move forward' with Fernandes as captain</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
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
        <a class="news-item" href="https://www.bbc.co.uk/sport/articles/cwx2836e1mp7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport的Ask Me Anything团队解释了本周末英超联赛的周日14:00 GMT开球在哪里。" data-title="Why is there only one Premier League match on Sunday?" data-date="10-29 20:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 20:47</span>
          <span class="news-item-title">为什么周日只有一场英超比赛？</span>
          <span class="news-item-title-en">Why is there only one Premier League match on Sunday?</span>
          <span class="news-value-point">💡 BBC Sport的Ask Me Anything团队解释了本周末英超联赛的周日14:00 GMT开球在哪里</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjvgx0ek6rz2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）表示，由于曼联坚持与压力不足的老板迈克尔·卡里克（ Michael Carrick ）合作，有时需要“为了自己的利益”解雇经理。" data-title="Sometimes managers need sacking for own good" data-date="10-29 19:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 19:00</span>
          <span class="news-item-title">有时管理者需要为了自己的利益而解雇</span>
          <span class="news-item-title-en">Sometimes managers need sacking for own good</span>
          <span class="news-value-point">💡 加里·内维尔（ Gary Neville ）表示，由于曼联坚持与压力不足的老板迈克尔·卡里克（ Michael Carrick ）合作，有时需要…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/29/tottenham-season-spurs-chelsea-win-table" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺有一个糟糕的开局，但在切尔西取得令人印象深刻的胜利后，他们突然抬头看了看Opta Analyst的桌子，实际上只有三分。托特纳姆热刺上周六晚上在切尔西的2-0胜利是一个有益的推动力" data-title="Tottenham’s season has finally taken off. How far up the table can they go?" data-date="10-29 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-29 16:00</span>
          <span class="news-item-title">托特纳姆热刺的赛季终于起飞了。他们能在桌子上走多远？</span>
          <span class="news-item-title-en">Tottenham’s season has finally taken off. How far up the table can they go?</span>
          <span class="news-value-point">💡 马刺有一个糟糕的开局，但在切尔西取得令人印象深刻的胜利后，他们突然抬头看了看Opta Analyst的桌子，实际上只有三分</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx05487d6r9vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="塔里克·穆哈雷莫维奇（ Tarik Muharemovic ）花费了利兹联（ Leeds United ）一笔“令人垂涎的”费用，给人留下了深刻的印象，以至于有些人担心俱乐部会" data-title="Chiellini guidance to Leeds &#39;rock&#39; - could Muharemovic be signing of season?" data-date="10-29 14:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 14:27</span>
          <span class="news-item-title">基耶利尼对利兹“摇滚”的指导-穆哈雷莫维奇会签下本赛季吗？</span>
          <span class="news-item-title-en">Chiellini guidance to Leeds 'rock' - could Muharemovic be signing of season?</span>
          <span class="news-value-point">💡 塔里克·穆哈雷莫维奇（ Tarik Muharemovic ）花费了利兹联（ Leeds United ）一笔“令人垂涎的”费用，给人留下了深刻…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1022440/ikea-varmblixt-smart-lamp-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凭借其俏皮的设计、多功能性和相对实惠的价格，宜家Varmblixt在4月份测试时迅速成为我的同事Jennifer Pattison Tuohy最喜欢的智能灯产品之一。现在，甜甜圈形状的灯在SAL上" data-title="Ikea’s colorful donut-shaped smart lamp is $20 off" data-date="10-30 02:18" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 02:18</span>
          <span class="news-item-title">宜家色彩缤纷的甜甜圈形智能灯$ 20折扣</span>
          <span class="news-item-title-en">Ikea’s colorful donut-shaped smart lamp is $20 off</span>
          <span class="news-value-point">💡 凭借其俏皮的设计、多功能性和相对实惠的价格，宜家Varmblixt在4月份测试时迅速成为我的同事Jennifer Pattison Tuohy最…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13605472/england-head-coach-brendon-mccullum-hails-captain-harry-brook-after-tourists-end-odi-tri-series-with-consolation-win" target="_blank" rel="noopener" data-cat="zonghe" data-summary="布伦登·麦卡勒姆（ Brendon McCullum ）称哈里·布鲁克（ Harry Brook ）是“我见过的最好的战术队长之一” ，此前英格兰队在拉合尔结束了一场艰难的ODI三连胜，安慰斯里兰卡队。" data-title="McCullum: Brook one of best tactical captains I&#39;ve come across" data-date="10-30 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 02:00</span>
          <span class="news-item-title">麦卡勒姆：布鲁克是我见过的最好的战术队长之一</span>
          <span class="news-item-title-en">McCullum: Brook one of best tactical captains I've come across</span>
          <span class="news-value-point">💡 布伦登·麦卡勒姆（ Brendon McCullum ）称哈里·布鲁克（ Harry Brook ）是“我见过的最好的战术队长之一” ，此前英格…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/1022347/apple-macbook-supports-new-cmf" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新款MacBook Pro为Apple笔记本电脑带来了一系列首创，其中最引人注目的两个是OLED显示屏和触摸屏功能。但作为一名图像准确性爱好者、训练有素的校准员和常驻显示专家，最让我兴奋的是" data-title="Apple’s new laptop supports one of the coolest features for color pros" data-date="10-30 01:48" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 01:48</span>
          <span class="news-item-title">Apple的新款笔记本电脑支持色彩专业人士最酷的功能之一</span>
          <span class="news-item-title-en">Apple’s new laptop supports one of the coolest features for color pros</span>
          <span class="news-value-point">💡 新款MacBook Pro为Apple笔记本电脑带来了一系列首创，其中最引人注目的两个是OLED显示屏和触摸屏功能</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1022400/utah-kalshi-criminal-charges" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据《盐湖论坛报》和美联社报道，犹他州已对Kalshi及其高管提起刑事指控，指控预测市场违反反赌博法。该州已对Kalshi提起了14项指控，并" data-title="Utah charges Kalshi and its CEO with illegally promoting online gambling" data-date="10-30 01:40" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 01:40</span>
          <span class="news-item-title">犹他州指控Kalshi及其首席执行官非法推广在线赌博</span>
          <span class="news-item-title-en">Utah charges Kalshi and its CEO with illegally promoting online gambling</span>
          <span class="news-value-point">💡 据《盐湖论坛报》和美联社报道，犹他州已对Kalshi及其高管提起刑事指控，指控预测市场违反反赌博法</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13605457/alcaraz-battles-into-vienna-open-quarter-finals" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡洛斯·阿尔卡拉斯（ Carlos Alcaraz ）被迫努力进入维也纳公开赛的四分之一决赛，因为世界排名第三的球队被尼科洛斯·巴西拉什维利（ Nikoloz Basilashvili ）带到了戏剧性的第二盘决胜局，之后他以6-1 7-6 （ 13-11 ）获胜。" data-title="Vienna Open: Carlos Alcaraz survives tiebreak scare against Nikoloz Basilashvili as Daniil Medvedev beats Cameron Norrie" data-date="10-30 01:15" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 01:15</span>
          <span class="news-item-title">维也纳公开赛：卡洛斯·阿尔卡拉兹在与尼科洛斯·巴西拉什维利的比赛中幸存下来，丹尼尔·梅德韦杰夫击败卡梅伦·诺里</span>
          <span class="news-item-title-en">Vienna Open: Carlos Alcaraz survives tiebreak scare against Nikoloz Basilashvili as Daniil Medvedev beats Cameron Norrie</span>
          <span class="news-value-point">💡 卡洛斯·阿尔卡拉斯（ Carlos Alcaraz ）被迫努力进入维也纳公开赛的四分之一决赛，因为世界排名第三的球队被尼科洛斯·巴西拉什维利（ …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1022258/data-centers-climate-change-carbon-dioxide-pollution-gas" target="_blank" rel="noopener" data-cat="zonghe" data-summary="根据Sierra C的一项新分析，到2030年，美国电力部门可能比2025年多释放42%的供暖二氧化碳污染，因为它建造了更多的化石燃料基础设施来满足数据中心的电力需求" data-title="Data centers could send US climate pollution skyrocketing" data-date="10-30 01:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 01:10</span>
          <span class="news-item-title">数据中心可能导致美国气候污染飙升</span>
          <span class="news-item-title-en">Data centers could send US climate pollution skyrocketing</span>
          <span class="news-value-point">💡 根据Sierra C的一项新分析，到2030年，美国电力部门可能比2025年多释放42%的供暖二氧化碳污染，因为它建造了更多的化石燃料基础设施来…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13605421/kimi-antonelli-to-miss-mexico-city-gp-media-day-due-to-viral-illness-ahead-of-likely-world-championship-coronation" target="_blank" rel="noopener" data-cat="zonghe" data-summary="由于周末之前的病毒性疾病， Kimi Antonelli将错过周四在墨西哥城大奖赛上的媒体日，届时他可能会成为一级方程式世界冠军。" data-title="Antonelli to miss Mexico media day with viral illness" data-date="10-30 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-30 01:00</span>
          <span class="news-item-title">安东内利因病毒性疾病错过墨西哥媒体日</span>
          <span class="news-item-title-en">Antonelli to miss Mexico media day with viral illness</span>
          <span class="news-value-point">💡 由于周末之前的病毒性疾病， Kimi Antonelli将错过周四在墨西哥城大奖赛上的媒体日，届时他可能会成为一级方程式世界冠军</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022214/yourownweigh-sync-withings-smart-scale-data-wireless-web-app-free" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当本月早些时候透露Withings将要求新用户订阅Withings Plus订阅以将公司设备中的健康数据同步到第三方应用程序时， Tom Anthony已经厌倦了Withings手机" data-title="This open-source project lets you sync Withings data to other apps without a subscription" data-date="10-30 00:14" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 00:14</span>
          <span class="news-item-title">这个开源项目允许您在没有订阅的情况下将Withings数据同步到其他应用程序</span>
          <span class="news-item-title-en">This open-source project lets you sync Withings data to other apps without a subscription</span>
          <span class="news-value-point">💡 当本月早些时候透露Withings将要求新用户订阅Withings Plus订阅以将公司设备中的健康数据同步到第三方应用程序时， Tom Ant…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/798.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 30 日消息，10 月 29 日，梅赛德斯 AMG GLC 53 4MATIC+ 在浙江国际赛车场正式上市，官方指导价 59.90 万元，仅此一款配置。其核心变化是用 3.0T 直列六缸 +48V 轻混系统接替了 GLC 43 上的 2.0T 四缸动力，六缸重回 GLC 性能序列。新车搭载了 M256 Evo 3.0T 直列六缸涡轮增压发动机，AMG 对其进行了专属升级，包括重新设计缸盖、优化进排气道、换用升级进气凸轮轴，并将涡轮增压压力提升至 1.5bar。发动机本体输出 330kW，峰值扭矩 600N·m，5200rpm 后进入超增压模式，可在 10 秒内将扭矩推至 640N·m。同时，48V 系统包含一台 7.5kW 电动辅助增压器和第二代 ISG 启动电机，ISG" data-title="59.9 万元梅赛德斯 AMG GLC 53 4MATIC+ 车型上市，3.0T 六缸回归" data-date="10-30 00:10" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-30 00:10</span>
          <span class="news-item-title">59.9 万元梅赛德斯 AMG GLC 53 4MATIC+ 车型上市，3.0T 六缸回归</span>
          <span class="news-value-point">💡 IT之家 10 月 30 日消息，10 月 29 日，梅赛德斯 AMG GLC 53 4MATIC+ 在浙江国际赛车场正式上市，官方指导价 59…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022295/joshua-kushner-thrive-holdings-adt-acquisition" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Joshua Kushner领导的Thrive Holdings正在以76亿美元的全现金交易收购ADT。正如彭博早些时候报道的那样，该交易预计将于2027年第一季度完成，并将ADT私有化。Joshua Kushner是兄弟" data-title="Joshua Kushner’s Thrive Holdings is acquiring ADT for $7.6 billion" data-date="10-30 00:03" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-30 00:03</span>
          <span class="news-item-title">Joshua Kushner的Thrive Holdings以76亿美元收购ADT</span>
          <span class="news-item-title-en">Joshua Kushner’s Thrive Holdings is acquiring ADT for $7.6 billion</span>
          <span class="news-value-point">💡 Joshua Kushner领导的Thrive Holdings正在以76亿美元的全现金交易收购ADT</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/29/us/politics/midterms-third-party-independent-candidates.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="阿拉斯加的另一位丹·沙利文（ Dan Sullivan ）引起了最多的关注，但两党都在悄悄地试图利用其他战场上鲜为人知的候选人来吸引选票。" data-title="Third-Party Spoilers, Long Fueled by Both Parties, Could Matter This Year" data-date="10-30 00:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-30 00:00</span>
          <span class="news-item-title">长期由双方推动的第三方破坏者今年可能很重要</span>
          <span class="news-item-title-en">Third-Party Spoilers, Long Fueled by Both Parties, Could Matter This Year</span>
          <span class="news-value-point">💡 阿拉斯加的另一位丹·沙利文（ Dan Sullivan ）引起了最多的关注，但两党都在悄悄地试图利用其他战场上鲜为人知的候选人来吸引选票</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/797.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，《星闪 SLE3.0 技术标准演进蓝皮书》已在国际星闪联盟官网正式上线。蓝皮书中详细介绍了星闪 SLE 3.0 的核心技术演进背景与目标。据介绍，星闪 SLE 当前支持 12Mbps 物理层，能基本满足通用数传、高清音频等应用场景。星闪 SLE 3.0 将在当前物理层基础上，链路峰值速率提升至 16Mbps+。根据规划，星闪 SLE 3.0 通过进一步优化 Polar 编码提升接收灵敏度，引入应用波束成形、更窄信道划分等技术，将兼顾提升应用的覆盖范围，同时还要改善大规模节点的接入，实现分布式自组网、多并发调度、多层同步网络、网络低时延能力、网络自愈能力。目前，星闪测距在星闪数字车钥匙和查找等应用中已落地达到亚米级精度。蓝皮书提到，未来还会在此领域中继续优化提" data-title="为 XR 设备无线音频铺路：星闪 SLE 3.0 计划链路峰值速率提至 16Mbps+，真正做到 Hi" data-date="10-29 23:59" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 23:59</span>
          <span class="news-item-title">为 XR 设备无线音频铺路：星闪 SLE 3.0 计划链路峰值速率提至 16Mbps+，真正做到 Hi</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，《星闪 SLE3.0 技术标准演进蓝皮书》已在国际星闪联盟官网正式上线</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10723072.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网伦敦10月29日电 (欧阳开宇 卢映菏)在中国驻伦敦旅游办支持下，由四川旅游学院与英国重庆商会联合主办的“行走的川菜非遗”(伦敦站)活动日前在伦敦举行。活动以川菜非物质文化遗产为核心纽带，搭建交流平台，积极推动川菜非遗海外传承发展，深化中英两国在教育、文化、餐饮及旅游领域的务实合作与友好往来。" data-title="“行走的川菜非遗”美食推介在伦敦举行" data-date="10-29 23:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:45</span>
          <span class="news-item-title">“行走的川菜非遗”美食推介在伦敦举行</span>
          <span class="news-value-point">💡 中新网伦敦10月29日电 (欧阳开宇 卢映菏)在中国驻伦敦旅游办支持下，由四川旅游学院与英国重庆商会联合主办的“行走的川菜非遗”(伦敦站)活动日…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723073.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社北京10月29日电 中宣部29日晚在京召开学习宣传贯彻党的二十届五中全会精神电视电话会议。中共中央政治局委员、中宣部部长李书磊出席会议并讲话。" data-title="中宣部组织召开学习宣传贯彻党的二十届五中全会精神电视电话会议" data-date="10-29 23:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 23:34</span>
          <span class="news-item-title">中宣部组织召开学习宣传贯彻党的二十届五中全会精神电视电话会议</span>
          <span class="news-value-point">💡 新华社北京10月29日电 中宣部29日晚在京召开学习宣传贯彻党的二十届五中全会精神电视电话会议</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/795.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，在昨日的华为双十一焕新季全场景新品发布会上，华为 Pura 90 Plus 手机正式发布，首发搭载麒麟 9025 芯片，焕新优惠价 5199 元起。IT之家从华为官方了解到，Pura 90 Plus 手机采用 NearLink E2.0 技术方案，上市即支持星闪音频功能。根据华为官方描述，星闪音频物理层传输速率可达 16Mbps，带宽能力超传统技术，充足的通道容量能够承载 48kHz/24bit Hi-Fi 音频无损传输。目前支持星闪音频的耳机包括 FreeClip 2 典藏版、FreeClip 2、FreeBuds Pro 5 等。" data-title="NearLink E2.0：华为 Pura 90 Plus 手机上市即支持星闪音频功能" data-date="10-29 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 23:28</span>
          <span class="news-item-title">NearLink E2.0：华为 Pura 90 Plus 手机上市即支持星闪音频功能</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，在昨日的华为双十一焕新季全场景新品发布会上，华为 Pura 90 Plus 手机正式发布，首发搭载麒麟 902…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-30 02:34（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
