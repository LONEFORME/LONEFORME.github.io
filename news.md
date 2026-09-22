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
      <span>2026-09-22 14:57 抓取更新</span>
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
        <span class="channel-count">54</span>
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
        <span class="channel-count">9</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">0</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.bbc.com/zhongwen/articles/cjp30pv25xd7o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随后，当川普前往纽约参加联合国峰会时，美国各大电视网暂停了白宫的电视转播。" data-title="CNN 等三家美国媒体被禁入白宫后 起诉特朗普政府" data-date="09-22 14:52" data-source="BBC">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
        <span class="hero-featured-date">🕒 09-22 14:52</span>
      </div>
      <h2 class="hero-featured-title">CNN 等三家美国媒体被禁入白宫后 起诉特朗普政府</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/005/705.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 22 日消息，已经升级最新版 FSD（监督版）更新的特斯拉车主，在中控屏幕上遇到了一个恼人的异常问题。在升级至 14.3.9 版本之后，大量车主反馈车辆会频繁弹出警示，提示前置 FSD 摄像头脏污，要求车主前往服务中心检修；然而此时挡风玻璃与摄像头外壳实际上干干净净，没有任何污渍。所幸问题并非硬件损坏，摄像头本身并没有脏。用户 @CARN0N 在 X 平台发帖反映该现象，并且晒出特斯拉客服人员的回复，证实这类弹窗属于软件漏洞，特斯拉方面已经知晓该问题。报错背后的程序漏洞IT之家注意到，该故障是特斯拉本月早些时候推送 FSD v14.3.9 之后随即出现的。这一版本虽然新增了全新的自动碰撞避险功能，但同时引入了一个视觉编码器过度敏感的程序缺陷。该版本软件让神经网络的摄像头可视" data-title="误报摄像头脏污，特斯拉 FSD v14.3.9 出现软件漏洞" data-date="09-22 14:50" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">误报摄像头脏污，特斯拉 FSD v14.3.9 出现软件漏洞</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/005/713.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 9 月 22 日消息，宝马集团今日宣布为旗下电动 MINI 品牌推出一款全新特别版车型，定名为“酷不列颠”版。MINI 酷不列颠特别版共推出 4 款车型，售价 20.88-32.08 万元。其中，MINI 酷不列颠收藏版限量 3 台，限时礼遇价 298888 元。该版本最大亮点在于将英国米字旗图案完整喷涂于整车车身，以此展现鲜明的英伦文化特征。据官方介绍，“酷不列颠”（Cool Britannia）源自 20 世纪 90 年代的英国文化浪潮。音乐、艺术、电影与时尚重新诠释传统英国元素，米字旗也由此成为鲜明的流行文化符号。MINI 将它铺展在车身上，既致敬英伦文化，也表达打破常规的个性。该车型车身采用不对称设计，一面完整的米字旗覆盖整个车体表面。喷涂工艺需在全车范围内进行三次喷漆作业" data-title="宝马 MINI 酷不列颠系列车型正式上市：20.88 万元起，手工打磨 74 条分色线" data-date="09-22 14:55" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">宝马 MINI 酷不列颠系列车型正式上市：20.88 万元起，手工打磨 74 条分色线</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/005/712.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，Omdia 英国当地时间今日根据其统计的最新数据表示，中国大陆 PC 出货量在 2026 年第 2 季度达到 1140 万台，同比增长 11%。从形态上来看，尽管笔记本电脑出货在 2026Q2 下滑 2% 至 710 万台，但激增 42% 的台式机出货（430 万台）扭转了整体局面。而如果依用途划分，消费级 PC 出货在 2026Q2 下滑 2%，广义商用 PC 增长 29%。Omdia 同时预测，2026 年全年的中国大陆 PC 出货量将为 3970 万台，下降 6%；其中消费级产品跌幅将达到 10%，狭义商用级下滑 4%，政府及教育类别同比增长 16%。图源：PexelsOmdia 高级分析师 Emma Xu 表示：中国大陆的商用 PC 需求，尤其是来自大" data-title="Omdia：中国大陆 PC 出货 2026Q2 同比增长 11%，预计全年下滑 6%" data-date="09-22 14:55" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">Omdia：中国大陆 PC 出货 2026Q2 同比增长 11%，预计全年下滑 6%</p>
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
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cjp30pv25xd7o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随后，当川普前往纽约参加联合国峰会时，美国各大电视网暂停了白宫的电视转播。" data-title="CNN 等三家美国媒体被禁入白宫后 起诉特朗普政府" data-date="09-22 14:52" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 14:52</span>
          <span class="news-item-title">CNN 等三家美国媒体被禁入白宫后 起诉特朗普政府</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701451.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 综合外媒报道，阿根廷总统米莱当地时间21日表示，不会以军事手段解决马尔维纳斯群岛(简称马岛，英国称福克兰群岛)主权争端。" data-title="阿根廷总统表态：不会用军事手段解决马岛主权争端" data-date="09-22 14:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 14:49</span>
          <span class="news-item-title">阿根廷总统表态：不会用军事手段解决马岛主权争端</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701433.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 综合韩联社、韩国《京乡新闻》报道，韩国首尔高等法院22日对前总统尹锡悦妻子金建希涉嫌“卖官鬻爵”案作出二审判决，判处其有期徒刑5年。刑期较一审判决减轻。" data-title="金建希涉嫌“卖官鬻爵”案二审获刑5年 刑期较一审判决减轻" data-date="09-22 14:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 14:27</span>
          <span class="news-item-title">金建希涉嫌“卖官鬻爵”案二审获刑5年 刑期较一审判决减轻</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701403.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月22日电 (记者 官逸伦)泰国驻华大使韩灿才21日在北京表示，下一个50年，在推动泰国与中国紧密合作、构建两国紧密伙伴关系的过程中，人的作用愈发关键，尤其是青年群体，“因为你们是国家的未来”。" data-title="泰国驻华大使：冀泰中青年推动两国关系持续发展" data-date="09-22 14:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 14:00</span>
          <span class="news-item-title">泰国驻华大使：冀泰中青年推动两国关系持续发展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701415.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 据韩国《中央日报》报道，韩国总统李在明21日与同属共同民主党的韩国前总统文在寅通电话，就国政议题交换了意见。" data-title="李在明和文在寅通电话 就国政议题交换意见" data-date="09-22 13:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 13:54</span>
          <span class="news-item-title">李在明和文在寅通电话 就国政议题交换意见</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701389.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州9月22日电 (方伟彬 李典 匡雷)中越海警第二届党政工作交流活动21日在中国广东广州正式拉开帷幕。中方代表团团长、中国海警局南海分局政治委员王小兵，越方代表团团长、越南海警司令部第一海区少将政治委员陈文厚共同出席启动仪式。双方海警政治工作、国际合作及相关业务部门负责人参加本次活动。" data-title="中越海警第二届党政工作交流活动在广州开幕" data-date="09-22 13:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 13:21</span>
          <span class="news-item-title">中越海警第二届党政工作交流活动在广州开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701377.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社福建三明9月22日电 题：从乡建乡创到城建城创：台湾团队“陪伴式”扎根福建" data-title="从乡建乡创到城建城创：台湾团队“陪伴式”扎根福建" data-date="09-22 12:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 12:55</span>
          <span class="news-item-title">从乡建乡创到城建城创：台湾团队“陪伴式”扎根福建</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701350.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 9月22日，国新办就促进自然资源安全高效永续利用有关情况举行新闻发布会。自然资源部党组书记、国家自然资源总督察刘国洪在会上介绍，我国推动自然保护地整合优化方案陆续落地，国家公园旗舰物种数量持续恢复增长，海南长臂猿种群数量增至44只，野生东北虎增至72只。新一批“山水工程”全面启动，“三北”工程攻坚战累计完成各类建设任务2.65亿亩，生态系统质量和稳定性稳步提升。" data-title="自然资源部：我国野生东北虎增至72只" data-date="09-22 12:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 12:21</span>
          <span class="news-item-title">自然资源部：我国野生东北虎增至72只</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701376.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="9月22日，第48届世界技能大赛将在上海开幕，68个国家和地区的1385名选手飞来参赛。很多人看到新闻的第一反应是这比的是什么？看到比赛项目也有人会好奇，焊管子、砌墙，也有世界比赛？" data-title="比了76年！全世界都来上海比&quot;手艺活&quot;，比的到底是啥" data-date="09-22 12:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 12:19</span>
          <span class="news-item-title">比了76年！全世界都来上海比"手艺活"，比的到底是啥</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701374.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 据领事直通车微信公众号消息，中秋、国庆假期将至，外交部领事保护中心提醒拟赴海外中国公民提升防范意识，安全文明出行。" data-title="外交部领事保护中心提醒中国公民中秋、国庆假期注意海外出行安全" data-date="09-22 12:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 12:04</span>
          <span class="news-item-title">外交部领事保护中心提醒中国公民中秋、国庆假期注意海外出行安全</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701333.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 综合日媒报道，近日，大批日本民众在日本国会前举行集会，抗议日本高市早苗政府的修宪企图，反对高市政府“再军事化”动向。" data-title="日本上万民众集会抗议 反对高市政府打造“战争国家”" data-date="09-22 11:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 11:21</span>
          <span class="news-item-title">日本上万民众集会抗议 反对高市政府打造“战争国家”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701329.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月22日电 哥本哈根消息：丹麦首相府当地时间21日发布新闻稿，宣布丹麦及其自治领地格陵兰岛将于22日在纽约和美国签署一项协议，以加强北极和北大西洋地区安全。" data-title="丹麦及格陵兰岛将和美国签署安全协议" data-date="09-22 11:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 11:19</span>
          <span class="news-item-title">丹麦及格陵兰岛将和美国签署安全协议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701328.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月22日电 据朝中社22日报道，朝鲜导弹总局20日成功进行新型武器试验。朝鲜劳动党总书记、国务委员长金正恩观摩了试验。" data-title="金正恩观摩朝鲜导弹总局新型武器试验" data-date="09-22 11:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 11:16</span>
          <span class="news-item-title">金正恩观摩朝鲜导弹总局新型武器试验</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c98r687436nvo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="现年73岁的习近平，早已不再是那名访美时的县级官员。在近14年的中国领导人任期内，他改变了中国共产党以及这个国家在世界上的地位。" data-title="习近平：从失去一切的“太子”到中国最有权势的领导人" data-date="09-22 10:49" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 10:49</span>
          <span class="news-item-title">习近平：从失去一切的“太子”到中国最有权势的领导人</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/21/business/china-rare-earth-summit.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着美国和中国官员就出口限制进行谈判，对全球工业产生影响，制造商正在努力应对供应限制。" data-title="中国对稀土的持续控制笼罩着特朗普" data-date="09-22 10:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 10:00</span>
          <span class="news-item-title">中国对稀土的持续控制笼罩着特朗普</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/005/705.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 22 日消息，已经升级最新版 FSD（监督版）更新的特斯拉车主，在中控屏幕上遇到了一个恼人的异常问题。在升级至 14.3.9 版本之后，大量车主反馈车辆会频繁弹出警示，提示前置 FSD 摄像头脏污，要求车主前往服务中心检修；然而此时挡风玻璃与摄像头外壳实际上干干净净，没有任何污渍。所幸问题并非硬件损坏，摄像头本身并没有脏。用户 @CARN0N 在 X 平台发帖反映该现象，并且晒出特斯拉客服人员的回复，证实这类弹窗属于软件漏洞，特斯拉方面已经知晓该问题。报错背后的程序漏洞IT之家注意到，该故障是特斯拉本月早些时候推送 FSD v14.3.9 之后随即出现的。这一版本虽然新增了全新的自动碰撞避险功能，但同时引入了一个视觉编码器过度敏感的程序缺陷。该版本软件让神经网络的摄像头可视" data-title="误报摄像头脏污，特斯拉 FSD v14.3.9 出现软件漏洞" data-date="09-22 14:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:50</span>
          <span class="news-item-title">误报摄像头脏污，特斯拉 FSD v14.3.9 出现软件漏洞</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493629.html" target="_blank" rel="noopener" data-cat="keji" data-summary="未来Qwen4.5、Qwen5等版本将扩展至5-10T参数。" data-title="阿里研究员透露Qwen4.5后模型将扩展至5" data-date="09-22 11:48" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 11:48</span>
          <span class="news-item-title">阿里研究员透露Qwen4.5后模型将扩展至5</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493625.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月22日， 2026云栖大会开幕，阿里巴巴公布大模型最新进展。" data-title="阿里公布全模态模型新进展，Qwen4和下代视频模型均在训练中" data-date="09-22 11:42" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 11:42</span>
          <span class="news-item-title">阿里公布全模态模型新进展，Qwen4和下代视频模型均在训练中</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493502.html" target="_blank" rel="noopener" data-cat="keji" data-summary="吴泳铭表示，阿里巴巴将坚定投入AI模型、AI芯片和AI云这三项基础设施建设，这是阿里的长期战略选择。" data-title="阿里巴巴：机器智能时代，坚定投入AI模型 AI芯片 AI云三大基石" data-date="09-22 10:59" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 10:59</span>
          <span class="news-item-title">阿里巴巴：机器智能时代，坚定投入AI模型 AI芯片 AI云三大基石</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493363.html" target="_blank" rel="noopener" data-cat="keji" data-summary="弥补算力缺口，不能只靠堆料" data-title="AI算力之争不靠堆卡！浪潮信息捅破智算“能力天花板”，还瓦解了“产能焦虑”" data-date="09-22 10:22" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 10:22</span>
          <span class="news-item-title">AI算力之争不靠堆卡！浪潮信息捅破智算“能力天花板”，还瓦解了“产能焦虑”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/21/nyregion/trump-mamdani-meeting-nyc.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Mayor Zohran Mamdani invited the president to his official residence in Manhattan, where the two spoke about policing, immigration and affordable housing." data-title="Trump and Mamdani Show Their Unlikely Rapport, This Time in New York" data-date="09-22 08:10" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 08:10</span>
          <span class="news-item-title">Trump and Mamdani Show Their Unlikely Rapport, This Time in New York</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/21/the-man-who-built-apples-stores-doesnt-buy-silicon-valleys-bet-on-ai-shopping/" target="_blank" rel="noopener" data-cat="keji" data-summary="苹果零售店建筑师罗恩·约翰逊（ Ron Johnson ）表示，苹果的秘密酱汁一直" data-title="建造苹果商店的人不会买硅谷在人工智能购物上的赌注" data-date="09-22 07:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-22 07:44</span>
          <span class="news-item-title">建造苹果商店的人不会买硅谷在人工智能购物上的赌注</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/21/world/un-general-assembly-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Diplomats, dignitaries and tech experts gathered amid the United Nations General Assembly to debate how to address the threats and harness the potential of artificial intelligence." data-title="Spectre of Rogue A.I. Looms Over U.N. Talks on Digital Cooperation" data-date="09-22 05:08" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 05:08</span>
          <span class="news-item-title">Spectre of Rogue A.I. Looms Over U.N. Talks on Digital Cooperation</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/998453/california-ai-data-center-bills" target="_blank" rel="noopener" data-cat="keji" data-summary="正如《洛杉矶时报》早些时候报道的那样，加利福尼亚州州长加文·纽瑟姆（ Gavin Newsom ）签署了七项法案，旨在防止人工智能数据中心将公用事业成本转嫁给居民。这套法律要求加州公用事业委员会为数据中心引入新的费率分类，同时迫使它们支付升级到[…]的费用" data-title="加州收紧人工智能数据中心能源和水资源使用规定" data-date="09-22 04:29" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-22 04:29</span>
          <span class="news-item-title">加州收紧人工智能数据中心能源和水资源使用规定</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/" target="_blank" rel="noopener" data-cat="keji" data-summary="该小组不会有放慢或重定向OpenAI正在进行的数学研究的余地。" data-title="OpenAI成立数学咨询小组，其AI解决了100多个未解决的问题" data-date="09-22 04:15" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-22 04:15</span>
          <span class="news-item-title">OpenAI成立数学咨询小组，其AI解决了100多个未解决的问题</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/21/metas-muse-is-outpacing-chatgpts-early-mobile-launch/" target="_blank" rel="noopener" data-cat="keji" data-summary="根据Appfigures的最新估计， Meta的新人工智能代理Muse在美国和加拿大的下载量和日活跃用户数量超过了ChatGPT在移动首次亮相后的同期。" data-title="Meta的Muse正在超越ChatGPT的早期移动发布" data-date="09-22 03:19" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-22 03:19</span>
          <span class="news-item-title">Meta的Muse正在超越ChatGPT的早期移动发布</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd" target="_blank" rel="noopener" data-cat="keji" data-summary="沃尔玛正在销售一款配备Ryzen 7 9800X3D、GeForce RTX 5080 Founders Edition、32GB DDR5-6000内存和1TB PCIe 4.0 SSD的CyberPowerPC游戏PC ，售价为$ 2,299。" data-title="在游戏PC中获得世界上最快的游戏CPU和DLSS 5功能GPU ，价格为$ 2,299 —满载的Powerhouse Sports Ryzen 7 9800X3D、RTX 5080 Founders Edition、32GB RAM和1TB SSD" data-date="09-22 01:19" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 01:19</span>
          <span class="news-item-title">在游戏PC中获得世界上最快的游戏CPU和DLSS 5功能GPU ，价格为$ 2,299 —满载的Powerhouse Sports Ryzen 7 9800X3D、RTX 5080 Founders Edition、32GB RAM和1TB SSD</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd" target="_blank" rel="noopener" data-cat="keji" data-summary="沃尔玛正在销售一款配备Ryzen 7 9800X3D、GeForce RTX 5080 Founders Edition、32GB DDR5-6000内存和1TB PCIe 4.0 SSD的CyberPowerPC游戏PC ，售价为$ 2,299。" data-title="在游戏PC中获得世界上最快的游戏CPU和DLSS 5功能GPU ，价格为$ 2,299 —满载Powerhouse Sport Ryzen 7 9800X3D、RTX 5080 Founders Edition、32GB RAM和1TB SSD [更新]" data-date="09-22 01:19" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 01:19</span>
          <span class="news-item-title">在游戏PC中获得世界上最快的游戏CPU和DLSS 5功能GPU ，价格为$ 2,299 —满载Powerhouse Sport Ryzen 7 9800X3D、RTX 5080 Founders Edition、32GB RAM和1TB SSD [更新]</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/21/science/ai-anthropomorphism-consciousness.html" target="_blank" rel="noopener" data-cat="keji" data-summary="A corporate spat between two tech giants last week was just the latest volley in a conflict over whether dangerous mistakes are being made in A.I. training." data-title="人工智能模型是否被误导为过于人性化？" data-date="09-22 01:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 01:00</span>
          <span class="news-item-title">人工智能模型是否被误导为过于人性化？</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/21/with-tabby-a-former-accountant-is-using-ai-to-make-accountants-obsolete/" target="_blank" rel="noopener" data-cat="keji" data-summary="Tabby旨在作为一个实时簿记界面，处理客户的文书工作，因为它为他们提供有关其业务盈亏的最新数据。" data-title="对于Tabby ，一位前会计师正在使用人工智能来使会计师过时" data-date="09-22 00:38" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-22 00:38</span>
          <span class="news-item-title">对于Tabby ，一位前会计师正在使用人工智能来使会计师过时</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/005/713.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 9 月 22 日消息，宝马集团今日宣布为旗下电动 MINI 品牌推出一款全新特别版车型，定名为“酷不列颠”版。MINI 酷不列颠特别版共推出 4 款车型，售价 20.88-32.08 万元。其中，MINI 酷不列颠收藏版限量 3 台，限时礼遇价 298888 元。该版本最大亮点在于将英国米字旗图案完整喷涂于整车车身，以此展现鲜明的英伦文化特征。据官方介绍，“酷不列颠”（Cool Britannia）源自 20 世纪 90 年代的英国文化浪潮。音乐、艺术、电影与时尚重新诠释传统英国元素，米字旗也由此成为鲜明的流行文化符号。MINI 将它铺展在车身上，既致敬英伦文化，也表达打破常规的个性。该车型车身采用不对称设计，一面完整的米字旗覆盖整个车体表面。喷涂工艺需在全车范围内进行三次喷漆作业" data-title="宝马 MINI 酷不列颠系列车型正式上市：20.88 万元起，手工打磨 74 条分色线" data-date="09-22 14:55" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:55</span>
          <span class="news-item-title">宝马 MINI 酷不列颠系列车型正式上市：20.88 万元起，手工打磨 74 条分色线</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c51kxgj43n89o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚历杭德罗·加纳乔（ Alejandro Garnacho ）从切尔西（ Chelsea ）租借到阿斯顿维拉（ Aston Villa ） ，以开启他的职业生涯，但他在米德兰兹（ Midlands ）的最初几周一直" data-title="加纳乔（ Garnacho ）是否已经处于别墅的十字路口？" data-date="09-22 14:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 14:19</span>
          <span class="news-item-title">加纳乔（ Garnacho ）是否已经处于别墅的十字路口？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/premier-league-mega-product-brighton-arsenal-international-break" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿本赛季的开局令人印象深刻，在一个仍然是一个残酷强大的吸引力的联赛中，为多巴胺崩溃做好准备。而这一个真的是一个真正的秋季暴跌。过去17天（包括周日截止日期）为我们带来了30场英超比赛和79个进球。如果你把马刺队排除在外，这是公平的，因为马刺队现在是后进球，一个与进球甚至足球无关的娱乐概念" data-title="很快回归英超联赛，无休止的超级产品| Barney Ronay" data-date="09-22 04:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-22 04:30</span>
          <span class="news-item-title">很快回归英超联赛，无休止的超级产品| Barney Ronay</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/long-range-hits-goals-galore-inside-premier-league-chaos" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛的端到端足球接管分部，球队正在进一步发展，定位球罢工正在减少。混乱又回来了，端到端的足球又回来了。该部门在更多方面更加开放。数据显示，从上赛季的每场比赛2.75个进球上升到今年迄今为止的2.82个，这是一个小的平均增长–但可以很容易地扩大。每场比赛的进球率至少高出0.21个AC" data-title="各种远程命中和进球：英超联赛重返混乱|安德鲁·比斯利" data-date="09-22 00:45" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-22 00:45</span>
          <span class="news-item-title">各种远程命中和进球：英超联赛重返混乱|安德鲁·比斯利</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqrl6pe56348o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）在周日富勒姆（ Fulham ）的1-1平局中称曼联“缺乏努力”是否正确？" data-title="内维尔指责曼联“缺乏努力”是正确的吗？" data-date="09-21 23:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-21 23:39</span>
          <span class="news-item-title">内维尔指责曼联“缺乏努力”是正确的吗？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/tottenham-hotspur-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="对于Roberto De Zerbi的团队来说，季前赛对欧洲资格的想法已经开始显得令人困惑地乐观在这里注册我们的免费通讯3月，托特纳姆热刺担心可能降级，花费巨资引进Roberto De Zerbi ，他可能永远不会以更强大的手势进行谈判。有明显的改善，他们在赛季的最后一天熬夜。从那时起，马刺花费了净£ 1.75亿（ $ 2.34亿）" data-title="过去两个赛季对马刺来说是严峻的。这和以往一样糟糕|乔纳森·威尔逊" data-date="09-21 23:20" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-21 23:20</span>
          <span class="news-item-title">过去两个赛季对马刺来说是严峻的。这和以往一样糟糕|乔纳森·威尔逊</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/to-minimise-the-risks-to-young-football-players-we-should-ban-agents-recruiting-under-18s" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Phil Murray responds to articles about the precarious path talented young athletes faceJonathan Liew’s piece (Raheem Sterling’s bleak tale a reminder of absurd path young footballers face, 17 September) is informative and timely, particularly when set against Jacob Steinberg’s report (‘They are very similar’: Arsenal’s Dowman reminds Merino of Lami" data-title="为了最大限度地减少年轻足球运动员的风险，我们应该禁止代理商招募" data-date="09-21 23:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-21 23:01</span>
          <span class="news-item-title">为了最大限度地减少年轻足球运动员的风险，我们应该禁止代理商招募</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6e30pz1dkj9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰的布莱恩·布罗比（ Brian Brobbey ）在英超联赛中以失败的一方获得了第一个帽子戏法19年-但还有多少人这样做过？" data-title="一名球员在英超联赛失利中打进帽子戏法的次数是多少？" data-date="09-21 17:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-21 17:05</span>
          <span class="news-item-title">一名球员在英超联赛失利中打进帽子戏法的次数是多少？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦在后面看起来更强壮，年轻人为布莱顿和布伦特福德闪耀，詹姆斯·特拉福德在利兹超级联赛桌上展示了他的英格兰案例|最佳射手在本周， 16岁的马克斯·道曼（ Max Dowman ）被推入聚光灯下，另一位青少年让我们瞥见了布莱顿在击败阿森纳时令人印象深刻的胜利中的未来。Charalampos Kostoulas –在家乡被昵称为“Babis” ，向前阿根廷前锋Gabrie致敬" data-title="英超联赛：周末行动的10个谈话要点" data-date="09-21 15:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-21 15:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/005/712.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，Omdia 英国当地时间今日根据其统计的最新数据表示，中国大陆 PC 出货量在 2026 年第 2 季度达到 1140 万台，同比增长 11%。从形态上来看，尽管笔记本电脑出货在 2026Q2 下滑 2% 至 710 万台，但激增 42% 的台式机出货（430 万台）扭转了整体局面。而如果依用途划分，消费级 PC 出货在 2026Q2 下滑 2%，广义商用 PC 增长 29%。Omdia 同时预测，2026 年全年的中国大陆 PC 出货量将为 3970 万台，下降 6%；其中消费级产品跌幅将达到 10%，狭义商用级下滑 4%，政府及教育类别同比增长 16%。图源：PexelsOmdia 高级分析师 Emma Xu 表示：中国大陆的商用 PC 需求，尤其是来自大" data-title="Omdia：中国大陆 PC 出货 2026Q2 同比增长 11%，预计全年下滑 6%" data-date="09-22 14:55" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:55</span>
          <span class="news-item-title">Omdia：中国大陆 PC 出货 2026Q2 同比增长 11%，预计全年下滑 6%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701426.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网宁德9月22日电 (记者 叶茂)宁德市文化和旅游局21日透露，2026年中秋、国庆期间，宁德市各地将上线精彩纷呈的系列主题活动，重点推荐特色文旅活动53场。" data-title="福建宁德53场重点特色活动“烹”出中秋国庆“文旅大餐”" data-date="09-22 14:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 14:45</span>
          <span class="news-item-title">福建宁德53场重点特色活动“烹”出中秋国庆“文旅大餐”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/689.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，特斯拉的 FSD（监督版）正在欧洲加速落地，又一个国家加入了许可名单。捷克共和国已经正式批准特斯拉 FSD（监督版）系统可在公共道路上使用，中东欧地区的车主终于有机会体验这套功能。这一消息由特斯拉欧洲分部直接在 X 平台对外确认。该区域部门表示，FSD 很快就会在捷克开始推送上线。此次获批之后，捷克成为欧盟第七个允许普通用户使用监督版 FSD 的国家。就在两周之前，斯洛文尼亚刚刚打破欧洲 FSD 审批长达两个月的停滞状态，成为该地区第六个开放这套软件的国家。FSD 在欧洲呈雪球式扩张至此，捷克正式加入持续扩容的欧洲许可阵营，此前获批的国家包括荷兰、立陶宛、爱沙尼亚、丹麦、比利时以及斯洛文尼亚。各国目前是依靠本国豁免审批机制快速放行这套系统。各成员国并没有坐等欧" data-title="特斯拉 FSD 欧洲再下一城，捷克批准其上路使用" data-date="09-22 14:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:42</span>
          <span class="news-item-title">特斯拉 FSD 欧洲再下一城，捷克批准其上路使用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/688.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，国家发展改革委今天举行新闻发布会，据央视新闻报道，新闻发言人表示，当前，我国正在加大“双一流”高校新校区建设，扩大优质本科教育招生规模和研究生培养规模。国家发展改革委新闻发言人李超介绍，按照“十五五”规划《纲要》部署要求，“十五五”期间，我国将有序扩大优质本科教育招生规模和研究生培养规模，支持建设若干“双一流”高校新校区。推动新校区建设融入区域重大战略。国家发展改革委新闻发言人李超：支持北京交通大学、北京科技大学、北京林业大学、中国地质大学（北京）等在京高校向雄安新区疏解、规划建设新校区，是贯彻落实京津冀协同发展战略的重要举措。目前，相关校区建设已进入攻坚阶段，预计将在明年 9 月开门办学。▲ 北京交通大学雄安校区南门、门牌号、爱创湾于 9 月 10 日揭牌同" data-title="多所“双一流”高校新校区预计明年 9 月在雄安新区开学" data-date="09-22 14:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:41</span>
          <span class="news-item-title">多所“双一流”高校新校区预计明年 9 月在雄安新区开学</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701439.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州9月22日电 (记者 程景伟)2026年中国农民丰收节广州市主会场活动21日在花都区炭步镇塱头村启幕。" data-title="2026年中国农民丰收节广州市主会场活动启幕" data-date="09-22 14:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 14:39</span>
          <span class="news-item-title">2026年中国农民丰收节广州市主会场活动启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701381.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月22日电 据“宁武你好”微信公众号消息，9月22日，山西忻州市宁武县委宣传部发布通报称，9月21日，央视新闻报道“山西明长城损毁事件调查”，指出神达朝凯煤业损毁明长城、有关部门长期监管不力等突出问题。宁武县第一时间召开县委常委(扩大)会议，复盘加压推进整改整治工作。有关情况通报如下：" data-title="山西宁武县通报“明长城损毁事件”" data-date="09-22 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 14:08</span>
          <span class="news-item-title">山西宁武县通报“明长城损毁事件”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701401.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月22日电 #8204;据南京江北新区管理委员会网站消息，9月22日，江苏南京江北新区联合调查组发布情况通报称，近期有网民反映，南京信息工程大学附属幼儿园涉食品卫生安全问题。新区立即成立联合调查组，依法开展全面调查。经调取查看该园食堂后厨监控视频，对相关人员进行询问调查等，查明该园食堂后厨卫生管理存在严重问题。同时，调查组对6月30日该园多名幼儿在午餐后出现呕吐症状的后续处置情况，进行了全面回溯和调查。现将查处情况通报如下：" data-title="官方通报南京信息工程大学附属幼儿园食品卫生安全问题查处情况" data-date="09-22 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 13:32</span>
          <span class="news-item-title">官方通报南京信息工程大学附属幼儿园食品卫生安全问题查处情况</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701358.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海南东方9月22日电 (郎作友)9月21日，海南东方CZ8海上风电场最后一台风机精准吊装就位，标志着项目42台风机全部完成海上安装。" data-title="海南东方CZ8海上风电项目完成海上风机安装" data-date="09-22 12:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 12:56</span>
          <span class="news-item-title">海南东方CZ8海上风电项目完成海上风机安装</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701366.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨9月22日电 (王琳 王迎春)“镜泊湖·渤海雪国冬捕季”牡丹江镜泊湖旅游集团2026-2027冬季旅游产品政策推介会于21日在哈尔滨召开。会上透露，当地今冬将创新打造“风雪宁古塔”沉浸式体验场景。" data-title="牡丹江推介冬季旅游：打造“风雪宁古塔”沉浸式体验场景" data-date="09-22 11:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 11:59</span>
          <span class="news-item-title">牡丹江推介冬季旅游：打造“风雪宁古塔”沉浸式体验场景</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701321.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原9月22日电 (记者 胡健)为规范游览秩序、保护文物古迹、保障游览安全，山西省太原市文物保护研究院21日发布公告，晋祠博物馆将在“春节”“五一”“中秋”“国庆”等重要节假日期间严格实行预约限流管理，按景区最大承载量管控客流，基本实现“无预约、不入馆”。" data-title="晋祠博物馆重要节假日实行预约限流 游客可提前10天预约" data-date="09-22 11:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 11:52</span>
          <span class="news-item-title">晋祠博物馆重要节假日实行预约限流 游客可提前10天预约</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493485.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月22日，在2026杭州云栖大会上，阿里巴巴集团CEO吴泳铭发表最新演讲，阐述了对“机器智能”时代的思考。" data-title="阿里吴泳铭最新演讲：未来机器思考的总量将达到人类的1000倍以上" data-date="09-22 10:52" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 10:52</span>
          <span class="news-item-title">阿里吴泳铭最新演讲：未来机器思考的总量将达到人类的1000倍以上</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/998550/a-cut-cable-disrupted-hundreds-of-flights-across-the-us" target="_blank" rel="noopener" data-cat="zonghe" data-summary="周一，在新泽西州的建筑工人意外切断用于空中交通管制的Verizon光纤电缆后，数百个航班被取消或延误。据美国广播公司新闻报道，美国联邦航空局局长布莱恩·贝德福德（ Bryan Bedford ）表示，电路故障导致切断的光纤电缆被发现。停电袭击了整个东北地区的机场，导致[…]" data-title="切断的电缆扰乱了美国各地的数百个航班" data-date="09-22 07:48" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-22 07:48</span>
          <span class="news-item-title">切断的电缆扰乱了美国各地的数百个航班</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/998539/amazon-data-center-water-conservation-colorado-river" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊计划在科罗拉多河沿岸的节水项目上花费2000万$ ，这是美国西部4000万人口的一个重要但不断减少的供水。这一举措出台之际，亚马逊和其他科技公司正面临着对其数据中心用水量的日益严格的审查。亚马逊的目标是成为水[…]" data-title="亚马逊希望帮助科罗拉多河，但我们仍然不知道该公司使用了多少水" data-date="09-22 07:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-22 07:15</span>
          <span class="news-item-title">亚马逊希望帮助科罗拉多河，但我们仍然不知道该公司使用了多少水</span>
        </a>
        <a class="news-item" href="https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="简单的ClickFix攻击只是完全劫持新代理的一种方法。" data-title="Muse ， Meta的超级特权AI助手，有一个严重的0" data-date="09-22 06:24" data-source="Ars Technica">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-arstechnica">🔬 Ars Technica</span>
          <span class="news-item-date">09-22 06:24</span>
          <span class="news-item-title">Muse ， Meta的超级特权AI助手，有一个严重的0</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="由于公众对这些耗能设施的强烈反对，与数据中心行业有关的几家公司推迟了首次公开募股。" data-title="华尔街对数据中心热潮越来越怀疑" data-date="09-22 04:04" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 04:04</span>
          <span class="news-item-title">华尔街对数据中心热潮越来越怀疑</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-22 14:57（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
