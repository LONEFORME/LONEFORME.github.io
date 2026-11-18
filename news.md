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
      <span>2026-11-18 17:21 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×19 · 天空体育×17</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-18/10734214.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月18日电(记者马卓言、赵瀚泽)11月18日下午，国家主席习近平在深圳宝安国际机场迎接来华出席亚太经合组织领导人非正式会议的美国总统特朗普。" data-title="习近平迎接美国总统特朗普" data-date="11-18 17:12" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-18 17:12</span>
      </div>
      <h2 class="hero-featured-title">习近平迎接美国总统特朗普</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/028/914.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，腾讯今日发布 2026 年第三季度财报，截至 11 月初，WorkBuddy 日活跃用户数超过 1000 万，日均 Token 调用量超过 100 万亿，成为中国大语言模型日均 Token 用量最高的 AI 产品。官方表示，自今年 3 月发布以来，WorkBuddy 已完成 100 多个大版本更新。开放平台上线两个月以来，Buddy 应用已覆盖 55 个专业场景、超 30 个垂直领域，包括金融、法律、医疗、教育、公益、设计、SaaS 等。IT之家获悉，目前 WorkBuddy 企业版已落地 50 多个行业，覆盖中国企业 500 强中的 50%。模型方面，Hy4 flash 上线首日 Token 调用量已突破 50 万亿，创混元系列模型首日调用量新高，并登顶" data-title="腾讯 WorkBuddy 日活跃用户数超 1000 万，成为中国大语言模型日均 Token 用量最高 AI 产品" data-date="11-18 16:52" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">腾讯 WorkBuddy 日活跃用户数超 1000 万，成为中国大语言模型日均 Token 用量最高 AI 产品</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Gunners on a contract roll" data-title="Arsenal latest: Gunners on a contract roll" data-date="11-18 17:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">阿森纳最新消息：枪手续约势头正盛</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-18/10734209.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网台州11月18日电(张益聪)“再见，花街！”近日，浙江台州临海“老食客”心目中承载着烟火记忆的花街小吃夜市，将迁至靖鹰广场靖江里夜市。消息一出，不少民众、游客心生感慨，故地重游。一座小城，缘何如此有人情味和烟火气？" data-title="浙江临海“小城故事”：何以让青年创业“不烧心”" data-date="11-18 17:12" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">浙江临海“小城故事”：何以让青年创业“不烧心”</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734214.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月18日电(记者马卓言、赵瀚泽)11月18日下午，国家主席习近平在深圳宝安国际机场迎接来华出席亚太经合组织领导人非正式会议的美国总统特朗普。" data-title="习近平迎接美国总统特朗普" data-date="11-18 17:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:12</span>
          <span class="news-item-title">习近平迎接美国总统特朗普</span>
          <span class="news-value-point">💡 新华社深圳11月18日电(记者马卓言、赵瀚泽)11月18日下午，国家主席习近平在深圳宝安国际机场迎接来华出席亚太经合组织领导人非正式会议的美国总…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734175.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月18日电 (记者 王梦瑶)中国邮政18日发行《亚太经合组织第三十三次领导人非正式会议》纪念邮票一套1枚。中国集邮有限公司配合邮票发行，同步推出首日封、邮戳卡、护邮卡和版票折等系列邮品。" data-title="（深圳APEC）《亚太经合组织第三十三次领导人非正式会议》纪念邮票发行" data-date="11-18 17:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:06</span>
          <span class="news-item-title">（深圳APEC）《亚太经合组织第三十三次领导人非正式会议》纪念邮票发行</span>
          <span class="news-value-point">💡 中新社北京11月18日电 (记者 王梦瑶)中国邮政18日发行《亚太经合组织第三十三次领导人非正式会议》纪念邮票一套1枚</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734161.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月18日电 (记者 张杨彬 张晓曦)国务院台办例行新闻发布会18日在北京举行，发言人陈斌华就台湾各界人士发出“两岸和平倡议”、台湾音乐人罗大佑批评民进党当局钳制言论等近期热点回答记者提问。" data-title="国台办发布会回应“两岸和平倡议”、罗大佑发声等热点" data-date="11-18 16:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 16:58</span>
          <span class="news-item-title">国台办发布会回应“两岸和平倡议”、罗大佑发声等热点</span>
          <span class="news-value-point">💡 中新社北京11月18日电 (记者 张杨彬 张晓曦)国务院台办例行新闻发布会18日在北京举行，发言人陈斌华就台湾各界人士发出“两岸和平倡议”、台湾…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734198.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="本周，亚太经合组织(APEC)第三十三次领导人非正式会议将在深圳举行，世界进入“中国时间”。" data-title="日月谭天丨这场举世瞩目的盛会再次让岛内震撼！" data-date="11-18 16:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 16:54</span>
          <span class="news-item-title">日月谭天丨这场举世瞩目的盛会再次让岛内震撼！</span>
          <span class="news-value-point">💡 本周，亚太经合组织(APEC)第三十三次领导人非正式会议将在深圳举行，世界进入“中国时间”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734188.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="解放日报 安峥" data-title="APEC“全”观察 | 中国第三次主办APEC，海外舆论聚焦哪三件事？" data-date="11-18 16:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 16:50</span>
          <span class="news-item-title">APEC“全”观察 | 中国第三次主办APEC，海外舆论聚焦哪三件事？</span>
          <span class="news-value-point">💡 解放日报 安峥</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734179.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中青报·中青网记者 赵婷婷" data-title="亚太青年眼中的APEC“中国年”" data-date="11-18 16:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 16:48</span>
          <span class="news-item-title">亚太青年眼中的APEC“中国年”</span>
          <span class="news-value-point">💡 中青报·中青网记者 赵婷婷</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/world/asia/trump-marcos-philippines-fried-chicken-jollibee.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在马尼拉接待特朗普总统的东道主为这位美国领导人向菲律宾快餐连锁店Jollibee下了深夜订单。" data-title="Trump and Marcos Share a Moment Over Jollibee Fried Chicken" data-date="11-18 16:34" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 16:34</span>
          <span class="news-item-title">特朗普和马科斯一起享用快乐蜂炸鸡</span>
          <span class="news-item-title-en">Trump and Marcos Share a Moment Over Jollibee Fried Chicken</span>
          <span class="news-value-point">💡 在马尼拉接待特朗普总统的东道主为这位美国领导人向菲律宾快餐连锁店Jollibee下了深夜订单</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqn0dy4ppxp7o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="麒麟山庄离APEC主会场约30分钟车程，三面环山、一面临水，封闭性和安保条件都很好。它也与习近平的父亲习仲勋有渊源，还接待过已故朝鲜领导人金正日。" data-title="美中俄峰会：为何选在深圳麒麟山庄？习仲勋、金正日都曾下榻" data-date="11-18 16:06" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 16:06</span>
          <span class="news-item-title">美中俄峰会：为何选在深圳麒麟山庄？习仲勋、金正日都曾下榻</span>
          <span class="news-value-point">💡 麒麟山庄离APEC主会场约30分钟车程，三面环山、一面临水，封闭性和安保条件都很好</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/us/politics/alaska-senate-sullivan-peltola.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="玛丽·佩尔托拉击败了连任两届的参议员丹·S·沙利文，成为自2015年以来首位代表该保守派州进入参议院的民主党人。" data-title="Democrats Claim 56 Senate Seats After Mary Peltola Wins in Alaska" data-date="11-18 15:43" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 15:43</span>
          <span class="news-item-title">随着玛丽·佩尔托拉在阿拉斯加州获胜，民主党人已拿下56个参议院席位</span>
          <span class="news-item-title-en">Democrats Claim 56 Senate Seats After Mary Peltola Wins in Alaska</span>
          <span class="news-value-point">💡 玛丽·佩尔托拉击败了连任两届的参议员丹·S·沙利文，成为自2015年以来首位代表该保守派州进入参议院的民主党人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734071.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月18日电 据伊朗媒体18日报道，伊朗军方表示，其动用无人机对美军在科威特的阿里·萨利姆空军基地进行了打击。" data-title="伊朗打击美军基地" data-date="11-18 15:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 15:08</span>
          <span class="news-item-title">伊朗打击美军基地</span>
          <span class="news-value-point">💡 中新网11月18日电 据伊朗媒体18日报道，伊朗军方表示，其动用无人机对美军在科威特的阿里·萨利姆空军基地进行了打击</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734089.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月18日电 据《印度快报》报道，印度外交部17日对一艘悬挂巴拿马国旗的液化石油气运输船16日在霍尔木兹海峡遭袭一事予以谴责。船上24名印度籍人员中，21人已安全撤至阿曼海塞卜，2名船员受伤入院，另有1人失踪。" data-title="霍尔木兹海峡船只遇袭致1名印度籍船员失踪 印度外交部予以谴责" data-date="11-18 14:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 14:55</span>
          <span class="news-item-title">霍尔木兹海峡船只遇袭致1名印度籍船员失踪 印度外交部予以谴责</span>
          <span class="news-value-point">💡 中新网11月18日电 据《印度快报》报道，印度外交部17日对一艘悬挂巴拿马国旗的液化石油气运输船16日在霍尔木兹海峡遭袭一事予以谴责</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734017.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月18日电 布宜诺斯艾利斯消息：阿根廷外交部当地时间17日发表声明，抗议英国安妮公主在马尔维纳斯群岛(简称马岛，英国称福克兰群岛)和南乔治亚岛开展官方访问。" data-title="阿根廷抗议英国安妮公主在马岛等地开展官方访问" data-date="11-18 14:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 14:18</span>
          <span class="news-item-title">阿根廷抗议英国安妮公主在马岛等地开展官方访问</span>
          <span class="news-value-point">💡 中新网北京11月18日电 布宜诺斯艾利斯消息：阿根廷外交部当地时间17日发表声明，抗议英国安妮公主在马尔维纳斯群岛(简称马岛，英国称福克兰群岛)…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10733996.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月18日电 综合报道，11月17日，智利总统卡斯特抵达中国深圳。当天，卡斯特在社交媒体X上发文称，“智利和中国之间有着兄弟般的情谊和相互尊重的历史关系，更重要的是，两国拥有共同发展、共同繁荣的未来。”" data-title="智利总统来华之际发文：智利和中国之间有着“兄弟般的情谊”" data-date="11-18 12:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 12:42</span>
          <span class="news-item-title">智利总统来华之际发文：智利和中国之间有着“兄弟般的情谊”</span>
          <span class="news-value-point">💡 中新网11月18日电 综合报道，11月17日，智利总统卡斯特抵达中国深圳</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10733995.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月18日电 据俄罗斯卫星通讯社当地时间18日报道，俄罗斯总统普京感谢中方出色主办APEC会议。" data-title="俄媒：普京感谢中方出色主办APEC会议" data-date="11-18 12:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 12:40</span>
          <span class="news-item-title">俄媒：普京感谢中方出色主办APEC会议</span>
          <span class="news-value-point">💡 中新网11月18日电 据俄罗斯卫星通讯社当地时间18日报道，俄罗斯总统普京感谢中方出色主办APEC会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10733993.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月18日电 11月18日凌晨，俄罗斯总统普京乘专机抵达深圳。18日上午，普京在深圳前海国际会议中心出席2026年亚太经合组织工商领导人峰会开幕式，并发表讲话。" data-title="普京APEC发表讲话点赞深圳：“充满活力、蓬勃发展，令人印象深刻”" data-date="11-18 12:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 12:39</span>
          <span class="news-item-title">普京APEC发表讲话点赞深圳：“充满活力、蓬勃发展，令人印象深刻”</span>
          <span class="news-value-point">💡 中新网11月18日电 11月18日凌晨，俄罗斯总统普京乘专机抵达深圳</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/028/914.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，腾讯今日发布 2026 年第三季度财报，截至 11 月初，WorkBuddy 日活跃用户数超过 1000 万，日均 Token 调用量超过 100 万亿，成为中国大语言模型日均 Token 用量最高的 AI 产品。官方表示，自今年 3 月发布以来，WorkBuddy 已完成 100 多个大版本更新。开放平台上线两个月以来，Buddy 应用已覆盖 55 个专业场景、超 30 个垂直领域，包括金融、法律、医疗、教育、公益、设计、SaaS 等。IT之家获悉，目前 WorkBuddy 企业版已落地 50 多个行业，覆盖中国企业 500 强中的 50%。模型方面，Hy4 flash 上线首日 Token 调用量已突破 50 万亿，创混元系列模型首日调用量新高，并登顶" data-title="腾讯 WorkBuddy 日活跃用户数超 1000 万，成为中国大语言模型日均 Token 用量最高 AI 产品" data-date="11-18 16:52" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 16:52</span>
          <span class="news-item-title">腾讯 WorkBuddy 日活跃用户数超 1000 万，成为中国大语言模型日均 Token 用量最高 AI 产品</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，腾讯今日发布 2026 年第三季度财报，截至 11 月初，WorkBuddy 日活跃用户数超过 1000 万，…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/913.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，华为官方今日继续揭秘首款“逻辑折叠”技术 τ 芯片 —— 麒麟 9050 系列更多配置信息，今日最新公开了新一代芯片级安全架构的情报。据介绍，麒麟 9050 系列芯片是首批获权威检测的抗量子攻击移动 SoC，也是首个芯片级隐私安全平台，支持 MSP 安全处理器与 eSE 安全芯片双芯协同，并获 CCRC EAL5+ 安全认证。IT之家了解到，麒麟 9050 系列进一步增强了芯片级安全能力，支持后量子密码相关安全功能；此外，它还是首个芯片级隐私安全 SoC 平台，通过移动安全处理器与独立安全芯片协同，可为启动安全、数据安全、隐私保护和通信安全提供底层支撑。值得一提的是，下一代麒麟 2027 芯片已经就绪。华为半导体业务无线终端芯片产品管理部部长徐松余表示，到目" data-title="华为麒麟 9050 系列新一代芯片级安全架构公开：双芯协同，首批获权威检测的抗量子攻击移动 SoC" data-date="11-18 16:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 16:46</span>
          <span class="news-item-title">华为麒麟 9050 系列新一代芯片级安全架构公开：双芯协同，首批获权威检测的抗量子攻击移动 SoC</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，华为官方今日继续揭秘首款“逻辑折叠”技术 τ 芯片 —— 麒麟 9050 系列更多配置信息，今日最新公开了新一…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/912.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，据路透社报道，英伟达（Nvidia）为公司高管和董事购买了保险，以应对证券诉讼可能带来的个人责任风险，但公司自身却没有购买相应保险。这意味着，如果围绕黄仁勋突然辞去 CEO 职务而引发的诉讼最终胜诉，英伟达可能不得不动用现金储备承担相关赔偿。The Insurer 上周六报道称，英伟达为公司高管和董事购买的保险，最高赔付额度达到 9.5 亿美元（IT之家注：现汇率约合 63.46 亿元人民币）。不过，英伟达并未购买通常用于承担公司在证券诉讼中辩护费用、和解金及法院判决赔偿金的企业责任保险。这意味着，如果英伟达董事或高管因未能妥善履行公司监督职责而承担个人法律责任，保险公司可以根据保单条款，支付英伟达无法代为承担的合规和解金或判决赔偿，从而保护相关人员的个人资" data-title="黄仁勋离职风波引发诉讼风险：英伟达高管有保险，公司自身却未投保" data-date="11-18 16:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 16:43</span>
          <span class="news-item-title">黄仁勋离职风波引发诉讼风险：英伟达高管有保险，公司自身却未投保</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，据路透社报道，英伟达（Nvidia）为公司高管和董事购买了保险，以应对证券诉讼可能带来的个人责任风险，但公司自…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/909.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，据《商业内幕》报道，对于黄仁勋离开英伟达会给公司业务带来多大影响，新兴云服务商（或称“新云服务商”） CoreWeave 的 CEO 迈克尔 · 因特拉托尔似乎并不担心。当地时间 17 日，在 Semafor 举办的“硅谷与世界”活动上，因特拉托尔谈及双方的合作关系时显得相当淡定。他认为，英伟达是一家了不起的公司，拥有成千上万名优秀的工程师和员工，这些人仍会与 CoreWeave 保持合作，“每天都有数千名英伟达员工与 CoreWeave 团队协作，处理设备部署、数据中心建设、基础设施网络搭建等工作。这些合作都会继续下去。”主持人接着问，黄仁勋离开英伟达后，CoreWeave 在为数据中心基础设施寻求融资时，是否会感受到他的缺席带来的影响，哪怕只是心理层面的" data-title="CoreWeave CEO 因特拉托尔：黄仁勋离开英伟达，我不担心会影响业务" data-date="11-18 16:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 16:28</span>
          <span class="news-item-title">CoreWeave CEO 因特拉托尔：黄仁勋离开英伟达，我不担心会影响业务</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，据《商业内幕》报道，对于黄仁勋离开英伟达会给公司业务带来多大影响，新兴云服务商（或称“新云服务商”） Core…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/908.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，黄仁勋突然离职后，许多玩家担心，失去黄仁勋掌舵的英伟达可能会进一步向 AI 业务倾斜，而牺牲游戏显卡业务。爆料人士 Moore&#39;s Law Is Dead（以下简称 MLID）最新披露的一则消息，似乎印证了玩家的担忧：黄仁勋此前曾希望推出一款高端 RTX 5080 显卡，作为给游戏玩家的“安慰”，以弥补 RTX 5090 价格过高、普通玩家难以负担的问题。MLID 在 YouTube 最新一期《Broken Silicon》播客节目中透露了这一消息，他讨论了近期有关 RTX 5080 24GB 显卡可能取消的传闻。据称，由于 GDDR7 显存芯片价格高昂，这款显卡的推出计划可能已经搁浅。MLID 援引一位英伟达内部消息人士的说法称，RTX 5080 24GB" data-title="消息称黄仁勋曾力推 RTX 5080 24GB 显卡安抚游戏玩家，如今英伟达或将其取消" data-date="11-18 16:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 16:27</span>
          <span class="news-item-title">消息称黄仁勋曾力推 RTX 5080 24GB 显卡安抚游戏玩家，如今英伟达或将其取消</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，黄仁勋突然离职后，许多玩家担心，失去黄仁勋掌舵的英伟达可能会进一步向 AI 业务倾斜，而牺牲游戏显卡业务</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510916.html" target="_blank" rel="noopener" data-cat="keji" data-summary="近日，全球首个医疗健康 AI 独立评测与分析平台InclusionMed 正式上线" data-title="全球首个医疗健康AI独立评测与分析平台InclusionMed正式上线" data-date="11-18 15:24" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-18 15:24</span>
          <span class="news-item-title">全球首个医疗健康AI独立评测与分析平台InclusionMed正式上线</span>
          <span class="news-value-point">💡 近日，全球首个医疗健康 AI 独立评测与分析平台InclusionMed 正式上线</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510821.html" target="_blank" rel="noopener" data-cat="keji" data-summary="具身全栈玩家" data-title="英伟达AMD首次联手押注！Genesis完成A轮融资，估值超230亿" data-date="11-18 12:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-18 12:28</span>
          <span class="news-item-title">英伟达AMD首次联手押注！Genesis完成A轮融资，估值超230亿</span>
          <span class="news-value-point">💡 具身全栈玩家</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/nvidias-startup-stakes-ballooned-to-65b-but-huangs-exit-puts-future-deals-in-doubt/" target="_blank" rel="noopener" data-cat="keji" data-summary="在过去九个月里，英伟达的私募投资价值几乎翻了两番，这得益于黄仁勋激进的交易策略以及其现有投资组合公司的估值不断攀升。" data-title="Nvidia’s startup stakes ballooned to $65B, but Huang’s exit puts future  deals in doubt" data-date="11-18 09:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 09:44</span>
          <span class="news-item-title">英伟达的初创企业投资额飙升至650亿美元，但黄仁勋的退出使未来的交易蒙上阴影</span>
          <span class="news-item-title-en">Nvidia’s startup stakes ballooned to $65B, but Huang’s exit puts future  deals in doubt</span>
          <span class="news-value-point">💡 在过去九个月里，英伟达的私募投资价值几乎翻了两番，这得益于黄仁勋激进的交易策略以及其现有投资组合公司的估值不断攀升</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510726.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达公布了老黄离职后的首份财报" data-title="黄仁勋不再沉默：我愿重掌英伟达！董事会：不考虑" data-date="11-18 09:03" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-18 09:03</span>
          <span class="news-item-title">黄仁勋不再沉默：我愿重掌英伟达！董事会：不考虑</span>
          <span class="news-value-point">💡 英伟达公布了老黄离职后的首份财报</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/510707.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Sol逼近旗舰性能" data-title="GPT-6.2 Astra和Sol王炸双发！3D又危了" data-date="11-18 08:49" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-18 08:49</span>
          <span class="news-item-title">GPT-6.2 Astra和Sol王炸双发！3D又危了</span>
          <span class="news-value-point">💡 Sol逼近旗舰性能</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/nvidia-promises-that-revenue-will-keep-soaring-for-now/" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管在声名狼藉的创始人兼首席执行官黄仁勋离职后，Nvidia 陷入了动荡，但该公司预计其创纪录的营收势头不会就此止步。" data-title="Nvidia promises that revenue will keep soaring" data-date="11-18 08:16" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 08:16</span>
          <span class="news-item-title">英伟达承诺收入将持续飙升</span>
          <span class="news-item-title-en">Nvidia promises that revenue will keep soaring</span>
          <span class="news-value-point">💡 尽管在声名狼藉的创始人兼首席执行官黄仁勋离职后，Nvidia 陷入了动荡，但该公司预计其创纪录的营收势头不会就此止步</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1036111/satya-nadella-says-hes-agi-pilled-now" target="_blank" rel="noopener" data-cat="keji" data-summary="微软首席执行官萨蒂亚·纳德拉表示，他相信AGI，至少在谈到人工智能可能会对经济结构带来惊人变化以及政治可能会因此而发生变化时，他相信AGI。“我之所以相信AGI，是因为在经济层面，" data-title="Satya Nadella says he’s AGI" data-date="11-18 07:41" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 07:41</span>
          <span class="news-item-title">萨蒂亚·纳德拉表示，他是AGI</span>
          <span class="news-item-title-en">Satya Nadella says he’s AGI</span>
          <span class="news-value-point">💡 微软首席执行官萨蒂亚·纳德拉表示，他相信AGI，至少在谈到人工智能可能会对经济结构带来惊人变化以及政治可能会因此而发生变化时，他相信AGI</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达的临时首席执行官表示，该公司已停止向中国销售芯片。这会造成多大损失？" data-title="Nvidia is abandoning China after Jensen Huang’s ouster" data-date="11-18 07:37" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 07:37</span>
          <span class="news-item-title">在黄仁勋被罢免后，英伟达正在放弃中国市场</span>
          <span class="news-item-title-en">Nvidia is abandoning China after Jensen Huang’s ouster</span>
          <span class="news-value-point">💡 英伟达的临时首席执行官表示，该公司已停止向中国销售芯片</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huangs-exit/" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管黄仁勋突然离职，但英伟达的临时首席执行官重申了其开源人工智能战略，并计划收购Hugging Face。" data-title="Nvidia says its open source AI strategy remains intact after Jensen Huang’s exit" data-date="11-18 07:04" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 07:04</span>
          <span class="news-item-title">英伟达表示，在黄仁勋离任后，其开源人工智能战略仍将保持不变。</span>
          <span class="news-item-title-en">Nvidia says its open source AI strategy remains intact after Jensen Huang’s exit</span>
          <span class="news-value-point">💡 尽管黄仁勋突然离职，但英伟达的临时首席执行官重申了其开源人工智能战略，并计划收购Hugging Face</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/17/nvidia-says-it-doesnt-plan-to-reappoint-jensen-huang-as-ceo/" target="_blank" rel="noopener" data-cat="keji" data-summary="这位前首席执行官在上周辞职后提出要重返公司担任最高职位。" data-title="Nvidia says it doesn’t plan to reappoint Jensen Huang as CEO" data-date="11-18 06:42" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 06:42</span>
          <span class="news-item-title">英伟达表示不打算再次任命黄仁勋担任首席执行官</span>
          <span class="news-item-title-en">Nvidia says it doesn’t plan to reappoint Jensen Huang as CEO</span>
          <span class="news-value-point">💡 这位前首席执行官在上周辞职后提出要重返公司担任最高职位</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Gunners on a contract roll" data-title="Arsenal latest: Gunners on a contract roll" data-date="11-18 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 17:00</span>
          <span class="news-item-title">阿森纳最新消息：枪手续约势头正盛</span>
          <span class="news-item-title-en">Arsenal latest: Gunners on a contract roll</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/18/premier-league-teams-full-backs-opta-analyst" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="近年来，边后卫的角色发生了巨大变化。我们分析了所有20支球队如何看待这一位置。文：Opta分析师重叠。内切。边卫内收。传统。边后卫的角色发生了巨大变化。曾经是防守型球员" data-title="Overlap, underlap or sit back? How Premier League teams use their full" data-date="11-18 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-18 16:00</span>
          <span class="news-item-title">是重叠、内切还是回撤？英超球队如何使用边后卫</span>
          <span class="news-item-title-en">Overlap, underlap or sit back? How Premier League teams use their full</span>
          <span class="news-value-point">💡 近年来，边后卫的角色发生了巨大变化</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Pochettino set for first day in charge" data-title="Man Utd latest: Pochettino set for first day in charge" data-date="11-18 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 15:00</span>
          <span class="news-item-title">曼联最新消息：波切蒂诺即将迎来执教首日</span>
          <span class="news-item-title-en">Man Utd latest: Pochettino set for first day in charge</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! Get your questions in for today&#39;s SSN transfer special!" data-title="Transfer Centre LIVE! Get your questions in for today&#39;s SSN transfer special!" data-date="11-18 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 15:00</span>
          <span class="news-item-title">转会中心直播！为今天的SSN转会特别节目提问吧！</span>
          <span class="news-item-title-en">Transfer Centre LIVE! Get your questions in for today's SSN transfer special!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/wales-vs-portugal/report/554136" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在切尔西的佩德罗·内托被罚下场后，威尔士在卡迪夫以 3-2 负于 10 人应战的葡萄牙，结束了欧洲国家联赛的小组赛征程。" data-title="Wales beaten by 10-man Portugal as Neto scores but is sent off" data-date="11-18 05:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 05:40</span>
          <span class="news-item-title">葡萄牙10人应战击败威尔士，内托进球但被罚下场</span>
          <span class="news-item-title-en">Wales beaten by 10-man Portugal as Neto scores but is sent off</span>
          <span class="news-value-point">💡 在切尔西的佩德罗·内托被罚下场后，威尔士在卡迪夫以 3-2 负于 10 人应战的葡萄牙，结束了欧洲国家联赛的小组赛征程</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqvg2e4208zmo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在准备可能转会至皇家马德里之际，小将加布里埃尔发布了告别信息，表示曼联将永远是他故事的一部分。" data-title="Madrid-bound Gabriel posts farewell Man Utd message" data-date="11-18 03:35" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 03:35</span>
          <span class="news-item-title">即将加盟皇马的加布里埃尔发布告别曼联的讯息</span>
          <span class="news-item-title-en">Madrid-bound Gabriel posts farewell Man Utd message</span>
          <span class="news-value-point">💡 在准备可能转会至皇家马德里之际，小将加布里埃尔发布了告别信息，表示曼联将永远是他故事的一部分</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/wales-vs-portugal/live/554136" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Wales and Portugal searching for fifth goal in thriller LIVE!" data-title="Wales and Portugal searching for fifth goal in thriller LIVE!" data-date="11-18 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 02:30</span>
          <span class="news-item-title">威尔士和葡萄牙在精彩的比赛中争夺第五个进球，正在直播！</span>
          <span class="news-item-title-en">Wales and Portugal searching for fifth goal in thriller LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613361/jj-gabriel-transfer-news-manchester-united-teenager-announces-departure-from-club-amid-real-madrid-agreement" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="JJ·加布里埃尔宣布他将离开曼联，并期待在皇家马德里开启他的“下一篇章”。" data-title="JJ Gabriel says goodbye to Man Utd with Real Madrid move close" data-date="11-18 02:29" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 02:29</span>
          <span class="news-item-title">随着皇马转会临近，J.J. 加布里埃尔与曼联告别</span>
          <span class="news-item-title-en">JJ Gabriel says goodbye to Man Utd with Real Madrid move close</span>
          <span class="news-value-point">💡 JJ·加布里埃尔宣布他将离开曼联，并期待在皇家马德里开启他的“下一篇章”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613361/jj-gabriel-transfer-news-manchester-united-teenager-announces-departure-from-club-amid-real-madrid-agreement" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="JJ·加布里埃尔宣布他将离开曼联，并期待在皇家马德里开启他的“下一篇章”。" data-title="JJ Gabriel says goodbye to Man Utd with Real Madrid move close" data-date="11-18 02:29" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 02:29</span>
          <span class="news-item-title">随着皇马转会临近，J.J. 加布里埃尔与曼联告别</span>
          <span class="news-item-title-en">JJ Gabriel says goodbye to Man Utd with Real Madrid move close</span>
          <span class="news-value-point">💡 JJ·加布里埃尔宣布他将离开曼联，并期待在皇家马德里开启他的“下一篇章”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613327/arsenal-transfer-news-david-raya-jurrien-timber-and-piero-hincapie-close-to-finalising-new-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同。" data-title="Arsenal close to new deals for Raya, Timber and Hincapie" data-date="11-18 00:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 00:23</span>
          <span class="news-item-title">阿森纳即将与拉亚、廷伯和欣卡皮埃达成新合同</span>
          <span class="news-item-title-en">Arsenal close to new deals for Raya, Timber and Hincapie</span>
          <span class="news-value-point">💡 阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613327/arsenal-transfer-news-david-raya-jurrien-timber-and-piero-hincapie-close-to-finalising-new-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同。" data-title="Arsenal close to new deals for Raya, Timber and Hincapie" data-date="11-18 00:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 00:23</span>
          <span class="news-item-title">阿森纳即将与拉亚、廷伯和欣卡皮埃达成新合同</span>
          <span class="news-item-title-en">Arsenal close to new deals for Raya, Timber and Hincapie</span>
          <span class="news-value-point">💡 阿森纳即将与大卫·拉亚、尤里恩·廷伯和皮耶罗·因卡皮埃敲定新合同</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613275/wayne-rooney-says-he-contemplated-suicide-during-lowest-point-of-manchester-united-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头。" data-title="Rooney contemplated suicide at ‘lowest point’ of Man Utd career" data-date="11-17 22:36" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 22:36</span>
          <span class="news-item-title">鲁尼在曼联生涯的“最低谷”曾有过自杀念头</span>
          <span class="news-item-title-en">Rooney contemplated suicide at ‘lowest point’ of Man Utd career</span>
          <span class="news-value-point">💡 韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613275/wayne-rooney-says-he-contemplated-suicide-during-lowest-point-of-manchester-united-career" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头。" data-title="Rooney contemplated suicide at ‘lowest point’ of Man Utd career" data-date="11-17 22:36" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 22:36</span>
          <span class="news-item-title">鲁尼在曼联生涯的“最低谷”曾有过自杀念头</span>
          <span class="news-item-title-en">Rooney contemplated suicide at ‘lowest point’ of Man Utd career</span>
          <span class="news-value-point">💡 韦恩·鲁尼透露，在他效力曼联的职业生涯中，曾有一段时间他有过自杀的念头</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6ge39lgyzzzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳正与后卫皮耶罗·因卡皮耶就新合同进行深入谈判。" data-title="Hincapie in advanced talks over new Arsenal deal" data-date="11-17 21:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 21:09</span>
          <span class="news-item-title">欣卡皮耶正在就与阿森纳的新合同进行深入谈判</span>
          <span class="news-item-title-en">Hincapie in advanced talks over new Arsenal deal</span>
          <span class="news-value-point">💡 阿森纳正与后卫皮耶罗·因卡皮耶就新合同进行深入谈判</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: Henderson says everyone responsible for creating right culture" data-title="Chelsea latest: Henderson says everyone responsible for creating right culture" data-date="11-17 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 20:00</span>
          <span class="news-item-title">切尔西最新消息：亨德森表示，每个人都有责任营造正确的文化氛围</span>
          <span class="news-item-title-en">Chelsea latest: Henderson says everyone responsible for creating right culture</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734209.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网台州11月18日电(张益聪)“再见，花街！”近日，浙江台州临海“老食客”心目中承载着烟火记忆的花街小吃夜市，将迁至靖鹰广场靖江里夜市。消息一出，不少民众、游客心生感慨，故地重游。一座小城，缘何如此有人情味和烟火气？" data-title="浙江临海“小城故事”：何以让青年创业“不烧心”" data-date="11-18 17:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:12</span>
          <span class="news-item-title">浙江临海“小城故事”：何以让青年创业“不烧心”</span>
          <span class="news-value-point">💡 中新网台州11月18日电(张益聪)“再见，花街</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734172.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福州11月18日电 (彭莉芳)中国红十字会18日在福建福州举行新闻发布会，揭晓第四届“全国十佳救护员”获评名单。两名因挽救他人生命而牺牲的施救者获评“特别致敬人选”。" data-title="第四届“全国十佳救护员”名单在福州发布" data-date="11-18 17:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:05</span>
          <span class="news-item-title">第四届“全国十佳救护员”名单在福州发布</span>
          <span class="news-value-point">💡 中新网福州11月18日电 (彭莉芳)中国红十字会18日在福建福州举行新闻发布会，揭晓第四届“全国十佳救护员”获评名单</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734168.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广西柳州11月18日电(韦莹芸 韦蒙玲 周晓玉)时下，广西柳州市柳江区三都镇油茶果陆续成熟，进入集中采摘期，饱满的油茶果缀满枝头，山间洋溢着丰收的气息。" data-title="（乡村行·看振兴）广西柳江油茶丰收 小果子成富民“金果子”" data-date="11-18 17:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:05</span>
          <span class="news-item-title">（乡村行·看振兴）广西柳江油茶丰收 小果子成富民“金果子”</span>
          <span class="news-value-point">💡 中新网广西柳州11月18日电(韦莹芸 韦蒙玲 周晓玉)时下，广西柳州市柳江区三都镇油茶果陆续成熟，进入集中采摘期，饱满的油茶果缀满枝头，山间洋溢…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734184.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网厦门11月18日电 (叶艺琳)由中国社会福利与养老服务协会发起并主办的第二届中国银龄合唱大会18日在厦门闽南大戏院开幕。来自全国各地的近2000名银龄歌者齐聚厦门，参加为期5天的合唱展演、合唱快闪、文化考察等活动，充分展现银龄群体正从“被照护者”转变为文化养老的参与者、创造者。" data-title="第二届中国银龄合唱大会在厦门开幕 探索“展演+研学”文化养老新模式" data-date="11-18 17:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:04</span>
          <span class="news-item-title">第二届中国银龄合唱大会在厦门开幕 探索“展演+研学”文化养老新模式</span>
          <span class="news-value-point">💡 中新网厦门11月18日电 (叶艺琳)由中国社会福利与养老服务协会发起并主办的第二届中国银龄合唱大会18日在厦门闽南大戏院开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734189.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网邵阳11月18日电 (刘剑平 吕伟铭 刘翼)“戴叔叔每个月都来看我，给我送生活费，还会陪我聊天，教我怎么保护自己。”11月17日，在湖南城步苗族自治县金树社区，看到戴方财上门走访，12岁的阳玲(化名)说道。每次上门，戴方财总要先问问她最近学习怎么样，聊聊学校里的趣事，再叮嘱几句生活中的注意事项。" data-title="把爱心种进苗乡山水间 湖南城步公益人的乡土公益路" data-date="11-18 17:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:01</span>
          <span class="news-item-title">把爱心种进苗乡山水间 湖南城步公益人的乡土公益路</span>
          <span class="news-value-point">💡 中新网邵阳11月18日电 (刘剑平 吕伟铭 刘翼)“戴叔叔每个月都来看我，给我送生活费，还会陪我聊天，教我怎么保护自己</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734192.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福建永安11月18日电 (黄中泉 廖金朋)近日，观鸟爱好者刘永生等鸟友在通往位于福建永安的天宝岩国家级自然保护区公路附近的农田里，意外邂逅了一只水鸟。经确认，这正是当地鸟友们心心念念许久的长嘴剑鸻。" data-title="长嘴剑鸻再现福建永安 南北迁徙记录终闭环" data-date="11-18 17:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 17:01</span>
          <span class="news-item-title">长嘴剑鸻再现福建永安 南北迁徙记录终闭环</span>
          <span class="news-value-point">💡 中新网福建永安11月18日电 (黄中泉 廖金朋)近日，观鸟爱好者刘永生等鸟友在通往位于福建永安的天宝岩国家级自然保护区公路附近的农田里，意外邂逅…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734164.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网湖北当阳11月18日电 (郭晓莹 陈昕)未来5年，湖北省当阳市将强化文旅赋能，打造更显特色的信义之城和具有海内外影响力的关公文化旅游目的地。这是记者18日从当阳市第十届人民代表大会第一次会议上获知的信息。" data-title="湖北当阳聚力打造关公文化旅游目的地" data-date="11-18 16:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 16:58</span>
          <span class="news-item-title">湖北当阳聚力打造关公文化旅游目的地</span>
          <span class="news-value-point">💡 中新网湖北当阳11月18日电 (郭晓莹 陈昕)未来5年，湖北省当阳市将强化文旅赋能，打造更显特色的信义之城和具有海内外影响力的关公文化旅游目的地</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13613489/cameron-bancroft-former-australia-batter-releases-explosive-statement-accusing-pat-cummins-and-bowlers-of-sandpaper-knowledge" target="_blank" rel="noopener" data-cat="zonghe" data-summary="尽管澳大利亚队长帕特·坎明斯（Pat Cummins）周五在新闻发布会上否认自己是同谋，但卡梅伦·班克罗夫特（Cameron Bancroft）仍直接指控坎明斯知晓2018年对阵南非时使用砂纸一事。" data-title="&#39;It was cheating&#39; - Bancroft accuses Cummins of sandpaper knowledge" data-date="11-18 16:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 16:40</span>
          <span class="news-item-title">“这是作弊”——班克罗夫特指责卡明斯知道砂纸一事</span>
          <span class="news-item-title-en">'It was cheating' - Bancroft accuses Cummins of sandpaper knowledge</span>
          <span class="news-value-point">💡 尽管澳大利亚队长帕特·坎明斯（Pat Cummins）周五在新闻发布会上否认自己是同谋，但卡梅伦·班克罗夫特（Cameron Bancroft）…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/906.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 18 日消息，奇妙工具箱 11 月 16 日数据显示，华为鸿蒙 HarmonyOS 操作系统装机量在当日 9:22 突破 1 亿台，达成又一里程碑时刻。IT之家注意到，华为开发者官网昨晚更新了存量设备 API 版本使用数量参考，截至 2026 年 11 月 15 日，HarmonyOS 7（API 26.0.0）的设备量占比已达 82.21%，较上一统计周期又出现大幅增长。最新 HarmonyOS 设备各 API 版本使用量占比如下（数据约 15 天进行一次更新，开发者可根据占比来为应用合理定义需要兼容的 API 版本）：HarmonyOS 版本API 版本设备量占比7.0.026.0.082.21%6.1.06.1.1(24)12.87%6.1.06.1.0(23)3." data-title="华为鸿蒙系统装机量被曝破亿后，HarmonyOS 7 设备占比突破 82%" data-date="11-18 16:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 16:26</span>
          <span class="news-item-title">华为鸿蒙系统装机量被曝破亿后，HarmonyOS 7 设备占比突破 82%</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，奇妙工具箱 11 月 16 日数据显示，华为鸿蒙 HarmonyOS 操作系统装机量在当日 9:22 突破 1…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5y4jmvxr9vyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国时隔26年失去麻疹消除状态，今年病例达5400例、死亡10人，创1990年代以来新高。“疫苗怀疑论”持续遭到质疑。" data-title="美国今年已10人死于麻疹 26年后失去“麻疹消除状态”" data-date="11-18 16:16" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 16:16</span>
          <span class="news-item-title">美国今年已10人死于麻疹 26年后失去“麻疹消除状态”</span>
          <span class="news-value-point">💡 美国时隔26年失去麻疹消除状态，今年病例达5400例、死亡10人，创1990年代以来新高</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/live-blog/12040/13612700/australia-vs-england-third-odi-live-latest-cricket-score-and-updates-as-harry-brooks-side-face-mitch-marshs-team-in-series-decider-at-hobart" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Australia&#39;s Renshaw out after twice being dropped as England strike LIVE!" data-title="Australia&#39;s Renshaw out after twice being dropped as England strike LIVE!" data-date="11-18 14:58" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 14:58</span>
          <span class="news-item-title">澳大利亚的伦肖在被英格兰队两次漏接后出局，直播中！</span>
          <span class="news-item-title-en">Australia's Renshaw out after twice being dropped as England strike LIVE!</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/world/asia/tech-outages-cyberattack-hack-rubio.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国务卿马可·鲁比奥（Marco Rubio）表示，由于人工智能揭示了系统的漏洞，人们急于修补这些系统，这可能是最近空中交通管制、银行和政府机构出现故障的原因。" data-title="Rubio Says Rush to Secure Systems May Be Causing Failures" data-date="11-18 14:46" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 14:46</span>
          <span class="news-item-title">鲁比奥表示，仓促部署安全系统可能会导致故障</span>
          <span class="news-item-title-en">Rubio Says Rush to Secure Systems May Be Causing Failures</span>
          <span class="news-value-point">💡 国务卿马可·鲁比奥（Marco Rubio）表示，由于人工智能揭示了系统的漏洞，人们急于修补这些系统，这可能是最近空中交通管制、银行和政府机构出…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13613446/sandpapergate-usman-khawaja-and-david-warner-question-cricket-australias-new-forum-following-explosive-fallout" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乌斯曼·卡瓦贾（Usman Khawaja）和戴维·华纳（David Warner）对澳大利亚板球协会（Cricket Australia）设立独立论坛以调查“砂纸门”丑闻的决定提出质疑。" data-title="Khawaja and Warner question Cricket Australia’s new Sandpapergate forum" data-date="11-18 14:19" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 14:19</span>
          <span class="news-item-title">哈瓦加和华纳对澳大利亚板球协会的新“砂纸门”听证会提出质疑</span>
          <span class="news-item-title-en">Khawaja and Warner question Cricket Australia’s new Sandpapergate forum</span>
          <span class="news-value-point">💡 乌斯曼·卡瓦贾（Usman Khawaja）和戴维·华纳（David Warner）对澳大利亚板球协会（Cricket Australia）设立…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13612907/today-on-sky-sports-racing-supreme-hero-old-park-star-makes-chasing-debut-at-ffos-las" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，所有人的目光都将聚焦于弗斯拉斯赛马场，因为老园明星将首次在公众面前越过障碍，与他的顶级对手清醒荣耀一决高下。" data-title="Supreme hero Old Park Star makes chasing debut at Ffos Las" data-date="11-18 14:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 14:00</span>
          <span class="news-item-title">顶级英雄马Old Park Star在弗斯拉斯赛马场首次亮相追逐赛</span>
          <span class="news-item-title-en">Supreme hero Old Park Star makes chasing debut at Ffos Las</span>
          <span class="news-value-point">💡 今天，所有人的目光都将聚焦于弗斯拉斯赛马场，因为老园明星将首次在公众面前越过障碍，与他的顶级对手清醒荣耀一决高下</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13611983/las-vegas-gp-whats-still-to-play-for-over-final-three-races-of-f1-2026-season-with-battles-in-drivers-and-constructors-championships" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2026年F1赛季还剩三场比赛，本周末的拉斯维加斯大奖赛将拉开本赛季最后三连赛的帷幕。" data-title="What&#39;s still to play for in 2026 as F1 hits Vegas?" data-date="11-18 14:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 14:00</span>
          <span class="news-item-title">2026年F1进军拉斯维加斯，还有哪些看点？</span>
          <span class="news-item-title-en">What's still to play for in 2026 as F1 hits Vegas?</span>
          <span class="news-value-point">💡 2026年F1赛季还剩三场比赛，本周末的拉斯维加斯大奖赛将拉开本赛季最后三连赛的帷幕</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-18 17:21（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
