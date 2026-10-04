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
      <span>2026-10-04 09:54 抓取更新</span>
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
        <span class="channel-count">49</span>
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
        <span class="channel-count">4</span>
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
  <div class="ov-item"><span class="ov-num">49</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · Tom's Hardware×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-04/10707705.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本多个民间团体3日在东京江户川区联合举办“战争展”，展示日本在二战期间发动侵略战争的历史资料，呼吁日本社会坚守和平，反对高市政府扩军修宪动向。主办方表示，希望这些展示，能够让日本民众正确了解历史，阻止日本再次走上战争道路。" data-title="日本民间团体展示侵略战争史料 呼吁日本社会坚守和平" data-date="10-04 09:29" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-04 09:29</span>
      </div>
      <h2 class="hero-featured-title">日本民间团体展示侵略战争史料 呼吁日本社会坚守和平</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.qbitai.com/2026/10/501451.html" target="_blank" rel="noopener" data-cat="keji" data-summary="专业3D模型反而更稀缺了" data-title="GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元" data-date="10-04 08:53" data-source="量子位">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🧠 量子位</span>
      </div>
      <p class="hero-sub-title">GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/577.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队。点球大战中，中国队 4 比 3 取胜，获得本次亚运会男足比赛铜牌。上半场，中国队胡荷韬破门。半场结束，中国男足与对手 1-1 战平。下半场，中国队王钰栋破门。90 分钟双方战成 2-2。这也是中国队时隔 28 年再次获得亚运会男足比赛铜牌！也是亚运会男足项目实行 U23 年龄限制后，中国队首次获得奖牌。IT之家查询获悉，中国男足曾在 1994 年广岛亚运会上获得银牌，并于 1978 年、1998 年两次获得铜牌。本届比赛，中国队时隔 28 年再次闯入亚运会男足四强，并最终登上领奖台。另外，今年 1 月，在 2026 年 U23 亚洲杯半决赛中，中国 U23 男足以" data-title="点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌" data-date="10-03 22:51" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-04/10707715.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国庆假期，云南省德宏傣族景颇族自治州梁河县备好了一场民族文化的盛宴：热烈奔放的目瑙纵歌、穿越时光的庭院剧、充满野趣的稻花鱼体验、烟火氤氲的古镇美食、惬意畅快的山野徒步……" data-title="“甜蜜业态”婚旅：让新人把“我愿意”说给山海听" data-date="10-04 09:57" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">“甜蜜业态”婚旅：让新人把“我愿意”说给山海听</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707705.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本多个民间团体3日在东京江户川区联合举办“战争展”，展示日本在二战期间发动侵略战争的历史资料，呼吁日本社会坚守和平，反对高市政府扩军修宪动向。主办方表示，希望这些展示，能够让日本民众正确了解历史，阻止日本再次走上战争道路。" data-title="日本民间团体展示侵略战争史料 呼吁日本社会坚守和平" data-date="10-04 09:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:29</span>
          <span class="news-item-title">日本民间团体展示侵略战争史料 呼吁日本社会坚守和平</span>
          <span class="news-value-point">💡 日本多个民间团体3日在东京江户川区联合举办“战争展”，展示日本在二战期间发动侵略战争的历史资料，呼吁日本社会坚守和平，反对高市政府扩军修宪动向</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707704.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“完善全球治理和推动多极化的重要力量”" data-title="“完善全球治理和推动多极化的重要力量”" data-date="10-04 09:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:25</span>
          <span class="news-item-title">“完善全球治理和推动多极化的重要力量”</span>
          <span class="news-value-point">💡 “完善全球治理和推动多极化的重要力量”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707687.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="家是最小国，国是千万家。修齐治平、兴亡有责的家国情怀是中华优秀传统文化的重要元素。习近平总书记始终高度重视家国情怀的传承和弘扬，在多个场合深刻阐述“家”“国”关系。一起重温这些深情话语，感悟总书记心中的“家”与“国”。" data-title="学习新语·家国同心丨总书记心中的“家”与“国”" data-date="10-04 09:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:23</span>
          <span class="news-item-title">学习新语·家国同心丨总书记心中的“家”与“国”</span>
          <span class="news-value-point">💡 家是最小国，国是千万家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707680.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="有些浪漫，跨越千年，依旧温柔；有些风韵，历经岁月，熠熠如新。" data-title="微视频｜因为国 所以潮" data-date="10-04 09:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:18</span>
          <span class="news-item-title">微视频｜因为国 所以潮</span>
          <span class="news-value-point">💡 有些浪漫，跨越千年，依旧温柔</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707701.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据哥伦比亚广播公司(CBS)当地时间3日援引美国海岸警卫队和美国联邦航空管理局消息，一架载有6人的小型飞机在从百慕大飞往波士顿途中失联。目前救援方已展开大规模搜寻工作。" data-title="一小型飞机从百慕大飞波士顿途中失联 从2.4万英尺急降至1.1万英尺" data-date="10-04 09:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:12</span>
          <span class="news-item-title">一小型飞机从百慕大飞波士顿途中失联 从2.4万英尺急降至1.1万英尺</span>
          <span class="news-value-point">💡 中新网10月4日电 据哥伦比亚广播公司(CBS)当地时间3日援引美国海岸警卫队和美国联邦航空管理局消息，一架载有6人的小型飞机在从百慕大飞往波士…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707692.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据朝中社4日报道，朝鲜3日凌晨在东部地区进行了中程战略导弹发射训练。朝鲜劳动党总书记、国务委员长金正恩现场观摩训练。" data-title="朝中社：金正恩观摩中程战略导弹发射训练（图）" data-date="10-04 09:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:07</span>
          <span class="news-item-title">朝中社：金正恩观摩中程战略导弹发射训练（图）</span>
          <span class="news-value-point">💡 中新网10月4日电 据朝中社4日报道，朝鲜3日凌晨在东部地区进行了中程战略导弹发射训练</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707675.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据朝鲜方面4日消息，朝鲜3日凌晨在东部地区进行了中程战略导弹发射训练。朝鲜劳动党总书记、国务委员长金正恩现场观摩训练。" data-title="金正恩观摩中程战略导弹发射训练" data-date="10-04 07:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 07:07</span>
          <span class="news-item-title">金正恩观摩中程战略导弹发射训练</span>
          <span class="news-value-point">💡 据朝鲜方面4日消息，朝鲜3日凌晨在东部地区进行了中程战略导弹发射训练</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707673.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月3日，据伊朗方面消息，过去5天内，伊朗伊斯兰革命卫队海军在霍尔木兹海峡针对至少7艘“违规”油轮采取行动。" data-title="伊朗革命卫队近日对7艘“违规”油轮采取行动" data-date="10-04 06:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 06:52</span>
          <span class="news-item-title">伊朗革命卫队近日对7艘“违规”油轮采取行动</span>
          <span class="news-value-point">💡 当地时间10月3日，据伊朗方面消息，过去5天内，伊朗伊斯兰革命卫队海军在霍尔木兹海峡针对至少7艘“违规”油轮采取行动</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/03/upshot/polls-midterms-senate-times-siena.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在特朗普总统在2024年轻松获胜的州，五项新的泰晤士报/锡耶纳民意调查继续为民主党人带来强劲的结果。" data-title="Democrats May Have Found the Recipe for Flipping Red" data-date="10-03 23:16" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-03 23:16</span>
          <span class="news-item-title">民主党人可能已经找到了翻转红色的秘诀</span>
          <span class="news-item-title-en">Democrats May Have Found the Recipe for Flipping Red</span>
          <span class="news-value-point">💡 在特朗普总统在2024年轻松获胜的州，五项新的泰晤士报/锡耶纳民意调查继续为民主党人带来强劲的结果</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-03/10707660.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这个假期，有人假日不休、生产不停，还有人坚守战位、守护安全。国庆佳节，正在远海执行护航任务的海军第49批护航编队，举行了一场特殊的升旗仪式。五星红旗在深蓝大洋上升起，护航官兵坚守战位，用忠诚与担当，在远海大洋护卫国际航道安全。" data-title="国庆假期 海军编队坚守战位 护卫国际航道安全" data-date="10-03 22:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-03 22:07</span>
          <span class="news-item-title">国庆假期 海军编队坚守战位 护卫国际航道安全</span>
          <span class="news-value-point">💡 这个假期，有人假日不休、生产不停，还有人坚守战位、守护安全</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-03/10707653.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="央视网消息：长征的征途，既有翻越天险的战斗行军，也有军民共处的岁月。1935年，红一方面军和红四方面军先后完成翻雪山、过草地的艰苦行军。同年8月，红二十五军先期北上，进入宁夏南部地区，他们在西吉兴隆镇一带休整，与当地百姓结下了不解之缘。" data-title="新的长征之路 | 九十载军民情 小小“红军粉”铺就富民振兴路" data-date="10-03 22:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">新的长征之路 | 九十载军民情 小小“红军粉”铺就富民振兴路</span>
          <span class="news-value-point">💡 央视网消息：长征的征途，既有翻越天险的战斗行军，也有军民共处的岁月</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-03/10707627.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="策划：张芮绮、丁翊睿" data-title="学习进行时丨中国式现代化，民生为大" data-date="10-03 21:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-03 21:35</span>
          <span class="news-item-title">学习进行时丨中国式现代化，民生为大</span>
          <span class="news-value-point">💡 策划：张芮绮、丁翊睿</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-03/10707638.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月3日电 中国外交部发言人郭嘉昆10月3日答记者问时表示，中方欢迎普京总统出席今年11月将在深圳举行的亚太经合组织(APEC)领导人非正式会议。" data-title="中方：欢迎普京总统出席APEC领导人非正式会议" data-date="10-03 21:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-03 21:24</span>
          <span class="news-item-title">中方：欢迎普京总统出席APEC领导人非正式会议</span>
          <span class="news-value-point">💡 中新社北京10月3日电 中国外交部发言人郭嘉昆10月3日答记者问时表示，中方欢迎普京总统出席今年11月将在深圳举行的亚太经合组织(APEC)领导…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-03/10707636.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月3日电 中国外交部发言人郭嘉昆10月3日答记者问时表示，所谓新疆存在“种族灭绝”是赤裸裸的谎言。美方有关机构惯于出于政治目的无中生有、攻击抹黑中国，毫无信誉可言。" data-title="中方：所谓新疆存在“种族灭绝”是赤裸裸的谎言" data-date="10-03 21:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-03 21:24</span>
          <span class="news-item-title">中方：所谓新疆存在“种族灭绝”是赤裸裸的谎言</span>
          <span class="news-value-point">💡 中新社北京10月3日电 中国外交部发言人郭嘉昆10月3日答记者问时表示，所谓新疆存在“种族灭绝”是赤裸裸的谎言</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-03/10707633.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月3日电 中国外交部发言人郭嘉昆10月3日答记者问时表示，中方一贯反对将民用无人机用于军事目的。各方应为乌克兰危机的政治解决发挥建设性作用，而非无端炒作和恶意关联。" data-title="中国外交部：一贯反对将民用无人机用于军事目的" data-date="10-03 21:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-03 21:16</span>
          <span class="news-item-title">中国外交部：一贯反对将民用无人机用于军事目的</span>
          <span class="news-value-point">💡 中新社北京10月3日电 中国外交部发言人郭嘉昆10月3日答记者问时表示，中方一贯反对将民用无人机用于军事目的</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501451.html" target="_blank" rel="noopener" data-cat="keji" data-summary="专业3D模型反而更稀缺了" data-title="GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元" data-date="10-04 08:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 08:53</span>
          <span class="news-item-title">GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元</span>
          <span class="news-value-point">💡 专业3D模型反而更稀缺了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar" target="_blank" rel="noopener" data-cat="keji" data-summary="Shield TV Pro仍然是英伟达运行时间最长的消费设备之一，但其299.99 $的价格标签现在使流媒体盒比推出时贵得多。" data-title="7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage" data-date="10-04 00:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 00:59</span>
          <span class="news-item-title">7年历史的Nvidia Shield TV Pro在人工智能内存短缺的推动下，价格上涨了50% ，令人震惊</span>
          <span class="news-item-title-en">7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage</span>
          <span class="news-value-point">💡 Shield TV Pro仍然是英伟达运行时间最长的消费设备之一，但其299.99 $的价格标签现在使流媒体盒比推出时贵得多</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1004418/capcom-ai-game-development" target="_blank" rel="noopener" data-cat="keji" data-summary="Capcom的Pragmata可能完全是关于人工智能的恐怖，但在实践中，工作室似乎并不那么低调。在CAPCOM公开会议RE: 2026期间，程序员Satoshi Ishida发表了一篇演讲，题目是： “The Outlook a" data-title="Capcom is preparing for a ‘future where we create games together with AI’" data-date="10-04 00:49" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 00:49</span>
          <span class="news-item-title">Capcom正在为“我们与人工智能一起创造游戏的未来”做准备</span>
          <span class="news-item-title-en">Capcom is preparing for a ‘future where we create games together with AI’</span>
          <span class="news-value-point">💡 Capcom的Pragmata可能完全是关于人工智能的恐怖，但在实践中，工作室似乎并不那么低调</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）自己承认，他“有些陈词滥调” ：一家领先的人工智能公司的员工在辞职时发出可怕的警告。" data-title="OpenAI安全员工辞职，声称公司的“文化被打破”" data-date="10-04 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-04 00:30</span>
          <span class="news-item-title">OpenAI安全员工辞职，声称公司的“文化被打破”</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）自己承认，他“有些陈词滥调” ：一家领先的人工智能公司的员工在辞职时发出可怕的警告</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/580.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，在 10 月 1 日的华为 Mate 90 系列及全场景新品发布会上，华为年度旗舰 Mate 90 系列手机正式发布。其中，Mate 90 Pro Max / RS 非凡大师搭载的是首款逻辑折叠 τ 芯片 —— 麒麟 9050 Pro。根据华为官方介绍，麒麟 9050 Pro 是麒麟性能新巅峰，通过软硬芯云垂直整合，整机性能提升 31%。这枚芯片 CPU 还支持 9 核 16 线程超线程技术，多核性能提升 23%、GPU 渲染性能提升 40%、NPU 性能提升 140%。极客湾发布了一期针对华为 Mate 90 Pro Max 的性能分析报告，讲解了麒麟 9050 Pro 的逻辑折叠是如何实现，并公开了 Mate 90 Pro Max 的实际性能续航表现。需要" data-title="华为 Mate 90 Pro Max 性能解禁：搭载麒麟 9050 Pro，部分游戏能效优于第五代骁龙 8 至尊版机型" data-date="10-04 00:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 00:20</span>
          <span class="news-item-title">华为 Mate 90 Pro Max 性能解禁：搭载麒麟 9050 Pro，部分游戏能效优于第五代骁龙 8 至尊版机型</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，在 10 月 1 日的华为 Mate 90 系列及全场景新品发布会上，华为年度旗舰 Mate 90 系列手机正式…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会。" data-title="Elon Musk确认与台积电就Terafab芯片制造合作进行讨论" data-date="10-03 22:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:50</span>
          <span class="news-item-title">Elon Musk确认与台积电就Terafab芯片制造合作进行讨论</span>
          <span class="news-value-point">💡 据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会。" data-title="Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration" data-date="10-03 22:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:50</span>
          <span class="news-item-title">Elon Musk确认与台积电就Terafab芯片制造合作进行讨论</span>
          <span class="news-item-title-en">Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration</span>
          <span class="news-value-point">💡 据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/576.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 3 日消息，海马云 (haimacloud) 近日推出了 haimacloud GEAR 端云混合掌机。其本地采用高通骁龙 865 移动平台，运行 Android 13 操作系统，支持海马云的云游戏服务。该掌机拥有 8GB + 128GB 的存储器组合，搭配 7&quot; FHD 144Hz 2ms 800nits OLED 屏幕，内置 8000mAh 电池，具备主动散热、TMR 摇杆、霍尔扳机、机械微动按键、六轴体感，ABXY 为模块化设计，支持 Wi-Fi 6 &amp; BT 5.1，质量 450g。IT之家获悉，配套的云游戏服务基于英特尔酷睿 i7-12700KF 处理器、&quot;70&quot; 级 NVIDIA GeForce RTX 显卡，支持 1080p 144FPS。haimaclou" data-title="海马云推出 haimacloud GEAR 端云混合掌机：高通骁龙 865，硬件首发价 3149 元" data-date="10-03 22:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 22:47</span>
          <span class="news-item-title">海马云推出 haimacloud GEAR 端云混合掌机：高通骁龙 865，硬件首发价 3149 元</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，海马云 (haimacloud) 近日推出了 haimacloud GEAR 端云混合掌机</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告。本周，他辞去了职务，现在正在《大西洋月刊》的一篇社论中发表讲话。如果你对突然从木制品中走出来的每个人都感到有点愤世嫉俗，警告他们有多危险，这是可以理解的[…]" data-title="OpenAI安全员工已辞职并正在敲响警钟" data-date="10-03 22:31" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-03 22:31</span>
          <span class="news-item-title">OpenAI安全员工已辞职并正在敲响警钟</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告。本周，他辞去了职务，现在正在《大西洋月刊》的一篇社论中发表讲话。如果你觉得有点愤世嫉俗是可以理解的" data-title="An OpenAI safety employee has quit and is sounding the alarm" data-date="10-03 22:31" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-03 22:31</span>
          <span class="news-item-title">OpenAI安全员工已辞职并正在敲响警钟</span>
          <span class="news-item-title-en">An OpenAI safety employee has quit and is sounding the alarm</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表。" data-title="所有可以存在于您的短信中的人工智能代理" data-date="10-03 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">所有可以存在于您的短信中的人工智能代理</span>
          <span class="news-value-point">💡 我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety" target="_blank" rel="noopener" data-cat="keji" data-summary="本周在Tom&#39;s Hardware Premium上，我们通过免费访问的芯片设计周打开了闸门，包括专家访谈、与OpenAI坐下来讨论其定制ASIC等等。" data-title="本周Tom&#39;s Hardware Premium ： 2026年10月3日" data-date="10-03 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium ： 2026年10月3日</span>
          <span class="news-value-point">💡 本周在Tom's Hardware Premium上，我们通过免费访问的芯片设计周打开了闸门，包括专家访谈、与OpenAI坐下来讨论其定制ASI…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety" target="_blank" rel="noopener" data-cat="keji" data-summary="本周在Tom&#39;s Hardware Premium上，我们通过免费访问的芯片设计周打开了闸门，包括专家访谈、与OpenAI坐下来讨论其定制ASIC等等。" data-title="This week on Tom&#39;s Hardware Premium: October 3, 2026" data-date="10-03 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium ： 2026年10月3日</span>
          <span class="news-item-title-en">This week on Tom's Hardware Premium: October 3, 2026</span>
          <span class="news-value-point">💡 本周在Tom's Hardware Premium上，我们通过免费访问的芯片设计周打开了闸门，包括专家访谈、与OpenAI坐下来讨论其定制ASI…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen" target="_blank" rel="noopener" data-cat="keji" data-summary="Daniel Newman的数据来自OpenRouter数据，其中代理商在2月份超过了人类，并在8月份增长了14倍。" data-title="随着缓存提示爆炸，人工智能代理使用的代币数量比人类多5倍，达到10倍" data-date="10-03 21:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 21:10</span>
          <span class="news-item-title">随着缓存提示爆炸，人工智能代理使用的代币数量比人类多5倍，达到10倍</span>
          <span class="news-value-point">💡 Daniel Newman的数据来自OpenRouter数据，其中代理商在2月份超过了人类，并在8月份增长了14倍</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen" target="_blank" rel="noopener" data-cat="keji" data-summary="Daniel Newman的数据来自OpenRouter数据，其中代理商在2月份超过了人类，并在8月份增长了14倍。" data-title="AI agents use 5x more tokens than humans as cached prompts explode, headed for 10x" data-date="10-03 21:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 21:10</span>
          <span class="news-item-title">随着缓存提示爆炸，人工智能代理使用的代币数量比人类多5倍，达到10倍</span>
          <span class="news-item-title-en">AI agents use 5x more tokens than humans as cached prompts explode, headed for 10x</span>
          <span class="news-value-point">💡 Daniel Newman的数据来自OpenRouter数据，其中代理商在2月份超过了人类，并在8月份增长了14倍</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">4 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/577.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队。点球大战中，中国队 4 比 3 取胜，获得本次亚运会男足比赛铜牌。上半场，中国队胡荷韬破门。半场结束，中国男足与对手 1-1 战平。下半场，中国队王钰栋破门。90 分钟双方战成 2-2。这也是中国队时隔 28 年再次获得亚运会男足比赛铜牌！也是亚运会男足项目实行 U23 年龄限制后，中国队首次获得奖牌。IT之家查询获悉，中国男足曾在 1994 年广岛亚运会上获得银牌，并于 1978 年、1998 年两次获得铜牌。本届比赛，中国队时隔 28 年再次闯入亚运会男足四强，并最终登上领奖台。另外，今年 1 月，在 2026 年 U23 亚洲杯半决赛中，中国 U23 男足以" data-title="点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌" data-date="10-03 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 22:51</span>
          <span class="news-item-title">点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/03/manchester-city-whistleblower-rui-pinto-ready-to-help-uk-authorities-in-return-for-protection" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="《卫报》了解到， Rui Pinto在葡萄牙面临证人保护的损失有关城市事务的更多文件可能会提供Rui Pinto ，他的泄密有助于引发英超联赛对曼城金融事务的调查，他准备帮助英国当局处理法律案件，以换取免受威胁的保护。尽管周五发起了众筹活动，为离开公关后的新生活提供资金" data-title="曼城举报人随时准备为英国当局提供帮助，以换取保护" data-date="10-03 19:12" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-03 19:12</span>
          <span class="news-item-title">曼城举报人随时准备为英国当局提供帮助，以换取保护</span>
          <span class="news-value-point">💡 《卫报》了解到， Rui Pinto在葡萄牙面临证人保护的损失有关城市事务的更多文件可能会提供Rui Pinto ，他的泄密有助于引发英超联赛对…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c65y51nvn24wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="卢顿镇经理杰克·威尔希尔（ Jack Wilshere ）讲述了他回到8岁时开始的地方，以及他从阿森纳时期学到的经验教训。" data-title="向Arteta学习并激励年轻人- Wilshere的管理" data-date="10-03 13:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-03 13:19</span>
          <span class="news-item-title">向Arteta学习并激励年轻人- Wilshere的管理</span>
          <span class="news-value-point">💡 卢顿镇经理杰克·威尔希尔（ Jack Wilshere ）讲述了他回到8岁时开始的地方，以及他从阿森纳时期学到的经验教训</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/news/ng-interactive/2026/oct/03/manchester-city-guilty-verdict-football" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在安迪·伯纳姆（ Andy Burnham ）谈到英国在撒切尔（ Thatcher ）统治下的错误转折点的那一天，足球正面临着对自己收购企业的故事进行清算的日子。不知何故，周二对曼城的诅咒裁决落入了工党大会的核心，在安迪·伯纳姆（ Andy Burnham ）狂热地接受了总理的演讲之后。我在那里，阅读了令人惊讶的40页调查结果–曼城创造了“" data-title="曼城的有罪判决给足球带来了巨大的抛售崩溃" data-date="10-03 13:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-03 13:00</span>
          <span class="news-item-title">曼城的有罪判决给足球带来了巨大的抛售崩溃</span>
          <span class="news-value-point">💡 在安迪·伯纳姆（ Andy Burnham ）谈到英国在撒切尔（ Thatcher ）统治下的错误转折点的那一天，足球正面临着对自己收购企业的故…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707715.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国庆假期，云南省德宏傣族景颇族自治州梁河县备好了一场民族文化的盛宴：热烈奔放的目瑙纵歌、穿越时光的庭院剧、充满野趣的稻花鱼体验、烟火氤氲的古镇美食、惬意畅快的山野徒步……" data-title="“甜蜜业态”婚旅：让新人把“我愿意”说给山海听" data-date="10-04 09:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:57</span>
          <span class="news-item-title">“甜蜜业态”婚旅：让新人把“我愿意”说给山海听</span>
          <span class="news-value-point">💡 国庆假期，云南省德宏傣族景颇族自治州梁河县备好了一场民族文化的盛宴：热烈奔放的目瑙纵歌、穿越时光的庭院剧、充满野趣的稻花鱼体验、烟火氤氲的古镇美…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707713.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国庆小长假来临，不少人选择了出境旅游。无论是出境还是入境，都要绷紧生物安全这根弦，这些红线千万不能踩！" data-title="出境游必看！这些东西不能随意带……" data-date="10-04 09:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:50</span>
          <span class="news-item-title">出境游必看！这些东西不能随意带……</span>
          <span class="news-value-point">💡 国庆小长假来临，不少人选择了出境旅游</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707712.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网郴州10月4日电 (徐志雄 刘翔宇)“像我们在外漂泊的游子，每次逢年过节回家乡都要带着自己的孩子，到红军墓来看一看。”又到一年国庆假期，湖南郴州北湖区仰天湖瑶族乡瑞金村村民刘诗斌再度邀上三两发小，相约来到村背山上的无名红军烈士墓，为91年前长眠于此的7名烈士扫墓，缅怀先烈。" data-title="（长征胜利90周年）湖南郴州瑞金村接力守护红军烈士墓 红色故事带动瑶乡振兴" data-date="10-04 09:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:49</span>
          <span class="news-item-title">（长征胜利90周年）湖南郴州瑞金村接力守护红军烈士墓 红色故事带动瑶乡振兴</span>
          <span class="news-value-point">💡 中新网郴州10月4日电 (徐志雄 刘翔宇)“像我们在外漂泊的游子，每次逢年过节回家乡都要带着自己的孩子，到红军墓来看一看</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707711.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月4日电 据中央气象台网站消息，昨日，江西、湖南、贵州、广西等地出现较强降雨，内蒙古、河北等地出现大风或降温天气。预计4日至5日，内蒙古中东部、华北、黄淮、江汉及东部、南部海区风力较大，东北地区局地降水较强，关注对人体健康、交通出行、农牧业及沿海养殖、海上航行等的影响。4日，贵州、云南、广西、广东、福建、海南局地仍有较强降雨，关注对假期旅游、交通出行、秋收等的影响，防范可能引发的山洪、地质灾害。" data-title="贵州广西云南湖南广东等地有较强降水 中东部地区有大风降温天气" data-date="10-04 09:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:49</span>
          <span class="news-item-title">贵州广西云南湖南广东等地有较强降水 中东部地区有大风降温天气</span>
          <span class="news-value-point">💡 中新网10月4日电 据中央气象台网站消息，昨日，江西、湖南、贵州、广西等地出现较强降雨，内蒙古、河北等地出现大风或降温天气</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707709.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网贺州10月4日电(韦佳秀 贝琲 廖法丽)国庆假期，广西贺州市多地推出特色夜间文旅活动，篝火金曲晚会、音乐节轮番上演，山水夜景与文化演出深度交融，为市民与八方游客打造沉浸式假日体验，持续激活地方夜间文旅消费活力。" data-title="广西贺州国庆假期多元活动激活夜间消费市场" data-date="10-04 09:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:47</span>
          <span class="news-item-title">广西贺州国庆假期多元活动激活夜间消费市场</span>
          <span class="news-value-point">💡 中新网贺州10月4日电(韦佳秀 贝琲 廖法丽)国庆假期，广西贺州市多地推出特色夜间文旅活动，篝火金曲晚会、音乐节轮番上演，山水夜景与文化演出深度…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707682.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网西安10月4日电 (记者 阿琳娜)陕西省推出“金秋银龄·惠享三秦”旅居养老消费补贴活动。从10月1日至12月31日，60岁及以上老年人在陕跨县域旅居，可享每人每天30元至50元的专项消费补贴，单人单次最高补贴不超过500元。" data-title="陕西省推出旅居养老消费补贴活动" data-date="10-04 08:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 08:49</span>
          <span class="news-item-title">陕西省推出旅居养老消费补贴活动</span>
          <span class="news-value-point">💡 中新网西安10月4日电 (记者 阿琳娜)陕西省推出“金秋银龄·惠享三秦”旅居养老消费补贴活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707676.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据印尼气象、气候和地球物理局消息，当地时间10月4日5时55分，印尼东努沙登加拉省西南松巴县西南14公里处发生6.1级地震，震源深度为10公里。" data-title="印尼东努沙登加拉省发生6.1级地震 震源深度10公里" data-date="10-04 07:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 07:29</span>
          <span class="news-item-title">印尼东努沙登加拉省发生6.1级地震 震源深度10公里</span>
          <span class="news-value-point">💡 据印尼气象、气候和地球物理局消息，当地时间10月4日5时55分，印尼东努沙登加拉省西南松巴县西南14公里处发生6.1级地震，震源深度为10公里</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october" target="_blank" rel="noopener" data-cat="zonghe" data-summary="现在还不到10月，亚马逊已经在自己的硬件上提供一些Prime Big Deal Day折扣，以及许多其他受欢迎的产品。这一切都是为了宣传10月黄金日，从10月6日美国东部时间凌晨3点开始，如果你在东部，则持续到8日美国东部时间凌晨3点[…]" data-title="目前最优惠的10月初黄金日优惠" data-date="10-04 00:22" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 00:22</span>
          <span class="news-item-title">目前最优惠的10月初黄金日优惠</span>
          <span class="news-value-point">💡 现在还不到10月，亚马逊已经在自己的硬件上提供一些Prime Big Deal Day折扣，以及许多其他受欢迎的产品</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october" target="_blank" rel="noopener" data-cat="zonghe" data-summary="现在还不到10月，亚马逊已经在自己的硬件上提供一些Prime Big Deal Day折扣，以及许多其他受欢迎的产品。这一切都是为了宣传10月Prime日，从10月6日美国东部时间凌晨3点开始，一直持续到3点" data-title="The best early October Prime Day deals happening now" data-date="10-04 00:22" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 00:22</span>
          <span class="news-item-title">目前最优惠的10月初黄金日优惠</span>
          <span class="news-item-title-en">The best early October Prime Day deals happening now</span>
          <span class="news-value-point">💡 现在还不到10月，亚马逊已经在自己的硬件上提供一些Prime Big Deal Day折扣，以及许多其他受欢迎的产品</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/03/us/tennessee-prison-commissioner-resigns-christa-pike.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="弗兰克·斯特拉达（ Frank Strada ）负责监督导致克里斯塔·派克（ Christa Pike ）昏迷并住院治疗的过程，随着独立审查的开始，他辞" data-title="Tennessee Commissioner Resigns After Failed Execution of Christa Pike" data-date="10-04 00:17" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-04 00:17</span>
          <span class="news-item-title">田纳西州专员在克里斯塔·派克处决失败后辞职</span>
          <span class="news-item-title-en">Tennessee Commissioner Resigns After Failed Execution of Christa Pike</span>
          <span class="news-value-point">💡 弗兰克·斯特拉达（ Frank Strada ）负责监督导致克里斯塔·派克（ Christa Pike ）昏迷并住院治疗的过程，随着独立审查的开…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/579.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 3 日消息，据交通运输部动态研判，10 月 4 日，全国高速公路有 33 个路段易发拥堵，主要集中在江苏、四川、广东、湖南、浙江等省份。如计划途经这些路段，请合理安排出行时间和路线。序号省份城市路线编号路线名称起点桩号止点桩号方向1江苏南京市G25长深高速K2152K2094下行2江苏无锡市G2京沪高速K1091K1121上行3江苏无锡市S48沪宜高速K134K171上行4江苏常州市G4221沪武高速K196K166下行5江苏南通市G15沈海高速K1180K1219上行6江苏淮安市G1516盐洛高速K220K187下行7江苏盐城市G15沈海高速K954K984上行8江苏盐城市G15沈海高速K1076K1147上行9江苏扬州市G2京沪高速K893K933上行10江苏镇江市G" data-title="明日出行请注意，交通运输部提示 33 个高速公路路段易发拥堵" data-date="10-03 23:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 23:27</span>
          <span class="news-item-title">明日出行请注意，交通运输部提示 33 个高速公路路段易发拥堵</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，据交通运输部动态研判，10 月 4 日，全国高速公路有 33 个路段易发拥堵，主要集中在江苏、四川、广东、湖南、…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/578.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 3 日消息，泰坦军团旗下“P2511G+”24.5 英寸显示器现已在京东发售，该机主打 1080P 215Hz 超频，定价为 509 元，部分地区国补后低至 483.55 元。京东泰坦军团 P2511G+ 显示器 509 元直达链接该机配备一块 1920x1080 分辨率 215Hz 超频（原生 200Hz）Fast IPS 面板，显示器亮度 400 尼特，GtG 响应速度 1ms，显示器支持 8-Bit 色彩，覆盖 99% sRGB 色域。该机支架支持俯仰，显示器本体支持 VESA 100x100mm 壁挂，提供 1 个 HDMI 2.0、1 个 DP1.4、1 个 3.5mm 音频接口。IT之家附显示器参数如下：" data-title="泰坦军团“P2511G+”24.5 英寸显示器发售：1080P 215Hz 超频，509 元" data-date="10-03 23:18" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 23:18</span>
          <span class="news-item-title">泰坦军团“P2511G+”24.5 英寸显示器发售：1080P 215Hz 超频，509 元</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，泰坦军团旗下“P2511G+”24.5 英寸显示器现已在京东发售，该机主打 1080P 215Hz 超频，定价为…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1004162/splice-ceo-kakul-srivastava-ai-interview" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡库尔·斯里瓦斯塔瓦（ Kakul Srivastava ）是Splice的首席执行官，无数制片人依靠这个样品平台进行一次性拍摄和旋律循环。从服务中提取的样品已经成为Lisa的“Money”和Sabrina Carpenter的“Espresso”等热门歌曲。（原始样品在这里和这里，为了好奇。）在此之前， Kakul曾担任行政职务[…]" data-title="Splice首席执行官Kakul Srivastava认为人工智能电子邮件正在扼杀对话" data-date="10-03 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-03 23:00</span>
          <span class="news-item-title">Splice首席执行官Kakul Srivastava认为人工智能电子邮件正在扼杀对话</span>
          <span class="news-value-point">💡 卡库尔·斯里瓦斯塔瓦（ Kakul Srivastava ）是Splice的首席执行官，无数制片人依靠这个样品平台进行一次性拍摄和旋律循环</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1004162/splice-ceo-kakul-srivastava-ai-interview" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡库尔·斯里瓦斯塔瓦（ Kakul Srivastava ）是Splice的首席执行官，无数制片人依靠这个样品平台进行一次性拍摄和旋律循环。从服务中提取的样本已经成为Lisa的“Money”和Sabrina Carpenter的“Espresso”等热门歌曲。（ T" data-title="Splice CEO Kakul Srivastava thinks AI emails are killing conversations" data-date="10-03 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-03 23:00</span>
          <span class="news-item-title">Splice首席执行官Kakul Srivastava认为人工智能电子邮件正在扼杀对话</span>
          <span class="news-item-title-en">Splice CEO Kakul Srivastava thinks AI emails are killing conversations</span>
          <span class="news-value-point">💡 卡库尔·斯里瓦斯塔瓦（ Kakul Srivastava ）是Splice的首席执行官，无数制片人依靠这个样品平台进行一次性拍摄和旋律循环</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/find-tech-deals-in-neweggs-fantastech-sale-ii-ahead-of-october-5-price-protection-guarantee-lets-you-start-shopping-now" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在Newegg的Fantastech Sale II于10月5日推出之前，如果产品价格在销售中下跌，您可以抓住一些早期交易并获得价格保护安全。" data-title="在亚马逊大促销日之前，在Newegg的Fantastech促销活动中查找技术优惠--如果硬件价格下跌，早期购物者将获得自动退款" data-date="10-03 22:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:40</span>
          <span class="news-item-title">在亚马逊大促销日之前，在Newegg的Fantastech促销活动中查找技术优惠--如果硬件价格下跌，早期购物者将获得自动退款</span>
          <span class="news-value-point">💡 在Newegg的Fantastech Sale II于10月5日推出之前，如果产品价格在销售中下跌，您可以抓住一些早期交易并获得价格保护安全</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-04 09:54（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
