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
      <span>2026-10-06 22:23 抓取更新</span>
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
        <span class="channel-count">47</span>
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
        <span class="channel-count">2</span>
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
  <div class="ov-item"><span class="ov-num">47</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×16 · IT之家×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.ithome.com/1/010/110.htm" target="_blank" rel="noopener" data-cat="shizheng" data-summary="IT之家 10 月 6 日消息，据科技媒体 Tom&#39;s Hardware 今天报道，日本半导体光刻设备制造商 Gigaphoton 现已推出新型氖气回收系统 hTGM，用于氟化氩（ArF）准分子激光器。据报道，这套系统可实现 50% 氖气回收率，未来调整系统配置后，有望进一步提升回收效率。该技术有望弥补俄乌冲突后的芯片供应链缺口。2022 年前，乌克兰供应了全球半导体大约 50% 的氖气，后续被迫停止出口。同时，全球约 70% 的氖气产量用于半导体制造，其中很大一部分应用于先进的深紫外（IT之家注：DUV）光刻工艺。在此之后，中国、韩国等地区均加大了氖气生产力度，多家芯片制造商也在晶圆制造流程引入了氖气回收系统。" data-title="日本半导体光刻设备制造商 Gigaphoton 推出 hTGM 新型氖气回收系统，号称回收率达 50%" data-date="10-06 22:18" data-source="IT之家">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
        <span class="hero-featured-date">🕒 10-06 22:18</span>
      </div>
      <h2 class="hero-featured-title">日本半导体光刻设备制造商 Gigaphoton 推出 hTGM 新型氖气回收系统，号称回收率达 50%</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/10/06/pinterests-ai-now-turns-beauty-pins-into-action-plans/" target="_blank" rel="noopener" data-cat="keji" data-summary="Pinterest新的人工智能美容指南将美发和美甲别针转化为沙龙术语，包括预估成本、预约时间和维护需求。" data-title="Pinterest’s AI now turns beauty Pins into action plans" data-date="10-06 22:00" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Pinterest’s AI now turns beauty Pins into action plans</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/955.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 6 日消息，几天之前，OpenAI 指责苹果在商业秘密诉讼当中违规提交新证据。如今苹果予以反击，反过来指控 OpenAI 在其提交的回应中超出了法院规则允许的范围。据IT之家了解，这起诉讼由苹果发起，起诉两名前员工（刘畅〔Chang Liu〕、谭唐〔Tang Tan〕）、OpenAI 以及 io Products 涉嫌盗用商业秘密。案件当中的一项核心诉求，是申请一项临时禁令。简单来说，苹果请求法院颁布临时禁令。苹果的理由是，在案件审理期间，需要阻止自家的商业秘密进一步融入 OpenAI 的硬件开发工作。围绕这项禁令申请展开的多轮法律交锋过程中，苹果提交了一份答辩法律意见书，并附带五份专家书面证言作为支撑。此举随即招致几名被告的指责，被告方认为苹果违规引入新证据，请求法庭对" data-title="苹果与 OpenAI 商业秘密诉讼交锋升级：互指违规提交新证据" data-date="10-06 09:59" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">苹果与 OpenAI 商业秘密诉讼交锋升级：互指违规提交新证据</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/live/2026/10/06/world/france-protests-students-schools" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这些集会是对学生领导的抗议运动实力的考验，自9月下旬以来，抗议运动已经关闭了数百所法国高中。" data-title="Live Updates: Protests Spread Across France as Unions Join Student Demonstrations" data-date="10-06 22:20" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Live Updates: Protests Spread Across France as Unions Join Student Demonstrations</p>
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
        <a class="news-item" href="https://www.ithome.com/1/010/110.htm" target="_blank" rel="noopener" data-cat="shizheng" data-summary="IT之家 10 月 6 日消息，据科技媒体 Tom&#39;s Hardware 今天报道，日本半导体光刻设备制造商 Gigaphoton 现已推出新型氖气回收系统 hTGM，用于氟化氩（ArF）准分子激光器。据报道，这套系统可实现 50% 氖气回收率，未来调整系统配置后，有望进一步提升回收效率。该技术有望弥补俄乌冲突后的芯片供应链缺口。2022 年前，乌克兰供应了全球半导体大约 50% 的氖气，后续被迫停止出口。同时，全球约 70% 的氖气产量用于半导体制造，其中很大一部分应用于先进的深紫外（IT之家注：DUV）光刻工艺。在此之后，中国、韩国等地区均加大了氖气生产力度，多家芯片制造商也在晶圆制造流程引入了氖气回收系统。" data-title="日本半导体光刻设备制造商 Gigaphoton 推出 hTGM 新型氖气回收系统，号称回收率达 50%" data-date="10-06 22:18" data-source="IT之家">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 22:18</span>
          <span class="news-item-title">日本半导体光刻设备制造商 Gigaphoton 推出 hTGM 新型氖气回收系统，号称回收率达 50%</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，据科技媒体 Tom's Hardware 今天报道，日本半导体光刻设备制造商 Gigaphoton 现已推出新型…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/06/world/asia/trump-los-angeles-san-diego-iran.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="州长加文·纽森(Gavin Newsom)在一次政治集会上发表讲话后，称总统“危险而疯狂” ，特朗普在集会上表示，伊朗战争对于“维护世界安全”是必要的。" data-title="Trump Suggests Iran Could ‘Take Out’ L.A. or San Diego, Drawing Anger From California Leaders" data-date="10-06 22:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-06 22:03</span>
          <span class="news-item-title">特朗普建议伊朗可以“拿下”洛杉矶或圣地亚哥，引起加州领导人的愤怒</span>
          <span class="news-item-title-en">Trump Suggests Iran Could ‘Take Out’ L.A. or San Diego, Drawing Anger From California Leaders</span>
          <span class="news-value-point">💡 州长加文·纽森(Gavin Newsom)在一次政治集会上发表讲话后，称总统“危险而疯狂” ，特朗普在集会上表示，伊朗战争对于“维护世界安全”是…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708548.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月6日，法国伊夫林省发生大规模停电，著名景点凡尔赛宫当天宣布暂时关闭，开放时间另行通知。" data-title="法国凡尔赛宫因大规模停电暂时关闭" data-date="10-06 22:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 22:02</span>
          <span class="news-item-title">法国凡尔赛宫因大规模停电暂时关闭</span>
          <span class="news-value-point">💡 当地时间10月6日，法国伊夫林省发生大规模停电，著名景点凡尔赛宫当天宣布暂时关闭，开放时间另行通知</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708547.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月6日，欧盟委员会主席冯德莱恩在社交媒体发文表示，袭击民用船只的行为不可接受。" data-title="冯德莱恩：袭击黑海民用船只的行为不可接受" data-date="10-06 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 22:00</span>
          <span class="news-item-title">冯德莱恩：袭击黑海民用船只的行为不可接受</span>
          <span class="news-value-point">💡 当地时间10月6日，欧盟委员会主席冯德莱恩在社交媒体发文表示，袭击民用船只的行为不可接受</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦10月6日电 (记者 欧阳开宇)英国国家统计局6日发布数据显示，英国电子烟使用者规模持续攀升，2025年，新增电子烟使用者达110万人，较2024年的94万人显著增长。" data-title="英国电子烟使用者规模持续攀升" data-date="10-06 21:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 21:34</span>
          <span class="news-item-title">英国电子烟使用者规模持续攀升</span>
          <span class="news-value-point">💡 中新社伦敦10月6日电 (记者 欧阳开宇)英国国家统计局6日发布数据显示，英国电子烟使用者规模持续攀升，2025年，新增电子烟使用者达110万人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708541.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月6日电 中国外交部发言人郭嘉昆6日答记者问时表示，希望欧方同中方相向而行，通过对话协商解决彼此关切，共同维护全球产供链稳定畅通，推动中欧经贸关系健康稳定发展。" data-title="外交部：希望欧方同中方相向而行，通过对话协商解决彼此关切" data-date="10-06 21:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 21:11</span>
          <span class="news-item-title">外交部：希望欧方同中方相向而行，通过对话协商解决彼此关切</span>
          <span class="news-value-point">💡 中新社北京10月6日电 中国外交部发言人郭嘉昆6日答记者问时表示，希望欧方同中方相向而行，通过对话协商解决彼此关切，共同维护全球产供链稳定畅通，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708537.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月6日电 中国外交部发言人郭嘉昆6日答记者问时表示，中方反对借战事关联抹黑中国。" data-title="外交部：反对借战事关联抹黑中国" data-date="10-06 21:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 21:08</span>
          <span class="news-item-title">外交部：反对借战事关联抹黑中国</span>
          <span class="news-value-point">💡 中新社北京10月6日电 中国外交部发言人郭嘉昆6日答记者问时表示，中方反对借战事关联抹黑中国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708532.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州10月6日电 (郭军 彭国曦 张晓敏)进入国庆中秋假期第六天，国铁广州局迎来客流返程小高峰，当天预计发送旅客283.5万人次，较2025年同期增加61.7万人次，增幅27.8%。" data-title="国铁广州局迎来返程小高峰 假期第六天预计送客逾283万人次" data-date="10-06 21:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 21:08</span>
          <span class="news-item-title">国铁广州局迎来返程小高峰 假期第六天预计送客逾283万人次</span>
          <span class="news-value-point">💡 中新网广州10月6日电 (郭军 彭国曦 张晓敏)进入国庆中秋假期第六天，国铁广州局迎来客流返程小高峰，当天预计发送旅客283.5万人次，较202…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708535.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月6日电 中国外交部发言人郭嘉昆6日答记者问时表示，中方坚决反对菲律宾损害中国主权和权益的任何行径，将继续采取必要措施，坚定捍卫自身在南海的领土主权和海洋权益。" data-title="中方：坚决反对菲律宾损害中国主权和权益的任何行径" data-date="10-06 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 21:07</span>
          <span class="news-item-title">中方：坚决反对菲律宾损害中国主权和权益的任何行径</span>
          <span class="news-value-point">💡 中新社北京10月6日电 中国外交部发言人郭嘉昆6日答记者问时表示，中方坚决反对菲律宾损害中国主权和权益的任何行径，将继续采取必要措施，坚定捍卫自…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708524.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月6日，外交部发言人郭嘉昆答记者问。" data-title="外交部回应台接收美战斗机：中方坚决反对美对台军售" data-date="10-06 20:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 20:28</span>
          <span class="news-item-title">外交部回应台接收美战斗机：中方坚决反对美对台军售</span>
          <span class="news-value-point">💡 10月6日，外交部发言人郭嘉昆答记者问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708523.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近日，菲方飞机和船只未经中方允许，擅自闯入中国管辖海空域。对此，外交部发言人回应。" data-title="中国军队正当合理！中方正告菲方立即停止侵权挑衅" data-date="10-06 20:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 20:27</span>
          <span class="news-item-title">中国军队正当合理！中方正告菲方立即停止侵权挑衅</span>
          <span class="news-value-point">💡 近日，菲方飞机和船只未经中方允许，擅自闯入中国管辖海空域</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708520.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月6日，外交部发言人郭嘉昆答记者问。" data-title="外交部：解决台湾问题完全是中国人自己的事 不容任何外部势力干涉" data-date="10-06 20:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 20:25</span>
          <span class="news-item-title">外交部：解决台湾问题完全是中国人自己的事 不容任何外部势力干涉</span>
          <span class="news-value-point">💡 10月6日，外交部发言人郭嘉昆答记者问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708500.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月6日电 斯德哥尔摩消息：瑞典皇家科学院6日宣布，将2026年诺贝尔物理学奖授予弗朗西斯·哈尔岑(Francis Halzen)，以表彰他对“冰立方中微子天文台”作出的决定性贡献，以及在发现具有天体物理起源的高能中微子方面取得的成就。" data-title="弗朗西斯·哈尔岑获得2026年诺贝尔物理学奖" data-date="10-06 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 19:29</span>
          <span class="news-item-title">弗朗西斯·哈尔岑获得2026年诺贝尔物理学奖</span>
          <span class="news-value-point">💡 中新社北京10月6日电 斯德哥尔摩消息：瑞典皇家科学院6日宣布，将2026年诺贝尔物理学奖授予弗朗西斯·哈尔岑(Francis Halzen)，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708497.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科10月6日电 俄罗斯莫斯科州州长沃罗比约夫6日表示，该州遭到乌克兰大规模无人机袭击，目前已导致2人死亡、9人受伤。" data-title="俄罗斯莫斯科地区遭无人机袭击造成2死9伤" data-date="10-06 19:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 19:27</span>
          <span class="news-item-title">俄罗斯莫斯科地区遭无人机袭击造成2死9伤</span>
          <span class="news-value-point">💡 中新社莫斯科10月6日电 俄罗斯莫斯科州州长沃罗比约夫6日表示，该州遭到乌克兰大规模无人机袭击，目前已导致2人死亡、9人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708477.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月6日电(甘甜) 当地时间10月6日，瑞典皇家科学院决定将2026年诺贝尔物理学奖授予弗朗西斯·哈尔岑，以表彰他对冰立方中微子天文台作出的决定性贡献，以及对天体物理来源高能中微子的发现。" data-title="2026年诺贝尔物理学奖揭晓：1名科学家收获殊荣" data-date="10-06 18:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 18:02</span>
          <span class="news-item-title">2026年诺贝尔物理学奖揭晓：1名科学家收获殊荣</span>
          <span class="news-value-point">💡 中新网10月6日电(甘甜) 当地时间10月6日，瑞典皇家科学院决定将2026年诺贝尔物理学奖授予弗朗西斯·哈尔岑，以表彰他对冰立方中微子天文台作…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/10/06/pinterests-ai-now-turns-beauty-pins-into-action-plans/" target="_blank" rel="noopener" data-cat="keji" data-summary="Pinterest新的人工智能美容指南将美发和美甲别针转化为沙龙术语，包括预估成本、预约时间和维护需求。" data-title="Pinterest’s AI now turns beauty Pins into action plans" data-date="10-06 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-06 22:00</span>
          <span class="news-item-title">Pinterest的人工智能现在将美容徽章转化为行动计划</span>
          <span class="news-item-title-en">Pinterest’s AI now turns beauty Pins into action plans</span>
          <span class="news-value-point">💡 Pinterest新的人工智能美容指南将美发和美甲别针转化为沙龙术语，包括预估成本、预约时间和维护需求</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/109.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，当地时间上午 9 点 30 分，纳斯达克市场开盘。开盘钟声敲响后的二十分钟左右，英伟达（NVDA）市值达到 5.82 万亿美元（IT之家注：现汇率约合 39.08 万亿元人民币），创下历史新高，同时距 6 万亿美元（现汇率约合 40.29 万亿元人民币）仅有一步之遥。今日开盘时，英伟达股价为 242.10 美元（现汇率约合 1,626 元人民币），最高 243.37 美元（现汇率约合 1,634 元人民币），最低 240.76 美元（现汇率约合 1,617 元人民币）。同时，英伟达股价于美东时间 10 月 5 日星期一再度刷新历史纪录，收盘报 238.90 美元（现汇率约合 1,604 元人民币），单日上涨 2.12%，连续第三个交易日以收盘价创历史新高。如果" data-title="距 6 万亿美元仅一步之遥！英伟达市值达 5.8 万亿美元，创历史新高" data-date="10-06 21:58" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 21:58</span>
          <span class="news-item-title">距 6 万亿美元仅一步之遥！英伟达市值达 5.8 万亿美元，创历史新高</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，当地时间上午 9 点 30 分，纳斯达克市场开盘</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/108.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，当地时间 10 月 6 日，法国公司 Mistral AI 正式推出 Mistral Large 4 模型的公开预览版（Public Preview），简称 ML4，代号 le Chonk。即日起，用户可以在 Mistral Studio 上体验预览版 API，模型权重将于本月底正式开放下载。目前，官方正联合顶尖网络安全机构、受信任的合作伙伴及政府监管部门，在真实业务环境中对模型展开红队测试（Red-Teaming）。相关合作方将获得该模型的专项测试访问权限；该测试版本适当放宽了内容安全审查策略，并强化了网络安全攻防技术能力。ML4 是一款拥有 1 万亿总参数、490 亿激活参数的原生多模态模型，Mistral 称其实测表现不仅足以媲美全球顶尖的开源模型，更大" data-title="宣称“欧美最强开源模型”：Mistral AI 发布 Mistral Large 4 公开预览版，月底开放权重" data-date="10-06 21:56" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 21:56</span>
          <span class="news-item-title">宣称“欧美最强开源模型”：Mistral AI 发布 Mistral Large 4 公开预览版，月底开放权重</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，当地时间 10 月 6 日，法国公司 Mistral AI 正式推出 Mistral Large 4 模型的公开…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/105.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，红魔 12 Pro+ 手机新品今日在京东开启新品预约，价格暂未公布，新机将于 10 月 15 日 14:30 正式发布。京东红魔 12 Pro+ 游戏旗舰手机待公布立即预约IT之家了解到，红魔 12 Pro+ 手机将搭载高通第六代骁龙 8 超级至尊版芯片。该机号称“迄今为止手感最好的红魔旗舰”，主打“更轻、更薄、更窄、更圆润”。预热图显示，新机相比前代厚度更薄、重量更轻，同时屏幕黑边、边框圆角都有优化，屏幕黑边由前代的 1.25mm 减小到了 0.96mm。红魔游戏手机产品总经理姜超曾表示，红魔 12Pro+ 仍然是一台真正属于玩家的手机：“性能在高负载下站得住，散热扛得住长时间鏖战，手感更进一步轻薄，设计有独一份的辨识度，正面无开孔的屏下全面屏完整纯粹，日常" data-title="红魔 12 Pro+ 手机新品开启预约，10 月 15 日发布" data-date="10-06 21:34" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 21:34</span>
          <span class="news-item-title">红魔 12 Pro+ 手机新品开启预约，10 月 15 日发布</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，红魔 12 Pro+ 手机新品今日在京东开启新品预约，价格暂未公布，新机将于 10 月 15 日 14:30 正…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/gigaphoton-debuts-neon-recycling-system-with-claimed-50-percent-recovery-rate-systems-throw-a-lifeline-to-chipmakers-that-utilize-70-percent-of-global-neon-supply-in-duv-lithography" target="_blank" rel="noopener" data-cat="keji" data-summary="新的氖气回收系统有望减少主要芯片制造商使用DUV光刻对惰性气体的需求。但随着这项技术被取代，这种急需的修复可能只是暂时的。" data-title="Gigaphoton debuts neon recycling system with claimed 50% recovery rate" data-date="10-06 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 21:20</span>
          <span class="news-item-title">Gigaphoton推出霓虹灯回收系统，声称回收率为50 ％</span>
          <span class="news-item-title-en">Gigaphoton debuts neon recycling system with claimed 50% recovery rate</span>
          <span class="news-value-point">💡 新的氖气回收系统有望减少主要芯片制造商使用DUV光刻对惰性气体的需求</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1005451/google-gemini-free-flash-lite-only" target="_blank" rel="noopener" data-cat="keji" data-summary="从10月9日开始，任何使用免费套餐的Google Gemini用户将仅限于Flash Lite型号。免费用户目前可以从Gemini Flash Lite、Flash和Pro中进行选择，但现在您需要每月$ 4.99的Google AI Plus订阅才能获得" data-title="Google is about to remove free access to Gemini Flash and Pro" data-date="10-06 21:19" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 21:19</span>
          <span class="news-item-title">谷歌即将取消对Gemini Flash和Pro的免费访问权限</span>
          <span class="news-item-title-en">Google is about to remove free access to Gemini Flash and Pro</span>
          <span class="news-value-point">💡 从10月9日开始，任何使用免费套餐的Google Gemini用户将仅限于Flash Lite型号</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/ev-charging-company-plans-to-deploy-100-000-nvidia-gpus-in-pods-at-its-roadside-sites-across-the-us-aims-to-offer-worlds-first-edge-inference-compute-network-using-idle-ev-charging-capacity" target="_blank" rel="noopener" data-cat="keji" data-summary="电动汽车充电公司Xeal计划利用其现有的美国网络部署“世界上第一个使用空闲电动汽车充电容量的边缘推理计算网络”。" data-title="EV charging company plans to deploy 100,000 Nvidia GPUs in pods at its roadside sites across the US" data-date="10-06 20:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 20:45</span>
          <span class="news-item-title">电动汽车充电公司计划在美国各地的路边站点部署10万个英伟达GPU</span>
          <span class="news-item-title-en">EV charging company plans to deploy 100,000 Nvidia GPUs in pods at its roadside sites across the US</span>
          <span class="news-value-point">💡 电动汽车充电公司Xeal计划利用其现有的美国网络部署“世界上第一个使用空闲电动汽车充电容量的边缘推理计算网络”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/hackers-suspected-of-using-ai-agents-for-cyberattacks-on-south-korean-banks-exposing-data-from-about-25-000-customers-officials-believe-ai-models-enable-actors-to-hack-with-ease-even-without-specialized-skills" target="_blank" rel="noopener" data-cat="keji" data-summary="韩国总统李宰明（ Lee Jae Myung ）告诉内阁，有迹象表明，黑客利用人工智能对银行进行攻击。" data-title="Hackers suspected of using AI agents for cyberattacks on South Korean banks, exposing data from about 25,000 customers" data-date="10-06 20:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 20:15</span>
          <span class="news-item-title">涉嫌使用人工智能代理对韩国银行进行网络攻击的黑客，暴露了大约25,000名客户的数据</span>
          <span class="news-item-title-en">Hackers suspected of using AI agents for cyberattacks on South Korean banks, exposing data from about 25,000 customers</span>
          <span class="news-value-point">💡 韩国总统李宰明（ Lee Jae Myung ）告诉内阁，有迹象表明，黑客利用人工智能对银行进行攻击</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501736.html" target="_blank" rel="noopener" data-cat="keji" data-summary="不er，咋陶哲轩也成AI减速派了？？" data-title="不er，咋陶哲轩也成AI减速派了？？" data-date="10-06 15:59" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-06 15:59</span>
          <span class="news-item-title">不er，咋陶哲轩也成AI减速派了？？</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/007.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，OPPO 现已在印度市场推出 F35 5G/F35 Pro 5G 手机，新品定位中低端市场，采用 8000mAh 大电池，以及天玑 6360 Max/7360 Max 芯片，起售价为 38,999 卢比（IT之家注：现汇率约合 2,725 元人民币）。据介绍，OPPO F35 5G 手机搭载 6.57 英寸 AMOLED 屏幕，分辨率为 2372×1080，支持 120Hz 高刷，亮度可达 800nits。配备联发科天玑 6360 Max 芯片，提供 6GB/8GB 内存以及 128GB 存储空间，具备 4300mm² 大面积 VC 液冷散热。同时，该手机拥有 5000 万像素后置主摄和 200 万像素黑白辅助镜头，前置 5000 万像素自拍镜头。拥有 800" data-title="OPPO 推出 F35 5G 系列手机：8000mAh 电池，天玑 6360 Max/7360 Max 芯片" data-date="10-06 15:55" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:55</span>
          <span class="news-item-title">OPPO 推出 F35 5G 系列手机：8000mAh 电池，天玑 6360 Max/7360 Max 芯片</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，OPPO 现已在印度市场推出 F35 5G/F35 Pro 5G 手机，新品定位中低端市场，采用 8000mAh…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/006.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，科技媒体 gigazine 今天（10 月 6 日）报道，报道称开发者 Niko1221 开源推出 Strata 引擎，可以在 12GB 及以上显存的消费级显卡上，运行量化的 Qwen3.8-Flash-Next 模型（1250 亿参数）。IT之家注：Qwen3.8-Flash-Next 模型是阿里巴巴 Qwen 团队于 2026 年 8 月推出的多模态混合专家（MoE）模型的压缩版本，配有 125B 参数，另含 51B 参数的 n-gram 嵌入表，原生支持 262K token 上下文长度。Strata 为了降低显存占用，主要采用两项关键技术：其一是将 MoE（混合专家）模型整体载入 RAM，仅将高频使用的专家模型载入 VRAM。其二使用轻量模型进行投机解" data-title="12GB 显存显卡跑 125B Qwen3.8 模型：Strata 登场，单张 RTX 5070 跑出 94 词元 / 秒" data-date="10-06 15:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:45</span>
          <span class="news-item-title">12GB 显存显卡跑 125B Qwen3.8 模型：Strata 登场，单张 RTX 5070 跑出 94 词元 / 秒</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，科技媒体 gigazine 今天（10 月 6 日）报道，报道称开发者 Niko1221 开源推出 Strata…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/003.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，据路透社报道，OpenAI 与 Anthropic 于周二向澳大利亚议会表态，支持出台相关法规，强制要求企业通报其 AI 智能体所造成的数据泄露事件。两家机构同时坦承，目前是否通知监管当局完全由企业自主决定。此前，ChatGPT 开发商 OpenAI 旗下的一款智能体入侵了澳大利亚的核心医疗门户网站，但该机构历时三个月才向澳大利亚政府通报，由此引发了公众的强烈抗议。上述表态正是对此事作出的回应。目前，OpenAI 与 Claude 的开发商 Anthropic 均承诺作为核心算力采购方，参与澳大利亚本土开发商规划的数座大型数据中心项目，两家机构正在等待相关监管审批。OpenAI 首席战略官杰森 · 权（Jason Kwon）在悉尼举行的一场听证会上表态：“我们" data-title="OpenAI 与 Anthropic 向澳大利亚表态：支持出台数据泄露相关监管法规" data-date="10-06 15:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:32</span>
          <span class="news-item-title">OpenAI 与 Anthropic 向澳大利亚表态：支持出台数据泄露相关监管法规</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，据路透社报道，OpenAI 与 Anthropic 于周二向澳大利亚议会表态，支持出台相关法规，强制要求企业通报…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501726.html" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI“疯狂28天”首日，这都发了些啥啊…" data-title="OpenAI“疯狂28天”首日，这都发了些啥啊…" data-date="10-06 14:45" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-06 14:45</span>
          <span class="news-item-title">OpenAI“疯狂28天”首日，这都发了些啥啊…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/974.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，华为海外 X 账号今日（10 月 6 日）发布了 9 月 29 日的国际媒体圆桌会议摘要。华为常务董事、产品投资评审委员会主任、终端 BG 董事长余承东与多家国际媒体的记者就华为消费者业务及 HarmonyOS 生态系统进行了交流。余承东表示，自己于 1993 年加入华为，那是 33 年前的事了。当时，公司只有几百名员工。目前，华为拥有超过 20 万名员工，其中近一半从事研发工作。2007 年至 2025 年底，华为在研发方面投入了超过 1.8 万亿元人民币。早期，华为将约 10% 的年收入再投资于研发；近年来，这一比例已跃升至 20% 以上。余承东还提到，自 2019 年以来，华为克服了许多困难以求生存。华为与国内供应链合作，依靠本土技术和能力制造先进芯片、" data-title="华为余承东官宣鸿蒙出海：正在考虑未来逐步将 HarmonyOS 推向全球市场" data-date="10-06 12:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 12:20</span>
          <span class="news-item-title">华为余承东官宣鸿蒙出海：正在考虑未来逐步将 HarmonyOS 推向全球市场</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，华为海外 X 账号今日（10 月 6 日）发布了 9 月 29 日的国际媒体圆桌会议摘要</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708398.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="水网、新型电网、算力网、新一代通信网、城市地下管网、物流网，这“六张网”，是我国“十五五”时期现代化基础设施体系建设的核心内容。" data-title="“十五五”末水网织成什么样？水利部给出六组目标数据" data-date="10-06 11:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 11:49</span>
          <span class="news-item-title">“十五五”末水网织成什么样？水利部给出六组目标数据</span>
          <span class="news-value-point">💡 水网、新型电网、算力网、新一代通信网、城市地下管网、物流网，这“六张网”，是我国“十五五”时期现代化基础设施体系建设的核心内容</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">2 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/955.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 6 日消息，几天之前，OpenAI 指责苹果在商业秘密诉讼当中违规提交新证据。如今苹果予以反击，反过来指控 OpenAI 在其提交的回应中超出了法院规则允许的范围。据IT之家了解，这起诉讼由苹果发起，起诉两名前员工（刘畅〔Chang Liu〕、谭唐〔Tang Tan〕）、OpenAI 以及 io Products 涉嫌盗用商业秘密。案件当中的一项核心诉求，是申请一项临时禁令。简单来说，苹果请求法院颁布临时禁令。苹果的理由是，在案件审理期间，需要阻止自家的商业秘密进一步融入 OpenAI 的硬件开发工作。围绕这项禁令申请展开的多轮法律交锋过程中，苹果提交了一份答辩法律意见书，并附带五份专家书面证言作为支撑。此举随即招致几名被告的指责，被告方认为苹果违规引入新证据，请求法庭对" data-title="苹果与 OpenAI 商业秘密诉讼交锋升级：互指违规提交新证据" data-date="10-06 09:59" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 09:59</span>
          <span class="news-item-title">苹果与 OpenAI 商业秘密诉讼交锋升级：互指违规提交新证据</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，几天之前，OpenAI 指责苹果在商业秘密诉讼当中违规提交新证据</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/05/manchester-city-spending-and-the-fine-margins-of-premier-league-football" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Mike Alhadeff在回应有关该团队违反金融法规的文章时说，曼城的钱花得非常少， Ed Barrett说利物浦的头衔被抢走了，而Neil Smith则警告不要胜利主义。" data-title="Manchester City’s spending and the fine margins of Premier League football | Letters" data-date="10-06 00:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-06 00:50</span>
          <span class="news-item-title">曼城的支出和英超足球的良好利润|信件</span>
          <span class="news-item-title-en">Manchester City’s spending and the fine margins of Premier League football | Letters</span>
          <span class="news-value-point">💡 Mike Alhadeff在回应有关该团队违反金融法规的文章时说，曼城的钱花得非常少， Ed Barrett说利物浦的头衔被抢走了，而Neil …</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/live/2026/10/06/world/france-protests-students-schools" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这些集会是对学生领导的抗议运动实力的考验，自9月下旬以来，抗议运动已经关闭了数百所法国高中。" data-title="Live Updates: Protests Spread Across France as Unions Join Student Demonstrations" data-date="10-06 22:20" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-06 22:20</span>
          <span class="news-item-title">实时更新：随着工会加入学生示威活动，抗议活动在法国各地蔓延</span>
          <span class="news-item-title-en">Live Updates: Protests Spread Across France as Unions Join Student Demonstrations</span>
          <span class="news-value-point">💡 这些集会是对学生领导的抗议运动实力的考验，自9月下旬以来，抗议运动已经关闭了数百所法国高中</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708550.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="山野风险不容小觑，不论是否有户外徒步经验，都要提前科学规划，量力而行。一旦遇到突发状况该如何自救？来看专业人员的提示。" data-title="秋季山野出行提示：科学规划防险情，远离网红野游路线谨防失温" data-date="10-06 22:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 22:16</span>
          <span class="news-item-title">秋季山野出行提示：科学规划防险情，远离网红野游路线谨防失温</span>
          <span class="news-value-point">💡 山野风险不容小觑，不论是否有户外徒步经验，都要提前科学规划，量力而行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708549.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国庆假期，全国7座及7座以下小客车从10月1日0时到10月7日24时免收高速公路通行费。假期最后一天的返程计费问题也是很多车主的高频踩坑点，交通运输部提醒，千万别为省钱冒险“踩零点”驶离高速。" data-title="国庆返程必看！高速免费看出口时间 千万别卡点下高速" data-date="10-06 22:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 22:11</span>
          <span class="news-item-title">国庆返程必看！高速免费看出口时间 千万别卡点下高速</span>
          <span class="news-value-point">💡 国庆假期，全国7座及7座以下小客车从10月1日0时到10月7日24时免收高速公路通行费</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/06/business/media/paramount-warner-bros-discovery-skydance.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="经过一场法律纠纷，派拉蒙终于收购了华纳兄弟探索。在给员工的一份备忘录中，合并后的公司领导暗示要削减成本。" data-title="Paramount Closes Its Deal for Warner Bros. Discovery" data-date="10-06 22:08" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-06 22:08</span>
          <span class="news-item-title">派拉蒙完成与Warner Bros. Discovery的交易</span>
          <span class="news-item-title-en">Paramount Closes Its Deal for Warner Bros. Discovery</span>
          <span class="news-value-point">💡 经过一场法律纠纷，派拉蒙终于收购了华纳兄弟探索</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/06/get-all-your-questions-answered-at-techcrunch-disrupt-2026-the-full-breakout-session-agenda-revealed/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在TechCrunch Disrupt 2026上解答您的所有扩展和技术问题。以下是10月13日至15日在旧金山举行的分组会议的完整议程。立即注册，即可享受高达$ 100的优惠，并以50%的折扣获得第二张通行证。" data-title="Get all your questions answered at TechCrunch Disrupt 2026: The full breakout session agenda revealed" data-date="10-06 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-06 22:00</span>
          <span class="news-item-title">在TechCrunch Disrupt 2026上解答您的所有问题：完整的分组会议议程揭晓</span>
          <span class="news-item-title-en">Get all your questions answered at TechCrunch Disrupt 2026: The full breakout session agenda revealed</span>
          <span class="news-value-point">💡 在TechCrunch Disrupt 2026上解答您的所有扩展和技术问题</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1003583/pixel-watch-5-prime-day-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Google Pixel Watch 5在亚马逊10月份的销售期间打折了60 $ ， 41mm版本的售价为$ 334.99 ， 45mm版本的售价为$ 364.99。谷歌智能手表的最新版本在8月份与Pixel 11手机一起推出，" data-title="The Pixel Watch 5 is a better value at $65 off" data-date="10-06 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 22:00</span>
          <span class="news-item-title">Pixel Watch 5优惠$ 65</span>
          <span class="news-item-title-en">The Pixel Watch 5 is a better value at $65 off</span>
          <span class="news-value-point">💡 Google Pixel Watch 5在亚马逊10月份的销售期间打折了60 $ ， 41mm版本的售价为$ 334.99 ， 45mm版本的售…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/gta-v-playable-in-browser-immediately-nuked-unofficial-webassembly-port-built-with-ai-gets-taken-down-within-hours-of-going-live" target="_blank" rel="noopener" data-cat="zonghe" data-summary="目前尚不清楚是谁关闭了PlayGTA5.com ，但如果Take-Two看到该网站，可能会迅速采取行动。" data-title="GTA V playable in browser immediately nuked" data-date="10-06 21:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 21:50</span>
          <span class="news-item-title">GTA V可立即在浏览器中播放</span>
          <span class="news-item-title-en">GTA V playable in browser immediately nuked</span>
          <span class="news-value-point">💡 目前尚不清楚是谁关闭了PlayGTA5.com ，但如果Take-Two看到该网站，可能会迅速采取行动</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/107.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，据央视新闻报道，当地时间 5 日，在 77 届国际宇航大会（IAC 2026）上，中国首飞航天员、航天英雄、现任中国载人航天工程副总设计师杨利伟表示，中国空间站将成为一个面向全球科学家开放的实验平台。杨利伟透露，中国空间站后续可在科学研究、航天员培训、提供飞行机会，以及科普教育等方面，开展深化合作。IT之家从原报道获悉，中国空间站将在今年下半年，迎来首批外籍航天员。杨利伟介绍道：“这两名巴基斯坦的预备航天员，在整个训练过程当中，表现非常优异，正在和中国航天员进行配合训练。按照计划，一名巴基斯坦航天员将作为载荷专家，执行短期飞行任务。”此外，就中国载人登月计划，杨利伟表示，中国希望与各国展开合作交流。“将开展月球科学的研究与开发，建设月球的科研站。”" data-title="杨利伟：中国空间站将成全球开放实验平台，下半年迎来首批外籍航天员" data-date="10-06 21:48" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 21:48</span>
          <span class="news-item-title">杨利伟：中国空间站将成全球开放实验平台，下半年迎来首批外籍航天员</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，据央视新闻报道，当地时间 5 日，在 77 届国际宇航大会（IAC 2026）上，中国首飞航天员、航天英雄、现任…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/104.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，当地时间 10 月 6 日，亚马逊 Prime Video 与美国电视艺术与科学学院（Television Academy）联合宣布达成一项为期六年的合作协议，Prime Video 将获得艾美奖（Emmy Awards）的全球独家直播权。IT之家注：艾美奖始办于 1949 年，与奥斯卡金像奖、格莱美奖、托尼奖并称美国演艺界四大奖（EGOT）。自 2027 年起，用户可在 Prime Video 上免费观看艾美奖颁奖典礼直播 —— 这也标志着该典礼首次拥有一个专属的直播平台。官方表示，这项历史性协议的达成，标志着电视学院沿用已久由 ABC、CBS、FOX 和 NBC 四大商业地面电视广播网络（四大电视网）轮流转播的“轮播协议”（Wheel Deal）正式结束，" data-title="取代四大电视网“轮播模式”，亚马逊 Prime Video 拿下艾美奖全球独家直播权" data-date="10-06 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 21:32</span>
          <span class="news-item-title">取代四大电视网“轮播模式”，亚马逊 Prime Video 拿下艾美奖全球独家直播权</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，当地时间 10 月 6 日，亚马逊 Prime Video 与美国电视艺术与科学学院（Television Ac…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1005480/paramount-warner-bros-discovey-merger-closed" target="_blank" rel="noopener" data-cat="zonghe" data-summary="派拉蒙已完成以1100亿美元收购Warner Bros. Discovery ，组建了一家名为Skydance的合并公司。此次合并正式将派拉蒙和WBD的电影制片厂以及HBO、CBS新闻和CN等主要网络和品牌" data-title="Paramount and Warner Bros. Discovery complete $110 billion media megamerger" data-date="10-06 21:32" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 21:32</span>
          <span class="news-item-title">派拉蒙和华纳兄弟发现完成$ 1100亿媒体巨型合并</span>
          <span class="news-item-title-en">Paramount and Warner Bros. Discovery complete $110 billion media megamerger</span>
          <span class="news-value-point">💡 派拉蒙已完成以1100亿美元收购Warner Bros. Discovery ，组建了一家名为Skydance的合并公司</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/cd-players-are-back-with-modern-interesting-features-starting-as-low-as-usd89-here-are-some-of-the-best-and-most-interesting-new-models" target="_blank" rel="noopener" data-cat="zonghe" data-summary="CD销量在过去一年中增长了近60 ％ ，超过了黑胶唱片，并带来了大量有趣的新硬件。如果您想找一个新的驱动器来播放您的旧光盘，有很多有趣的选择。" data-title="CD players are back, and offering up modern, interesting features" data-date="10-06 21:28" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 21:28</span>
          <span class="news-item-title">CD播放器又回来了，并提供了现代、有趣的功能</span>
          <span class="news-item-title-en">CD players are back, and offering up modern, interesting features</span>
          <span class="news-value-point">💡 CD销量在过去一年中增长了近60 ％ ，超过了黑胶唱片，并带来了大量有趣的新硬件</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/996983/best-october-prime-day-deal-sale-tech" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊的Prime Big Deal Days活动已经开始，持续到美国东部时间10月8日星期四凌晨3点。我们已经浏览了公司的大量交易列表，以找到Verge读者会喜欢的产品（以及我们个人也喜欢的产品）。主要订阅者" data-title="The best October Prime Day tech deals we found" data-date="10-06 21:27" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 21:27</span>
          <span class="news-item-title">我们找到的最佳十月黄金日科技优惠</span>
          <span class="news-item-title-en">The best October Prime Day tech deals we found</span>
          <span class="news-value-point">💡 亚马逊的Prime Big Deal Days活动已经开始，持续到美国东部时间10月8日星期四凌晨3点</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1005436/amazon-prime-video-emmys-deal" target="_blank" rel="noopener" data-cat="zonghe" data-summary="艾美奖有了一个新家--看起来亚马逊为这些权利付出了很多。颁奖典礼和亚马逊宣布了一项为期六年的协议，将艾美奖从其传统的广播电视之家转移到Prime Video。轮班从20岁开始" data-title="Amazon reportedly pays $120 million to stream the Emmys for free" data-date="10-06 21:26" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 21:26</span>
          <span class="news-item-title">据报道，亚马逊支付1.2亿美元免费播放艾美奖</span>
          <span class="news-item-title-en">Amazon reportedly pays $120 million to stream the Emmys for free</span>
          <span class="news-value-point">💡 艾美奖有了一个新家--看起来亚马逊为这些权利付出了很多</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/103.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，任天堂现已在 eShop 平台推出两款 Switch 游戏《你好，碧姬公主！》（Hello, Peach!）《你好，路易吉！》（Hello, Luigi!），面向儿童用户。IT之家了解到，这两款作品属于“My Mario”系列产品。游戏内容正如标题所示，玩家可以使用 Switch 游戏机的触控屏，与碧姬公主或路易吉进行活动。同时，任天堂已在此前推出过《你好，马力欧！》和《你好，耀西！》游戏，如今“My Mario”系列作品已经有 4 款。此外，本次新上架的两款游戏无需网络连接即可游玩，未来还将登陆 iOS 和 Android 应用市场。" data-title="任天堂推出两款免费 Switch 游戏《你好，碧姬公主！》《你好，路易吉！》，面向儿童用户" data-date="10-06 21:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 21:24</span>
          <span class="news-item-title">任天堂推出两款免费 Switch 游戏《你好，碧姬公主！》《你好，路易吉！》，面向儿童用户</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，任天堂现已在 eShop 平台推出两款 Switch 游戏《你好，碧姬公主</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1005193/apple-screen-time-update-struggles-ios-27-parental-controls" target="_blank" rel="noopener" data-cat="zonghe" data-summary="After suffering years of frustration with Apple&#39;s parental control features, I&#39;ve been eagerly anticipating the revamped Screen Time that launched last month with iOS 27. Unfortunately, I can&#39;t use it. Technically, this is because my 18-year-old son hasn&#39;t got round to updating his MacBook. But mostly, it&#39;s because Apple&#39;s rollout of the new featur" data-title="I can’t use Apple’s new Screen Time on my daughter’s iPhone because my son won’t update his MacBook" data-date="10-06 21:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 21:15</span>
          <span class="news-item-title">我无法在女儿的iPhone上使用Apple的新屏幕时间，因为我的儿子不会更新他的MacBook</span>
          <span class="news-item-title-en">I can’t use Apple’s new Screen Time on my daughter’s iPhone because my son won’t update his MacBook</span>
          <span class="news-value-point">💡 After suffering years of frustration with Apple's parental control featu…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-06 22:23（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
