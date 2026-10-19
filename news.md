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
      <span>2026-10-19 17:16 抓取更新</span>
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
        <span class="channel-count">58</span>
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
        <span class="channel-count">13</span>
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
  <div class="ov-item"><span class="ov-num">58</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×24 · IT之家×15</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-19/10717279.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社青岛10月19日电 题：做军舰“心脏”的守护者：一名蒙古族水兵的“长征”" data-title="（长征胜利90周年）做军舰“心脏”的守护者：一名蒙古族水兵的“长征”" data-date="10-19 17:11" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-19 17:11</span>
      </div>
      <h2 class="hero-featured-title">（长征胜利90周年）做军舰“心脏”的守护者：一名蒙古族水兵的“长征”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-19/10717266.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网10月19日电 国务院新闻办公室19日举行新闻发布会，商务部部长助理袁晓明表示，随着人民生活水平提升，消费者更加注重产品的品质和消费体验。根据商务部商务大数据显示，今年1-9月，重点平台智能眼镜销售额增长1.1倍。人工智能、物联网、区块链等新技术，在消费领域广泛应用，科技创新日益成为推动消费扩容升级的重要举措。" data-title="商务部：1" data-date="10-19 16:46" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">商务部：1</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/19/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="弗洛里安·维尔茨（ Florian Wirtz ）在利物浦的进攻中承担了更多的责任，而皮埃尔·塞奇（ Pierre Sage ）在水晶宫（ Crystal Palace ）承受着压力多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）的身体状况在曼联（ Manchester United ）地区的一个角落里击败了布莱恩·姆博莫" data-title="Premier League: 10 talking points from the weekend’s action" data-date="10-19 15:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Premier League: 10 talking points from the weekend’s action</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/014/938.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，FlymeAIOS 今日透露，9 月，Flyme Auto 新增装机 154,206 辆，前三季度装机量超 1,326,000 辆，全球累计搭载超 3,594,000 辆。据IT之家此前报道，魅族 Flyme Auto 车载软件系统发布于 2023 年 3 月，支持无缝接力、手机辅助 OTA、手机-汽车硬件互通共享硬件能力，支持手机寻车，支持平行视窗、小窗展示、跨端可见即可说等软件功能。Flyme Auto 2 发布于去年 8 月，带来了实况桌面 3D 质感、全场景一镜到底、Alive 壁纸、自定义桌面插件等功能，Aicy 大卡片、全新小窗模式提供了更轻量更高效的交互方式。AI 能力贯通整车全域，AI 读心术主动判断用户意图，自动完成常用操作，并且此次更新还" data-title="Flyme Auto 车机 9 月新增装机 15.4 万辆，累计搭载超 359 万辆" data-date="10-19 17:15" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">Flyme Auto 车机 9 月新增装机 15.4 万辆，累计搭载超 359 万辆</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717279.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社青岛10月19日电 题：做军舰“心脏”的守护者：一名蒙古族水兵的“长征”" data-title="（长征胜利90周年）做军舰“心脏”的守护者：一名蒙古族水兵的“长征”" data-date="10-19 17:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 17:11</span>
          <span class="news-item-title">（长征胜利90周年）做军舰“心脏”的守护者：一名蒙古族水兵的“长征”</span>
          <span class="news-value-point">💡 中新社青岛10月19日电 题：做军舰“心脏”的守护者：一名蒙古族水兵的“长征”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717278.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 据中央纪委国家监委网站消息，经中共中央批准，中央纪委国家监委对中国人民保险集团股份有限公司原党委委员、副总裁俞小平严重违纪违法问题进行了立案审查调查。" data-title="中国人保原党委委员、副总裁俞小平被开除党籍" data-date="10-19 17:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 17:03</span>
          <span class="news-item-title">中国人保原党委委员、副总裁俞小平被开除党籍</span>
          <span class="news-value-point">💡 中新网10月19日电 据中央纪委国家监委网站消息，经中共中央批准，中央纪委国家监委对中国人民保险集团股份有限公司原党委委员、副总裁俞小平严重违纪…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717277.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 据中央纪委国家监委网站消息，经中共中央批准，中央纪委国家监委对全国社会保障基金理事会原党组成员、副理事长王文灵严重违纪违法问题进行了立案审查调查。" data-title="社保基金会原党组成员、副理事长王文灵被“双开”" data-date="10-19 17:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 17:02</span>
          <span class="news-item-title">社保基金会原党组成员、副理事长王文灵被“双开”</span>
          <span class="news-value-point">💡 中新网10月19日电 据中央纪委国家监委网站消息，经中共中央批准，中央纪委国家监委对全国社会保障基金理事会原党组成员、副理事长王文灵严重违纪违法…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717276.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 据中央纪委国家监委网站消息，经中共中央批准，中央纪委国家监委对自然资源部原党组成员，国家林业和草原局原党组书记、局长张建龙严重违纪违法问题进行了立案审查调查。" data-title="自然资源部原党组成员，国家林草局原党组书记、局长张建龙被开除党籍" data-date="10-19 17:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 17:01</span>
          <span class="news-item-title">自然资源部原党组成员，国家林草局原党组书记、局长张建龙被开除党籍</span>
          <span class="news-value-point">💡 中新网10月19日电 据中央纪委国家监委网站消息，经中共中央批准，中央纪委国家监委对自然资源部原党组成员，国家林业和草原局原党组书记、局长张建龙…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717267.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：国新办就2026年前三季度工业和信息化发展情况举行新闻发布会" data-title="直播海报：国新办就2026年前三季度工业和信息化发展情况举行新闻发布会" data-date="10-19 16:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:42</span>
          <span class="news-item-title">直播海报：国新办就2026年前三季度工业和信息化发展情况举行新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717262.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社沈阳10月19日电 (记者 李𬀪)鲁迅美术学院19日发布讣告，著名油画家、美术教育家，国务院政府特殊津贴获得者，中国美术家协会原常务理事，鲁迅美术学院原党委书记、原院长、名誉院长、荣誉终身教授宋惠民因病医治无效，于18日在沈阳逝世，享年89岁。" data-title="中国著名油画家、鲁迅美术学院原院长宋惠民逝世" data-date="10-19 16:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:36</span>
          <span class="news-item-title">中国著名油画家、鲁迅美术学院原院长宋惠民逝世</span>
          <span class="news-value-point">💡 中新社沈阳10月19日电 (记者 李𬀪)鲁迅美术学院19日发布讣告，著名油画家、美术教育家，国务院政府特殊津贴获得者，中国美术家协会原常务理事，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717229.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社湖南株洲10月19日电 (付敬懿)2026(丙午)年海峡两岸炎帝神农文化交流大会19日在湖南炎陵县举行，两岸各界代表300余人齐聚中华民族始祖圣地炎帝陵，共拜始祖、共叙文脉、共话亲情。" data-title="2026（丙午）年海峡两岸同胞湖南共拜炎帝陵" data-date="10-19 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:22</span>
          <span class="news-item-title">2026（丙午）年海峡两岸同胞湖南共拜炎帝陵</span>
          <span class="news-value-point">💡 中新社湖南株洲10月19日电 (付敬懿)2026(丙午)年海峡两岸炎帝神农文化交流大会19日在湖南炎陵县举行，两岸各界代表300余人齐聚中华民族…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717224.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 据商务部网站19日消息，商务部、海关总署公布优化调整挖泥船相关物项出口管制措施的决定。" data-title="两部门公布优化调整挖泥船相关物项出口管制措施的决定" data-date="10-19 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:20</span>
          <span class="news-item-title">两部门公布优化调整挖泥船相关物项出口管制措施的决定</span>
          <span class="news-value-point">💡 中新网10月19日电 据商务部网站19日消息，商务部、海关总署公布优化调整挖泥船相关物项出口管制措施的决定</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717206.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 据商务部网站19日消息，商务部、海关总署公布对盾构机等物项实施出口管制的决定。" data-title="两部门公布对盾构机等物项实施出口管制的决定" data-date="10-19 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:20</span>
          <span class="news-item-title">两部门公布对盾构机等物项实施出口管制的决定</span>
          <span class="news-value-point">💡 中新网10月19日电 据商务部网站19日消息，商务部、海关总署公布对盾构机等物项实施出口管制的决定</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717216.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社杜尚别10月19日电 (记者 单璐)10月19日上午，中国国务院总理李强在杜尚别会见塔吉克斯坦总统拉赫蒙。" data-title="李强会见塔吉克斯坦总统拉赫蒙" data-date="10-19 16:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:09</span>
          <span class="news-item-title">李强会见塔吉克斯坦总统拉赫蒙</span>
          <span class="news-value-point">💡 中新社杜尚别10月19日电 (记者 单璐)10月19日上午，中国国务院总理李强在杜尚别会见塔吉克斯坦总统拉赫蒙</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717228.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="前不久，上小学一年级的孩子放学回家，郑重其事地告诉我：“爸爸，今天我们要‘飞夺泸定桥’了。”原来，老师把课本的各个单元变成了长征路上的节点，印刻在书本首页，每次按照要求完成预习复习，就可以获得一枚“奖章”。" data-title="长征精神何以穿越时空、历久弥新（人民论坛）" data-date="10-19 16:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:04</span>
          <span class="news-item-title">长征精神何以穿越时空、历久弥新（人民论坛）</span>
          <span class="news-value-point">💡 前不久，上小学一年级的孩子放学回家，郑重其事地告诉我：“爸爸，今天我们要‘飞夺泸定桥’了</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-19/10717184.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社东京10月19日电 据日本广播协会报道，日本首相高市早苗19日向靖国神社供奉“玉串料”(祭祀费)。" data-title="日本首相高市早苗向靖国神社供奉祭祀费" data-date="10-19 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 15:30</span>
          <span class="news-item-title">日本首相高市早苗向靖国神社供奉祭祀费</span>
          <span class="news-value-point">💡 中新社东京10月19日电 据日本广播协会报道，日本首相高市早苗19日向靖国神社供奉“玉串料”(祭祀费)</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-19/10717187.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 综合日媒报道，当地时间19日，日本首相高市早苗向供奉有二战甲级战犯的靖国神社供奉“玉串料”(祭祀费)。17日，高市早苗还曾向靖国神社供奉名为“真榊”的祭品。日本首相在靖国神社秋季大祭期间，先后供奉祭品和祭祀费，再度引发外界对日本政界历史认识问题的关注。" data-title="高市早苗三天内两次向靖国神社供奉，国内外批评声持续" data-date="10-19 15:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 15:16</span>
          <span class="news-item-title">高市早苗三天内两次向靖国神社供奉，国内外批评声持续</span>
          <span class="news-value-point">💡 中新网10月19日电 综合日媒报道，当地时间19日，日本首相高市早苗向供奉有二战甲级战犯的靖国神社供奉“玉串料”(祭祀费)</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-19/10717166.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月19日电 综合外媒报道，美国总统特朗普当地时间18日在社交媒体发文批评乌克兰袭击俄罗斯柴油炼油厂，称乌克兰总统泽连斯基可能从未想过结束俄乌战事。" data-title="特朗普批评泽连斯基：他可能从未想过结束俄乌战事" data-date="10-19 14:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 14:50</span>
          <span class="news-item-title">特朗普批评泽连斯基：他可能从未想过结束俄乌战事</span>
          <span class="news-value-point">💡 中新网10月19日电 综合外媒报道，美国总统特朗普当地时间18日在社交媒体发文批评乌克兰袭击俄罗斯柴油炼油厂，称乌克兰总统泽连斯基可能从未想过结…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-19/10717163.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近期，国务院学位委员会办公室印发《关于做好专业学位研究生以实践成果申请学位工作的意见》(以下简称《意见》)。国务院学位委员会办公室(教育部学位管理与研究生教育司)负责人就有关问题回答了记者提问。" data-title="国务院学位办负责人就《关于做好专业学位研究生以实践成果申请学位工作的意见》答记者问" data-date="10-19 14:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 14:45</span>
          <span class="news-item-title">国务院学位办负责人就《关于做好专业学位研究生以实践成果申请学位工作的意见》答记者问</span>
          <span class="news-value-point">💡 近期，国务院学位委员会办公室印发《关于做好专业学位研究生以实践成果申请学位工作的意见》(以下简称《意见》)</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717266.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网10月19日电 国务院新闻办公室19日举行新闻发布会，商务部部长助理袁晓明表示，随着人民生活水平提升，消费者更加注重产品的品质和消费体验。根据商务部商务大数据显示，今年1-9月，重点平台智能眼镜销售额增长1.1倍。人工智能、物联网、区块链等新技术，在消费领域广泛应用，科技创新日益成为推动消费扩容升级的重要举措。" data-title="商务部：1" data-date="10-19 16:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:46</span>
          <span class="news-item-title">商务部：1</span>
          <span class="news-value-point">💡 中新网10月19日电 国务院新闻办公室19日举行新闻发布会，商务部部长助理袁晓明表示，随着人民生活水平提升，消费者更加注重产品的品质和消费体验</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/887.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 19 日消息，奇瑞将于 10 月 20 日在芜湖举办以“Change· 改变”为主题的 2026 奇瑞全球创新大会，发布首个行业垂域大模型。本次创新大会，奇瑞将展望瑶光 2035 计划，以智能 AI 技术为支撑，系统标定从汽车企业迈向全球智能科技公司的路线蓝图。作为实现这一目标的技术底座，大会上还将发布首个汽车行业垂域大模型，该模型融合了奇瑞在算力、算法、数据等领域的前沿技术能力，底层硬件则将展示专为物理 AI 世界模型设计的车规级芯片，不仅推动汽车产业进入全域 AI 体系化造车的新阶段，更为技术解决生活真实需求打开了更多可能。据介绍，在出行领域，猎鹰驾辅、灵犀智舱持续升级、全面上车，行业首款为全球而生原生前装 Robotaxi 亮相，凌霄 eVTOL 让立体空域出行更加" data-title="奇瑞将于 10 月 20 日举办全球创新大会，发布首个行业垂域大模型、人形机器人“墨宝”" data-date="10-19 16:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 16:39</span>
          <span class="news-item-title">奇瑞将于 10 月 20 日举办全球创新大会，发布首个行业垂域大模型、人形机器人“墨宝”</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，奇瑞将于 10 月 20 日在芜湖举办以“Change· 改变”为主题的 2026 奇瑞全球创新大会，发布首个…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/826.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 19 日消息，微博博主 @数码闲聊站 今天在微博透露，某厂超大杯手机基本确定采用 SM8975 / 骁龙 8EE6 芯片，暂定排期 2027 年 3 月-4 月。据介绍，这款手机将采用 6.85 英寸 BOE 2K+144Hz LTPO 屏幕，LIPO 四等边大 R 角直屏，配备 3D 超声波指纹。后续有用户在评论区询问：“有三超大底两亿吗”，博主回复道：“没有”；另一名用户则询问道：“米 20u 还有机会吗”，博主回复称：“不知道，暂时没有看到量产机规划。”结合博主文中暗示和评论区猜测，我们可以合理推测该机为 vivo X500 Ultra。据IT之家此前报道，vivo 副总裁、产品副总裁黄韬先前确认，X500 Ultra 机型会正常迭代，预计明年 3-4 月发布，影像" data-title="消息称某厂超大杯手机基本确定骁龙 8EE6 芯片、暂定排期明年 3-4 月，预计为 vivo X500 Ultra" data-date="10-19 14:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 14:44</span>
          <span class="news-item-title">消息称某厂超大杯手机基本确定骁龙 8EE6 芯片、暂定排期明年 3-4 月，预计为 vivo X500 Ultra</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，微博博主 @数码闲聊站 今天在微博透露，某厂超大杯手机基本确定采用 SM8975 / 骁龙 8EE6 芯片，暂…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/816.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 19 日消息，理想汽车 CEO 李想今日再度发文，谈及了“自研和合作”。他表示，这是不同阶段的不同选择。2020 年，我们决定自研。芯片、三电、增程器，这些核心环节，我们一步步做了起来。同时，我们也不排斥和任何技术顶级的供应商合作。自研和合作，是不同阶段的不同选择。据IT之家今日早些时候报道，李想认为汽车主机厂深入研究电池核心技术，有利于行业发展和消费者利益。他称这个世界既需要最懂智能电动车的电池企业，也需要最懂电池的智能电动车企业。理想汽车想做的是成为最懂电池的那一类企业，和最懂汽车的电池供应商一起，把长期没解决的问题往前推一步。根据规划，Power Day 理想汽车电动技术发布会已定档 10 月 20 日 19:30，届时将公布理想汽车的最新技术进展。" data-title="理想汽车 CEO 李想谈“自研和合作”，称是不同阶段的不同选择" data-date="10-19 14:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 14:39</span>
          <span class="news-item-title">理想汽车 CEO 李想谈“自研和合作”，称是不同阶段的不同选择</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，理想汽车 CEO 李想今日再度发文，谈及了“自研和合作”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/815.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 19 日消息，大晓机器人发布视觉空间锚定增强型具身基模型 ACE-Brain-0.6，该模型基于 Qwen3.5-9B 进行监督微调，重点提升目标识别、空间定位及交互区域判断能力。据大晓披露，该模型使用约百万条空间锚定训练样本，在八项 Grounding 评测中有六项成绩超过 OpenAI GPT-6 Astra。其中，七项公开基准平均得分为 74.53 分，高于后者的 73.68 分；在真实机器人场景评测 RobotGrounding 中取得 94.13 分，超越 Astra 的 91.10 分。ACE-Brain-0.6 技术概览图ACE-Brain-0.6 在八项 Grounding 评测中的六项超过 GPT-6 Astra据IT之家了解，大晓机器人是由商汤科技联合" data-title="大晓机器人发布具身基模型 ACE-Brain-0.6，六项空间感知评测超越 OpenAI GPT-6 Astra" data-date="10-19 14:37" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 14:37</span>
          <span class="news-item-title">大晓机器人发布具身基模型 ACE-Brain-0.6，六项空间感知评测超越 OpenAI GPT-6 Astra</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，大晓机器人发布视觉空间锚定增强型具身基模型 ACE-Brain-0.6，该模型基于 Qwen3.5-9B 进行…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-19/10717033.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网布鲁塞尔10月19日电 (记者 德永健)2026世界青年科学家峰会欧洲专场暨首届中欧青年科学家交流活动16日在布鲁塞尔举行，围绕科学外交、人工智能、中欧科技交流合作等议题展开深入研讨。" data-title="2026世界青年科学家峰会欧洲专场活动在布鲁塞尔举行" data-date="10-19 10:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 10:52</span>
          <span class="news-item-title">2026世界青年科学家峰会欧洲专场活动在布鲁塞尔举行</span>
          <span class="news-value-point">💡 中新网布鲁塞尔10月19日电 (记者 德永健)2026世界青年科学家峰会欧洲专场暨首届中欧青年科学家交流活动16日在布鲁塞尔举行，围绕科学外交、…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic表示，它将向该基金承诺其5%的股份。" data-title="Anthropic says it’s committing 5% of its shares to a ‘public benefit fund’" data-date="10-19 04:37" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-19 04:37</span>
          <span class="news-item-title">Anthropic表示，它将把5%的股份投入“公益基金”</span>
          <span class="news-item-title-en">Anthropic says it’s committing 5% of its shares to a ‘public benefit fund’</span>
          <span class="news-value-point">💡 Anthropic表示，它将向该基金承诺其5%的股份</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1013541/a-woman-was-arrested-in-philly-for-blocking-a-delivery-robot" target="_blank" rel="noopener" data-cat="keji" data-summary="Carolyn Marvin因阻挡优步派送机器人的路径并拒绝让路而被捕，并被指控行为不检。马文告诉费城的ABC13 “我知道他们正在接受人类送货员的工作，所以，" data-title="A woman was arrested in Philly for blocking a delivery robot" data-date="10-19 02:28" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-19 02:28</span>
          <span class="news-item-title">一名女子因拦截派送机器人而在费城被捕</span>
          <span class="news-item-title-en">A woman was arrested in Philly for blocking a delivery robot</span>
          <span class="news-value-point">💡 Carolyn Marvin因阻挡优步派送机器人的路径并拒绝让路而被捕，并被指控行为不检</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/amd-cards-now-run-all-dlss-features-thanks-to-one-developers-project-plans-to-match-native-nvidia-gpu-performance" target="_blank" rel="noopener" data-cat="keji" data-summary="Radeon GPU通过SOLO项目移植RDNA2-4 GPU的所有DLSS功能，获得完整的DLSS体验。" data-title="Modder brings full Nvidia DLSS 5 suite to three generations of AMD gaming GPUs" data-date="10-19 00:03" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-19 00:03</span>
          <span class="news-item-title">Modder为三代AMD游戏GPU带来了完整的Nvidia DLSS 5套件</span>
          <span class="news-item-title-en">Modder brings full Nvidia DLSS 5 suite to three generations of AMD gaming GPUs</span>
          <span class="news-value-point">💡 Radeon GPU通过SOLO项目移植RDNA2-4 GPU的所有DLSS功能，获得完整的DLSS体验</span>
        </a>
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
        <a class="news-item" href="https://www.qbitai.com/2026/10/504136.html" target="_blank" rel="noopener" data-cat="keji" data-summary="让人人都能自由创造并体验可交互世界" data-title="VAST开源实时世界模型EdenLive！单消费级显卡、720P超24FPS" data-date="10-18 19:49" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-18 19:49</span>
          <span class="news-item-title">VAST开源实时世界模型EdenLive！单消费级显卡、720P超24FPS</span>
          <span class="news-value-point">💡 让人人都能自由创造并体验可交互世界</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/19/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="弗洛里安·维尔茨（ Florian Wirtz ）在利物浦的进攻中承担了更多的责任，而皮埃尔·塞奇（ Pierre Sage ）在水晶宫（ Crystal Palace ）承受着压力多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）的身体状况在曼联（ Manchester United ）地区的一个角落里击败了布莱恩·姆博莫" data-title="Premier League: 10 talking points from the weekend’s action" data-date="10-19 15:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-19 15:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 弗洛里安·维尔茨（ Florian Wirtz ）在利物浦的进攻中承担了更多的责任，而皮埃尔·塞奇（ Pierre Sage ）在水晶宫（ Cr…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3qjnyw8qe4do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺尼·马杜埃克（ Noni Madueke ）在阿森纳可能没有他想要的角色，但他对诺丁汉森林队的胜利进球表明了他为什么是米克尔·阿尔特塔（ Mikel Arteta ）的重要球员之一。" data-title="Madueke&#39;s &#39;anger and conviction&#39; shows he&#39;s more than a &#39;finisher&#39;" data-date="10-19 03:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-19 03:55</span>
          <span class="news-item-title">Madueke的“愤怒和信念”表明他不仅仅是一个“终结者”</span>
          <span class="news-item-title-en">Madueke's 'anger and conviction' shows he's more than a 'finisher'</span>
          <span class="news-value-point">💡 诺尼·马杜埃克（ Noni Madueke ）在阿森纳可能没有他想要的角色，但他对诺丁汉森林队的胜利进球表明了他为什么是米克尔·阿尔特塔（ Mi…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6073pmddk0ko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰后卫Nordi Mukiele表示，由于上赛季的惊喜套餐在本赛季英超联赛中口吃，黑猫队可能已经变得“傲慢”。" data-title="&#39;Maybe we became arrogant&#39; - Sunderland struggles continue" data-date="10-19 02:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-19 02:49</span>
          <span class="news-item-title">“也许我们变得傲慢了” -桑德兰的斗争仍在继续</span>
          <span class="news-item-title-en">'Maybe we became arrogant' - Sunderland struggles continue</span>
          <span class="news-value-point">💡 桑德兰后卫Nordi Mukiele表示，由于上赛季的惊喜套餐在本赛季英超联赛中口吃，黑猫队可能已经变得“傲慢”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmwyd05wj00do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿在七场英超比赛中打进23球，包括一些惊人的一击，继续取悦他们的球迷，让他们梦想着可能发生的事情。" data-title="Shades of Barca and Beckham - Brighton aim to maintain superb start" data-date="10-19 02:33" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-19 02:33</span>
          <span class="news-item-title">巴萨和贝克汉姆的色调-布莱顿旨在保持出色的开局</span>
          <span class="news-item-title-en">Shades of Barca and Beckham - Brighton aim to maintain superb start</span>
          <span class="news-value-point">💡 布莱顿在七场英超比赛中打进23球，包括一些惊人的一击，继续取悦他们的球迷，让他们梦想着可能发生的事情</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/18/nottingham-forest-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="来自诺尼·马杜埃克（ Noni Madueke ）的一位迟到的偏转赢家在一场低质量的比赛中给了阿森纳一场至关重要的胜利，森林然后错过了两次扳平比分的好机会森林想要–也可能需要–让这场比赛变得一团糟。如果它是开放的并且通过中场打球， Arse" data-title="Nottingham Forest 0-1 Arsenal: Premier League – as it happened" data-date="10-19 01:41" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-19 01:41</span>
          <span class="news-item-title">诺丁汉森林0-1阿森纳：英超联赛–事实如此</span>
          <span class="news-item-title-en">Nottingham Forest 0-1 Arsenal: Premier League – as it happened</span>
          <span class="news-value-point">💡 来自诺尼·马杜埃克（ Noni Madueke ）的一位迟到的偏转赢家在一场低质量的比赛中给了阿森纳一场至关重要的胜利，森林然后错过了两次扳平比…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/nottingham-forest-arsenal-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="开球前的主题是空白。或者，更准确地说，任何一支球队是否可以停止向城市地面开火。让奥利弗·格拉斯纳（ Oliver Glasner ）感到非常不舒服的一个细节是，他的诺丁汉森林队（ Nottingham Forest team ）仍然需要在自己的比赛中得分" data-title="Madueke breaks Nottingham Forest’s resistance as dogged Arsenal edge to victory" data-date="10-19 01:39" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-19 01:39</span>
          <span class="news-item-title">Madueke打破诺丁汉森林的阻力，顽强的阿森纳取得胜利</span>
          <span class="news-item-title-en">Madueke breaks Nottingham Forest’s resistance as dogged Arsenal edge to victory</span>
          <span class="news-value-point">💡 开球前的主题是空白</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c699zmgmx9vzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）说，他本周戴着耳机，所以没有听到曼联周围的噪音，但在利兹1-1战平意味着这是六场没有胜利的比赛。" data-title="Mbeumo offers Carrick solace as Man Utd winless run goes on" data-date="10-19 01:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-19 01:24</span>
          <span class="news-item-title">Mbeumo为曼联提供Carrick慰藉，因为曼联的无胜跑仍在继续</span>
          <span class="news-item-title-en">Mbeumo offers Carrick solace as Man Utd winless run goes on</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）说，他本周戴着耳机，所以没有听到曼联周围的噪音，但在利兹1-1战平意味着这是六场没有胜利的比…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/18/leeds-v-manchester-united-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利兹的多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）取消了布莱恩·姆贝乌莫（ Bryan Mbeumo ）的⚽揭幕战，为参观者结束了动荡的一周六人的喜悦：利兹对曼联的比赛利兹经理丹尼尔·法克（ Daniel Farke ）是下一位与天空体育（ Sky Sports ）交谈的人：我们必须确保" data-title="Leeds United 1-1 Manchester United: Premier League – as it happened" data-date="10-18 23:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:25</span>
          <span class="news-item-title">利兹联队1-1曼联：英超联赛–实际情况</span>
          <span class="news-item-title-en">Leeds United 1-1 Manchester United: Premier League – as it happened</span>
          <span class="news-value-point">💡 利兹的多米尼克·卡尔弗特-莱温（ Dominic Calvert-Lewin ）取消了布莱恩·姆贝乌莫（ Bryan Mbeumo ）的⚽揭幕战…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/bournemouth-sunderland-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="伯恩茅斯和马可·罗斯等待英超冠军的胜利已经结束。被锁定在倒数三名的桑德兰，正在成为本赛季走得太远、太快的客观教训。一旦凯文·丹索在第17分钟因拒绝而被解雇" data-title="Evanilson swivels his hips to seal Bournemouth win against 10" data-date="10-18 23:19" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 23:19</span>
          <span class="news-item-title">埃文尼尔森旋转臀部，以封印伯恩茅斯对10的胜利</span>
          <span class="news-item-title-en">Evanilson swivels his hips to seal Bournemouth win against 10</span>
          <span class="news-value-point">💡 伯恩茅斯和马可·罗斯等待英超冠军的胜利已经结束</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/18/leeds-manchester-united-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克和曼联的下一步是什么？从游戏角度来看，答案是周三的COMO之旅，但在再次失败之后，他们的联赛胜利数量翻了一番，达到了两倍，你不得不怀疑一支已经扁平化的球队的目的地。" data-title="Manchester United held as Calvert-Lewin’s Leeds leveller keeps pressure on Carrick" data-date="10-18 23:08" data-source="卫报">
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/014/938.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，FlymeAIOS 今日透露，9 月，Flyme Auto 新增装机 154,206 辆，前三季度装机量超 1,326,000 辆，全球累计搭载超 3,594,000 辆。据IT之家此前报道，魅族 Flyme Auto 车载软件系统发布于 2023 年 3 月，支持无缝接力、手机辅助 OTA、手机-汽车硬件互通共享硬件能力，支持手机寻车，支持平行视窗、小窗展示、跨端可见即可说等软件功能。Flyme Auto 2 发布于去年 8 月，带来了实况桌面 3D 质感、全场景一镜到底、Alive 壁纸、自定义桌面插件等功能，Aicy 大卡片、全新小窗模式提供了更轻量更高效的交互方式。AI 能力贯通整车全域，AI 读心术主动判断用户意图，自动完成常用操作，并且此次更新还" data-title="Flyme Auto 车机 9 月新增装机 15.4 万辆，累计搭载超 359 万辆" data-date="10-19 17:15" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 17:15</span>
          <span class="news-item-title">Flyme Auto 车机 9 月新增装机 15.4 万辆，累计搭载超 359 万辆</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，FlymeAIOS 今日透露，9 月，Flyme Auto 新增装机 154,206 辆，前三季度装机量超 1…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/934.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，据汽车媒体 Motor1 今天报道，美国造车新势力 Rivian 最近启动自动驾驶早期体验计划，邀请小部分车主体验点对点辅助驾驶功能。IT之家从原报道获悉，所有订阅 Autonomy+ 付费服务的第二代 R1 或 R2 车主均可申请加入计划。Rivian 正按计划推进开发工作，目标年底前向公众推出首个测试版本，并在 2027 年进一步扩大覆盖范围。Rivian 表示，点对点辅助驾驶功能基于 Universal Hands-Free 系统打造。启用该功能后，车辆能实现的不只是保持车道行驶，而是能够自行完成道路汇入、转向等操作，进行完整的辅助驾驶。不过需要注意的是，这套系统仍然是 L2 级辅助驾驶，驾驶员必须集中注意力观察路面，随时做好接管准备。" data-title="美国造车新势力 Rivian 推出点到点辅助驾驶，年底开放测试" data-date="10-19 17:13" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 17:13</span>
          <span class="news-item-title">美国造车新势力 Rivian 推出点到点辅助驾驶，年底开放测试</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，据汽车媒体 Motor1 今天报道，美国造车新势力 Rivian 最近启动自动驾驶早期体验计划，邀请小部分车主…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/915.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，日本知名视觉小说工作室 Key 社今天宣布，其核心创作者麻枝准罹患咽喉癌。Key 社表示，麻枝准从今年春季开始感觉喉咙不适，进入夏季后，他的喉咙肿胀和疼痛症状逐渐加重。经医疗机构检查后，他被确诊为咽喉癌。麻枝准反复考虑自身病情和治疗前景后，希望尽可能保留自身精力专注于创作活动。因此他决定不接受积极治疗，而是选择以姑息治疗为主的疗养方式。同时，麻枝准正在负责《炽焰天穹》游戏的剧情撰写和音乐制作，同时在构想全新音乐项目。他已经完成《绯染天空》主线剧情第六章前篇部分，直至第六章完结的主要部分也已经全部创作完成。并且，本作第六章前篇相关歌曲的作词和作曲工作也已完成。随着病情发展，麻枝准本人可能无法完成以后的剧情和音乐制作。此外，麻枝准还在构想一个全新音乐项目。确诊咽" data-title="Key 社核心作者麻枝准罹患咽喉癌：本人选择放弃积极治疗，专注更新《炽焰天穹》、制作全新音乐项目" data-date="10-19 17:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 17:01</span>
          <span class="news-item-title">Key 社核心作者麻枝准罹患咽喉癌：本人选择放弃积极治疗，专注更新《炽焰天穹》、制作全新音乐项目</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，日本知名视觉小说工作室 Key 社今天宣布，其核心创作者麻枝准罹患咽喉癌</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717265.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月19日电 (记者 孙自法)由中国科学院心理研究所主办、该所国民心理健康评估发展中心承办的“圆梦工程”农村未成年人心理健康教育三周年成果展，10月19日在北京海淀中关村融科资讯中心·融空间开幕，来自全国各地参与2026年度“圆梦工程”艺术疗育课堂上创作的400余幅作品将持续展出至11月6日，线上云展同步上线。" data-title="农村未成年人心理健康教育三周年 “圆梦工程”专题成果展在北京开幕" data-date="10-19 16:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:43</span>
          <span class="news-item-title">农村未成年人心理健康教育三周年 “圆梦工程”专题成果展在北京开幕</span>
          <span class="news-value-point">💡 中新网北京10月19日电 (记者 孙自法)由中国科学院心理研究所主办、该所国民心理健康评估发展中心承办的“圆梦工程”农村未成年人心理健康教育三周…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/878.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="此为资源机，介意慎拍！iPhone 17 Pro Max 2TB 美版无锁权益机（双 esim）今日“京东数码海外自营旗舰店”裸机（不含数据线 + 京东包装非原封）直降至 9399 元。权益机 / 资源机是由苹果代工厂对苹果官方 7 天无理由退货以及产线上多余的原材料进行生产，经过产品工程师相应功能测试，且确保为 Apple 官方原装部件后，再由苹果全球合作伙伴进行销售。由于 Apple 授权工厂生产环节较多，无法保证机身无瑕疵，有可能会造成机身框、屏幕等存在划痕白点凹痕等外观瑕疵问题，介意慎拍。本次支持免费改双卡，不支持苹果官方保修，京东售后 1 年。京东 iPhone 17 Pro Max 2TB 美版无锁 需录开箱视频 9399 元直达链接京东 11.11 红包至高 26888 元无门" data-title="iPhone 17 Pro Max 2TB 美版 9339 元京东再降价，支持免费改双卡" data-date="10-19 16:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 16:32</span>
          <span class="news-item-title">iPhone 17 Pro Max 2TB 美版 9339 元京东再降价，支持免费改双卡</span>
          <span class="news-value-point">💡 此为资源机，介意慎拍</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/877.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，金摇杆奖（Golden Joystick Awards）昨日公布“年度主机游戏”奖项提名，卡普空旗下 3 款作品《鬼武者：剑之道》《识质存在》《生化危机：安魂曲》入围。IT之家附金摇杆奖年度主机游戏提名作品如下：《007：初露锋芒》《火焰之纹章万缕千丝》《极限竞速：地平线 6》《乐高蝙蝠侠：黑暗骑士之遗》《仁王 3》《鬼武者：剑之道》《宝可梦 Pokopia》《识质存在》《生化危机：安魂曲》《沙罗周期》金摇杆奖评选活动始于 1983 年，是最古老的游戏产业大奖之一。该奖最初由英国公众投票选出，现已成为一项可通过 GamesRadar+ 网站投票的全球活动。这个奖项最初只包含电脑游戏，后来扩展至主机游戏。" data-title="卡普空 3 款作品获金摇杆奖“年度主机游戏”提名：含《鬼武者：剑之道》《识质存在》《生化危机：安魂曲》" data-date="10-19 16:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 16:28</span>
          <span class="news-item-title">卡普空 3 款作品获金摇杆奖“年度主机游戏”提名：含《鬼武者：剑之道》《识质存在》《生化危机：安魂曲》</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，金摇杆奖（Golden Joystick Awards）昨日公布“年度主机游戏”奖项提名，卡普空旗下 3 款作…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717248.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨10月19日电(白玛玉珍)2026年西藏自治区田径耐力性项目青少年夏令营暨业余体校对抗赛于10月19日至22日在拉萨市举办。来自全区七市地重点业余体校及西藏自治区体育运动技术学校的180余名运动员、教练员参赛。" data-title="西藏举办青少年田径夏令营暨业余体校对抗赛 创新模式选拔后备人才" data-date="10-19 16:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:23</span>
          <span class="news-item-title">西藏举办青少年田径夏令营暨业余体校对抗赛 创新模式选拔后备人才</span>
          <span class="news-value-point">💡 中新网拉萨10月19日电(白玛玉珍)2026年西藏自治区田径耐力性项目青少年夏令营暨业余体校对抗赛于10月19日至22日在拉萨市举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717244.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆10月19日电 (梁钦卿)重庆市气象局副局长周国兵19日在重庆市政府新闻办举行的政策例行吹风会上介绍，聚焦防灾减灾，川渝两地织密流域联防“一张网”，已划定川东北渝东北、合广长碚、涪江中下游、川南渝西四大联防片区，实现毗邻区县气象联防全覆盖。" data-title="川渝织密流域联防“一张网” 实现毗邻区县气象联防全覆盖" data-date="10-19 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 16:22</span>
          <span class="news-item-title">川渝织密流域联防“一张网” 实现毗邻区县气象联防全覆盖</span>
          <span class="news-value-point">💡 中新网重庆10月19日电 (梁钦卿)重庆市气象局副局长周国兵19日在重庆市政府新闻办举行的政策例行吹风会上介绍，聚焦防灾减灾，川渝两地织密流域联…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717176.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网怀化10月19日电 (张建雄 滕雪慧)湖南麻阳苗族自治县19日透露，10月25日，“张雪机车”创始人张雪将驾驶改装摩托车张雪机车MX450，在该县郭公坪镇小坡村挑战拟定40公里距离的“改装摩托车在开阔水域行驶最远距离”吉尼斯世界纪录。" data-title="张雪将在麻阳挑战机车水上漂吉尼斯世界纪录" data-date="10-19 15:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 15:08</span>
          <span class="news-item-title">张雪将在麻阳挑战机车水上漂吉尼斯世界纪录</span>
          <span class="news-value-point">💡 中新网怀化10月19日电 (张建雄 滕雪慧)湖南麻阳苗族自治县19日透露，10月25日，“张雪机车”创始人张雪将驾驶改装摩托车张雪机车MX450…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/836.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，据央视新闻报道，在陕西西安雁塔法院审结的一起“不当得利纠纷”案中，游戏公司在返还未成年人充值退款后，却因为转账时操作失误，多退了三万多元。面对这笔“意外之财”，对方不仅拒不返还，而且在庭审中还使用 AI 伪造通话录音试图蒙混过关。小涵（化名）使用游戏平台充值了约 5 万元，其母亲刘某将游戏公司诉至广州某法院。经法院调解，双方达成协议：游戏公司按 30% 的比例退还 15695.4 元。然而，游戏公司工作人员在操作退款时出现失误，实际退还了 49323 元，比约定金额多退了 33627.6 元。发现失误后，游戏公司立即联系刘某，要求返还多退的款项，但遭到拒绝。无奈之下，游戏公司将刘某诉至西安市雁塔区人民法院。庭审中，被告刘某辩称，游戏公司已经通过电话同意免除其" data-title="游戏公司未成年退款多退三万元，对方拒不返还、AI 伪造录音被当庭训诫" data-date="10-19 15:08" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 15:08</span>
          <span class="news-item-title">游戏公司未成年退款多退三万元，对方拒不返还、AI 伪造录音被当庭训诫</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，据央视新闻报道，在陕西西安雁塔法院审结的一起“不当得利纠纷”案中，游戏公司在返还未成年人充值退款后，却因为转账…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/834.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，据韩媒 The Elec 报道，韩国外卖平台 Baedal Minjok（배달의민족）旗下约 201 名骑手的个人信息近日被发现暴露在一家配送外包公司的网站服务器中，相关数据无需身份验证即可从外部访问。据报道，相应配送外包公司的网站旨在让骑手查询配送业绩，正常情况下用户需要输入姓名、电话号码末尾几位数字以及密码才能查看相关信息。然而，存储个人信息的数据文件夹却没有设置独立的身份验证机制，因此外部人员只需在网站地址后添加特定路径，就能直接访问相关数据，Baedal Minjok 的运营商 Woowa Brothers 对此回应称：“此事与我们的服务没有直接关系。”目前，相关信息泄露事件的具体影响范围及后续处理情况尚待进一步确认。" data-title="因配送外包公司网站验证机制设置不当，韩国外卖平台 Baedal Minjok 旗下约 201 名骑手信息遭曝光" data-date="10-19 15:04" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 15:04</span>
          <span class="news-item-title">因配送外包公司网站验证机制设置不当，韩国外卖平台 Baedal Minjok 旗下约 201 名骑手信息遭曝光</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，据韩媒 The Elec 报道，韩国外卖平台 Baedal Minjok（배달의민족）旗下约 201 名骑手的…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717170.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网乌鲁木齐10月19日电 (胡嘉琛)“我们是一家人，以后一定要常来常往。”19日，结束“看海之约”返回新疆阿克陶县的牧民麦麦提萨伍提·亚森接受中新网采访时，反复说起与深圳“摩友”道别时的约定——“帕米尔高原再见”。" data-title="新疆牧民与深圳“摩友”的双向奔赴" data-date="10-19 15:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 15:02</span>
          <span class="news-item-title">新疆牧民与深圳“摩友”的双向奔赴</span>
          <span class="news-value-point">💡 中新网乌鲁木齐10月19日电 (胡嘉琛)“我们是一家人，以后一定要常来常往</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717167.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南京10月19日电 (记者 徐珊珊)“百万青年聚金陵·百校巡回招引”东南大学专场活动近日在东南大学九龙湖校区举行。活动集城市宣介、专场招聘、主题市集于一体，向高校青年学子发出“选择南京、扎根金陵”的诚挚邀约。" data-title="110家单位携2500个岗位揽才 南京向青年学子发出邀约" data-date="10-19 15:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 15:01</span>
          <span class="news-item-title">110家单位携2500个岗位揽才 南京向青年学子发出邀约</span>
          <span class="news-value-point">💡 中新网南京10月19日电 (记者 徐珊珊)“百万青年聚金陵·百校巡回招引”东南大学专场活动近日在东南大学九龙湖校区举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-19/10717173.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国新闻周刊记者：徐鹏远" data-title="顾彬：跟李白“坐在一起喝酒”" data-date="10-19 14:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-19 14:59</span>
          <span class="news-item-title">顾彬：跟李白“坐在一起喝酒”</span>
          <span class="news-value-point">💡 中国新闻周刊记者：徐鹏远</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/832.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 19 日消息，腾讯官方今天宣布，旗下人工智能管家 Marvis（马维斯）已上架麒麟软件商店，面向银河麒麟桌面操作系统版本：V10SP1（X86、ARM），支持多款国产 CPU 和主流计算平台。IT之家了解到，Marvis 是一款操作系统层级的个人 AI 管家，它可以直接操控电脑，执行调整屏幕亮度、切换深色模式等。例如用户可以向它提问：“鼠标用着怎么不跟手，帮我调下”，小马就会自行尝试诊断问题。同时，Marvis 还可以按指令打开“安全中心”进行安全体检、病毒查杀和漏洞修复，也可以调用“麒麟管家”进行垃圾清理、故障诊断。或者在官方渠道安装 / 卸载软件。此外，该软件还拥有系统运维、本地文档智能检索处理、任务自动化及跨端远控等功能。用户哪怕离开电脑，也可以通过 Marvis" data-title="腾讯 AI 管家 Marvis（马维斯）上架麒麟软件商店，深度适配国产操作系统" data-date="10-19 14:59" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-19 14:59</span>
          <span class="news-item-title">腾讯 AI 管家 Marvis（马维斯）上架麒麟软件商店，深度适配国产操作系统</span>
          <span class="news-value-point">💡 IT之家 10 月 19 日消息，腾讯官方今天宣布，旗下人工智能管家 Marvis（马维斯）已上架麒麟软件商店，面向银河麒麟桌面操作系统版本：V…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-19 17:16（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
