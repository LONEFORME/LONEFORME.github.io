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
      <span>2026-10-02 22:00 抓取更新</span>
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
        <span class="channel-count">52</span>
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
        <span class="channel-count">7</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-02/10707323.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 新德里消息：当地时间10月2日凌晨，印度西部马哈拉施特拉邦发生一起交通事故，导致至少7人死亡、19人受伤。" data-title="印度一起交通事故导致至少7人死亡19人受伤" data-date="10-02 21:22" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-02 21:22</span>
      </div>
      <h2 class="hero-featured-title">印度一起交通事故导致至少7人死亡19人受伤</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/amazon-and-synopsys-ink-multi-year-billion-dollar-deal-in-multi-year-ip-agreement-to-accelerate-ai-chip-design-efforts-synopsys-to-adopt-amazon-bedrock-to-deploy-ai-agents-harnessing-aws-compute-and-storage-capabilities" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊和芯片设计工具制造商Synopsys签署了一项价值超过10亿美元的多年合作伙伴关系。作为协议的一部分，亚马逊将许可Synopsys的芯片设计及其设计工具，以创建和优化新的人工智能芯片。Synopsys将采用Amazon Bedrock构建和部署AI代理，并采用AWS计算和存储服务，同时为Amazon硬件优化自己的工具。" data-title="亚马逊和Synopsys签署多年知识产权协议，达成数十亿美元协议，以加快人工智能芯片设计工作" data-date="10-02 21:50" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">亚马逊和Synopsys签署多年知识产权协议，达成数十亿美元协议，以加快人工智能芯片设计工作</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cqn7470513n0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="俱乐部的声明称，该裁决“在法律、原则和事实方面存在明显的重大错误，是不安全的”。" data-title="曼城确认对有罪判决的上诉" data-date="10-02 16:50" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">曼城确认对有罪判决的上诉</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/365.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，Meta 现已公布雷朋 Display 眼镜 2026 年下半年大型更新详情，主要改进导航体验、通知功能、视频通话功能等。在导航方面，Meta 进一步改善了步行时的语音功能。此前系统会直接播报街道名称，例如“在第三街左转”，而在更新后，眼镜会更多结合用户眼前的实际环境进行描述，例如提示“在前方黄色房子处左转”，让语音导航更加自然。同时官方还为导航新增“骑行”和“公共交通”两种模式。在通知功能方面，用户现在能够自由控制眼镜显示的通知，并选择需要关闭的通知类型，从而进一步减少无关信息对使用体验的干扰。此外，Meta 计划在今年晚些时候向美国地区参与 Early Access 计划的用户推送 Hologram 虚拟化身功能，首批支持 WhatsApp 视频通话。用户" data-title="Meta 预热雷朋 Display 眼镜 2026 年下半年大型更新：改进导航功能、支持控制通知推送、Hologram 虚拟化身..." data-date="10-02 22:01" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">Meta 预热雷朋 Display 眼镜 2026 年下半年大型更新：改进导航功能、支持控制通知推送、Hologram 虚拟化身...</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707323.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 新德里消息：当地时间10月2日凌晨，印度西部马哈拉施特拉邦发生一起交通事故，导致至少7人死亡、19人受伤。" data-title="印度一起交通事故导致至少7人死亡19人受伤" data-date="10-02 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 21:22</span>
          <span class="news-item-title">印度一起交通事故导致至少7人死亡19人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707297.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社阿斯塔纳10月2日电 比什凯克消息：吉尔吉斯斯坦总统府网站2日发布消息称，该国首颗卫星于当地时间1日在美国发射升空并成功入轨，将用于自然资源监测和灾害预警等领域。" data-title="吉尔吉斯斯坦首颗卫星成功入轨" data-date="10-02 20:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:50</span>
          <span class="news-item-title">吉尔吉斯斯坦首颗卫星成功入轨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707296.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 据朝中社2日报道，朝鲜劳动党中央委员会部长金与正当天就日前发生在朝韩非军事区的地雷爆炸事件发表谈话，谴责韩方企图把朝鲜半岛局势再次拖入危险境地。" data-title="金与正谴责韩方企图把朝鲜半岛局势再次拖入危险境地" data-date="10-02 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:49</span>
          <span class="news-item-title">金与正谴责韩方企图把朝鲜半岛局势再次拖入危险境地</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707299.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【东盟专线】第169次中老缅泰湄公河联合巡逻执法行动结束" data-title="第169次中老缅泰湄公河联合巡逻执法行动结束" data-date="10-02 20:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:39</span>
          <span class="news-item-title">第169次中老缅泰湄公河联合巡逻执法行动结束</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707292.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 据公安部交通管理局微信公众号消息，国庆假期第二天，全国公路交通流量较昨天有所下降，除京津冀、长三角、珠三角、成渝等地大城市周边出入城方向部分路段有局部车多缓行情况外，主干公路通行总体有序。各地公安交管部门结合道路交通流量、交通违法的规律特点，加强交通安全态势分析评估，加大警力投入和巡查频次，严查严处“三超一疲劳”、酒驾醉驾等肇事突出交通违法，广泛开展安全宣传警示，全力维护群众假期出行安全。" data-title="国庆假期第二天全国道路交通总体平稳有序 公安部交管局发布道路出行安全提示" data-date="10-02 20:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:22</span>
          <span class="news-item-title">国庆假期第二天全国道路交通总体平稳有序 公安部交管局发布道路出行安全提示</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707280.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2日，据相关消息，阿联酋总统顾问安瓦尔·加尔贾什当天表示，迪拜航空公司客机驾驶舱冲突事件是一起“恐袭行为”。" data-title="阿联酋总统顾问称迪拜航空驾驶舱冲突系“恐袭”" data-date="10-02 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 19:35</span>
          <span class="news-item-title">阿联酋总统顾问称迪拜航空驾驶舱冲突系“恐袭”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707246.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 据朝中社10月2日报道，朝鲜劳动党中央委员会部长金与正当天发表谈话，就日前发生在朝韩非军事区的地雷爆炸事件，谴责韩方企图把朝鲜半岛局势再次拖入危险境地。" data-title="金与正：韩方企图把朝鲜半岛局势再次拖入危险境地" data-date="10-02 19:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 19:17</span>
          <span class="news-item-title">金与正：韩方企图把朝鲜半岛局势再次拖入危险境地</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707248.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月2日，中方53108艇顺利返航，安全靠泊云南西双版纳景哈警务码头，标志着为期12天的第169次中老缅泰湄公河联合巡逻执法行动圆满结束。" data-title="第169次中老缅泰湄公河联合巡逻执法行动圆满结束" data-date="10-02 18:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 18:52</span>
          <span class="news-item-title">第169次中老缅泰湄公河联合巡逻执法行动圆满结束</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707238.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 伊斯兰堡消息：当地时间10月2日，巴基斯坦安全部队在该国开伯尔-普什图省(KP)北瓦济里斯坦地区展开的一次反恐行动中，共击毙7名恐怖分子。" data-title="巴基斯坦安全部队在反恐行动中击毙7名恐怖分子" data-date="10-02 18:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 18:50</span>
          <span class="news-item-title">巴基斯坦安全部队在反恐行动中击毙7名恐怖分子</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707244.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 韩国检察制度10月2日迎来重大改革。据韩联社报道，韩国公诉厅和重大犯罪调查厅10月2日正式成立，取代10月1日结束最后一个工作日的韩国检察厅。1948年成立、运行了78年的韩国检察厅正式退出历史舞台。" data-title="韩国检察制度迎重大改革 检察厅退出历史舞台" data-date="10-02 18:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 18:35</span>
          <span class="news-item-title">韩国检察制度迎重大改革 检察厅退出历史舞台</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707242.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 综合外媒10月1日报道，挪威球员哈兰德正起诉挪威航空，指控后者非法使用其肖像。航空公司方面回应称，难以理解此项诉讼，并表示“遗憾”。" data-title="哈兰德起诉挪威航空" data-date="10-02 18:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 18:26</span>
          <span class="news-item-title">哈兰德起诉挪威航空</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707228.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网福州10月2日电 (郑江洛)近期，“八闽楷模”福建省科技特派员群体先进事迹发布仪式在福州举行。多年来，福建科技特派员走出实验室、扎根田野乡间，把论文写在八闽大地上，将科研技术成果持续转化为富民兴农实效。" data-title="山海作田垄，八闽有群人" data-date="10-02 18:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 18:09</span>
          <span class="news-item-title">山海作田垄，八闽有群人</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/02/podcasts/voters-abandoning-trump-new-cancer-treatments.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="此外，还有周五的新闻测验。" data-title="选民放弃特朗普的地方，以及新癌症治疗的障碍" data-date="10-02 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-02 18:00</span>
          <span class="news-item-title">选民放弃特朗普的地方，以及新癌症治疗的障碍</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707200.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社南京10月2日电 题：台青文旅博主李天启：行走中品味大陆" data-title="台青文旅博主李天启：行走中品味大陆" data-date="10-02 17:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 17:53</span>
          <span class="news-item-title">台青文旅博主李天启：行走中品味大陆</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c61585j4vlkgo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="迪拜航空这班飞往特拉维夫的航班上，斯米特·马查尔机长（Capt Smit Machchhar）遭另一名机师袭击。以色列总理内塔尼亚胡赞扬他是“真正的英雄”，“拯救了174人的生命”，并阻止了一场“灾难性的空中事故”。" data-title="“救了174人的生命”：迪拜航空劫机案，遭刺伤的印度机师是谁？" data-date="10-02 16:24" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-02 16:24</span>
          <span class="news-item-title">“救了174人的生命”：迪拜航空劫机案，遭刺伤的印度机师是谁？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/amazon-and-synopsys-ink-multi-year-billion-dollar-deal-in-multi-year-ip-agreement-to-accelerate-ai-chip-design-efforts-synopsys-to-adopt-amazon-bedrock-to-deploy-ai-agents-harnessing-aws-compute-and-storage-capabilities" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊和芯片设计工具制造商Synopsys签署了一项价值超过10亿美元的多年合作伙伴关系。作为协议的一部分，亚马逊将许可Synopsys的芯片设计及其设计工具，以创建和优化新的人工智能芯片。Synopsys将采用Amazon Bedrock构建和部署AI代理，并采用AWS计算和存储服务，同时为Amazon硬件优化自己的工具。" data-title="亚马逊和Synopsys签署多年知识产权协议，达成数十亿美元协议，以加快人工智能芯片设计工作" data-date="10-02 21:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 21:50</span>
          <span class="news-item-title">亚马逊和Synopsys签署多年知识产权协议，达成数十亿美元协议，以加快人工智能芯片设计工作</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/364.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，极氪汽车今日宣布，焕新极氪 007GT 色彩上新，带来全新外饰色河谷绿、全新内饰色墨绿。2026 年 10 月 1 日-10 月 31 日，下定焕新极氪 007GT 可享更多限时权益。IT之家注意到，焕新极氪 007/007GT 于今年 4 月正式上市，定价 20.39 万元起，限时 19.39 万元起。系列车型标配 19 英寸轮毂，其中焕新极氪 007 前脸新增动感通风口造型，并提供碳纤维套件选装服务，强化运动属性。两款车型搭载算力更强的 NVIDIA DRIVE Thor-U 智驾芯片，智能化水平显著提升。规格方面，焕新极氪 007 长宽高为 4858（4880）x 1900 x 1450mm，轴距 2925mm。而 007GT 车身尺寸微调至 4858（" data-title="焕新极氪 007GT 色彩上新：推出“河谷绿”车色、“墨绿”内饰" data-date="10-02 21:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 21:43</span>
          <span class="news-item-title">焕新极氪 007GT 色彩上新：推出“河谷绿”车色、“墨绿”内饰</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/363.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，Meta 宣布旗下 AI 智能体 Muse 将于近期登陆智能眼镜，用户无需拿出手机，只需通过语音下达指令，Muse 就能在后台代用户完成一系列任务。Meta 表示，Muse 基于 Muse Spark AI 模型运行，其核心运行环境是一台部署在云端的私有持久化 Linux 虚拟机，配备独立的网页浏览器、文件系统和终端。即使用户关闭应用，这些组件仍会持续运行。为了完成用户交代的任务，Muse 可以自行决定编写并运行代码，也可以将工作分配给多个子智能体，还能创建定时任务。此外，Muse 还能够生成文档、PDF、网站以及消费记录追踪器、数据仪表盘等交互式工具。与主要面向开发者和专业用户的其他 AI 智能体相比，Muse 的定位更加偏向普通消费者。其界面采用类似即时通" data-title="Meta 旗下 AI 智能体 Muse 将登陆智能眼镜平台，可代用户完成各种任务" data-date="10-02 21:38" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 21:38</span>
          <span class="news-item-title">Meta 旗下 AI 智能体 Muse 将登陆智能眼镜平台，可代用户完成各种任务</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/359.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，英伟达今天正式对外披露 DGX Spark 产品更新，推出 64GB 内存版本 DGX Spark 桌面 AI 计算机，起售价 4,999 美元（现汇率约合 33,566 元人民币），将于 10 月 23 日正式发售，宏碁、戴尔、华硕、技嘉、微星、H3C 等众多 OEM 厂商均会推出基于该平台的整机产品。官方此前推出的 128GB 版本同步更新定价，128GB FE 版本售价 6,950 美元（IT之家注：现汇率约合 46,666 元人民币）。硬件层面，DGX Spark 基于 GB10 Grace‑Blackwell 超算芯片，依靠统一内存架构打通 CPU 与 GPU 内存空间，本次新增 64GB 内存版本，整机总内存 64GB，系统预留约 8GB 内存，可" data-title="桌面 AI 超算新选择：英伟达 NVIDIA DGX Spark 64GB 内存版正式发布，4999 美元" data-date="10-02 21:00" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 21:00</span>
          <span class="news-item-title">桌面 AI 超算新选择：英伟达 NVIDIA DGX Spark 64GB 内存版正式发布，4999 美元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/openais-jalapeno-asics-are-deployed-alongside-amd-epyc-turin-cpus-as-hosts-hardware-vp-says-nvidias-vera-standalone-is-a-little-bit-behind-on-that-maturity-level" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI选择将其Jalapeño ASIC的机架规模部署与AMD EPYC Turin CPU配对，而不是像Arm的AGI或Nvidia的Vera这样的高性能代理芯片浪潮。" data-title="OpenAI的Jalapeño ASIC与AMD EPYC “Turin” CPU一起部署为主机，而不是英伟达的Vera" data-date="10-02 20:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 20:40</span>
          <span class="news-item-title">OpenAI的Jalapeño ASIC与AMD EPYC “Turin” CPU一起部署为主机，而不是英伟达的Vera</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1002963/ai-hallucinations-customer-service-jobs-agents" target="_blank" rel="noopener" data-cat="keji" data-summary="Madison是纽约市的一家服务员，他向每张桌子打招呼，询问每个餐厅的过敏情况。最近，有一些亲密的电话。“有时人们会告诉我他们对贝类过敏，我会回来的，他们不会问我任何问题，”麦迪逊说，她要求将她的姓氏隐瞒给[…]" data-title="人工智能幻觉使有资格的客户变得更糟" data-date="10-02 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 20:00</span>
          <span class="news-item-title">人工智能幻觉使有资格的客户变得更糟</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1003681/microsoft-data-centers-ai-environment-biomimicry" target="_blank" rel="noopener" data-cat="keji" data-summary="圣安东尼奥市议会议员里克·加尔文（ Ric Galvan ）记得2000年代数据中心首次进入他的城市时，看起来像相对不起眼的办公楼。但近年来情况发生了变化，数据中心已经发展成为跨越数百万平方英尺的大型“超大规模”设施，并容纳了人工智能的物理基础设施。现在有更多[…]" data-title="如果数据中心被伪装在树林里，有人会讨厌它吗？" data-date="10-02 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 20:00</span>
          <span class="news-item-title">如果数据中心被伪装在树林里，有人会讨厌它吗？</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1003929/amazon-ai-data-center-blog-warning" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊呼吁人们支持人工智能数据中心项目，否则将对美国经济和国家安全造成无法弥补的伤害。在今天发布的一篇3000多字的博客中，亚马逊网络服务首席执行官马特·加曼（ Matt Garman ）反驳了公众对数据中心可能对就业、电力需求和[…]产生影响的担忧。" data-title="亚马逊撰写可怕的博客，警告社区不要封锁数据中心" data-date="10-02 19:52" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 19:52</span>
          <span class="news-item-title">亚马逊撰写可怕的博客，警告社区不要封锁数据中心</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/micron-now-has-an-88-percent-margin-on-consumer-memory-price-hikes-drive-revenue-client-business-is-microns-only-unit-that-shipped-less-memory-this-quarter" target="_blank" rel="noopener" data-cat="keji" data-summary="根据该公司2026年第四季度财务报告，美光的消费者业务利润率最高，尽管该季度的内存较少。" data-title="由于价格上涨推动利润增长，美光现在在消费者记忆上有88%的利润率" data-date="10-02 19:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 19:40</span>
          <span class="news-item-title">由于价格上涨推动利润增长，美光现在在消费者记忆上有88%的利润率</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/micro-center-requires-photo-id-and-signed-no-export-pledge-to-buy-rtx-5090-gaming-gpu-buyer-forced-to-sign-declaration-disclosing-install-location-and-promise-gpu-will-remain-in-the-us" target="_blank" rel="noopener" data-cat="keji" data-summary="该表格要求RTX 5090买家在获得批准进行购买之前输入他们的个人数据。但是，目前尚不清楚Micro Center如何使用这些信息来跟踪非法出口的GPU。" data-title="Micro Center要求购买RTX 5090游戏GPU需要带照片的身份证和签署的无出口承诺" data-date="10-02 19:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 19:15</span>
          <span class="news-item-title">Micro Center要求购买RTX 5090游戏GPU需要带照片的身份证和签署的无出口承诺</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/02/business/ai-stocks-bonds-economy.html" target="_blank" rel="noopener" data-cat="keji" data-summary="我们的专栏作家说，人工智能的繁荣推高了股市，即使利率已经拉低了它。" data-title="支撑股票和经济的强大而脆弱的力量" data-date="10-02 17:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-02 17:03</span>
          <span class="news-item-title">支撑股票和经济的强大而脆弱的力量</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/500098.html" target="_blank" rel="noopener" data-cat="keji" data-summary="让每一次请求选对模型，让每一次反馈都成为下一次更优、更省的选择" data-title="openJiuwen X-Router自演进模型路由技术首发，升腾亲和，Agent越跑越省，实测减少50+%Token消耗" data-date="10-02 15:34" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-02 15:34</span>
          <span class="news-item-title">openJiuwen X-Router自演进模型路由技术首发，升腾亲和，Agent越跑越省，实测减少50+%Token消耗</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/306.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，《战争机器：事变日（Gears of War：E-Day）》开发商 The Coalition 现已公布游戏发售宣传片，本作将于北京时间 10 月 7 日正式发售，登陆 XBOX Series X|S 与 PC 平台（包括 Steam 与 Microsoft Store），首发加入 XBOX Game Pass。游戏在 PC 平台首发支持英伟达 DLSS 4.5 技术以及硬件光线追踪功能。价格方面，本作标准版 298 元，预购高级版（428 元）的玩家可提前最多 5 天抢先体验，并可在游戏发售时解锁“Exfil Dom”角色皮肤与“Exfil”武器皮肤套装。IT之家附游戏商品页（https://store.steampowered.com/app/301085" data-title="《战争机器：事变日》游戏发售宣传片公开：首发支持 DLSS 4.5 及光追，10 月 7 日正式发售" data-date="10-02 15:33" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:33</span>
          <span class="news-item-title">《战争机器：事变日》游戏发售宣传片公开：首发支持 DLSS 4.5 及光追，10 月 7 日正式发售</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/304.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，OpenAI 宣布进一步升级 ChatGPT 的购物功能，新增虚拟试穿和 Favorites（收藏）两项功能，用户现在可以上传自己的照片，让 ChatGPT 生成穿着特定服饰或配饰后的效果图，同时也可以将感兴趣的商品保存下来，方便之后继续查看。IT之家注意到，去年 OpenAI 曾为 ChatGPT 推出专门的 Shopping Research 购物研究功能，主要面向较为复杂的购物需求。其不仅仅局限于“简单提供商品链接”，用户可以通过自然语言告知 ChatGPT 自己预算和需求，之后 ChatGPT 便会在全网搜索相关商品，并根据不同产品的优缺点生成个性化购买指南，同时提供购买链接。而如今，OpenAI 为 ChatGPT 新增的虚拟试穿功能将以“Try o" data-title="OpenAI 升级 ChatGPT 购物体验，新增 AI 衣服虚拟试穿体验" data-date="10-02 15:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:28</span>
          <span class="news-item-title">OpenAI 升级 ChatGPT 购物体验，新增 AI 衣服虚拟试穿体验</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/499991.html" target="_blank" rel="noopener" data-cat="keji" data-summary="44年前被亲自列入问题清单" data-title="丘成桐新论文致谢了GPT和Claude" data-date="10-02 15:27" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-02 15:27</span>
          <span class="news-item-title">丘成桐新论文致谢了GPT和Claude</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqn7470513n0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="俱乐部的声明称，该裁决“在法律、原则和事实方面存在明显的重大错误，是不安全的”。" data-title="曼城确认对有罪判决的上诉" data-date="10-02 16:50" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-02 16:50</span>
          <span class="news-item-title">曼城确认对有罪判决的上诉</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/politics/2026/oct/01/success-manchester-city-helped-put-andy-burnham-in-power" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="PM称赞阿布扎比集团是重塑曼彻斯特的“巨大合作伙伴” ，但批评人士表示，这忽视了城市转型的公共成本。2016年7月，曼城球员YayaTouré漫步在北京工人体育场附近的一个小酒吧里，当数十名中国球迷冲向他时，他露出了困惑的微笑。曼城刚刚在Sheikh Mansour的阿布扎比联合集团和" data-title="曼城的成功如何帮助Andy Burnham掌权" data-date="10-02 02:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:53</span>
          <span class="news-item-title">曼城的成功如何帮助Andy Burnham掌权</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/fears-manchester-city-whistleblower-rui-pinto-loses-protected-witness-status" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一名男子的私人文件泄露促使对城市的调查被建议不要回家，联系家人或访问拥挤的地方。Rui Pinto在2015年国际足联丑闻引发的十字军东征中建立了Football Leaks网站十多年后，他发现自己正处于日益严重的风暴之中。这位前历史系学生有着标志性的尖刺头发，曾经赚取额外的现金出售有关第二次世界大战的书籍" data-title="犯罪分子还是救世主？ Rui Pinto在曼城泄密后被葡萄牙当局遗弃" data-date="10-02 02:40" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:40</span>
          <span class="news-item-title">犯罪分子还是救世主？ Rui Pinto在曼城泄密后被葡萄牙当局遗弃</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjkg7g93y5yno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="负责监督HMRC的财政委员会已敦促该机构仔细审查曼城判决的税务影响。" data-title="HMRC敦促审查曼城案件的税务影响" data-date="10-02 02:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-02 02:21</span>
          <span class="news-item-title">HMRC敦促审查曼城案件的税务影响</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/fears-manchester-city-whistleblower-rui-pinto-loses-protected-witness-status" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Pinto的私人文件泄露引发了对曼城的调查，据了解，他担心自己的安全。Rui Pinto在2015年国际足联丑闻引发的十字军东征中建立了Football Leaks网站十多年后，他发现自己正处于日益严重的风暴之中。这位前历史系学生曾经是商标，头发尖刺，曾经赚取额外的现金出售有关第二次世界大战的书籍，他的统计数据并没有阻止他" data-title="城市举报人Rui Pinto失去受保护证人身份后的恐惧" data-date="10-02 02:20" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:20</span>
          <span class="news-item-title">城市举报人Rui Pinto失去受保护证人身份后的恐惧</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/andy-burnhams-manchester-city-comments-stir-fresh-tensions-with-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据说政府对缺乏警告感到不满财政委员会主席希望HMRC参与城市案件安迪·伯纳姆（ Andy Burnham ）在曼城辩论中的干预重新引发了英超联赛与首相之间的紧张关系。据了解，政府官员感到不满的是，他们没有得到通知，独立委员会对9亿英镑金融操纵和“虚假合同”的诅咒判决将于本周公布，" data-title="安迪·伯纳姆（ Andy Burnham ）的曼城评论引发了英超联赛的新紧张局势" data-date="10-02 02:10" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:10</span>
          <span class="news-item-title">安迪·伯纳姆（ Andy Burnham ）的曼城评论引发了英超联赛的新紧张局势</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/manchester-city-premier-league-financial-rule-breaches-fans-anger-owners" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿布扎比政权下取得的成功让支持者感到自豪，但他们只能在新监护人的领导下真正恢复这些感受。在写作和谈到曼城被判犯有严重违反英超联赛规则的数十万字中，罗伯托·曼奇尼（ Roberto Mancini ）在宣布“不关我的事”时可能是最尖锐的。为什么会这样？他从其中一份“虚假合同”中赚了数百万美元，并享受了他的" data-title="曼城球迷感到愤怒是正确的–现在他们需要直接向老板| Will Unwin" data-date="10-01 22:04" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 22:04</span>
          <span class="news-item-title">曼城球迷感到愤怒是正确的–现在他们需要直接向老板| Will Unwin</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/365.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，Meta 现已公布雷朋 Display 眼镜 2026 年下半年大型更新详情，主要改进导航体验、通知功能、视频通话功能等。在导航方面，Meta 进一步改善了步行时的语音功能。此前系统会直接播报街道名称，例如“在第三街左转”，而在更新后，眼镜会更多结合用户眼前的实际环境进行描述，例如提示“在前方黄色房子处左转”，让语音导航更加自然。同时官方还为导航新增“骑行”和“公共交通”两种模式。在通知功能方面，用户现在能够自由控制眼镜显示的通知，并选择需要关闭的通知类型，从而进一步减少无关信息对使用体验的干扰。此外，Meta 计划在今年晚些时候向美国地区参与 Early Access 计划的用户推送 Hologram 虚拟化身功能，首批支持 WhatsApp 视频通话。用户" data-title="Meta 预热雷朋 Display 眼镜 2026 年下半年大型更新：改进导航功能、支持控制通知推送、Hologram 虚拟化身..." data-date="10-02 22:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 22:01</span>
          <span class="news-item-title">Meta 预热雷朋 Display 眼镜 2026 年下半年大型更新：改进导航功能、支持控制通知推送、Hologram 虚拟化身...</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1004016/paramount-warner-bros-skydance-megamerger-name" target="_blank" rel="noopener" data-cat="zonghe" data-summary="派拉蒙Skydance首席执行官大卫·埃里森（ David Ellison ）宣布，当该公司下周完成与华纳兄弟发现公司（ Warner Bros. Discovery ）的1100亿美元合并时，该公司将被称为Skydance。Ellison在X上的一篇文章中写道： “我们想要一个名字，让合并后的公司拥有自己的身份，同时允许派拉蒙和[…]" data-title="派拉蒙的华纳兄弟巨型合并将被称为Skydance" data-date="10-02 21:42" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 21:42</span>
          <span class="news-item-title">派拉蒙的华纳兄弟巨型合并将被称为Skydance</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/02/nyregion/cornell-investigation-prosecution-challenges.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="性侵犯案件的专家表示，对于Jane Doe对兄弟会成员提出的强奸指控，要赢得定罪可能并不容易。" data-title="为什么检察官在康奈尔大学的调查中可能面临法律障碍" data-date="10-02 21:41" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-02 21:41</span>
          <span class="news-item-title">为什么检察官在康奈尔大学的调查中可能面临法律障碍</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/flock-drones-with-cameras-deployed-as-first-responders-in-some-us-cities-amid-privacy-concerns-uavs-connect-to-wider-emergency-services-system-and-streams-video-to-dispatchers-officers" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国城市考虑部署可自动响应紧急呼叫的Flock无人机。然而，由于隐私和其他问题，其他司法管辖区正在抵制这项服务。" data-title="由于隐私问题，在美国一些城市部署了配备摄像头的无人机，作为急救人员" data-date="10-02 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 21:20</span>
          <span class="news-item-title">由于隐私问题，在美国一些城市部署了配备摄像头的无人机，作为急救人员</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/362.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，B 站 App 宣布上架鸿蒙手表端应用市场，用户在华为 WATCH 系列手表上就能看视频、刷弹幕、听播客。官方表示，用户只需前往应用市场，即可下载安装哔哩哔哩手表端，相应 App 提供收藏、倍速、循环播放、下载缓存等各种特性，适合早高峰地铁、夜跑、做饭、洗碗、排队、等人等各种场景，精彩内容抬腕即达。" data-title="B 站 App 上架鸿蒙手表端应用市场：用户可在华为 WATCH 系列手表上自由看视频、刷弹幕" data-date="10-02 21:18" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 21:18</span>
          <span class="news-item-title">B 站 App 上架鸿蒙手表端应用市场：用户可在华为 WATCH 系列手表上自由看视频、刷弹幕</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1003936/home-assistant-says-big-tech-ruined-the-cloud-so-were-out" target="_blank" rel="noopener" data-cat="zonghe" data-summary="开源智能家居平台Home Assistant正在将云计算踢到路边--至少名义上是这样。“我们将Home Assistant Cloud更名为Home Assistant Link ，因为我们讨厌云，”创始人Paulus Schoutsen在今天宣布之前接受采访时告诉The Verge。“大科技毁了云，所以我们出局了。“这[…]" data-title="Home Assistant说： “大科技毁了云，所以我们出局了”" data-date="10-02 21:02" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 21:02</span>
          <span class="news-item-title">Home Assistant说： “大科技毁了云，所以我们出局了”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-introduces-64gb-dgx-spark-to-throw-local-ai-fans-a-lifeline-amid-the-rampocalypse-new-gb10-config-starts-at-usd4999-for-those-who-can-work-with-less" target="_blank" rel="noopener" data-cat="zonghe" data-summary="英伟达正在推出64GB版本的DGX Spark本地AI工作站，该工作站专为新一代高度智能且紧凑的本地模型量身定制。起价为4999 $ ，更实惠的配置与原来的128GB Spark及其GB10兄弟相同。" data-title="英伟达推出64GB DGX Spark ，在RAMpocalypse中为本地AI粉丝提供生命线" data-date="10-02 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 21:00</span>
          <span class="news-item-title">英伟达推出64GB DGX Spark ，在RAMpocalypse中为本地AI粉丝提供生命线</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/993521/ayaneo-konkr-pocket-advance-nintendo-game-boy-advance-handheld" target="_blank" rel="noopener" data-cat="zonghe" data-summary="虽然我把最初的Game Boy视为我最初的技术痴迷之一，但我仍然认为任天堂的Game Boy Advance是我有史以来最喜欢的游戏机，这要归功于它更舒适的水平设计（适合我的大手）和它广泛的优秀32位和16位游戏目录。Ayaneo并不是第一家[…]" data-title="Pocket Advance几乎完美了我最喜欢的任天堂手持设备" data-date="10-02 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 21:00</span>
          <span class="news-item-title">Pocket Advance几乎完美了我最喜欢的任天堂手持设备</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707321.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南京10月2日电 (张传明 唐娟)国庆假期首日，南京“热”力全开。途牛平台数据显示，南京成为国庆假期首日境内游热门目的地；去哪儿旅行数据显示，南京是国庆假期首日酒店入住热门城市。热度背后，是这座历史文化名城以文博、夜游、演艺、乡村、商业等多元场景，为游客奉上充满文化气息的文旅“盛宴”。" data-title="国庆假期首日 古都南京“热”力全开" data-date="10-02 20:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:52</span>
          <span class="news-item-title">国庆假期首日 古都南京“热”力全开</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/358.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，HKC 旗下“神盾 25Q360B”24.5 英寸电竞显示器现已在京东发售，定价为 2221 元，部分地区国补后低至 1999 元。京东 HKC 神盾 25Q360B 显示器 2221 元直达链接该机搭载一块 2560×1440 分辨率 1152 分区 QD-Mini LED 背光 360Hz 刷新率 Fast IPS 面板，GtG 响应速度 1ms，拥有 1400nit HDR 峰值亮度，对比度达到 300000:1。覆盖 98.5% DCI-P3、98.5% Adobe RGB、100% sRGB，出厂逐台校色达到 ΔE≤2 专业级色准。它搭载 HKC 自研 DIC 2.0 动态模糊消除技术，通过 MiniLED 精密分区控光技术结合同步插黑帧技术，三档可" data-title="HKC“神盾 25Q360B”24.5 英寸显示器发售：2K 360Hz QD-Mini LED，2221 元（国补后 1999 元）" data-date="10-02 20:51" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 20:51</span>
          <span class="news-item-title">HKC“神盾 25Q360B”24.5 英寸显示器发售：2K 360Hz QD-Mini LED，2221 元（国补后 1999 元）</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/357.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，9 月 30 日，上海市委网信办组织召开未成年人网络保护专题指导会，聚焦压实网站平台主体责任，深入推进未成年人网络保护专项行动，重点加强心理健康工作，全方位守护未成年人上网环境。属地哔哩哔哩、小红书、拼多多、喜马拉雅、SOUL、阅文集团、米哈游等 17 家重点平台参会。IT之家注意到，会议通报了专项行动期间涉未成年人违法违规和不良信息典型案例，重点部署进一步加强未成年人心理健康工作，督促平台严格落实主体责任，重点防范化解七类涉未成年人心理健康风险。一是网络沉迷成瘾风险，避免造成未成年人作息失调、注意力下降、厌学逃避等问题；二是网络欺凌风险，防范其造成未成年人长期心理创伤；三是容貌身材焦虑扩散风险，警惕由此滋生未成年人自卑心理等；四是自残自杀类消极有害信息传播风" data-title="上海市委网信办：督促平台重点防范化解七类涉未成年人心理健康风险，哔哩哔哩、小红书、拼多多等参会" data-date="10-02 20:49" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 20:49</span>
          <span class="news-item-title">上海市委网信办：督促平台重点防范化解七类涉未成年人心理健康风险，哔哩哔哩、小红书、拼多多等参会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707298.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社广州10月2日电 (记者 王坚)在冷空气影响下，广东广州、深圳、江门、肇庆等地2日遭遇强降雨。当日白天，全省有71个镇街出现暴雨、大暴雨，全省最大降雨量达125毫米。" data-title="广东超70个镇街遭遇暴雨  全省最大降雨量达125毫米" data-date="10-02 20:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:36</span>
          <span class="news-item-title">广东超70个镇街遭遇暴雨  全省最大降雨量达125毫米</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/networking/routers/grab-an-usd80-discount-on-this-tp-link-wi-fi-7-router-with-five-2-5g-ethernet-ports-limited-time-deal-on-the-archer-be550-nets-a-tri-band-router-with-fast-speeds-to-upgrade-your-home-network" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TP-Link Archer BE550 Wi-Fi 7路由器仅限时销售，价格低至$ 169.99 ，配备6根天线和5个2.5G以太网端口，功能强大。" data-title="这款配备五个2.5G以太网端口的TP-Link Wi-Fi 7路由器可享受$ 80折扣，现价$ 169.99" data-date="10-02 20:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 20:20</span>
          <span class="news-item-title">这款配备五个2.5G以太网端口的TP-Link Wi-Fi 7路由器可享受$ 80折扣，现价$ 169.99</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707263.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南通10月2日电(记者 谷华)2日，据江苏南通市公安局交管支队消息，国庆假期首日，苏通长江公路大桥(以下简称：苏通大桥)全天总流量达16.59万辆，创下大桥开通以来单日流量历史新高。" data-title="苏通大桥国庆假期首日流量达16.59万辆 创开通以来单日流量新高" data-date="10-02 20:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 20:04</span>
          <span class="news-item-title">苏通大桥国庆假期首日流量达16.59万辆 创开通以来单日流量新高</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/save-usd50-on-elgatos-biggest-stream-deck-this-32-key-monster-macro-pad-is-now-down-to-usd199" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Elgato的Stream Deck在亚马逊享受20%的折扣。只需$ 199即可购买Stream Deck XL。" data-title="购买Elgato最大的Stream Deck ，立省$ 50" data-date="10-02 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-02 20:00</span>
          <span class="news-item-title">购买Elgato最大的Stream Deck ，立省$ 50</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-02 22:00（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
