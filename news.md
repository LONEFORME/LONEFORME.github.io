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
      <span>2026-09-04 16:03 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar" style="margin: 12px 0 8px; display: flex; align-items: center; gap: 8px; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.2); border-radius: 8px; padding: 7px 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity: 0.65;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)" style="flex: 1; background: transparent; border: none; outline: none; color: inherit; font-size: 13px;">
    <span id="news-search-count" style="font-size: 12px; opacity: 0.7; font-weight: 500;"></span>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">53</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">9</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">14</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-03/10689967.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【本期导读】" data-title="【讲习所·中国与世界】习近平以4点主张推动上合组织实现更高质量发展" data-date="09-03 22:57" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-03 22:57</span>
      </div>
      <h2 class="hero-featured-title">【讲习所·中国与世界】习近平以4点主张推动上合组织实现更高质量发展</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/09/03/ollie-is-betting-privacy-can-win-the-ai-assistant-race/" target="_blank" rel="noopener" data-cat="keji" data-summary="这款以家庭为中心的人工智能助手希望了解你日常生活的细节，但表示不会使用这些数据来训练人工智能模型或与他人分享。" data-title="Ollie押注其对隐私的关注可以帮助它赢得AI助手竞赛" data-date="09-04 00:09" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Ollie押注其对隐私的关注可以帮助它赢得AI助手竞赛</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ce87v0e868qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="过去有句老话说，英国球员的价值很高。现在这似乎只适用于已经在英超联赛中的球员。" data-title="英超联赛的溢价为 2000 万英镑——这让欧洲俱乐部感到担忧" data-date="09-03 19:13" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">英超联赛的溢价为 2000 万英镑——这让欧洲俱乐部感到担忧</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/0/998/179.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 3 日消息，英特尔 Graphics Software 32.0.101.8992 显卡驱动（适用于 Arc）今日发布。本次为 Non-WHQL 测试版本，为英特尔 Arc B 系列、A 系列独立显卡以及英特尔酷睿 Ultra 系列集成 Arc 核显提供支持，新增两款新游戏支持，修复了多款游戏存在的画面异常问题。IT之家附官方公告链接（https://www.intel.com/content/www/us/en/download/785597/intel-arc-graphics-windows.html）。新游戏支持与性能优化为《鬼武者：剑之道》提供支持为《黎明行者之血》提供支持问题修复修复《失落星船：马拉松》（DX12）在各产品线中，使用各向异性过滤时游戏过程中部分物" data-title="英特尔 Arc 显卡驱动 32.0.101.8992 测试版发布：支持两款新游戏，修复多款游戏画面异常问题" data-date="09-03 22:20" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">英特尔 Arc 显卡驱动 32.0.101.8992 测试版发布：支持两款新游戏，修复多款游戏画面异常问题</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-03/10689967.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【本期导读】" data-title="【讲习所·中国与世界】习近平以4点主张推动上合组织实现更高质量发展" data-date="09-03 22:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 22:57</span>
          <span class="news-item-title">【讲习所·中国与世界】习近平以4点主张推动上合组织实现更高质量发展</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/business/economy/trump-irs-college-nonprofits.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国财政部发布了规定，禁止开展种族项目的学校获得免税资格，这对高等教育和其他私立学校构成威胁。" data-title="特朗普采取行动取消帮助少数族裔学生的学校的免税" data-date="09-04 00:17" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 00:17</span>
          <span class="news-item-title">特朗普采取行动取消帮助少数族裔学生的学校的免税</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/upshot/trump-dc-mall-garden-heroes.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="拟议中的英雄花园正在沿着一条熟悉的道路前进，在这条道路上，地面上的事实比法庭能够跟上的速度更快。" data-title="特朗普的华盛顿特区改造项目“只是一个想法” ，直到它们变得更多" data-date="09-04 00:18" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 00:18</span>
          <span class="news-item-title">特朗普的华盛顿特区改造项目“只是一个想法” ，直到它们变得更多</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/world/americas/lake-ontario-bodies-of-water-naming-disputes-south-china-sea.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统将其命名为“美国湖”的举动在一个充满争议地名的世界中脱颖而出，这些地名通常代表更深层次的政治或领土争端。" data-title="安大略湖是众多在命名斗争中被淹没的水体之一" data-date="09-03 17:04" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-03 17:04</span>
          <span class="news-item-title">安大略湖是众多在命名斗争中被淹没的水体之一</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-04/10690286.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月4日电 (记者 张素 李纯)中国最高人民检察院、国家医疗保障局4日联合发布6件依法从严惩治医保骗保犯罪典型案例，其中一起案例中涉案41人因“回流药”骗保犯罪获刑。" data-title="中国最高检、国家医保局联合发布案例 涉惩治“回流药”骗保等" data-date="09-04 14:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-04 14:30</span>
          <span class="news-item-title">中国最高检、国家医保局联合发布案例 涉惩治“回流药”骗保等</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/us/politics/trump-triumphal-arch-plans-approval.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="内政部长道格·布尔古姆 (Doug Burgum) 宣布计划开始修建 250 英尺高的凯旋门。该项目仍有待最终批准。" data-title="特朗普将在获得批准之前破土动工" data-date="09-04 07:44" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 07:44</span>
          <span class="news-item-title">特朗普将在获得批准之前破土动工</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/us/politics/vance-iran-press-briefing.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在卡罗琳·莱维特卸任新闻秘书后的首次白宫新闻发布会上，副总统表示，冲突何时结束取决于德黑兰。" data-title="JD万斯表示他不会将伊朗冲突称为战争" data-date="09-04 05:51" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 05:51</span>
          <span class="news-item-title">JD万斯表示他不会将伊朗冲突称为战争</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/us/politics/trump-acting-army-secretary.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="此举是在丹尼尔·P·德里斯科尔辞职几天后发生的，他与国防部长皮特·赫格斯在清洗陆军高级将领问题上发生了冲突。" data-title="特朗普任命陆军工程官员担任代理部长" data-date="09-04 09:18" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 09:18</span>
          <span class="news-item-title">特朗普任命陆军工程官员担任代理部长</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/business/economy/labor-secretary-chavez-deremer-report.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="监察长发现，洛里·查韦斯-德雷默将劳工部的资金用于个人旅行，并容忍该机构内的骚扰行为。" data-title="部门报告发现前劳工部长引发功能障碍和毒性" data-date="09-04 09:52" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 09:52</span>
          <span class="news-item-title">部门报告发现前劳工部长引发功能障碍和毒性</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/09/03/ollie-is-betting-privacy-can-win-the-ai-assistant-race/" target="_blank" rel="noopener" data-cat="keji" data-summary="这款以家庭为中心的人工智能助手希望了解你日常生活的细节，但表示不会使用这些数据来训练人工智能模型或与他人分享。" data-title="Ollie押注其对隐私的关注可以帮助它赢得AI助手竞赛" data-date="09-04 00:09" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-04 00:09</span>
          <span class="news-item-title">Ollie押注其对隐私的关注可以帮助它赢得AI助手竞赛</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/03/googles-latest-ai-weather-model-gives-you-no-excuse-to-forget-your-umbrella/" target="_blank" rel="noopener" data-cat="keji" data-summary="WeatherNext 3 是深度学习技术带来的气象学巨变的最新浪潮。谷歌表示，它将开始向用户在搜索、谷歌地图和 Gemini 中看到的天气信息提供信息。" data-title="谷歌最新的人工智能天气模型让您没有借口忘记带雨伞" data-date="09-03 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-03 23:00</span>
          <span class="news-item-title">谷歌最新的人工智能天气模型让您没有借口忘记带雨伞</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia 表示 Hugging Face 拥有超过 300 万个模型，并被超过 1800 万开发者使用。" data-title="英伟达确认将以129亿美元收购Hugging Face" data-date="09-03 20:42" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-03 20:42</span>
          <span class="news-item-title">英伟达确认将以129亿美元收购Hugging Face</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/lenovo-details-its-rtx-spark-laptops-yoga-pro-9n-and-yoga-9n-2-in-1-get-full-specs-stylus-support" target="_blank" rel="noopener" data-cat="keji" data-summary="联想在柏林IFA之前详细介绍了其RTX Spark笔记本电脑，发布了完整规格并展示了触控笔兼容性。" data-title="联想详细介绍其RTX Spark笔记本电脑— Yoga Pro 9n和Yoga 9n 2合1获得完整规格、触控笔支持" data-date="09-04 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">联想详细介绍其RTX Spark笔记本电脑— Yoga Pro 9n和Yoga 9n 2合1获得完整规格、触控笔支持</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/lenovos-ideapad-vibe-laptops-stand-out-with-seven-colors-and-swappable-keycaps-14-15-inch-models-with-snapdragon-x-and-amd-ai-400-cpus-to-start-at-usd699" target="_blank" rel="noopener" data-cat="keji" data-summary="联想最新的IdeaPad笔记本电脑充满了五彩缤纷的氛围。Vibe系列将有七种色调，带有可更换的键盘键帽，因此您可以搭配机箱或获得一流的对比度。这款14英寸和15英寸笔记本电脑将于今年晚些时候上市，起价为699 $。" data-title="联想的IdeaPad Vibe笔记本电脑以七种颜色和可更换的键帽脱颖而出–配备Snapdragon X和AMD AI 400 CPU的14,15英寸型号起价为$ 699" data-date="09-04 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">联想的IdeaPad Vibe笔记本电脑以七种颜色和可更换的键帽脱颖而出–配备Snapdragon X和AMD AI 400 CPU的14,15英寸型号起价为$ 699</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/lenovo-ditches-fans-in-favor-of-solid-state-airjet-tech-in-super-slim-1-8-pound-aeroblade-laptop-concept-company-also-lands-at-ifa-with-a-14-inch-rollable-screen-notebook-that-expands-to-17-inches" target="_blank" rel="noopener" data-cat="keji" data-summary="联想在IFA 2026上推出了两款新的笔记本电脑概念：采用Frore System的AirJet固态冷却技术的1.83磅0.39英寸厚的AeroBlade ，以及可扩展到17英寸屏幕的紧凑型14英寸可卷屏便携式笔记本电脑，被称为Project Swan。" data-title="联想放弃了风扇，转而采用超薄、1.8磅重的AeroBlade笔记本电脑概念的固态AirJet技术--该公司还推出了一款可扩展到17英寸的14英寸可卷式屏幕笔记本电脑" data-date="09-04 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">联想放弃了风扇，转而采用超薄、1.8磅重的AeroBlade笔记本电脑概念的固态AirJet技术--该公司还推出了一款可扩展到17英寸的14英寸可卷式屏幕笔记本电脑</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/lenovo-thinkcentre-x-ultra-packs-gorgon-halo-amd-ryzen-ai-max-pro-495-shows-up-in-mini-workstation" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD 的 Gorgon Halo 芯片即将揭开神秘面纱。在 IFA 之前，联想展示了搭载 AMD Ryzen AI Max+ Pro 495 的 THinkCentre X Ultra。" data-title="联想ThinkCentre X Ultra包装Gorgon Halo — AMD Ryzen AI Max + Pro 495出现在迷你工作站中" data-date="09-04 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">联想ThinkCentre X Ultra包装Gorgon Halo — AMD Ryzen AI Max + Pro 495出现在迷你工作站中</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/nvidias-rtx-spark-n1x-launches-in-october-for-laptops-and-desktops-18-or-20-cpu-cores-paired-with-5-120-or-6-144-cuda-cores-up-to-128gb-of-unified-memory" target="_blank" rel="noopener" data-cat="keji" data-summary="采用英伟达RTX Spark N1X芯片的系统将于10月份在迷你PC和笔记本电脑上推出，芯片有两种配置。" data-title="英伟达的RTX Spark N1X于10月推出，适用于笔记本电脑和台式机— 18或20个CPU内核，配有5,120或6,144个CUDA内核，高达128GB的统一内存" data-date="09-04 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">英伟达的RTX Spark N1X于10月推出，适用于笔记本电脑和台式机— 18或20个CPU内核，配有5,120或6,144个CUDA内核，高达128GB的统一内存</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达的个人AI路由器（ PAIR ）集群实用程序使代理AI工作负载能够利用家庭网络上的每个备用GPU周期，从而实现更快的执行和更私密的推理。" data-title="Nvidia PAIR实用程序将家庭中的每个GPU连接到一个集群中，以执行代理AI任务—该工具使用备用周期来防止代理群撞击一个GPU" data-date="09-04 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">Nvidia PAIR实用程序将家庭中的每个GPU连接到一个集群中，以执行代理AI任务—该工具使用备用周期来防止代理群撞击一个GPU</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔的酷睿超400系列“Nova Lake-S” CPU有望在下个季度量产，但它们将仅在2027年第一季度推出， 28核型号将排在第一位。" data-title="英特尔Core Ultra 400 “Nova Lake”发布时间表泄露—第四季度量产， 2027年第一季度首批Nova Lake CPU" data-date="09-03 23:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-03 23:58</span>
          <span class="news-item-title">英特尔Core Ultra 400 “Nova Lake”发布时间表泄露—第四季度量产， 2027年第一季度首批Nova Lake CPU</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/how-to-install-a-ps5-ssd-in-2026" target="_blank" rel="noopener" data-cat="keji" data-summary="了解如何在五分钟内在PlayStation 5、PlayStation 5 Slim或PlayStation 5 Pro中安装M.2 NVMe SSD。" data-title="2026 年如何安装 PS5 SSD" data-date="09-03 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-03 23:30</span>
          <span class="news-item-title">2026 年如何安装 PS5 SSD</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/985009/tecno-bezelless-concept-phone-ifa" target="_blank" rel="noopener" data-cat="keji" data-summary="回想十年左右的时间，智能手机制造商痴迷于缩小手机的挡板。屏幕越来越大，周围的黑条越来越小，有一段时间，它看起来像真正的边缘到边缘显示迫在眉睫。然后，进度就停止了。表圈缩小到1毫米或[…]" data-title="我拿着第一个真正的挡板" data-date="09-04 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">我拿着第一个真正的挡板</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/988517/circular-ring-3-pro-slim-nfc-contactless-payment-vibrating-alerts" target="_blank" rel="noopener" data-cat="keji" data-summary="Circular 今天宣布推出新的 Ring 3 系列，作为在 CES 2025 上首次亮相的 Ring 2 的后续产品，配备升级的传感器和 FDA 批准的心房颤动检测。新的 Ring 3 系列包括一个 Pro 型号，它继承了相同的健康跟踪功能，以及一个较小的 Slim 选项，提供更有限的 […]" data-title="Circular的新智能戒指增加了非接触式支付和振动警报" data-date="09-04 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">Circular的新智能戒指增加了非接触式支付和振动警报</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/988734/moto-watch-ultra-release-date-price-specs-wear-os-ifa" target="_blank" rel="noopener" data-cat="keji" data-summary="在重返智能手表市场几个月后，摩托罗拉推出了首款Moto Watch Ultra ，瞄准了高端市场。它配备了最近的Moto Watch的一些升级-最明显的是跳转到Wear OS -但缺乏户外功能，使其成为[…]" data-title="Moto Watch Ultra是Wear OS的回归" data-date="09-04 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">Moto Watch Ultra是Wear OS的回归</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/988765/lenovo-ideapad-vibe-laptop-macbook-neo-competitor-ifa-colors-price-specs" target="_blank" rel="noopener" data-cat="keji" data-summary="联想宣布推出IdeaPad Vibe ，这是一款生产力笔记本电脑，旨在以相似的起价和更广泛的颜色推出MacBook Neo。Vibe有14英寸和15英寸的尺寸， AMD和高通的芯片选项分别定于10月和11月推出。英特尔版本（可能是Wildcat Lake ）设置为[…]" data-title="联想的新款 MacBook Neo 竞争对手有两种尺寸和七种颜色" data-date="09-04 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-04 00:00</span>
          <span class="news-item-title">联想的新款 MacBook Neo 竞争对手有两种尺寸和七种颜色</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ce87v0e868qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="过去有句老话说，英国球员的价值很高。现在这似乎只适用于已经在英超联赛中的球员。" data-title="英超联赛的溢价为 2000 万英镑——这让欧洲俱乐部感到担忧" data-date="09-03 19:13" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 19:13</span>
          <span class="news-item-title">英超联赛的溢价为 2000 万英镑——这让欧洲俱乐部感到担忧</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ce87vzgyzd9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据信，切尔西今年夏天通过出售或租借多达 39 名球员，收回了超过 5 亿英镑的收入。" data-title="解析切尔西夏季 39 场令人震惊的出局" data-date="09-04 00:20" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 00:20</span>
          <span class="news-item-title">解析切尔西夏季 39 场令人震惊的出局</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgjql4w604eo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英超裁判迈克·迪恩表示，在比赛期间，他会尽可能长时间地留在中圈。" data-title="我过去常常玩比赛游戏来搞笑——迪恩" data-date="09-03 19:45" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 19:45</span>
          <span class="news-item-title">我过去常常玩比赛游戏来搞笑——迪恩</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c14dx8eze1do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="主教练安多尼·伊拉奥拉讨论了利物浦的转会业务、布拉德利·巴克拉的到来以及留住科迪·加克波。" data-title="伊劳拉对签约感到满意，巴可拉即将首次亮相" data-date="09-03 18:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 18:58</span>
          <span class="news-item-title">伊劳拉对签约感到满意，巴可拉即将首次亮相</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/czdz349nyl7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="老鹰队主教练皮埃尔·萨奇表示，水晶宫前锋伊斯梅拉·萨尔需要时间来应对他转会利物浦计划的失败。" data-title="萨尔需要时间来处理利物浦转会失败的问题" data-date="09-03 23:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 23:05</span>
          <span class="news-item-title">萨尔需要时间来处理利物浦转会失败的问题</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/03/deadline-day-deals-premier-league-transfers" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这名 18 岁的球员曾参加过两场大型国际赛事，是上赛季该分区的顶级解围者，也是一名狡猾、令人兴奋、快速且多才多艺的中场球员，阿齐兹在过去两个赛季随米尔沃尔在英冠联赛中证明了自己，现在值得有机会在顶级联赛中检验自己。继续阅读..." data-title="阿齐兹对安德烈斯：七个看起来很聪明的英超联赛截止日交易" data-date="09-03 17:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-03 17:00</span>
          <span class="news-item-title">阿齐兹对安德烈斯：七个看起来很聪明的英超联赛截止日交易</span>
        </a>
        <a class="news-item" href="https://arstechnica.com/information-technology/2026/09/vmware-migration-reduces-tottenham-hotspurs-licensing-fees-by-85-percent/" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="职业足球队的首席技术官指出了“博通收购问题”。" data-title="VMware迁移将Tottenham Hotspur的许可费降低了85%" data-date="09-04 02:58" data-source="Ars Technica">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-arstechnica">🔬 Ars Technica</span>
          <span class="news-item-date">09-04 02:58</span>
          <span class="news-item-title">VMware迁移将Tottenham Hotspur的许可费降低了85%</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq5xl575q7no?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳边锋加布里埃尔·马丁内利以 6000 万英镑加盟沙特职业联赛球队阿尔希拉尔。" data-title="阿森纳球星马蒂内利加盟阿尔" data-date="09-04 00:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 00:30</span>
          <span class="news-item-title">阿森纳球星马蒂内利加盟阿尔</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c62j5lkjg74o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）与卡萨比亚（ Kasabian ）主唱塞尔日·皮佐尔诺（ Serge Pizzorno ）以及英国广播公司（ BBC ）的读者和人工智能（ AI ）进行了对本周末英" data-title="萨顿对 Kasabian 主唱 Serge Pizzorno 的预测" data-date="09-04 03:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 03:58</span>
          <span class="news-item-title">萨顿对 Kasabian 主唱 Serge Pizzorno 的预测</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ce87v0e868qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="过去的格言是英格兰球员溢价。现在，这似乎只适用于已经在英超联赛中的球员。" data-title="英超联赛的溢价为2000万英镑，这让欧洲俱乐部感到担忧" data-date="09-03 19:13" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 19:13</span>
          <span class="news-item-title">英超联赛的溢价为2000万英镑，这让欧洲俱乐部感到担忧</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c07lk45y3ego?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="摩根·吉布斯-怀特（ Morgan Gibbs-White ）被排除在英格兰世界杯阵容之外-托马斯·图切尔（ Thomas Tuchel ）是否无法忽视他的持续良好状态？" data-title="“Adonis” Gibbs-White闪耀的机会- Tuchel会注意到吗？" data-date="09-04 01:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 01:07</span>
          <span class="news-item-title">“Adonis” Gibbs-White闪耀的机会- Tuchel会注意到吗？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgjql4w604eo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英超联赛裁判迈克·迪恩（ Mike Dean ）表示，他将在比赛中尽可能长时间地留在中场。" data-title="我过去常常笑着玩比赛- Dean" data-date="09-03 19:45" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 19:45</span>
          <span class="news-item-title">我过去常常笑着玩比赛- Dean</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cp301d314xyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育FPL专家吉安尼·巴蒂斯（ Gianni Buttice ）研究了幻想英超联赛经理在进入第三周比赛时面临的一些最大困境。" data-title="谁是曼城最适合购买的球员？ FPL游戏周三难题" data-date="09-04 14:15" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 14:15</span>
          <span class="news-item-title">谁是曼城最适合购买的球员？ FPL游戏周三难题</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c14dx8eze1do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理Andoni Iraola讨论了利物浦的转会业务、Bradley Barcola的到来以及Cody Gakpo的留任。" data-title="Iraola对签约感到高兴，因为Barcola即将首次亮相" data-date="09-03 18:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 18:58</span>
          <span class="news-item-title">Iraola对签约感到高兴，因为Barcola即将首次亮相</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/998/179.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 3 日消息，英特尔 Graphics Software 32.0.101.8992 显卡驱动（适用于 Arc）今日发布。本次为 Non-WHQL 测试版本，为英特尔 Arc B 系列、A 系列独立显卡以及英特尔酷睿 Ultra 系列集成 Arc 核显提供支持，新增两款新游戏支持，修复了多款游戏存在的画面异常问题。IT之家附官方公告链接（https://www.intel.com/content/www/us/en/download/785597/intel-arc-graphics-windows.html）。新游戏支持与性能优化为《鬼武者：剑之道》提供支持为《黎明行者之血》提供支持问题修复修复《失落星船：马拉松》（DX12）在各产品线中，使用各向异性过滤时游戏过程中部分物" data-title="英特尔 Arc 显卡驱动 32.0.101.8992 测试版发布：支持两款新游戏，修复多款游戏画面异常问题" data-date="09-03 22:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-03 22:20</span>
          <span class="news-item-title">英特尔 Arc 显卡驱动 32.0.101.8992 测试版发布：支持两款新游戏，修复多款游戏画面异常问题</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crm93nv8n7yo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="利兹联队主教练丹尼尔·法克表示，中后卫乔·罗登由于“严重的腿筋受伤”将缺席八到十周。" data-title="利兹联队球员罗登因腿筋受伤将缺席长达 10 周" data-date="09-03 22:39" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 22:39</span>
          <span class="news-item-title">利兹联队球员罗登因腿筋受伤将缺席长达 10 周</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/clyeq3v7829o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="赫尔城批评新援罗比尼奥·瓦兹在宣布签约时受到“令人憎恶的种族主义辱骂”。" data-title="对新签约瓦兹的种族主义虐待令人憎恶" data-date="09-03 18:28" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-03 18:28</span>
          <span class="news-item-title">对新签约瓦兹的种族主义虐待令人憎恶</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-04/10689974.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="西藏日喀则市吉隆县泥石流灾害发生后，应急管理部迅速调派中央企业工程应急救援力量796人、522台(套)装备驰援西藏，在现场指挥部统一指挥下，协同开展排查搜救、道路抢通、风险监测等抢险救援工作。此外，中交集团、中国中铁还选派7名隧道专家赴尼泊尔灾区协助开展隧道救援工作。" data-title="应急管理部调派央企力量全力支持吉隆泥石流灾害抢险救援" data-date="09-04 00:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-04 00:03</span>
          <span class="news-item-title">应急管理部调派央企力量全力支持吉隆泥石流灾害抢险救援</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/ty/2026/09-03/10689973.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社深圳9月3日电 (记者 张璐 索有为)正在深圳举行的2026李宁·中国羽毛球大师赛9月3日结束第二轮较量，男单世界第一、印尼选手乔纳坦以0:2不敌中国香港选手吴英伦，爆冷出局；中国混双组合冯彦哲/黄东萍以2:1逆转战胜泰国组合帕克卡波/沙西丽。" data-title="中国羽毛球大师赛：男单世界第一乔纳坦爆冷出局" data-date="09-03 23:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 23:59</span>
          <span class="news-item-title">中国羽毛球大师赛：男单世界第一乔纳坦爆冷出局</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-03/10689972.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社广州9月3日电 (记者 王坚)受台风“沙德尔”影响，9月2日以来，粤东等地出现一轮强降雨过程。广东省水利厅3日晚通报称，广东韩江高陂水利枢纽(广东梅州)当日18时入库流量涨至4850立方米每秒，依据主要江河洪水编号规定，此次洪水编号为“韩江2026年第1号洪水”。" data-title="粤东持续强降雨 韩江发生2026年第1号洪水" data-date="09-03 23:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 23:29</span>
          <span class="news-item-title">粤东持续强降雨 韩江发生2026年第1号洪水</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/ty/2026/09-03/10689971.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月3日电 2026京西国际山地户外季新闻发布会2日举行。据了解，本次户外季活动将推出覆盖徒步、越野、自行车三大门类的六项高水平赛事，预计吸引上万名户外运动爱好者参与。" data-title="2026京西国际山地户外季包含六大赛事" data-date="09-03 23:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 23:21</span>
          <span class="news-item-title">2026京西国际山地户外季包含六大赛事</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-03/10689970.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社西藏吉隆9月3日电 题：西藏吉隆泥石流灾害核心区见闻：科技助力搜寻，护航救援" data-title="西藏吉隆泥石流灾害核心区见闻：科技助力搜寻，护航救援" data-date="09-03 23:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 23:20</span>
          <span class="news-item-title">西藏吉隆泥石流灾害核心区见闻：科技助力搜寻，护航救援</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-03/10689969.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="通往吉隆口岸的路，通了。" data-title="每一分钟仿佛都长得不止60秒(记者手记)" data-date="09-03 23:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 23:08</span>
          <span class="news-item-title">每一分钟仿佛都长得不止60秒(记者手记)</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-03/10689968.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月3日电 (记者 孙自法)甘肃地区位于中国黄土高原、青藏高原、蒙古高原三大地理单元交汇地带，在亚欧史前交流特别是农牧业交流进程中扮演了重要的枢纽角色。" data-title="史前甘肃人群为何形成独特遗传演化和社会结构？古基因组研究揭示" data-date="09-03 23:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-03 23:01</span>
          <span class="news-item-title">史前甘肃人群为何形成独特遗传演化和社会结构？古基因组研究揭示</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/us/politics/gloria-steinem-dead.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="她挑战了性别歧视的假设，帮助女性发展自我价值感，并在工作、家庭和整个社会中获得一定程度的平等。" data-title="格洛丽亚·斯泰纳姆（ Gloria Steinem ） ，女权运动的化身， 92岁去世" data-date="09-03 22:39" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-03 22:39</span>
          <span class="news-item-title">格洛丽亚·斯泰纳姆（ Gloria Steinem ） ，女权运动的化身， 92岁去世</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/books/review/gloria-steinem-writing-appraisal.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="她1983年的著作《令人发指的行为和日常叛乱》（ Outrageous Acts and Everyday Rebellions ）是一门关于勇气、同理心、好奇心和喧嚣的大师班。" data-title="格洛丽亚·斯泰纳姆（ Gloria Steinem ）来到纽约成为一名作家。她变成了一场运动。" data-date="09-03 23:26" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-03 23:26</span>
          <span class="news-item-title">格洛丽亚·斯泰纳姆（ Gloria Steinem ）来到纽约成为一名作家。她变成了一场运动。</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/03/style/gloria-steinem-style-feminism.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="眼镜、发型、铃铛裤和腰带都包裹在她的女权主义事业中。" data-title="格洛丽亚·斯泰纳姆（ Gloria Steinem ）的魅力是达到目的的手段" data-date="09-03 21:46" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-03 21:46</span>
          <span class="news-item-title">格洛丽亚·斯泰纳姆（ Gloria Steinem ）的魅力是达到目的的手段</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/989962/steve-ballmer-kawhi-leonard-pablo-torre-finds-out" target="_blank" rel="noopener" data-cat="zonghe" data-summary="去年九月，史蒂夫·鲍尔默在接受 ESPN 采访时坚称，快船队并没有参与为他的明星球员科怀·伦纳德提供的看似可疑的 2800 万美元代言交易，该交易没有涉及任何实际代言。现在，这位前微软首席执行官已被 NBA 停赛一年，而联盟表示他的球队将失去五名 [...]" data-title="史蒂夫·鲍尔默因播客和大屏幕腐败丑闻被 NBA 停赛" data-date="09-04 07:37" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-04 07:37</span>
          <span class="news-item-title">史蒂夫·鲍尔默因播客和大屏幕腐败丑闻被 NBA 停赛</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/989880/dungeons-and-dragons-ravenloft-netflix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据 Deadline 报道，执行制片人阿方索·卡隆、编剧兼执行制片人约翰·奥古斯特以及孩之宝娱乐公司目前正在开发《Ravenloft》系列。它可以使《龙与地下城》最具标志性的战役设定之一变得栩栩如生，该设定在今年早些时候的《Ravenloft: The Horrors Within》中得到了更新。据报道，Netflix 的《Ravenloft》系列将以 [...]" data-title="《龙与地下城》将推出 Netflix 真人剧集《Ravenloft》" data-date="09-04 04:48" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-04 04:48</span>
          <span class="news-item-title">《龙与地下城》将推出 Netflix 真人剧集《Ravenloft》</span>
        </a>
  </div>
</div>

<script>
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
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'flex' : 'block') : 'none';
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


---

<p class="news-updated">🕐 抓取更新于 2026-09-04 16:03（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
