---
layout: default
title: 热点新闻
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">时政国际、AI 与芯片、足球及综合资讯</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>2026-11-15 22:54 抓取更新</span>
    </div>
  </div>
  <div class="news-search-bar">
    <svg class="news-search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="search" id="news-search-input" class="news-search-input" aria-label="搜索新闻" placeholder="搜索标题、摘要、人物或信源" oninput="onNewsSearch(this.value)">
    <span id="news-search-count" class="news-search-count"></span>
  </div>
  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">56</span>
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
        <span class="channel-count">11</span>
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
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×17 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.tomshardware.com/tech-industry/drones/pentagon-tests-pack-hunting-with-autonomous-war-robots-darpa-experimented-with-four-drone-ground-vehicles-that-detected-tracked-and-engaged-simulated-threats" target="_blank" rel="noopener" data-cat="shizheng" data-summary="五角大楼一直在模拟战斗情境中测试多辆自主地面车辆。" data-title="Pentagon tests pack hunting with autonomous war robots" data-date="11-15 22:19" data-source="Tom's Hardware">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
        <span class="hero-featured-date">🕒 11-15 22:19</span>
      </div>
      <h2 class="hero-featured-title">五角大楼测试自主作战机器人群猎</h2>
      <div class="hero-featured-title-en">Pentagon tests pack hunting with autonomous war robots</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/027/458.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 15 日消息，法国银行及保险集团 Crédit Mutuel Arkéa 通报公司遭遇一起重大网络攻击，攻击者利用一家第三方服务供应商遭入侵的系统作为突破口，随后通过伪造即时转账指令，从银行自身账户转走约 1 亿欧元（IT之家注：现汇率约合 7.38 亿元人民币）。该集团董事长 Julien Carmona 表示，此次攻击“很可能”借助了先进人工智能技术，但其目前并未提供任何确凿性证据。当前银行正在与相关金融机构合作追回资金，法国警方也已展开刑事调查。Carmona 指出，这笔损失约占集团股本的 1%，相当于集团一个季度的利润，因此不会对银行整体经营及财务稳定性造成实质性影响。据披露，此次攻击最早可追溯至 10 月 27 日。当时，Crédit Mutuel Arkéa" data-title="法国 Crédit Mutuel Arkéa 银行遭网络攻击，被黑客转走 1 亿欧元" data-date="11-15 22:39" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">法国 Crédit Mutuel Arkéa 银行遭网络攻击，被黑客转走 1 亿欧元</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/rugby-league/news/12040/13612427/mens-rugby-league-world-cup-final-australia-32-12-new-zealand-kangaroos-brush-off-kiwis-to-win-fourth-straight-world-title" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在男子橄榄球世界杯决赛中，澳大利亚以32-12大胜新西兰，连续第四次夺得世界冠军，杰克·博斯托克（Jack Bostock）和利亚姆·马丁（Liam Martin）均有出色表现。" data-title="Australia brush off New Zealand to win fourth straight Rugby League World Cup" data-date="11-15 18:27" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">澳大利亚击败新西兰，四连胜夺得橄榄球联盟世界杯冠军</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-15/10732515.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社深圳11月15日电 题：APEC盛会核心场馆“静待花开” 会场外围成打卡热点" data-title="（深圳APEC）APEC盛会核心场馆“静待花开”  会场外围成打卡热点" data-date="11-15 22:44" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">（深圳APEC）APEC盛会核心场馆“静待花开”  会场外围成打卡热点</p>
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
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/pentagon-tests-pack-hunting-with-autonomous-war-robots-darpa-experimented-with-four-drone-ground-vehicles-that-detected-tracked-and-engaged-simulated-threats" target="_blank" rel="noopener" data-cat="shizheng" data-summary="五角大楼一直在模拟战斗情境中测试多辆自主地面车辆。" data-title="Pentagon tests pack hunting with autonomous war robots" data-date="11-15 22:19" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 22:19</span>
          <span class="news-item-title">五角大楼测试自主作战机器人群猎</span>
          <span class="news-item-title-en">Pentagon tests pack hunting with autonomous war robots</span>
          <span class="news-value-point">💡 五角大楼一直在模拟战斗情境中测试多辆自主地面车辆</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732511.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月15日电(记者潘洁、王丰)在15日举行的2026年APEC工商界活动专题新闻发布会上，中国贸促会副会长李庆霜介绍，2000余位政商界领袖将齐聚深圳前海，参加2026年APEC工商领导人峰会，共谋区域合作大计，共绘亚太发展蓝图。" data-title="聚焦APEC丨2000余位政商界领袖将参加APEC工商领导人峰会" data-date="11-15 21:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:33</span>
          <span class="news-item-title">聚焦APEC丨2000余位政商界领袖将参加APEC工商领导人峰会</span>
          <span class="news-value-point">💡 新华社深圳11月15日电(记者潘洁、王丰)在15日举行的2026年APEC工商界活动专题新闻发布会上，中国贸促会副会长李庆霜介绍，2000余位政…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732513.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月15日电 (记者 李京泽)亚太经合组织(APEC)第三十三次领导人非正式会议将于深圳启幕。作为此次APEC盛会的核心场馆，深圳国际交流中心、深圳湾文化广场、前海国际会议中心备受外界关注。" data-title="（深圳APEC）三个建筑师，给深圳APEC写了一份“国家答卷”" data-date="11-15 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:22</span>
          <span class="news-item-title">（深圳APEC）三个建筑师，给深圳APEC写了一份“国家答卷”</span>
          <span class="news-value-point">💡 中新社深圳11月15日电 (记者 李京泽)亚太经合组织(APEC)第三十三次领导人非正式会议将于深圳启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732495.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海11月15日电 (记者 陈静)“星”光守护——上海市关爱自闭症儿童公益联合体15日在沪正式启动，将重点开展艺术活动与文体疗愈、社区融合与场景体验，联合募款与资源对接。" data-title="上海：多方携手成立关爱自闭症儿童公益联合体" data-date="11-15 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:09</span>
          <span class="news-item-title">上海：多方携手成立关爱自闭症儿童公益联合体</span>
          <span class="news-value-point">💡 中新网上海11月15日电 (记者 陈静)“星”光守护——上海市关爱自闭症儿童公益联合体15日在沪正式启动，将重点开展艺术活动与文体疗愈、社区融合…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732498.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉11月15日电 应东盟轮值主席国菲律宾总统马科斯邀请，中国国务院总理李强乘包机于11月15日晚抵达马尼拉尼诺伊·阿基诺国际机场，将出席中国－东盟领导人会议。" data-title="李强抵马尼拉出席中国－东盟领导人会议" data-date="11-15 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:09</span>
          <span class="news-item-title">李强抵马尼拉出席中国－东盟领导人会议</span>
          <span class="news-value-point">💡 中新社马尼拉11月15日电 应东盟轮值主席国菲律宾总统马科斯邀请，中国国务院总理李强乘包机于11月15日晚抵达马尼拉尼诺伊·阿基诺国际机场，将出…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732501.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广西钦州11月15日电 题：平陆运河之畔文脉新生 广西钦江两岸文旅织新" data-title="平陆运河之畔文脉新生 广西钦江两岸文旅织新" data-date="11-15 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:07</span>
          <span class="news-item-title">平陆运河之畔文脉新生 广西钦江两岸文旅织新</span>
          <span class="news-value-point">💡 中新网广西钦州11月15日电 题：平陆运河之畔文脉新生 广西钦江两岸文旅织新</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732480.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月15日电 (记者 应妮)“河源·昆仑·玉帛：黄河文化与中华文明突出特性”研讨会日前在京召开。" data-title="“黄河文化与中华文明突出特性”研讨会在京举行" data-date="11-15 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:07</span>
          <span class="news-item-title">“黄河文化与中华文明突出特性”研讨会在京举行</span>
          <span class="news-value-point">💡 中新网北京11月15日电 (记者 应妮)“河源·昆仑·玉帛：黄河文化与中华文明突出特性”研讨会日前在京召开</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c9j3km83x5z2o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在被揭露婚外情后，黄仁勋于周四突然辞去了全球最有价值的公司之一的总裁职务。" data-title="黄仁勋被召出席参议院听证 商务部长卢特尼克受波及同须作证" data-date="11-15 18:32" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-15 18:32</span>
          <span class="news-item-title">黄仁勋被召出席参议院听证 商务部长卢特尼克受波及同须作证</span>
          <span class="news-value-point">💡 在被揭露婚外情后，黄仁勋于周四突然辞去了全球最有价值的公司之一的总裁职务</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/15/us/politics/trump-lutnick-ai-chips-cantor-fitzgerald.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="商务部长一直在起草新的规则，这些规则将影响东南亚的数据中心，其中一些数据中心是他前东家的客户。" data-title="Lutnick Pushed to Weaken Chip Rules That Overlap With His Family Business" data-date="11-15 18:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-15 18:02</span>
          <span class="news-item-title">卢特尼克推动放松与他家族企业有重叠的芯片规则</span>
          <span class="news-item-title-en">Lutnick Pushed to Weaken Chip Rules That Overlap With His Family Business</span>
          <span class="news-value-point">💡 商务部长一直在起草新的规则，这些规则将影响东南亚的数据中心，其中一些数据中心是他前东家的客户</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-15/10732416.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月15日电 综合美媒报道，14日晚间，一架货运飞机与一架喷气式客运飞机在迈阿密国际机场相撞。" data-title="美国突发飞机相撞事故" data-date="11-15 17:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 17:56</span>
          <span class="news-item-title">美国突发飞机相撞事故</span>
          <span class="news-value-point">💡 中新网11月15日电 综合美媒报道，14日晚间，一架货运飞机与一架喷气式客运飞机在迈阿密国际机场相撞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-15/10732408.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月15日电 综合美媒报道，美国太空探索技术公司重型运载火箭“星舰”的第二级飞船14日返回地球，并由发射塔机械臂“捕获”回收，这是该公司首次实现以这种方式回收飞船。" data-title="美“星舰”第15次试飞：“筷子夹飞船”首试成功，助推器未能返回发射场" data-date="11-15 17:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 17:22</span>
          <span class="news-item-title">美“星舰”第15次试飞：“筷子夹飞船”首试成功，助推器未能返回发射场</span>
          <span class="news-value-point">💡 中新网11月15日电 综合美媒报道，美国太空探索技术公司重型运载火箭“星舰”的第二级飞船14日返回地球，并由发射塔机械臂“捕获”回收，这是该公司…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732342.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="亚太经合组织第三十三次领导人非正式会议将于11月18日至19日在深圳举行，会议主题为“建设亚太共同体，促进共同繁荣”。国家主席习近平将主持会议并发表讲话。2013年以来，习近平主席出席或主持历次APEC领导人会议并发表重要讲话，在讲话中用一个个生动比喻，深刻阐述亚太合作的美好愿景，展现了对构建亚太共同体的深邃思考。" data-title="近镜头｜习近平主席妙论亚太合作之道" data-date="11-15 16:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 16:12</span>
          <span class="news-item-title">近镜头｜习近平主席妙论亚太合作之道</span>
          <span class="news-value-point">💡 亚太经合组织第三十三次领导人非正式会议将于11月18日至19日在深圳举行，会议主题为“建设亚太共同体，促进共同繁荣”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732358.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="携手共建亚太命运共同体※" data-title="携手共建亚太命运共同体" data-date="11-15 16:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 16:11</span>
          <span class="news-item-title">携手共建亚太命运共同体</span>
          <span class="news-value-point">💡 携手共建亚太命运共同体※</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732371.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：2026年亚太经合组织工商咨询理事会（ABAC）第四次会议新闻发布会" data-title="直播海报：2026年亚太经合组织工商咨询理事会（ABAC）第四次会议新闻发布会" data-date="11-15 16:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 16:10</span>
          <span class="news-item-title">直播海报：2026年亚太经合组织工商咨询理事会（ABAC）第四次会议新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732369.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：共赴深圳之约" data-title="直播海报：共赴深圳之约" data-date="11-15 16:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 16:08</span>
          <span class="news-item-title">直播海报：共赴深圳之约</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/027/458.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 15 日消息，法国银行及保险集团 Crédit Mutuel Arkéa 通报公司遭遇一起重大网络攻击，攻击者利用一家第三方服务供应商遭入侵的系统作为突破口，随后通过伪造即时转账指令，从银行自身账户转走约 1 亿欧元（IT之家注：现汇率约合 7.38 亿元人民币）。该集团董事长 Julien Carmona 表示，此次攻击“很可能”借助了先进人工智能技术，但其目前并未提供任何确凿性证据。当前银行正在与相关金融机构合作追回资金，法国警方也已展开刑事调查。Carmona 指出，这笔损失约占集团股本的 1%，相当于集团一个季度的利润，因此不会对银行整体经营及财务稳定性造成实质性影响。据披露，此次攻击最早可追溯至 10 月 27 日。当时，Crédit Mutuel Arkéa" data-title="法国 Crédit Mutuel Arkéa 银行遭网络攻击，被黑客转走 1 亿欧元" data-date="11-15 22:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 22:39</span>
          <span class="news-item-title">法国 Crédit Mutuel Arkéa 银行遭网络攻击，被黑客转走 1 亿欧元</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，法国银行及保险集团 Crédit Mutuel Arkéa 通报公司遭遇一起重大网络攻击，攻击者利用一家第三方…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/457.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 15 日消息，利用詹姆斯 · 韦布空间望远镜（JWST），天文学家发现了迄今观测到的最古老的一对由超大质量黑洞驱动的类星体。不过，这项发现也带来了一个难题：按照现有理论，它们本不应该如此早就存在。这对紧密相邻的类星体借助双子座北望远镜（Gemini North）得到确认，编号为 J1602+4228AB，昵称为 Nāpōwawāʻenakaulua。这个名称意为“在热量中重生、将能量注入宇宙的无尽强大黑暗中的两个天体”。天文学家观测到的，是这对类星体在宇宙大爆炸后约 9 亿年时的模样。当时宇宙还处于极其早期的阶段，按照现有理论，超大质量黑洞本应没有足够时间增长到如此惊人的质量。Nāpōwawāʻenakaulua 不仅是迄今发现的最古老、距离最遥远的类星体双星，两颗超大质" data-title="韦布望远镜发现迄今最古老类星体双星，现有黑洞成长理论难以解释" data-date="11-15 22:37" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 22:37</span>
          <span class="news-item-title">韦布望远镜发现迄今最古老类星体双星，现有黑洞成长理论难以解释</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，利用詹姆斯 · 韦布空间望远镜（JWST），天文学家发现了迄今观测到的最古老的一对由超大质量黑洞驱动的类星体</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/nvidia-board-director-cashed-out-usd1-billion-in-stock-before-jensen-huang-scandal-mark-stevens-sold-4-2-million-shares-without-a-trading-plan" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达董事会董事在8月31日至9月18日期间出售了约420万股股票，此次出售为其带来了约9.47亿美元的收益。" data-title="Nvidia board director cashed out $1 billion in stock before Jensen Huang scandal" data-date="11-15 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 22:00</span>
          <span class="news-item-title">在黄仁勋丑闻爆发前，英伟达董事会董事套现了10亿美元的股票</span>
          <span class="news-item-title-en">Nvidia board director cashed out $1 billion in stock before Jensen Huang scandal</span>
          <span class="news-value-point">💡 英伟达董事会董事在8月31日至9月18日期间出售了约420万股股票，此次出售为其带来了约9.47亿美元的收益</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1033948/sony-aibo-robot-dog-version-history" target="_blank" rel="noopener" data-cat="keji" data-summary="20世纪90年代，索尼深信我们正处于机器人接管的边缘。公司认为，很快我们所有人都会生活在无数人形机器人之中。有些会成为我们的同事；有些会成为我们的朋友；至少" data-title="The Sony Aibo was a robot revolution dressed like a dog" data-date="11-15 21:57" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-15 21:57</span>
          <span class="news-item-title">索尼Aibo是一款外形酷似狗狗的革命性机器人</span>
          <span class="news-item-title-en">The Sony Aibo was a robot revolution dressed like a dog</span>
          <span class="news-value-point">💡 20世纪90年代，索尼深信我们正处于机器人接管的边缘</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/453.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 15 日消息，据韩联社今日报道，由于税务师考试第一名考生存在利用人工智能进行作弊的行为被曝光，韩国政府决定对今年所有国家资格考试进行全面调查，以打击此类作弊行为。报道称，劳动部和相关机构决定对在第 63 届税务师考试中发现有 AI 作弊行为的第一名考生 A 进行取消考试成绩的处理，并限制其五年内不得参加该考试，以尽快落实后续措施。政府还计划年内出台一系列综合措施来防止国家资格考试中的作弊行为，比如引入红外线探测器等设备。此外，他们还将积极配合警方等调查机构的调查，并推进相关指控程序。报道提到，考生 A 不仅在税务师考试中作弊，甚至在注册会计师第一次考试中也使用了同样的手段进行作弊。鉴于此情况，根据这次作弊行为的模式，政府计划立即对今年所有国家资格考试中的人工智能作弊行为展" data-title="韩国税务师考试头名 AI 作弊曝光后，政府全面调查今年国家资格考试" data-date="11-15 21:42" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 21:42</span>
          <span class="news-item-title">韩国税务师考试头名 AI 作弊曝光后，政府全面调查今年国家资格考试</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，据韩联社今日报道，由于税务师考试第一名考生存在利用人工智能进行作弊的行为被曝光，韩国政府决定对今年所有国家资格…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-reclaims-overall-cpu-market-share-for-the-first-time-since-2025-massive-desktop-gains-offset-amds-record-server-and-mobile-growth" target="_blank" rel="noopener" data-cat="keji" data-summary="Mercury Research表示，随着第三季度客户端CPU销售额的下降，AMD在数据中心处理器出货量飙升之际，继续赢得服务器CPU市场份额。" data-title="Intel reclaims overall CPU market share for the first time since 2025" data-date="11-15 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 21:30</span>
          <span class="news-item-title">英特尔自2025年以来首次夺回CPU市场整体份额</span>
          <span class="news-item-title-en">Intel reclaims overall CPU market share for the first time since 2025</span>
          <span class="news-value-point">💡 Mercury Research表示，随着第三季度客户端CPU销售额的下降，AMD在数据中心处理器出货量飙升之际，继续赢得服务器CPU市场份额</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/450.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 15 日消息，华为云今日宣布，华为云 MaaS 模型即服务平台正式上线开源盘古模型 openPangu-2.1-Pro。该模型围绕 Agent 开发、AI 编码和推理优化三大方向进行能力升级，在深度研究、鸿蒙系统操控、鸿蒙 App 开发、升腾算子生成及推理链路优化等场景实现增强。在 Agent 能力方面，openPangu-2.1-Pro 基于 10 万余条专项数据优化 Skills 触发、工具选择与调用能力，提升复杂任务规划和执行效果，在深度研究及鸿蒙系统操控等场景实现能力增强。在代码能力方面，新模型重点面向鸿蒙 App 开发和升腾算子生成进行优化适配。围绕鸿蒙 ArkTS 语言及相关开发任务，持续提升代码生成的准确性和应用可用性；针对升腾算子开发流程进行专项优化，增强" data-title="开源盘古模型 openPangu-2.1-Pro 上线华为云，围绕 Agent 开发、AI 编码、推理优化方向能力升级" data-date="11-15 21:16" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 21:16</span>
          <span class="news-item-title">开源盘古模型 openPangu-2.1-Pro 上线华为云，围绕 Agent 开发、AI 编码、推理优化方向能力升级</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，华为云今日宣布，华为云 MaaS 模型即服务平台正式上线开源盘古模型 openPangu-2.1-Pro</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/column/1033943/jensen-huang-nvidia-china-spying-scandal-resignation" target="_blank" rel="noopener" data-cat="keji" data-summary="本期是《The Stepback》，这是一份每周通讯，深入剖析科技界的一则重要新闻。如需了解有关黄仁勋辞职以及英伟达领导层危机所产生影响的更多信息，请关注Terrence O&#39;Brien。The Stepback 将送达订阅者的" data-title="An overview of Jensen Huang’s messy days" data-date="11-15 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-15 21:00</span>
          <span class="news-item-title">黄仁勋的混乱日子概览</span>
          <span class="news-item-title-en">An overview of Jensen Huang’s messy days</span>
          <span class="news-value-point">💡 本期是《The Stepback》，这是一份每周通讯，深入剖析科技界的一则重要新闻</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/14/technology/jensen-huang-nvidia-board.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达的掌门人表示，他与一位女性客户的关系纯属业务往来。但他所隐瞒的事情最终导致他从自己创立的公司辞职。" data-title="How Jensen Huang’s Secret Led to His Downfall at Nvidia" data-date="11-15 20:40" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-15 20:40</span>
          <span class="news-item-title">黄仁勋的秘密是如何导致他在英伟达的陨落的</span>
          <span class="news-item-title-en">How Jensen Huang’s Secret Led to His Downfall at Nvidia</span>
          <span class="news-value-point">💡 英伟达的掌门人表示，他与一位女性客户的关系纯属业务往来</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/elon-musk-signs-petition-to-reinstate-jensen-huang-as-nvidia-ceo-over-130-000-sign-online-petition-but-not-all-nvidians-support-jensens-return" target="_blank" rel="noopener" data-cat="keji" data-summary="一份拥有超过9.1万个签名的在线请愿书呼吁让Nvidia声名狼藉的前首席执行官复职。" data-title="Elon Musk signs petition to reinstate Jensen Huang as Nvidia CEO" data-date="11-15 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 20:00</span>
          <span class="news-item-title">埃隆·马斯克签署请愿书，要求恢复黄仁勋的英伟达首席执行官职务</span>
          <span class="news-item-title-en">Elon Musk signs petition to reinstate Jensen Huang as Nvidia CEO</span>
          <span class="news-value-point">💡 一份拥有超过9.1万个签名的在线请愿书呼吁让Nvidia声名狼藉的前首席执行官复职</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/15/business/jensen-huang-taiwan.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达首席执行官的辞职震惊了他家乡的人们，在那里他被称为“人民的爸爸”。" data-title="Jensen Huang’s Downfall Brings Disbelief in Taiwan" data-date="11-15 18:01" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-15 18:01</span>
          <span class="news-item-title">黄仁勋的陨落让台湾人难以置信</span>
          <span class="news-item-title-en">Jensen Huang’s Downfall Brings Disbelief in Taiwan</span>
          <span class="news-value-point">💡 英伟达首席执行官的辞职震惊了他家乡的人们，在那里他被称为“人民的爸爸”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/392.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 15 日消息，据韩媒 Etnews 今天报道，尽管英伟达 CEO 更替等因素加剧 AI 行业不确定性，但 SK 海力士仍认为 HBM（IT之家注：高带宽内存）需求强劲。该公司计划重点投资 HBM 封装和测试环节的设备，并计划于明年上半年正式投入使用。据多位半导体设备行业人士透露，SK 海力士正与合作伙伴商讨采购 HBM4 生产设备。该公司主要与负责 HBM 键合、切割和检测等后道工序的设备供应商协调采购时间和数量。一位熟悉相关情况的 SK 海力士合作伙伴表示：“SK 海力士正推进 HBM4 生产设备的追加投资，正加快相关安排，目标是在明年上半年完成设备进场和安装调试。”据悉，SK 海力士计划加快设备投资进度，部分设备甚至要求供应商在第一季度前完成交付。同时，SK 海力士此" data-title="消息称 SK 海力士加快设备投资进度，进一步扩大 HBM4 产能" data-date="11-15 16:15" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 16:15</span>
          <span class="news-item-title">消息称 SK 海力士加快设备投资进度，进一步扩大 HBM4 产能</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，据韩媒 Etnews 今天报道，尽管英伟达 CEO 更替等因素加剧 AI 行业不确定性，但 SK 海力士仍认为…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq39gn7g7depo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋的丑闻使外界开始关注新加坡作为半导体贸易中心的成功——以及其是否成为非法贸易行为场所的疑问。" data-title="Nvidia黄仁勋丑闻如何令亲商的新加坡大感头疼" data-date="11-15 14:46" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-15 14:46</span>
          <span class="news-item-title">Nvidia黄仁勋丑闻如何令亲商的新加坡大感头疼</span>
          <span class="news-value-point">💡 黄仁勋的丑闻使外界开始关注新加坡作为半导体贸易中心的成功——以及其是否成为非法贸易行为场所的疑问</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/14/where-was-nvidias-security-team/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达的安全主管已于8月份悄然离职，而今首席执行官黄仁勋也因其人际关系而辞职，其中包括与一家涉嫌向中国输送芯片的公司的某位高管的关系。一位前情报官员表示，这正是问题所在。" data-title="Where was Nvidia’s security team?" data-date="11-15 08:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-15 08:08</span>
          <span class="news-item-title">Nvidia 的安全团队在哪里？</span>
          <span class="news-item-title-en">Where was Nvidia’s security team?</span>
          <span class="news-value-point">💡 英伟达的安全主管已于8月份悄然离职，而今首席执行官黄仁勋也因其人际关系而辞职，其中包括与一家涉嫌向中国输送芯片的公司的某位高管的关系</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/" target="_blank" rel="noopener" data-cat="keji" data-summary="截至周六下午，该请愿书已获得超过11.5万个签名。" data-title="Elon Musk, other tech execs sign petition calling on Nvidia to reinstate Jensen Huang" data-date="11-15 05:41" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-15 05:41</span>
          <span class="news-item-title">埃隆·马斯克和其他科技公司高管签署请愿书，呼吁英伟达恢复黄仁勋的职位</span>
          <span class="news-item-title-en">Elon Musk, other tech execs sign petition calling on Nvidia to reinstate Jensen Huang</span>
          <span class="news-value-point">💡 截至周六下午，该请愿书已获得超过11.5万个签名</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/rugby-league/news/12040/13612427/mens-rugby-league-world-cup-final-australia-32-12-new-zealand-kangaroos-brush-off-kiwis-to-win-fourth-straight-world-title" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在男子橄榄球世界杯决赛中，澳大利亚以32-12大胜新西兰，连续第四次夺得世界冠军，杰克·博斯托克（Jack Bostock）和利亚姆·马丁（Liam Martin）均有出色表现。" data-title="Australia brush off New Zealand to win fourth straight Rugby League World Cup" data-date="11-15 18:27" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 18:27</span>
          <span class="news-item-title">澳大利亚击败新西兰，四连胜夺得橄榄球联盟世界杯冠军</span>
          <span class="news-item-title-en">Australia brush off New Zealand to win fourth straight Rugby League World Cup</span>
          <span class="news-value-point">💡 在男子橄榄球世界杯决赛中，澳大利亚以32-12大胜新西兰，连续第四次夺得世界冠军，杰克·博斯托克（Jack Bostock）和利亚姆·马丁（Li…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13612415/x-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日报纸上的头条新闻和转会传闻……" data-title="Papers: Fernandes wants to see if Poch is &#39;real deal&#39; before signing new contract" data-date="11-15 17:47" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 17:47</span>
          <span class="news-item-title">媒体报道：费尔南德斯希望在与波切蒂诺签订新合同前确认他是否“货真价实”</span>
          <span class="news-item-title-en">Papers: Fernandes wants to see if Poch is 'real deal' before signing new contract</span>
          <span class="news-value-point">💡 周日报纸上的头条新闻和转会传闻……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13612415/x-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日报纸上的头条新闻和转会传闻……" data-title="Papers: Fernandes wants to see if Poch is &#39;real deal&#39; before signing new contract" data-date="11-15 17:47" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 17:47</span>
          <span class="news-item-title">媒体报道：费尔南德斯希望在与波切蒂诺签订新合同前确认他是否“货真价实”</span>
          <span class="news-item-title-en">Papers: Fernandes wants to see if Poch is 'real deal' before signing new contract</span>
          <span class="news-value-point">💡 周日报纸上的头条新闻和转会传闻……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: USA thrash Haiti in Poch&#39;s penultimate match" data-title="Man Utd latest: USA thrash Haiti in Poch&#39;s penultimate match" data-date="11-15 16:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 16:15</span>
          <span class="news-item-title">曼联最新消息：波切蒂诺执教倒数第二场比赛，美国队大胜海地队</span>
          <span class="news-item-title-en">Man Utd latest: USA thrash Haiti in Poch's penultimate match</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025499/man-city-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City latest: Haaland &#39;hasn&#39;t read much&#39; about PL charges guilty verdict" data-title="Man City latest: Haaland &#39;hasn&#39;t read much&#39; about PL charges guilty verdict" data-date="11-15 06:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 06:50</span>
          <span class="news-item-title">曼城最新消息：哈兰德“没有多看”英超指控的“有罪”判决</span>
          <span class="news-item-title-en">Man City latest: Haaland 'hasn't read much' about PL charges guilty verdict</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: Kulusevski makes first appearance for Sweden in 725 days" data-title="Spurs latest: Kulusevski makes first appearance for Sweden in 725 days" data-date="11-15 06:33" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 06:33</span>
          <span class="news-item-title">热刺最新消息：库卢塞夫斯基在725天后首次代表瑞典出场</span>
          <span class="news-item-title-en">Spurs latest: Kulusevski makes first appearance for Sweden in 725 days</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq0mdzrjn0j2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中场球员德克兰·赖斯（Declan Rice）在英格兰于温布利球场战胜克罗地亚的比赛中，为遭到嘘声的阿森纳队友本·怀特（Ben White）进行了辩护。" data-title="White has &#39;exciting future&#39; despite boos" data-date="11-15 06:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-15 06:26</span>
          <span class="news-item-title">尽管遭到嘘声，怀特仍有“光明的前途”</span>
          <span class="news-item-title-en">White has 'exciting future' despite boos</span>
          <span class="news-value-point">💡 中场球员德克兰·赖斯（Declan Rice）在英格兰于温布利球场战胜克罗地亚的比赛中，为遭到嘘声的阿森纳队友本·怀特（Ben White）进行…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Gyokeres continues superb Sweden form" data-title="Arsenal latest: Gyokeres continues superb Sweden form" data-date="11-15 06:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 06:00</span>
          <span class="news-item-title">阿森纳最新消息：乔克雷斯延续瑞典队出色状态</span>
          <span class="news-item-title-en">Arsenal latest: Gyokeres continues superb Sweden form</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279298/crystal-palace-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Palace latest: Sage thanks fans after exit" data-title="Palace latest: Sage thanks fans after exit" data-date="11-15 05:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 05:00</span>
          <span class="news-item-title">水晶宫最新消息：塞奇在离队后感谢球迷</span>
          <span class="news-item-title-en">Palace latest: Sage thanks fans after exit</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13612238/spain-vs-england-james-trafford-set-to-replace-jordan-pickford-as-goalkeeper-and-how-does-thomas-tuchel-stop-lamine-yamal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="面对世界上最出色的球队，托马斯·图赫尔的防守决策将是关键。而他需要做出很多决定。" data-title="A new No 1? How to stop Lamine Yamal? Tuchel&#39;s selection issues" data-date="11-15 00:02" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 00:02</span>
          <span class="news-item-title">新的头号球星？如何阻止拉明·亚马尔？图赫尔的选人问题</span>
          <span class="news-item-title-en">A new No 1? How to stop Lamine Yamal? Tuchel's selection issues</span>
          <span class="news-value-point">💡 面对世界上最出色的球队，托马斯·图赫尔的防守决策将是关键</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/norway-vs-wales/live/554107" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Nusa breaks Wales&#39; resistance in Oslo LIVE!" data-title="Nusa breaks Wales&#39; resistance in Oslo LIVE!" data-date="11-14 23:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-14 23:30</span>
          <span class="news-item-title">努萨在奥斯陆打破威尔士的防线，直播中！</span>
          <span class="news-item-title-en">Nusa breaks Wales' resistance in Oslo LIVE!</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-15/10732515.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社深圳11月15日电 题：APEC盛会核心场馆“静待花开” 会场外围成打卡热点" data-title="（深圳APEC）APEC盛会核心场馆“静待花开”  会场外围成打卡热点" data-date="11-15 22:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 22:44</span>
          <span class="news-item-title">（深圳APEC）APEC盛会核心场馆“静待花开”  会场外围成打卡热点</span>
          <span class="news-value-point">💡 中新社深圳11月15日电 题：APEC盛会核心场馆“静待花开” 会场外围成打卡热点</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/retro-gaming/enthusiast-builds-a-working-486-dx2-retro-pc-on-a-breadboard-in-just-16-days-immediately-runs-doom-build-includes-a-66-mhz-intel-chip-and-custom-five-inch-3d-printed-display" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一位应用工程师展示了他自制的面包板 486DX2 PC，这款电脑仅用两周多一点的时间就组装完成，并成功运行了《毁灭战士》。" data-title="Enthusiast builds a working 486 DX2 retro PC on a breadboard in just 16 days, immediately runs Doom" data-date="11-15 22:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 22:30</span>
          <span class="news-item-title">一位爱好者仅用16天就在面包板上打造了一台可正常运行的486 DX2复古电脑，并立即运行了《毁灭战士》</span>
          <span class="news-item-title-en">Enthusiast builds a working 486 DX2 retro PC on a breadboard in just 16 days, immediately runs Doom</span>
          <span class="news-value-point">💡 一位应用工程师展示了他自制的面包板 486DX2 PC，这款电脑仅用两周多一点的时间就组装完成，并成功运行了《毁灭战士》</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1033432/lg-b6e-oled-tv-best-buy-doorbuster-black-friday-2026-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="LG的B6E已经是市面上最实惠的OLED电视之一，但现在它被纳入百思买最新“开门抢购”活动的优惠行列，性价比就更胜一筹了。从现在起到今天（11月15日）结束，55英寸型号的价格为原价的50%。" data-title="LG’s budget-friendly B6E OLED TV is up to 50 percent off this weekend" data-date="11-15 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-15 22:00</span>
          <span class="news-item-title">LG的经济型B6E OLED电视本周末最高可享五折优惠</span>
          <span class="news-item-title-en">LG’s budget-friendly B6E OLED TV is up to 50 percent off this weekend</span>
          <span class="news-value-point">💡 LG的B6E已经是市面上最实惠的OLED电视之一，但现在它被纳入百思买最新“开门抢购”活动的优惠行列，性价比就更胜一筹了</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13612458/england-beat-australia-in-second-odi-sonny-baker-new-ball-switch-from-jofra-archer-pays-off-in-adelaide" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着英格兰队在阿德莱德以135分的优势扳平了与澳大利亚的三场ODI系列赛，他们是否已经找到了完美的投球方案，并着眼于2027年板球世界杯？" data-title="One for the World Cup? England&#39;s new-ball switch to Baker pays dividends" data-date="11-15 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 22:00</span>
          <span class="news-item-title">世界杯的一员？英格兰将新球交给贝克，效果显著</span>
          <span class="news-item-title-en">One for the World Cup? England's new-ball switch to Baker pays dividends</span>
          <span class="news-value-point">💡 随着英格兰队在阿德莱德以135分的优势扳平了与澳大利亚的三场ODI系列赛，他们是否已经找到了完美的投球方案，并着眼于2027年板球世界杯</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/live-blog/12040/13612212/dp-world-tour-championship-final-round-live-latest-scores-highlights-as-rory-mcilroy-chases-race-to-dubai-win" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Which players secured their PGA Tour cards via the Race to Dubai?" data-title="Which players secured their PGA Tour cards via the Race to Dubai?" data-date="11-15 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-15 22:00</span>
          <span class="news-item-title">哪些球员通过“通往迪拜之路”获得了PGA巡回赛参赛资格？</span>
          <span class="news-item-title-en">Which players secured their PGA Tour cards via the Race to Dubai?</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/454.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 15 日消息，汽车博主 @未来的学习笔记 昨日分享了鸿蒙智行尚界 Z7T 星野套装实车图。尚界 Z7T 星野套装最明显的变化属车尾部分。从画面可以看到，该版本车型新增了银色行李架、银色后视镜外壳、全车跨界套件以及黑色尾翼。参考IT之家此前报道，尚界 Z7T 是一款猎装车型，于今年 4 月上市，售价 22.98 万元起。尚界 Z7 全系标配华为干昆智驾 ADS 4.1、华为巨鲸 800V 高压电池平台、华为干昆 896 线双光路图像级激光雷达、华为鸿蒙座舱、华为途灵平台；全系标配鸿蒙 ALPS 健康座舱 2.0、随动屏、副驾零重力座椅、HUD 抬头显示、流媒体内后视镜、静音电吸门、连续可变阻尼减振器、Knock-Knock 电弹电吸前备箱。根据规划，鸿蒙智行尚界 Z7T 星" data-title="鸿蒙智行尚界 Z7T 星野套装实车图曝光，新增行李架、跨界套件、黑色尾翼等" data-date="11-15 21:53" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 21:53</span>
          <span class="news-item-title">鸿蒙智行尚界 Z7T 星野套装实车图曝光，新增行李架、跨界套件、黑色尾翼等</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，汽车博主 @未来的学习笔记 昨日分享了鸿蒙智行尚界 Z7T 星野套装实车图</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/14/us/flight-delays-cancelations-what-to-know.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在周五的全国性地面停飞之后，旅客仍然面临着种种障碍，航班时刻表可能需要几天时间才能恢复正常。" data-title="What to Know About Continued Flight Disruptions" data-date="11-15 21:53" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-15 21:53</span>
          <span class="news-item-title">关于持续性航班中断须知</span>
          <span class="news-item-title-en">What to Know About Continued Flight Disruptions</span>
          <span class="news-value-point">💡 在周五的全国性地面停飞之后，旅客仍然面临着种种障碍，航班时刻表可能需要几天时间才能恢复正常</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/networking/two-hpe-juniper-network-routers-grounded-all-the-us-flights-on-friday-faas-decades-old-copper-network-buckled-under-a-feature-hpe-says-worked-as-intended-creaking-air-traffic-communication-system-became-overloaded-by-very-high-rate-pinging" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国联邦航空管理局（FAA）认定，两台新安装的路由器中的一个异常功能是导致全国航班停飞的通信故障的罪魁祸首。" data-title="Two HPE Juniper network routers grounded all the US flights on Friday" data-date="11-15 21:42" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 21:42</span>
          <span class="news-item-title">两台HPE Juniper网络路由器导致美国周五所有航班停飞</span>
          <span class="news-item-title-en">Two HPE Juniper network routers grounded all the US flights on Friday</span>
          <span class="news-value-point">💡 美国联邦航空管理局（FAA）认定，两台新安装的路由器中的一个异常功能是导致全国航班停飞的通信故障的罪魁祸首</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/452.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 15 日消息，在本周举行的 TCL 华星全球显示生态大会 DTC 2026 上，TCL 华星以 RGBX 四基色显示架构为主题，展出三款全球首款 10.95 英寸 OLED 平板屏幕 —— 四基色双模色域、四基色双模低功耗、四基色双模低蓝害。官方表示，三款展品同源同平台，在传统 RGB 三基色基础上引入第四基色 X，通过 X 的不同选择（深红光／蓝磷光／浅蓝光 EL 材料），分别实现色域、能效、护眼三个维度的突破。▲ RGBX 四基色像素架构示意图（RGB vs RGBX，三种 X 对比）IT之家附三款产品介绍如下：双模色域全球首款四基色双模色域 OLED 平板屏幕（10.95&quot;），采用 RGBX 四基色技术，引入深红 RD 并搭配窄光谱 G，支持 BT.2020 89%" data-title="RGB 基础上引入第四基色 X，TCL 华星展出三款全球首款 10.95 英寸 OLED 平板屏幕" data-date="11-15 21:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 21:39</span>
          <span class="news-item-title">RGB 基础上引入第四基色 X，TCL 华星展出三款全球首款 10.95 英寸 OLED 平板屏幕</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，在本周举行的 TCL 华星全球显示生态大会 DTC 2026 上，TCL 华星以 RGBX 四基色显示架构为主…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/027/451.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 15 日消息，据福布斯报道，一项最新研究指出，地球上的冰冻区域正在全面退化，冰盖、山地冰川、海冰、积雪和永久冻土等关键组成部分，均面临日益严峻的环境风险。研究人员警告，这些区域的变化正在超出安全环境极限，并给地球及其生态系统带来越来越大的长期威胁。这项研究由斯德哥尔摩大学斯德哥尔摩韧性中心的研究人员牵头完成。研究指出，这些冰冻景观统称为“冰冻圈”（Cryosphere），在调节地球能量、水循环、碳循环和甲烷循环，以及储存碳方面发挥着不可替代的作用。随着冰冻圈持续退化，全球气温上升、海平面上涨和生态系统破坏等问题可能进一步加剧，灾难性洪水和干旱事件发生的风险也将随之增加。极地、沿海地区以及低洼地带尤其容易受到影响。研究认为，冰冻景观退化主要由人类活动引发的气候变化推动，工业" data-title="研究警告：地球冰冻圈退化正突破安全环境极限，海平面上升与极端灾害风险加剧" data-date="11-15 21:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-15 21:20</span>
          <span class="news-item-title">研究警告：地球冰冻圈退化正突破安全环境极限，海平面上升与极端灾害风险加剧</span>
          <span class="news-value-point">💡 IT之家 11 月 15 日消息，据福布斯报道，一项最新研究指出，地球上的冰冻区域正在全面退化，冰盖、山地冰川、海冰、积雪和永久冻土等关键组成部…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732493.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明11月15日电 (杨琼)云南民族大学15日消息，日前，该校彩带龙队在“国缘V3杯”第十八届全国舞龙舞狮锦标赛(舞龙项目)彩带龙自选套路比赛中，以8.95分斩获该项目第一名，让云岭龙狮在全国赛场舞出新气象。" data-title="云岭龙狮舞出新气象 云南民族大学彩带龙队全国锦标赛夺魁" data-date="11-15 21:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:10</span>
          <span class="news-item-title">云岭龙狮舞出新气象 云南民族大学彩带龙队全国锦标赛夺魁</span>
          <span class="news-value-point">💡 中新网昆明11月15日电 (杨琼)云南民族大学15日消息，日前，该校彩带龙队在“国缘V3杯”第十八届全国舞龙舞狮锦标赛(舞龙项目)彩带龙自选套路…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-15/10732497.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明11月15日电 (时文枝)云南省森林草原防灭火指挥部15日消息，9月1日以来，该省平均降水仅79.4毫米，较常年同期偏少64.3%，叠加超强厄尔尼诺现象影响，今冬明春预计持续高温少雨，林下可燃物富集、野外生产用火增多，火险等级将持续走高，森林草原防灭火工作面临前所未有的严峻挑战。经云南省人民政府批准，2026年11月15日起，该省正式进入2027年度森林草原防火期。" data-title="旱情叠加超强厄尔尼诺 云南提前启动2027年度森林草原防火期" data-date="11-15 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:09</span>
          <span class="news-item-title">旱情叠加超强厄尔尼诺 云南提前启动2027年度森林草原防火期</span>
          <span class="news-value-point">💡 中新网昆明11月15日电 (时文枝)云南省森林草原防灭火指挥部15日消息，9月1日以来，该省平均降水仅79.4毫米，较常年同期偏少64.3%，叠…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-15/10732499.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨11月15日电 (贡嘎来松)15日，以“美育浸润高原·青春艺彩飞扬”为主题的西藏自治区第二届大学生艺术展演暨颁奖晚会在西藏自治区群众艺术馆(区非遗保护中心)举行，西藏高校学子以艺为媒，共赴一场高原美育盛宴。" data-title="西藏第二届大学生艺术展演暨颁奖晚会在拉萨举办" data-date="11-15 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:07</span>
          <span class="news-item-title">西藏第二届大学生艺术展演暨颁奖晚会在拉萨举办</span>
          <span class="news-value-point">💡 中新网拉萨11月15日电 (贡嘎来松)15日，以“美育浸润高原·青春艺彩飞扬”为主题的西藏自治区第二届大学生艺术展演暨颁奖晚会在西藏自治区群众艺…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-15/10732508.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州11月15日电 (记者 王坚)广州市气象局15日晚宣布，基于前期气象资料判定，确定今年广州进入气候学上的秋季的时间是11月9日。" data-title="广州官宣“入秋” 今年夏季长达235天" data-date="11-15 21:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-15 21:06</span>
          <span class="news-item-title">广州官宣“入秋” 今年夏季长达235天</span>
          <span class="news-value-point">💡 中新网广州11月15日电 (记者 王坚)广州市气象局15日晚宣布，基于前期气象资料判定，确定今年广州进入气候学上的秋季的时间是11月9日</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/university-of-rochester-researchers-made-a-3d-bioprinter-from-a-modified-ender-3-usd450-bioprinter-makes-engineered-living-material-research-accessible" target="_blank" rel="noopener" data-cat="zonghe" data-summary="罗切斯特大学的微生物学家将一台Ender 3 FDM打印机改装成了一台3D生物打印机，成本仅为450美元，其性能却优于售价超过10万美元的3D生物打印机。" data-title="Modified Ender 3 becomes a $450 bioprinter for 3D printing engineered living materials" data-date="11-15 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-15 21:00</span>
          <span class="news-item-title">经过改装的Ender 3成为一台售价450美元的生物打印机，可用于3D打印工程化生物材料</span>
          <span class="news-item-title-en">Modified Ender 3 becomes a $450 bioprinter for 3D printing engineered living materials</span>
          <span class="news-value-point">💡 罗切斯特大学的微生物学家将一台Ender 3 FDM打印机改装成了一台3D生物打印机，成本仅为450美元，其性能却优于售价超过10万美元的3D生…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-15 22:54（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
