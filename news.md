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
      <span>2026-11-10 23:42 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/10/us/thomas-massie-impeachment-hegseth.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）在任期结束时退休，此前他输给了特朗普总统支持的主要挑战者。" data-title="What to Know About Thomas Massie, Leader of Drive to Impeach Hegseth" data-date="11-10 23:30" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-10 23:30</span>
      </div>
      <h2 class="hero-featured-title">关于弹劾赫格塞斯运动的领导者托马斯·马西（ Thomas Massie ）的须知</h2>
      <div class="hero-featured-title-en">What to Know About Thomas Massie, Leader of Drive to Impeach Hegseth</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/10/technology/anthropic-ipo-valuation-share-price.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这家人工智能公司的定价将使其成为有史以来规模最大的公开上市公司之一。它发生在市场动荡的时刻，投资者质疑人工智能繁荣的可持续性。" data-title="Anthropic Targets Valuation of Up to $1.4 Trillion for Blockbuster I.P.O." data-date="11-10 23:39" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Anthropic Targets Valuation of Up to $1.4 Trillion for Blockbuster I.P.O.</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13610675/man-utd-qa-michael-carrick-mauricio-pochettino-ineos-and-more-kaveh-solhekol-answers-your-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kaveh Solhekol已经回答了你关于曼联的最新问题，迈克尔·卡里克的未来在空中，俱乐部在降级区，还有更多的幕后问题。" data-title="Man Utd Q&amp;A: Carrick, Poch, INEOS and more answered" data-date="11-10 23:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Man Utd Q&A: Carrick, Poch, INEOS and more answered</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-10/10729864.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近期，社交平台上出现了一批内容为“取消外卖”“下架外卖”等话题的短视频，引发广泛关注。这些视频呈现出明显的模板化，且通常由多个账号在短期内批量生产，看似是个别餐饮商家的表态和呼吁，实则是深谙“情绪即流量”的MCN机构炮制的舆论噱头。" data-title="商家呼吁“取消外卖”？实为MCN制造对立、虚假摆拍引流" data-date="11-10 23:33" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">商家呼吁“取消外卖”？实为MCN制造对立、虚假摆拍引流</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/10/us/thomas-massie-impeachment-hegseth.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）在任期结束时退休，此前他输给了特朗普总统支持的主要挑战者。" data-title="What to Know About Thomas Massie, Leader of Drive to Impeach Hegseth" data-date="11-10 23:30" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 23:30</span>
          <span class="news-item-title">关于弹劾赫格塞斯运动的领导者托马斯·马西（ Thomas Massie ）的须知</span>
          <span class="news-item-title-en">What to Know About Thomas Massie, Leader of Drive to Impeach Hegseth</span>
          <span class="news-value-point">💡 肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）在任期结束时退休，此前他输给了特朗普总统支持的主要挑战者</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/10/us/politics/hegseth-impeachment-explainer-massie.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这些指控指责国防部长非法发动与伊朗的战争，指挥法外处决，无视旨在尽量减少平民伤亡的法律。" data-title="The Impeachment Charges Against Defense Secretary Pete Hegseth, Explained" data-date="11-10 23:09" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 23:09</span>
          <span class="news-item-title">针对国防部长皮特·赫格塞特的弹劾指控，解释</span>
          <span class="news-item-title-en">The Impeachment Charges Against Defense Secretary Pete Hegseth, Explained</span>
          <span class="news-value-point">💡 这些指控指责国防部长非法发动与伊朗的战争，指挥法外处决，无视旨在尽量减少平民伤亡的法律</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729850.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔11月10日电 (记者 金旭)当地时间10日，韩国总统李在明在总统府青瓦台主持召开国务会议，审议通过关于延长清海部队派遣期限的修订同意案。该议案将提交韩国国会履行同意程序。" data-title="韩国拟扩大派驻亚丁湾部队任务区域" data-date="11-10 22:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:10</span>
          <span class="news-item-title">韩国拟扩大派驻亚丁湾部队任务区域</span>
          <span class="news-value-point">💡 中新社首尔11月10日电 (记者 金旭)当地时间10日，韩国总统李在明在总统府青瓦台主持召开国务会议，审议通过关于延长清海部队派遣期限的修订同意…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729849.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社济南11月10日电 (周艺伟)据山东省地质矿产勘查开发局11月10日消息，日前投用的中国地矿领域首台全自动化钻机——ZJ50DB/XD70DB，将中国深部岩芯钻探的最大深度提升至7000米级。" data-title="中国深部岩芯钻探最大深度提升至7000米级" data-date="11-10 22:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:10</span>
          <span class="news-item-title">中国深部岩芯钻探最大深度提升至7000米级</span>
          <span class="news-value-point">💡 中新社济南11月10日电 (周艺伟)据山东省地质矿产勘查开发局11月10日消息，日前投用的中国地矿领域首台全自动化钻机——ZJ50DB/XD70…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729844.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网安塔利亚11月10日电(记者 王庆凯 魏园)当地时间11月10日，在土耳其安塔利亚举行的《联合国气候变化框架公约》第三十一次缔约方大会(COP31)中国角主题边会上，宁夏回族自治区生态环境厅宣传教育处处长王波分享了生态环境保护的宁夏探索实践。" data-title="中国首个实现沙漠化逆转的省区，如何做到？宁夏官员向世界分享生态保护经验" data-date="11-10 22:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:05</span>
          <span class="news-item-title">中国首个实现沙漠化逆转的省区，如何做到？宁夏官员向世界分享生态保护经验</span>
          <span class="news-value-point">💡 中新网安塔利亚11月10日电(记者 王庆凯 魏园)当地时间11月10日，在土耳其安塔利亚举行的《联合国气候变化框架公约》第三十一次缔约方大会(C…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729840.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社台北11月10日电 (记者 路梅)今年适逢孙中山先生诞辰160周年，中国国民党10日在位于台北的中央党部中山厅举办纪念座谈会。" data-title="中国国民党举办孙中山先生诞辰纪念座谈会" data-date="11-10 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:03</span>
          <span class="news-item-title">中国国民党举办孙中山先生诞辰纪念座谈会</span>
          <span class="news-value-point">💡 中新社台北11月10日电 (记者 路梅)今年适逢孙中山先生诞辰160周年，中国国民党10日在位于台北的中央党部中山厅举办纪念座谈会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729833.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月10日电 (阮煜琳蔡望田晶文)记者从中国海警局南海分局获悉，近期，中国海警局南海分局组织广东、广西、海南三省(区)海警力量开展集中打击走私行动，重点强化雷州半岛、琼州海峡管控，成效显著。" data-title="中国海警局南海分局集中打击走私查办案件21起" data-date="11-10 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:01</span>
          <span class="news-item-title">中国海警局南海分局集中打击走私查办案件21起</span>
          <span class="news-value-point">💡 中新网北京11月10日电 (阮煜琳蔡望田晶文)记者从中国海警局南海分局获悉，近期，中国海警局南海分局组织广东、广西、海南三省(区)海警力量开展集…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729838.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月10日电 11月10日，中共中央政治局委员、外交部长王毅应约同法国外长巴罗通电话。" data-title="王毅同法国外长巴罗通电话" data-date="11-10 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:01</span>
          <span class="news-item-title">王毅同法国外长巴罗通电话</span>
          <span class="news-value-point">💡 中新社北京11月10日电 11月10日，中共中央政治局委员、外交部长王毅应约同法国外长巴罗通电话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729842.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦11月10日电 (记者 欧阳开宇))英国卫生安全局(UKHSA)10日发布2026#8209;2027年冬季首个低温健康黄色警报，警报覆盖英格兰西北部及西米德兰兹地区，生效时间为当地11月12日上午9时至14日中午12时，英格兰其余地区暂不受影响。" data-title="英国发布今冬首个低温健康黄色警报" data-date="11-10 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">英国发布今冬首个低温健康黄色警报</span>
          <span class="news-value-point">💡 中新网伦敦11月10日电 (记者 欧阳开宇))英国卫生安全局(UKHSA)10日发布2026#8209;2027年冬季首个低温健康黄色警报，警报…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729841.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社东京11月10日电 据日本共同社报道，日本东京地方法院10日对强闯中国驻日本大使馆的日本自卫队官员村田晃大进行第二次公开庭审，日本检方建议判处其18个月监禁，辩方则请求判处罚金。判决将于12月24日作出。" data-title="日本检方寻求判处强闯中国使馆的自卫队官员18个月监禁" data-date="11-10 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 21:59</span>
          <span class="news-item-title">日本检方寻求判处强闯中国使馆的自卫队官员18个月监禁</span>
          <span class="news-value-point">💡 中新社东京11月10日电 据日本共同社报道，日本东京地方法院10日对强闯中国驻日本大使馆的日本自卫队官员村田晃大进行第二次公开庭审，日本检方建议…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729810.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网石家庄11月10日电(陈林 宋文浩)河北省政府新闻办10日举行河北省奋力推动“四好农村路”高质量发展新闻发布会。据通报，今年以来，河北建设改造农村公路5215.8公里，为全年任务的104.3%。" data-title="河北今年已建设改造农村公路5215.8公里" data-date="11-10 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 21:59</span>
          <span class="news-item-title">河北今年已建设改造农村公路5215.8公里</span>
          <span class="news-value-point">💡 中新网石家庄11月10日电(陈林 宋文浩)河北省政府新闻办10日举行河北省奋力推动“四好农村路”高质量发展新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729808.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月10日电 (记者 谢雁冰)以“深入学习贯彻党的二十届五中全会精神 持之以恒推进全面从严治党与纪检监察学科高质量发展”为主题，第三届纪检监察学科建设高端论坛11月8日在中国人民大学举办。" data-title="第三届纪检监察学科建设高端论坛在中国人民大学举办" data-date="11-10 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 21:59</span>
          <span class="news-item-title">第三届纪检监察学科建设高端论坛在中国人民大学举办</span>
          <span class="news-value-point">💡 中新网北京11月10日电 (记者 谢雁冰)以“深入学习贯彻党的二十届五中全会精神 持之以恒推进全面从严治党与纪检监察学科高质量发展”为主题，第三…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729799.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月10日电 全国政协主席王沪宁10日在京会见老挝建国阵线中央委员会副主席布沙迪。" data-title="王沪宁会见老挝建国阵线中央委员会副主席布沙迪" data-date="11-10 21:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 21:58</span>
          <span class="news-item-title">王沪宁会见老挝建国阵线中央委员会副主席布沙迪</span>
          <span class="news-value-point">💡 新华社北京11月10日电 全国政协主席王沪宁10日在京会见老挝建国阵线中央委员会副主席布沙迪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729809.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网金边11月10日电 (张堰林 张安琪 杨强)柬埔寨干拉省警察局当地时间10日通报称，干拉省克萨干丹县当天发生的运送学生车辆坠塘事故造成5名学生死亡、21人受伤。柬副首相兼教育、青年和体育部大臣韩春那洛当天前往医院探望受伤学生。" data-title="柬埔寨运送学生车辆坠塘事故致5死21伤 涉事司机被拘" data-date="11-10 21:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 21:55</span>
          <span class="news-item-title">柬埔寨运送学生车辆坠塘事故致5死21伤 涉事司机被拘</span>
          <span class="news-value-point">💡 中新网金边11月10日电 (张堰林 张安琪 杨强)柬埔寨干拉省警察局当地时间10日通报称，干拉省克萨干丹县当天发生的运送学生车辆坠塘事故造成5名…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729759.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦11月10日电 （记者 欧阳开宇）英国英格兰地区校园手机管理政策将进一步收紧，按照新版政府指导文件，自2027年9月起，中小学生在校全天都不能接触手机。" data-title="英格兰拟推新规中小学生在校全天不能接触手机" data-date="11-10 20:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 20:56</span>
          <span class="news-item-title">英格兰拟推新规中小学生在校全天不能接触手机</span>
          <span class="news-value-point">💡 中新网伦敦11月10日电 （记者 欧阳开宇）英国英格兰地区校园手机管理政策将进一步收紧，按照新版政府指导文件，自2027年9月起，中小学生在校全…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/10/technology/anthropic-ipo-valuation-share-price.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这家人工智能公司的定价将使其成为有史以来规模最大的公开上市公司之一。它发生在市场动荡的时刻，投资者质疑人工智能繁荣的可持续性。" data-title="Anthropic Targets Valuation of Up to $1.4 Trillion for Blockbuster I.P.O." data-date="11-10 23:39" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 23:39</span>
          <span class="news-item-title">重磅I.P.O.的人类目标估值高达1.4万$</span>
          <span class="news-item-title-en">Anthropic Targets Valuation of Up to $1.4 Trillion for Blockbuster I.P.O.</span>
          <span class="news-value-point">💡 这家人工智能公司的定价将使其成为有史以来规模最大的公开上市公司之一</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/10/metas-ai-agent-muse-lands-on-apple-watch-and-wear-os/" target="_blank" rel="noopener" data-cat="keji" data-summary="用户现在可以通过语音通话、短信或Apple Watch上的听写与Meta的AI助手进行交互。" data-title="Meta’s AI agent Muse lands on Apple Watch and Android Wear OS" data-date="11-10 23:29" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 23:29</span>
          <span class="news-item-title">Meta的AI代理Muse登陆Apple Watch和Android Wear OS</span>
          <span class="news-item-title-en">Meta’s AI agent Muse lands on Apple Watch and Android Wear OS</span>
          <span class="news-value-point">💡 用户现在可以通过语音通话、短信或Apple Watch上的听写与Meta的AI助手进行交互</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/191.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 10 日消息，今天（10 日）深夜，MiniMax 宣布，MiniMax H3-Image 正式发布并开放权重。这是一款衍生自 H3 的图像生成模型，其具备文本生成图像、图像参考和图像编辑能力。IT之家从官方介绍获悉，其能够在 10 秒内生成一张 4096 x 4096 像素、约 16 MP（4K）的高分辨率图像，同时呈现丰富、真实的细节，并具备优秀的指令遵循和多参考图理解能力。MiniMax 称，在 H3 预训练赋予的广泛图像能力基础上，H3-Image 进一步强化了整个后训练链路，在数据、强化学习、步数压缩、PE、部署优化等方面做了许多扎实的工作。这些工作的组合，使得 MiniMax H3-image 同时具备了速度、画面质量、指令遵循三个方面的竞争力：相比于主流的" data-title="MiniMax 开源 H3-Image 生图模型，10 秒就能生成一张 4K 图像" data-date="11-10 23:25" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 23:25</span>
          <span class="news-item-title">MiniMax 开源 H3-Image 生图模型，10 秒就能生成一张 4K 图像</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，今天（10 日）深夜，MiniMax 宣布，MiniMax H3-Image 正式发布并开放权重</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/190.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 10 日消息，据英国《金融时报》今天（10 日）晚间报道，作为 Anthropic 上市牵头投行的高盛，对 Anthropic 的未来给出了乐观预测：营收到 2030 年将突破 6,000 亿美元（IT之家注：现汇率约合 4.01 万亿元人民币），是 2025 年的 130 多倍。高盛向一名潜在投资者披露的预测显示，Anthropic 今年的营收预计约为 520 亿美元（现汇率约合 3,477.02 亿元人民币），2027 年增至 1,360 亿美元（现汇率约合 9,093.75 亿元人民币），2029 年达到 4,420 亿美元（现汇率约合 2.96 万亿元人民币），到 2030 年进一步突破 6,000 亿美元（现汇率约合 4.01 万亿元人民币）。相比之下，Anth" data-title="高盛预计 Anthropic 2030 年营收突破 6000 亿美元，并跻身全球营收最高企业之列" data-date="11-10 23:17" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 23:17</span>
          <span class="news-item-title">高盛预计 Anthropic 2030 年营收突破 6000 亿美元，并跻身全球营收最高企业之列</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，据英国《金融时报》今天（10 日）晚间报道，作为 Anthropic 上市牵头投行的高盛，对 Anthropi…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1030703/anthropic-ipo-1-4-trillion" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic周二证实，即使没有达到此前的预期，其IPO也可能是有史以来规模最大的IPO之一。其IPO价格预计在每股70.00 $至78.00 $之间，估值将高达1.4万亿$" data-title="Anthropic targets $1.4 trillion IPO" data-date="11-10 22:06" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 22:06</span>
          <span class="news-item-title">Anthropic的目标是$ 1.4万亿IPO</span>
          <span class="news-item-title-en">Anthropic targets $1.4 trillion IPO</span>
          <span class="news-value-point">💡 Anthropic周二证实，即使没有达到此前的预期，其IPO也可能是有史以来规模最大的IPO之一</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/" target="_blank" rel="noopener" data-cat="keji" data-summary="Adobe正在Firefly中使用新的原型构建器工具来对抗Figma。" data-title="Adobe brings AI agents and new creative tools to Photoshop, Premiere, and Firefly" data-date="11-10 22:05" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 22:05</span>
          <span class="news-item-title">Adobe将AI代理和新的创意工具引入Photoshop、Premiere和Firefly</span>
          <span class="news-item-title-en">Adobe brings AI agents and new creative tools to Photoshop, Premiere, and Firefly</span>
          <span class="news-value-point">💡 Adobe正在Firefly中使用新的原型构建器工具来对抗Figma</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/10/anthropic-sets-ipo-price-range-of-70-to-78-per-share-to-reach-an-implied-valuation-of-1-404-trillion/" target="_blank" rel="noopener" data-cat="keji" data-summary="如果其股票在完全摊薄的基础上处于价格范围的顶端，该公司最终可能价值高达1.404万亿$。" data-title="Anthropic sets IPO price range of $70 to $78 per share to reach an implied valuation of $1.404 trillion" data-date="11-10 22:01" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 22:01</span>
          <span class="news-item-title">Anthropic将IPO价格设定在每股70美元至78美元之间，以达到1.404万亿美元的隐含估值</span>
          <span class="news-item-title-en">Anthropic sets IPO price range of $70 to $78 per share to reach an implied valuation of $1.404 trillion</span>
          <span class="news-value-point">💡 如果其股票在完全摊薄的基础上处于价格范围的顶端，该公司最终可能价值高达1.404万亿$</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1030593/adobe-max-ai-agents-mcp-firefly-assistant-updates" target="_blank" rel="noopener" data-cat="keji" data-summary="Adobe致力于让聊天机器人和人工智能代理成为您的下一个设计助手，甚至代表您实现创意工作流程和重复性任务的自动化。今天在Adobe Max会议上宣布的一些工具和功能" data-title="Adobe is going all in on agentic AI" data-date="11-10 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">Adobe正在全力以赴使用agentic AI</span>
          <span class="news-item-title-en">Adobe is going all in on agentic AI</span>
          <span class="news-value-point">💡 Adobe致力于让聊天机器人和人工智能代理成为您的下一个设计助手，甚至代表您实现创意工作流程和重复性任务的自动化</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729815.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网成都11月10日电(王利文)2026年“第六届成渝双城科普行”活动10日在成都举行。活动现场，《成渝地区青少年科普研学线路与场景清单》正式发布，集中推出成渝两地共30条研学线路、40个特色点位，涵盖人工智能、航空航天、低空经济、自然保护、防灾减灾、现代农业等领域，推动两地科普资源共建共享，为青少年开展科学探究、参与科普实践提供更多选择。" data-title="成渝科普“场景清单”在蓉发布 推出30条研学线路" data-date="11-10 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 21:54</span>
          <span class="news-item-title">成渝科普“场景清单”在蓉发布 推出30条研学线路</span>
          <span class="news-value-point">💡 中新网成都11月10日电(王利文)2026年“第六届成渝双城科普行”活动10日在成都举行</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/new-framework-grades-ai-jailbreaks-across-capability-gains-scope-and-how-easy-they-are-to-deploy-frontier-model-forum-proposes-cvss-style-rating-system-for-new-ai-models" target="_blank" rel="noopener" data-cat="keji" data-summary="Frontier Model Forum发布了越狱评级框架，以估计模特逃离笼子有多容易，以及他们可以造成多少伤害。" data-title="New framework grades AI jailbreaks across capability gains, scope, and how easy they are to deploy" data-date="11-10 21:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 21:40</span>
          <span class="news-item-title">新框架针对能力提升、范围以及部署难易程度对AI越狱进行评级</span>
          <span class="news-item-title-en">New framework grades AI jailbreaks across capability gains, scope, and how easy they are to deploy</span>
          <span class="news-value-point">💡 Frontier Model Forum发布了越狱评级框架，以估计模特逃离笼子有多容易，以及他们可以造成多少伤害</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/going-deep-on-local-ai-performance-with-apples-mac-studio-with-m5-ultra-inference-engine-recipes-mandatory-for-bigger-models-as-mlx-stack-matures" target="_blank" rel="noopener" data-cat="keji" data-summary="但是，如果您正在考虑为构建本地AI推理设置而花费超过$ 1万美元， Mac Studio是否适合您？" data-title="Going deep on local AI performance benchmarking with Apple’s Mac Studio with M5 Ultra taking on Nvidia DGX Spark" data-date="11-10 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 21:20</span>
          <span class="news-item-title">使用配备M5 Ultra的Apple Mac Studio对Nvidia DGX Spark进行本地AI性能基准测试</span>
          <span class="news-item-title-en">Going deep on local AI performance benchmarking with Apple’s Mac Studio with M5 Ultra taking on Nvidia DGX Spark</span>
          <span class="news-value-point">💡 但是，如果您正在考虑为构建本地AI推理设置而花费超过$ 1万美元， Mac Studio是否适合您</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/10/technology/jensen-huang-nvidia-board.html" target="_blank" rel="noopener" data-cat="keji" data-summary="治理专家质疑，正在调查黄先生行为的董事会是否过于恭敬，因为他已经将英伟达变成了一家全球巨头。" data-title="Nvidia’s Board Has a History of Letting Jensen Huang Get His Way" data-date="11-10 21:07" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 21:07</span>
          <span class="news-item-title">英伟达董事会有让Jensen Huang按自己的方式行事的历史</span>
          <span class="news-item-title-en">Nvidia’s Board Has a History of Letting Jensen Huang Get His Way</span>
          <span class="news-value-point">💡 治理专家质疑，正在调查黄先生行为的董事会是否过于恭敬，因为他已经将英伟达变成了一家全球巨头</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/10/cyberattacks-threaten-to-make-open-source-ai-a-little-less-open-hugging-face-exec-warns/" target="_blank" rel="noopener" data-cat="keji" data-summary="Hugging Face高管艾琳·索莱曼（ Irene Solaiman ）警告说，开放式人工智能平台上不断增长的网络攻击可能会迫使更严格的安全限制，威胁到开放源代码社区对全球开发人员有价值的可访问性。" data-title="Cyberattacks threaten to make open-source AI a little less open, Hugging Face exec warns" data-date="11-10 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 21:00</span>
          <span class="news-item-title">Hugging Face高管警告称，网络攻击可能会使开源人工智能变得不那么开放</span>
          <span class="news-item-title-en">Cyberattacks threaten to make open-source AI a little less open, Hugging Face exec warns</span>
          <span class="news-value-point">💡 Hugging Face高管艾琳·索莱曼（ Irene Solaiman ）警告说，开放式人工智能平台上不断增长的网络攻击可能会迫使更严格的安全…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-targets-1-million-wafers-a-month-after-2032-planned-700-000-monthly-memory-wafers-could-rival-samsungs-entire-estimated-dram-production-capacity" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，特斯拉和SpaceX的Terafab计划在2032年后每月生产100万片晶圆，其中约70万片用于内存。" data-title="Elon Musk’s Terafab targets 1 million wafers a month after 2032" data-date="11-10 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 21:00</span>
          <span class="news-item-title">埃隆·马斯克（ Elon Musk ）的Terafab计划在2032年后每月生产100万片晶圆</span>
          <span class="news-item-title-en">Elon Musk’s Terafab targets 1 million wafers a month after 2032</span>
          <span class="news-value-point">💡 据报道，特斯拉和SpaceX的Terafab计划在2032年后每月生产100万片晶圆，其中约70万片用于内存</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/president-trump-says-the-fbi-is-investigating-jensen-huangs-affair-nvidia-also-accused-of-intervening-in-megaspeed-chip-smuggling-investigation" target="_blank" rel="noopener" data-cat="keji" data-summary="联邦调查局可能担心中国特工对美国领先的人工智能芯片制造商的领导者具有影响力。" data-title="President Trump says the FBI is investigating Jensen Huang’s affair" data-date="11-10 20:33" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 20:33</span>
          <span class="news-item-title">特朗普总统表示，联邦调查局正在调查黄延森的婚外情</span>
          <span class="news-item-title-en">President Trump says the FBI is investigating Jensen Huang’s affair</span>
          <span class="news-value-point">💡 联邦调查局可能担心中国特工对美国领先的人工智能芯片制造商的领导者具有影响力</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610675/man-utd-qa-michael-carrick-mauricio-pochettino-ineos-and-more-kaveh-solhekol-answers-your-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kaveh Solhekol已经回答了你关于曼联的最新问题，迈克尔·卡里克的未来在空中，俱乐部在降级区，还有更多的幕后问题。" data-title="Man Utd Q&amp;A: Carrick, Poch, INEOS and more answered" data-date="11-10 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 23:00</span>
          <span class="news-item-title">曼联问答： Carrick、Poch、INEOS等回答</span>
          <span class="news-item-title-en">Man Utd Q&A: Carrick, Poch, INEOS and more answered</span>
          <span class="news-value-point">💡 Kaveh Solhekol已经回答了你关于曼联的最新问题，迈克尔·卡里克的未来在空中，俱乐部在降级区，还有更多的幕后问题</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610675/man-utd-qa-michael-carrick-mauricio-pochettino-ineos-and-more-kaveh-solhekol-answers-your-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kaveh Solhekol已经回答了你关于曼联的最新问题，迈克尔·卡里克的未来在空中，俱乐部在降级区，还有更多的幕后问题。" data-title="Man Utd Q&amp;A: Carrick, Poch, INEOS and more answered" data-date="11-10 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 23:00</span>
          <span class="news-item-title">曼联问答： Carrick、Poch、INEOS等回答</span>
          <span class="news-item-title-en">Man Utd Q&A: Carrick, Poch, INEOS and more answered</span>
          <span class="news-value-point">💡 Kaveh Solhekol已经回答了你关于曼联的最新问题，迈克尔·卡里克的未来在空中，俱乐部在降级区，还有更多的幕后问题</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/180.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 11 月 10 日消息，Steam 平台现已公布了最新一周游戏销量排行榜（2026 年 11 月 3 日 - 2026 年 11 月 10 日，无免费游戏），《使命召唤：现代战争 4》反超《影之刃零》登顶全球榜，《影之刃零》继续蝉联国区榜首，新游《哥斯拉：怪兽大乱斗复刻版》《最终幻想 14：Evercold》首次上榜。全球榜单使命召唤：现代战争 4影之刃零AION 2足球经理 27深空当铺：可能是偷的EA SPORTS FC™ 27使命召唤 ®最终幻想 14 OnlineMoon Sweepers哥斯拉：怪兽大乱斗复刻版国区榜单影之刃零深空当铺：可能是偷的使命召唤：现代战争 4使命召唤NBA 2K27土豆兄弟 (Brotato)Wallpaper Engine：壁纸引擎足球经理 2" data-title="Steam 新一周游戏销量榜：《COD：MW4》反超《影之刃零》登顶全球" data-date="11-10 22:31" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 22:31</span>
          <span class="news-item-title">Steam 新一周游戏销量榜：《COD：MW4》反超《影之刃零》登顶全球</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，Steam 平台现已公布了最新一周游戏销量排行榜（2026 年 11 月 3 日 - 2026 年 11 月 …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610645/man-utds-transfer-policy-to-blame-for-clubs-worst-premier-league-start-and-not-michael-carrick-says-paul-merson" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的保罗·默森（ Paul Merson ）认为，曼联的转会策略是他们顶级赛季最糟糕的开局，而不是主教练迈克尔·卡里克（ Michael Carrick ）。" data-title="Merson: Man Utd transfer policy is to blame" data-date="11-10 21:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 21:30</span>
          <span class="news-item-title">Merson ： Man Utd转会政策是罪魁祸首</span>
          <span class="news-item-title-en">Merson: Man Utd transfer policy is to blame</span>
          <span class="news-value-point">💡 天空体育的保罗·默森（ Paul Merson ）认为，曼联的转会策略是他们顶级赛季最糟糕的开局，而不是主教练迈克尔·卡里克（ Michael …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610645/man-utds-transfer-policy-to-blame-for-clubs-worst-premier-league-start-and-not-michael-carrick-says-paul-merson" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的保罗·默森（ Paul Merson ）认为，曼联的转会策略是他们顶级赛季最糟糕的开局，而不是主教练迈克尔·卡里克（ Michael Carrick ）。" data-title="Merson: Man Utd transfer policy is to blame" data-date="11-10 21:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 21:30</span>
          <span class="news-item-title">Merson ： Man Utd转会政策是罪魁祸首</span>
          <span class="news-item-title-en">Merson: Man Utd transfer policy is to blame</span>
          <span class="news-value-point">💡 天空体育的保罗·默森（ Paul Merson ）认为，曼联的转会策略是他们顶级赛季最糟糕的开局，而不是主教练迈克尔·卡里克（ Michael …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Van Dijk &#39;not panicking&#39; about new deal." data-title="Liverpool latest: Van Dijk &#39;not panicking&#39; about new deal." data-date="11-10 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 20:00</span>
          <span class="news-item-title">利物浦最新消息：范迪克对新协议“不恐慌”。</span>
          <span class="news-item-title-en">Liverpool latest: Van Dijk 'not panicking' about new deal.</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmy0r041ed0po?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克的未来将在周三在摩纳哥举行的会议上讨论。" data-title="Carrick&#39;s Man Utd future to be decided at Wednesday meeting" data-date="11-10 19:23" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 19:23</span>
          <span class="news-item-title">Carrick's Man Utd的未来将在周三的会议上决定</span>
          <span class="news-item-title-en">Carrick's Man Utd future to be decided at Wednesday meeting</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克的未来将在周三在摩纳哥举行的会议上讨论</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610412/michael-carrick-future-man-utd-head-coach-position-increasingly-in-doubt-with-mauricio-pochettino-open-to-talks" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）作为曼联主教练的地位越来越受到质疑，如果俱乐部接近他，毛里西奥·波切蒂诺（ Mauricio Pochettino ）愿意进行讨论。" data-title="Poch open to Man Utd talks with Carrick&#39;s position in doubt" data-date="11-10 18:24" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 18:24</span>
          <span class="news-item-title">POCH对曼联持开放态度，与Carrick的立场有疑问</span>
          <span class="news-item-title-en">Poch open to Man Utd talks with Carrick's position in doubt</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）作为曼联主教练的地位越来越受到质疑，如果俱乐部接近他，毛里西奥·波切蒂诺（ Mauricio…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610138/chelsea-not-showing-the-consistency-to-get-champions-league-football-this-season-says-paul-merson" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在他最新的天空体育专栏中，保罗·默森（ Paul Merson ）阐述了他对切尔西击败桑德兰的看法-因为哈比·阿隆索（ Xabi Alonso ）在斯坦福桥（ Stamford Bridge ）的生活开始不一致。" data-title="Merson: If Chelsea don&#39;t get Champions League it&#39;s a massive failure" data-date="11-10 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 18:00</span>
          <span class="news-item-title">默森：如果切尔西没有获得冠军联赛，那就是一个巨大的失败</span>
          <span class="news-item-title-en">Merson: If Chelsea don't get Champions League it's a massive failure</span>
          <span class="news-value-point">💡 在他最新的天空体育专栏中，保罗·默森（ Paul Merson ）阐述了他对切尔西击败桑德兰的看法-因为哈比·阿隆索（ Xabi Alonso …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025491/aston-villa-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Aston Villa latest: Lindelof agrees new contract" data-title="Aston Villa latest: Lindelof agrees new contract" data-date="11-10 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 18:00</span>
          <span class="news-item-title">阿斯顿维拉最新消息：林德洛夫同意新合同</span>
          <span class="news-item-title-en">Aston Villa latest: Lindelof agrees new contract</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! What has Poch said about Premier League return?" data-title="Transfer Centre LIVE! What has Poch said about Premier League return?" data-date="11-10 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 17:00</span>
          <span class="news-item-title">转会中心直播！ Poch对英超联赛的回归有什么看法？</span>
          <span class="news-item-title-en">Transfer Centre LIVE! What has Poch said about Premier League return?</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13608837/james-penrice-scotland-and-rangers-defender-on-his-slow-rise-from-part-time-football-to-international-call-up" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“我一直认为，如果我继续比赛并继续表演，它就会到来。谢天谢地，它做到了。”" data-title="Penrice on &#39;slow rise&#39; from part-time football to Scotland call-up" data-date="11-10 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 16:00</span>
          <span class="news-item-title">Penrice谈从兼职足球到苏格兰征召的“缓慢崛起”</span>
          <span class="news-item-title-en">Penrice on 'slow rise' from part-time football to Scotland call-up</span>
          <span class="news-value-point">💡 “我一直认为，如果我继续比赛并继续表演，它就会到来</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13610462/sandpapergate-mitchell-starc-denies-knowledge-after-usman-khawaja-claims-as-cricket-australia-says-investigation-will-not-be-re-opened" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在前队友Usman Khawaja爆炸性地声称整个更衣室都知道2018年南非的球篡改计划之后，澳大利亚快速投球手Mitchell Starc否认了“Sandpapergate”的任何先前知识。" data-title="Starc denies Khawaja claims as Cricket Australia says investigation won&#39;t reopen" data-date="11-10 15:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 15:45</span>
          <span class="news-item-title">Starc否认Khawaja的说法，因为Cricket Australia表示调查不会重新开始</span>
          <span class="news-item-title-en">Starc denies Khawaja claims as Cricket Australia says investigation won't reopen</span>
          <span class="news-value-point">💡 在前队友Usman Khawaja爆炸性地声称整个更衣室都知道2018年南非的球篡改计划之后，澳大利亚快速投球手Mitchell Starc否认…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610412/michael-carrick-future-man-utd-head-coach-position-increasingly-in-doubt-but-no-final-decision-made" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）作为曼联主教练的地位越来越令人怀疑，但天空体育新闻（ Sky Sports News ）迄今为止已被告知，尚未就他在老特拉福德的未来做出最终决定。" data-title="Carrick&#39;s position increasingly in doubt" data-date="11-10 07:04" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 07:04</span>
          <span class="news-item-title">卡里克的立场越来越令人怀疑</span>
          <span class="news-item-title-en">Carrick's position increasingly in doubt</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）作为曼联主教练的地位越来越令人怀疑，但天空体育新闻（ Sky Sports News ）迄今…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw4g1g7z2mdgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛。" data-title="Man Utd yet to make decision on Carrick&#39;s future" data-date="11-10 01:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 01:49</span>
          <span class="news-item-title">曼联尚未就卡里克的未来做出决定</span>
          <span class="news-item-title-en">Man Utd yet to make decision on Carrick's future</span>
          <span class="news-value-point">💡 曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729864.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近期，社交平台上出现了一批内容为“取消外卖”“下架外卖”等话题的短视频，引发广泛关注。这些视频呈现出明显的模板化，且通常由多个账号在短期内批量生产，看似是个别餐饮商家的表态和呼吁，实则是深谙“情绪即流量”的MCN机构炮制的舆论噱头。" data-title="商家呼吁“取消外卖”？实为MCN制造对立、虚假摆拍引流" data-date="11-10 23:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 23:33</span>
          <span class="news-item-title">商家呼吁“取消外卖”？实为MCN制造对立、虚假摆拍引流</span>
          <span class="news-value-point">💡 近期，社交平台上出现了一批内容为“取消外卖”“下架外卖”等话题的短视频，引发广泛关注</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/secretlab-debuts-monitor-light-bar-add-on-to-reduce-glare-and-eye-strain-ergoarch-has-a-three-point-adjustment-arm-costs-usd179" target="_blank" rel="noopener" data-cat="zonghe" data-summary="广受欢迎的桌椅制造商Secretlab推出了新的显示器灯条。" data-title="Secretlab debuts monitor light bar add-on to reduce glare and eye strain" data-date="11-10 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 23:30</span>
          <span class="news-item-title">Secretlab首次推出监视器灯条附加组件，以减少眩光和眼睛疲劳</span>
          <span class="news-item-title-en">Secretlab debuts monitor light bar add-on to reduce glare and eye strain</span>
          <span class="news-value-point">💡 广受欢迎的桌椅制造商Secretlab推出了新的显示器灯条</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/189.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，据央视新闻报道，今天，第 39 届中国电影金鸡奖颁奖典礼举行。获奖名单如下：最佳女主角：高叶《南京照相馆》最佳男主角：梁家辉 《捕风追影》最佳女配角：兰西雅 《震耳欲聋》最佳男配角：吾守尔 · 赛来 《万桐书》最佳故事片：《南京照相馆》最佳导演：郑大圣《密档》评委会特别奖：《给阿嬷的情书》最佳新晋导演：万力《震耳欲聋》最佳中小成本故事片：《菜肉馄饨》最佳录音：王砚伟《镖人：风起大漠》最佳剪辑：黄曾鸿辰 《飞行家》最佳美术：王竞 《得闲谨制》最佳音乐：高小阳 《万桐书》最佳摄影：董劲松 《狂野时代》最佳动画：《浪浪山小妖怪》最佳纪录 / 科教片：《窗外是蓝星》最佳儿童片：《马兰花开的声音》最佳戏曲片：《顾炎武》最佳外语片：《情感价值》最佳编剧：《给阿嬷的情书》" data-title="第 39 届中国电影金鸡奖全名单公布，《浪浪山小妖怪》《窗外是蓝星》《给阿嬷的情书》等获奖" data-date="11-10 23:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 23:05</span>
          <span class="news-item-title">第 39 届中国电影金鸡奖全名单公布，《浪浪山小妖怪》《窗外是蓝星》《给阿嬷的情书》等获奖</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，据央视新闻报道，今天，第 39 届中国电影金鸡奖颁奖典礼举行</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1030211/reddit-reviews-product-recommendations-electronics-beauty-shopping" target="_blank" rel="noopener" data-cat="zonghe" data-summary="数以百万计的人转向Reddit寻求第一手建议和对消费品的评论。现在，该平台正在发挥其作为购物者目的地的作用，以挑战发布产品评论和" data-title="Reddit wants to guide your next purchase" data-date="11-10 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 23:00</span>
          <span class="news-item-title">Reddit希望指导您的下一次购买</span>
          <span class="news-item-title-en">Reddit wants to guide your next purchase</span>
          <span class="news-value-point">💡 数以百万计的人转向Reddit寻求第一手建议和对消费品的评论</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/187.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，QQ 鸿蒙版 App 今日在华为应用市场（App Gallery）开启 9.2.83 (3628) 版本邀测升级（需收到短信通知后点击链接跳转安装），测试时间为 2026/11/10-2026/11/24。IT之家附 QQ 鸿蒙版 App 本次测试版本新特性如下：1、新增支持表情搜索。2、新增支持查看历史头像。3、修复一些已知体验问题。据用户反馈，QQ 最新邀测版还适配了平板端的分栏显示功能。目前 QQ 鸿蒙版已获 5.2 万个评分（评分 2.4），已支持单聊、群聊、多人语音或视频通话、抢红包，刷空间好友动态、短视频、频道、扫一扫、手机 / 平板双端登录等功能。" data-title="QQ 鸿蒙版 App 获 9.2.83 邀测升级，新增支持查看历史头像等功能" data-date="11-10 22:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 22:56</span>
          <span class="news-item-title">QQ 鸿蒙版 App 获 9.2.83 邀测升级，新增支持查看历史头像等功能</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，QQ 鸿蒙版 App 今日在华为应用市场（App Gallery）开启 9.2.83 (3628) 版本邀测升…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/185.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，今天（10 日）晚间，Rockstar Games（R 星）公布了下周发售的《GTA 6》的多项重要信息。预购玩家现可在 PS5 和 Xbox Series X|S 上预载游戏，数字版玩家可以立即下载，实体版玩家则需等收到兑换码后才能预载。开发团队也正式确认，《GTA 6》不设性能模式，所有主机版本均以 30fps 为目标帧率，PS5 Pro 也不例外。不过，PS5 Pro 仍能凭借独占的 PlayStation 光谱超分辨率技术（PSSR）和光线追踪阴影获得更好的画质。据IT之家了解，《GTA 6》还充分利用了 PS5 的多项独占功能。缩短加载时间：利用 PS5 的高速固态硬盘和 I/O 架构加快游戏加载。增强空间音效：改进游戏音效的空间渲染，充分发挥 T" data-title="PS5 Pro 也不例外：R 星确认《GTA 6》所有主机目标帧率都是 30fps" data-date="11-10 22:50" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 22:50</span>
          <span class="news-item-title">PS5 Pro 也不例外：R 星确认《GTA 6》所有主机目标帧率都是 30fps</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，今天（10 日）晚间，Rockstar Games（R 星）公布了下周发售的《GTA 6》的多项重要信息</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/025/184.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，据央视新闻今日报道，根据世界气象组织公布的最新数据，2023 年至 2026 年成为有记录以来最热的四年。报告指出，年初的拉尼娜现象曾短暂抑制全球升温，但随着厄尔尼诺现象发展，全球气温再次攀升。预计厄尔尼诺将持续至 2027 年初，可能进一步推高 2026 年全年平均气温。与此同时，2025 年全球温室气体浓度再创新高，二氧化碳浓度较工业化前增加 53%。海洋热含量和卫星观测表明，地球系统积累热量的速度正在加快，2025 年地球能量失衡达到 1960 年有观测记录以来最高水平，2026 年可能再次刷新纪录。IT之家查询世界气象组织数据获悉，2026 年 1 月至 9 月，全球近地表平均气温较工业化前（1850 年至 1900 年）水平高出 1.47℃，与 2" data-title="2025 年地球能量失衡达 1960 年有观测记录以来最高水平，今年可能再次刷新纪录" data-date="11-10 22:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 22:41</span>
          <span class="news-item-title">2025 年地球能量失衡达 1960 年有观测记录以来最高水平，今年可能再次刷新纪录</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，据央视新闻今日报道，根据世界气象组织公布的最新数据，2023 年至 2026 年成为有记录以来最热的四年</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1030714/gta-vi-xbox-cloud-gaming-support" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Rockstar Games将于下周在Xbox Cloud Gaming上推出《侠盗猎车手VI》。虽然你通常认为这意味着《侠盗猎车手VI》可以在PC、网络、Xbox游戏机甚至电视上播放，但" data-title="GTA VI will be available on Xbox Cloud Gaming for Xbox One consoles" data-date="11-10 22:37" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 22:37</span>
          <span class="news-item-title">GTA VI将在Xbox One游戏机的Xbox Cloud Gaming上提供</span>
          <span class="news-item-title-en">GTA VI will be available on Xbox Cloud Gaming for Xbox One consoles</span>
          <span class="news-value-point">💡 Rockstar Games将于下周在Xbox Cloud Gaming上推出《侠盗猎车手VI》</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729843.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口11月10日电 (记者 王子谦)记者10日从《海南省应对气候变化的政策与行动2026年度报告》白皮书新闻发布会上获悉，海南近年来加快提升建筑领域绿色低碳发展质量，目前绿色建筑实现全面推广，装配式建造“应建尽建”。" data-title="海南推进城乡建设低碳转型 全面推广绿色建筑" data-date="11-10 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:01</span>
          <span class="news-item-title">海南推进城乡建设低碳转型 全面推广绿色建筑</span>
          <span class="news-value-point">💡 中新网海口11月10日电 (记者 王子谦)记者10日从《海南省应对气候变化的政策与行动2026年度报告》白皮书新闻发布会上获悉，海南近年来加快提…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729818.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川11月10日电 (记者 李佩珊)立冬过后，贺兰山东麓的风一天比一天硬。11月10日，宁夏贺兰山东麓葡萄酒产区银川子产区美贺庄园的千亩葡萄园里，工人们俯身垄间，把藤蔓从架上卸下，顺着一侧盘压进沟，再覆土压实。一行行葡萄藤没入土中，安静“冬眠”。" data-title="宁夏贺兰山东麓葡萄藤埋土越冬 静待春展" data-date="11-10 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:01</span>
          <span class="news-item-title">宁夏贺兰山东麓葡萄藤埋土越冬 静待春展</span>
          <span class="news-value-point">💡 中新网银川11月10日电 (记者 李佩珊)立冬过后，贺兰山东麓的风一天比一天硬</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729834.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆11月10日电 (殷缘)2026年陆海新通道暨巴蜀文化旅游走廊酒店厨师技能大赛10日在重庆举行。来自川渝两地及贵州、广西、新疆等西部陆海新通道沿线地区的20支代表队、80名厨师齐聚山城，展开厨艺对决。" data-title="以味为桥 80名厨师烹制西部陆海新通道沿线美食" data-date="11-10 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">以味为桥 80名厨师烹制西部陆海新通道沿线美食</span>
          <span class="news-value-point">💡 中新网重庆11月10日电 (殷缘)2026年陆海新通道暨巴蜀文化旅游走廊酒店厨师技能大赛10日在重庆举行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/10/spotifys-ai-dj-gets-new-voices-personalities-and-an-option-for-less-chatter/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Spotify Premium用户现在可以使用具有不同个性的新声音自定义他们的AI DJ ，或关闭歌曲之间的评论。" data-title="Spotify’s AI DJ gets new voices, personalities, and an option for less chatter" data-date="11-10 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">Spotify的AI DJ获得了新的声音、个性和减少聊天的选择</span>
          <span class="news-item-title-en">Spotify’s AI DJ gets new voices, personalities, and an option for less chatter</span>
          <span class="news-value-point">💡 Spotify Premium用户现在可以使用具有不同个性的新声音自定义他们的AI DJ ，或关闭歌曲之间的评论</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/10/after-challenging-googles-android-with-cyanogen-its-co-founder-takes-aim-at-windows-for-ai-era/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Kora将作为Windows的免费替代品推出，面向严重依赖AI模型和代理的用户。" data-title="After challenging Google’s Android with Cyanogen, its co-founder takes aim at Windows for AI era" data-date="11-10 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">在用Cyanogen挑战谷歌的Android之后，其联合创始人瞄准了人工智能时代的Windows</span>
          <span class="news-item-title-en">After challenging Google’s Android with Cyanogen, its co-founder takes aim at Windows for AI era</span>
          <span class="news-value-point">💡 Kora将作为Windows的免费替代品推出，面向严重依赖AI模型和代理的用户</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1027926/aura-e-ink-digital-photo-frame-10-inch-price-availability" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Aura刚刚推出了一个较小版本的彩色E Ink框架，有一些改进和更实惠的价格。全新Aura Ink相框采用10英寸E Ink面板，可在更高的像素密度下显示更多颜色。这也是不同的" data-title="Aura’s next color E Ink photo frame is smaller, cheaper, sharper, and more colorful" data-date="11-10 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">Aura的下一代Color E Ink相框更小、更便宜、更锐利、更丰富多彩</span>
          <span class="news-item-title-en">Aura’s next color E Ink photo frame is smaller, cheaper, sharper, and more colorful</span>
          <span class="news-value-point">💡 Aura刚刚推出了一个较小版本的彩色E Ink框架，有一些改进和更实惠的价格</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1030186/peak-design-roller-lite-carry-on-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当我们去年对Peak Design的Roller Pro进行采样时，我们几乎喜欢这款相机齿轮强国首次尝试合适的手提箱的一切。一切，也就是说，除了价格。当时，在众筹推出期间， Pro可以" data-title="Peak Design’s Roller Lite Carry-On is bigger on the inside — and cheaper, too" data-date="11-10 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 22:00</span>
          <span class="news-item-title">Peak Design的Roller Lite随身包内部更大，也更便宜</span>
          <span class="news-item-title-en">Peak Design’s Roller Lite Carry-On is bigger on the inside — and cheaper, too</span>
          <span class="news-value-point">💡 当我们去年对Peak Design的Roller Pro进行采样时，我们几乎喜欢这款相机齿轮强国首次尝试合适的手提箱的一切</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-10 23:42（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
