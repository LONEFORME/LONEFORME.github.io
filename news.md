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
      <span>2026-11-09 01:59 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · 天空体育×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/08/world/middleeast/israel-eisenkot-netanyahu-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Eisenkot先生是一名职业将领，也是以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）的主要竞争对手，现在将有长达六周的时间组建联盟。" data-title="Who Is Gadi Eisenkot, Israel’s Opposition Leader?" data-date="11-09 01:46" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-09 01:46</span>
      </div>
      <h2 class="hero-featured-title">以色列反对党领袖加迪·艾森科特（ Gadi Eisenkot ）是谁？</h2>
      <div class="hero-featured-title-en">Who Is Gadi Eisenkot, Israel’s Opposition Leader?</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/1029533/elvis-eminem-suno-ai-music-clone-lawsuit" target="_blank" rel="noopener" data-cat="keji" data-summary="Suno正面临另一起诉讼。埃尔维斯·普雷斯利（ Elvis Presley ）音乐的一群版权所有者和阿姆（ Eminem ）一些最大唱片的发行商正在起诉这家AI音乐公司，声称它非法制作模仿这些音乐和歌词的音乐和歌词。" data-title="Elvis and Eminem rights holders are suing Suno" data-date="11-09 01:23" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Elvis and Eminem rights holders are suing Suno</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/nov/08/man-utd-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="格林威治标准时间下午4:30的⚽️英超联赛最新消息乔纳森·威尔逊（⚽️ Jonathan Wilson ） ：埃默⚽️里离开别墅的原因不多| Mail TimSunderland坚持以1-0击败切尔西，这对他们来说是一个很好的结果。还有另一个尴尬" data-title="Manchester United v Aston Villa: Premier League" data-date="11-09 01:58" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Manchester United v Aston Villa: Premier League</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/11661/13279295/brighton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Brighton latest: VOTE - Are Hurzeler&#39;s side genuine PL title contenders?" data-title="Brighton latest: VOTE - Are Hurzeler&#39;s side genuine PL title contenders?" data-date="11-09 00:27" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Brighton latest: VOTE - Are Hurzeler's side genuine PL title contenders?</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/world/middleeast/israel-eisenkot-netanyahu-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Eisenkot先生是一名职业将领，也是以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）的主要竞争对手，现在将有长达六周的时间组建联盟。" data-title="Who Is Gadi Eisenkot, Israel’s Opposition Leader?" data-date="11-09 01:46" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 01:46</span>
          <span class="news-item-title">以色列反对党领袖加迪·艾森科特（ Gadi Eisenkot ）是谁？</span>
          <span class="news-item-title-en">Who Is Gadi Eisenkot, Israel’s Opposition Leader?</span>
          <span class="news-value-point">💡 Eisenkot先生是一名职业将领，也是以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）的主要竞争对手，现在将有长达六周…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/trump-midterm-election-america-future.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着美国人吸收了一个惊人的新政治现实，他们面临着他们实际决定与总统完成的时间和他实际完成的时间之间的差距。" data-title="For Trump and America, a Clear Election Verdict but a Murky Future" data-date="11-09 00:25" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 00:25</span>
          <span class="news-item-title">对于特朗普和美国来说，一个明确的选举裁决，但一个模糊的未来</span>
          <span class="news-item-title-en">For Trump and America, a Clear Election Verdict but a Murky Future</span>
          <span class="news-value-point">💡 随着美国人吸收了一个惊人的新政治现实，他们面临着他们实际决定与总统完成的时间和他实际完成的时间之间的差距</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/08/ipswich-bournemouth-premier-league-match-report" target="_blank" rel="noopener" data-cat="shizheng" data-summary="埃文尼尔森的另一个进球帮助马可·罗斯（ Marco Rose ）的伯恩茅斯（ Bournemouth ）连续第八场胜利，在伊普斯维奇（ Ipswich ）以2-1艰难获胜。埃文尼尔森在本赛季的前六场比赛中未能得分，但连续第五次获得总理利亚（ Premier Lea ）的净胜利" data-title="Evanilson launches eighth straight Bournemouth win at blundering Ipswich" data-date="11-09 00:14" data-source="卫报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:14</span>
          <span class="news-item-title">伊万尼尔森在浮躁的伊普斯维奇连续第八次赢得伯恩茅斯</span>
          <span class="news-item-title-en">Evanilson launches eighth straight Bournemouth win at blundering Ipswich</span>
          <span class="news-value-point">💡 埃文尼尔森的另一个进球帮助马可·罗斯（ Marco Rose ）的伯恩茅斯（ Bournemouth ）连续第八场胜利，在伊普斯维奇（ Ipsw…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/hakeem-jeffries-house-democrats-speaker.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="排队成为第一位黑人议长的人是一位保守的温和派，左翼活动人士认为他太胆小，无法对抗特朗普总统。他说，他“非常有能力”把事情做好。" data-title="Hakeem Jeffries, in Line to Become House Speaker, Promises Bold Agenda" data-date="11-09 00:12" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 00:12</span>
          <span class="news-item-title">Hakeem Jeffries ，即将成为众议院议长，承诺大胆的议程</span>
          <span class="news-item-title-en">Hakeem Jeffries, in Line to Become House Speaker, Promises Bold Agenda</span>
          <span class="news-value-point">💡 排队成为第一位黑人议长的人是一位保守的温和派，左翼活动人士认为他太胆小，无法对抗特朗普总统</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728548.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据埃及方面8日消息，一列由埃及首都开罗开往该国南部阿斯旺的列车在埃及吉萨省境内发生脱轨事故，4节车厢脱轨。事故导致列车司机死亡。埃及卫生部长称事故还导致64人受伤。" data-title="埃及列车脱轨事故致司机死亡 64人受伤" data-date="11-08 21:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 21:20</span>
          <span class="news-item-title">埃及列车脱轨事故致司机死亡 64人受伤</span>
          <span class="news-value-point">💡 据埃及方面8日消息，一列由埃及首都开罗开往该国南部阿斯旺的列车在埃及吉萨省境内发生脱轨事故，4节车厢脱轨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728534.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网加德满都11月8日电 (郑怡雯)尼泊尔8日迎来传统“敬狗日”。由尼泊尔总理夫人萨宾娜·卡夫莱发起的庆祝活动在首都加德满都举行。" data-title="尼泊尔举行敬狗日庆祝活动 呼吁关注动物福利" data-date="11-08 21:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 21:02</span>
          <span class="news-item-title">尼泊尔举行敬狗日庆祝活动 呼吁关注动物福利</span>
          <span class="news-value-point">💡 中新网加德满都11月8日电 (郑怡雯)尼泊尔8日迎来传统“敬狗日”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728543.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据埃及方面8日消息，当日发生的列车脱轨事故导致列车司机死亡。" data-title="埃及列车脱轨事故致司机死亡" data-date="11-08 21:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 21:02</span>
          <span class="news-item-title">埃及列车脱轨事故致司机死亡</span>
          <span class="news-value-point">💡 据埃及方面8日消息，当日发生的列车脱轨事故导致列车司机死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728539.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社四川宜宾11月8日电 (程兆)以“共筑互信桥梁，开启合作新局”为主题的2026中国北欧民间友好对话会8日在四川宜宾举办。来自中国有关部门、地方政府及瑞典、丹麦、芬兰、挪威、冰岛五国友好组织等各界的代表约100人参会，探讨深化民间交往与务实合作的路径。" data-title="2026中国北欧民间友好对话会在四川宜宾举行" data-date="11-08 21:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 21:02</span>
          <span class="news-item-title">2026中国北欧民间友好对话会在四川宜宾举行</span>
          <span class="news-value-point">💡 中新社四川宜宾11月8日电 (程兆)以“共筑互信桥梁，开启合作新局”为主题的2026中国北欧民间友好对话会8日在四川宜宾举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728540.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达11月8日电 (记者 李志全)印度尼西亚一架执行森林和土地火灾扑救任务的直升机8日在南加里曼丹省巴里托瓜拉县坠入巴里托河，机上2人获救，1人遇难。" data-title="印尼一周内发生两起灭火直升机坠毁事故" data-date="11-08 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 21:01</span>
          <span class="news-item-title">印尼一周内发生两起灭火直升机坠毁事故</span>
          <span class="news-value-point">💡 中新社雅加达11月8日电 (记者 李志全)印度尼西亚一架执行森林和土地火灾扑救任务的直升机8日在南加里曼丹省巴里托瓜拉县坠入巴里托河，机上2人获…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728530.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月8日电 综合外媒8日报道，埃及吉萨省发生火车脱轨事故，已致约50人受伤。" data-title="埃及发生火车脱轨事故 已致约50人受伤" data-date="11-08 20:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 20:46</span>
          <span class="news-item-title">埃及发生火车脱轨事故 已致约50人受伤</span>
          <span class="news-value-point">💡 中新网11月8日电 综合外媒8日报道，埃及吉萨省发生火车脱轨事故，已致约50人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728529.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：据埃及媒体8日报道，一列由埃及首都开罗开往该国南部阿斯旺的列车当天在埃及吉萨省境内发生脱轨事故，4节车厢脱轨，导致至少50人受伤。" data-title="新华社快讯：埃及发生列车脱轨事故致至少50人受伤" data-date="11-08 20:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 20:44</span>
          <span class="news-item-title">新华社快讯：埃及发生列车脱轨事故致至少50人受伤</span>
          <span class="news-value-point">💡 新华社快讯：据埃及媒体8日报道，一列由埃及首都开罗开往该国南部阿斯旺的列车当天在埃及吉萨省境内发生脱轨事故，4节车厢脱轨，导致至少50人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728528.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：手无寸铁的百万兵" data-title="没有一兵一卒，一支笔却“胜过百万兵”，他们是谁？" data-date="11-08 20:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 20:38</span>
          <span class="news-item-title">没有一兵一卒，一支笔却“胜过百万兵”，他们是谁？</span>
          <span class="news-value-point">💡 原标题：手无寸铁的百万兵</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728521.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月8日电 作为东道主服务中外记者采访报道的重要数字基础设施——2026年亚太经合组织(APEC)领导人会议周新闻中心网站(press.apec2026.cn)8日上线运行。" data-title="2026年APEC领导人会议周新闻中心网站上线" data-date="11-08 20:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 20:37</span>
          <span class="news-item-title">2026年APEC领导人会议周新闻中心网站上线</span>
          <span class="news-value-point">💡 中新社深圳11月8日电 作为东道主服务中外记者采访报道的重要数字基础设施——2026年亚太经合组织(APEC)领导人会议周新闻中心网站(pres…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728499.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社上海11月8日电(记者阚静文#8195;陆佳飞#8195;宿亮)第九届进博会上，展商来自五洲四海，展品覆盖千行百业。一场展会，万千“不同”。置身现场，既能感受到“回头客”的信任，也能体会到“头回客”的热情。参展故事各不相同，相同的，是对进博会的信心与期待。" data-title="透视进博｜在进博会，寻找“不同”的答案" data-date="11-08 19:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 19:54</span>
          <span class="news-item-title">透视进博｜在进博会，寻找“不同”的答案</span>
          <span class="news-value-point">💡 新华社上海11月8日电(记者阚静文#8195;陆佳飞#8195;宿亮)第九届进博会上，展商来自五洲四海，展品覆盖千行百业</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/07/science/space/holley-bockelmann-astrophysicist-space-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="凯莉·霍利-博克尔曼（ Kelly Holley-Bockelmann ）是美国顶尖的天体物理学家之一，直到特朗普总统的政策影响了她工作的方方面面。" data-title="Top Astrophysicist Leaves U.S. After Trump Policies Affect Her Work" data-date="11-08 19:49" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 19:49</span>
          <span class="news-item-title">在特朗普政策影响她的工作后，顶级天体物理学家离开美国</span>
          <span class="news-item-title-en">Top Astrophysicist Leaves U.S. After Trump Policies Affect Her Work</span>
          <span class="news-value-point">💡 凯莉·霍利-博克尔曼（ Kelly Holley-Bockelmann ）是美国顶尖的天体物理学家之一，直到特朗普总统的政策影响了她工作的方方面…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">10 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1029533/elvis-eminem-suno-ai-music-clone-lawsuit" target="_blank" rel="noopener" data-cat="keji" data-summary="Suno正面临另一起诉讼。埃尔维斯·普雷斯利（ Elvis Presley ）音乐的一群版权所有者和阿姆（ Eminem ）一些最大唱片的发行商正在起诉这家AI音乐公司，声称它非法制作模仿这些音乐和歌词的音乐和歌词。" data-title="Elvis and Eminem rights holders are suing Suno" data-date="11-09 01:23" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-09 01:23</span>
          <span class="news-item-title">猫王和Eminem权利人起诉Suno</span>
          <span class="news-item-title-en">Elvis and Eminem rights holders are suing Suno</span>
          <span class="news-value-point">💡 Suno正面临另一起诉讼</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/013.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 8 日消息，彭博社记者马克 · 古尔曼在今天（8 日）晚间更新的《Power On》时事通讯中披露，苹果新任 CEO 约翰 · 特努斯敦促软件工程主管克雷格 · 费德里吉加快 AI 业务发展，采取更大胆的策略，目标是将 Siri 升级为能够自主替用户完成任务的 AI 智能体。上周的财报电话会议上，特努斯对苹果的 AI 业务表现得相当乐观。谈及新版 Siri 时特努斯更是自信十足：苹果终于实现了多年来的设想，公司 AI 业务迎来了新篇章。“我们对收到的评价和反馈非常满意，也非常高兴看到越来越多的用户能够体验到它。”但在苹果内部，特努斯的态度却截然不同。他深知苹果仍远远落后于竞争对手。最近几周，特努斯与去年接替原 AI 负责人、掌管苹果 AI 业务的费德里吉举行了一次闭门会议" data-title="古尔曼称苹果 CEO 特努斯“上任三把火”，敦促软件主管费德里吉大胆搞 AI" data-date="11-08 23:36" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 23:36</span>
          <span class="news-item-title">古尔曼称苹果 CEO 特努斯“上任三把火”，敦促软件主管费德里吉大胆搞 AI</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，彭博社记者马克 · 古尔曼在今天（8 日）晚间更新的《Power On》时事通讯中披露，苹果新任 CEO 约翰 …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cooling/diamond-foundry-creates-worlds-first-200mm-single-crystal-diamond-wafer-massive-gem-aims-to-solve-ai-chip-cooling-crisis-envisioned-as-a-cooling-material-for-semiconductors" target="_blank" rel="noopener" data-cat="keji" data-summary="这款200毫米单晶金刚石晶圆旨在有效去除热量并防止AI处理器上形成热点。" data-title="Diamond Foundry creates world&#39;s first 200mm single-crystal diamond wafer" data-date="11-08 23:25" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 23:25</span>
          <span class="news-item-title">Diamond Foundry打造全球首款200mm单晶金刚石晶圆</span>
          <span class="news-item-title-en">Diamond Foundry creates world's first 200mm single-crystal diamond wafer</span>
          <span class="news-value-point">💡 这款200毫米单晶金刚石晶圆旨在有效去除热量并防止AI处理器上形成热点</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/010.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 8 日消息，蚂蚁集团旗下 AI 助手灵光宣布：自今年 10 月 27 日灵光 2.0 上线以来，一周内已帮助用户管理超 116 万项事务，执行超 360 万次任务。灵光用户已突破 2000 万。参考IT之家先前报道，蚂蚁集团于 10 月 27 日发布灵光 2.0，其最大特性是 AI 介入任务的起点进一步前移。过去，用户需要先发现问题、提出需求，再由 AI 执行；如今，在获得用户授权后，灵光能够结合已接入的信息与服务，主动识别潜在需求，并发起分析、监测和跟进，并在需要用户关注的节点及时提醒。AI 不再只是等待指令的工具，而开始成为能够持续管理事务的助手。除此之外，灵光 2.0 还接入了蚂蚁 APASS，作为 AI 时代跨智能体、跨设备、跨应用与服务场景的统一账号和安全管理基" data-title="蚂蚁集团：旗下 AI 助手灵光用户数量已突破 2000 万，2.0 版本上线一周已帮助用户管理超 116 万项事务" data-date="11-08 22:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 22:47</span>
          <span class="news-item-title">蚂蚁集团：旗下 AI 助手灵光用户数量已突破 2000 万，2.0 版本上线一周已帮助用户管理超 116 万项事务</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，蚂蚁集团旗下 AI 助手灵光宣布：自今年 10 月 27 日灵光 2.0 上线以来，一周内已帮助用户管理超 11…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/linux/the-end-of-an-era-as-linux-7-5-purges-the-last-30-year-old-intel-mmx-optimizations-from-pentium-age-open-source-os-retires-ancient-1997-pentium-instructions-to-streamline-code" target="_blank" rel="noopener" data-cat="keji" data-summary="Linux开发人员正准备让英特尔古老的多媒体扩展变得无关紧要，现在将从内核中删除最后一段MMX代码。" data-title="The end of an era as Linux 7.5 purges the last 30-year-old Intel MMX optimizations from Pentium age" data-date="11-08 22:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 22:40</span>
          <span class="news-item-title">Linux 7.5时代的结束清除了奔腾时代过去30年的英特尔MMX优化</span>
          <span class="news-item-title-en">The end of an era as Linux 7.5 purges the last 30-year-old Intel MMX optimizations from Pentium age</span>
          <span class="news-value-point">💡 Linux开发人员正准备让英特尔古老的多媒体扩展变得无关紧要，现在将从内核中删除最后一段MMX代码</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-released-its-8800-gtx-gpu-20-years-ago-today-celebrates-with-steam-game-homage-interactive-demos-eye-watering-minimum-requirements-include-rtx-4070-32gb-ram-and-30gb-storage" target="_blank" rel="noopener" data-cat="keji" data-summary="在2006年的这一天，英伟达发布了传奇的GeForce 8800 GTX显卡，并以非常苛刻（但免费）的交互式Steam演示来庆祝这一事件。" data-title="Nvidia released its 8800 GTX GPU 20 years ago today, celebrates with Steam game homage" data-date="11-08 22:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 22:20</span>
          <span class="news-item-title">Nvidia在20年前的今天发布了其8800 GTX GPU ，以Steam游戏致敬</span>
          <span class="news-item-title-en">Nvidia released its 8800 GTX GPU 20 years ago today, celebrates with Steam game homage</span>
          <span class="news-value-point">💡 在2006年的这一天，英伟达发布了传奇的GeForce 8800 GTX显卡，并以非常苛刻（但免费）的交互式Steam演示来庆祝这一事件</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728516.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社合肥11月8日电 (记者 张俊)中国首款可互联中性原子量子计算机“干阵”原型机8日在安徽省合肥市发布。" data-title="中国首款可互联中性原子量子计算机“干阵”原型机在合肥发布" data-date="11-08 20:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 20:40</span>
          <span class="news-item-title">中国首款可互联中性原子量子计算机“干阵”原型机在合肥发布</span>
          <span class="news-value-point">💡 中新社合肥11月8日电 (记者 张俊)中国首款可互联中性原子量子计算机“干阵”原型机8日在安徽省合肥市发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728502.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="新华社北京11月8日电#8195;专访｜“推动全球人工智能治理不断完善，中国是正确的”——访俄罗斯塔斯社社长安德烈·孔德拉绍夫" data-title="专访｜“推动全球人工智能治理不断完善，中国是正确的”" data-date="11-08 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 20:07</span>
          <span class="news-item-title">专访｜“推动全球人工智能治理不断完善，中国是正确的”</span>
          <span class="news-value-point">💡 新华社北京11月8日电#8195;专访｜“推动全球人工智能治理不断完善，中国是正确的”——访俄罗斯塔斯社社长安德烈·孔德拉绍夫</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508466.html" target="_blank" rel="noopener" data-cat="keji" data-summary="没有永远的夏天" data-title="资本正在撤离“世界模型”" data-date="11-08 12:09" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-08 12:09</span>
          <span class="news-item-title">资本正在撤离“世界模型”</span>
          <span class="news-value-point">💡 没有永远的夏天</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，今年早些时候分发的一份备忘录声称，中国国家安全部聘请了一名女性技术高管来监视英伟达的首席执行官。" data-title="Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo" data-date="11-08 05:17" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-08 05:17</span>
          <span class="news-item-title">根据美国情报备忘录， Megaspeed高管被招募来监视Nvidia首席执行官</span>
          <span class="news-item-title-en">Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo</span>
          <span class="news-value-point">💡 据报道，今年早些时候分发的一份备忘录声称，中国国家安全部聘请了一名女性技术高管来监视英伟达的首席执行官</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/08/man-utd-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="格林威治标准时间下午4:30的⚽️英超联赛最新消息乔纳森·威尔逊（⚽️ Jonathan Wilson ） ：埃默⚽️里离开别墅的原因不多| Mail TimSunderland坚持以1-0击败切尔西，这对他们来说是一个很好的结果。还有另一个尴尬" data-title="Manchester United v Aston Villa: Premier League" data-date="11-09 01:58" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 01:58</span>
          <span class="news-item-title">曼联v阿斯顿维拉：英超联赛</span>
          <span class="news-item-title-en">Manchester United v Aston Villa: Premier League</span>
          <span class="news-value-point">💡 格林威治标准时间下午4:30的⚽️英超联赛最新消息乔纳森·威尔逊（⚽️ Jonathan Wilson ） ：埃默⚽️里离开别墅的原因不多| M…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-09 00:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:42</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/08/crystal-palace-v-liverpool-brighton-v-brentford-and-more-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰击败切尔西脱颖而出，布莱顿击败布伦特福德排名第二，而利物浦在击败水晶宫后排名第四。伊普斯维奇的灾难性进球！主队的守门员克里斯·沃尔顿（ Chris Walton ）试图将球带过" data-title="Crystal Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, and more: Premier League – as it happened" data-date="11-09 00:35" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:35</span>
          <span class="news-item-title">水晶宫1-3利物浦，桑德兰1-0切尔西和更多：英超联赛–事实如此</span>
          <span class="news-item-title-en">Crystal Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, and more: Premier League – as it happened</span>
          <span class="news-value-point">💡 桑德兰击败切尔西脱颖而出，布莱顿击败布伦特福德排名第二，而利物浦在击败水晶宫后排名第四</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/08/brighton-brentford-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="谁能阻止布莱顿在英格兰和欧洲足球的崛起？他们继续设定标准，让几乎所有其他人都落后于他们的做法。他们在英超联赛中排名第二的位置曾经读起来像一个小故障" data-title="Diego Gómez hits another stunner as Brighton beat 10-man Brentford to go second" data-date="11-09 00:17" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:17</span>
          <span class="news-item-title">迭戈·戈麦斯（ Diego Gómez ）击败布莱顿（ Brighton ）击败10人布伦特福德（ Brentford ）获得第二</span>
          <span class="news-item-title-en">Diego Gómez hits another stunner as Brighton beat 10-man Brentford to go second</span>
          <span class="news-value-point">💡 谁能阻止布莱顿在英格兰和欧洲足球的崛起</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/08/sunderland-chelsea-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="五个半月内可能会有很多变化，但随着本周Wearside的初冬寒意–无论是气象还是隐喻–桑德兰都决定有些事情应该保持不变。就在他们击败切尔西的时候" data-title="Le Fée’s penalty stuns Chelsea and breathes life into defiant Sunderland" data-date="11-09 00:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:16</span>
          <span class="news-item-title">勒菲的点球让切尔西眩晕，为反抗的桑德兰注入活力</span>
          <span class="news-item-title-en">Le Fée’s penalty stuns Chelsea and breathes life into defiant Sunderland</span>
          <span class="news-value-point">💡 五个半月内可能会有很多变化，但随着本周Wearside的初冬寒意–无论是气象还是隐喻–桑德兰都决定有些事情应该保持不变</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/08/crystal-palace-liverpool-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="就在那一刻，利物浦知道他们将在伦敦南部赢得比赛，因此从上周日的英超联赛失利转会到安菲尔德的阿森纳，以及周中在欧洲冠军联赛的费内巴切。弗洛里安·维尔茨（ Florian Wirtz ）将他的比赛时间定为李" data-title="Wirtz provides quality to seal Liverpool win over lacklustre Crystal Palace" data-date="11-09 00:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:16</span>
          <span class="news-item-title">Wirtz为利物浦赢得平淡无奇的水晶宫提供了优质服务</span>
          <span class="news-item-title-en">Wirtz provides quality to seal Liverpool win over lacklustre Crystal Palace</span>
          <span class="news-value-point">💡 就在那一刻，利物浦知道他们将在伦敦南部赢得比赛，因此从上周日的英超联赛失利转会到安菲尔德的阿森纳，以及周中在欧洲冠军联赛的费内巴切</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c94g1n4pzev3o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="恩佐·勒菲（ Enzo Le Fee ）的点球是桑德兰（ Sunderland ）从桌子底部爬下来的差异，但球员们如何对阵切尔西？" data-title="Failed to deal with Brobbey - player ratings for Sunderland v Chelsea" data-date="11-09 00:13" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 00:13</span>
          <span class="news-item-title">未能处理Brobbey -桑德兰对切尔西的球员评分</span>
          <span class="news-item-title-en">Failed to deal with Brobbey - player ratings for Sunderland v Chelsea</span>
          <span class="news-value-point">💡 恩佐·勒菲（ Enzo Le Fee ）的点球是桑德兰（ Sunderland ）从桌子底部爬下来的差异，但球员们如何对阵切尔西</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqkgjm2dlpv6o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="水晶宫和利物浦的球员在英超比赛后的评分。" data-title="Who was back to his best? Player ratings for Crystal Palace v Liverpool" data-date="11-09 00:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 00:04</span>
          <span class="news-item-title">谁恢复了最佳状态？水晶宫对利物浦的球员评分</span>
          <span class="news-item-title-en">Who was back to his best? Player ratings for Crystal Palace v Liverpool</span>
          <span class="news-value-point">💡 水晶宫和利物浦的球员在英超比赛后的评分</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279298/crystal-palace-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Palace latest: Carragher expects Sage to be sacked after Liverpool loss" data-title="Palace latest: Carragher expects Sage to be sacked after Liverpool loss" data-date="11-09 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 00:00</span>
          <span class="news-item-title">宫殿最新消息： Carragher预计Sage将在利物浦输球后被解雇</span>
          <span class="news-item-title-en">Palace latest: Carragher expects Sage to be sacked after Liverpool loss</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/brighton-and-hove-albion-vs-brentford/report/559535" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿以2比0战胜10人布伦特福德，超越曼城，在英超联赛中排名第二。" data-title="Brighton beat 10-man Brentford to leapfrog Man City into second" data-date="11-09 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 00:00</span>
          <span class="news-item-title">布莱顿击败10人布伦特福德，超越曼城跻身第二</span>
          <span class="news-item-title-en">Brighton beat 10-man Brentford to leapfrog Man City into second</span>
          <span class="news-value-point">💡 布莱顿以2比0战胜10人布伦特福德，超越曼城，在英超联赛中排名第二</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/ipswich-town-vs-bournemouth/report/559539" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="伯恩茅斯在所有比赛中连续八场胜利，他们在伊普斯维奇以2比1的胜利继续夺得英超联赛冠军。" data-title="Bournemouth win at Ipswich to record eight straight victories" data-date="11-09 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 00:00</span>
          <span class="news-item-title">伯恩茅斯在伊普斯维奇赢得连续八场胜利</span>
          <span class="news-item-title-en">Bournemouth win at Ipswich to record eight straight victories</span>
          <span class="news-value-point">💡 伯恩茅斯在所有比赛中连续八场胜利，他们在伊普斯维奇以2比1的胜利继续夺得英超联赛冠军</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/sunderland-vs-chelsea/report/559543" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西表现不温不火，桑德兰以1-0的胜利脱颖而出，缓解了火力不足的经理雷吉斯·勒布里斯的压力。" data-title="Tepid Chelsea beaten by Sunderland who move off the bottom" data-date="11-09 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 00:00</span>
          <span class="news-item-title">特皮德·切尔西（ Tepid Chelsea ）被桑德兰（ Sunderland ）击败，后</span>
          <span class="news-item-title-en">Tepid Chelsea beaten by Sunderland who move off the bottom</span>
          <span class="news-value-point">💡 切尔西表现不温不火，桑德兰以1-0的胜利脱颖而出，缓解了火力不足的经理雷吉斯·勒布里斯的压力</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609757/goal-f-wirtz-54-crystal-palace-0-2-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Wirtz结束了12场比赛的PL进球干旱，将利物浦的领先优势翻了一番。" data-title="Wirtz ends 12-game PL goal drought to double Liverpool’s lead over Palace" data-date="11-08 23:19" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 23:19</span>
          <span class="news-item-title">Wirtz结束了12场比赛的PL进球干旱，将利物浦的领先优势翻了一番</span>
          <span class="news-item-title-en">Wirtz ends 12-game PL goal drought to double Liverpool’s lead over Palace</span>
          <span class="news-value-point">💡 Wirtz结束了12场比赛的PL进球干旱，将利物浦的领先优势翻了一番</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-united-vs-aston-villa/live/559541" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="CALAMITY! Man Utd&#39;s awful defending gifts Aston Villa the lead LIVE!" data-title="CALAMITY! Man Utd&#39;s awful defending gifts Aston Villa the lead LIVE!" data-date="11-08 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 23:00</span>
          <span class="news-item-title">灾难！曼联的可怕防守礼物阿斯顿维拉现场直播！</span>
          <span class="news-item-title-en">CALAMITY! Man Utd's awful defending gifts Aston Villa the lead LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609739/goal-a-mac-allister-crystal-palace-0-1-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Mac Allister回到家中， Szoboszlai的任意球给了利物浦揭幕战。" data-title="Mac Allister heads home Szoboszlai&#39;s free kick to give Liverpool opener" data-date="11-08 22:46" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 22:46</span>
          <span class="news-item-title">Mac Allister回家Szoboszlai的任意球给利物浦揭幕战</span>
          <span class="news-item-title-en">Mac Allister heads home Szoboszlai's free kick to give Liverpool opener</span>
          <span class="news-value-point">💡 Mac Allister回到家中， Szoboszlai的任意球给了利物浦揭幕战</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279295/brighton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Brighton latest: VOTE - Are Hurzeler&#39;s side genuine PL title contenders?" data-title="Brighton latest: VOTE - Are Hurzeler&#39;s side genuine PL title contenders?" data-date="11-09 00:27" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 00:27</span>
          <span class="news-item-title">布莱顿最新：投票-赫泽勒的球队是真正的PL冠军竞争者吗？</span>
          <span class="news-item-title-en">Brighton latest: VOTE - Are Hurzeler's side genuine PL title contenders?</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1029019/apple-macbook-air-13-15-inch-m5-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="最新的13英寸MacBook Air目前售价为$ 1,099.99 ，这是继该公司夏季价格大幅上涨之后，我们第二次看到200 $的折扣。虽然基本型号—采用苹果M5处理器， 1" data-title="Apple’s M5 MacBook Air is down to its lowest price since July" data-date="11-09 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-09 00:00</span>
          <span class="news-item-title">苹果M5 MacBook Air降至7月以来最低价</span>
          <span class="news-item-title-en">Apple’s M5 MacBook Air is down to its lowest price since July</span>
          <span class="news-value-point">💡 最新的13英寸MacBook Air目前售价为$ 1,099.99 ，这是继该公司夏季价格大幅上涨之后，我们第二次看到200 $的折扣</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/014.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，彭博社记者马克 · 古尔曼在今晚更新的《Power On》时事通讯中爆料，曾主导 Vision Pro 头显开发、同时负责新版 Siri AI 项目的迈克 · 罗克韦尔，仍在认真考虑离开现有岗位。古尔曼披露，罗克韦尔或将于明年卸任 Siri 工程副总裁，甚至彻底离开苹果。新版 Siri 跳票了两年才得以上市，考虑到罗克韦尔在其中发挥的作用，他的离开将给苹果造成重大损失。IT之家获悉，如果罗克韦尔最终离职，或在苹果内部转任其他岗位，更多工作预计将交给两名高管：去年从谷歌加入苹果、负责加强 AI 业务的阿马尔 · 苏布拉马尼亚，以及费德里吉的副手塞巴斯蒂安 · 马里诺。苹果内部一些人认为，马里诺未来有望接替费德里吉出任软件工程主管，而且他对 AI 发展的态度更加积" data-title="古尔曼称苹果 Siri AI 团队或迎大调整，工程副总裁罗克韦尔考虑明年走人" data-date="11-08 23:47" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 23:47</span>
          <span class="news-item-title">古尔曼称苹果 Siri AI 团队或迎大调整，工程副总裁罗克韦尔考虑明年走人</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，彭博社记者马克 · 古尔曼在今晚更新的《Power On》时事通讯中爆料，曾主导 Vision Pro 头显开发…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/012.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，美国 CNBC 分析亚马逊的招聘信息发现，过去几个月，亚马逊组建了一支新团队，准备开发一款前所未有的机器人产品。亚马逊近期发布的一则工程师招聘信息写道：“机器人即将走出电影，进入我们的家中。”这条被撤掉的招聘信息透露，新产品能够适应不断变化的家庭环境，并在人类家庭成员身边自主活动。亚马逊一向愿意押注长期项目，即便短期内不被外界理解，只要能够帮助公司抢占新市场的先机，就值得投入。此前的 Alexa 语音助手和 Kindle 电子书阅读器，都采用了这种发展策略。亚马逊 CEO 安迪 · 贾西在最近的年度股东信中重申了这一思路，认为人工智能和机器人技术将带来人们一生中最重大的变革之一。“我们努力预判什么能让客户每天的生活更轻松、更美好，并创造下一个重大转折点。”Li" data-title="亚马逊成立新团队专攻家用机器人，剑指“前所未有”的新产品" data-date="11-08 23:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 23:24</span>
          <span class="news-item-title">亚马逊成立新团队专攻家用机器人，剑指“前所未有”的新产品</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，美国 CNBC 分析亚马逊的招聘信息发现，过去几个月，亚马逊组建了一支新团队，准备开发一款前所未有的机器人产品</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/live-blog/12040/13608639/f1-sao-paulo-gp-live-race-updates-results-stream-and-highlights-from-20th-round-of-2026-formula-1-season-in-brazil-at-interlagos" target="_blank" rel="noopener" data-cat="zonghe" data-summary="关注现场更新，观看巴西圣保罗大奖赛的最佳视频。观看Sky Sports F1直播" data-title="Sao Paulo GP: Norris leads Hadjar with rain expected to return LIVE!" data-date="11-08 23:20" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 23:20</span>
          <span class="news-item-title">圣保罗大奖赛：诺里斯带领哈贾尔，预计雨水将现场回归！</span>
          <span class="news-item-title-en">Sao Paulo GP: Norris leads Hadjar with rain expected to return LIVE!</span>
          <span class="news-value-point">💡 关注现场更新，观看巴西圣保罗大奖赛的最佳视频</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1029526/chatbots-might-be-coming-to-apples-homeview" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IOS 27.3测试版的代码表明，苹果可能会在其智能家居中心增加对聊天机器人的支持。“对话式应用”类别列出了一个标记。虽然没有关于哪些应用程序属于该标题的细节，但似乎有理由认为" data-title="Chatbots might be coming to Apple’s HomeView" data-date="11-08 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-08 23:00</span>
          <span class="news-item-title">聊天机器人可能会进入Apple的HomeView</span>
          <span class="news-item-title-en">Chatbots might be coming to Apple’s HomeView</span>
          <span class="news-value-point">💡 IOS 27.3测试版的代码表明，苹果可能会在其智能家居中心增加对聊天机器人的支持</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/011.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，特斯拉计划对 Cybercab 进行多项重大升级，带来能效提升和新的车身配色。今天（8 日）凌晨，特斯拉 CEO 马斯克在 X 上透露，公司还将进一步改进 Cybercab。“我们会进一步提高能效，让 Cybercab 用上 40kWh 电池组。我们还会推出液态银色，免得车身颜色太单调。”据IT之家了解，本周早些时候，特斯拉宣布将取消得州超级工厂的 Cybertruck 生产线，把产能腾出来生产更多 Cybercab。能效更高的新款 Cybercab 有望帮助特斯拉提高盈利能力和利润率。从商业角度来看，也让停产 Cybertruck 的主张更有说服力。目前在得克萨斯州奥斯汀投入 Robotaxi 运营的 Cybercab 配备 48kWh 电池组。从马斯克的表" data-title="马斯克：特斯拉将进一步改进 Cybercab，提升能效、新增配色" data-date="11-08 23:00" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 23:00</span>
          <span class="news-item-title">马斯克：特斯拉将进一步改进 Cybercab，提升能效、新增配色</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，特斯拉计划对 Cybercab 进行多项重大升级，带来能效提升和新的车身配色</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-mice/logitech-g502-x-lightspeed-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="罗技的G502 X Lightspeed剥离了G502 X Plus的照明，但保留了160 $的价格标签。" data-title="Logitech G502 X Lightspeed Review: No lights, same price" data-date="11-08 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 23:00</span>
          <span class="news-item-title">罗技G502 X LIGHTSPEED评测：无灯，价格不变</span>
          <span class="news-item-title-en">Logitech G502 X Lightspeed Review: No lights, same price</span>
          <span class="news-value-point">💡 罗技的G502 X Lightspeed剥离了G502 X Plus的照明，但保留了160 $的价格标签</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/japanese-arcades-suffer-week-long-blackout-following-sega-server-hack-bandai-namco-titles-resume-trial-operations-as-sega-games-remain-offline" target="_blank" rel="noopener" data-cat="zonghe" data-summary="本周，日本视频游戏商场的感官超载在一些场馆中奇怪地消失了。" data-title="Japanese arcades suffer week-long blackout following Sega server hack" data-date="11-08 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 23:00</span>
          <span class="news-item-title">世嘉服务器遭黑客入侵后，日本商场遭遇为期一周的停电</span>
          <span class="news-item-title-en">Japanese arcades suffer week-long blackout following Sega server hack</span>
          <span class="news-value-point">💡 本周，日本视频游戏商场的感官超载在一些场馆中奇怪地消失了</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728568.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原11月8日电 (记者 胡健)山西省太原市“迎泽发布”8日晚间发布通报称，当日发生在迎泽区的火灾致5人遇难。" data-title="山西太原一公寓发生火灾 致5人遇难" data-date="11-08 22:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 22:49</span>
          <span class="news-item-title">山西太原一公寓发生火灾 致5人遇难</span>
          <span class="news-value-point">💡 中新网太原11月8日电 (记者 胡健)山西省太原市“迎泽发布”8日晚间发布通报称，当日发生在迎泽区的火灾致5人遇难</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/robotics/ukraine-builds-combat-robots-to-hunt-russian-troops-in-underground-gas-pipelines-ugvs-adapted-following-15-kilometer-subterranean-assault" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乌克兰正在开发一种新型作战机器人，设计用于在地下天然气管道内作战。" data-title="Ukraine builds combat robots to hunt Russian troops in underground gas pipelines" data-date="11-08 22:36" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 22:36</span>
          <span class="news-item-title">乌克兰建造战斗机器人，在地下天然气管道中追捕俄罗斯军队</span>
          <span class="news-item-title-en">Ukraine builds combat robots to hunt Russian troops in underground gas pipelines</span>
          <span class="news-value-point">💡 乌克兰正在开发一种新型作战机器人，设计用于在地下天然气管道内作战</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/009.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，当贝现已在京东上架 H5 第二代电视盒子，该产品主要升级全志 H626 处理器，支持双频 Wi-Fi 6，定价为 469 元，部分地区国补后低至 399 元。该产品尺寸为 98 x 98 x 21.5mm，采用白色配色，正面配备一条多彩呼吸灯，提供五种灯光效果模式。机身背部提供了一个 HDMI 2.1 接口、一个 USB-A 接口、一个 3.5mm 的复合音视频接口。该机搭载了全志 H626 芯片，配备了 2GB RAM 以及 16GB 机身存储空间，具备 8K@24fps 的视频解码能力与 4K@60fps 画面输出能力，并支持 HDR10 与 HDR10+ 技术。机器支持双频 Wi-Fi 6、蓝牙 5.4，运行基于安卓 14 的当贝 OS。IT之家附产品参" data-title="当贝推出 H5 第二代电视盒子：升级全志 H626 处理器，469 元" data-date="11-08 22:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 22:31</span>
          <span class="news-item-title">当贝推出 H5 第二代电视盒子：升级全志 H626 处理器，469 元</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，当贝现已在京东上架 H5 第二代电视盒子，该产品主要升级全志 H626 处理器，支持双频 Wi-Fi 6，定价为…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/magazine/keisha-lance-bottoms-interview.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="佐治亚州州长当选人对她的政党在南方的胜利感到高兴，但他知道重新调整远非安全。" data-title="Keisha Lance Bottoms on What Democrats Have to Do to Not Squander the Win" data-date="11-08 22:31" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 22:31</span>
          <span class="news-item-title">凯莎·兰斯（ Keisha Lance ）谈民主党人必须做些什么才能不挥霍胜利</span>
          <span class="news-item-title-en">Keisha Lance Bottoms on What Democrats Have to Do to Not Squander the Win</span>
          <span class="news-value-point">💡 佐治亚州州长当选人对她的政党在南方的胜利感到高兴，但他知道重新调整远非安全</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c61kd9gnge0ro/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="匈牙利正将其完整的国家安全纪录档案库上载至网上，这些档案可能揭示在1989年前长达40年的共产主义统治期间，谁曾监视邻居、同事、朋友和亲属。" data-title="间谍、线人与秘密警察：匈牙利公开共产统治时期档案" data-date="11-08 21:42" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 21:42</span>
          <span class="news-item-title">间谍、线人与秘密警察：匈牙利公开共产统治时期档案</span>
          <span class="news-value-point">💡 匈牙利正将其完整的国家安全纪录档案库上载至网上，这些档案可能揭示在1989年前长达40年的共产主义统治期间，谁曾监视邻居、同事、朋友和亲属</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/hundreds-arrested-after-microsoft-data-center-protest-turns-violent-stop-dirty-data-centers-coalition-demands-halt-to-ai-data-center-expansion-dutch-police-seize-break-in-tools-suspected-stolen-items-from-construction-site" target="_blank" rel="noopener" data-cat="zonghe" data-summary="目前尚不清楚哪个团体首先进入建筑工地，但这一行动导致150至200名抗议者被捕。" data-title="Hundreds arrested after Microsoft data center protest turns violent" data-date="11-08 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 21:20</span>
          <span class="news-item-title">数百人在微软数据中心抗议演变成暴力事件后被捕</span>
          <span class="news-item-title-en">Hundreds arrested after Microsoft data center protest turns violent</span>
          <span class="news-value-point">💡 目前尚不清楚哪个团体首先进入建筑工地，但这一行动导致150至200名抗议者被捕</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-09 01:59（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
