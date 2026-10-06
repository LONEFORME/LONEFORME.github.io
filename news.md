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
      <span>2026-10-06 16:14 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×19 · IT之家×14</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-06/10708446.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="央视网消息(焦点访谈)：民心所向是长征胜利的力量源泉，长征路上，红军与群众同心同向，发生了很多感人至深的故事。“半条被子”的故事发生在1934年11月，在湖南汝城县沙洲村，3名女红军借宿在村民家。临走时，她们把仅有的一条被子剪下一半，留给了这位村民。" data-title="焦点访谈｜“半条被子” 映初心 长征精神启新程" data-date="10-06 15:49" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-06 15:49</span>
      </div>
      <h2 class="hero-featured-title">焦点访谈｜“半条被子” 映初心 长征精神启新程</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/010/007.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，OPPO 现已在印度市场推出 F35 5G/F35 Pro 5G 手机，新品定位中低端市场，采用 8000mAh 大电池，以及天玑 6360 Max/7360 Max 芯片，起售价为 38,999 卢比（IT之家注：现汇率约合 2,725 元人民币）。据介绍，OPPO F35 5G 手机搭载 6.57 英寸 AMOLED 屏幕，分辨率为 2372×1080，支持 120Hz 高刷，亮度可达 800nits。配备联发科天玑 6360 Max 芯片，提供 6GB/8GB 内存以及 128GB 存储空间，具备 4300mm² 大面积 VC 液冷散热。同时，该手机拥有 5000 万像素后置主摄和 200 万像素黑白辅助镜头，前置 5000 万像素自拍镜头。拥有 800" data-title="OPPO 推出 F35 5G 系列手机：8000mAh 电池，天玑 6360 Max/7360 Max 芯片" data-date="10-06 15:55" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">OPPO 推出 F35 5G 系列手机：8000mAh 电池，天玑 6360 Max/7360 Max 芯片</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/955.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 6 日消息，几天之前，OpenAI 指责苹果在商业秘密诉讼当中违规提交新证据。如今苹果予以反击，反过来指控 OpenAI 在其提交的回应中超出了法院规则允许的范围。据IT之家了解，这起诉讼由苹果发起，起诉两名前员工（刘畅〔Chang Liu〕、谭唐〔Tang Tan〕）、OpenAI 以及 io Products 涉嫌盗用商业秘密。案件当中的一项核心诉求，是申请一项临时禁令。简单来说，苹果请求法院颁布临时禁令。苹果的理由是，在案件审理期间，需要阻止自家的商业秘密进一步融入 OpenAI 的硬件开发工作。围绕这项禁令申请展开的多轮法律交锋过程中，苹果提交了一份答辩法律意见书，并附带五份专家书面证言作为支撑。此举随即招致几名被告的指责，被告方认为苹果违规引入新证据，请求法庭对" data-title="苹果与 OpenAI 商业秘密诉讼交锋升级：互指违规提交新证据" data-date="10-06 09:59" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">苹果与 OpenAI 商业秘密诉讼交锋升级：互指违规提交新证据</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1004820/this-remote-controlled-wagon-is-silly-but-useful" target="_blank" rel="noopener" data-cat="zonghe" data-summary="忏悔：当BougeRV告诉我其带有动画照明的遥控车时，我打电话给它取笑，希望在评论中剔除它。可以肯定的是，这太荒谬了。但沙丘漫游者也被证明是非常强大的，有足够的扭矩" data-title="This remote-controlled wagon is silly but so very useful" data-date="10-06 16:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">This remote-controlled wagon is silly but so very useful</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708446.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="央视网消息(焦点访谈)：民心所向是长征胜利的力量源泉，长征路上，红军与群众同心同向，发生了很多感人至深的故事。“半条被子”的故事发生在1934年11月，在湖南汝城县沙洲村，3名女红军借宿在村民家。临走时，她们把仅有的一条被子剪下一半，留给了这位村民。" data-title="焦点访谈｜“半条被子” 映初心 长征精神启新程" data-date="10-06 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 15:49</span>
          <span class="news-item-title">焦点访谈｜“半条被子” 映初心 长征精神启新程</span>
          <span class="news-value-point">💡 央视网消息(焦点访谈)：民心所向是长征胜利的力量源泉，长征路上，红军与群众同心同向，发生了很多感人至深的故事</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708445.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="平凡岗位，不凡坚守。国庆假期，重大工程现场机械轰鸣，民生保障持续稳定……千千万万劳动者用汗水建设家园，以实干再立新功。" data-title="坚守岗位践初心 实干担当立新功" data-date="10-06 15:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 15:47</span>
          <span class="news-item-title">坚守岗位践初心 实干担当立新功</span>
          <span class="news-value-point">💡 平凡岗位，不凡坚守</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708423.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月6日电 当地时间10月5日，日本首相高市早苗在国会发表施政演说(所信表明演说)，演说引发广泛批评。日本舆论认为，其演说内容空洞无物，轻视民生。还有日本民众表示，对高市的系列政策深感不安。" data-title="高市早苗施政演说遭多方批评：空洞无物，忽视民生" data-date="10-06 14:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 14:00</span>
          <span class="news-item-title">高市早苗施政演说遭多方批评：空洞无物，忽视民生</span>
          <span class="news-value-point">💡 中新网10月6日电 当地时间10月5日，日本首相高市早苗在国会发表施政演说(所信表明演说)，演说引发广泛批评</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708415.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月6日电 据中国驻沙特大使馆微信公众号消息，10月6日凌晨，沙特内政部用多语种发布紧急公告称：拍摄、发布或传播与拦截导弹和无人机以及其坠落地点相关的信息，将使您面临法律追责。" data-title="中国驻沙特使馆提醒在沙机构和公民注意安全并遵守当地法律" data-date="10-06 13:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 13:47</span>
          <span class="news-item-title">中国驻沙特使馆提醒在沙机构和公民注意安全并遵守当地法律</span>
          <span class="news-value-point">💡 中新网10月6日电 据中国驻沙特大使馆微信公众号消息，10月6日凌晨，沙特内政部用多语种发布紧急公告称：拍摄、发布或传播与拦截导弹和无人机以及其…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708409.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海10月6日电 (陈静 曹乃文)记者6日获悉，国庆假期进入尾声，跨境出游旅客陆续返程，客流由前期“出境热”逐渐转向“返程热”。上海口岸迎来返程客流高峰。" data-title="上海口岸迎来返程客流高峰" data-date="10-06 13:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 13:46</span>
          <span class="news-item-title">上海口岸迎来返程客流高峰</span>
          <span class="news-value-point">💡 中新网上海10月6日电 (陈静 曹乃文)记者6日获悉，国庆假期进入尾声，跨境出游旅客陆续返程，客流由前期“出境热”逐渐转向“返程热”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708406.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月6日电 据俄罗斯卫星通讯社报道，俄罗斯首都莫斯科市市长索比亚宁表示，自当地时间5日20时30分至6日5时，共有650架乌克兰无人机飞往莫斯科地区方向，大部分无人机被俄防空部队在远距离击落。" data-title="多达650架 俄罗斯首都遭乌克兰大规模无人机袭击" data-date="10-06 13:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 13:19</span>
          <span class="news-item-title">多达650架 俄罗斯首都遭乌克兰大规模无人机袭击</span>
          <span class="news-value-point">💡 中新网10月6日电 据俄罗斯卫星通讯社报道，俄罗斯首都莫斯科市市长索比亚宁表示，自当地时间5日20时30分至6日5时，共有650架乌克兰无人机飞…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/979.htm" target="_blank" rel="noopener" data-cat="shizheng" data-summary="IT之家 10 月 6 日消息，据路透社报道，公开档案显示，意大利总理焦尔吉娅 · 梅洛尼已经向欧盟知识产权局（EUIPO）提交申请，希望将自己的声音注册成为商标，以此防范由 AI 生成的深度伪造内容。图源：梅洛尼 X 账号欧盟知识产权局网站上这份申请的日期为 10 月 5 日，梅洛尼办公室也证实了该申请。申请材料当中附带一段时长 4 秒的录音，录音里她用意大利语重复说了两遍：“我是焦尔吉娅 · 梅洛尼。”“Io sono Giorgia（我是焦尔吉娅）”正是她 2021 年自传的书名。这句话源自梅洛尼 2019 年在一场政治集会上的著名发言，甚至还曾经被改编成迪斯科舞曲。近些年来，经过篡改的梅洛尼影像多次在网络上流传，部分还被网友当作真实内容转发。其中就有一张伪造图片，画面当中的她身着内衣" data-title="为防范 AI 深度伪造，意大利总理梅洛尼申请将自己的声音注册为商标" data-date="10-06 12:58" data-source="IT之家">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 12:58</span>
          <span class="news-item-title">为防范 AI 深度伪造，意大利总理梅洛尼申请将自己的声音注册为商标</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，据路透社报道，公开档案显示，意大利总理焦尔吉娅 · 梅洛尼已经向欧盟知识产权局（EUIPO）提交申请，希望将自己…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/05/us/politics/iran-drone-attack-threat.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据美国和英国官员称，由于伊朗伊斯兰革命卫队下令进行无人机袭击的风险，来自费尔福德空军基地的12架B-1空军轰炸机被撤回。" data-title="Potential Iranian Drone Attack Led to Exit of U.S. Aircraft From British Air Base" data-date="10-06 12:18" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-06 12:18</span>
          <span class="news-item-title">潜在的伊朗无人机袭击导致美国飞机从英国空军基地撤离</span>
          <span class="news-item-title-en">Potential Iranian Drone Attack Led to Exit of U.S. Aircraft From British Air Base</span>
          <span class="news-value-point">💡 据美国和英国官员称，由于伊朗伊斯兰革命卫队下令进行无人机袭击的风险，来自费尔福德空军基地的12架B-1空军轰炸机被撤回</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/06/world/europe/france-crisis-autumn-discontent.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="学校、街头和市场的混乱源于法国为社会福利国家提供资金的斗争，总统选举即将到来。" data-title="Strikes, Barricades and Fiscal Turmoil: An Autumn of Discontent Grips France" data-date="10-06 12:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-06 12:01</span>
          <span class="news-item-title">罢工、路障和财政动荡：法国的不满之秋</span>
          <span class="news-item-title-en">Strikes, Barricades and Fiscal Turmoil: An Autumn of Discontent Grips France</span>
          <span class="news-value-point">💡 学校、街头和市场的混乱源于法国为社会福利国家提供资金的斗争，总统选举即将到来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708377.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月6日电 综合消息：当地时间5日，也门政府宣布启动“也门黎明”行动，沙特阿拉伯主导的多国联军当天出动战机空袭胡塞武装目标，也门政府军向红海沿岸推进。作为回应，胡塞武装同日袭击沙特境内多个目标，并警告国际航空公司停止飞越沙特领空。" data-title="沙特主导联军空袭胡塞武装遭反击" data-date="10-06 11:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 11:48</span>
          <span class="news-item-title">沙特主导联军空袭胡塞武装遭反击</span>
          <span class="news-value-point">💡 中新社北京10月6日电 综合消息：当地时间5日，也门政府宣布启动“也门黎明”行动，沙特阿拉伯主导的多国联军当天出动战机空袭胡塞武装目标，也门政府…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708376.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月6日电 题：短剧《过海》折射两岸同胞“双向奔赴”" data-title="评论：短剧《过海》折射两岸同胞“双向奔赴”" data-date="10-06 11:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 11:13</span>
          <span class="news-item-title">评论：短剧《过海》折射两岸同胞“双向奔赴”</span>
          <span class="news-value-point">💡 中新社北京10月6日电 题：短剧《过海》折射两岸同胞“双向奔赴”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-06/10708373.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社纽约10月5日电 (记者 王帆)美国纽约州州长凯茜·霍楚尔当地时间5日签署一项行政令，宣布该州因麻疹疫情进入灾难紧急状态，为期一个月。" data-title="美国纽约州因麻疹疫情进入灾难紧急状态" data-date="10-06 11:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 11:11</span>
          <span class="news-item-title">美国纽约州因麻疹疫情进入灾难紧急状态</span>
          <span class="news-value-point">💡 中新社纽约10月5日电 (记者 王帆)美国纽约州州长凯茜·霍楚尔当地时间5日签署一项行政令，宣布该州因麻疹疫情进入灾难紧急状态，为期一个月</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708359.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网南宁10月6日电(周祥 李志农 林浩)10月6日，广西壮族自治区农业机械化服务中心介绍，广西“滴滴农机”平台自2025年10月试运行以来，推动农机服务进入数字化新阶段，截至2026年9月底，平台注册用户超9000人，接入远程监测北斗农机终端超1.75万台，促成农机作业面积62万余亩。" data-title="广西“滴滴农机”接入北斗终端超1.75万台 作业面积62万余亩" data-date="10-06 11:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 11:03</span>
          <span class="news-item-title">广西“滴滴农机”接入北斗终端超1.75万台 作业面积62万余亩</span>
          <span class="news-value-point">💡 中新网南宁10月6日电(周祥 李志农 林浩)10月6日，广西壮族自治区农业机械化服务中心介绍，广西“滴滴农机”平台自2025年10月试运行以来，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-06/10708372.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社联合国10月5日电 中国常驻联合国副代表孙磊5日针对少数国家在联大第三委员会一般性辩论中恶意诋毁中国人权状况作答辩发言，指出这些国家自以为高人一等，动辄摆出一副“人权教师爷”的做派，但其国内人权问题突出，根本没有资格奢谈人权，更无权对中国说三道四。" data-title="中国代表驳斥少数国家诋毁中国人权状况" data-date="10-06 11:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 11:01</span>
          <span class="news-item-title">中国代表驳斥少数国家诋毁中国人权状况</span>
          <span class="news-value-point">💡 中新社联合国10月5日电 中国常驻联合国副代表孙磊5日针对少数国家在联大第三委员会一般性辩论中恶意诋毁中国人权状况作答辩发言，指出这些国家自以为…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708362.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="由公安部和中央广播电视总台联合摄制的纪录片《缅北电诈覆灭纪实》于10月5日至7日，在央视综合频道18点档首播。纪录片全面展现了在党中央坚强领导下，我国公安机关会同有关部门开展打击缅北涉我犯罪专项工作，彻底铲除缅北“四大家族”等犯罪集团的艰苦历程和显著成就。" data-title="缅北电诈主犯随机杀人祭天、有受害者头骨7个弹孔 案件细节曝光" data-date="10-06 10:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 10:24</span>
          <span class="news-item-title">缅北电诈主犯随机杀人祭天、有受害者头骨7个弹孔 案件细节曝光</span>
          <span class="news-value-point">💡 由公安部和中央广播电视总台联合摄制的纪录片《缅北电诈覆灭纪实》于10月5日至7日，在央视综合频道18点档首播</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
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
        <a class="news-item" href="https://www.ithome.com/1/009/971.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，据彭博社报道，知情人士消息，月之暗面（Moonshot AI）已经完成上市前最后一轮私募融资，估值约 500 亿美元（IT之家注：现汇率约合 3,357.23 亿元人民币）；该公司计划于明年第一季度在香港进行首次公开募股（IPO）。部分知情人士称，这家国内头部人工智能企业已经开始筹备投资者摸底沟通，最早将于本月就开展先期意向会议，以此评估资本市场态度。月之暗面是中国 AI 赛道当中最受瞩目的企业之一。今年 7 月，Kimi K3 开源大模型正式发布，一举站上全球舞台；在多项评测指标上，该模型几乎可以同 OpenAI、Anthropic 的头部模型相抗衡。其 IPO 也成为港股市场最受期待的交易项目之一。眼下 AI 驱动的新股融资活动正在香港接连刷新纪录。知情人" data-title="消息称月之暗面完成上市前最后一轮融资：估值约 500 亿美元，计划明年一季度赴港 IPO" data-date="10-06 11:38" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 11:38</span>
          <span class="news-item-title">消息称月之暗面完成上市前最后一轮融资：估值约 500 亿美元，计划明年一季度赴港 IPO</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，据彭博社报道，知情人士消息，月之暗面（Moonshot AI）已经完成上市前最后一轮私募融资，估值约 500 亿…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/961.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，据彭博社报道，知情人士透露，OpenAI 正在与来自阿联酋的多家投资基金（总部位于阿布扎比的 MGX 也在其中）展开磋商，希望由这些基金作为基石投资方，助力这家 ChatGPT 开发商完成一轮规模 300 亿美元（IT之家注：现汇率约合 2,014.34 亿元人民币）的融资。其中一位知情人士称，这些阿联酋基金将会组建投资财团参与本轮融资。另有消息表示，几家阿联酋基金合计的出资规模最高可能达到 100 亿美元（现汇率约合 671.45 亿元人民币）。知情人士还称，贝莱德集团（BlackRock Inc.）也正在洽谈，计划随同该财团一同参与本轮融资。知情人士同时表示，本轮融资仍在推进过程中，各项细节仍有可能发生变动。据彭博社此前报道，OpenAI 计划至少募资 3" data-title="消息称 OpenAI 洽谈 300 亿美元融资，阿联酋基金、贝莱德入局磋商" data-date="10-06 10:29" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 10:29</span>
          <span class="news-item-title">消息称 OpenAI 洽谈 300 亿美元融资，阿联酋基金、贝莱德入局磋商</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，据彭博社报道，知情人士透露，OpenAI 正在与来自阿联酋的多家投资基金（总部位于阿布扎比的 MGX 也在其中）…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/960.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，综合 CNBC 与《金融时报》报道，Groq 当地时间本周二被告上美国特拉华州衡平法院，被指控在与 NVIDIA（英伟达）的“类收购”非独家授权交易中牺牲了少数股东的权益。原告 Joshua Rubin 和 Benjamin Serebrin 曾是 Groq 的员工，但在与 NVIDIA 的交易前离职。两位员工仍持有 Groq 的股份。根据披露的诉讼文件，Groq 与 NVIDIA 的 200 亿美元（IT之家注：现汇率约合 1,342.89 亿元人民币）交易分为 2 个部分：170 亿美元由所有持股者共享，另外 30 亿美元以 NVIDIA 限售股的形式被分给跳槽 NVIDIA 的 Groq 员工。原告方认为 Groq 董事会存在严重的利益冲突，未能履行其为" data-title="Groq 遭起诉：被控与英伟达 200 亿美元“类收购”交易牺牲少数股东权益" data-date="10-06 10:18" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 10:18</span>
          <span class="news-item-title">Groq 遭起诉：被控与英伟达 200 亿美元“类收购”交易牺牲少数股东权益</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，综合 CNBC 与《金融时报》报道，Groq 当地时间本周二被告上美国特拉华州衡平法院，被指控在与 NVIDIA…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/958.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 6 日消息，科技媒体 Windows Central 昨日（10 月 5 日）发布博文，报道称在 Word 文档处理应用中，微软优化 Copilot AI 体验，新增引用功能，帮助用户溯源遏制 AI 幻觉。信息引用方面，Copilot 回复现在会附带来源链接，用户可直接点击跳转至原始网页或内部文档，核实信息上下文与准确性。微软表示，此举提高了透明度，帮助用户理解 Copilot 信息的出处。IT之家附上相关截图如下：AI 工具常因训练数据滞后或语境误读而输出错误结论，甚至编造看似真实的来源，业内也将其称为“幻觉”。引用功能允许用户快速回溯原始材料，确认 Copilot 是否正确提取并理解了信息。微软同时优化了 Copilot Chat 的设计与功能，并为 Copilot" data-title="防止 AI 胡编乱造：微软 Word Copilot 新增引用功能，可溯源查证" data-date="10-06 10:12" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 10:12</span>
          <span class="news-item-title">防止 AI 胡编乱造：微软 Word Copilot 新增引用功能，可溯源查证</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，科技媒体 Windows Central 昨日（10 月 5 日）发布博文，报道称在 Word 文档处理应用中，…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/its-finally-a-good-time-to-buy-a-raptor-lake-cpu-during-prime-big-deals-day-chips-drop-to-all-time-low-prices-as-inventory-seemingly-stabilizes" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔的第14代Raptor Lake Refresh CPU在经历了一年不一致的价格后，终于获得了一些不错的折扣，其中一些芯片甚至跌至历史最低点。" data-title="It&#39;s finally a good time to buy a Raptor Lake CPU during Prime Big Deals Day" data-date="10-06 07:25" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 07:25</span>
          <span class="news-item-title">终于在Prime Big Deals Day购买Raptor Lake CPU的好时机了</span>
          <span class="news-item-title-en">It's finally a good time to buy a Raptor Lake CPU during Prime Big Deals Day</span>
          <span class="news-value-point">💡 英特尔的第14代Raptor Lake Refresh CPU在经历了一年不一致的价格后，终于获得了一些不错的折扣，其中一些芯片甚至跌至历史最低…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1005177/google-gemini-call-for-me-expansion-rumors" target="_blank" rel="noopener" data-cat="keji" data-summary="Google可能会将其“Call for Me”人工智能功能扩展到商务电话之外，以便您可以使用它向亲朋好友发送消息。Android Authority报告在APK拆解中找到“Gemini Calling”介绍屏幕，其中包含示例" data-title="Gemini Call for Me might tell your mom you’re running late" data-date="10-06 07:09" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 07:09</span>
          <span class="news-item-title">双子座给我打电话可能会告诉你妈妈你迟到了</span>
          <span class="news-item-title-en">Gemini Call for Me might tell your mom you’re running late</span>
          <span class="news-value-point">💡 Google可能会将其“Call for Me”人工智能功能扩展到商务电话之外，以便您可以使用它向亲朋好友发送消息</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI将在欧盟对ChatGPT和Codex文本进行水印，以符合《人工智能法》。它说，编辑会使隐形标记更难被检测到。" data-title="OpenAI will start watermarking ChatGPT’s text in the EU" data-date="10-06 04:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-06 04:36</span>
          <span class="news-item-title">OpenAI将开始在欧盟为ChatGPT的文本添加水印</span>
          <span class="news-item-title-en">OpenAI will start watermarking ChatGPT’s text in the EU</span>
          <span class="news-value-point">💡 OpenAI将在欧盟对ChatGPT和Codex文本进行水印，以符合《人工智能法》</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1005075/nolla-health-acne-ai-prescriptions" target="_blank" rel="noopener" data-cat="keji" data-summary="犹他州的人们现在可以使用人工智能来获得治疗痤疮的处方。周一，医疗保健初创公司Nolla Health宣布，该州的用户可以使用其应用程序扫描他们的面部，从而使其人工智能系统能够自主分析痤疮的严重程度，" data-title="This startup is issuing AI-generated acne prescriptions" data-date="10-06 04:14" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 04:14</span>
          <span class="news-item-title">这家初创公司正在发布人工智能生成的痤疮处方</span>
          <span class="news-item-title-en">This startup is issuing AI-generated acne prescriptions</span>
          <span class="news-value-point">💡 犹他州的人们现在可以使用人工智能来获得治疗痤疮的处方</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/" target="_blank" rel="noopener" data-cat="keji" data-summary="Reflection将Beam和未来模型瞄准企业和主权国家。推销的目的是建立“人工智能工厂” ，该产品将允许机构通过自行培训Reflection的人工智能模型来构建自己的定制本地人工智能系统" data-title="Reflection debuts Beam, an open-weight AI model to rival Chinese models at lower compute cost" data-date="10-06 03:33" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-06 03:33</span>
          <span class="news-item-title">Reflection推出开放式权重AI模型Beam ，以更低的计算成本与中国机型相媲美</span>
          <span class="news-item-title-en">Reflection debuts Beam, an open-weight AI model to rival Chinese models at lower compute cost</span>
          <span class="news-value-point">💡 Reflection将Beam和未来模型瞄准企业和主权国家</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004933/ai-math-openai-breakthrough-solution" target="_blank" rel="noopener" data-cat="keji" data-summary="在过去的一年中， OpenAI、Anthropic和其他实验室宣布在许多长期存在的数学问题上取得突破，在某些情况下，这些突破远远超出了研究人员对当前系统的预期--包括解决" data-title="All the drama around AI’s takeover of mathematics" data-date="10-06 03:28" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 03:28</span>
          <span class="news-item-title">围绕人工智能接管数学的所有戏剧</span>
          <span class="news-item-title-en">All the drama around AI’s takeover of mathematics</span>
          <span class="news-value-point">💡 在过去的一年中， OpenAI、Anthropic和其他实验室宣布在许多长期存在的数学问题上取得突破，在某些情况下，这些突破远远超出了研究人员对…</span>
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
        <a class="news-item" href="https://www.theverge.com/tech/1004820/this-remote-controlled-wagon-is-silly-but-useful" target="_blank" rel="noopener" data-cat="zonghe" data-summary="忏悔：当BougeRV告诉我其带有动画照明的遥控车时，我打电话给它取笑，希望在评论中剔除它。可以肯定的是，这太荒谬了。但沙丘漫游者也被证明是非常强大的，有足够的扭矩" data-title="This remote-controlled wagon is silly but so very useful" data-date="10-06 16:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-06 16:00</span>
          <span class="news-item-title">这辆遥控马车很傻，但非常有用</span>
          <span class="news-item-title-en">This remote-controlled wagon is silly but so very useful</span>
          <span class="news-value-point">💡 忏悔：当BougeRV告诉我其带有动画照明的遥控车时，我打电话给它取笑，希望在评论中剔除它</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/008.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，日本烤肉连锁店“烧肉王”的运营方 —— 物语集团 10 月 5 日发布公告，其烧肉王官方 App 的会员管理系统被第三方非法访问，10,788,963 名会员信息被泄露。该应用的注册用户数为 10,808,784，泄露信息覆盖了大部分用户。IT之家从公告获悉，泄露的信息包括会员号码、姓名（应用注册名）、电子邮件地址和电话号码。另一方面，登录密码、出生日期、性别、邮政编码和持有积分等信息尚未泄露。10 月 2 日，未经授权的访问得到确认。该公司关闭了通讯并采取了其他防御措施，但在第二天，即 10 月 3 日，该公司确认了会员信息泄露。目前，没有证据表明泄露的信息已被滥用。官方确认此次信息泄露是由于第三方未经授权访问造成的，仍在调查泄露原因。在实施防止外部未经授权" data-title="日本烤肉连锁店“烧肉王”会员系统被黑，超千万条顾客信息泄露" data-date="10-06 15:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:56</span>
          <span class="news-item-title">日本烤肉连锁店“烧肉王”会员系统被黑，超千万条顾客信息泄露</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，日本烤肉连锁店“烧肉王”的运营方 —— 物语集团 10 月 5 日发布公告，其烧肉王官方 App 的会员管理系统…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/06/world/europe/france-student-strikes-protests.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="计划于周二举行的示威活动规模将考验自9月下旬以来在法国高中蔓延的学生领导的抗议运动的实力。" data-title="France Set for Nationwide Strikes, as School Protests Escalate" data-date="10-06 15:55" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-06 15:55</span>
          <span class="news-item-title">随着学校抗议活动升级，法国将发动全国性罢工</span>
          <span class="news-item-title-en">France Set for Nationwide Strikes, as School Protests Escalate</span>
          <span class="news-value-point">💡 计划于周二举行的示威活动规模将考验自9月下旬以来在法国高中蔓延的学生领导的抗议运动的实力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708442.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海南万宁10月6日电 题：国庆假期海南侨乡万宁“学艺式旅行”走红" data-title="国庆假期海南侨乡万宁“学艺式旅行”走红" data-date="10-06 15:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 15:53</span>
          <span class="news-item-title">国庆假期海南侨乡万宁“学艺式旅行”走红</span>
          <span class="news-value-point">💡 中新网海南万宁10月6日电 题：国庆假期海南侨乡万宁“学艺式旅行”走红</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708441.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南宁10月6日电 (于莉 郑长贤 周爱斌)中国铁路南宁局集团有限公司(简称国铁南宁局)6日提供的信息显示，2026年国庆假期进入尾声，铁路运输迎来旅客返程高峰。10月6日至8日客流高峰期间，国铁南宁局加开动车组列车517列，充分满足旅客假期返程需求。" data-title="国铁南宁局加开517列动车组列车助力旅客返程" data-date="10-06 15:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 15:53</span>
          <span class="news-item-title">国铁南宁局加开517列动车组列车助力旅客返程</span>
          <span class="news-value-point">💡 中新网南宁10月6日电 (于莉 郑长贤 周爱斌)中国铁路南宁局集团有限公司(简称国铁南宁局)6日提供的信息显示，2026年国庆假期进入尾声，铁路…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708444.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网绍兴10月6日电 题：六旬老汉炸臭豆腐三十余年 “闻臭食香”揭开别样江南" data-title="六旬老汉炸臭豆腐三十余年 “闻臭食香”揭开别样江南" data-date="10-06 15:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 15:51</span>
          <span class="news-item-title">六旬老汉炸臭豆腐三十余年 “闻臭食香”揭开别样江南</span>
          <span class="news-value-point">💡 中新网绍兴10月6日电 题：六旬老汉炸臭豆腐三十余年 “闻臭食香”揭开别样江南</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/004.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，博主 @科技饭相机情报 今日曝光了适马 APS-C 变焦镜头 50-120mm F2.8 DC OS | Contemporary 的官方渲染图以及完整规格，这款镜头预计将于 10 月 8 日发布。据悉，这款镜头具备索尼 E、富士 X 和佳能 RF 三大卡口版本，主打轻便（E 卡口版仅 390 克），内置 HLA 高速线性马达，支持光学防抖，并且针对视频拍摄做了优化（呼吸效应低）。IT之家附这款镜头主要参数如下：光学结构：13 组 18 片（3 SLD 、1 FLD、4 片非球面）光圈叶片：11 片（圆形）最近对焦距离：广角端为 23 厘米，长焦端为 55 厘米最大放大倍率：50mm 端 1:3，120mm 端 1:4.7滤镜直径：Ø55mm重量：索尼 E 卡" data-title="适马 50-120mm F2.8 APS-C 相机镜头曝光：支持光学防抖，覆盖索尼 E、富士 X、佳能 RF 卡口" data-date="10-06 15:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:41</span>
          <span class="news-item-title">适马 50-120mm F2.8 APS-C 相机镜头曝光：支持光学防抖，覆盖索尼 E、富士 X、佳能 RF 卡口</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，博主 @科技饭相机情报 今日曝光了适马 APS-C 变焦镜头 50-120mm F2.8 DC OS | Con…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708440.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网嘉兴10月6日电(林波)国庆假期，浙江大学海宁国际校区国际联合商学院的意大利留学生伊莱尼亚·阿利收拾好行囊，开启黄山之旅。对她而言，假期的打开方式，是登高览胜、寻访古村，在绿水青山间感受中国自然与人文；闲暇时，她还会继续练习太极拳，在一招一式间体会东方哲思。" data-title="爱打太极拳的意大利姑娘：把假期留给中国山水和乡村" data-date="10-06 15:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 15:38</span>
          <span class="news-item-title">爱打太极拳的意大利姑娘：把假期留给中国山水和乡村</span>
          <span class="news-value-point">💡 中新网嘉兴10月6日电(林波)国庆假期，浙江大学海宁国际校区国际联合商学院的意大利留学生伊莱尼亚·阿利收拾好行囊，开启黄山之旅</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cr3wvq8l864do/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="纳达尔·马里克·哈桑的处决将是自1961年以来首次军事处决，也是自第二次世界大战结束以来首次以行刑队枪决方式执行死刑。" data-title="美军拟枪决胡德堡基地枪击案凶手 二战后首例" data-date="10-06 15:34" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-06 15:34</span>
          <span class="news-item-title">美军拟枪决胡德堡基地枪击案凶手 二战后首例</span>
          <span class="news-value-point">💡 纳达尔·马里克·哈桑的处决将是自1961年以来首次军事处决，也是自第二次世界大战结束以来首次以行刑队枪决方式执行死刑</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/002.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，首批谷歌 Googlebook 笔记本已经于前两天在美国市场上市，宏碁、华硕、联想、惠普、戴尔等厂商均有推出对应机型。这些笔记本运行 Googlebook OS 操作系统，融合了 Android 的软件和 ChromeOS 桌面特性，支持运行完整版 Chrome 浏览器并提供独立 Linux 环境。如今，谷歌已经在官网给出了 Googlebook 的解锁 Bootloader 指南。用户可以在设置的关于设备页面下点击 build 号 7 次，然后在开发者选项中开启 OEM 解锁。之后需要进入 Recovery 模式，然后再恢复屏幕的“高级选项”找到“解锁引导加载程序”。需要注意的是，解锁 BL 会清除设备所有数据，并关闭安全保护功能。谷歌提醒，解锁的设备可能出" data-title="谷歌 Googlebook 笔记本解锁 BL 指南上线后，Magisk 确认适配" data-date="10-06 15:29" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:29</span>
          <span class="news-item-title">谷歌 Googlebook 笔记本解锁 BL 指南上线后，Magisk 确认适配</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，首批谷歌 Googlebook 笔记本已经于前两天在美国市场上市，宏碁、华硕、联想、惠普、戴尔等厂商均有推出对应…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/001.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 6 日消息，金融时报（FT）昨日（10 月 5 日）发布博文，报道称索尼音乐已要求各数字平台删除超过 26 万首冒充其旗下艺人的 AI 生成曲目。在数量方面，报道称是索尼音乐娱乐公司（Sony Music Entertainment）要求流媒体平台在 9 月底前下架超过 26 万首歌曲，这一数字几乎是 3 月底 13.5 万首的两倍。索尼表示，这些曲目利用生成式 AI 深度伪造技术，在未经许可的情况下模仿旗下艺人的声音与形象。索尼音乐全球数字业务总裁丹尼斯 · 库克（Dennis Kooker）表示，欺诈性流媒体播放量可能占音乐流媒体网站曲目总量的 10%。唱片公司高管估计，流媒体欺诈每年给行业造成的损失高达 22 亿美元（IT之家注：现汇率约合 147.72 亿元人民币" data-title="索尼音乐 9 月要求下架 26 万首 AI 伪造歌曲：阿黛尔等艺人被冒充，请求量较 3 月近乎翻倍" data-date="10-06 15:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-06 15:19</span>
          <span class="news-item-title">索尼音乐 9 月要求下架 26 万首 AI 伪造歌曲：阿黛尔等艺人被冒充，请求量较 3 月近乎翻倍</span>
          <span class="news-value-point">💡 IT之家 10 月 6 日消息，金融时报（FT）昨日（10 月 5 日）发布博文，报道称索尼音乐已要求各数字平台删除超过 26 万首冒充其旗下艺…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708430.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网泰州10月6日电 题：从“好人成林”到“好人森林” 泰州市海陵区厚植“好人文化”引领时代新风" data-title="从“好人成林”到“好人森林” 泰州市海陵区厚植“好人文化”引领时代新风" data-date="10-06 14:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 14:53</span>
          <span class="news-item-title">从“好人成林”到“好人森林” 泰州市海陵区厚植“好人文化”引领时代新风</span>
          <span class="news-value-point">💡 中新网泰州10月6日电 题：从“好人成林”到“好人森林” 泰州市海陵区厚植“好人文化”引领时代新风</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026-day-one" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在2026年10月的Amazon Prime Big Deal Days技术活动中获取所有超值优惠。" data-title="Best Amazon Prime Day tech deals live" data-date="10-06 14:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-06 14:50</span>
          <span class="news-item-title">亚马逊Prime Day技术实时超值优惠</span>
          <span class="news-item-title-en">Best Amazon Prime Day tech deals live</span>
          <span class="news-value-point">💡 在2026年10月的Amazon Prime Big Deal Days技术活动中获取所有超值优惠</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwzrd73z6k6mo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国公共图书馆已成为一场激烈意识形态冲突的战场，这场冲突的焦点在于学生应该能够获得哪些书籍。" data-title="美国图书馆为何正迅速下架众多图书？" data-date="10-06 14:31" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-06 14:31</span>
          <span class="news-item-title">美国图书馆为何正迅速下架众多图书？</span>
          <span class="news-value-point">💡 美国公共图书馆已成为一场激烈意识形态冲突的战场，这场冲突的焦点在于学生应该能够获得哪些书籍</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-06/10708418.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社青海玉树10月6日电 题：青海玉树千年古村：朴韵藏式碉楼引客来" data-title="（走进中国乡村）青海玉树千年古村：朴韵藏式碉楼引客来" data-date="10-06 14:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-06 14:30</span>
          <span class="news-item-title">（走进中国乡村）青海玉树千年古村：朴韵藏式碉楼引客来</span>
          <span class="news-value-point">💡 中新社青海玉树10月6日电 题：青海玉树千年古村：朴韵藏式碉楼引客来</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-06 16:14（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
