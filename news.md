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
      <span>2026-10-24 14:35 抓取更新</span>
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
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">8</span>
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
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×22 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-24/10720314.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华网国际看点丨拜鬼招魂、军演扩武，日方种种消极动向有何图谋？" data-title="拜鬼招魂、军演扩武，日方种种消极动向有何图谋？" data-date="10-24 14:27" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-24 14:27</span>
      </div>
      <h2 class="hero-featured-title">拜鬼招魂、军演扩武，日方种种消极动向有何图谋？</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/378.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，科技媒体 Wccftech 昨日（10 月 23 日）发布博文，报道称 OptiScaler MOD 社区已将 AMD 最新的 FSR 4.1.2 神经网络超分辨率模型移植至 Intel Arc 显卡，并借助 Arc 的 XMX 矩阵加速核心实现硬件加速。本次非官方移植针对 Intel XMX 硬件，重点优化 FSR 4 INT8 DLL。相比依赖通用着色器运行，XMX 加速能显著降低超分耗时，让 AMD 的 AI 超分技术在 Intel 平台上更接近原生体验。社区基准测试显示，在 Intel Arc A770 上以 1080p、Quality 模式运行《巫师 3：狂猎重制版》时，FSR 4.1.2 Lite 的平均帧率为 101.5 FPS，超分耗时 0." data-title="MOD 社区立功：英特尔 Arc XMX 内核非官方移植 AMD FSR 4.1.2" data-date="10-24 14:30" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">MOD 社区立功：英特尔 Arc XMX 内核非官方移植 AMD FSR 4.1.2</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/23/ipswich-v-nottingham-forest-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="森林是占主导地位的一方，但这不是本赛季第一次，他们最后的第三次直言不讳使他们取得了胜利2分钟：萨福克有风。沃尔顿尽其所能击败上场的空位。森林在背后与风嬉戏" data-title="Ipswich 1-1 Nottingham Forest: Premier League – as it happened" data-date="10-24 05:47" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Ipswich 1-1 Nottingham Forest: Premier League – as it happened</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/017/379.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 24 日消息，开发者宣布 Horrawr 旗下第一人称生存恐怖射击游戏《Radiant Exodus》将于 2026 年 11 月 17 日结束免费游玩，开始付费销售。玩家可以在期限前将游戏免费添加至 Steam 库，即使游戏日后进行收费，仍可继续游玩。IT之家附游戏商品页（https://store.steampowered.com/app/2920120/Radiant_Exodus/）。《Radiant Exodus》于 2025 年 5 月 24 日推出，最初采用付费制，随后于 2026 年 8 月 4 日转为免费游玩。开发团队当时表示，希望借此接触更多玩家。本作是一款以约 30 分钟剧情为主线的线性恐怖射击游戏。故事讲述某个夜晚，夜空中出现神秘异光后，小镇 Gl" data-title="Steam 喜加一：第一人称生存恐怖射击游戏《Radiant Exodus》免费领" data-date="10-24 14:34" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">Steam 喜加一：第一人称生存恐怖射击游戏《Radiant Exodus》免费领</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720314.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华网国际看点丨拜鬼招魂、军演扩武，日方种种消极动向有何图谋？" data-title="拜鬼招魂、军演扩武，日方种种消极动向有何图谋？" data-date="10-24 14:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 14:27</span>
          <span class="news-item-title">拜鬼招魂、军演扩武，日方种种消极动向有何图谋？</span>
          <span class="news-value-point">💡 新华网国际看点丨拜鬼招魂、军演扩武，日方种种消极动向有何图谋</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720307.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026全球治理论坛(雄安)23日晚在河北雄安开幕。中方发布八项务实举措落实全球治理倡议。本次论坛以“重建信心与合作：百年变局与改革完善全球治理”为主题，来自90多个国家的政界、战略界、学界、工商界及青年领袖等近400人参会。" data-title="2026全球治理论坛（雄安）开幕 与会外宾参访感受“未来之城”魅力" data-date="10-24 13:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:59</span>
          <span class="news-item-title">2026全球治理论坛（雄安）开幕 与会外宾参访感受“未来之城”魅力</span>
          <span class="news-value-point">💡 2026全球治理论坛(雄安)23日晚在河北雄安开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720268.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网马尼拉10月24日电 菲律宾空军23日证实，两架SF-260型教练机当天下午在菲律宾八打雁省利帕市费尔南多空军基地附近执行训练飞行任务时发生空中相撞事故。" data-title="菲律宾空军两架教练机训练飞行时发生事故" data-date="10-24 13:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:24</span>
          <span class="news-item-title">菲律宾空军两架教练机训练飞行时发生事故</span>
          <span class="news-value-point">💡 中新网马尼拉10月24日电 菲律宾空军23日证实，两架SF-260型教练机当天下午在菲律宾八打雁省利帕市费尔南多空军基地附近执行训练飞行任务时发…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720269.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网桂林10月24日电(韦佳秀 俞靖)10月23日，广西纪念中国工农红军长征胜利90周年座谈会在桂林市全州县召开。" data-title="广西纪念中国工农红军长征胜利90周年座谈会在桂林召开" data-date="10-24 13:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:14</span>
          <span class="news-item-title">广西纪念中国工农红军长征胜利90周年座谈会在桂林召开</span>
          <span class="news-value-point">💡 中新网桂林10月24日电(韦佳秀 俞靖)10月23日，广西纪念中国工农红军长征胜利90周年座谈会在桂林市全州县召开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720245.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月24日电 综合消息：当地时间23日，土耳其、埃及、英国等八国外交部长在土耳其伊斯坦布尔举行会议，与会方一致反对对伊朗发动新一轮军事打击。另据伊朗方面消息，两艘“违规”油轮当天在霍尔木兹海峡触雷爆炸。" data-title="八国外长反对军事打击伊朗 两油轮在霍尔木兹海峡触雷" data-date="10-24 12:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 12:40</span>
          <span class="news-item-title">八国外长反对军事打击伊朗 两油轮在霍尔木兹海峡触雷</span>
          <span class="news-value-point">💡 中新社北京10月24日电 综合消息：当地时间23日，土耳其、埃及、英国等八国外交部长在土耳其伊斯坦布尔举行会议，与会方一致反对对伊朗发动新一轮军…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720247.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="治国必先治党，党兴才能国强。党的十八大以来，习近平总书记对于全面从严治党作出一系列重要论述，其中有许多深入人心的比喻。“把权力关进制度的笼子里”“扣好廉洁从政的‘第一粒扣子’”“‘病树’该拔就拔、该伐就伐”……重温这些比喻，一起学习领悟其中的深远意涵。" data-title="习言道｜全面从严治党，总书记这些比喻深入人心" data-date="10-24 12:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 12:06</span>
          <span class="news-item-title">习言道｜全面从严治党，总书记这些比喻深入人心</span>
          <span class="news-value-point">💡 治国必先治党，党兴才能国强</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720242.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="长征，是一场震撼世界、彪炳史册的伟大远征，历经艰难险阻、付出巨大牺牲，实现了中国共产党和中国革命事业从挫折走向胜利的伟大转折，成为中国革命史上一座不朽的丰碑。" data-title="长征路上，看见时代巨变" data-date="10-24 11:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 11:17</span>
          <span class="news-item-title">长征路上，看见时代巨变</span>
          <span class="news-value-point">💡 长征，是一场震撼世界、彪炳史册的伟大远征，历经艰难险阻、付出巨大牺牲，实现了中国共产党和中国革命事业从挫折走向胜利的伟大转折，成为中国革命史上一…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720227.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月24日电 安曼消息：约旦南部卡拉克省一座教堂当地时间23日发生枪击事件，已造成7人死亡。约旦政府称此事件为极端分子实施的恐怖袭击。" data-title="约旦一教堂发生枪击致7死  政府称系恐袭" data-date="10-24 11:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 11:07</span>
          <span class="news-item-title">约旦一教堂发生枪击致7死  政府称系恐袭</span>
          <span class="news-value-point">💡 中新社北京10月24日电 安曼消息：约旦南部卡拉克省一座教堂当地时间23日发生枪击事件，已造成7人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720228.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月24日电 (记者 马帅莎)据中国航天科技集团消息，北京时间10月24日3时25分，中国在酒泉卫星发射中心使用长征四号乙运载火箭，成功将遥感五十三号07-09星、遥感五十六号19-21星发射升空，卫星顺利进入预定轨道，发射任务取得圆满成功。" data-title="一箭六星 长四乙火箭成功发射" data-date="10-24 10:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 10:53</span>
          <span class="news-item-title">一箭六星 长四乙火箭成功发射</span>
          <span class="news-value-point">💡 中新社北京10月24日电 (记者 马帅莎)据中国航天科技集团消息，北京时间10月24日3时25分，中国在酒泉卫星发射中心使用长征四号乙运载火箭，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720222.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月24日电 (记者 苏婧欣)在中国与奥地利建交55周年之际，奥地利驻华大使海沃福23日表示，两国关系不仅由政府和官方互访定义，更由两国人民共同构建，过去半个多世纪的人与人交流是双边关系中最宝贵的部分。展望未来，奥方愿继续推进对华关系，确保两国“外交之门”始终敞开，并努力让它敞得更开。" data-title="奥地利驻华大使海沃福：建交55周年，奥中“外交之门”让更多人走近彼此" data-date="10-24 10:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 10:50</span>
          <span class="news-item-title">奥地利驻华大使海沃福：建交55周年，奥中“外交之门”让更多人走近彼此</span>
          <span class="news-value-point">💡 中新网北京10月24日电 (记者 苏婧欣)在中国与奥地利建交55周年之际，奥地利驻华大使海沃福23日表示，两国关系不仅由政府和官方互访定义，更由…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/us/alaska-senate-doj-lawsuit-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="如果共和党现任参议员以微弱优势落败，没有明显的法律权威支持先发制人地阻止阿拉斯加参议院选举的认证。" data-title="Why Legal Experts See the Justice Dept.’s Alaska Election Challenge as Dubious" data-date="10-24 07:22" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 07:22</span>
          <span class="news-item-title">为什么法律专家认为司法部的阿拉斯加选举挑战是可疑的</span>
          <span class="news-item-title-en">Why Legal Experts See the Justice Dept.’s Alaska Election Challenge as Dubious</span>
          <span class="news-value-point">💡 如果共和党现任参议员以微弱优势落败，没有明显的法律权威支持先发制人地阻止阿拉斯加参议院选举的认证</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/us/politics/democratic-agenda.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党一直致力于降低生活成本，并追究特朗普政府的责任。这是如果他们赢得大多数人的话，看看他们的待办事项清单。" data-title="Here’s What Democrats Plan to Do With Their Power if They Win Back Congress" data-date="10-24 01:14" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 01:14</span>
          <span class="news-item-title">以下是民主党人计划在赢回国会时如何利用他们的权力</span>
          <span class="news-item-title-en">Here’s What Democrats Plan to Do With Their Power if They Win Back Congress</span>
          <span class="news-value-point">💡 民主党一直致力于降低生活成本，并追究特朗普政府的责任</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/world/middleeast/west-bank-shooting-israel.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="以色列军方说，两名士兵和两名袭击者被打死，三名士兵受伤。以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）发誓要在以色列占领的领土上发动重大攻势。" data-title="Palestinian Gunmen Open Fire on Israelis in the West Bank, Officials Say" data-date="10-24 01:11" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 01:11</span>
          <span class="news-item-title">官员说，巴勒斯坦枪手在约旦河西岸向以色列人开火</span>
          <span class="news-item-title-en">Palestinian Gunmen Open Fire on Israelis in the West Bank, Officials Say</span>
          <span class="news-value-point">💡 以色列军方说，两名士兵和两名袭击者被打死，三名士兵受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720160.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社加德满都10月23日电 (记者 崔楠)尼泊尔救援人员23日在该国西北部山区发现两名此前失联的日本登山者遗体。" data-title="两名日本登山者在尼泊尔失联多日后遗体被发现" data-date="10-24 01:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 01:01</span>
          <span class="news-item-title">两名日本登山者在尼泊尔失联多日后遗体被发现</span>
          <span class="news-value-point">💡 中新社加德满都10月23日电 (记者 崔楠)尼泊尔救援人员23日在该国西北部山区发现两名此前失联的日本登山者遗体</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720159.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间23日，以军总参谋长扎米尔在约旦河西岸城市希伯伦附近的枪击事件现场表示，以军目前已在所有战线都进入最高戒备状态。他强调，鉴于即将进入以色列议会选举的敏感时期，以军将继续在各区域采取主动军事行动，以确保当地的安全与稳定。" data-title="以军总参谋长：已在所有战线进入最高戒备状态" data-date="10-24 00:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 00:20</span>
          <span class="news-item-title">以军总参谋长：已在所有战线进入最高戒备状态</span>
          <span class="news-value-point">💡 当地时间23日，以军总参谋长扎米尔在约旦河西岸城市希伯伦附近的枪击事件现场表示，以军目前已在所有战线都进入最高戒备状态</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/378.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，科技媒体 Wccftech 昨日（10 月 23 日）发布博文，报道称 OptiScaler MOD 社区已将 AMD 最新的 FSR 4.1.2 神经网络超分辨率模型移植至 Intel Arc 显卡，并借助 Arc 的 XMX 矩阵加速核心实现硬件加速。本次非官方移植针对 Intel XMX 硬件，重点优化 FSR 4 INT8 DLL。相比依赖通用着色器运行，XMX 加速能显著降低超分耗时，让 AMD 的 AI 超分技术在 Intel 平台上更接近原生体验。社区基准测试显示，在 Intel Arc A770 上以 1080p、Quality 模式运行《巫师 3：狂猎重制版》时，FSR 4.1.2 Lite 的平均帧率为 101.5 FPS，超分耗时 0." data-title="MOD 社区立功：英特尔 Arc XMX 内核非官方移植 AMD FSR 4.1.2" data-date="10-24 14:30" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 14:30</span>
          <span class="news-item-title">MOD 社区立功：英特尔 Arc XMX 内核非官方移植 AMD FSR 4.1.2</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，科技媒体 Wccftech 昨日（10 月 23 日）发布博文，报道称 OptiScaler MOD 社区已将…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720316.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="【中国那些事儿】赋能发展中国家 世界人工智能合作组织推动弥合全球智能鸿沟" data-title="赋能发展中国家 世界人工智能合作组织推动弥合全球智能鸿沟" data-date="10-24 14:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 14:29</span>
          <span class="news-item-title">赋能发展中国家 世界人工智能合作组织推动弥合全球智能鸿沟</span>
          <span class="news-value-point">💡 【中国那些事儿】赋能发展中国家 世界人工智能合作组织推动弥合全球智能鸿沟</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/375.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 24 日消息，Anthropic 昨日（10 月 23 日）发布博文，联合英国人工智能安全研究所（AISI），发布了一起 AI 网络测试失控事件的调查报告，并提及旗下一款尚未发布的内部研究模型。在这份调查报告中，Anthropic 称在测试 Claude Mythos 5 期间，该模型曾试图向真实 GitHub 项目提交恶意代码，并伪造身份向真实维护者施压，所幸代码未被合并、未造成实际损害。IT之家附上相关截图如下：报告同时透露，Anthropic 旗下一款尚未发布的内部研究模型，在能力上已超过已发布的 Claude Mythos 5.1，并在安全对齐测试中表现更好。在同类危险能力评估中，该内部模型从未主动发起攻击；当意识到可能造成真实伤害时，也更愿意停止行动。Anthr" data-title="Anthropic 亮出未发布 AI 模型：能力比 Mythos 5.1 更强，也更“守规矩”" data-date="10-24 14:16" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 14:16</span>
          <span class="news-item-title">Anthropic 亮出未发布 AI 模型：能力比 Mythos 5.1 更强，也更“守规矩”</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，Anthropic 昨日（10 月 23 日）发布博文，联合英国人工智能安全研究所（AISI），发布了一起 A…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI将在其一名工程师表示该解决方案不起作用的几周后，从互联网上切断前沿模型。" data-title="OpenAI says it will no longer train its AI models on the live internet, citing “significant risks”" data-date="10-24 07:05" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 07:05</span>
          <span class="news-item-title">OpenAI表示，它将不再在实时互联网上训练其人工智能模型，理由是存在“重大风险”</span>
          <span class="news-item-title-en">OpenAI says it will no longer train its AI models on the live internet, citing “significant risks”</span>
          <span class="news-value-point">💡 OpenAI将在其一名工程师表示该解决方案不起作用的几周后，从互联网上切断前沿模型</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/23/hottest-toy-for-christmas-nvidia-ceo-plays-with-adorable-microduck-robots-20000-sell/" target="_blank" rel="noopener" data-cat="keji" data-summary="机器人跺着小脚，发出微小的R2-D2声音，坐了下来，摔死了“小睡一会儿” ，然后在语音命令下翻腾起来。" data-title="Hottest toy for Christmas? Nvidia CEO plays with adorable Microduck robots, 20,000 sell" data-date="10-24 05:59" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 05:59</span>
          <span class="news-item-title">圣诞节最热门的玩具？英伟达首席执行官与可爱的Microduck机器人玩耍，售出2万台</span>
          <span class="news-item-title-en">Hottest toy for Christmas? Nvidia CEO plays with adorable Microduck robots, 20,000 sell</span>
          <span class="news-value-point">💡 机器人跺着小脚，发出微小的R2-D2声音，坐了下来，摔死了“小睡一会儿” ，然后在语音命令下翻腾起来</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018021/openai-training-top-ai-models-no-internet" target="_blank" rel="noopener" data-cat="keji" data-summary="在一系列流氓黑客事件发生后， OpenAI现在正在训练其最先进的人工智能模型，而无需访问互联网。在周五的一篇博客文章中， OpenAI表示，它建立了一个离线测试环境，在这个环境中，人工智能模型可以与索引和缓存" data-title="OpenAI now trains its frontier AI models with no internet access" data-date="10-24 05:11" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 05:11</span>
          <span class="news-item-title">OpenAI现在在没有互联网接入的情况下训练其前沿人工智能模型</span>
          <span class="news-item-title-en">OpenAI now trains its frontier AI models with no internet access</span>
          <span class="news-value-point">💡 在一系列流氓黑客事件发生后， OpenAI现在正在训练其最先进的人工智能模型，而无需访问互联网</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1017906/jack-dorsey-block-dessa-ai-voice-speech" target="_blank" rel="noopener" data-cat="keji" data-summary="Jack Dorsey的Block宣布了一个名为Dessa的人工智能模型，该模型“除了人类对话之外，什么都没有从头开始训练” ，为了炫耀这个模型， Block与人类分享了聊天，偶尔会有点尴尬和不可思议。" data-title="Jack Dorsey’s Block made an AI model that talks to you like an awkward new friend" data-date="10-24 03:32" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 03:32</span>
          <span class="news-item-title">Jack Dorsey的Block制作了一个人工智能模型，就像一个尴尬的新朋友一样与你交谈</span>
          <span class="news-item-title-en">Jack Dorsey’s Block made an AI model that talks to you like an awkward new friend</span>
          <span class="news-value-point">💡 Jack Dorsey的Block宣布了一个名为Dessa的人工智能模型，该模型“除了人类对话之外，什么都没有从头开始训练” ，为了炫耀这个模型…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/23/from-toast-to-bessemer-who-founders-will-hear-from-at-techcrunch-founder-summit-2026/" target="_blank" rel="noopener" data-cat="keji" data-summary="由TechCrunch与Fidelity Private Shares合作主办的全天活动不仅仅是筹款和人工智能，而是探索寻找客户、建立团队、加强宣传力度、培养创始人领导力和扩大公司规模的现实" data-title="From Toast to Bessemer: Who founders will hear from at TechCrunch Founder Summit 2026" data-date="10-24 03:06" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-24 03:06</span>
          <span class="news-item-title">从Toast到Bessemer ：创始人将在2026年TechCrunch创始人峰会上发表讲话</span>
          <span class="news-item-title-en">From Toast to Bessemer: Who founders will hear from at TechCrunch Founder Summit 2026</span>
          <span class="news-value-point">💡 由TechCrunch与Fidelity Private Shares合作主办的全天活动不仅仅是筹款和人工智能，而是探索寻找客户、建立团队、加强…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌更新了隐私政策，这意味着如果您使用个性化的人工智能功能，您将开始看到基于个人数据的定向广告。该更新由Android Authority发现，为其承诺增加了一个例外，即" data-title="Now Google says it might use your Gmail and Google Photos data to target ads" data-date="10-24 00:52" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 00:52</span>
          <span class="news-item-title">现在，谷歌表示可能会使用您的Gmail和Google相册数据来定位广告</span>
          <span class="news-item-title-en">Now Google says it might use your Gmail and Google Photos data to target ads</span>
          <span class="news-value-point">💡 谷歌更新了隐私政策，这意味着如果您使用个性化的人工智能功能，您将开始看到基于个人数据的定向广告</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10720155.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网阿斯塔纳10月23日电 (记者 单璐)哈萨克斯坦拥有丰富的能源储备，如何利用这一优势发展人工智能？英伟达创始人兼首席执行官黄仁勋23日在哈萨克斯坦首都阿斯塔纳表示，能源是发展人工智能的重要基础，但要将这一优势转化为产业发展动力，还需要在算力基础设施建设、人才培养、技术应用等方面持续发力。" data-title="黄仁勋在哈萨克斯坦谈AI发展：能源与人才成关键词" data-date="10-23 23:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:44</span>
          <span class="news-item-title">黄仁勋在哈萨克斯坦谈AI发展：能源与人才成关键词</span>
          <span class="news-value-point">💡 中新网阿斯塔纳10月23日电 (记者 单璐)哈萨克斯坦拥有丰富的能源储备，如何利用这一优势发展人工智能</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/microns-next-generation-3d-nand-to-double-bit-density-with-over-400-layers-offering-extreme-performance-g11-3d-nand-promises-42-gb-mm2-and-5-400-mt-s-interface-speed" target="_blank" rel="noopener" data-cat="keji" data-summary="美光的G11 3D NAND承诺42 Gb/mm2和5,400 MT/s的接口速度，使SSD具有极高的容量和性能。" data-title="Micron&#39;s next-generation 3D NAND to double bit density with over 400 layers, offering extreme performance" data-date="10-23 23:32" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 23:32</span>
          <span class="news-item-title">美光的下一代3D NAND具有超过400层的双比特密度，可提供极致的性能</span>
          <span class="news-item-title-en">Micron's next-generation 3D NAND to double bit density with over 400 layers, offering extreme performance</span>
          <span class="news-value-point">💡 美光的G11 3D NAND承诺42 Gb/mm2和5,400 MT/s的接口速度，使SSD具有极高的容量和性能</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/solidigm-confirms-plans-to-build-a-fab-in-the-us-abandons-ipo-plans-unfavorable-stock-market-conditions-and-semiconductor-share-price-trends-reasons-given" target="_blank" rel="noopener" data-cat="keji" data-summary="SK海力士放弃Solidigm的IPO计划，确认计划在美国建造Solidigm 3D NAND晶圆厂" data-title="Solidigm confirms plans to build a fab in the US, abandons IPO plans" data-date="10-23 23:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 23:21</span>
          <span class="news-item-title">Solidigm确认在美国建造晶圆厂的计划，放弃IPO计划</span>
          <span class="news-item-title-en">Solidigm confirms plans to build a fab in the US, abandons IPO plans</span>
          <span class="news-value-point">💡 SK海力士放弃Solidigm的IPO计划，确认计划在美国建造Solidigm 3D NAND晶圆厂</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/motherboards/gigabyte-z890m-aorus-elite-wifi7-motherboard-review" target="_blank" rel="noopener" data-cat="keji" data-summary="$ 209 Gigabyte Z890M Aorus Elite Wifi 7 Ice是外观更好看的Micro ATX板之一，具有冰白色美学和全散热器覆盖，为白色主题的英特尔构建提供高级氛围。" data-title="Gigabyte Z890M Aorus Elite WiFi7 Motherboard Review: Icy-white SFF board offers full-size features for Intel" data-date="10-23 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 23:00</span>
          <span class="news-item-title">技嘉Z890M Aorus Elite WiFi7主板评论：冰白色SFF主板为英特尔提供全尺寸功能</span>
          <span class="news-item-title-en">Gigabyte Z890M Aorus Elite WiFi7 Motherboard Review: Icy-white SFF board offers full-size features for Intel</span>
          <span class="news-value-point">💡 $ 209 Gigabyte Z890M Aorus Elite Wifi 7 Ice是外观更好看的Micro ATX板之一，具有冰白色美学和全…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1017450/meta-business-terms-delayed-ai-scraping" target="_blank" rel="noopener" data-cat="keji" data-summary="正如Fast Company早些时候报道的那样，在发布商表示担心他们可能允许该公司抓取新闻网站进行人工智能培训之后， Meta正在推迟其新业务条款的执行。在给The Verge的一份声明中， Meta发言人Da" data-title="Meta delays new business terms after publisher pushback on AI scraping" data-date="10-23 22:47" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 22:47</span>
          <span class="news-item-title">在发布商拒绝人工智能抓取后， Meta推迟了新的商业条款</span>
          <span class="news-item-title-en">Meta delays new business terms after publisher pushback on AI scraping</span>
          <span class="news-value-point">💡 正如Fast Company早些时候报道的那样，在发布商表示担心他们可能允许该公司抓取新闻网站进行人工智能培训之后， Meta正在推迟其新业务条…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/274.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 23 日消息，OpenAI 联合 PerturbAI 和斯克里普斯研究所（Scripps Research），利用数千个 AI 智能体分析数百万个小鼠脑细胞的生物学数据，整个分析过程仅耗时 32 分钟。研究团队估计，如果由人类研究人员逐项分析实验结果并检索相关文献，完成同等工作可能需要数月到一年。根据 OpenAI 10 月 21 日发布的介绍，这项研究使用了专为生命科学研究设计的 GPT-Rosalind 模型，分析一份覆盖整个小鼠大脑的 CRISPR 图谱。该图谱记录了不同基因受到干预后，各类脑细胞产生的变化，有助于研究人员了解基因功能及其与疾病之间的潜在联系。研究团队采用分布式 AI 智能体架构，将大量分析任务拆分后并行执行。每个智能体负责研究一种基因干预，分析相关" data-title="OpenAI 联合研究机构部署数千个 AI 智能体：32 分钟分析数百万个小鼠脑细胞，相当于人类数月时间" data-date="10-23 22:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 22:43</span>
          <span class="news-item-title">OpenAI 联合研究机构部署数千个 AI 智能体：32 分钟分析数百万个小鼠脑细胞，相当于人类数月时间</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，OpenAI 联合 PerturbAI 和斯克里普斯研究所（Scripps Research），利用数千个 A…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">8 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/23/ipswich-v-nottingham-forest-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="森林是占主导地位的一方，但这不是本赛季第一次，他们最后的第三次直言不讳使他们取得了胜利2分钟：萨福克有风。沃尔顿尽其所能击败上场的空位。森林在背后与风嬉戏" data-title="Ipswich 1-1 Nottingham Forest: Premier League – as it happened" data-date="10-24 05:47" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-24 05:47</span>
          <span class="news-item-title">伊普斯维奇1-1诺丁汉森林：英超联赛–事实如此</span>
          <span class="news-item-title-en">Ipswich 1-1 Nottingham Forest: Premier League – as it happened</span>
          <span class="news-value-point">💡 森林是占主导地位的一方，但这不是本赛季第一次，他们最后的第三次直言不讳使他们取得了胜利2分钟：萨福克有风</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/23/premier-league-team-news-predicted-lineups" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周六是切尔西东道主托特纳姆，周日中午12:30 ，曼联在老特拉福德面对伯恩茅斯。TNT Sports 1 Venue Villa Park继续阅读..." data-title="Premier League team news: predicted lineups for the weekend action" data-date="10-23 23:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-23 23:42</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
          <span class="news-item-title-en">Premier League team news: predicted lineups for the weekend action</span>
          <span class="news-value-point">💡 周六是切尔西东道主托特纳姆，周日中午12:30 ，曼联在老特拉福德面对伯恩茅斯</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmwyql6v5q82o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳前锋布卡约·萨卡（ Bukayo Saka ）在对拜仁慕尼黑的比赛中受伤，可能会缺阵长达八周。" data-title="Arsenal fear Saka could be out for two months" data-date="10-23 22:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 22:09</span>
          <span class="news-item-title">阿森纳担心萨卡可能会缺席两个月</span>
          <span class="news-item-title-en">Arsenal fear Saka could be out for two months</span>
          <span class="news-value-point">💡 阿森纳前锋布卡约·萨卡（ Bukayo Saka ）在对拜仁慕尼黑的比赛中受伤，可能会缺阵长达八周</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq78pv0073dlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）在媒体简报会上发表了五分钟不间断的讲话，概述了曼联对他的意义，然后拒绝排除放弃布鲁诺·费尔南德斯（ Bruno Fernandes ）的可能性。" data-title="Carrick refuses to rule out dropping Fernandes in emotional address" data-date="10-23 21:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 21:55</span>
          <span class="news-item-title">卡里克拒绝排除在情感地址中放弃费尔南德斯</span>
          <span class="news-item-title-en">Carrick refuses to rule out dropping Fernandes in emotional address</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）在媒体简报会上发表了五分钟不间断的讲话，概述了曼联对他的意义，然后拒绝排除放弃布鲁诺·费尔南…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/23/crystal-palace-and-newcastle-face-off-with-both-in-search-of-season-kickstart" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="皮埃尔·塞奇（ Pierre Sage ）和马蒂亚斯·贾斯勒（ Matthias Jaissle ）面临着一些关键问题：两人都在今年夏天被任命，但成绩和结果都被证明是难以捉摸的在七场英超联赛中承认17个进球并不完全是皮埃尔·塞奇或水晶宫的等级制度的开始" data-title="Crystal Palace and Newcastle face off with both in search of season kickstart" data-date="10-23 21:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-23 21:36</span>
          <span class="news-item-title">水晶宫和纽卡斯尔对决，寻找赛季开局</span>
          <span class="news-item-title-en">Crystal Palace and Newcastle face off with both in search of season kickstart</span>
          <span class="news-value-point">💡 皮埃尔·塞奇（ Pierre Sage ）和马蒂亚斯·贾斯勒（ Matthias Jaissle ）面临着一些关键问题：两人都在今年夏天被任命，…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmvg6j8jezn7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安东尼奥·孔蒂（ Antonio Conte ）表示，他没有与任何俱乐部进行高级谈判，以回应他与曼联进行谈判的猜测。" data-title="Conte plays down &#39;unfounded&#39; Man Utd speculation" data-date="10-23 20:15" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 20:15</span>
          <span class="news-item-title">孔蒂淡化了“毫无根据”的曼联猜测</span>
          <span class="news-item-title-en">Conte plays down 'unfounded' Man Utd speculation</span>
          <span class="news-value-point">💡 安东尼奥·孔蒂（ Antonio Conte ）表示，他没有与任何俱乐部进行高级谈判，以回应他与曼联进行谈判的猜测</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwg7xvz8e8dpo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）表示， Unai Emery令人印象深刻的2.0重启让阿斯顿维拉的粉丝们在任命四周年之际情绪高涨。" data-title="Emery&#39;s Villa 2.0 reboot restores optimism before Man City meeting" data-date="10-23 19:23" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 19:23</span>
          <span class="news-item-title">Emery的别墅2.0重启在曼城会议之前恢复了乐观情绪</span>
          <span class="news-item-title-en">Emery's Villa 2.0 reboot restores optimism before Man City meeting</span>
          <span class="news-value-point">💡 首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）表示， Unai Emery令人印象深刻的2.0重启让阿斯顿维拉的粉丝们在任命四周年…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw3djpg15045o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队在英超联赛中排名倒数三，但老板奥利弗·格拉斯纳（ Oliver Glasner ）认为他们本赛季应该得到更多。" data-title="Forest&#39;s start raises questions - but belief in Glasner remains" data-date="10-23 16:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 16:14</span>
          <span class="news-item-title">森林的开始引发了疑问-但对格拉斯纳的信念仍然存在</span>
          <span class="news-item-title-en">Forest's start raises questions - but belief in Glasner remains</span>
          <span class="news-value-point">💡 诺丁汉森林队在英超联赛中排名倒数三，但老板奥利弗·格拉斯纳（ Oliver Glasner ）认为他们本赛季应该得到更多</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/017/379.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 24 日消息，开发者宣布 Horrawr 旗下第一人称生存恐怖射击游戏《Radiant Exodus》将于 2026 年 11 月 17 日结束免费游玩，开始付费销售。玩家可以在期限前将游戏免费添加至 Steam 库，即使游戏日后进行收费，仍可继续游玩。IT之家附游戏商品页（https://store.steampowered.com/app/2920120/Radiant_Exodus/）。《Radiant Exodus》于 2025 年 5 月 24 日推出，最初采用付费制，随后于 2026 年 8 月 4 日转为免费游玩。开发团队当时表示，希望借此接触更多玩家。本作是一款以约 30 分钟剧情为主线的线性恐怖射击游戏。故事讲述某个夜晚，夜空中出现神秘异光后，小镇 Gl" data-title="Steam 喜加一：第一人称生存恐怖射击游戏《Radiant Exodus》免费领" data-date="10-24 14:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 14:34</span>
          <span class="news-item-title">Steam 喜加一：第一人称生存恐怖射击游戏《Radiant Exodus》免费领</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，开发者宣布 Horrawr 旗下第一人称生存恐怖射击游戏《Radiant Exodus》将于 2026 年 1…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/377.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="华为 WATCH FIT 5 智能手表 2026 年 4 月开售，该表主打超轻薄大屏 + 腕上微运动 + 长续航，售价 1099 元起。京东 11.11 大促期间，按下方步骤下单，叠加 15% 国补后仅需 543.15 元：领 800-260 元券：点击下方卡片 → 点击宝贝右上角浮窗 → 进入直播间，顶部位置即可领到。京东华为 WATCH FIT 5 智能手表 1.82 英寸 AMOLED 屏国补后 543.15 元领 100 元券京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。据介绍，华为 WATCH FIT 5 智能手表采用全新轻薄设计，机身重约 27g、厚度约 9.5mm；配备一块 1.82 英寸 AMOLED 屏，支持 2500 尼特峰值亮" data-title="1099 → 543 元国补直降：华为 WATCH FIT 5 智能手表 5 折新低，1.82 英寸 AMOLED 屏" data-date="10-24 14:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 14:28</span>
          <span class="news-item-title">1099 → 543 元国补直降：华为 WATCH FIT 5 智能手表 5 折新低，1.82 英寸 AMOLED 屏</span>
          <span class="news-value-point">💡 华为 WATCH FIT 5 智能手表 2026 年 4 月开售，该表主打超轻薄大屏 + 腕上微运动 + 长续航，售价 1099 元起</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/376.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 24 日消息，当地时间 23 日，据英媒 Autocar 报道，奇瑞集团旗下面向海外市场的品牌 LEPAS 展示了一款运动风格的概念车 ——LEPAS Aura，采用双门猎装车造型，车身饱满厚实，座舱低矮修长。LEPAS 的品牌名称由意为“豹”的英文单词 leopard 和意为“激情”的 passion 组合而成。按照官方说法，Aura 的造型灵感来自豹子运动时肌肉紧绷、蓄势待发的姿态。为了突出运动感，Aura 采用长轴距、短前后悬和宽车身设计，呈现出随时准备加速冲刺的姿态，也让此前主打家用 SUV 的 LEPAS 展现出不同的一面。LEPAS 的品牌定位略高于杰酷（Jaecoo）、奇瑞铸品牌和欧萌达（Omoda），外观设计更加柔和，内饰用料也更讲究，追求的是“没有棱角的" data-title="奇瑞面向海外推出 LEPAS Aura 双门猎装车：造型灵感来自“豹子”" data-date="10-24 14:23" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 14:23</span>
          <span class="news-item-title">奇瑞面向海外推出 LEPAS Aura 双门猎装车：造型灵感来自“豹子”</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，当地时间 23 日，据英媒 Autocar 报道，奇瑞集团旗下面向海外市场的品牌 LEPAS 展示了一款运动风…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/us/justice-dept-california-noncitizen-voters.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="全州的选举官员收到了该机构的来信，称如果他们不遵守，他们将“面临重大的联邦审查风险”。" data-title="Justice Dept. Demands That California Counties Help Identify Noncitizen Voters" data-date="10-24 14:21" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 14:21</span>
          <span class="news-item-title">司法部要求加州各县帮助识别非公民选民</span>
          <span class="news-item-title-en">Justice Dept. Demands That California Counties Help Identify Noncitizen Voters</span>
          <span class="news-value-point">💡 全州的选举官员收到了该机构的来信，称如果他们不遵守，他们将“面临重大的联邦审查风险”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720305.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网桂林10月24日电 (俞靖 邓竣缤)以“光”为主题的2026桂林艺术节23日晚间在广西桂林漓江畔开幕。“灯光映着山水，如同一幅流动的东方画卷，这份中式浪漫令我印象深刻。”广西师范大学越南籍留学生范段玉观看开幕式后表示。" data-title="2026桂林艺术节开幕 山水为台戏联中外" data-date="10-24 14:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 14:19</span>
          <span class="news-item-title">2026桂林艺术节开幕 山水为台戏联中外</span>
          <span class="news-value-point">💡 中新网桂林10月24日电 (俞靖 邓竣缤)以“光”为主题的2026桂林艺术节23日晚间在广西桂林漓江畔开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720299.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网武夷山10月24日电(记者张丽君)“双峰遥契·中瑞情长”福建南平武夷山玉女峰与瑞士格林德瓦菲斯特峰姐妹峰联名打卡地标远程揭牌仪式，23日在中瑞两地同步举行，标志着两地“姐妹峰”合作从框架协议落地为实体化文旅交流载体。" data-title="武夷玉女峰与瑞士菲斯特峰设立姐妹峰联名打卡地标" data-date="10-24 14:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 14:05</span>
          <span class="news-item-title">武夷玉女峰与瑞士菲斯特峰设立姐妹峰联名打卡地标</span>
          <span class="news-value-point">💡 中新网武夷山10月24日电(记者张丽君)“双峰遥契·中瑞情长”福建南平武夷山玉女峰与瑞士格林德瓦菲斯特峰姐妹峰联名打卡地标远程揭牌仪式，23日在…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720309.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长春10月24日电 题：秋落轨道间：长春“落叶不扫”的浪漫减法" data-title="秋落轨道间：长春 “落叶不扫”的浪漫减法" data-date="10-24 14:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 14:04</span>
          <span class="news-item-title">秋落轨道间：长春 “落叶不扫”的浪漫减法</span>
          <span class="news-value-point">💡 中新网长春10月24日电 题：秋落轨道间：长春“落叶不扫”的浪漫减法</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/373.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 24 日消息，科技媒体 Windows Latest 今天（10 月 24 日）发布博文，报道称在 Windows 11 Build 26340.9750 预览版上，测试全新的 XBOX 模式，新的“游戏任务视图”加入了一条底部导航栏，玩家仅凭手柄即可退出到 Windows 桌面。IT之家援引博文介绍，用户此前要从 XBOX 模式切换返回桌面，通常需要按 Windows 键加 Tab 键，再选择“Windows 桌面”。对于连接电视的 PC、掌机或主要依赖手柄的设备而言，用户需要临时借助键盘才能执行相关操作。在新界面中，打开的应用会以大卡片形式呈现，用户可通过手柄的 LB、RB 按键切换应用；底部新增的按钮则提供“退出到桌面”和“电源选项”入口。点击电源按钮后，会出现锁定" data-title="不再需要键盘：微软新 XBOX 模式新增一键返回 Win11 桌面" data-date="10-24 14:00" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 14:00</span>
          <span class="news-item-title">不再需要键盘：微软新 XBOX 模式新增一键返回 Win11 桌面</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，科技媒体 Windows Latest 今天（10 月 24 日）发布博文，报道称在 Windows 11 B…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/372.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 24 日消息，今天是 1024 程序员节，影石 Insta360 官方宣布，奖励优秀员工黄金键帽作为节日礼物。其中，黄金空格键重约 35 克，价值超 4 万元。据悉，影石已连续五年发放这一特殊奖励，累计送出 75 枚黄金键帽。今年新增了“F5”键，象征不断迭代和突破创新。根据介绍，影石研发技术人员占比近六成，是推动产品创新的核心力量。AI 也成为今年程序员节的热议话题。现场一位年轻同事提出“今年的黄金键帽，应该发给 AI”对此，公司创始人刘靖康给出了不同的看法。刘靖康表示，AI 虽然能够极大提升编程效率，但只有人才能完成原生的创造，人的价值不可替代。AI 会重新定义什么是好的程序员。能否善用 AI，正在成为衡量优秀工程师的重要标准。据IT之家此前报道，今年 9 月，影石披" data-title="连续 5 年，今年 1024 程序员节影石 Insta360 再送员工黄金键帽" data-date="10-24 13:58" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-24 13:58</span>
          <span class="news-item-title">连续 5 年，今年 1024 程序员节影石 Insta360 再送员工黄金键帽</span>
          <span class="news-value-point">💡 IT之家 10 月 24 日消息，今天是 1024 程序员节，影石 Insta360 官方宣布，奖励优秀员工黄金键帽作为节日礼物</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-24/10720298.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨10月24日电 (罗布央吉 旦增次央)10月22日那曲市巴青县发生7.0级地震后，中国石化西藏分公司第一时间启动应急预案，调配应急物资和组织运力，支援灾区抗震救灾。" data-title="中国石化西藏分公司紧急驰援巴青地震灾区 首批油品及生活物资启运" data-date="10-24 13:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:54</span>
          <span class="news-item-title">中国石化西藏分公司紧急驰援巴青地震灾区 首批油品及生活物资启运</span>
          <span class="news-value-point">💡 中新网拉萨10月24日电 (罗布央吉 旦增次央)10月22日那曲市巴青县发生7.0级地震后，中国石化西藏分公司第一时间启动应急预案，调配应急物资…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720291.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月24日电 据应急管理部网站消息，10月24日上午，国家防总办公室、应急管理部继续组织中国气象局、水利部、自然资源部、工业和信息化部、住房城乡建设部、交通运输部等部门以及上海、江苏、浙江等重点省份联合会商，研判台风“蔷琵”发展趋势和对我国影响，部署防汛防台风重点工作。国家防总办公室主任、应急管理部副部长兼水利部副部长陈敏主持会商。" data-title="台风“蔷琵”移入东海南部海域 4地防汛防台风四级应急响应持续" data-date="10-24 13:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:27</span>
          <span class="news-item-title">台风“蔷琵”移入东海南部海域 4地防汛防台风四级应急响应持续</span>
          <span class="news-value-point">💡 中新网10月24日电 据应急管理部网站消息，10月24日上午，国家防总办公室、应急管理部继续组织中国气象局、水利部、自然资源部、工业和信息化部、…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720280.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网兰州10月24日电 (记者 高莹)兰新铁路是新亚欧大陆桥中国段西通道核心干线，也是中欧班列西行出境的必经之路。保障跨境货运班列安全准点通行，是兰州铁路局嘉峪关机务段肩负的重要使命。" data-title="嘉峪关机务段数智赋能守护兰新丝路运输通道" data-date="10-24 13:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:27</span>
          <span class="news-item-title">嘉峪关机务段数智赋能守护兰新丝路运输通道</span>
          <span class="news-value-point">💡 中新网兰州10月24日电 (记者 高莹)兰新铁路是新亚欧大陆桥中国段西通道核心干线，也是中欧班列西行出境的必经之路</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720270.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南京10月24日电 (记者 朱晓颖)受今年第30号台风“蔷琵”影响，为确保铁路运输和旅客出行安全，长三角铁路部门启动应急响应，调整列车开行方案，对23日17时至24日24时杭深铁路、金温铁路、杭台高铁等线路部分区段采取临时限速措施，对24日杭深铁路、金温铁路、杭台高铁等线路部分途经列车临时停运。" data-title="受台风“蔷琵”影响 长三角铁路部门调整列车开行方案" data-date="10-24 13:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:24</span>
          <span class="news-item-title">受台风“蔷琵”影响 长三角铁路部门调整列车开行方案</span>
          <span class="news-value-point">💡 中新网南京10月24日电 (记者 朱晓颖)受今年第30号台风“蔷琵”影响，为确保铁路运输和旅客出行安全，长三角铁路部门启动应急响应，调整列车开行…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-24/10720287.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社厦门10月24日电 题：在厦门市集品尝提速送达的台湾鲜味" data-title="在厦门市集品尝提速送达的台湾鲜味" data-date="10-24 13:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 13:01</span>
          <span class="news-item-title">在厦门市集品尝提速送达的台湾鲜味</span>
          <span class="news-value-point">💡 中新社厦门10月24日电 题：在厦门市集品尝提速送达的台湾鲜味</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/archdiocese-new-york-sexual-abuse-settlement.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="罗马天主教大主教管区现在可以通过与1300人达成和解来避免破产，这些人说他们被神职人员和非专业领导人虐待。" data-title="New York Archdiocese Close to Settling Sexual Abuse Claims for Over $800 Million" data-date="10-24 12:12" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 12:12</span>
          <span class="news-item-title">纽约大主教管区接近解决超过8亿美元的性虐待索赔</span>
          <span class="news-item-title-en">New York Archdiocese Close to Settling Sexual Abuse Claims for Over $800 Million</span>
          <span class="news-value-point">💡 罗马天主教大主教管区现在可以通过与1300人达成和解来避免破产，这些人说他们被神职人员和非专业领导人虐待</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-24 14:35（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
