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
      <span>2026-10-25 15:02 抓取更新</span>
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
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">57</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · BBC×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-25/10720681.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社福州10月25日电 (记者 朱贺 刘子衿)中国国民党前主席洪秀柱25日在福建福州表示，台湾前途系于中华民族伟大复兴，台湾同胞福祉离不开两岸和平发展。期盼台湾青年朋友找回身为堂堂正正中国人的骄傲，两岸同胞共同传承抗日先贤守护国土的精神。" data-title="纪念台湾光复81周年 洪秀柱盼共同传承先贤守护国土精神" data-date="10-25 14:58" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-25 14:58</span>
      </div>
      <h2 class="hero-featured-title">纪念台湾光复81周年 洪秀柱盼共同传承先贤守护国土精神</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/600.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 25 日消息，据 SteamDB 数据，《赛博朋克 2077》游戏 2.5 版本更新后，Steam 平台 24 小时内同时在线玩家峰值达 162291 人，创下近 3 年来的最高纪录。值得注意的是，本作上一次取得如此高的关注度，还是《往日之影》资料片推出以后。2023 年 10 月，《赛博朋克 2077》的同时在线玩家峰值曾突破 27.4 万人。IT之家注意到，本次更新带来了双持武器、新服装等特性，并新增一项任务，其内容可作为《边缘行者 2》动画的前传。此外，CDPR 现在还为本作带来了 3 折优惠，Steam 国区现价 89.4 元（https://store.steampowered.com/app/1091500/%E8%B5%9B%E5%8D%9A%E6%9C%8" data-title="《赛博朋克 2077》游戏 2.5 更新后 Steam 峰值突破 16.2 万，创三年来新高" data-date="10-25 14:43" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">《赛博朋克 2077》游戏 2.5 更新后 Steam 峰值突破 16.2 万，创三年来新高</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ck78p37y5508o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫击败后的评论表明，目前管理俱乐部是多么困难。" data-title="What Man Utd need now is stability, not more changes" data-date="10-25 14:34" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">What Man Utd need now is stability, not more changes</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/603.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，曜越现已在京东上架“AX600 Pro”机箱，该机箱采用商务风格外形设计，定价为 899 元。该机箱尺寸为 555x250x650mm，支持 M-ITX、ATX、E-ATX 至 HPTX 等多种主板规格，机箱外部采用多面散热孔设计，底部配备了滚轮。I/O 方面其顶部提供 1 个 USB-C 接口、2 个 USB-A 3.0 接口以及 1 个 3.5mm 音频接口。该机箱支持安装双 ATX 电源，配备可拆卸电源架，电源限长为 180mm。CPU 散热器限高 180mm，VGA 显卡限长为 400mm。提供 10 PCS 的 PCI 插槽。该机箱在标配状态下底板支持四块 3.5&quot; HDD 或四个 2.5&quot; SSD，电源仓支持一块 2.5&quot; SSD，主板后侧支持一" data-title="曜越推出 AX600 Pro 机箱：提供多达 20 个风扇位，899 元" data-date="10-25 15:02" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">曜越推出 AX600 Pro 机箱：提供多达 20 个风扇位，899 元</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720681.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社福州10月25日电 (记者 朱贺 刘子衿)中国国民党前主席洪秀柱25日在福建福州表示，台湾前途系于中华民族伟大复兴，台湾同胞福祉离不开两岸和平发展。期盼台湾青年朋友找回身为堂堂正正中国人的骄傲，两岸同胞共同传承抗日先贤守护国土的精神。" data-title="纪念台湾光复81周年 洪秀柱盼共同传承先贤守护国土精神" data-date="10-25 14:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:58</span>
          <span class="news-item-title">纪念台湾光复81周年 洪秀柱盼共同传承先贤守护国土精神</span>
          <span class="news-value-point">💡 中新社福州10月25日电 (记者 朱贺 刘子衿)中国国民党前主席洪秀柱25日在福建福州表示，台湾前途系于中华民族伟大复兴，台湾同胞福祉离不开两岸…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720676.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网太原10月25日电 (记者 范丽芳 杨静)10月24日下午，中共山西省委新闻发布会在太原举行，深入介绍和解读省第十三次党代会精神。省委常委、秘书长王帅红作主旨发布，就省第十三次党代会的总体情况、重要成果、主要精神等分别作了介绍。" data-title="中共山西省委举行新闻发布会 介绍和解读省第十三次党代会精神" data-date="10-25 14:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:40</span>
          <span class="news-item-title">中共山西省委举行新闻发布会 介绍和解读省第十三次党代会精神</span>
          <span class="news-value-point">💡 中新网太原10月25日电 (记者 范丽芳 杨静)10月24日下午，中共山西省委新闻发布会在太原举行，深入介绍和解读省第十三次党代会精神</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720675.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥10月25日电 (记者 赵强)安徽省马鞍山市第十七届人民代表大会第七次会议25日举行，会议选举阙方俊为马鞍山市人民政府市长。" data-title="阙方俊当选为安徽省马鞍山市市长" data-date="10-25 14:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:32</span>
          <span class="news-item-title">阙方俊当选为安徽省马鞍山市市长</span>
          <span class="news-value-point">💡 中新网合肥10月25日电 (记者 赵强)安徽省马鞍山市第十七届人民代表大会第七次会议25日举行，会议选举阙方俊为马鞍山市人民政府市长</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720671.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网温州10月25日电(鲍梦妮)10月24日至25日，2026世界青年科学家峰会深海资源环境论坛在浙江温州举行。" data-title="2026青科会深海资源环境论坛举行 各国专家共话深海开发保护" data-date="10-25 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:14</span>
          <span class="news-item-title">2026青科会深海资源环境论坛举行 各国专家共话深海开发保护</span>
          <span class="news-value-point">💡 中新网温州10月25日电(鲍梦妮)10月24日至25日，2026世界青年科学家峰会深海资源环境论坛在浙江温州举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720667.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="1950年10月25日" data-title="76年了，我们永远不能忘记！" data-date="10-25 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:08</span>
          <span class="news-item-title">76年了，我们永远不能忘记！</span>
          <span class="news-value-point">💡 1950年10月25日</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720638.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="24日晚，日本民众在东京都新宿车站前举行集会，反对高市政府推动修改“无核三原则”。民众表示，修改“无核三原则”不可接受，日本若引进核潜艇等核武器，将给东亚地区局势带来不稳定性。" data-title="日本民众举行集会 反对修改“无核三原则”" data-date="10-25 13:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 13:34</span>
          <span class="news-item-title">日本民众举行集会 反对修改“无核三原则”</span>
          <span class="news-value-point">💡 24日晚，日本民众在东京都新宿车站前举行集会，反对高市政府推动修改“无核三原则”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720636.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社石家庄10月24日电(记者赵瀚泽、龚璟璐)来华出席2026全球治理论坛(雄安)的联合国副秘书长盖·莱德24日在河北雄安新区接受记者采访时表示，中国在全球治理中发挥着关键作用，四大全球倡议同联合国目标高度契合。中国面向未来的前瞻性眼光令人印象深刻，这正是国际社会所需要的。" data-title="联合国副秘书长在雄安赞赏中国面向未来的前瞻性眼光" data-date="10-25 13:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 13:27</span>
          <span class="news-item-title">联合国副秘书长在雄安赞赏中国面向未来的前瞻性眼光</span>
          <span class="news-value-point">💡 新华社石家庄10月24日电(记者赵瀚泽、龚璟璐)来华出席2026全球治理论坛(雄安)的联合国副秘书长盖·莱德24日在河北雄安新区接受记者采访时表…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720602.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网布鲁塞尔10月25日电 (记者 德永健)比利时首都布鲁塞尔著名景点“撒尿小童”24日换上唐装，庆祝中比建交55周年。" data-title="比利时“撒尿小童”换唐装庆祝中比建交55周年" data-date="10-25 12:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 12:17</span>
          <span class="news-item-title">比利时“撒尿小童”换唐装庆祝中比建交55周年</span>
          <span class="news-value-point">💡 中新网布鲁塞尔10月25日电 (记者 德永健)比利时首都布鲁塞尔著名景点“撒尿小童”24日换上唐装，庆祝中比建交55周年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720600.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦10月25日电 (记者 欧阳开宇)2026年伦敦世界旅游交易会(WTM)将于11月3日至5日在英国伦敦皇家维多利亚码头埃克赛尔国际会展中心举办。本届展会以“韧性·复苏·重塑：全球旅游新时代”为主题，聚焦全球旅游市场复苏、AI与数字技术创新、可持续旅游发展等前沿议题。" data-title="2026伦敦世界旅游交易会：中国展区规模创历届新高" data-date="10-25 12:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 12:16</span>
          <span class="news-item-title">2026伦敦世界旅游交易会：中国展区规模创历届新高</span>
          <span class="news-value-point">💡 中新网伦敦10月25日电 (记者 欧阳开宇)2026年伦敦世界旅游交易会(WTM)将于11月3日至5日在英国伦敦皇家维多利亚码头埃克赛尔国际会展…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/politics/obama-trump-midterms-campaign.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="第44任总统严厉批评了当天晚些时候反击的特朗普。奥巴马还抨击了共和党俄亥俄州州长候选人维韦克·拉马斯瓦米(Vivek Ramaswamy)。" data-title="Obama Issues Searing Attacks on Trump, Ramaswamy in Return to Campaign Trail" data-date="10-25 10:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 10:39</span>
          <span class="news-item-title">奥巴马对特朗普发出灼热的攻击，拉马斯瓦米返回竞选活动</span>
          <span class="news-item-title-en">Obama Issues Searing Attacks on Trump, Ramaswamy in Return to Campaign Trail</span>
          <span class="news-value-point">💡 第44任总统严厉批评了当天晚些时候反击的特朗普</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/world/europe/ukraine-starshield-drone-speed.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这些评论是他自该国卫星服务中断以来的第一次评论。早些时候，乌克兰表示，使用五角大楼资助的Starshield服务的无人机已恢复正常速度。" data-title="Elon Musk Says Ukraine Violated Starlink’s Rules" data-date="10-25 08:10" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 08:10</span>
          <span class="news-item-title">埃隆·马斯克（ Elon Musk ）称乌克兰违反了Starlink的规则</span>
          <span class="news-item-title-en">Elon Musk Says Ukraine Violated Starlink’s Rules</span>
          <span class="news-value-point">💡 这些评论是他自该国卫星服务中断以来的第一次评论</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/politics/alaska-senate-election-trump-justice-department.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着阿拉斯加和加利福尼亚的行动，该部门加强了对中期选举的干预，作为总统无中介行政权力的工具。" data-title="Alaska Election Gambit Shows Justice Dept. Has Bowed to Trump’s Demands" data-date="10-25 03:21" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 03:21</span>
          <span class="news-item-title">阿拉斯加选举策略显示司法部已屈服于特朗普的要求</span>
          <span class="news-item-title-en">Alaska Election Gambit Shows Justice Dept. Has Bowed to Trump’s Demands</span>
          <span class="news-value-point">💡 随着阿拉斯加和加利福尼亚的行动，该部门加强了对中期选举的干预，作为总统无中介行政权力的工具</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/politics/democrats-expectations-blue-wave.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党人对中期选举越来越乐观。但他们正在被共和党人超支。他们正试图在偏袒特朗普总统的国家进行竞争。" data-title="Why Democrats Could Find It Hard to Win the Senate Despite Their Strong Polls" data-date="10-25 01:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 01:00</span>
          <span class="news-item-title">尽管民调强劲，为什么民主党人很难赢得参议院</span>
          <span class="news-item-title-en">Why Democrats Could Find It Hard to Win the Senate Despite Their Strong Polls</span>
          <span class="news-value-point">💡 民主党人对中期选举越来越乐观</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月25日电(记者 李京统)10月24日是2027年国考报名最后一天，报名热度持续攀升，热门岗位竞争超6000：1。" data-title="2027国考报名截止，多职位数千人竞争一岗" data-date="10-25 00:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 00:01</span>
          <span class="news-item-title">2027国考报名截止，多职位数千人竞争一岗</span>
          <span class="news-value-point">💡 中新网北京10月25日电(记者 李京统)10月24日是2027年国考报名最后一天，报名热度持续攀升，热门岗位竞争超6000：1</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720516.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河北雄安10月24日电 (记者 周昕 曾玥)2026全球治理论坛(雄安)23日至25日在河北雄安新区举行。24日，联合国政策事务副秘书长莱德在大会发言并接受媒体采访。他表示，世界面临着巨大变革，中国提出的全球治理倡议能够帮助联合国落实相关目标。" data-title="联合国政策事务副秘书长：全球治理倡议帮助落实联合国目标" data-date="10-24 21:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 21:49</span>
          <span class="news-item-title">联合国政策事务副秘书长：全球治理倡议帮助落实联合国目标</span>
          <span class="news-value-point">💡 中新社河北雄安10月24日电 (记者 周昕 曾玥)2026全球治理论坛(雄安)23日至25日在河北雄安新区举行</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/600.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 25 日消息，据 SteamDB 数据，《赛博朋克 2077》游戏 2.5 版本更新后，Steam 平台 24 小时内同时在线玩家峰值达 162291 人，创下近 3 年来的最高纪录。值得注意的是，本作上一次取得如此高的关注度，还是《往日之影》资料片推出以后。2023 年 10 月，《赛博朋克 2077》的同时在线玩家峰值曾突破 27.4 万人。IT之家注意到，本次更新带来了双持武器、新服装等特性，并新增一项任务，其内容可作为《边缘行者 2》动画的前传。此外，CDPR 现在还为本作带来了 3 折优惠，Steam 国区现价 89.4 元（https://store.steampowered.com/app/1091500/%E8%B5%9B%E5%8D%9A%E6%9C%8" data-title="《赛博朋克 2077》游戏 2.5 更新后 Steam 峰值突破 16.2 万，创三年来新高" data-date="10-25 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 14:43</span>
          <span class="news-item-title">《赛博朋克 2077》游戏 2.5 更新后 Steam 峰值突破 16.2 万，创三年来新高</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，据 SteamDB 数据，《赛博朋克 2077》游戏 2.5 版本更新后，Steam 平台 24 小时内同时在…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018205/blue-planet-iii-authentic-organic-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="英国广播公司的蓝色星球III希望通过拍摄不那么完美的照片来证明其真实性。以前的自然系列的化身是由他们华丽，水晶般清晰的镜头定义的，这些镜头看起来几乎太好了，不可能是真实的。但" data-title="Blue Planet III is keeping the rough edges in the age of AI" data-date="10-25 05:29" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 05:29</span>
          <span class="news-item-title">蓝色星球III在人工智能时代保持着粗糙的边缘</span>
          <span class="news-item-title-en">Blue Planet III is keeping the rough edges in the age of AI</span>
          <span class="news-value-point">💡 英国广播公司的蓝色星球III希望通过拍摄不那么完美的照片来证明其真实性</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目。" data-title="The AI graveyard: a running list of projects and startups that didn’t make it" data-date="10-25 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-25 03:00</span>
          <span class="news-item-title">人工智能墓地：未成功完成的项目和初创公司的运行列表</span>
          <span class="news-item-title-en">The AI graveyard: a running list of projects and startups that didn’t make it</span>
          <span class="news-value-point">💡 从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018187/pennsylvania-ai-deceptive-advertising-act" target="_blank" rel="noopener" data-cat="keji" data-summary="周四，宾夕法尼亚州州长乔希·夏皮罗（ Josh Shapiro ）签署了《人工智能欺骗性广告法》（ Artificial Intelligence Deceptive Advertising Act ） ，要求披露人工智能生成的广告。法律要求任何广告-无论是静止图像，视频，音频还是文本- “" data-title="Pennsylvania will require labels on AI" data-date="10-25 02:32" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 02:32</span>
          <span class="news-item-title">宾夕法尼亚州将要求在人工智能上贴标签</span>
          <span class="news-item-title-en">Pennsylvania will require labels on AI</span>
          <span class="news-value-point">💡 周四，宾夕法尼亚州州长乔希·夏皮罗（ Josh Shapiro ）签署了《人工智能欺骗性广告法》（ Artificial Intelligenc…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/forced-to-pick-groks-ai-model-chooses-republicans-openais-picks-democrats/" target="_blank" rel="noopener" data-cat="keji" data-summary="一项新的研究发现， Grok的人工智能压倒性地推荐了共和党候选人，而OpenAI的GPT则倾向于民主党人，在近500场选举中，有90%以上的人工智能模式存在分歧。" data-title="Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats." data-date="10-24 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 23:00</span>
          <span class="news-item-title">被迫选择，格罗克的人工智能模型选择了共和党人。OpenAI挑选民主党人。</span>
          <span class="news-item-title-en">Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats.</span>
          <span class="news-value-point">💡 一项新的研究发现， Grok的人工智能压倒性地推荐了共和党候选人，而OpenAI的GPT则倾向于民主党人，在近500场选举中，有90%以上的人工…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/519.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，小米 REDMI Book 2027 系列笔记本已经官宣将于 10 月 27 日发布。这款笔记本搭载第三代英特尔酷睿平台，内置 72Wh 电池，提供多彩配色，质感全面升级，主打移动办公。小米产品行销总监、数码博主马志宇表示，REDMI Book 16 2027 在外观焕新的同时，还将加入用户长期反复提及的诉求 —— 数字小键盘。当然，对于 16 英寸笔记本而言，数字小键盘并非技术难题，也不能严格称为优点或缺点，更多是产品定义上的取舍。结合此前爆料，REDMI Book 16 2027 将搭载酷睿 5 320 处理器，并配备可自主更换的 DDR5 内存，不再延续前代内存板载的设计。其他已确认或接近确认的信息包括：14 英寸版本采用 2.8K 分辨率屏幕，保留双" data-title="小米 REDMI Book 2027 预热：外观焕新，16 英寸机型标配数字小键盘" data-date="10-24 22:53" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 22:53</span>
          <span class="news-item-title">小米 REDMI Book 2027 预热：外观焕新，16 英寸机型标配数字小键盘</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，小米 REDMI Book 2027 系列笔记本已经官宣将于 10 月 27 日发布</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/518.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，据中国信通院，随着大模型技术的迅速迭代，词元（Token）服务成为从技术走向应用的关键点，我国日均词元调用量持续攀升，2026 年 6 月，国内词元日均消耗量约 500 万亿，是 2025 年 12 月的近 4 倍。产业中越来越多的 MaaS（Model as a Service，模型即服务）平台厂商通过公有云 API 方式供给大模型词元服务。然而用户对词元服务性能缺乏直观的判断依据，且面临选型困难等各类问题。为有效衡量服务性能，中国信息通信研究院（简称“中国信通院”）人工智能研究所、人工智能大模型及软硬件评测工业和信息化部重点实验室和中国人工智能产业发展联盟，自 2025 年以来持续开展公有云大模型词元服务性能监测工作，为产业应用提供重要参考，现联合发布《" data-title="中国信通院：6 月国内词元日均消耗量约 500 万亿，是 2025 年 12 月的近 4 倍" data-date="10-24 22:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 22:41</span>
          <span class="news-item-title">中国信通院：6 月国内词元日均消耗量约 500 万亿，是 2025 年 12 月的近 4 倍</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，据中国信通院，随着大模型技术的迅速迭代，词元（Token）服务成为从技术走向应用的关键点，我国日均词元调用量持…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/all-the-ai-agents-that-can-live-in-your-text-messages/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表。" data-title="Here are the top AI agents that can live in your text messages" data-date="10-24 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 22:00</span>
          <span class="news-item-title">以下是可以存在于您的短信中的顶级AI代理</span>
          <span class="news-item-title-en">Here are the top AI agents that can live in your text messages</span>
          <span class="news-value-point">💡 我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1018131/apple-macbook-touchscreen-stylus-pencil-lenovo-laptop-analysis" target="_blank" rel="noopener" data-cat="keji" data-summary="看起来传闻已久的触摸屏MacBook实际上可能会在下周发布，在使用联想Yoga 9n测试Nvidia的RTX Spark平台之后，我开始思考：这是我想从触摸屏MacBook中获得的很多东西。" data-title="I hope Apple’s touchscreen MacBook takes some lessons from this Lenovo laptop" data-date="10-24 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 22:00</span>
          <span class="news-item-title">我希望苹果的触摸屏MacBook能从这款联想笔记本电脑中吸取一些教训</span>
          <span class="news-item-title-en">I hope Apple’s touchscreen MacBook takes some lessons from this Lenovo laptop</span>
          <span class="news-value-point">💡 看起来传闻已久的触摸屏MacBook实际上可能会在下周发布，在使用联想Yoga 9n测试Nvidia的RTX Spark平台之后，我开始思考：这…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/save-up-to-usd800-on-acers-ultra-slim-rtx-5070-ti-gaming-laptop-pay-usd2225-for-the-16gb-ram-model-or-upgrade-to-32gb-for-usd2400" target="_blank" rel="noopener" data-cat="keji" data-summary="宏碁Predator Helios Neo 16S AI将240 Hz QHD + OLED显示屏与英特尔的24核酷睿Ultra 9处理器和Nvidia RTX 5070 Ti显卡相结合，百思买提供高达800 $的折扣。" data-title="Save up to $800 on Acer’s ultra-slim RTX 5070 Ti gaming laptop — pay $2225 for the 16GB RAM model or upgrade to 32GB for $2400" data-date="10-24 21:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-24 21:58</span>
          <span class="news-item-title">宏碁超薄RTX 5070 Ti游戏笔记本电脑最高可节省800美元—支付2225美元购买16GB RAM型号或升级到32GB仅需2400美元</span>
          <span class="news-item-title-en">Save up to $800 on Acer’s ultra-slim RTX 5070 Ti gaming laptop — pay $2225 for the 16GB RAM model or upgrade to 32GB for $2400</span>
          <span class="news-value-point">💡 宏碁Predator Helios Neo 16S AI将240 Hz QHD + OLED显示屏与英特尔的24核酷睿Ultra 9处理器和Nv…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720517.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社曼谷10月24日电(梁峻祥 李映民)泰国总理阿努廷24日发表讲话说，面对地缘政治冲突、气候变化以及科技和人工智能发展带来的新挑战，泰国坚持维护各国主权和国家平等，主张以和平方式解决争端、尊重国际法，并将积极、建设性地参与国际合作，推动和平与可持续发展。" data-title="泰国总理：泰国将积极参与国际合作推动和平与可持续发展" data-date="10-24 21:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 21:51</span>
          <span class="news-item-title">泰国总理：泰国将积极参与国际合作推动和平与可持续发展</span>
          <span class="news-value-point">💡 中新社曼谷10月24日电(梁峻祥 李映民)泰国总理阿努廷24日发表讲话说，面对地缘政治冲突、气候变化以及科技和人工智能发展带来的新挑战，泰国坚持…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/leaked-video-exposes-how-chinese-factories-are-stripping-rtx-5090s-to-fuel-ai-custom-partner-cards-to-nvidia-founders-editions-on-the-chopping-block" target="_blank" rel="noopener" data-cat="keji" data-summary="想知道为什么很难找到腾讯通5090 ？泄露的镜头显示，包括Founders Editions在内的数千个消费者GPU被撕成碎片，用于AI服务器。" data-title="Leaked video exposes how industrial-scale Chinese factories are dismantling RTX 5090s by the thousands to fuel AI servers" data-date="10-24 19:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-24 19:15</span>
          <span class="news-item-title">泄露的视频揭示了中国工业规模的工厂如何拆除成千上万的RTX 5090来为人工智能服务器提供燃料</span>
          <span class="news-item-title-en">Leaked video exposes how industrial-scale Chinese factories are dismantling RTX 5090s by the thousands to fuel AI servers</span>
          <span class="news-value-point">💡 想知道为什么很难找到腾讯通5090</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck78p37y5508o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫击败后的评论表明，目前管理俱乐部是多么困难。" data-title="What Man Utd need now is stability, not more changes" data-date="10-25 14:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:34</span>
          <span class="news-item-title">曼联现在需要的是稳定性，而不是更多的变化</span>
          <span class="news-item-title-en">What Man Utd need now is stability, not more changes</span>
          <span class="news-value-point">💡 英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c94g1p32gyrro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦本赛季在四场杯赛中打进了15球，但在七场英超比赛中只打进了9球。" data-title="Why are Liverpool struggling for Premier League goals?" data-date="10-25 14:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:26</span>
          <span class="news-item-title">为什么利物浦要为英超进球而苦苦挣扎？</span>
          <span class="news-item-title-en">Why are Liverpool struggling for Premier League goals?</span>
          <span class="news-value-point">💡 利物浦本赛季在四场杯赛中打进了15球，但在七场英超比赛中只打进了9球</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmy83vg66zngo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着曼联主教练迈克尔·卡里克（ Michael Carrick ）的压力越来越大，英国广播公司体育台（ BBC Sport ）关注英超联赛的“裁员赛季”何时开始。" data-title="When is Premier League &#39;sacking season&#39; - and who should be worried?" data-date="10-25 14:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:17</span>
          <span class="news-item-title">英超联赛的“裁员季”是什么时候？谁应该担心？</span>
          <span class="news-item-title-en">When is Premier League 'sacking season' - and who should be worried?</span>
          <span class="news-value-point">💡 随着曼联主教练迈克尔·卡里克（ Michael Carrick ）的压力越来越大，英国广播公司体育台（ BBC Sport ）关注英超联赛的“裁…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/alaska-early-voting-sites.html" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一位州议员表示， 18个投票站未能开放提前投票“没有法律依据”。" data-title="In Alaska, Some Early Voting Sites in Rural Villages Have Not Yet Opened" data-date="10-25 06:06" data-source="纽约时报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 06:06</span>
          <span class="news-item-title">在阿拉斯加，农村的一些提前投票点尚未开放</span>
          <span class="news-item-title-en">In Alaska, Some Early Voting Sites in Rural Villages Have Not Yet Opened</span>
          <span class="news-value-point">💡 一位州议员表示， 18个投票站未能开放提前投票“没有法律依据”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9ly0dxxgp7lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，在伯恩茅斯周日访问老特拉福德时，他有可能有效地管理曼联。" data-title="Man Utd not an unmanageable club" data-date="10-25 05:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 05:34</span>
          <span class="news-item-title">曼联不是一个难以管理的俱乐部</span>
          <span class="news-item-title-en">Man Utd not an unmanageable club</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，在伯恩茅斯周日访问老特拉福德时，他有可能有效地管理曼联</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqev38dz34vxo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺在周六的英超联赛中排名第12 ，这是他们自1月2日以来的最高联赛位置。他们终于要回来了？" data-title="The candid meeting that &#39;changed&#39; Spurs - are they finally on way back?" data-date="10-25 05:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 05:14</span>
          <span class="news-item-title">“改变”马刺的坦率会议-他们终于回来了吗？</span>
          <span class="news-item-title-en">The candid meeting that 'changed' Spurs - are they finally on way back?</span>
          <span class="news-value-point">💡 托特纳姆热刺在周六的英超联赛中排名第12 ，这是他们自1月2日以来的最高联赛位置</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/24/chelsea-v-tottenham-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Mathys Tel打进了一个很好的单人进球，为马刺在桥梁上的罕见胜利奠定了基础。球队进入球场。蓝色的切尔西，白色的马刺，不久之后，每件衬衫都会湿透。拥有Harry J All St的标志性作品" data-title="Chelsea 0-2 Tottenham: Premier League – as it happened" data-date="10-25 03:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 03:01</span>
          <span class="news-item-title">切尔西0-2托特纳姆热刺：英超联赛–事实就是这样</span>
          <span class="news-item-title-en">Chelsea 0-2 Tottenham: Premier League – as it happened</span>
          <span class="news-value-point">💡 Mathys Tel打进了一个很好的单人进球，为马刺在桥梁上的罕见胜利奠定了基础</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/24/chelsea-tottenham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺有时会参加这些大型比赛，并想方设法击败自己。然而，这一次，他们把神经放在了一个他们大多只知道厄运的地方。马刺发挥控制力，保持耐心，在斯坦福桥赢得比赛" data-title="Tottenham stun Chelsea for second league win in a week as Cole Palmer is sent off" data-date="10-25 02:32" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 02:32</span>
          <span class="news-item-title">托特纳姆热刺击败切尔西，在一周内第二次赢得联赛冠军，科尔·帕尔默被罚下场</span>
          <span class="news-item-title-en">Tottenham stun Chelsea for second league win in a week as Cole Palmer is sent off</span>
          <span class="news-value-point">💡 托特纳姆热刺有时会参加这些大型比赛，并想方设法击败自己</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqwy7x6e672eo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="守门员迈克·彭德斯（ Mike Penders ）经历了艰难的英超首发，在马刺队2-0战胜切尔西的比赛中打进了自己的进球。以下是我们（以及您）对玩家进行评分的方式。" data-title="Penders error &amp; Palmer sees red - player ratings for Chelsea v Spurs" data-date="10-25 02:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 02:26</span>
          <span class="news-item-title">潘德斯错误和帕尔默看到红色-切尔西对马刺的球员评分</span>
          <span class="news-item-title-en">Penders error & Palmer sees red - player ratings for Chelsea v Spurs</span>
          <span class="news-value-point">💡 守门员迈克·彭德斯（ Mike Penders ）经历了艰难的英超首发，在马刺队2-0战胜切尔西的比赛中打进了自己的进球</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6p9gkdzzpnro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尼古拉斯·杰克逊（ Nicolas Jackson ）凭借对阵曼城的比赛获胜双打，继续在阿斯顿维拉（ Aston Villa ）的职业生涯中" data-title="From Chelsea reject to Watkins &#39;upgrade&#39; - Jackson makes fast Villa start" data-date="10-25 00:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 00:58</span>
          <span class="news-item-title">从切尔西拒绝到沃特金斯“升级” -杰克逊让别墅快速启动</span>
          <span class="news-item-title-en">From Chelsea reject to Watkins 'upgrade' - Jackson makes fast Villa start</span>
          <span class="news-value-point">💡 尼古拉斯·杰克逊（ Nicolas Jackson ）凭借对阵曼城的比赛获胜双打，继续在阿斯顿维拉（ Aston Villa ）的职业生涯中</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/24/tottenham-arsenal-wsl-premier-league-efl-football-clockwatch-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳战胜埃弗顿，缩小了与曼城的差距，富勒姆在考文垂阿森纳的回击中取得了重要胜利！ Alessia Russo挑选了Georgia Stanway ，她进入禁区，这位前拜仁中场引导她射门" data-title="Arsenal 2-0 Everton, Coventry 0-1 Fulham: football clockwatch – as it happened" data-date="10-25 00:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 00:13</span>
          <span class="news-item-title">阿森纳2-0埃弗顿，考文垂0-1富勒姆：足球钟表–恰巧</span>
          <span class="news-item-title-en">Arsenal 2-0 Everton, Coventry 0-1 Fulham: football clockwatch – as it happened</span>
          <span class="news-value-point">💡 阿森纳战胜埃弗顿，缩小了与曼城的差距，富勒姆在考文垂阿森纳的回击中取得了重要胜利</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/24/coventry-fulham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="奥斯卡·鲍勃（ Oscar Bobb ）在富勒姆（ Fulham ）的第一个英超联赛进球赢得了对考文垂的胜利，将阿尔瓦罗·阿贝洛亚（ Álvaro Arbeloa ）的球队提升到了降级区之外。鲍勃（ Bobb ）在第80分钟产生了一些个人得分技巧，扭曲了他进入该地区的方式，" data-title="Fulham climb out of drop zone after Oscar Bobb’s late show sinks Coventry" data-date="10-25 00:11" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 00:11</span>
          <span class="news-item-title">奥斯卡·波布（ Oscar Bobb ）的晚间演出沉没考文垂（ Coventry ）后，富勒姆（ Fulham ）</span>
          <span class="news-item-title-en">Fulham climb out of drop zone after Oscar Bobb’s late show sinks Coventry</span>
          <span class="news-value-point">💡 奥斯卡·鲍勃（ Oscar Bobb ）在富勒姆（ Fulham ）的第一个英超联赛进球赢得了对考文垂的胜利，将阿尔瓦罗·阿贝洛亚（ Álvar…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/24/arsenal-everton-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="David Moyes的等待还在继续。这位63岁的苏格兰人一定希望在他作为埃弗顿的经理第14次访问这个体育场时，他的运气会改变。然而，从埃兹里·康萨（ Ezri Konsa ）作为总理利亚（ Premier Lea ）猛烈抨击阿森纳（ Arsenal ）的第一个进球的那一刻" data-title="Clinical Arsenal earn precious win against Everton thanks to Konsa and Gabriel" data-date="10-25 00:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 00:03</span>
          <span class="news-item-title">得益于Konsa和Gabriel ，临床阿森纳赢得了对埃弗顿的宝贵胜利</span>
          <span class="news-item-title-en">Clinical Arsenal earn precious win against Everton thanks to Konsa and Gabriel</span>
          <span class="news-value-point">💡 David Moyes的等待还在继续</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6kg7z700k7jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城在英超赛季的100%胜利开局突然结束了对阵阿斯顿维拉的比赛，这让恩佐·马雷斯卡面临着明显的防守问题。" data-title="Man City&#39;s leaky defence highlights Donnarumma &amp; Guehi struggles" data-date="10-24 23:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-24 23:05</span>
          <span class="news-item-title">曼城的防守漏洞突显了Donnarumma和Guehi的挣扎</span>
          <span class="news-item-title-en">Man City's leaky defence highlights Donnarumma & Guehi struggles</span>
          <span class="news-value-point">💡 曼城在英超赛季的100%胜利开局突然结束了对阵阿斯顿维拉的比赛，这让恩佐·马雷斯卡面临着明显的防守问题</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/24/aston-villa-v-manchester-city-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尼古拉斯·杰克逊（ Nicolas Jackson ）两次得分并领先一线，因为维拉（ Villa ）在一场激动人心的比赛中结束了曼城（ City ）的胜利开局恩佐·马雷斯卡（ Enzo Maresca ）对菲尔·福登（ Phil Foden ）的遗漏幸运的是，由于我们玩了这么多比赛，我们" data-title="Aston Villa 2-1 Manchester City: Premier League – as it happened" data-date="10-24 21:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-24 21:42</span>
          <span class="news-item-title">阿斯顿维拉2-1曼城：英超联赛–事实就是这样</span>
          <span class="news-item-title-en">Aston Villa 2-1 Manchester City: Premier League – as it happened</span>
          <span class="news-value-point">💡 尼古拉斯·杰克逊（ Nicolas Jackson ）两次得分并领先一线，因为维拉（ Villa ）在一场激动人心的比赛中结束了曼城（ City…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/603.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，曜越现已在京东上架“AX600 Pro”机箱，该机箱采用商务风格外形设计，定价为 899 元。该机箱尺寸为 555x250x650mm，支持 M-ITX、ATX、E-ATX 至 HPTX 等多种主板规格，机箱外部采用多面散热孔设计，底部配备了滚轮。I/O 方面其顶部提供 1 个 USB-C 接口、2 个 USB-A 3.0 接口以及 1 个 3.5mm 音频接口。该机箱支持安装双 ATX 电源，配备可拆卸电源架，电源限长为 180mm。CPU 散热器限高 180mm，VGA 显卡限长为 400mm。提供 10 PCS 的 PCI 插槽。该机箱在标配状态下底板支持四块 3.5&quot; HDD 或四个 2.5&quot; SSD，电源仓支持一块 2.5&quot; SSD，主板后侧支持一" data-title="曜越推出 AX600 Pro 机箱：提供多达 20 个风扇位，899 元" data-date="10-25 15:02" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 15:02</span>
          <span class="news-item-title">曜越推出 AX600 Pro 机箱：提供多达 20 个风扇位，899 元</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，曜越现已在京东上架“AX600 Pro”机箱，该机箱采用商务风格外形设计，定价为 899 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/601.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，技嘉现已在京东上架“FO32U24G”显示器，该机主打 4K 240Hz / FHD 480Hz 双模，定价为 5789 元。京东技嘉“FO32U24G”显示器 5789 元直达链接该机基于 32&quot; 第四代 Tandem WOLED 面板，采用镜面屏技术，支持 UHD 240Hz / FHD 480Hz 双模切换。其通过 VESA DisplayHDR True Black 500 认证，HDR 峰值亮度可达 1500nits，色域 99.5% DCI-P3，色差 ΔE＜2，GtG 响应速度 0.03ms；同时搭载 AI OLED Care Pro 智能面板保护系统。该机支架支持升降 / 倾斜 / 旋转，显示器本体支持 VESA 壁挂，提供 2 个 HDMI" data-title="技嘉上架“FO32U24G”31.5 英寸显示器：4K 240Hz / FHD 480Hz，5789 元" data-date="10-25 14:49" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 14:49</span>
          <span class="news-item-title">技嘉上架“FO32U24G”31.5 英寸显示器：4K 240Hz / FHD 480Hz，5789 元</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，技嘉现已在京东上架“FO32U24G”显示器，该机主打 4K 240Hz / FHD 480Hz 双模，定价为…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720678.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海10月25日电 题：在前滩，产城融合构筑栖息沃土" data-title="在前滩，产城融合构筑栖息沃土" data-date="10-25 14:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:45</span>
          <span class="news-item-title">在前滩，产城融合构筑栖息沃土</span>
          <span class="news-value-point">💡 中新网上海10月25日电 题：在前滩，产城融合构筑栖息沃土</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/599.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，八位堂 (8BitDo) 现已在国内电商平台上架《战争机器：事变日》主题版本的 Retro 87 机械键盘与 Retro R8 鼠标，键盘单品价格 599 元、鼠标单品价格 299 元。京东八位堂 Retro 87 机械键盘《战争机器：事变日》联名版 599 元直达链接京东八位堂 Retro R8 鼠标《战争机器：事变日》联名版 299 元直达链接这两款产品均得到 XBOX 官方授权，号称将《战争机器：事变日》的战场印记融入鼠标和键盘。其整体采用红黑配色，带有游戏 Logo。京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3 次：点此抽红包。淘宝 11.11 无门槛红包 面额至高 26888 元，每天抽 1 次：点此抽红包。" data-title="八位堂《战争机器：事变日》主题 Retro 87 机械键盘及 Retro R8 鼠标上市，599 元 / 299 元" data-date="10-25 14:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 14:41</span>
          <span class="news-item-title">八位堂《战争机器：事变日》主题 Retro 87 机械键盘及 Retro R8 鼠标上市，599 元 / 299 元</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，八位堂 (8BitDo) 现已在国内电商平台上架《战争机器：事变日》主题版本的 Retro 87 机械键盘与 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/597.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，在最新的特斯拉财报电话会议上，特斯拉副总裁阿肖克 · 埃卢斯瓦米（Ashok Elluswamy）宣布，特斯拉正在自研一套基于 AI 的地图导航系统。这套全新地图方案将随 FSD v15 上线，融合车队采集数据、个性化路线规划，同时支持 FSD 语音控制。据IT之家了解，特斯拉目前的导航是第三方地图内容搭配自研软件。此前“偏好路线”功能上线时就有报道说明：谷歌通过 API 提供底图瓦片、街道数据、卫星影像、兴趣点以及路况信息；特斯拉自己开发导航应用、计算路线，因此可以把超充站点、用户偏好纳入路线决策。财报会上，一位股东提问，提到 FSD 在限速识别、泊车、路线选择上存在问题。埃卢斯瓦米对此表示认同：“你说得完全没错，我们本就不该依赖外部厂商的地图。”他随后确" data-title="特斯拉确认正自研 AI 地图，将随 FSD v15 逐步推送" data-date="10-25 14:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 14:34</span>
          <span class="news-item-title">特斯拉确认正自研 AI 地图，将随 FSD v15 逐步推送</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，在最新的特斯拉财报电话会议上，特斯拉副总裁阿肖克 · 埃卢斯瓦米（Ashok Elluswamy）宣布，特斯拉…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/596.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，盛色现已在京东上架型号为“OF24QC”的 23.8 英寸显示器，该机主打 2K 100Hz，定价为 595 元，部分地区国补后低至 513 元。京东 SANC“OF24QC”显示器券后 595 元领 90 元券该机配备一块 2560x1440 分辨率 100Hz IPS 面板，峰值亮度 280 尼特，静态对比度 1300:1，显示器支持 8-Bit 色彩，覆盖 120% sRGB 色域容积。该机采用固定支架，显示器本体支持 VESA 100x100mm 壁挂，提供 1 个 HDMI 2.0、1 个 DP 1.4 接口。IT之家附显示器参数：京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3 次：点此抽红包。淘宝 11.11 无门槛红包 面额" data-title="盛色推出“OF24QC”23.8 英寸显示器：2K 100Hz，595 元" data-date="10-25 14:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 14:33</span>
          <span class="news-item-title">盛色推出“OF24QC”23.8 英寸显示器：2K 100Hz，595 元</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，盛色现已在京东上架型号为“OF24QC”的 23.8 英寸显示器，该机主打 2K 100Hz，定价为 595 …</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cm5ynx99yxzwo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="观鸟近年愈来愈受长者和认知障碍症患者欢迎。研究人员分析这项活动对他们的身心健康有何影响，以及可能带来哪些益处。" data-title="观鸟如何重塑大脑，延缓认知衰退？" data-date="10-25 14:30" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:30</span>
          <span class="news-item-title">观鸟如何重塑大脑，延缓认知衰退？</span>
          <span class="news-value-point">💡 观鸟近年愈来愈受长者和认知障碍症患者欢迎</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720670.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社沈阳10月25日电 (韩宏 王翕瞳)“铭记伟大胜利 传承红色基因”纪念中国人民志愿军抗美援朝出国作战76周年活动，25日在沈阳举行，志愿军老战士等社会各界约400人参加。" data-title="纪念中国人民志愿军抗美援朝出国作战76周年活动在沈阳举行" data-date="10-25 14:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:26</span>
          <span class="news-item-title">纪念中国人民志愿军抗美援朝出国作战76周年活动在沈阳举行</span>
          <span class="news-value-point">💡 中新社沈阳10月25日电 (韩宏 王翕瞳)“铭记伟大胜利 传承红色基因”纪念中国人民志愿军抗美援朝出国作战76周年活动，25日在沈阳举行，志愿军…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720666.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原10月25日电 (记者 杨杰英 李庭耀)10月25日，2026年“晋台·汾酒杯”海峡两岸青年精英网球团体公开赛开幕式在山西体育中心举行。全国台联副会长杨毅周、山西省委台办主任王成禹、山西省海联会常务副会长郭延斌、山西省台联党组书记隋欣哲、山西省体育局二级巡视员武锐强等出席。两岸青年以球会友，共同开启本届赛事。" data-title="海峡两岸青年精英网球团体公开赛在太原开幕 两岸青年以球会友" data-date="10-25 14:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:20</span>
          <span class="news-item-title">海峡两岸青年精英网球团体公开赛在太原开幕 两岸青年以球会友</span>
          <span class="news-value-point">💡 中新网太原10月25日电 (记者 杨杰英 李庭耀)10月25日，2026年“晋台·汾酒杯”海峡两岸青年精英网球团体公开赛开幕式在山西体育中心举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720654.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社河北张家口10月25日电 (记者 陈林)深秋的河北阳原桑干河国家湿地公园，芦苇摇曳，水面如镜。在此聚集栖息的成群候鸟，或振翅翱翔，或在水中嬉戏。当地摄影爱好者张亚峰用手中相机，一次次将眼前画面定格。" data-title="桑干河入冀第一县：青头潜鸭“现身” 两千灰鹤飞舞" data-date="10-25 14:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:16</span>
          <span class="news-item-title">桑干河入冀第一县：青头潜鸭“现身” 两千灰鹤飞舞</span>
          <span class="news-value-point">💡 中新社河北张家口10月25日电 (记者 陈林)深秋的河北阳原桑干河国家湿地公园，芦苇摇曳，水面如镜</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720641.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网信阳10月25日电(王佳宁)今年是中国工农红军长征胜利90周年。24日晚，“红星照耀中国·90年后我站在何家冲”网络主题宣传活动在河南信阳启动。" data-title="“红星照耀中国·90年后我站在何家冲”网络主题宣传活动在河南信阳启动" data-date="10-25 14:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:12</span>
          <span class="news-item-title">“红星照耀中国·90年后我站在何家冲”网络主题宣传活动在河南信阳启动</span>
          <span class="news-value-point">💡 中新网信阳10月25日电(王佳宁)今年是中国工农红军长征胜利90周年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720656.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月25日电 (记者 吕少威)记者25日从北京市交通委获悉，随着红叶渐入最佳观赏期，为应对赏秋客流高峰、方便市民游客便捷赏秋、错峰出行，北京交通部门统筹地铁、有轨电车、地面公交等多元运力，优化推出多条香山赏叶专线及京郊赏秋通游专线，搭建多层次公共交通出行体系，全方位护航市民错峰赏秋、安全畅行。交通部门倡导市民错峰游园、预约出行，有序返程。" data-title="北京交通部门推出多条“赏叶专线”和通游专线" data-date="10-25 14:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 14:02</span>
          <span class="news-item-title">北京交通部门推出多条“赏叶专线”和通游专线</span>
          <span class="news-value-point">💡 中新网北京10月25日电 (记者 吕少威)记者25日从北京市交通委获悉，随着红叶渐入最佳观赏期，为应对赏秋客流高峰、方便市民游客便捷赏秋、错峰出…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720639.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网怀化10月25日电 (付敬懿 徐志雄)10月25日，“张雪机车”创始人张雪驾驶MX450两栖改装摩托车，在湖南麻阳苗族自治县锦江水域完成总里程40.74公里的水上行驶，刷新“改装摩托车在开阔水域行驶最远距离”吉尼斯世界纪录。" data-title="40.74公里！张雪刷新“改装摩托车在开阔水域行驶最远距离”吉尼斯世界纪录" data-date="10-25 13:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 13:41</span>
          <span class="news-item-title">40.74公里！张雪刷新“改装摩托车在开阔水域行驶最远距离”吉尼斯世界纪录</span>
          <span class="news-value-point">💡 中新网怀化10月25日电 (付敬懿 徐志雄)10月25日，“张雪机车”创始人张雪驾驶MX450两栖改装摩托车，在湖南麻阳苗族自治县锦江水域完成总…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/world/middleeast/iranians-face-anxious-wait-as-threat-of-attack-looms.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国和以色列已经制定了重新对伊朗发动罢工的计划，在厌倦战争的居民中制造了一种恐惧感。" data-title="Iranians Face Anxious Wait as Threat of Attack Looms" data-date="10-25 13:14" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 13:14</span>
          <span class="news-item-title">随着袭击的威胁迫在眉睫，伊朗人面临焦虑的等待</span>
          <span class="news-item-title-en">Iranians Face Anxious Wait as Threat of Attack Looms</span>
          <span class="news-value-point">💡 美国和以色列已经制定了重新对伊朗发动罢工的计划，在厌倦战争的居民中制造了一种恐惧感</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720621.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月25日电 (钱晨菲)25日，浙江省防指决定于11时将防台风应急响应调整为Ⅳ级。" data-title="“蔷琵”强度减弱 浙江调整防台风应急响应为Ⅳ级" data-date="10-25 13:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 13:06</span>
          <span class="news-item-title">“蔷琵”强度减弱 浙江调整防台风应急响应为Ⅳ级</span>
          <span class="news-value-point">💡 中新网杭州10月25日电 (钱晨菲)25日，浙江省防指决定于11时将防台风应急响应调整为Ⅳ级</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-25 15:02（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
