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
      <span>2026-10-13 00:53 抓取更新</span>
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
        <span class="channel-count">53</span>
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
  <div class="ov-item"><span class="ov-num">53</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-13/10712347.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社阿布贾10月12日电(记者洪泽华)尼日利亚军方12日发表声明说，军方10日在该国东北部博尔诺州实施空袭，打死40余名“疑似恐怖分子”和一名极端组织“伊斯兰国西非省”的高级指挥官。" data-title="尼日利亚军方称打死40余名“疑似恐怖分子”" data-date="10-13 00:41" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-13 00:41</span>
      </div>
      <h2 class="hero-featured-title">尼日利亚军方称打死40余名“疑似恐怖分子”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/jev-like-decision-models-are-flooding-the-ai-market-after-researcher-claims-typesafe-copied-their-research-microsoft-openai-among-companies-releasing-lightweight-system-one-ai-models" target="_blank" rel="noopener" data-cat="keji" data-summary="Jev和大量人工智能决策模型—据称TypeSafe复制了研究人员的架构，但自己也被复制了" data-title="Jev-like decision models are flooding the AI market, after researcher claims TypeSafe copied their research" data-date="10-13 00:00" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">Jev-like decision models are flooding the AI market, after researcher claims TypeSafe copied their research</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/12/man-citys-crisis-pushes-the-limits-of-language" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="不仅仅是俱乐部最近的收费本身是前所未有的，它也是用来描述它们的语言在这里注册我们的免费通讯足球语言是一种精美且高度细致入微的方言。大多数参与者" data-title="Winning is not enough for Manchester City to move on from this crisis | Jonathan Wilson" data-date="10-12 22:24" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Winning is not enough for Manchester City to move on from this crisis | Jonathan Wilson</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1009604/elon-musk-2026-midterm-republican-donations" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据《纽约时报》报道，埃隆·马斯克（ Elon Musk ）自7月以来已向共和党团体发放了至少2.76亿美元，使他成为该党最大的知名捐助者和最大的中期捐助者。其中1.58亿美元-最大的政治捐款人之一" data-title="Elon Musk has donated over $276 million to Republican midterm efforts" data-date="10-13 00:52" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Elon Musk has donated over $276 million to Republican midterm efforts</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-13/10712347.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社阿布贾10月12日电(记者洪泽华)尼日利亚军方12日发表声明说，军方10日在该国东北部博尔诺州实施空袭，打死40余名“疑似恐怖分子”和一名极端组织“伊斯兰国西非省”的高级指挥官。" data-title="尼日利亚军方称打死40余名“疑似恐怖分子”" data-date="10-13 00:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-13 00:41</span>
          <span class="news-item-title">尼日利亚军方称打死40余名“疑似恐怖分子”</span>
          <span class="news-value-point">💡 新华社阿布贾10月12日电(记者洪泽华)尼日利亚军方12日发表声明说，军方10日在该国东北部博尔诺州实施空袭，打死40余名“疑似恐怖分子”和一名…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/12/world/europe/russia-diesel-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统正着手购买俄罗斯柴油，同时也向乌克兰施压，要求其停止对炼油厂的袭击。炼油厂是莫斯科战争机器的命脉。" data-title="Trump Gives Putin a Hand in Russia’s Economic War With Ukraine" data-date="10-13 00:20" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-13 00:20</span>
          <span class="news-item-title">特朗普帮助普京参与俄罗斯与乌克兰的经济战争</span>
          <span class="news-item-title-en">Trump Gives Putin a Hand in Russia’s Economic War With Ukraine</span>
          <span class="news-value-point">💡 特朗普总统正着手购买俄罗斯柴油，同时也向乌克兰施压，要求其停止对炼油厂的袭击</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-13/10712346.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗伊斯兰革命卫队海军12日发表声明说，当天早些时候在霍尔木兹海峡打击了一艘违规的大型油轮。" data-title="伊朗革命卫队：在霍尔木兹海峡打击了一艘违规油轮" data-date="10-13 00:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-13 00:13</span>
          <span class="news-item-title">伊朗革命卫队：在霍尔木兹海峡打击了一艘违规油轮</span>
          <span class="news-value-point">💡 伊朗伊斯兰革命卫队海军12日发表声明说，当天早些时候在霍尔木兹海峡打击了一艘违规的大型油轮</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-13/10712345.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据也门胡塞武装12日消息，沙特阿拉伯战机当天空袭了也门北部焦夫省，造成至少9人死亡、7人受伤。" data-title="胡塞武装称沙特空袭也门北部已致9死7伤" data-date="10-13 00:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-13 00:12</span>
          <span class="news-item-title">胡塞武装称沙特空袭也门北部已致9死7伤</span>
          <span class="news-value-point">💡 据也门胡塞武装12日消息，沙特阿拉伯战机当天空袭了也门北部焦夫省，造成至少9人死亡、7人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-13/10712344.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社耶路撒冷10月12日电(记者庞昕熠 王卓伦)以色列急救组织“红色大卫盾”12日说，以北部靠近黎巴嫩边界的拉米姆山脊地区当天发生爆炸事件，已造成1人死亡、19人受伤，其中多人伤势严重。据以色列媒体报道，死者是一名学生。" data-title="以色列北部发生疑似未爆弹药爆炸致1死19伤" data-date="10-13 00:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-13 00:10</span>
          <span class="news-item-title">以色列北部发生疑似未爆弹药爆炸致1死19伤</span>
          <span class="news-value-point">💡 新华社耶路撒冷10月12日电(记者庞昕熠 王卓伦)以色列急救组织“红色大卫盾”12日说，以北部靠近黎巴嫩边界的拉米姆山脊地区当天发生爆炸事件，已…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-13/10712343.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据尼日利亚方面12日消息，该国西北部扎姆法拉州11日发生袭击事件，造成22人死亡。袭击者当天洗劫了3个村庄并纵火焚烧了12辆汽车。袭击发生时，有安全人员在现场执勤。" data-title="尼日利亚西北部袭击事件致22人死亡" data-date="10-13 00:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-13 00:06</span>
          <span class="news-item-title">尼日利亚西北部袭击事件致22人死亡</span>
          <span class="news-value-point">💡 据尼日利亚方面12日消息，该国西北部扎姆法拉州11日发生袭击事件，造成22人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-13/10712342.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社布鲁塞尔10月12日电 (记者 德永健)欧盟12日宣布对俄罗斯追加制裁措施，将俄罗斯1569名个人和实体列为制裁对象。" data-title="欧盟将俄罗斯近1600名个人和实体列为制裁对象" data-date="10-13 00:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-13 00:00</span>
          <span class="news-item-title">欧盟将俄罗斯近1600名个人和实体列为制裁对象</span>
          <span class="news-value-point">💡 中新社布鲁塞尔10月12日电 (记者 德永健)欧盟12日宣布对俄罗斯追加制裁措施，将俄罗斯1569名个人和实体列为制裁对象</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/12/world/middleeast/iran-houthis-saudi-arabia.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="沙特当局表示，在与也门的胡塞民兵进行了一个周末的对抗后，他们正在抵御无人机和导弹袭击，胡塞民兵的赞助人伊朗提出进行调解。" data-title="Saudi Arabia Faces More Attacks as It Reels From Airport Strikes" data-date="10-12 23:44" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 23:44</span>
          <span class="news-item-title">沙特阿拉伯因机场罢工而面临更多袭击</span>
          <span class="news-item-title-en">Saudi Arabia Faces More Attacks as It Reels From Airport Strikes</span>
          <span class="news-value-point">💡 沙特当局表示，在与也门的胡塞民兵进行了一个周末的对抗后，他们正在抵御无人机和导弹袭击，胡塞民兵的赞助人伊朗提出进行调解</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/12/microsoft-president-says-uk-is-best-placed-to-drive-ai-regulation/" target="_blank" rel="noopener" data-cat="shizheng" data-summary="微软总裁布拉德·史密斯（ Brad Smith ）呼吁对人工智能进行紧急监管，称牛奶和洗衣机比人工智能公司拥有更多的监" data-title="Microsoft president says UK is best placed to drive AI regulation" data-date="10-12 23:31" data-source="TechCrunch">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-12 23:31</span>
          <span class="news-item-title">微软总裁表示，英国最适合推动人工智能监管</span>
          <span class="news-item-title-en">Microsoft president says UK is best placed to drive AI regulation</span>
          <span class="news-value-point">💡 微软总裁布拉德·史密斯（ Brad Smith ）呼吁对人工智能进行紧急监管，称牛奶和洗衣机比人工智能公司拥有更多的监</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10712335.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社吉隆坡10月12日电 (记者 刘育英)马来西亚教育部长法丽娜12日公布最新烟霾停课安排，新增马六甲、森美兰及布城联邦直辖区全面停课，雪兰莪和彭亨部分地区扩大停课范围，柔佛则继续停课至16日，改为居家教学。" data-title="马来西亚教育部扩大烟霾停课范围" data-date="10-12 23:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 23:24</span>
          <span class="news-item-title">马来西亚教育部扩大烟霾停课范围</span>
          <span class="news-value-point">💡 中新社吉隆坡10月12日电 (记者 刘育英)马来西亚教育部长法丽娜12日公布最新烟霾停课安排，新增马六甲、森美兰及布城联邦直辖区全面停课，雪兰莪…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712340.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月12日电 10月12日，中共中央政治局委员、中央外办主任王毅在北京与俄罗斯总统助理、海事委员会主席帕特鲁舍夫举行会晤。" data-title="王毅与俄罗斯总统助理、海事委员会主席帕特鲁舍夫举行会晤" data-date="10-12 23:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 23:14</span>
          <span class="news-item-title">王毅与俄罗斯总统助理、海事委员会主席帕特鲁舍夫举行会晤</span>
          <span class="news-value-point">💡 中新社北京10月12日电 10月12日，中共中央政治局委员、中央外办主任王毅在北京与俄罗斯总统助理、海事委员会主席帕特鲁舍夫举行会晤</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/12/us/politics/ilhan-omar-home-searched.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="搜查是在中期选举的60天窗口内进行的，当时司法部历来避免采取与政治候选人有关的调查步骤。" data-title="Federal Agents Search Home of Rep. Ilhan Omar" data-date="10-12 23:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 23:02</span>
          <span class="news-item-title">联邦特工搜查众议员伊尔汗·奥马尔的家</span>
          <span class="news-item-title-en">Federal Agents Search Home of Rep. Ilhan Omar</span>
          <span class="news-value-point">💡 搜查是在中期选举的60天窗口内进行的，当时司法部历来避免采取与政治候选人有关的调查步骤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712330.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月12日电 全国人大常委会委员长赵乐际12日在北京人民大会堂同越南国会主席陈青敏举行会谈，并共同主持中越立法机构联合委员会第二次会议。" data-title="赵乐际同越南国会主席陈青敏会谈并共同主持中越立法机构联合委员会第二次会议" data-date="10-12 22:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 22:22</span>
          <span class="news-item-title">赵乐际同越南国会主席陈青敏会谈并共同主持中越立法机构联合委员会第二次会议</span>
          <span class="news-value-point">💡 中新社北京10月12日电 全国人大常委会委员长赵乐际12日在北京人民大会堂同越南国会主席陈青敏举行会谈，并共同主持中越立法机构联合委员会第二次会…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712324.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月12日下午，中国国务院总理李强在北京人民大会堂会见越南国会主席陈青敏。中新社记者 田雨昊 摄 中新社北京10月12日电 10月12日下午，中国国务院总理李强在北京人民大会堂会见越南国会主席陈青敏。" data-title="李强会见越南国会主席陈青敏" data-date="10-12 22:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 22:21</span>
          <span class="news-item-title">李强会见越南国会主席陈青敏</span>
          <span class="news-value-point">💡 10月12日下午，中国国务院总理李强在北京人民大会堂会见越南国会主席陈青敏</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-12/10712319.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月12日电 全国人大常委会委员长赵乐际12日在北京人民大会堂同越南国会主席陈青敏举行会谈，并共同主持中越立法机构联合委员会第二次会议。" data-title="赵乐际同越南国会主席陈青敏会谈并共同主持中越立法机构联合委员会第二次会议" data-date="10-12 21:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 21:55</span>
          <span class="news-item-title">赵乐际同越南国会主席陈青敏会谈并共同主持中越立法机构联合委员会第二次会议</span>
          <span class="news-value-point">💡 新华社北京10月12日电 全国人大常委会委员长赵乐际12日在北京人民大会堂同越南国会主席陈青敏举行会谈，并共同主持中越立法机构联合委员会第二次会…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">10 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/jev-like-decision-models-are-flooding-the-ai-market-after-researcher-claims-typesafe-copied-their-research-microsoft-openai-among-companies-releasing-lightweight-system-one-ai-models" target="_blank" rel="noopener" data-cat="keji" data-summary="Jev和大量人工智能决策模型—据称TypeSafe复制了研究人员的架构，但自己也被复制了" data-title="Jev-like decision models are flooding the AI market, after researcher claims TypeSafe copied their research" data-date="10-13 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-13 00:00</span>
          <span class="news-item-title">在研究人员声称TypeSafe复制了他们的研究之后，类似Jev的决策模型正在涌入人工智能市场</span>
          <span class="news-item-title-en">Jev-like decision models are flooding the AI market, after researcher claims TypeSafe copied their research</span>
          <span class="news-value-point">💡 Jev和大量人工智能决策模型—据称TypeSafe复制了研究人员的架构，但自己也被复制了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/meet-the-modders-porting-ringfenced-dlss-features-to-older-gpus-how-dlss-5-and-multi-frame-generation-were-unlocked-for-older-architectures" target="_blank" rel="noopener" data-cat="keji" data-summary="至少根据Nvidia的说法， DLSS多帧生成和DLSS 5神经渲染现在可以在从未打算用于它的硬件上运行。现在，这些社区进步发布的两个基础模块大声疾呼。" data-title="Meet the modders porting ringfenced DLSS features to older GPUs" data-date="10-12 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-12 23:30</span>
          <span class="news-item-title">了解将DLSS功能移植到旧GPU的调制解调器</span>
          <span class="news-item-title-en">Meet the modders porting ringfenced DLSS features to older GPUs</span>
          <span class="news-value-point">💡 至少根据Nvidia的说法， DLSS多帧生成和DLSS 5神经渲染现在可以在从未打算用于它的硬件上运行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/121.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 12 日消息，比亚迪今日宣布与荣耀战略合作，共创 AI 语音融合，A2A 打通车机与手机语音智能体，将手机 AI 能力和服务带入座舱空间。据介绍，比亚迪将支持 YOYO 远程控车，包括语音寻车、语音备车，一句话直达；手机镜像桌面，全量 App 上车，行车操控更从容；AI 语音融合，语音助手 A2A 跨端打通，车机语音轻松操控手机；YOYO 全技能上车，一句话随心控。IT之家注意到，比亚迪 8 月 25 日官宣与荣耀达成深度手车互联合作，地址流转一拖即达、音乐无缝流转、微信扫一扫一句话唤起（需要 DiLink100 及以上智能座舱平台）。2025 年 10 月，荣耀宣布与比亚迪签署战略合作协议，将聚焦核心技术与功能落地、渠道生态与用户权益、联合传播与用户触达三条主线纵深推进" data-title="比亚迪与荣耀战略合作：支持 YOYO 远程控车、手机镜像等" data-date="10-12 23:08" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 23:08</span>
          <span class="news-item-title">比亚迪与荣耀战略合作：支持 YOYO 远程控车、手机镜像等</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，比亚迪今日宣布与荣耀战略合作，共创 AI 语音融合，A2A 打通车机与手机语音智能体，将手机 AI 能力和服务…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/console-gaming/xbox-cloud-gaming-is-now-available-on-jailbroken-ps5s-allows-upscaling-to-4k-using-the-ps5-gpu" target="_blank" rel="noopener" data-cat="keji" data-summary="RafaelNGP发布了原生Xbox Game Pass应用程序，允许在PS5上使用Xbox Cloud Gaming ，在PS5 GPU上支持4个控制器和4K升级。" data-title="Developer uses Claude to enable Xbox Cloud Gaming on jailbroken PS5s" data-date="10-12 22:46" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-12 22:46</span>
          <span class="news-item-title">开发人员使用Claude在越狱的PS5上启用Xbox Cloud Gaming</span>
          <span class="news-item-title-en">Developer uses Claude to enable Xbox Cloud Gaming on jailbroken PS5s</span>
          <span class="news-value-point">💡 RafaelNGP发布了原生Xbox Game Pass应用程序，允许在PS5上使用Xbox Cloud Gaming ，在PS5 GPU上支持…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/115.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 12 日消息，微软今天正式发布 Maia 300 人工智能芯片。这款产品配备 288GB HBM4 内存，带宽达到 18TB/s，FP4 算力可达 13.8 PFLOPS，基于台积电 N2P 制程工艺打造，计划 2027 年部署。IT之家注意到，Maia 300 采用多芯粒设计，主要计算部分采用台积电 N2P 2 纳米制程，集成独立内存芯粒和 I/O 芯粒。FP4 算力最高可达 13.8 PFLOPS，FP8 算力为 6.9 PFLOPS。其 SoC 功耗额定值为 950W，明显高于 Maia 200 的 750W。同时，该产品配备 8 组 HBM4 内存，总容量可达 288GB，带宽为 18TB/s，更适合对内存要求较高的 AI 推理任务。双向扩展互连带宽达到 3.2T" data-title="微软 Maia 300 AI 芯片发布：台积电 N2P 工艺，288GB HBM4 内存、带宽 18TB/s" data-date="10-12 22:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 22:45</span>
          <span class="news-item-title">微软 Maia 300 AI 芯片发布：台积电 N2P 工艺，288GB HBM4 内存、带宽 18TB/s</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，微软今天正式发布 Maia 300 人工智能芯片</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-to-phase-out-sgx-after-xeon-diamond-rapids-in-favor-of-tdx-confidential-computing-pivot-adds-trusted-i-o-and-post-quantum-crypto-for-agentic-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔将在Xeon “Diamond Rapids”之后停产SGX ，并专注于扩展TDX功能，以满足云计算、企业工作负载和代理AI的新兴安全要求。" data-title="Intel to phase out SGX after Xeon Diamond Rapids in favor of TDX" data-date="10-12 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-12 22:00</span>
          <span class="news-item-title">英特尔将在Xeon Diamond Rapids之后逐步淘汰新加坡交易所，转而采用TDX</span>
          <span class="news-item-title-en">Intel to phase out SGX after Xeon Diamond Rapids in favor of TDX</span>
          <span class="news-value-point">💡 英特尔将在Xeon “Diamond Rapids”之后停产SGX ，并专注于扩展TDX功能，以满足云计算、企业工作负载和代理AI的新兴安全要求</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/liquid-cooling/diamond-infused-watercooling-coldplates-for-2-300w-nvidia-rubin-drop-temps-by-up-to-22c-bespoke-frore-liquidjet-diamond-cooling-tames-770-w-cm2-hotspots" target="_blank" rel="noopener" data-cat="keji" data-summary="为定制设计的人工智能服务器定制的冷板： Frore的LiquidJet Diamond。" data-title="Diamond-infused watercooling coldplates for 2,300W Nvidia Rubin drop temps by up to 22C" data-date="10-12 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-12 21:30</span>
          <span class="news-item-title">注入钻石的水冷却冷板，适用于2,300W Nvidia Rubin跌落温度高达22C</span>
          <span class="news-item-title-en">Diamond-infused watercooling coldplates for 2,300W Nvidia Rubin drop temps by up to 22C</span>
          <span class="news-value-point">💡 为定制设计的人工智能服务器定制的冷板： Frore的LiquidJet Diamond</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/12/technology/universal-basic-income-silicon-valley.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一年多来，《纽约时报》跟踪了全民基本收入计划的接受者，埃隆·马斯克(Elon Musk)和其他科技领袖一直将其作为解决人工智能推动的失业问题的解决方案。" data-title="Is Universal Basic Income the Answer to A.I." data-date="10-12 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 17:00</span>
          <span class="news-item-title">全民基本收入是解决人工智能问题的答案吗</span>
          <span class="news-item-title-en">Is Universal Basic Income the Answer to A.I.</span>
          <span class="news-value-point">💡 一年多来，《纽约时报》跟踪了全民基本收入计划的接受者，埃隆·马斯克(Elon Musk)和其他科技领袖一直将其作为解决人工智能推动的失业问题的解…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502654.html" target="_blank" rel="noopener" data-cat="keji" data-summary="游戏打到21:0，AI甚至不用再调用大模型了" data-title="华为AI靠RSI通关25款游戏！操作次数比人类少56%" data-date="10-12 13:48" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-12 13:48</span>
          <span class="news-item-title">华为AI靠RSI通关25款游戏！操作次数比人类少56%</span>
          <span class="news-value-point">💡 游戏打到21:0，AI甚至不用再调用大模型了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502649.html" target="_blank" rel="noopener" data-cat="keji" data-summary="GLM“速度仙人”来了？" data-title="智谱新模型，490 tokens/s！" data-date="10-12 10:37" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-12 10:37</span>
          <span class="news-item-title">智谱新模型，490 tokens/s！</span>
          <span class="news-value-point">💡 GLM“速度仙人”来了</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/12/man-citys-crisis-pushes-the-limits-of-language" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="不仅仅是俱乐部最近的收费本身是前所未有的，它也是用来描述它们的语言在这里注册我们的免费通讯足球语言是一种精美且高度细致入微的方言。大多数参与者" data-title="Winning is not enough for Manchester City to move on from this crisis | Jonathan Wilson" data-date="10-12 22:24" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 22:24</span>
          <span class="news-item-title">胜利不足以让曼城摆脱这场危机|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Winning is not enough for Manchester City to move on from this crisis | Jonathan Wilson</span>
          <span class="news-value-point">💡 不仅仅是俱乐部最近的收费本身是前所未有的，它也是用来描述它们的语言在这里注册我们的免费通讯足球语言是一种精美且高度细致入微的方言</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmq5nzn8ww98o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳主教练米克尔·阿尔特塔（ Mikel Arteta ）表示，皮耶罗·辛卡皮（ Piero Hincapie ）和马丁·祖比门迪（ Martin Zubimendi ）在赛后训练中受伤“远非" data-title="Hincapie and Zubimendi injured in post-match training session" data-date="10-12 22:22" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 22:22</span>
          <span class="news-item-title">Hincapie和Zubimendi在赛后训练中受伤</span>
          <span class="news-item-title-en">Hincapie and Zubimendi injured in post-match training session</span>
          <span class="news-value-point">💡 阿森纳主教练米克尔·阿尔特塔（ Mikel Arteta ）表示，皮耶罗·辛卡皮（ Piero Hincapie ）和马丁·祖比门迪（ Mart…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmp3gwz17qn7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛可能刚刚从三周的休息中恢复过来，但对于它的许多明星来说，他们根本没有休息。" data-title="Elite schedule &#39;not sustainable&#39; amid 55" data-date="10-12 18:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 18:26</span>
          <span class="news-item-title">55周年之际的精英赛程“不可持续”</span>
          <span class="news-item-title-en">Elite schedule 'not sustainable' amid 55</span>
          <span class="news-value-point">💡 英超联赛可能刚刚从三周的休息中恢复过来，但对于它的许多明星来说，他们根本没有休息</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/12/premier-league-10-talking-points-from-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城对胜利毫不后悔，马刺取得了某种进步，诺尼·马杜埃克迎接了这一时刻。曼城在利物浦获胜的方式既是辩护也是诽谤。那些兴高采烈地挥舞着充气香蕉" data-title="Premier League: 10 talking points from the weekend’s action" data-date="10-12 15:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 15:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 曼城对胜利毫不后悔，马刺取得了某种进步，诺尼·马杜埃克迎接了这一时刻</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/impervious-city-shrug-off-chaos-and-controversy-to-silence-anfield" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="被称为英超联赛冠军清算日的东西变成了周日下午的漫步安菲尔德欢迎曼城进入他们的新现实，一个肮脏的地方，每一次触摸都伴随着“作弊”的呼喊，任何有利的" data-title="Manchester City shrug off chaos and controversy in public shaming at Anfield | Andy Hunter" data-date="10-12 04:02" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 04:02</span>
          <span class="news-item-title">曼城在安菲尔德的公开羞辱中摆脱混乱和争议|安迪·亨特</span>
          <span class="news-item-title-en">Manchester City shrug off chaos and controversy in public shaming at Anfield | Andy Hunter</span>
          <span class="news-value-point">💡 被称为英超联赛冠军清算日的东西变成了周日下午的漫步安菲尔德欢迎曼城进入他们的新现实，一个肮脏的地方，每一次触摸都伴随着“作弊”的呼喊，任何有利的</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/enzo-maresca-manchester-city-liverpool-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“你无法想象我有多开心……我来这里是为了赢得&#39;自从有罪判决以来，曼城在安菲尔德的第一场比赛中以3比0获胜恩佐·马雷斯卡称赞曼城在利物浦“制造自己的噪音”，因为他们忽略了周围的争议和威胁" data-title="‘We make our own noise’: Maresca hails Manchester City after Liverpool triumph" data-date="10-12 03:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 03:43</span>
          <span class="news-item-title">“我们自己制造噪音” ：马雷斯卡在利物浦胜利后称赞曼城</span>
          <span class="news-item-title-en">‘We make our own noise’: Maresca hails Manchester City after Liverpool triumph</span>
          <span class="news-value-point">💡 “你无法想象我有多开心……我来这里是为了赢得'自从有罪判决以来，曼城在安菲尔德的第一场比赛中以3比0获胜恩佐·马雷斯卡称赞曼城在利物浦“制造自己…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck5yn20wej62o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦在安菲尔德的挣扎仍在继续，因为伊拉奥拉仍在等待他在安菲尔德的第一场英超联赛胜利。" data-title="Winless and an &#39;easy touch&#39; - what&#39;s happened to the Anfield fear factor?" data-date="10-12 03:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 03:41</span>
          <span class="news-item-title">无胜利和“轻松触摸” -安菲尔德的恐惧因素发生了什么？</span>
          <span class="news-item-title-en">Winless and an 'easy touch' - what's happened to the Anfield fear factor?</span>
          <span class="news-value-point">💡 利物浦在安菲尔德的挣扎仍在继续，因为伊拉奥拉仍在等待他在安菲尔德的第一场英超联赛胜利</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/premier-league-returns-in-shadow-of-manchester-citys-judgment-day" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从俱乐部被判犯有违反财务规则的罪行以来，足球在比赛的第一个周末感觉次要Cimbri正朝着危险的南方前进，但在罗马，生活仍在继续。小行星肯定是朝这边来的，但人们去上班，吃饭，" data-title="Premier League returns in shadow of Manchester City’s judgment day | Jonathan Wilson" data-date="10-12 03:11" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 03:11</span>
          <span class="news-item-title">英超联赛在曼城审判日的阴影下回归|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Premier League returns in shadow of Manchester City’s judgment day | Jonathan Wilson</span>
          <span class="news-value-point">💡 自从俱乐部被判犯有违反财务规则的罪行以来，足球在比赛的第一个周末感觉次要Cimbri正朝着危险的南方前进，但在罗马，生活仍在继续</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c962y5nd273no?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安迪·伯纳姆（ Andy Burnham ）在曼城被判犯有与违反英超财务规则有关的所有指控后发表的言论遭到了批评。" data-title="Burnham to release details of Man City meetings" data-date="10-12 02:01" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 02:01</span>
          <span class="news-item-title">伯纳姆将公布曼城会议的细节</span>
          <span class="news-item-title-en">Burnham to release details of Man City meetings</span>
          <span class="news-value-point">💡 安迪·伯纳姆（ Andy Burnham ）在曼城被判犯有与违反英超财务规则有关的所有指控后发表的言论遭到了批评</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/11/liverpool-v-manchester-city-premier-league-live-score-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在Ryan Gravenberch的红牌之后，曼城拥抱了一种充满敌意的气氛，并让利物浦不堪重负威尔·昂温（ Will Unwin ）的更新，他是我们安菲尔德队今天比赛的一员。600多名曼城球迷组成的队伍得到了警察的护送，穿过车站" data-title="Liverpool 0-3 Manchester City: Premier League – as it happened" data-date="10-12 01:52" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:52</span>
          <span class="news-item-title">利物浦0-3曼城：英超联赛–实际情况</span>
          <span class="news-item-title-en">Liverpool 0-3 Manchester City: Premier League – as it happened</span>
          <span class="news-value-point">💡 在Ryan Gravenberch的红牌之后，曼城拥抱了一种充满敌意的气氛，并让利物浦不堪重负威尔·昂温（ Will Unwin ）的更新，他是…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/liverpool-manchester-city-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是曼城以前听过的配乐，但在比赛期间从未听过如此持续的魔咒。它来自利物浦的支持，在开球前先在安菲尔德周围响起，然后定期来。它总是" data-title="Cherki cracker caps Manchester City win at Liverpool in face of Anfield taunts" data-date="10-12 01:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:42</span>
          <span class="news-item-title">面对安菲尔德的嘲讽，切尔基·克拉克（ Cherki Cracker ）在利物浦夺冠</span>
          <span class="news-item-title-en">Cherki cracker caps Manchester City win at Liverpool in face of Anfield taunts</span>
          <span class="news-value-point">💡 这是曼城以前听过的配乐，但在比赛期间从未听过如此持续的魔咒</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck87z1jjynyqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和曼城球员在英超比赛后的评分。" data-title="Who &#39;simply has to do better&#39;? Liverpool v Man City player ratings" data-date="10-12 01:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 01:30</span>
          <span class="news-item-title">谁“只需要做得更好” ？利物浦v曼城球员评分</span>
          <span class="news-item-title-en">Who 'simply has to do better'? Liverpool v Man City player ratings</span>
          <span class="news-value-point">💡 利物浦和曼城球员在英超比赛后的评分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-12 01:26" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:26</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1009604/elon-musk-2026-midterm-republican-donations" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据《纽约时报》报道，埃隆·马斯克（ Elon Musk ）自7月以来已向共和党团体发放了至少2.76亿美元，使他成为该党最大的知名捐助者和最大的中期捐助者。其中1.58亿美元-最大的政治捐款人之一" data-title="Elon Musk has donated over $276 million to Republican midterm efforts" data-date="10-13 00:52" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-13 00:52</span>
          <span class="news-item-title">埃隆·马斯克(Elon Musk)已向共和党中期计划捐款逾2.76亿美元($)</span>
          <span class="news-item-title-en">Elon Musk has donated over $276 million to Republican midterm efforts</span>
          <span class="news-value-point">💡 据《纽约时报》报道，埃隆·马斯克（ Elon Musk ）自7月以来已向共和党团体发放了至少2.76亿美元，使他成为该党最大的知名捐助者和最大的…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/3d-scanning/bambu-lab-announces-its-first-3d-scanner-and-it-might-be-expensive" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Bambu Lab嘲笑其S1 3D扫描仪， FCC文件暗示了Bambu Lab目前保密的内容。" data-title="Bambu Lab officially teases its first 3D scanner" data-date="10-13 00:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-13 00:15</span>
          <span class="news-item-title">Bambu Lab正式推出其首款3D扫描仪</span>
          <span class="news-item-title-en">Bambu Lab officially teases its first 3D scanner</span>
          <span class="news-value-point">💡 Bambu Lab嘲笑其S1 3D扫描仪， FCC文件暗示了Bambu Lab目前保密的内容</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/12/us/politics/whos-winning-the-race-for-congress.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="距离期中考试还有10月12日至22日。这就是游戏的状态。" data-title="Who’s Winning the Race for Congress?" data-date="10-12 23:52" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 23:52</span>
          <span class="news-item-title">谁在赢得国会竞选？</span>
          <span class="news-item-title-en">Who’s Winning the Race for Congress?</span>
          <span class="news-value-point">💡 距离期中考试还有10月12日至22日</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1009594/russian-bots-yandex-outage-drone-strikes-debunk" target="_blank" rel="noopener" data-cat="zonghe" data-summary="上周多次乌克兰无人机袭击使俄罗斯数据中心下线，据报道导致在线机器人流量急剧下降-但实际上，这可能不是大多数人与俄罗斯相关的那种机器人活动。" data-title="The Yandex outage probably didn’t blitz Russian bots" data-date="10-12 23:43" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-12 23:43</span>
          <span class="news-item-title">Yandex中断可能没有闪电击中俄罗斯机器人</span>
          <span class="news-item-title-en">The Yandex outage probably didn’t blitz Russian bots</span>
          <span class="news-value-point">💡 上周多次乌克兰无人机袭击使俄罗斯数据中心下线，据报道导致在线机器人流量急剧下降-但实际上，这可能不是大多数人与俄罗斯相关的那种机器人活动</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/127.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，苹果旗下品牌 Beats 今天在官方 X 账号发布视频，预热一款联名新品。从视频中的轮廓我们不难看出，这款产品就是 Beats Pill 蓝牙音箱，随着画面中亮起几道闪电，音箱的设计细节也随之显现。视频最后出现了 Beats 和宝可梦的图标。IT之家注意到，宝可梦系列最广为人知的角色“皮卡丘”曾在今年 8 月“到访”苹果总部 Apple Park，他那时候与时任苹果首席执行官蒂姆 · 库克、时任苹果硬件工程高级副总裁约翰 · 特努斯互动。" data-title="宝可梦联名：苹果 Beats 预热特别版 Pill 蓝牙音箱" data-date="10-12 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 23:28</span>
          <span class="news-item-title">宝可梦联名：苹果 Beats 预热特别版 Pill 蓝牙音箱</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，苹果旗下品牌 Beats 今天在官方 X 账号发布视频，预热一款联名新品</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/12/this-ai-startup-says-it-can-generate-permit-ready-blueprints-in-minutes/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Blueprints AI是一家总部位于圣莫尼卡的初创公司，它开发的软件可以从照片、PDF或草图中生成符合代码的施工蓝图。" data-title="This AI startup says it can generate permit-ready blueprints in minutes" data-date="10-12 23:27" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-12 23:27</span>
          <span class="news-item-title">这家AI初创公司表示，它可以在几分钟内生成许可证就绪的蓝图</span>
          <span class="news-item-title-en">This AI startup says it can generate permit-ready blueprints in minutes</span>
          <span class="news-value-point">💡 Blueprints AI是一家总部位于圣莫尼卡的初创公司，它开发的软件可以从照片、PDF或草图中生成符合代码的施工蓝图</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/126.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，熊猫旗下“S24Q6A”23.8 英寸显示器现已在京东发售，该机主打 2K 180Hz，定价为 599 元，部分地区国补后低至 521.1 元。京东熊猫“S24Q6A”显示器 599 元点此访问该机配备一块 2560x1440 分辨率 180Hz Fast IPS 面板，显示器亮度 400 尼特，GtG 响应速度 1ms，对比度 1000:1，显示器支持 8-Bit 色彩，覆盖 95% DCI-P3 色域。该机采用固定支架，显示器提供 1 个 HDMI 2.0、1 个 DP 1.4、1 个 3.5mm 音频接口，IT之家附显示器参数：京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3 次：点此抽红包。" data-title="熊猫“S24Q6A”23.8 英寸显示器发售：2K 180Hz，599 元（国补后 521.1 元）" data-date="10-12 23:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 23:27</span>
          <span class="news-item-title">熊猫“S24Q6A”23.8 英寸显示器发售：2K 180Hz，599 元（国补后 521.1 元）</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，熊猫旗下“S24Q6A”23.8 英寸显示器现已在京东发售，该机主打 2K 180Hz，定价为 599 元，部…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/125.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，Mozilla 今天推出火狐 Firefox 浏览器 158 版本，最大的亮点是默认启用 JPEG XL 图像支持。官方表示，JPEG XL 可作为 WebP、JPEG、PNG 和 GIF 等图像格式的替代方案。浏览器请求图像时默认使用的 HTTP Accept 请求头，已支持 JPEG XL 图像格式，此前版本需通过实验性选项才可开启。Firefox 158 还改进了智能窗口（IT之家注：Smart Window）表单填写功能。用户点击表单字段，或选择从来源中填充内容时，可以更快地完成表单填写。此外，该浏览器现已支持 CSS 类型化算术运算，允许使用 calc () 等函数对两个数据类型相同、但单位不同的值进行除法运算。" data-title="火狐 Firefox 158 浏览器发布，默认启用 JPEG XL 图像支持" data-date="10-12 23:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 23:19</span>
          <span class="news-item-title">火狐 Firefox 158 浏览器发布，默认启用 JPEG XL 图像支持</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，Mozilla 今天推出火狐 Firefox 浏览器 158 版本，最大的亮点是默认启用 JPEG XL 图像…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/122.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，赛力斯集团旗下豪华电动汽车品牌问界今天在巴黎车展宣布，计划 2027 年秋季进军欧洲市场，为欧洲用户带来全新智能出行体验。IT之家从官方新闻稿了解到，问界正在积极推进欧洲本地化、法规认证工作。产品研发层面，问界将以欧盟整车型式认证（WVTA）为基础，争取 2026 年获得欧盟新车安全评鉴协会（Euro NCAP）五星评级，满足欧洲各国法规要求并追求高安全标准。同时，问界将针对欧洲道路条件、驾驶习惯和当地生活方式展开全面本土化适配，公司正与合作伙伴共研辅助驾驶和泊车辅助功能，适应当地道路状况和驾驶场景。建设本地化服务网络，涵盖智能诊断、出行服务、本地备件供应和专属客户服务团队，为欧洲用户提供高效用车体验。除此之外，问界本次在巴黎车展带来了 M9、M8、M7 和" data-title="问界官宣 2027 年秋季进军欧洲市场，力争年内获得 Euro NCAP 五星评级" data-date="10-12 23:12" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 23:12</span>
          <span class="news-item-title">问界官宣 2027 年秋季进军欧洲市场，力争年内获得 Euro NCAP 五星评级</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，赛力斯集团旗下豪华电动汽车品牌问界今天在巴黎车展宣布，计划 2027 年秋季进军欧洲市场，为欧洲用户带来全新智…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712333.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社广西钦州10月12日电 (陈秋霞)参加第37届世界运河大会的中外嘉宾12日赴中国西部陆海新通道骨干工程平陆运河考察。内河航道国际组织(IWI)主席莎伦·莱顿表示，中国人把从漫长历史里学到的治水智慧，运用到了平陆运河项目当中。" data-title="中外专家考察平陆运河 探访工程建设经验" data-date="10-12 23:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 23:06</span>
          <span class="news-item-title">中外专家考察平陆运河 探访工程建设经验</span>
          <span class="news-value-point">💡 中新社广西钦州10月12日电 (陈秋霞)参加第37届世界运河大会的中外嘉宾12日赴中国西部陆海新通道骨干工程平陆运河考察</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/118.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 12 日消息，比亚迪旗下品牌腾势今天在巴黎国际车展宣布，将在欧洲推出“天神之眼”辅助驾驶系统，首批支持车型为 Z9 GT，预计明年通过 OTA 更新推送。据介绍，欧洲版腾势 Z9 GT 未来将能够实现自动识别红灯停车、进入环岛主动礼让、自动遵循道路限速，支持城市领航辅助驾驶（IT之家注：NOA）。官方宣称这套系统遇到双排停车车辆和缓慢行驶车流时可以自动变道，还能够礼让狭窄街道的行人和骑行者。目前，比亚迪和腾势团队正在进行软件开发后期工作、校准和适配，之后会申请联合国 R171 认证。腾势已确认，这套系统将检测驾驶员的视线方向、头部姿态，以及手是否放在方向盘上。" data-title="比亚迪腾势将在欧洲推出“天神之眼”辅助驾驶系统，Z9 GT 率先支持" data-date="10-12 23:00" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 23:00</span>
          <span class="news-item-title">比亚迪腾势将在欧洲推出“天神之眼”辅助驾驶系统，Z9 GT 率先支持</span>
          <span class="news-value-point">💡 IT之家 10 月 12 日消息，比亚迪旗下品牌腾势今天在巴黎国际车展宣布，将在欧洲推出“天神之眼”辅助驾驶系统，首批支持车型为 Z9 GT，预…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1008161/mechanism-basecase-switch-2-case-hands-on" target="_blank" rel="noopener" data-cat="zonghe" data-summary="大多数公司都放慢了发布新款Switch 2手机壳的速度，但我最喜欢的配件制造商之一最近在几次延迟之后首次亮相。Mechanism的$ 49 Basecase是控制台的搭扣式外壳，可接入公司的模块" data-title="Mechanism’s first Switch 2 case is as awesome as I hoped it would be" data-date="10-12 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-12 23:00</span>
          <span class="news-item-title">Mechanism的第一个Switch 2保护壳和我希望的一样棒</span>
          <span class="news-item-title-en">Mechanism’s first Switch 2 case is as awesome as I hoped it would be</span>
          <span class="news-value-point">💡 大多数公司都放慢了发布新款Switch 2手机壳的速度，但我最喜欢的配件制造商之一最近在几次延迟之后首次亮相</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/012/116.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【京东活动可能随时变更，需以实付款为准】腾达泰山 BE7200 Ultra 路由器 2026 年 1 月开售，该路由器宣称“挑战史上 7200 性价比之王”，售价 549 元，首发价 429 元。京东 11.11 大促期间，按下方步骤下单，叠加 10% 国补后仅需 244.36 元：领 480-60 元 PLUS 补贴券：点此查看。12 日晚 8 点 ~13 日下单返实付价 20%，晒单返 20 元，种草返 15 元。京东腾达泰山 BE7200 Ultra 路由器五天线设计 + 9 颗 FEM 国补后 244.36 元直达链接返现规则京东无门槛红包至高 26888 元无门槛可用：点此抽取。IT之家获悉，腾达泰山 BE7200 Ultra 路由器采用了五天线设计，集成 9 颗 FEM，其中 4" data-title="五天线设计 + 9 颗 FEM：腾达泰山 BE7200 Ultra 路由器 429 → 244 元国补直降" data-date="10-12 22:45" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-12 22:45</span>
          <span class="news-item-title">五天线设计 + 9 颗 FEM：腾达泰山 BE7200 Ultra 路由器 429 → 244 元国补直降</span>
          <span class="news-value-point">💡 【京东活动可能随时变更，需以实付款为准】腾达泰山 BE7200 Ultra 路由器 2026 年 1 月开售，该路由器宣称“挑战史上 7200 …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-unveils-7nm-class-fdx-fusion-node-fd-soi-node-doubles-22fdx-transistor-density-comes-7-years-after-firm-abandoned-finfet" target="_blank" rel="noopener" data-cat="zonghe" data-summary="GlobalFoundries通过7纳米级FDX融合工艺重返先进的FD-SOI开发—计划于2028年生产。" data-title="GlobalFoundries unveils 7nm-class FDX Fusion node — comes 7 years after firm abandoned FinFET" data-date="10-12 22:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-12 22:30</span>
          <span class="news-item-title">GlobalFoundries推出7纳米级FDX融合节点—在公司放弃FinFET 7年后推出</span>
          <span class="news-item-title-en">GlobalFoundries unveils 7nm-class FDX Fusion node — comes 7 years after firm abandoned FinFET</span>
          <span class="news-value-point">💡 GlobalFoundries通过7纳米级FDX融合工艺重返先进的FD-SOI开发—计划于2028年生产</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-12/10712328.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月12日电 (记者 陈杭)北京市规划和自然资源委员会12日发布的《关于本市住宅公共空间品质提升的意见(试行)》提出，北京鼓励采用下沉庭院、立体绿化等方式开展景观设计，鼓励采用屋顶绿化、垂直绿化等方式，增加社区绿色空间，做到“推窗见绿”。" data-title="北京提升社区公共空间品质 鼓励住宅“推窗见绿”" data-date="10-12 22:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 22:06</span>
          <span class="news-item-title">北京提升社区公共空间品质 鼓励住宅“推窗见绿”</span>
          <span class="news-value-point">💡 中新社北京10月12日电 (记者 陈杭)北京市规划和自然资源委员会12日发布的《关于本市住宅公共空间品质提升的意见(试行)》提出，北京鼓励采用下…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-13 00:53（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
