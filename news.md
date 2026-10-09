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
      <span>2026-10-09 16:05 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">7</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · BBC×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-09/10709658.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月9日电 据美国《华盛顿邮报》报道，当地时间10月8日，美国国防部发表声明表示，原定对胡德堡枪击案罪犯尼达尔·哈桑执行的枪决将通过网络直播，公众可在线观看。" data-title="美国防部：将网上直播枪决胡德堡枪击案凶手" data-date="10-09 15:55" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-09 15:55</span>
      </div>
      <h2 class="hero-featured-title">美国防部：将网上直播枪决胡德堡枪击案凶手</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/10-09/10709655.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京10月9日电 (记者 黄钰钦 曾玥)中国外交部发言人毛宁9日主持例行记者会。" data-title="日本右翼势力持续向国际主流大模型提供经过篡改的二战历史语料 中方驳斥" data-date="10-09 15:34" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">日本右翼势力持续向国际主流大模型提供经过篡改的二战历史语料 中方驳斥</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/09/carlos-baleba-manchester-united-debut" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛的回归，我们潜入签约谁可以提升曼联的中场–或进一步混淆事情卡洛斯·巴莱巴花了曼联$ 8870万（ £ 6500万）加上$ 680万（ £ 500万）的附加费，当他们在8月份从布莱顿签下他时。他可能b" data-title="Will Carlos Baleba fix Manchester United? Three big questions ahead of potential debut" data-date="10-09 16:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Will Carlos Baleba fix Manchester United? Three big questions ahead of potential debut</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/011.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，vivo 现已在其商城上架 Y600s Pro 手机，该机主打“10200mAh 蓝海电池、寰宇增强通信 3.0”，起售价 2699 元起。8GB RAM +256GB 存储空间：2699 元8GB RAM +512GB 存储空间：2999 元该机厚度 8.15mm，提供月光黑、浮光金、星紫和浩瀚蓝四种配色，手机正面搭载一块 6.83 英寸 2800×1260 分辨率 120Hz AMOLED 显示屏，匹配 3200 万像素前置自拍摄像头，手机后置 5000 万像素主摄。该机搭载联发科天玑 7300e 芯片，配备 8GB LPDDR5 RAM 内存和最高 512GB UFS 3.1 存储空间，内置 10200mAh 电池（支持 90W 有线充电和反向充电），搭" data-title="vivo Y600s Pro 手机上架：10200mAh 蓝海电池、天玑 7300e + 8GB RAM，2699 元起" data-date="10-09 16:03" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">vivo Y600s Pro 手机上架：10200mAh 蓝海电池、天玑 7300e + 8GB RAM，2699 元起</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709658.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月9日电 据美国《华盛顿邮报》报道，当地时间10月8日，美国国防部发表声明表示，原定对胡德堡枪击案罪犯尼达尔·哈桑执行的枪决将通过网络直播，公众可在线观看。" data-title="美国防部：将网上直播枪决胡德堡枪击案凶手" data-date="10-09 15:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:55</span>
          <span class="news-item-title">美国防部：将网上直播枪决胡德堡枪击案凶手</span>
          <span class="news-value-point">💡 中新网10月9日电 据美国《华盛顿邮报》报道，当地时间10月8日，美国国防部发表声明表示，原定对胡德堡枪击案罪犯尼达尔·哈桑执行的枪决将通过网络…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709669.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="记者：白佳丽、徐思钰" data-title="人均三个行李箱来华爆买，“China Haul”火了！" data-date="10-09 15:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:52</span>
          <span class="news-item-title">人均三个行李箱来华爆买，“China Haul”火了！</span>
          <span class="news-value-point">💡 记者：白佳丽、徐思钰</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709637.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月9日电 (记者 黄钰钦)中国外交部发言人毛宁9日主持例行记者会。" data-title="外交部：敦促美方与中方通过平等对话协商共同应对网络安全风险" data-date="10-09 15:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:51</span>
          <span class="news-item-title">外交部：敦促美方与中方通过平等对话协商共同应对网络安全风险</span>
          <span class="news-value-point">💡 中新网北京10月9日电 (记者 黄钰钦)中国外交部发言人毛宁9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709660.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月9日电 (记者 黄钰钦)中国外交部发言人毛宁9日主持例行记者会。" data-title="中方回应菲转运非法“坐滩”船只伤员：倒打一耙，令人不齿" data-date="10-09 15:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:39</span>
          <span class="news-item-title">中方回应菲转运非法“坐滩”船只伤员：倒打一耙，令人不齿</span>
          <span class="news-value-point">💡 中新网北京10月9日电 (记者 黄钰钦)中国外交部发言人毛宁9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709654.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月9日电 (记者 黄钰钦)中国外交部发言人毛宁9日主持例行记者会。" data-title="报道称中美讨论互访核设施可能性？ 外交部：与事实不符" data-date="10-09 15:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:33</span>
          <span class="news-item-title">报道称中美讨论互访核设施可能性？ 外交部：与事实不符</span>
          <span class="news-value-point">💡 中新网北京10月9日电 (记者 黄钰钦)中国外交部发言人毛宁9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-09/10709639.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月9日，外交部发言人毛宁主持例行记者会。" data-title="外交部回应网络安全问题：敦促美方摒弃双重标准和政治操弄" data-date="10-09 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:26</span>
          <span class="news-item-title">外交部回应网络安全问题：敦促美方摒弃双重标准和政治操弄</span>
          <span class="news-value-point">💡 10月9日，外交部发言人毛宁主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/us/politics/fort-hood-execution-streamed-public.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="如果执行，定于12月3日由行刑队公开处决Nidal Malik Hasan少校将是美国现代历史上的第一次。" data-title="Fort Hood Shooter’s Execution Will Be Public and Streamed Live, Pentagon Says" data-date="10-09 14:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 14:03</span>
          <span class="news-item-title">五角大楼表示，胡德堡射手的处决将公开并直播</span>
          <span class="news-item-title-en">Fort Hood Shooter’s Execution Will Be Public and Streamed Live, Pentagon Says</span>
          <span class="news-value-point">💡 如果执行，定于12月3日由行刑队公开处决Nidal Malik Hasan少校将是美国现代历史上的第一次</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709561.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月9日电 综合美媒报道，美国“林肯”号航空母舰在海上部署300多天后，于当地时间10月8日终于返抵加利福尼亚州圣迭戈母港。" data-title="超长部署300多天，美国“林肯”号航母返回圣迭戈母港" data-date="10-09 12:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 12:49</span>
          <span class="news-item-title">超长部署300多天，美国“林肯”号航母返回圣迭戈母港</span>
          <span class="news-value-point">💡 中新网10月9日电 综合美媒报道，美国“林肯”号航空母舰在海上部署300多天后，于当地时间10月8日终于返抵加利福尼亚州圣迭戈母港</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqr7yvg2n4kvo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国国防部长赫格塞斯表示，这场处决将公开进行，但一名法律专家指出，这项“前所未有”的决定处于“法律基础不明确的领域”。" data-title="美国要网上直播军法枪决胡德堡基地枪击案凶手" data-date="10-09 12:39" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 12:39</span>
          <span class="news-item-title">美国要网上直播军法枪决胡德堡基地枪击案凶手</span>
          <span class="news-value-point">💡 美国国防部长赫格塞斯表示，这场处决将公开进行，但一名法律专家指出，这项“前所未有”的决定处于“法律基础不明确的领域”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/us/fiery-senate-debates-in-maine-michigan-and-georgia-five-takeaways.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="可能决定参议院控制权的三场比赛的候选人进行了激烈的人身攻击。" data-title="Fiery Senate Debates in Maine, Michigan and Georgia: Five Takeaways" data-date="10-09 12:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 12:01</span>
          <span class="news-item-title">缅因州、密歇根州和佐治亚州参议院激烈辩论：五大要点</span>
          <span class="news-item-title-en">Fiery Senate Debates in Maine, Michigan and Georgia: Five Takeaways</span>
          <span class="news-value-point">💡 可能决定参议院控制权的三场比赛的候选人进行了激烈的人身攻击</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709520.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网悉尼10月9日电 (记者 薄雯雯)澳大利亚著名汉学家马克林(Colin Mackerras)当地时间10月8日晚在布里斯班因病离世，享年87岁。" data-title="澳大利亚著名汉学家马克林逝世 享年87岁" data-date="10-09 11:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 11:50</span>
          <span class="news-item-title">澳大利亚著名汉学家马克林逝世 享年87岁</span>
          <span class="news-value-point">💡 中新网悉尼10月9日电 (记者 薄雯雯)澳大利亚著名汉学家马克林(Colin Mackerras)当地时间10月8日晚在布里斯班因病离世，享年8…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709537.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月9日电 据日本广播协会(NHK)报道，当地时间9日，日本政府在内阁会议上敲定了把食品饮料的消费税税率从8%下调至1%的相关法案，并计划当天提交给国会。同时，日本在野党和民众进一步质疑减税措施的效果和资金来源问题。" data-title="高市减税政策持续遭质疑：日本民众对政治不信任感加剧" data-date="10-09 11:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 11:47</span>
          <span class="news-item-title">高市减税政策持续遭质疑：日本民众对政治不信任感加剧</span>
          <span class="news-value-point">💡 中新网10月9日电 据日本广播协会(NHK)报道，当地时间9日，日本政府在内阁会议上敲定了把食品饮料的消费税税率从8%下调至1%的相关法案，并计…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709526.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="车 斌" data-title="邦加岛惨案，日军罪行岂容遗忘（环球走笔）" data-date="10-09 11:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 11:06</span>
          <span class="news-item-title">邦加岛惨案，日军罪行岂容遗忘（环球走笔）</span>
          <span class="news-value-point">💡 车 斌</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-09/10709492.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月9日电 综合消息：伊朗原子能组织主席伊斯拉米当地时间8日表示，伊朗绝对不会放弃铀浓缩，也不会交出铀。美国总统特朗普8日称，美伊双方正在进行磋商，美国不会在国会中期选举前攻击伊朗。" data-title="伊朗拒绝放弃铀浓缩 特朗普称美中期选举前不会攻击伊朗" data-date="10-09 10:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 10:45</span>
          <span class="news-item-title">伊朗拒绝放弃铀浓缩 特朗普称美中期选举前不会攻击伊朗</span>
          <span class="news-value-point">💡 中新社北京10月9日电 综合消息：伊朗原子能组织主席伊斯拉米当地时间8日表示，伊朗绝对不会放弃铀浓缩，也不会交出铀</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1008530/us-government-livestream-execution-firing-squad-fort-hood" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国国防部匿名官员告诉英国广播公司和美联社，美国对胡德堡射手的处决将进行直播。计划处决前美国陆军少校尼达尔·哈桑（ Nidal Hasan ） ，因杀害13人而被定罪" data-title="US plans livestream of execution by firing squad" data-date="10-09 06:32" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 06:32</span>
          <span class="news-item-title">美国计划通过行刑队进行处决直播</span>
          <span class="news-item-title-en">US plans livestream of execution by firing squad</span>
          <span class="news-value-point">💡 美国国防部匿名官员告诉英国广播公司和美联社，美国对胡德堡射手的处决将进行直播</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
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
        <a class="news-item" href="https://www.qbitai.com/2026/10/502125.html" target="_blank" rel="noopener" data-cat="keji" data-summary="星动纪元选择将视频预测与动作学习分阶段训练，重点不是“视频、动作一锅炖”，而是把两者“解耦”，重新“排序”。" data-title="清华具身模型登顶全球第一！突围GPT" data-date="10-09 11:52" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 11:52</span>
          <span class="news-item-title">清华具身模型登顶全球第一！突围GPT</span>
          <span class="news-value-point">💡 星动纪元选择将视频预测与动作学习分阶段训练，重点不是“视频、动作一锅炖”，而是把两者“解耦”，重新“排序”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502106.html" target="_blank" rel="noopener" data-cat="keji" data-summary="多Agent协同还能自我进化" data-title="openJiuwen发布并开源企业级AgentOS，加速智能体规模落地企业" data-date="10-09 10:37" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 10:37</span>
          <span class="news-item-title">openJiuwen发布并开源企业级AgentOS，加速智能体规模落地企业</span>
          <span class="news-value-point">💡 多Agent协同还能自我进化</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/science/mathematicians-respond-openai-release.html" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能产生的数百项新发现在一天之内推动了高等数学的前沿，消除了人们对该领域永远改变的任何怀疑。" data-title="‘Breathtaking,’ ‘Devastating’: Mathematics Reels After New OpenAI Release" data-date="10-09 10:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 10:27</span>
          <span class="news-item-title">“令人叹为观止”、“毁灭性” ：新的OpenAI发布后的数学卷轴</span>
          <span class="news-item-title-en">‘Breathtaking,’ ‘Devastating’: Mathematics Reels After New OpenAI Release</span>
          <span class="news-value-point">💡 人工智能产生的数百项新发现在一天之内推动了高等数学的前沿，消除了人们对该领域永远改变的任何怀疑</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502096.html" target="_blank" rel="noopener" data-cat="keji" data-summary="让AI反复试错的“练兵场”来了" data-title="代码造世界，扩散绘现实：AgentGarten让智能体在实时试炼场中边玩边进化" data-date="10-09 10:03" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 10:03</span>
          <span class="news-item-title">代码造世界，扩散绘现实：AgentGarten让智能体在实时试炼场中边玩边进化</span>
          <span class="news-value-point">💡 让AI反复试错的“练兵场”来了</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/nyregion/mamdani-nyc-october-7-vigil-protesters.html" target="_blank" rel="noopener" data-cat="keji" data-summary="巴勒斯坦倡导者承认他们运动中的各种观点，但对针对市长Zohran Mamdani的尖刻言辞感到沮丧，他是他们事业的长期盟友。" data-title="Some Palestinians Express Discomfort With Protest Targeting Mamdani" data-date="10-09 09:09" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 09:09</span>
          <span class="news-item-title">一些巴勒斯坦人对针对Mamdani的抗议活动表示不满</span>
          <span class="news-item-title-en">Some Palestinians Express Discomfort With Protest Targeting Mamdani</span>
          <span class="news-value-point">💡 巴勒斯坦倡导者承认他们运动中的各种观点，但对针对市长Zohran Mamdani的尖刻言辞感到沮丧，他是他们事业的长期盟友</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502089.html" target="_blank" rel="noopener" data-cat="keji" data-summary="彻底撕破脸了" data-title="陶哲轩带头宣战！人类数学家联合抵制OpenAI" data-date="10-09 08:35" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 08:35</span>
          <span class="news-item-title">陶哲轩带头宣战！人类数学家联合抵制OpenAI</span>
          <span class="news-value-point">💡 彻底撕破脸了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502083.html" target="_blank" rel="noopener" data-cat="keji" data-summary="新的“缝合怪”已经出现，怎么能够停滞不前" data-title="不等Gemini 4了！谷歌发布办公Agent，支持调用Claude" data-date="10-09 08:16" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-09 08:16</span>
          <span class="news-item-title">不等Gemini 4了！谷歌发布办公Agent，支持调用Claude</span>
          <span class="news-value-point">💡 新的“缝合怪”已经出现，怎么能够停滞不前</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1008521/anthropic-open-source-oss-scanner" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic提供名为OSS Scanner的新服务，帮助开源项目跟踪安全漏洞。它表示，选择加入的开源项目将“由我们最强大的模型免费进行全面、定期的安全扫描。”" data-title="Anthropic launches free AI security scans for open" data-date="10-09 05:53" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 05:53</span>
          <span class="news-item-title">Anthropic推出免费的人工智能安全扫描</span>
          <span class="news-item-title-en">Anthropic launches free AI security scans for open</span>
          <span class="news-value-point">💡 Anthropic提供名为OSS Scanner的新服务，帮助开源项目跟踪安全漏洞</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1008353/amd-will-bring-fsr-4-to-handhelds-by-the-end-of-2026" target="_blank" rel="noopener" data-cat="keji" data-summary="已经有可能在与Steam Deck一样老的手持设备上获得AMD的帧速率增强FSR 4提升-但在6月， AMD保留了让手持游戏玩家失望的权利，因为它没有正式将FSR 4带到旧的手持设备上。现在， AMD消费者芯片b" data-title="AMD will bring FSR 4 to handhelds by the end of 2026" data-date="10-09 05:01" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 05:01</span>
          <span class="news-item-title">AMD将在2026年底前将FSR 4引入手持设备</span>
          <span class="news-item-title-en">AMD will bring FSR 4 to handhelds by the end of 2026</span>
          <span class="news-value-point">💡 已经有可能在与Steam Deck一样老的手持设备上获得AMD的帧速率增强FSR 4提升-但在6月， AMD保留了让手持游戏玩家失望的权利，因为…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/nyregion/mamdani-oct-7-statement-events-israel-palestine.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这位市长在10月7日袭击周年纪念声明中受到犹太领导人的批评，后来在守夜时被亲巴勒斯坦活动人士嘘声后，他没有表示遗憾。" data-title="Mamdani Stands By His Handling of Oct. 7 Anniversary After Emotional Day" data-date="10-09 04:51" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-09 04:51</span>
          <span class="news-item-title">Mamdani在情感日之后处理10月7日的周年纪念日</span>
          <span class="news-item-title-en">Mamdani Stands By His Handling of Oct. 7 Anniversary After Emotional Day</span>
          <span class="news-value-point">💡 这位市长在10月7日袭击周年纪念声明中受到犹太领导人的批评，后来在守夜时被亲巴勒斯坦活动人士嘘声后，他没有表示遗憾</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
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
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c54g13we4rero?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="足球协会对埃弗顿前锋马丁·谢里夫处以5000 £的罚款，罪名是在15个月内违反其投注规则。" data-title="Everton&#39;s Sherif fined for breaching betting rules" data-date="10-08 22:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-08 22:24</span>
          <span class="news-item-title">埃弗顿的谢里夫因违反投注规则而被罚款</span>
          <span class="news-item-title-en">Everton's Sherif fined for breaching betting rules</span>
          <span class="news-value-point">💡 足球协会对埃弗顿前锋马丁·谢里夫处以5000 £的罚款，罪名是在15个月内违反其投注规则</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/video/2026/oct/08/manchester-city-liverpool-eckert-spygate-ban-too-lenient-football-weekly-video" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马克斯·拉什登（ Max Rushden ）与巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandini ）和保罗·沃森（ Paul Watson ）一起，预览了英超联赛的回归，包括曼城自他们有罪判决以来的第一场比赛。" data-title="Manchester City go to Anfield and is Eckert’s Spygate ban too lenient? | Football Weekly video" data-date="10-08 19:56" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 19:56</span>
          <span class="news-item-title">曼城去安菲尔德，埃克特的Spygate禁令是否过于宽松？ |《足球周刊》视频</span>
          <span class="news-item-title-en">Manchester City go to Anfield and is Eckert’s Spygate ban too lenient? | Football Weekly video</span>
          <span class="news-value-point">💡 马克斯·拉什登（ Max Rushden ）与巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandin…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/audio/2026/oct/08/manchester-city-liverpool-premier-league-tonda-eckert-spygate-football-weekly-podcast" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandini ）和保罗·沃森（ Paul Watson ）与马克斯·拉什登（ Max Rushden ）一起预览英超联赛价格的回归，查看、分享苹果播客，并通过电子邮件加入对话。今天的播客；英超联赛回归并解说" data-title="Manchester City’s trip to Anfield and is Eckert’s Spygate ban too lenient? – Football Weekly podcast" data-date="10-08 19:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 19:13</span>
          <span class="news-item-title">曼城的安菲尔德之旅以及埃克特的Spygate禁令是否过于宽松？ –《足球周刊》播客</span>
          <span class="news-item-title-en">Manchester City’s trip to Anfield and is Eckert’s Spygate ban too lenient? – Football Weekly podcast</span>
          <span class="news-value-point">💡 巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandini ）和保罗·沃森（ Paul Watson …</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/08/brighton-contenders-qualify-champions-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="他们是联盟中得分最高的球员，他们的进球差异最大，他们击败了冠军，没有丹尼·韦尔贝克（ Danny Welbeck ） ，在英超联赛中排名第三。布莱顿整个夏天都失去了一些最好的球员；" data-title="Are Brighton genuine contenders to qualify for the Champions League?" data-date="10-08 19:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 19:00</span>
          <span class="news-item-title">布莱顿的真正竞争者是否有资格参加欧洲冠军联赛？</span>
          <span class="news-item-title-en">Are Brighton genuine contenders to qualify for the Champions League?</span>
          <span class="news-value-point">💡 他们是联盟中得分最高的球员，他们的进球差异最大，他们击败了冠军，没有丹尼·韦尔贝克（ Danny Welbeck ） ，在英超联赛中排名第三</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm0e35gzgdqeo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿体育总监Mike Cave讨论了布莱顿的转会政策，以及俱乐部如何签约和培养比赛中最优秀的年轻人才。" data-title="How Brighton attract and develop the best young players ahead of their rivals" data-date="10-08 18:37" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-08 18:37</span>
          <span class="news-item-title">布莱顿如何在竞争对手之前吸引和培养最优秀的年轻球员</span>
          <span class="news-item-title-en">How Brighton attract and develop the best young players ahead of their rivals</span>
          <span class="news-value-point">💡 布莱顿体育总监Mike Cave讨论了布莱顿的转会政策，以及俱乐部如何签约和培养比赛中最优秀的年轻人才</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/011.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，vivo 现已在其商城上架 Y600s Pro 手机，该机主打“10200mAh 蓝海电池、寰宇增强通信 3.0”，起售价 2699 元起。8GB RAM +256GB 存储空间：2699 元8GB RAM +512GB 存储空间：2999 元该机厚度 8.15mm，提供月光黑、浮光金、星紫和浩瀚蓝四种配色，手机正面搭载一块 6.83 英寸 2800×1260 分辨率 120Hz AMOLED 显示屏，匹配 3200 万像素前置自拍摄像头，手机后置 5000 万像素主摄。该机搭载联发科天玑 7300e 芯片，配备 8GB LPDDR5 RAM 内存和最高 512GB UFS 3.1 存储空间，内置 10200mAh 电池（支持 90W 有线充电和反向充电），搭" data-title="vivo Y600s Pro 手机上架：10200mAh 蓝海电池、天玑 7300e + 8GB RAM，2699 元起" data-date="10-09 16:03" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 16:03</span>
          <span class="news-item-title">vivo Y600s Pro 手机上架：10200mAh 蓝海电池、天玑 7300e + 8GB RAM，2699 元起</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，vivo 现已在其商城上架 Y600s Pro 手机，该机主打“10200mAh 蓝海电池、寰宇增强通信 3.0…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709677.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“我的铁路风景”主题宣传家国季活动" data-title="我的铁路风景｜列车上、车站里、海峡间，唱响爱国赞歌！" data-date="10-09 15:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:57</span>
          <span class="news-item-title">我的铁路风景｜列车上、车站里、海峡间，唱响爱国赞歌！</span>
          <span class="news-value-point">💡 “我的铁路风景”主题宣传家国季活动</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/999.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，不少知名游戏工作室都有长期高强度加班的问题，《最后生还者》的开发商顽皮狗便是其中之一。多年来，可信媒体的报道早已让顽皮狗的加班文化广为人知，工作室人员也曾公开承认过这种情况。2025 年 12 月，有消息称顽皮狗强制员工加班，以赶制《星际：异端先知》的演示版本。今年 4 月，顽皮狗前高级游戏设计师本森 · 拉塞尔还暗示，员工接受高强度加班，是因为他们认为，要做出这种水准的游戏，就必须付出这样的代价。据外媒 GamesRadar 当地时间 8 日报道，曾参与《神秘海域 4：盗贼末路》和《最后生还者》制作的视觉特效美术师马特 · 拉德福德近日接受 Kiwi Talkz 采访时，也表达了类似的看法。他认为，外界对顽皮狗加班文化的理解并不全面。媒体报道的加班情况大体属" data-title="顽皮狗视觉特效美术师谈公司“加班文化”：伟大的艺术诞生于痛苦之中" data-date="10-09 15:55" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 15:55</span>
          <span class="news-item-title">顽皮狗视觉特效美术师谈公司“加班文化”：伟大的艺术诞生于痛苦之中</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，不少知名游戏工作室都有长期高强度加班的问题，《最后生还者》的开发商顽皮狗便是其中之一</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/998.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，据上海徐汇警方，近期徐汇警方破获一起恶意敲诈电商案件，33 岁女子杨某自导自演童装藏针伤人的戏码，一年半时间内先后 9 次敲诈多家服饰网店，涉案金额 3 万余元，现已因涉嫌敲诈勒索罪被依法刑事拘留。据悉，杨某曾有网店客服从业经历，深知电商品牌十分忌惮负面舆情，遇到消费者投诉往往愿意花钱息事宁人。2024 年底，她网购衣物时确实被异物划伤，并成功拿到商家赔偿，这次经历让她萌生恶意索赔的想法。作案期间，杨某借用亲友的账号下单，购买童装、鹅绒服等商品。收货后，她把家用绣花针剪断，再用红药水、少量鲜血涂抹在手指上，伪造孩子被衣服内针头扎伤的照片，向商家投诉，声称衣物藏针刺伤孩童，要求高额赔偿，还威胁如果不满足诉求就全网曝光、大量差评。直到一家鹅绒服网店接到其投诉“要求" data-title="女子 1 年半内 9 次以“童装藏针扎伤孩子”敲诈网店被警方刑拘，涉案金额 3 万余元" data-date="10-09 15:55" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 15:55</span>
          <span class="news-item-title">女子 1 年半内 9 次以“童装藏针扎伤孩子”敲诈网店被警方刑拘，涉案金额 3 万余元</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，据上海徐汇警方，近期徐汇警方破获一起恶意敲诈电商案件，33 岁女子杨某自导自演童装藏针伤人的戏码，一年半时间内先…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709674.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="极目新闻记者 陆缘" data-title="开局之年看中国·潮涌荆楚｜推进“微更新”，激活城市“金角银边”" data-date="10-09 15:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:54</span>
          <span class="news-item-title">开局之年看中国·潮涌荆楚｜推进“微更新”，激活城市“金角银边”</span>
          <span class="news-value-point">💡 极目新闻记者 陆缘</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/997.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，蚂蚁电竞 (ANTGAMER) 昨晚正式发售了显示器新品 ANT253PQ MAX。这一型号采用第二代 HMO（IT之家注：高迁移率氧化物）技术，在保持 QHD 分辨率的同时将刷新率提升至 380Hz，到手价 2498.4 元。ANT253PQ MAX 基于使用第二代 HFL 液晶材料的 24.5&quot; IPS 面板，灰阶 (GtG) 响应时间低至 1ms；获得 VESA DisplayHDR 400 认证；色域 99% DCI-P3，色偏（平均值）ΔE＜2；支持 DIC 2.0 动态模糊消除、战术目镜、快速破闪。其提供 1 个 DisplayPort 2.1 (UHBR13.5)、2 个 HDMI 2.1、1 个 3.5mm 音频输出插孔；配备人体工学支架，兼容" data-title="蚂蚁电竞 ANT253PQ MAX 显示器发售：第二代 HMO 技术，QHD 380Hz" data-date="10-09 15:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 15:52</span>
          <span class="news-item-title">蚂蚁电竞 ANT253PQ MAX 显示器发售：第二代 HMO 技术，QHD 380Hz</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，蚂蚁电竞 (ANTGAMER) 昨晚正式发售了显示器新品 ANT253PQ MAX</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/996.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，改装商“罗伦士汽车”宣布旗下罗伦士梦想家山河四座高顶版上市，该车基于岚图梦想家山河四座版（售 70.99 万元）打造而来，采用悬浮高顶设计，整车高度抬升 10cm，售价为 80.99 万元。该车配备罗伦士定制“云澜格栅”，设计灵感源自故宫太和殿的窗棂，带有可发光品牌。车身提供双色车漆涂装，匹配 20 英寸饼形轮圈。车辆后方融入扰流板提升运动感。车辆内饰以“阅览山河万象”为设计内核，大面积采用 Nappa 真皮包覆，搭配有百年山水纹影木饰板与“观山河”发光面板。智能化方面，该车搭载华为干昆智驾 ADS，并支持四分区语音识别。车辆后排配备双“鸿羽青云”零重力航空座椅，支持电动调节和 SPA 级理疗按摩，可一键开启“山河云榻”舒展模式，实现最大 166° 太空躺角，" data-title="罗伦士梦想家山河四座高顶版 MPV 上市，80.99 万元起" data-date="10-09 15:49" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 15:49</span>
          <span class="news-item-title">罗伦士梦想家山河四座高顶版 MPV 上市，80.99 万元起</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，改装商“罗伦士汽车”宣布旗下罗伦士梦想家山河四座高顶版上市，该车基于岚图梦想家山河四座版（售 70.99 万元）…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/995.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 9 日消息，洛图科技今日发布报告，2026 年 8 月，中国电子纸平板市场在线上全渠道平台的销量为 10.5 万台，同比上升 8.5%；销额为 1.5 亿元，同比下降 29.0%。从销量规模来看，当月市场克服了学习本的衰退影响，在经历了 16 个月的连续同比下降之后，终于迎来了正增长。今年 8 月，阅读器是市场增量的主要贡献品类，销量同比上升了 57.9%，在电子纸平板线上市场的内部分额由 2025 年同期的 52.9% 升至 77.0%；不过，市场均价降至了 989 元，这是阅读器线上均价近两年来首次跌至千元以下，其主要的影响因素为低价入门机型的增多和销售放量。与此同时，电子纸办公本的销量同比下降 4.4%；学习本更是同比大幅下降 90.4%，在市场内部的份额由 23." data-title="洛图科技：中国电子纸平板线上销量连跌 16 个月后首次上涨，阅读器撑大梁，学习本大降 9 成" data-date="10-09 15:46" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-09 15:46</span>
          <span class="news-item-title">洛图科技：中国电子纸平板线上销量连跌 16 个月后首次上涨，阅读器撑大梁，学习本大降 9 成</span>
          <span class="news-value-point">💡 IT之家 10 月 9 日消息，洛图科技今日发布报告，2026 年 8 月，中国电子纸平板市场在线上全渠道平台的销量为 10.5 万台，同比上升…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmvg9pgg4keyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="弗里德金集团（ Friedkin Group ）的埃弗顿（ Everton ）老板正在探索在接管俱乐部后不到两年的时间内出售俱乐部。" data-title="Everton owners consider selling club two years after takeover" data-date="10-09 15:46" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 15:46</span>
          <span class="news-item-title">埃弗顿业主考虑在收购两年后出售俱乐部</span>
          <span class="news-item-title-en">Everton owners consider selling club two years after takeover</span>
          <span class="news-value-point">💡 弗里德金集团（ Friedkin Group ）的埃弗顿（ Everton ）老板正在探索在接管俱乐部后不到两年的时间内出售俱乐部</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709642.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="江西于都，中央红军长征集结出发地。一支名叫“长征”的消防救援站自1965年扎根于此，一代代消防员全力守护着这里的万家灯火，他们的愿望是“当别人眼中的光”。" data-title="在长征出发地，那道光永远闪耀" data-date="10-09 15:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:28</span>
          <span class="news-item-title">在长征出发地，那道光永远闪耀</span>
          <span class="news-value-point">💡 江西于都，中央红军长征集结出发地</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1008581/microsoft-365-family-premium-shared-ai-features-storage-changes" target="_blank" rel="noopener" data-cat="zonghe" data-summary="去年，微软将其基于AI的Office功能捆绑到Microsoft 365个人和家庭订阅中，但它只允许主要帐户持有人访问AI福利。现在， Microsoft即将让Microsoft 365家庭版和高级版" data-title="Microsoft 365 Family subscribers will finally be able to share AI benefits" data-date="10-09 15:14" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-09 15:14</span>
          <span class="news-item-title">Microsoft 365家庭版订阅者最终将能够分享人工智能的好处</span>
          <span class="news-item-title-en">Microsoft 365 Family subscribers will finally be able to share AI benefits</span>
          <span class="news-value-point">💡 去年，微软将其基于AI的Office功能捆绑到Microsoft 365个人和家庭订阅中，但它只允许主要帐户持有人访问AI福利</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709629.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2026年10月9日，山西省原平市人民法院依法对潘当仁等41名被告人犯重大责任事故罪、不报安全事故罪、行贿罪一案一审公开宣判。" data-title="山西代县精诚矿业重大责任事故案一审宣判" data-date="10-09 15:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 15:05</span>
          <span class="news-item-title">山西代县精诚矿业重大责任事故案一审宣判</span>
          <span class="news-value-point">💡 2026年10月9日，山西省原平市人民法院依法对潘当仁等41名被告人犯重大责任事故罪、不报安全事故罪、行贿罪一案一审公开宣判</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709612.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆10月9日电 (记者 刘相琳)记者9日从重庆市公安局九龙坡区分局获悉，公安机关依法查处一起袭警案件，嫌疑人毛某被依法刑事拘留。" data-title="男子醉酒后辱骂击打民警被重庆警方刑事拘留" data-date="10-09 14:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 14:57</span>
          <span class="news-item-title">男子醉酒后辱骂击打民警被重庆警方刑事拘留</span>
          <span class="news-value-point">💡 中新网重庆10月9日电 (记者 刘相琳)记者9日从重庆市公安局九龙坡区分局获悉，公安机关依法查处一起袭警案件，嫌疑人毛某被依法刑事拘留</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709624.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法治在线丨外卖小哥拦凶、七旬奶奶救人 致敬身边的英雄" data-title="外卖小哥拦凶、七旬奶奶救人 致敬身边的英雄" data-date="10-09 14:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 14:48</span>
          <span class="news-item-title">外卖小哥拦凶、七旬奶奶救人 致敬身边的英雄</span>
          <span class="news-value-point">💡 法治在线丨外卖小哥拦凶、七旬奶奶救人 致敬身边的英雄</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-09/10709599.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社武汉10月9日电 (马芙蓉 黄双子)记者9日从华中科技大学获悉，该校联合北京大学、中国科学院高能物理研究所等机构，首次从大尺度环境和暗物质晕质量演化角度，揭示了宇宙早期“小红点”消失之谜。" data-title="中国科研团队揭示宇宙早期“小红点”消失之谜" data-date="10-09 14:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-09 14:46</span>
          <span class="news-item-title">中国科研团队揭示宇宙早期“小红点”消失之谜</span>
          <span class="news-value-point">💡 中新社武汉10月9日电 (马芙蓉 黄双子)记者9日从华中科技大学获悉，该校联合北京大学、中国科学院高能物理研究所等机构，首次从大尺度环境和暗物质…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-09 16:05（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
