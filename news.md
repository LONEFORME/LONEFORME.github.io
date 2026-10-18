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
      <span>2026-10-19 00:01 抓取更新</span>
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
        <span class="channel-count">55</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">10</span>
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
  <div class="ov-item"><span class="ov-num">55</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×16 · BBC×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-18/10716887.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 中共中央政治局委员、国务院副总理何立峰10月18日晚在钓鱼台国宾馆会见中投公司国际咨询委员会委员。" data-title="何立峰会见中投公司国际咨询委员会委员" data-date="10-18 22:42" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-18 22:42</span>
      </div>
      <h2 class="hero-featured-title">何立峰会见中投公司国际咨询委员会委员</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/014/615.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 18 日消息，据科技媒体 TechSpot 今天报道，索尼最近申请一项专利，描绘以下场景：让 AI 在 GPU 完成渲染前预测下一帧画面，减少游戏画面卡顿，同时避免帧生成技术带来的额外延迟。IT之家从原报道获悉，这项技术能够解决帧生成的缺点，让显示画面不再等待两帧画面完成渲染，才能生成插入其中的中间帧。而是直接利用已经生成的画面预测下一帧，无需等待两帧画面就能插值，帮助游戏维持更稳定的帧输出节奏。同时，索尼使用了联合训练的编解码器，将渲染完成的画面转换为嵌入表示，对图像进行紧凑的数值化表达，让解码器利用这些提示生成预测帧。游戏运行时，该系统会与图形渲染管线并行工作。硬件渲染下一帧时，AI 会处理上一帧，并将预测结果发送至显示缓冲区。因此在下一帧完成渲染之前，预测画面就有可" data-title="索尼新专利曝光：AI 可在 GPU 渲染完成前预测下一帧画面，减少游戏卡顿" data-date="10-18 23:16" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">索尼新专利曝光：AI 可在 GPU 渲染完成前预测下一帧画面，减少游戏卡顿</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/18/nottingham-forest-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="来自城市场地的⚽更新；下午4:30 BST⚽分数|桌子|阅读足球日报|邮件DanielForest想要–并且可能需要–让这场比赛变得一团糟。如果它是开放的，并通过中场打球，阿森纳将开放他们，因为，" data-title="Nottingham Forest v Arsenal: Premier League" data-date="10-18 23:59" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Nottingham Forest v Arsenal: Premier League</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/10/18/world/europe/france-protests-shock-arson.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在反政府抗议活动陷入混乱之后，来自各政治派别的领导人互相指责骚乱，尽管骚乱在周日基本平息。" data-title="France in Shock After Protests Turn Into Riots, Damaging Buildings and Shops" data-date="10-18 23:48" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">France in Shock After Protests Turn Into Riots, Damaging Buildings and Shops</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716887.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 中共中央政治局委员、国务院副总理何立峰10月18日晚在钓鱼台国宾馆会见中投公司国际咨询委员会委员。" data-title="何立峰会见中投公司国际咨询委员会委员" data-date="10-18 22:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 22:42</span>
          <span class="news-item-title">何立峰会见中投公司国际咨询委员会委员</span>
          <span class="news-value-point">💡 中新社北京10月18日电 中共中央政治局委员、国务院副总理何立峰10月18日晚在钓鱼台国宾馆会见中投公司国际咨询委员会委员</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1013485/trump-google-kiss-my-ass" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月17日星期六，在肯塔基州高地高地举行的一次集会上，唐纳德·特朗普吹嘘他在第二个任期内有多么强大和有影响力。在列举他的成就时，他提到他决定将G" data-title="Trump says Google kisses his ass" data-date="10-18 21:25" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-18 21:25</span>
          <span class="news-item-title">特朗普说谷歌亲吻他的屁股</span>
          <span class="news-item-title-en">Trump says Google kisses his ass</span>
          <span class="news-value-point">💡 10月17日星期六，在肯塔基州高地高地举行的一次集会上，唐纳德·特朗普吹嘘他在第二个任期内有多么强大和有影响力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716841.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社杭州10月18日电 (林波)亚洲文化遗产保护联盟理事会第四次会议18日在浙江杭州举行。会上，批准埃及成为联盟伙伴国、哈萨克斯坦成为联盟观察员国。至此，联盟成员国、观察员国、伙伴国总数达到26个。" data-title="亚洲文化遗产保护联盟新增1观察员国1伙伴国" data-date="10-18 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 20:49</span>
          <span class="news-item-title">亚洲文化遗产保护联盟新增1观察员国1伙伴国</span>
          <span class="news-value-point">💡 中新社杭州10月18日电 (林波)亚洲文化遗产保护联盟理事会第四次会议18日在浙江杭州举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716840.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 近日，接连曝出的阁僚丑闻对高市内阁支持率产生持续冲击。日本共同社18日公布的最新民调结果显示，高市早苗内阁的支持率降至49.1%，自去年10月执政以来首次跌破50%，创新低。" data-title="丑闻缠身 高市内阁支持率创新低" data-date="10-18 20:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 20:45</span>
          <span class="news-item-title">丑闻缠身 高市内阁支持率创新低</span>
          <span class="news-value-point">💡 中新网10月18日电 近日，接连曝出的阁僚丑闻对高市内阁支持率产生持续冲击</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716748.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 当地时间10月17日，黑山总统米拉托维奇在采蒂涅会见中共中央政治局委员、外交部长王毅。" data-title="黑山总统米拉托维奇会见王毅" data-date="10-18 20:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 20:37</span>
          <span class="news-item-title">黑山总统米拉托维奇会见王毅</span>
          <span class="news-value-point">💡 中新社北京10月18日电 当地时间10月17日，黑山总统米拉托维奇在采蒂涅会见中共中央政治局委员、外交部长王毅</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716813.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="我在现场｜动人的泪光，也是洒向国际舞台的星光" data-title="动人的泪光，也是洒向国际舞台的星光" data-date="10-18 20:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 20:17</span>
          <span class="news-item-title">动人的泪光，也是洒向国际舞台的星光</span>
          <span class="news-value-point">💡 我在现场｜动人的泪光，也是洒向国际舞台的星光</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716802.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网昆明10月18日电 (记者 陈静)“作为民族院校，如何在‘教育、科技、人才’三位一体战略布局中找准坐标，在高校分类改革中彰显不可替代的价值？”18日，云南民族大学建校75周年高质量发展论坛在该校举行，这个由云南民族大学党委书记阮朝奇在开幕式上抛出的问题，成为当天与会者共同的议题。" data-title="民族院校如何彰显“不可替代”？云南民族大学75周年论坛寻路" data-date="10-18 20:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 20:05</span>
          <span class="news-item-title">民族院校如何彰显“不可替代”？云南民族大学75周年论坛寻路</span>
          <span class="news-value-point">💡 中新网昆明10月18日电 (记者 陈静)“作为民族院校，如何在‘教育、科技、人才’三位一体战略布局中找准坐标，在高校分类改革中彰显不可替代的价值</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社天津10月18日电 题：中国“职教出海”绘就国际合作新图景" data-title="中国“职教出海”绘就国际合作新图景" data-date="10-18 20:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 20:04</span>
          <span class="news-item-title">中国“职教出海”绘就国际合作新图景</span>
          <span class="news-value-point">💡 新华社天津10月18日电 题：中国“职教出海”绘就国际合作新图景</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716783.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海10月18日电 题：50名西藏定日少年上海研学：把红色故事、科技梦想“装进行囊”" data-title="50名西藏定日少年上海研学：把红色故事、科技梦想“装进行囊”" data-date="10-18 19:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 19:45</span>
          <span class="news-item-title">50名西藏定日少年上海研学：把红色故事、科技梦想“装进行囊”</span>
          <span class="news-value-point">💡 中新网上海10月18日电 题：50名西藏定日少年上海研学：把红色故事、科技梦想“装进行囊”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716676.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科10月18日电(记者 田冰)俄罗斯国防部18日通报称，俄防空系统在俄境内多地及黑海水域上空击落1015架乌克兰无人机。圣彼得堡市、列宁格勒州、莫斯科市当日遭大规模无人机袭击，导致人员伤亡、石油码头起火，部分地区电力中断。" data-title="俄罗斯多地遭大规模无人机袭击" data-date="10-18 17:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 17:27</span>
          <span class="news-item-title">俄罗斯多地遭大规模无人机袭击</span>
          <span class="news-value-point">💡 中新社莫斯科10月18日电(记者 田冰)俄罗斯国防部18日通报称，俄防空系统在俄境内多地及黑海水域上空击落1015架乌克兰无人机</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716715.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 综合俄罗斯媒体报道，俄罗斯国防部18日通报，自17日20时至18日8时，俄多个地区遭无人机袭击，俄防空部队在别尔哥罗德州、布良斯克州、列宁格勒州、莫斯科州等地及黑海上空拦截并击落1015架乌克兰无人机。" data-title="俄罗斯多地遭大规模无人机袭击" data-date="10-18 17:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 17:17</span>
          <span class="news-item-title">俄罗斯多地遭大规模无人机袭击</span>
          <span class="news-value-point">💡 中新网10月18日电 综合俄罗斯媒体报道，俄罗斯国防部18日通报，自17日20时至18日8时，俄多个地区遭无人机袭击，俄防空部队在别尔哥罗德州、…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716702.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 据伊朗媒体报道，伊朗议会18日通过线上会议投票，批准阿赫拉基出任伊朗新任国防部长。" data-title="伊朗议会：批准阿赫拉基出任伊朗国防部长" data-date="10-18 17:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 17:07</span>
          <span class="news-item-title">伊朗议会：批准阿赫拉基出任伊朗国防部长</span>
          <span class="news-value-point">💡 中新网10月18日电 据伊朗媒体报道，伊朗议会18日通过线上会议投票，批准阿赫拉基出任伊朗新任国防部长</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/18/us/maha-voters-republican-split.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="MAHA与MAGA的联盟激励了选民支持特朗普总统2024年的竞选活动。现在，有些人不太确定。" data-title="Some MAHA Voters in Arizona Question Their G.O.P. Ties" data-date="10-18 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 17:00</span>
          <span class="news-item-title">亚利桑那州的一些MAHA选民质疑他们与G.O.P.的关系</span>
          <span class="news-item-title-en">Some MAHA Voters in Arizona Question Their G.O.P. Ties</span>
          <span class="news-value-point">💡 MAHA与MAGA的联盟激励了选民支持特朗普总统2024年的竞选活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716699.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社东京10月17日电(记者李子越#8195;陈泽安)据日本共同社17日报道，日本和美国将于19日至29日在日本多地开展“利剑27”大规模联合军演，投入兵力总计接近6万人，引发日本国内广泛担忧与反对。" data-title="日美将举行大规模联合军演 引发广泛担忧与反对" data-date="10-18 16:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 16:54</span>
          <span class="news-item-title">日美将举行大规模联合军演 引发广泛担忧与反对</span>
          <span class="news-value-point">💡 新华社东京10月17日电(记者李子越#8195;陈泽安)据日本共同社17日报道，日本和美国将于19日至29日在日本多地开展“利剑27”大规模联合…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716697.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间17日，日本首相高市早苗以“内阁总理大臣”名义，向供奉二战甲级战犯的靖国神社供奉祭品。" data-title="一年4次向靖国神社献祭 高市要干什么？" data-date="10-18 16:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 16:49</span>
          <span class="news-item-title">一年4次向靖国神社献祭 高市要干什么？</span>
          <span class="news-value-point">💡 当地时间17日，日本首相高市早苗以“内阁总理大臣”名义，向供奉二战甲级战犯的靖国神社供奉祭品</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">10 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/014/615.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 18 日消息，据科技媒体 TechSpot 今天报道，索尼最近申请一项专利，描绘以下场景：让 AI 在 GPU 完成渲染前预测下一帧画面，减少游戏画面卡顿，同时避免帧生成技术带来的额外延迟。IT之家从原报道获悉，这项技术能够解决帧生成的缺点，让显示画面不再等待两帧画面完成渲染，才能生成插入其中的中间帧。而是直接利用已经生成的画面预测下一帧，无需等待两帧画面就能插值，帮助游戏维持更稳定的帧输出节奏。同时，索尼使用了联合训练的编解码器，将渲染完成的画面转换为嵌入表示，对图像进行紧凑的数值化表达，让解码器利用这些提示生成预测帧。游戏运行时，该系统会与图形渲染管线并行工作。硬件渲染下一帧时，AI 会处理上一帧，并将预测结果发送至显示缓冲区。因此在下一帧完成渲染之前，预测画面就有可" data-title="索尼新专利曝光：AI 可在 GPU 渲染完成前预测下一帧画面，减少游戏卡顿" data-date="10-18 23:16" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 23:16</span>
          <span class="news-item-title">索尼新专利曝光：AI 可在 GPU 渲染完成前预测下一帧画面，减少游戏卡顿</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，据科技媒体 TechSpot 今天报道，索尼最近申请一项专利，描绘以下场景：让 AI 在 GPU 完成渲染前预…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/614.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="华为 FreeClip 2 典藏版耳夹耳机今年 6 月 15 日正式开售，价格为 1499 元。今日京东可叠加 1200-100 元惊喜红包，大部分地区还可叠加政府补贴，实付 1146.8 元即可入手：领京东超级惊喜红包：点此领券（进入会场后大概率自动领）京东华为 FreeClip 2 典藏版耳夹耳机国补后 1146.8 元直达链接京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。典藏版与普通版主要区别为：配有独立 AI 实体按键（华为设备可唤醒小艺，苹果安卓可唤醒豆包 *）。充电舱为鎏光“球形珠宝盒”，采用真空镀膜工艺。耳机在盒内竖向并列摆放，更好拿取。耳机 C 形桥为“鎏光云感 C 桥”，带珠光质感。* 三方智能体具体信息详见：点此查看。这款新品于 6 月 1" data-title="1499 → 1146.8 元：华为 FreeClip 2 典藏版耳夹耳机京东国补新低" data-date="10-18 23:07" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 23:07</span>
          <span class="news-item-title">1499 → 1146.8 元：华为 FreeClip 2 典藏版耳夹耳机京东国补新低</span>
          <span class="news-value-point">💡 华为 FreeClip 2 典藏版耳夹耳机今年 6 月 15 日正式开售，价格为 1499 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/612.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 18 日消息，据首尔经济日报今日报道，三星电子将采用全球最大晶圆代工厂台积电的制造工艺，生产英伟达下一代定制高带宽内存（HBM）的核心组件 —— 基底裸片（base die）。在此之前，三星供应的所有 HBM 产品中，作为存储芯片的核心裸片（core die）与充当系统半导体的基底裸片，均由三星自主生产。如今三星决定接受英伟达的技术要求，调整 HBM 的一站式全包制造模式。业内消息人士 18 日称，英伟达已向三家 NVHBM 供应商 —— 三星电子、SK 海力士（000660.KS）和美光提出要求：使用台积电 3 纳米工艺制造基底裸片。英伟达同时要求，核心裸片统一采用代号 1c 的第六代 DRAM 工艺。NVHBM 基于第七代下一代 HBM 标准 HBM4E 架构开发，是" data-title="三星将采用台积电 3nm 工艺为英伟达生产下一代 HBM 基底裸片" data-date="10-18 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 22:51</span>
          <span class="news-item-title">三星将采用台积电 3nm 工艺为英伟达生产下一代 HBM 基底裸片</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，据首尔经济日报今日报道，三星电子将采用全球最大晶圆代工厂台积电的制造工艺，生产英伟达下一代定制高带宽内存（HB…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-shipment-worth-usd470-000-goes-missing-in-brazilian-airport-two-pallets-disappear-distributor-seeks-explanations-but-met-with-zero-answers" target="_blank" rel="noopener" data-cat="keji" data-summary="巴西电子和IT分销商Oderço声称， Zotac RTX 5090 GPU的两个托盘已抵达机场，但此后已完全消失。" data-title="Nvidia RTX 5090 shipment worth $470,000 goes missing in Brazilian airport" data-date="10-18 21:24" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-18 21:24</span>
          <span class="news-item-title">Nvidia RTX 5090在巴西机场丢失价值47万$的货物</span>
          <span class="news-item-title-en">Nvidia RTX 5090 shipment worth $470,000 goes missing in Brazilian airport</span>
          <span class="news-value-point">💡 巴西电子和IT分销商Oderço声称， Zotac RTX 5090 GPU的两个托盘已抵达机场，但此后已完全消失</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/chip-fab-engineering-game-goes-viral-in-taiwan-realistic-and-stressful-simulation-is-basically-a-horror-game-say-some-players" target="_blank" rel="noopener" data-cat="keji" data-summary="《半导体晶圆工厂工人的一天》是一款全新的3D网络游戏，在台湾流行开来。" data-title="Web-based chip fab engineering game goes viral in Taiwan" data-date="10-18 20:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-18 20:50</span>
          <span class="news-item-title">基于网络的芯片晶圆厂工程游戏在台湾大行其道</span>
          <span class="news-item-title-en">Web-based chip fab engineering game goes viral in Taiwan</span>
          <span class="news-value-point">💡 《半导体晶圆工厂工人的一天》是一款全新的3D网络游戏，在台湾流行开来</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/18/business/economy/economy-midterm-elections.html" target="_blank" rel="noopener" data-cat="keji" data-summary="通货膨胀率高，消费者支出强劲，似乎一切都取决于人工智能发生了什么。" data-title="3 Charts That Explain the Economy as Voters Head to the Polls" data-date="10-18 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 17:00</span>
          <span class="news-item-title">3张图表解释了选民前往投票站时的经济状况</span>
          <span class="news-item-title-en">3 Charts That Explain the Economy as Voters Head to the Polls</span>
          <span class="news-value-point">💡 通货膨胀率高，消费者支出强劲，似乎一切都取决于人工智能发生了什么</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crz65gwv8gv5o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="研究发现越来越多毕业生利用人工智能在求职申请中编造个人资讯。但有人认为他们别无选择。" data-title="“我申请了200份工作”" data-date="10-18 08:32" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 08:32</span>
          <span class="news-item-title">“我申请了200份工作”</span>
          <span class="news-value-point">💡 研究发现越来越多毕业生利用人工智能在求职申请中编造个人资讯</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/17/meta-removes-language-that-raised-scraping-and-ai-training-concerns/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta发言人坚称，更新后的条款并未反映Meta爬网方式的变化。" data-title="Meta removes language that raised scraping and AI training concerns" data-date="10-18 05:31" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-18 05:31</span>
          <span class="news-item-title">Meta删除了引起抓取和人工智能培训问题的语言</span>
          <span class="news-item-title-en">Meta removes language that raised scraping and AI training concerns</span>
          <span class="news-value-point">💡 Meta发言人坚称，更新后的条款并未反映Meta爬网方式的变化</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/17/anthropic-says-its-workforce-has-become-less-junior-and-is-spending-more-time-in-meetings/" target="_blank" rel="noopener" data-cat="keji" data-summary="在过去的一年中， Anthropic的员工构成和工作类型发生了显着变化。" data-title="Anthropic says its workforce has become less junior and is spending more time in meetings" data-date="10-18 04:21" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-18 04:21</span>
          <span class="news-item-title">Anthropic表示，其员工队伍已经变得不那么初级了，并且在会议上花费了更多的时间</span>
          <span class="news-item-title-en">Anthropic says its workforce has become less junior and is spending more time in meetings</span>
          <span class="news-value-point">💡 在过去的一年中， Anthropic的员工构成和工作类型发生了显着变化</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/" target="_blank" rel="noopener" data-cat="keji" data-summary="上周末， Masad澄清说， OpenAI将取代Anthropic作为其默认模型提供商。Claude仍将向平台上的客户提供服务。" data-title="Replit makes OpenAI its default over Anthropic, CEO says" data-date="10-18 02:48" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-18 02:48</span>
          <span class="news-item-title">首席执行官表示， Replit使OpenAI成为Anthropic的默认值</span>
          <span class="news-item-title-en">Replit makes OpenAI its default over Anthropic, CEO says</span>
          <span class="news-value-point">💡 上周末， Masad澄清说， OpenAI将取代Anthropic作为其默认模型提供商</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/18/nottingham-forest-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="来自城市场地的⚽更新；下午4:30 BST⚽分数|桌子|阅读足球日报|邮件DanielForest想要–并且可能需要–让这场比赛变得一团糟。如果它是开放的，并通过中场打球，阿森纳将开放他们，因为，" data-title="Nottingham Forest v Arsenal: Premier League" data-date="10-18 23:59" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:59</span>
          <span class="news-item-title">诺丁汉森林v阿森纳：英超联赛</span>
          <span class="news-item-title-en">Nottingham Forest v Arsenal: Premier League</span>
          <span class="news-value-point">💡 来自城市场地的⚽更新</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/18/leeds-v-manchester-united-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利兹的多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）取消了布莱恩·姆贝乌莫（ Bryan Mbeumo ）的⚽揭幕战，为参观者结束了动荡的一周六人的喜悦：利兹对曼联的比赛利兹经理丹尼尔·法克（ Daniel Farke ）是下一位与天空体育（ Sky Sports ）交谈的人：我们必须确保" data-title="Leeds United 1-1 Manchester United: Premier League – as it happened" data-date="10-18 23:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:25</span>
          <span class="news-item-title">利兹联队1-1曼联：英超联赛–实际情况</span>
          <span class="news-item-title-en">Leeds United 1-1 Manchester United: Premier League – as it happened</span>
          <span class="news-value-point">💡 利兹的多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）取消了布莱恩·姆贝乌莫（ Bryan Mbeumo ）的⚽揭幕战…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/bournemouth-sunderland-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="伯恩茅斯和马可·罗斯对英超联赛胜利的期待已经结束。被锁定在倒数三名的桑德兰，正在成为本赛季旅行太快的客观教训。上赛季的第六和第七场比赛，两支球队都在国内挣扎" data-title="Evanilson swivels his hips to seal Bournemouth win against 10" data-date="10-18 23:19" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:19</span>
          <span class="news-item-title">埃文尼尔森旋转臀部，以封印伯恩茅斯对10的胜利</span>
          <span class="news-item-title-en">Evanilson swivels his hips to seal Bournemouth win against 10</span>
          <span class="news-value-point">💡 伯恩茅斯和马可·罗斯对英超联赛胜利的期待已经结束</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/leeds-manchester-united-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克和曼联的下一步是什么？从游戏角度来看，答案是周三的COMO之旅，但是在再次失败之后，为了将竞选活动的联赛胜利增加一倍，你必须想知道这支已经扁平化的球队将走向何方。周日" data-title="Manchester United held as Calvert-Lewin’s Leeds leveller keeps pressure on Carrick" data-date="10-18 23:08" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:08</span>
          <span class="news-item-title">曼联举行，卡尔弗特-莱温的利兹均衡器对卡里克施加压力</span>
          <span class="news-item-title-en">Manchester United held as Calvert-Lewin’s Leeds leveller keeps pressure on Carrick</span>
          <span class="news-value-point">💡 迈克尔·卡里克和曼联的下一步是什么</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckvg7v43x1xyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）的下半场均衡器意味着曼联自2019年以来首次在六场比赛中没有获胜-找出谁在埃兰路（ Elland Road ）得分最高。" data-title="Everything a struggle for Fernandes - Leeds v Man Utd ratings" data-date="10-18 22:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 22:56</span>
          <span class="news-item-title">一切都是费尔南德斯的斗争-利兹v曼联评级</span>
          <span class="news-item-title-en">Everything a struggle for Fernandes - Leeds v Man Utd ratings</span>
          <span class="news-value-point">💡 多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）的下半场均衡器意味着曼联自2019年以来首次在六场比赛中没有获胜-找出…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/how-to-watch-premier-league-nottingham-forest-arsenal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队和阿森纳队今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项。而本赛季英超冠军争夺战的真正风险要等到曼城的结果才能确定。" data-title="Premier League today: How to watch Nottingham Forest v Arsenal, TV channels &amp; live stream" data-date="10-18 18:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 18:30</span>
          <span class="news-item-title">今日英超联赛：如何观看Nottingham Forest v Arsenal、电视频道和直播</span>
          <span class="news-item-title-en">Premier League today: How to watch Nottingham Forest v Arsenal, TV channels & live stream</span>
          <span class="news-value-point">💡 诺丁汉森林队和阿森纳队今天的表现如何</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cked3vl198eyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西守门员埃米利亚诺·马丁内斯（ Emiliano Martinez ）表示，在与贾拉德·布兰斯韦特（ Jarrad Branthwaite ）相撞后，他将在“几周内”回来。" data-title="Martinez breaks jaw in Chelsea win at Everton" data-date="10-18 17:42" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 17:42</span>
          <span class="news-item-title">马丁内斯打破切尔西在埃弗顿的胜利</span>
          <span class="news-item-title-en">Martinez breaks jaw in Chelsea win at Everton</span>
          <span class="news-value-point">💡 切尔西守门员埃米利亚诺·马丁内斯（ Emiliano Martinez ）表示，在与贾拉德·布兰斯韦特（ Jarrad Branthwaite …</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck054652mv07o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉是一支球队，约翰·曼赞比（ Johan Manzambi ）在对阵纽卡斯尔队的比赛中得分，他拒绝转会到维拉公园（ Villa Park ）。" data-title="Villa&#39;s Manzambi shows Newcastle what they missed out on" data-date="10-18 05:18" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 05:18</span>
          <span class="news-item-title">别墅的Manzambi向纽卡斯尔展示了他们错过的景点</span>
          <span class="news-item-title-en">Villa's Manzambi shows Newcastle what they missed out on</span>
          <span class="news-value-point">💡 阿斯顿维拉是一支球队，约翰·曼赞比（ Johan Manzambi ）在对阵纽卡斯尔队的比赛中得分，他拒绝转会到维拉公园（ Villa Park…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9j34rke27zjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="弗洛里安·维尔茨（ Florian Wirtz ）在利物浦重返英超联赛的胜利之路上发挥了重要作用，但他仍然是老板安东尼·伊拉奥拉（ Andoni Iraola ）的大难题" data-title="Wirtz delivers but remains Liverpool&#39;s conundrum" data-date="10-18 04:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 04:07</span>
          <span class="news-item-title">Wirtz取得了成功，但仍是利物浦的难题</span>
          <span class="news-item-title-en">Wirtz delivers but remains Liverpool's conundrum</span>
          <span class="news-value-point">💡 弗洛里安·维尔茨（ Florian Wirtz ）在利物浦重返英超联赛的胜利之路上发挥了重要作用，但他仍然是老板安东尼·伊拉奥拉（ Andoni…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/cwdd897vvl8vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="约翰·曼赞比（ Johan Manzambi ）率领阿斯顿维拉（ Aston Villa ）战胜纽卡斯尔（ Newcastle ） ，标志着经理乌奈·埃默里（ Unai Emer" data-title="Manzambi heads Villa to victory at Newcastle" data-date="10-18 03:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 03:12</span>
          <span class="news-item-title">Manzambi带领别墅在纽卡斯尔取得胜利</span>
          <span class="news-item-title-en">Manzambi heads Villa to victory at Newcastle</span>
          <span class="news-value-point">💡 约翰·曼赞比（ Johan Manzambi ）率领阿斯顿维拉（ Aston Villa ）战胜纽卡斯尔（ Newcastle ） ，标志着经理…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/c65yn28p859wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦队在Gtech社区体育场以2比1击败布伦特福德队，东道主在Yehor Yarmoliuk和Vitaly Janelt的红牌后以9名男子结束比赛。" data-title="Liverpool come from behind to beat nine" data-date="10-18 03:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 03:00</span>
          <span class="news-item-title">利物浦从后面来到九强</span>
          <span class="news-item-title-en">Liverpool come from behind to beat nine</span>
          <span class="news-value-point">💡 利物浦队在Gtech社区体育场以2比1击败布伦特福德队，东道主在Yehor Yarmoliuk和Vitaly Janelt的红牌后以9名男子结束…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/c6pwgx89djn2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城在英超联赛中取得6分，恩佐·马雷斯卡（ Enzo Maresca ）的球队在阿提哈德以3-2战胜伊普斯维奇（ Ipswich ） ，连续第七次取得联赛胜利。" data-title="Haaland nets double as Man City go six points clear at the top" data-date="10-18 03:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 03:00</span>
          <span class="news-item-title">哈兰德篮网是曼城的两倍，在顶部得到6分</span>
          <span class="news-item-title-en">Haaland nets double as Man City go six points clear at the top</span>
          <span class="news-value-point">💡 曼城在英超联赛中取得6分，恩佐·马雷斯卡（ Enzo Maresca ）的球队在阿提哈德以3-2战胜伊普斯维奇（ Ipswich ） ，连续第七…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/newcastle-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="约翰·曼赞比（ Johan Manzambi ）在圣詹姆斯公园（ St James ’Park ）打进了给阿斯顿维拉（ Aston Villa ）应得胜利的唯一进球提醒球队看起来乔·威洛克（ Joe Willock ）将为纽卡斯尔（ Newcastle ）效力，乔林顿（ Joelinton ）与尼科·冈萨雷斯（ Nico Gonzalez ）并列中场。纽卡斯尔" data-title="Newcastle 0-1 Aston Villa: Premier League – as it happened" data-date="10-18 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 03:00</span>
          <span class="news-item-title">纽卡斯尔0-1阿斯顿维拉：英超联赛–事实如此</span>
          <span class="news-item-title-en">Newcastle 0-1 Aston Villa: Premier League – as it happened</span>
          <span class="news-value-point">💡 约翰·曼赞比（ Johan Manzambi ）在圣詹姆斯公园（ St James ’Park ）打进了给阿斯顿维拉（ Aston Villa …</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/cq146nz03k16o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="佩德罗·内托（ Pedro Neto ）在希尔·狄金森体育场（ Hill Dickinson Stadium ）以2比0击败埃弗顿（ Everton ）时为切尔西（ Chelsea ）得分两次，这场比赛因埃米利亚诺·马丁内斯（ Emiliano" data-title="Neto scores twice as Chelsea win at Everton" data-date="10-18 03:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 03:00</span>
          <span class="news-item-title">内托在埃弗顿的得分是切尔西的两倍</span>
          <span class="news-item-title-en">Neto scores twice as Chelsea win at Everton</span>
          <span class="news-value-point">💡 佩德罗·内托（ Pedro Neto ）在希尔·狄金森体育场（ Hill Dickinson Stadium ）以2比0击败埃弗顿（ Evert…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/17/newcastle-aston-villa-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉如此迫切地想要劫持约翰·曼赞比（ Johan Manzambi ）从弗莱堡（ Freiburg ）到纽卡斯尔（ Newcastle ）的夏季搬迁计划是有原因的。这位身材高大、快速、棘手、聪明、完美平衡的21岁瑞士进攻型中场球员看起来物有所值" data-title="Manzambi maintains Aston Villa progress with win to seal dismal week for Newcastle" data-date="10-18 02:38" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 02:38</span>
          <span class="news-item-title">曼赞比保持阿斯顿维拉的进步，赢得纽卡斯尔令人沮丧的一周</span>
          <span class="news-item-title-en">Manzambi maintains Aston Villa progress with win to seal dismal week for Newcastle</span>
          <span class="news-value-point">💡 阿斯顿维拉如此迫切地想要劫持约翰·曼赞比（ Johan Manzambi ）从弗莱堡（ Freiburg ）到纽卡斯尔（ Newcastle ）…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/10/18/world/europe/france-protests-shock-arson.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在反政府抗议活动陷入混乱之后，来自各政治派别的领导人互相指责骚乱，尽管骚乱在周日基本平息。" data-title="France in Shock After Protests Turn Into Riots, Damaging Buildings and Shops" data-date="10-18 23:48" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 23:48</span>
          <span class="news-item-title">法国在抗议活动演变成骚乱、破坏建筑物和商店后感到震惊</span>
          <span class="news-item-title-en">France in Shock After Protests Turn Into Riots, Damaging Buildings and Shops</span>
          <span class="news-value-point">💡 在反政府抗议活动陷入混乱之后，来自各政治派别的领导人互相指责骚乱，尽管骚乱在周日基本平息</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/619.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="荣耀新一代 Earbuds 耳夹式耳机将于今日开售，定价 499 元，首发到手价 449 元。评价返 10 元 E 卡（折合仅需 439 元），学生可再享 30 元教育优惠。部分地区支持政府补贴（例如广东），实付低至 382 元，评价后折合 372 元：京东荣耀 Earbuds 耳夹式耳机抢先购首发 449 元直达链接京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。这款耳机主打全天候舒适佩戴，耳挂采用食品级亲肤硅胶，搭配天鹅颈曲线设计；单只耳机重 5.6 克，C 桥最窄处 3.2mm；获得 Hi-Res Wireless 金标认证，支持 LHDC 5.0 无损格式。IT之家获悉，这款耳机综合续航可达 40 小时，单次连续听歌可达 10 小时，充电 10 分钟即可" data-title="首发即国补：荣耀 Earbuds 耳夹式耳机 499 → 378 元，全天候舒适佩戴" data-date="10-18 23:47" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 23:47</span>
          <span class="news-item-title">首发即国补：荣耀 Earbuds 耳夹式耳机 499 → 378 元，全天候舒适佩戴</span>
          <span class="news-value-point">💡 荣耀新一代 Earbuds 耳夹式耳机将于今日开售，定价 499 元，首发到手价 449 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/616.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，据央视财经今日报道，近日，国家电影局、体育总局联合印发《关于开展“跟着电影去运动”行动推动电影与体育双向赋能的通知》。在促进消费联动方面，支持电影院、体育场馆、体育赛事举办方、互联网平台企业、商业银行、支付结算机构等联合开展“电影 + 体育”促消费活动，推出观影与赛事票根联动、消费满减等优惠举措；鼓励结合电影场景，打造徒步、骑行、自驾等特色户外运动线路；支持电影、体育衍生产品联名合作；支持打造电影、运动市集，双向融入体育、电影元素。在影院场景拓展方面，鼓励在电影院设置体育主题影厅，打造观赛“第二现场”，利用电影院空闲时段开展重大体育赛事直播；鼓励利用虚拟现实电影技术，提供沉浸式体育项目体验；支持体育运动进影院，探索在符合条件的电影院开展适宜的运动项目。IT之" data-title="两部门：鼓励利用电影院空闲时段开展重大体育赛事直播" data-date="10-18 23:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 23:25</span>
          <span class="news-item-title">两部门：鼓励利用电影院空闲时段开展重大体育赛事直播</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，据央视财经今日报道，近日，国家电影局、体育总局联合印发《关于开展“跟着电影去运动”行动推动电影与体育双向赋能的…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/anycubics-award-winning-3d-printer-hits-all-time-low-pricing-kobra-x-is-an-excellent-entry-level-four-color-printer-thats-now-just-usd299-99-for-amazon-prime-members" target="_blank" rel="noopener" data-cat="zonghe" data-summary="编辑推荐Anycubic Kobra X多色3D打印机是我们见过的最低价格。" data-title="Anycubic&#39;s award-winning 3D printer hits all-time low pricing" data-date="10-18 23:24" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-18 23:24</span>
          <span class="news-item-title">Anycubic屡获殊荣的3D打印机价格创历史新低</span>
          <span class="news-item-title-en">Anycubic's award-winning 3D printer hits all-time low pricing</span>
          <span class="news-value-point">💡 编辑推荐Anycubic Kobra X多色3D打印机是我们见过的最低价格</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716906.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国庆后的南京红山森林动物园，" data-title="周杰伦家在大陆有大鹿" data-date="10-18 23:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 23:21</span>
          <span class="news-item-title">周杰伦家在大陆有大鹿</span>
          <span class="news-value-point">💡 国庆后的南京红山森林动物园，</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/18/nyregion/nyc-ice-shooting-oscar-belgal.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Oscar Belgal于2022年从多米尼加共和国来到这座城市。混乱似乎随之而来，以与移民局特工的致命遭遇而告终。" data-title="How a Dominican Man Became an ICE Target Before the NYC Shooting" data-date="10-18 23:20" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 23:20</span>
          <span class="news-item-title">多米尼加男子如何在纽约枪击事件前成为ICE目标</span>
          <span class="news-item-title-en">How a Dominican Man Became an ICE Target Before the NYC Shooting</span>
          <span class="news-value-point">💡 Oscar Belgal于2022年从多米尼加共和国来到这座城市</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/article/france-student-protests-why.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="周末，骚乱者袭击了市政厅和商店，抗议生活费用和学校条件恶劣。" data-title="Why Are There Protests in France?" data-date="10-18 23:15" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 23:15</span>
          <span class="news-item-title">法国为什么会发生抗议活动？</span>
          <span class="news-item-title-en">Why Are There Protests in France?</span>
          <span class="news-value-point">💡 周末，骚乱者袭击了市政厅和商店，抗议生活费用和学校条件恶劣</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/brighton-crystal-palace-premier-league-match-report" target="_blank" rel="noopener" data-cat="zonghe" data-summary="最后， Fabian Hürzeler以羞辱的方式拥有对所有布莱顿球迷来说最重要的头皮。迭戈·戈麦斯（ Diego Gómez ）从大卫·贝克汉姆（ David Beckham ）出发的令人叹为观止的赛季中线进球者，是另一个令人印象深刻的亮点" data-title="Gómez halfway-line wondergoal sparks Brighton’s 5-0 thrashing of sorry Crystal Palace" data-date="10-18 23:06" data-source="卫报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:06</span>
          <span class="news-item-title">戈麦斯（ Gómez ）中线奇观引发了布莱顿（ Brighton ） 5-0的遗憾水晶宫（ Crystal Palace ）</span>
          <span class="news-item-title-en">Gómez halfway-line wondergoal sparks Brighton’s 5-0 thrashing of sorry Crystal Palace</span>
          <span class="news-value-point">💡 最后， Fabian Hürzeler以羞辱的方式拥有对所有布莱顿球迷来说最重要的头皮</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/f-22-raptor-pilot-successfully-demonstrates-command-of-wingman-fighter-drone-in-simulated-combat-anduril-yfq-44a-fury-test-advances-usafs-program-to-integrate-uncrewed-aircraft-into-fighter-squadrons" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国空军的最新测试证明， F-22 “猛禽”战斗机可以在战斗条件下指挥YFQ-44A “狂怒”无人机。" data-title="F-22 Raptor pilot successfully demonstrates command of &#39;wingman&#39; fighter drone in simulated combat" data-date="10-18 23:02" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-18 23:02</span>
          <span class="news-item-title">F-22猛禽飞行员在模拟战斗中成功演示“僚机”战斗机的指挥</span>
          <span class="news-item-title-en">F-22 Raptor pilot successfully demonstrates command of 'wingman' fighter drone in simulated combat</span>
          <span class="news-value-point">💡 美国空军的最新测试证明， F-22 “猛禽”战斗机可以在战斗条件下指挥YFQ-44A “狂怒”无人机</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/613.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，彭博社记者马克 · 古尔曼在最新一期《Power On》通讯中透露，苹果明知 iPhone Duo 折叠屏手机面临严重的供应短缺，却仍然决定本周五开启预购，而不是等到备货更加充足时再启动预购。古尔曼表示：我就直说了：苹果这次犯了一个重大错误。他们明明知道供应严重受限，却坚持按计划推出 iPhone Duo。比起满足市场需求，苹果更希望在第一财季初期让这款设备上市。这将让许多希望首批购买的用户感到失望。IT之家注意到，古尔曼还透露，苹果最初仅计划在美国和中国推出 iPhone Duo，然后再扩展至其他国家或地区。但最终，苹果选择在全球 70 多个国家或地区同步开启预购。10 月 16 日预售开启不到 30 分钟，全球多地的 iPhone Duo 预计发货日期就" data-title="古尔曼：苹果明知 iPhone Duo 折叠屏手机供应不足，却坚持周五启动预售" data-date="10-18 23:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 23:01</span>
          <span class="news-item-title">古尔曼：苹果明知 iPhone Duo 折叠屏手机供应不足，却坚持周五启动预售</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，彭博社记者马克 · 古尔曼在最新一期《Power On》通讯中透露，苹果明知 iPhone Duo 折叠屏手机…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1013436/lenovo-legion-go-s-steamos-handheld-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="使用SteamOS的Legion Go S是$ 789 Steam Deck OLED的坚实替代品。它运行相同的软件，但附带两级触发器的设计，更大的8英寸IPS屏幕（ 1080p ，最高120Hz ，而甲板上为800p和90Hz ）" data-title="Lenovo’s fast, comfy SteamOS handheld is hundreds off" data-date="10-18 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-18 23:00</span>
          <span class="news-item-title">联想快速舒适的SteamOS手持设备</span>
          <span class="news-item-title-en">Lenovo’s fast, comfy SteamOS handheld is hundreds off</span>
          <span class="news-value-point">💡 使用SteamOS的Legion Go S是$ 789 Steam Deck OLED的坚实替代品</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/611.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，彭博社记者马克 · 古尔曼今天在最新一期《Power On》通讯中透露，苹果计划推出一款配备电动机械臂的 HomeView 智能家庭中枢，最快 2027 年发布。据介绍，这款产品将搭载电动机械臂，能够围绕底座旋转 360 度，并通过语音识别自动转向说话的人。新款 HomeView 预计将配备 9 英寸屏幕，可能会更像一款陪伴型产品。IT之家从原报道获悉，这款产品并非 HomeView 的直接继任机型，而是定位更高端的版本，其代号为 J595。古尔曼透露，该产品上市时可能会采用新名称，也可能只是在 HomeView 后面加上“Max”或“Ultra”等后缀。事实上，苹果在机械臂方面的布局已有数年历史。2024 年曾有传闻称，苹果计划把造车项目的机器人技术延续到" data-title="古尔曼：苹果计划为 HomeView 智能家庭中枢配备电动机械臂，最早 2027 年推出" data-date="10-18 22:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 22:44</span>
          <span class="news-item-title">古尔曼：苹果计划为 HomeView 智能家庭中枢配备电动机械臂，最早 2027 年推出</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，彭博社记者马克 · 古尔曼今天在最新一期《Power On》通讯中透露，苹果计划推出一款配备电动机械臂的 Ho…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716886.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月18日电 (记者 陈杭)四足机器人调整重心稳步通过断桥、人形机器人拾取灭火器对准模拟火源喷射……2026机器人勇士挑战赛秋季赛18日在北京举办，全国29支赛队现场“闯关”实景作业。" data-title="断桥与灭火成考场 机器人在北京闯关“实景作业”" data-date="10-18 22:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 22:42</span>
          <span class="news-item-title">断桥与灭火成考场 机器人在北京闯关“实景作业”</span>
          <span class="news-value-point">💡 中新社北京10月18日电 (记者 陈杭)四足机器人调整重心稳步通过断桥、人形机器人拾取灭火器对准模拟火源喷射……2026机器人勇士挑战赛秋季赛1…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/610.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果 AirPods 5 支持主动降噪，国行定价 999 元起。苹果 AirPods Pro 第三代支持升级版主动降噪 + 心率传感功能，国行定价 1899 元。京东目前支持 广东、江苏、北京、湖南、吉林、河北、云南、四川、大连 政府补贴 15%，收货地址在上述地区即可。AirPods Pro (第三代) 今日叠加国补后仅需 1316 元：京东 AirPods Pro 第三代搭配 MagSafe 充电盒国补后 1316 元直达链接京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。京东 PLUS 目前可领 100、125 元 AirPods 5 加补券，10 月 20 日可用：点此领券。如果在 20 日叠加百元 PLUS 券，AirPods 5 国补后预计仅需 75" data-title="新增广东湖南：苹果 AirPods 国补 15%，5 代 758 元起、Pro 3 仅 1316 元" data-date="10-18 22:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 22:40</span>
          <span class="news-item-title">新增广东湖南：苹果 AirPods 国补 15%，5 代 758 元起、Pro 3 仅 1316 元</span>
          <span class="news-value-point">💡 苹果 AirPods 5 支持主动降噪，国行定价 999 元起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716876.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月18日电(蓝伊旎)10月17日至18日，全国极弱磁技术及应用标准化工作组(SAC/SWG44)(以下简称“工作组”)成立大会暨第一次全体委员会议在杭州召开，标志着极弱磁领域标准化工作迈入体系化、规范化、国际化新阶段。" data-title="国家级极弱磁标准化工作组落户浙江 体系化发展提速" data-date="10-18 22:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 22:29</span>
          <span class="news-item-title">国家级极弱磁标准化工作组落户浙江 体系化发展提速</span>
          <span class="news-value-point">💡 中新网杭州10月18日电(蓝伊旎)10月17日至18日，全国极弱磁技术及应用标准化工作组(SAC/SWG44)(以下简称“工作组”)成立大会暨第…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-19 00:01（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
