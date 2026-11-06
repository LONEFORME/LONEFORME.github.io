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
      <span>2026-11-06 16:39 抓取更新</span>
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
        <span class="channel-count">60</span>
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
  <div class="ov-item"><span class="ov-num">60</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · 天空体育×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-06/10727357.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华时评丨警惕日本“认知投毒”的危险图谋" data-title="警惕日本“认知投毒”的危险图谋" data-date="11-06 16:32" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-06 16:32</span>
      </div>
      <h2 class="hero-featured-title">警惕日本“认知投毒”的危险图谋</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-06/10727356.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网11月6日电 11月6日，中国铁路广州局集团有限公司广州客运段官方微博通报称，近日，针对媒体报道“骨折旅客买到D28次列车中铺，想换下铺未成功”的信息，广州客运段调看了列车车载视频，询问了相关证人，客观还原了事情经过。经核查，相关报道内容不实。具体情况如下：" data-title="骨折旅客买到中铺，想换下铺未成功？官方通报" data-date="11-06 16:33" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">骨折旅客买到中铺，想换下铺未成功？官方通报</p>
    </a>
    <a class="hero-sub-card" href="https://www.qbitai.com/2026/11/508107.html" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一举刷新“AI安全世界杯”CyberGym世界纪录" data-title="99.4%登顶全球第一！这个中国AI师承世界冠军" data-date="11-06 13:01" data-source="量子位">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-techcrunch">🧠 量子位</span>
      </div>
      <p class="hero-sub-title">99.4%登顶全球第一！这个中国AI师承世界冠军</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/023/409.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 6 日消息，为进一步加强科普健康领域网络谣言突出问题整治，营造风清气正网络空间，近日，中央网信办印发通知，在全国范围内部署开展为期 2 个月的“清朗 · 整治科普健康类网络谣言”专项行动。中央网信办有关负责同志表示，本次专项行动重点整治以下 4 方面突出问题：（一）编造民生健康网络谣言，借机误导网民。一是以关注公众健康等为名义，将普通食品、保健品包装成“神药”，推广所谓“包治百病”偏方，发布伪科普信息，借审美焦虑制造“黄连素是减肥神药”等运动、减重类谣言。二是刻意夸大食品、药品、生活用品副作用，配以夸张骇人标题，编造所谓“长期服用降压药会使血管变脆”“献血会伤害身体”“味精加热有毒”“蜂蜜结晶不能吃”等缺乏科学依据、断章取义的谣言信息，制造焦虑恐慌情绪。三是以“科学辟谣”" data-title="重点整治滥用 AI 技术生成健康科普谣言等，中央网信办部署开展专项行动" data-date="11-06 16:38" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">重点整治滥用 AI 技术生成健康科普谣言等，中央网信办部署开展专项行动</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727357.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华时评丨警惕日本“认知投毒”的危险图谋" data-title="警惕日本“认知投毒”的危险图谋" data-date="11-06 16:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:32</span>
          <span class="news-item-title">警惕日本“认知投毒”的危险图谋</span>
          <span class="news-value-point">💡 新华时评丨警惕日本“认知投毒”的危险图谋</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727352.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月6日电 (记者 李纯)中国国防部新闻发言人陈曦6日就近期涉军问题发布消息。他表示，“攻击-21”隐身无人机首次在四川舰成功起降，是中国军队新域新质作战力量建设取得的重要阶段性成果。" data-title="中国国防部谈“攻击" data-date="11-06 16:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:30</span>
          <span class="news-item-title">中国国防部谈“攻击</span>
          <span class="news-value-point">💡 中新社北京11月6日电 (记者 李纯)中国国防部新闻发言人陈曦6日就近期涉军问题发布消息</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/la-mayor-raman-bass.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位45岁的市议会议员击败了现任市长、73岁的卡伦·巴斯（ Karen Bass ） ，这对新一代进步领导人来说是一个巨大的成功。" data-title="Nithya Raman Wins Los Angeles Mayoral Race, Defeating Karen Bass" data-date="11-06 16:30" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 16:30</span>
          <span class="news-item-title">Nithya Raman赢得洛杉矶市长竞选，击败Karen Bass</span>
          <span class="news-item-title-en">Nithya Raman Wins Los Angeles Mayoral Race, Defeating Karen Bass</span>
          <span class="news-value-point">💡 这位45岁的市议会议员击败了现任市长、73岁的卡伦·巴斯（ Karen Bass ） ，这对新一代进步领导人来说是一个巨大的成功</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727355.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="认知工作室丨当AI说出历史真相，日本右翼认知操弄无处遁形" data-title="当AI说出历史真相，日本右翼认知操弄无处遁形" data-date="11-06 16:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:30</span>
          <span class="news-item-title">当AI说出历史真相，日本右翼认知操弄无处遁形</span>
          <span class="news-value-point">💡 认知工作室丨当AI说出历史真相，日本右翼认知操弄无处遁形</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727342.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月6日电 (记者 李纯)中国国防部新闻发言人陈曦6日就近期涉军问题发布消息。他指出，国际社会必须高度警惕并坚决遏制日本重启“战争机器”、重走扩张邪路，共同守护战后国际秩序。" data-title="中国国防部：国际社会须高度警惕日本重启“战争机器”" data-date="11-06 16:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:26</span>
          <span class="news-item-title">中国国防部：国际社会须高度警惕日本重启“战争机器”</span>
          <span class="news-value-point">💡 中新社北京11月6日电 (记者 李纯)中国国防部新闻发言人陈曦6日就近期涉军问题发布消息</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727341.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社四川泸州11月6日电 (祝欢)第五届国际地理标志产品博览会6日在四川泸州启幕。匈牙利担任主宾国，玻利维亚、巴西、智利等28国嘉宾齐聚，参与国家数量为历届之最。" data-title="第五届国际地理标志产品博览会启幕  中外嘉宾共拓合作新空间" data-date="11-06 16:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:23</span>
          <span class="news-item-title">第五届国际地理标志产品博览会启幕  中外嘉宾共拓合作新空间</span>
          <span class="news-value-point">💡 中新社四川泸州11月6日电 (祝欢)第五届国际地理标志产品博览会6日在四川泸州启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727329.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社上海11月6日电 (记者 曾玥)谈及近期两国高层互动，中国美国商会会长何迈可(Michael Hart)6日在上海表示，两国政府间的持续对话有助于构建一个更可预期的环境，推动双方在知识产权保护等领域开展务实合作。" data-title="（第九届进博会）中国美国商会会长：美中政府间持续对话有助于构建更可预期环境" data-date="11-06 16:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:08</span>
          <span class="news-item-title">（第九届进博会）中国美国商会会长：美中政府间持续对话有助于构建更可预期环境</span>
          <span class="news-value-point">💡 中新社上海11月6日电 (记者 曾玥)谈及近期两国高层互动，中国美国商会会长何迈可(Michael Hart)6日在上海表示，两国政府间的持续对…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727330.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社厦门11月6日电 (记者 阮煜琳)记者从正在举行的2026厦门国际海洋周上获悉，截至目前，中国载人潜水器“蛟龙”号已累计下潜475次。实现迭代升级和关键部件国产化替代后的“蛟龙”号，作业效能极大提升。" data-title="中国载人潜水器“蛟龙”号累计下潜475次 迭代升级后效能大提升" data-date="11-06 16:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:07</span>
          <span class="news-item-title">中国载人潜水器“蛟龙”号累计下潜475次 迭代升级后效能大提升</span>
          <span class="news-value-point">💡 中新社厦门11月6日电 (记者 阮煜琳)记者从正在举行的2026厦门国际海洋周上获悉，截至目前，中国载人潜水器“蛟龙”号已累计下潜475次</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727323.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月6日电 据中央纪委国家监委网站消息，近日，在中央反腐败协调小组国际追逃追赃工作办公室统筹协调下，经广西壮族自治区监察机关、公安机关与有关国家执法机关密切合作，外逃职务犯罪嫌疑人李标在境外落网并被遣返回国。" data-title="广西蚕业技术推广站原站长李标被遣返回国" data-date="11-06 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:02</span>
          <span class="news-item-title">广西蚕业技术推广站原站长李标被遣返回国</span>
          <span class="news-value-point">💡 中新网11月6日电 据中央纪委国家监委网站消息，近日，在中央反腐败协调小组国际追逃追赃工作办公室统筹协调下，经广西壮族自治区监察机关、公安机关与…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727320.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月6日电 据应急管理部网站消息，为防范化解烟花爆竹安全风险，有效遏制事故发生，国务院安委会办公室在全国范围内部署开展烟花爆竹全链条“打非治违”专项行动。行动开展以来，各地区、各有关部门强化协同联动，加大执法检查力度，严肃查处了一批突出非法违法行为。当前已进入烟花爆竹产销旺季，为充分发挥警示震慑作用，推动安全生产形势持续稳定，国务院安委会办公室、应急管理部近日公布6起烟花爆竹全链条“打非治违”典型案例。" data-title="严查非法违法行为 6起烟花爆竹全链条“打非治违”典型案例公布" data-date="11-06 16:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:01</span>
          <span class="news-item-title">严查非法违法行为 6起烟花爆竹全链条“打非治违”典型案例公布</span>
          <span class="news-value-point">💡 中新网11月6日电 据应急管理部网站消息，为防范化解烟花爆竹安全风险，有效遏制事故发生，国务院安委会办公室在全国范围内部署开展烟花爆竹全链条“打…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727265.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月6日电 综合美国福克斯新闻、英国《每日电讯报》报道，当地时间5日，美国总统特朗普在椭圆形办公室签署行政命令时，办公桌上摆放的一顶红色帽子引发关注，帽子上用白色字母写着“否决权”(VETO)。" data-title="中期选举失利后 特朗普在办公桌上放了一顶帽子(图)" data-date="11-06 15:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 15:10</span>
          <span class="news-item-title">中期选举失利后 特朗普在办公桌上放了一顶帽子(图)</span>
          <span class="news-value-point">💡 中新网11月6日电 综合美国福克斯新闻、英国《每日电讯报》报道，当地时间5日，美国总统特朗普在椭圆形办公室签署行政命令时，办公桌上摆放的一顶红色…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727244.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月6日电 据日本《赤旗报》报道，日本参议院宪法审查会4日召开会议，日本共产党籍参议员山添拓在会上批评高市早苗政府推动修宪和大规模扩军，并认为当前没有必要推动修宪议程。" data-title="日本参议员批评高市政权罔顾民意 急于推动修宪扩军" data-date="11-06 14:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 14:44</span>
          <span class="news-item-title">日本参议员批评高市政权罔顾民意 急于推动修宪扩军</span>
          <span class="news-value-point">💡 中新网11月6日电 据日本《赤旗报》报道，日本参议院宪法审查会4日召开会议，日本共产党籍参议员山添拓在会上批评高市早苗政府推动修宪和大规模扩军，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727229.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月6日电(记者 刁炜)近日，巴基斯坦成功试射首枚自主研发的空对空导弹。美国“战区”网站称，这不仅是巴防务工业取得的重大成就，更标志着巴基斯坦已跻身全球少数拥有自主研发空对空导弹能力的国家之列。" data-title="射程超100公里，巴基斯坦自研空对空导弹可打隐身飞机？" data-date="11-06 14:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 14:43</span>
          <span class="news-item-title">射程超100公里，巴基斯坦自研空对空导弹可打隐身飞机？</span>
          <span class="news-value-point">💡 中新网11月6日电(记者 刁炜)近日，巴基斯坦成功试射首枚自主研发的空对空导弹</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/us/politics/trump-triumphal-arch-planning-commission.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在由总统盟友领导的联邦规划委员会周四批准特朗普的250英尺拱门项目后，法官迅速采取行动。" data-title="Trump’s Triumphal Arch Wins Commission Approval Despite Court Challenges" data-date="11-06 14:14" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 14:14</span>
          <span class="news-item-title">尽管面临法庭挑战，特朗普的凯旋门还是赢得了委员会的批准</span>
          <span class="news-item-title-en">Trump’s Triumphal Arch Wins Commission Approval Despite Court Challenges</span>
          <span class="news-value-point">💡 在由总统盟友领导的联邦规划委员会周四批准特朗普的250英尺拱门项目后，法官迅速采取行动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727181.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月6日电 开罗消息：当地时间11月5日，埃及军方宣布，在该国南部边境开展的一项旨在打击非法采金活动并追查犯罪网络的军事行动中，两名军官不幸丧生。" data-title="埃及军方：两名军官在边境打击非法采金行动中丧生" data-date="11-06 13:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 13:23</span>
          <span class="news-item-title">埃及军方：两名军官在边境打击非法采金行动中丧生</span>
          <span class="news-value-point">💡 中新社北京11月6日电 开罗消息：当地时间11月5日，埃及军方宣布，在该国南部边境开展的一项旨在打击非法采金活动并追查犯罪网络的军事行动中，两名…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727356.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网11月6日电 11月6日，中国铁路广州局集团有限公司广州客运段官方微博通报称，近日，针对媒体报道“骨折旅客买到D28次列车中铺，想换下铺未成功”的信息，广州客运段调看了列车车载视频，询问了相关证人，客观还原了事情经过。经核查，相关报道内容不实。具体情况如下：" data-title="骨折旅客买到中铺，想换下铺未成功？官方通报" data-date="11-06 16:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:33</span>
          <span class="news-item-title">骨折旅客买到中铺，想换下铺未成功？官方通报</span>
          <span class="news-value-point">💡 中新网11月6日电 11月6日，中国铁路广州局集团有限公司广州客运段官方微博通报称，近日，针对媒体报道“骨折旅客买到D28次列车中铺，想换下铺未…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/405.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 6 日消息，华为今日面向 Mate 90 系列手机推送了鸿蒙 HarmonyOS 7.0.0.111 SP15 版本升级，系统包大小约 727.57MB。▲ IT之家实拍：华为 Mate 90 Pro Max 典藏版据介绍，本次更新优化了在搭配华为睿影 Z10 模块相机时的拍摄效果，并同时优化了整机系统稳定性。据IT之家了解，华为睿影 Z10 模块相机代号“金刚”，集成红枫等多种传感器，支持与手机 SoC 协同，通过软硬芯 AI 协同 + 智能融合对焦，实现对焦快、准、稳；拥有独立光学防抖模块，与麒麟芯片协同，可实现旗舰级防抖体验。" data-title="华为 Mate 90 系列手机获 HarmonyOS 7.0.0.111SP15 升级，优化搭配睿影 Z10 模块相机的拍摄效果" data-date="11-06 16:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:32</span>
          <span class="news-item-title">华为 Mate 90 系列手机获 HarmonyOS 7.0.0.111SP15 升级，优化搭配睿影 Z10 模块相机的拍摄效果</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，华为今日面向 Mate 90 系列手机推送了鸿蒙 HarmonyOS 7.0.0.111 SP15 版本升级，系…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/404.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 6 日消息，在本周的 2026 移动网络大会上，高通公司总裁兼 CEO 安蒙表示，6G 从设计之初就将具备 AI 原生特性，让 AI 融入网络本身。安蒙称，借助网络连接，上下文信息可以持续在终端、边缘和云端之间交换。AI 将直接融入无线通信系统，使系统在估计信道状况的基础上，还能预测其变化，即使信号较弱，也能保持性能。此外，计算将遍布整个网络，从基站到网络边缘，再到数据中心。这样，AI 计算和推理任务可以分布在网络的不同节点上执行。今年 9 月，高通与中国移动在全球首次完成了 U6G 频段基站原型和 6G 终端原型互通测试，测试基于最新的 3GPP 定义开展。安蒙表示，这是 6G 从技术研究迈向系统验证的重要一步。高通与中国移动也在共同推进 AI 原生网络技术和新的无线通" data-title="高通 CEO 安蒙：6G 从设计之初就具备 AI 原生特性，目标 2029 年商用" data-date="11-06 16:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:32</span>
          <span class="news-item-title">高通 CEO 安蒙：6G 从设计之初就具备 AI 原生特性，目标 2029 年商用</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，在本周的 2026 移动网络大会上，高通公司总裁兼 CEO 安蒙表示，6G 从设计之初就将具备 AI 原生特性，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727327.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社杭州11月6日电 (记者 杨程晨 张杨彬)台湾宗教学者、国际儒学联合会副理事长林安梧6日在杭州受访时表示，面对人工智能(AI)快速演进，人类不能只谈算力和效率，更要谈“赋德”。" data-title="国际儒联副理事长林安梧：AI时代赋能更须“赋德”" data-date="11-06 16:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:08</span>
          <span class="news-item-title">国际儒联副理事长林安梧：AI时代赋能更须“赋德”</span>
          <span class="news-value-point">💡 中新社杭州11月6日电 (记者 杨程晨 张杨彬)台湾宗教学者、国际儒学联合会副理事长林安梧6日在杭州受访时表示，面对人工智能(AI)快速演进，人…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508155.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Q3营收实现数倍增长" data-title="DeepSeek带火稀疏计算，国产芯片公司加速突围：这家公司又融近10亿" data-date="11-06 15:00" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 15:00</span>
          <span class="news-item-title">DeepSeek带火稀疏计算，国产芯片公司加速突围：这家公司又融近10亿</span>
          <span class="news-value-point">💡 Q3营收实现数倍增长</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508118.html" target="_blank" rel="noopener" data-cat="keji" data-summary="挑战商业视频的高难度场景" data-title="一边赛博修仙，一边卖家电！AI短剧开始冲双11业绩了？" data-date="11-06 14:54" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 14:54</span>
          <span class="news-item-title">一边赛博修仙，一边卖家电！AI短剧开始冲双11业绩了？</span>
          <span class="news-value-point">💡 挑战商业视频的高难度场景</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508143.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11 月 20—21 日，2026 奇点智能技术大会将在北京万达文华酒店举行。" data-title="从RSI、Agent、Physical AI到整个系统栈，2026 奇点智能技术大会最新日程公布！" data-date="11-06 14:43" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 14:43</span>
          <span class="news-item-title">从RSI、Agent、Physical AI到整个系统栈，2026 奇点智能技术大会最新日程公布！</span>
          <span class="news-value-point">💡 11 月 20—21 日，2026 奇点智能技术大会将在北京万达文华酒店举行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/palo-alto-networks-in-talks-to-buy-ai-agent-security-startup-clutch-for-500m/" target="_blank" rel="noopener" data-cat="keji" data-summary="据一位消息人士称，由Lightspeed和SignalFire支持的Clutch最后估值为8500万美元$。" data-title="Palo Alto Networks in talks to buy AI agent security startup Clutch for $500M" data-date="11-06 14:28" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 14:28</span>
          <span class="news-item-title">Palo Alto Networks正在洽谈以5亿美元收购人工智能代理安全初创公司Clutch</span>
          <span class="news-item-title-en">Palo Alto Networks in talks to buy AI agent security startup Clutch for $500M</span>
          <span class="news-value-point">💡 据一位消息人士称，由Lightspeed和SignalFire支持的Clutch最后估值为8500万美元$</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507988.html" target="_blank" rel="noopener" data-cat="keji" data-summary="香港金融科技周 x StartmeupHK 2026踏入第11届" data-title="香港金融科技周 x StartmeupHK 2026主论坛：以“金融+”、“AI+”及全球拓展开拓新机遇" data-date="11-06 11:36" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 11:36</span>
          <span class="news-item-title">香港金融科技周 x StartmeupHK 2026主论坛：以“金融+”、“AI+”及全球拓展开拓新机遇</span>
          <span class="news-value-point">💡 香港金融科技周 x StartmeupHK 2026踏入第11届</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507972.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Seedance 2.5 单秒低至0.15元" data-title="AI短剧门槛降降降！实测即梦短剧工作室：剧本分镜预演一条龙，伙伴计划长期护航" data-date="11-06 11:20" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 11:20</span>
          <span class="news-item-title">AI短剧门槛降降降！实测即梦短剧工作室：剧本分镜预演一条龙，伙伴计划长期护航</span>
          <span class="news-value-point">💡 Seedance 2.5 单秒低至0.15元</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507967.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11月 5 日，腾讯宣布因 Hy4 调用激增，WorkBuddy 已进行十倍扩容" data-title="腾讯 Hy4 调用激增已十倍扩容，Agent 能力开源模型第一" data-date="11-06 10:00" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 10:00</span>
          <span class="news-item-title">腾讯 Hy4 调用激增已十倍扩容，Agent 能力开源模型第一</span>
          <span class="news-value-point">💡 11月 5 日，腾讯宣布因 Hy4 调用激增，WorkBuddy 已进行十倍扩容</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1028454/openai-data-center-nda" target="_blank" rel="noopener" data-cat="keji" data-summary="在本周的中期选举中，选民强烈反对数据中心扩张， OpenAI今天宣布了对正在开展数据中心项目的社区的新承诺，包括不会使用保密措施" data-title="OpenAI is stepping back from NDAs for data center projects" data-date="11-06 08:37" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 08:37</span>
          <span class="news-item-title">OpenAI正在退出数据中心项目的保密协议</span>
          <span class="news-item-title-en">OpenAI is stepping back from NDAs for data center projects</span>
          <span class="news-value-point">💡 在本周的中期选举中，选民强烈反对数据中心扩张， OpenAI今天宣布了对正在开展数据中心项目的社区的新承诺，包括不会使用保密措施</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028412/airbnb-ai-travel-agent-q3-2026-earnings" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司在今天发布的2026年第三季度收益股东信中表示，爱彼迎计划在2027年上半年推出一个人工智能代理，帮助用户规划和预订旅行。“今天的人工智能代理擅长简单的例行任务，比如做一个" data-title="Airbnb is working on an AI travel agent" data-date="11-06 08:06" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 08:06</span>
          <span class="news-item-title">爱彼迎正在与人工智能旅行社合作</span>
          <span class="news-item-title-en">Airbnb is working on an AI travel agent</span>
          <span class="news-value-point">💡 该公司在今天发布的2026年第三季度收益股东信中表示，爱彼迎计划在2027年上半年推出一个人工智能代理，帮助用户规划和预订旅行</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/05/airbnb-says-its-launching-an-ai-travel-agent-in-the-first-half-of-2027/" target="_blank" rel="noopener" data-cat="keji" data-summary="爱彼迎表示，即将推出的人工智能专员将帮助旅行者在整个住宿期间规划行程、比较选项、管理预订并获得帮助。" data-title="Airbnb says it’s launching an AI travel agent in the first half of 2027" data-date="11-06 06:40" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 06:40</span>
          <span class="news-item-title">爱彼迎表示将于2027年上半年推出人工智能旅行社</span>
          <span class="news-item-title-en">Airbnb says it’s launching an AI travel agent in the first half of 2027</span>
          <span class="news-value-point">💡 爱彼迎表示，即将推出的人工智能专员将帮助旅行者在整个住宿期间规划行程、比较选项、管理预订并获得帮助</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1028302/perplexity-teammates-ai-agents-work" target="_blank" rel="noopener" data-cat="keji" data-summary="Perplexity正在用自己的以工作为重点的人工智能代理来对抗OpenAI和Anthropic。创业公司新的始终在线的“团队成员”可以在一个工作区内担任多个角色，同时从Perplexity工具中提取现有项目、技能和记忆" data-title="Perplexity launches its own take on AI agents for work" data-date="11-06 06:26" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-06 06:26</span>
          <span class="news-item-title">Perplexity推出了自己对AI代理工作的看法</span>
          <span class="news-item-title-en">Perplexity launches its own take on AI agents for work</span>
          <span class="news-value-point">💡 Perplexity正在用自己的以工作为重点的人工智能代理来对抗OpenAI和Anthropic</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508107.html" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一举刷新“AI安全世界杯”CyberGym世界纪录" data-title="99.4%登顶全球第一！这个中国AI师承世界冠军" data-date="11-06 13:01" data-source="量子位">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 13:01</span>
          <span class="news-item-title">99.4%登顶全球第一！这个中国AI师承世界冠军</span>
          <span class="news-value-point">💡 一举刷新“AI安全世界杯”CyberGym世界纪录</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/06/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Lampard在Everton的欣赏， Glasner引发了森林大火， Zubimendi和Kroupi在聚光灯下， Carrick诉EmeryPremier联赛得分最高者没有什么能更好地概括Farhad Moshiri领导下的Everton的功能障碍，而不是" data-title="Premier League: 10 things to look out for this weekend" data-date="11-06 08:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-06 08:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 Lampard在Everton的欣赏， Glasner引发了森林大火， Zubimendi和Kroupi在聚光灯下， Carrick诉Emery…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm4g112qp051o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heisenberg ）回答了经理们在游戏周10中面临的一些最大困境。" data-title="Keep or sell Konsa? - FPL gameweek 10 dilemmas" data-date="11-06 06:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 06:26</span>
          <span class="news-item-title">保留或出售Konsa ？ - FPL游戏周10难题</span>
          <span class="news-item-title-en">Keep or sell Konsa? - FPL gameweek 10 dilemmas</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heise…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck5ynzry64p2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领电脑游戏《足球经理27》（ Football Manager 27 ） ，以及英国广播公司的读者和人工智能，对本周末的英超赛事进行了预测。" data-title="Sutton&#39;s predictions v Football Manager, the game" data-date="11-06 02:02" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 02:02</span>
          <span class="news-item-title">萨顿的预测v足球经理，比赛</span>
          <span class="news-item-title-en">Sutton's predictions v Football Manager, the game</span>
          <span class="news-value-point">💡 英国广播公司体育足球专家克里斯·萨顿（ Chris Sutton ）带领电脑游戏《足球经理27》（ Football Manager 27 ） …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13608535/jesus-de-miguel-funeral-family-friends-and-tenerife-players-gather-to-remember-striker-who-died-following-on-field-collision" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="特内里费岛前锋耶稣·德米格尔（ Jesus de Miguel ）的葬礼是在这位足球运动员在场上碰撞后去世后举行的。" data-title="Family, friends and Tenerife players gather for De Miguel&#39;s funeral" data-date="11-06 01:54" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:54</span>
          <span class="news-item-title">家人、朋友和特内里费岛球员聚集在一起参加德米格尔的葬礼</span>
          <span class="news-item-title-en">Family, friends and Tenerife players gather for De Miguel's funeral</span>
          <span class="news-value-point">💡 特内里费岛前锋耶稣·德米格尔（ Jesus de Miguel ）的葬礼是在这位足球运动员在场上碰撞后去世后举行的</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13608505/is-adil-rashid-still-englands-no-1-spinner-in-one-day-international-cricket" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在过去十年左右的英格兰白球板球的起伏中，其中一个常数是阿迪尔·拉希德（ Adil Rashid ）。" data-title="Is Rashid still England&#39;s No 1 spinner in ODI cricket?" data-date="11-06 01:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:45</span>
          <span class="news-item-title">拉希德仍然是英格兰ODI板球的头号旋转者吗？</span>
          <span class="news-item-title-en">Is Rashid still England's No 1 spinner in ODI cricket?</span>
          <span class="news-value-point">💡 在过去十年左右的英格兰白球板球的起伏中，其中一个常数是阿迪尔·拉希德（ Adil Rashid ）</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607998/premier-league-predictions-jones-knows-best-bets-nottingham-forest-vs-man-city-man-utd-vs-aston-villa-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩" data-title="PL Predictions: How will your team fare this weekend?" data-date="11-06 01:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:40</span>
          <span class="news-item-title">PL预测：您的团队本周末的表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your team fare this weekend?</span>
          <span class="news-value-point">💡 我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13607998/premier-league-predictions-jones-knows-best-bets-nottingham-forest-vs-man-city-man-utd-vs-aston-villa-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩" data-title="PL Predictions: How will your team fare this weekend?" data-date="11-06 01:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 01:40</span>
          <span class="news-item-title">PL预测：您的团队本周末的表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your team fare this weekend?</span>
          <span class="news-value-point">💡 我们的顶级提示者刘易斯·琼斯（ Lewis Jones ） ，又名琼斯知道（ Jones Knows ） ，在整个英超联赛周末提供他的分析和博彩</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw99zde82nmno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉经理Unai Emery即将同意与俱乐部续约。" data-title="Emery close to agreeing new Aston Villa contract" data-date="11-05 23:45" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-05 23:45</span>
          <span class="news-item-title">Emery即将同意新的阿斯顿维拉合同</span>
          <span class="news-item-title-en">Emery close to agreeing new Aston Villa contract</span>
          <span class="news-value-point">💡 阿斯顿维拉经理Unai Emery即将同意与俱乐部续约</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm93zvzzl33zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="菲尔·麦克纳尔蒂（ Phil McNulty ）写道，哈里·凯恩（ Harry Kane ）在拜仁慕尼黑（ Bayern Munich ）的新合同可能会结束他的英超联赛生涯，但他可以带领" data-title="What new Kane deal means for England and the Premier League record" data-date="11-05 22:44" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-05 22:44</span>
          <span class="news-item-title">新的凯恩交易对英格兰和英超联赛纪录意味着什么</span>
          <span class="news-item-title-en">What new Kane deal means for England and the Premier League record</span>
          <span class="news-value-point">💡 菲尔·麦克纳尔蒂（ Phil McNulty ）写道，哈里·凯恩（ Harry Kane ）在拜仁慕尼黑（ Bayern Munich ）的新合…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/05/the-international-break-is-almost-here-so-wave-goodbye-to-your-players-and-maybe-your-manager" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="过去是重置的时候，现在是重新雇佣的时候了，迈克尔·卡里克并不是唯一一个看着他肩上的英超经理。也许曼联复出对阵罗马的最有说服力的时刻是在终场哨响。" data-title="The international break is almost here: so wave goodbye to your players, and maybe your manager | Max Rushden" data-date="11-05 21:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-05 21:00</span>
          <span class="news-item-title">国际比赛即将到来：所以向你的球员，也许还有你的经理挥手告别| Max Rushden</span>
          <span class="news-item-title-en">The international break is almost here: so wave goodbye to your players, and maybe your manager | Max Rushden</span>
          <span class="news-value-point">💡 过去是重置的时候，现在是重新雇佣的时候了，迈克尔·卡里克并不是唯一一个看着他肩上的英超经理</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607957/man-utd-paul-merson-says-michael-carrick-needs-bruno-fernandes-on-side-and-matheus-cunha-to-be-consistent" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="保罗·梅森（ Paul Merson ）表示，迈克尔·卡里克（ Michael Carrick ）需要布鲁诺·费尔南德斯（ Bruno Fernandes ）的支持，并在曼联以3-2戏剧性地复出战胜罗马后，向马修斯·库尼亚（ Matheus Cunha" data-title="&#39;Carrick needs Bruno – but Villa could expose United&#39;" data-date="11-05 19:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 19:45</span>
          <span class="news-item-title">“卡里克需要布鲁诺–但维拉可能会暴露曼联”</span>
          <span class="news-item-title-en">'Carrick needs Bruno – but Villa could expose United'</span>
          <span class="news-value-point">💡 保罗·梅森（ Paul Merson ）表示，迈克尔·卡里克（ Michael Carrick ）需要布鲁诺·费尔南德斯（ Bruno Fern…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-05/10726787.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网11月5日电 据路透社报道，当地时间5日，葡萄牙球星克里斯蒂亚诺·罗纳尔多通过社交媒体宣布，他正式从葡萄牙国家足球队退役，结束多年的国家队生涯。" data-title="C罗宣布从葡萄牙国家足球队退役：“葡萄牙，永在我心”" data-date="11-05 18:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 18:54</span>
          <span class="news-item-title">C罗宣布从葡萄牙国家足球队退役：“葡萄牙，永在我心”</span>
          <span class="news-value-point">💡 中新网11月5日电 据路透社报道，当地时间5日，葡萄牙球星克里斯蒂亚诺·罗纳尔多通过社交媒体宣布，他正式从葡萄牙国家足球队退役，结束多年的国家队…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13608290/manchester-united-manager-latest-no-interim-planned-should-club-decide-to-sack-michael-carrick" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻被告知，如果他们决定在未来几周内取代迈克尔·卡里克，曼联不太可能任命另一位临时主教练。" data-title="Man Utd unlikely to appoint interim should they sack Carrick" data-date="11-05 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 18:00</span>
          <span class="news-item-title">如果他们解雇卡里克，曼联不太可能任命临时</span>
          <span class="news-item-title-en">Man Utd unlikely to appoint interim should they sack Carrick</span>
          <span class="news-value-point">💡 天空体育新闻被告知，如果他们决定在未来几周内取代迈克尔·卡里克，曼联不太可能任命另一位临时主教练</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13608280/liverpool-trey-nyoni-and-rio-ngumoha-starring-shows-reds-havent-spent-money-well-enough-says-jamie-carragher" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="杰米·卡拉格（ Jamie Carragher ）在欧洲冠军联赛中以3比2击败费内巴切（ Fenerbahce ）后，对利物浦的招募提出" data-title="Carra: Young guns starring shows Liverpool haven&#39;t spent money well enough" data-date="11-05 17:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 17:45</span>
          <span class="news-item-title">卡拉：主演的年轻枪手表明利物浦花的钱不够多</span>
          <span class="news-item-title-en">Carra: Young guns starring shows Liverpool haven't spent money well enough</span>
          <span class="news-value-point">💡 杰米·卡拉格（ Jamie Carragher ）在欧洲冠军联赛中以3比2击败费内巴切（ Fenerbahce ）后，对利物浦的招募提出</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/023/409.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 6 日消息，为进一步加强科普健康领域网络谣言突出问题整治，营造风清气正网络空间，近日，中央网信办印发通知，在全国范围内部署开展为期 2 个月的“清朗 · 整治科普健康类网络谣言”专项行动。中央网信办有关负责同志表示，本次专项行动重点整治以下 4 方面突出问题：（一）编造民生健康网络谣言，借机误导网民。一是以关注公众健康等为名义，将普通食品、保健品包装成“神药”，推广所谓“包治百病”偏方，发布伪科普信息，借审美焦虑制造“黄连素是减肥神药”等运动、减重类谣言。二是刻意夸大食品、药品、生活用品副作用，配以夸张骇人标题，编造所谓“长期服用降压药会使血管变脆”“献血会伤害身体”“味精加热有毒”“蜂蜜结晶不能吃”等缺乏科学依据、断章取义的谣言信息，制造焦虑恐慌情绪。三是以“科学辟谣”" data-title="重点整治滥用 AI 技术生成健康科普谣言等，中央网信办部署开展专项行动" data-date="11-06 16:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:38</span>
          <span class="news-item-title">重点整治滥用 AI 技术生成健康科普谣言等，中央网信办部署开展专项行动</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，为进一步加强科普健康领域网络谣言突出问题整治，营造风清气正网络空间，近日，中央网信办印发通知，在全国范围内部署开…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/408.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="小米 · 米家扫拖机器人 6 Max 开售于 2026 年 3 月，支持 AI 识别全景避障，“水箱版”官方定价 6599 元，“上下水版”官方定价 6999 元。按下方步骤下单，叠加 PLUS 立减 + 15% 国补后，“水箱版”仅需 2800.46 元、“上下水版”仅需 2981.26 元：领 8.2 折券：点此查看。下单时选择“以旧换新 → 个护健康 → 电动牙刷（无需回收）”补贴 20 元。晒单再返 20 元京豆。京东小米 米家扫地机器人 6 Max 水箱版以旧换新后 2800 元领 8.8 折券京东小米 米家扫地机器人 6 Max 上下水版以旧换新后 2981 元领 8.8 折券京东 11.11 无门槛红包至高 26888 元，支持即领即用，下单直接当钱花：点此抽取。这款产品支持实" data-title="小米米家扫拖机器人 6 Max 国补探新低：水箱版 2800 元、上下水版 2981 元" data-date="11-06 16:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:34</span>
          <span class="news-item-title">小米米家扫拖机器人 6 Max 国补探新低：水箱版 2800 元、上下水版 2981 元</span>
          <span class="news-value-point">💡 小米 · 米家扫拖机器人 6 Max 开售于 2026 年 3 月，支持 AI 识别全景避障，“水箱版”官方定价 6599 元，“上下水版”官方…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/407.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 6 日消息，异能者 (ERAZER) 现已推出二合一设备 U126。其本体采用平板电脑形态，随附磁吸背光键盘，支持 Windows 11 / Android 16 双操作系统。异能者 U126 拥有全金属机身，薄至 8.5mm，质量 760g。其基于英特尔酷睿 Ultra 5 处理器 115U，配备 LPDDR5 内存、SSD 存储，拥有一块 12.6&quot; 2560×1600 60Hz 450nits OLED 屏幕，集成 2 个 1W 扬声器、5MP 后摄，支持 Wi-Fi &amp; 蓝牙 5.0，内置 40.425Whr 电池。异能者 U126 二合一 8GB + 512GB 配置到手价 5,499 元、12GB + 512GB 配置到手价 5,999 元。京东异能者 U12" data-title="异能者推出 Windows &amp; Android 双系统二合一设备，基于 Ultra 5 115U" data-date="11-06 16:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:33</span>
          <span class="news-item-title">异能者推出 Windows & Android 双系统二合一设备，基于 Ultra 5 115U</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，异能者 (ERAZER) 现已推出二合一设备 U126</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/403.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 6 日消息，荣耀产品维护与升级 @荣耀小芳哥 今日公布了荣耀笔记本电脑 11 月升级内容，本月 PC 围绕 YOYO Claw 和 Magic 视界做体验优化，预计 11 月上旬开始逐步推送。YOYO Claw优化文档操作类场景，提供全面的文档编辑能力优化视频创作 Bot 操作，提供文生图、文生视频等操作能力等Magic 视界新增 AI 自定义卡片能力，支持用户自定义卡片新增桌面交互风格，提供桌面交互多样化选择等IT之家附覆盖机型如下：荣耀 WIN 游戏本 H9荣耀 WIN 游戏本 H7荣耀 MagicBook Pro 系列 2026荣耀 MagicBook 数字系列 2026荣耀笔记本 X Plus 系列 2026荣耀 MagicBook Art 14 2025荣耀 M" data-title="荣耀笔记本 11 月升级内容公布，优化 YOYO Claw、Magic 视界体验" data-date="11-06 16:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:31</span>
          <span class="news-item-title">荣耀笔记本 11 月升级内容公布，优化 YOYO Claw、Magic 视界体验</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，荣耀产品维护与升级 @荣耀小芳哥 今日公布了荣耀笔记本电脑 11 月升级内容，本月 PC 围绕 YOYO Cla…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727345.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州11月6日电(张煜欢 胡莘菻)走进浙江育英职业技术学院，一场有关无偿献血的科普宣讲活动正在举行。大三学生郑俊豪站在讲台前，没有空泛的说教，而是娓娓道来自己的一段段“热血历程”。" data-title="对话高校“热血”青年：传递生命暖意，续写青春担当" data-date="11-06 16:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:29</span>
          <span class="news-item-title">对话高校“热血”青年：传递生命暖意，续写青春担当</span>
          <span class="news-value-point">💡 中新网杭州11月6日电(张煜欢 胡莘菻)走进浙江育英职业技术学院，一场有关无偿献血的科普宣讲活动正在举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/402.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 6 日消息，据科技媒体 Android Authority 今天报道，谷歌现已为 Googlebook 笔记本带来 11 月更新，包含 30 项修复和改进，并更新 2026 年 11 月安全补丁。谷歌表示，本次更新有效降低了端侧 AI 的内存占用，释放 3GB-6GB 内存。上述改进可让笔记本获得更流畅的使用体验，打开大量标签页、处理高负载任务时，设备性能将得到提升，标签页重新加载和崩溃的情况有所减少。IT之家注意到，本次更新还修复了二合一设备的键盘 / 触控板输入无响应问题，以及使用 Zoom 多种特效时发生崩溃、使用显示器播放受 DRM 保护的视频时出现黑屏、外接 USB 麦克风无法使用等问题。其他修复还包括减少蓝牙耳机音频延迟、确保蓝牙 LE 鼠标在设备重启后能够可" data-title="谷歌为 Googlebook 带来 11 月更新：端侧 AI 性能占用降低，最多释放 6GB 内存" data-date="11-06 16:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 16:25</span>
          <span class="news-item-title">谷歌为 Googlebook 带来 11 月更新：端侧 AI 性能占用降低，最多释放 6GB 内存</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，据科技媒体 Android Authority 今天报道，谷歌现已为 Googlebook 笔记本带来 11 月…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727332.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社西藏林芝11月6日电 题：从采虫草到当向导：西藏波密普热村探索新增收路径" data-title="（走进中国乡村）从采虫草到当向导：西藏波密普热村探索新增收路径" data-date="11-06 16:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:12</span>
          <span class="news-item-title">（走进中国乡村）从采虫草到当向导：西藏波密普热村探索新增收路径</span>
          <span class="news-value-point">💡 中新社西藏林芝11月6日电 题：从采虫草到当向导：西藏波密普热村探索新增收路径</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727331.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社武汉11月6日电 (武一力 黄婧 尤海)为纪念孙中山先生诞辰160周年暨辛亥革命115周年，“世纪丰碑——孙中山与辛亥革命珍贵文物数字展”6日在武汉开幕，海内外观众可登录辛亥革命博物院官网、辛亥革命网观展。" data-title="孙中山与辛亥革命珍贵文物数字展“云端”开展" data-date="11-06 16:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:09</span>
          <span class="news-item-title">孙中山与辛亥革命珍贵文物数字展“云端”开展</span>
          <span class="news-value-point">💡 中新社武汉11月6日电 (武一力 黄婧 尤海)为纪念孙中山先生诞辰160周年暨辛亥革命115周年，“世纪丰碑——孙中山与辛亥革命珍贵文物数字展”…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727328.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网11月6日电 据“网信中国”微信公众号消息，为进一步加强科普健康领域网络谣言突出问题整治，营造风清气正网络空间，近日，中央网信办印发通知，在全国范围内部署开展为期2个月的“清朗·整治科普健康类网络谣言”专项行动。" data-title="中央网信办部署开展“清朗·整治科普健康类网络谣言”专项行动" data-date="11-06 16:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 16:06</span>
          <span class="news-item-title">中央网信办部署开展“清朗·整治科普健康类网络谣言”专项行动</span>
          <span class="news-value-point">💡 中新网11月6日电 据“网信中国”微信公众号消息，为进一步加强科普健康领域网络谣言突出问题整治，营造风清气正网络空间，近日，中央网信办印发通知，…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cmed33yn48gdo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="塞尔维亚公共广播机构于武契奇败选后直播道歉，承认多年偏颇报导、视而不见。新闻室内部不满累积十年，编辑与高层请辞，反对派声音开始出现，但分析指此举象征意义大于结构性改革。" data-title="塞尔维亚电视台为何在节目中就“多年来的片面报道”道歉？" data-date="11-06 16:00" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 16:00</span>
          <span class="news-item-title">塞尔维亚电视台为何在节目中就“多年来的片面报道”道歉？</span>
          <span class="news-value-point">💡 塞尔维亚公共广播机构于武契奇败选后直播道歉，承认多年偏颇报导、视而不见</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13607192/pierre-sage-under-pressure-how-crystal-palace-and-last-seasons-ligue-1-manager-of-the-year-are-both-suffering" target="_blank" rel="noopener" data-cat="zonghe" data-summary="去年五月，当皮埃尔·萨奇（ Pierre Sage ）作为RC Lens的胜利经理等待获得法兰西双门轿跑车奖杯时，他转向他的员工说： “你知道我们在哪里吗？”" data-title="What&#39;s gone wrong so quickly at Crystal Palace?" data-date="11-06 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 16:00</span>
          <span class="news-item-title">水晶宫怎么这么快就出了问题？</span>
          <span class="news-item-title-en">What's gone wrong so quickly at Crystal Palace?</span>
          <span class="news-value-point">💡 去年五月，当皮埃尔·萨奇（ Pierre Sage ）作为RC Lens的胜利经理等待获得法兰西双门轿跑车奖杯时，他转向他的员工说： “你知道我…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727317.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长春11月6日电 (记者 郭佳)2027年春节前夕，一支来自中国吉林的艺术团将赴英国、丹麦、爱尔兰演出，戏曲、民族舞蹈、民族器乐、杂技等节目将登上海外舞台。除剧场演出外，他们还将在当地开展快闪、巡游等活动。" data-title="二十载踏浪出海：吉林文化走向世界30余国" data-date="11-06 15:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 15:56</span>
          <span class="news-item-title">二十载踏浪出海：吉林文化走向世界30余国</span>
          <span class="news-value-point">💡 中新网长春11月6日电 (记者 郭佳)2027年春节前夕，一支来自中国吉林的艺术团将赴英国、丹麦、爱尔兰演出，戏曲、民族舞蹈、民族器乐、杂技等节…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cw62yyejjrlro/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这是澳门首宗国安案，案件过程并不公开，区锦新由“指派律师”辩护，审理法官及律师身份不明。从预审、开审到宣判，外界只能从政府新闻稿得知消息。" data-title="澳门国安首案宣判：区锦新囚12年半，妻子斥“莫须有迫害”" data-date="11-06 14:19" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 14:19</span>
          <span class="news-item-title">澳门国安首案宣判：区锦新囚12年半，妻子斥“莫须有迫害”</span>
          <span class="news-value-point">💡 这是澳门首宗国安案，案件过程并不公开，区锦新由“指派律师”辩护，审理法官及律师身份不明</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13608679/jacksonville-jaguars-33-10-baltimore-ravens-joe-fagnano-throws-two-interceptions-as-ravens-suffer-heavy-loss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乔·法尼亚诺（ Joe Fagnano ）的第一次NFL开局令人难忘，因为巴尔的摩乌鸦队（ Baltimore Ravens ）四分卫（他们本赛季的第三名）仅投掷了60码，并进行了两次拦截，因为杰克逊维尔美洲虎队（ Jacksonville Jaguars ）在周四晚上赢得了令人信服的33-10公" data-title="Fagnano&#39;s first NFL start ends in heavy Ravens defeat to Jaguars" data-date="11-06 14:14" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 14:14</span>
          <span class="news-item-title">法尼亚诺的第一次NFL首发以乌鸦队重击美洲虎队而告终</span>
          <span class="news-item-title-en">Fagnano's first NFL start ends in heavy Ravens defeat to Jaguars</span>
          <span class="news-value-point">💡 乔·法尼亚诺（ Joe Fagnano ）的第一次NFL开局令人难忘，因为巴尔的摩乌鸦队（ Baltimore Ravens ）四分卫（他们本赛…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/05/style/james-talarico-cowboy-boots-texas-senate-race.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="显然，德克萨斯州的选举不仅仅是鞋子。但象征意义很重要。" data-title="The Many Meanings of James Talarico’s Winning Cowboy Boots" data-date="11-06 10:25" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 10:25</span>
          <span class="news-item-title">James Talarico获奖牛仔靴的众多含义</span>
          <span class="news-item-title-en">The Many Meanings of James Talarico’s Winning Cowboy Boots</span>
          <span class="news-value-point">💡 显然，德克萨斯州的选举不仅仅是鞋子</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-06 16:39（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
