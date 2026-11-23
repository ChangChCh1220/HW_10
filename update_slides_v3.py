import re

html_path = 'wiki/slides/SL-FER-TaiwanFertilityDecline.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 升級 CSS：替換 duo-card 相關樣式為豐富飽滿的資訊圖表卡片架構
old_css_pattern = r'/\* 雙象限分流對比圖 \*/[\s\S]*?\.duo-card\.negative \.duo-card-title \{ color: #b91c1c; \}\s*\.duo-card-body \{[^}]+\}'

new_css = """/* 雙象限分流對比圖 (升級版：充實飽滿、三層次圖表、零留白空洞) */
        .duo-card-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 36px;
            width: 100%;
            height: 100%;
            align-items: stretch;
        }

        .duo-card {
            border-radius: 20px;
            padding: 30px 36px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            background: #ffffff;
            border: 3px solid #e2e8f0;
            overflow: hidden;
            box-sizing: border-box;
        }

        .duo-card.positive {
            background: linear-gradient(180deg, #f0fdf4 0%, #ffffff 32%);
            border-color: #22c55e;
        }

        .duo-card.negative {
            background: linear-gradient(180deg, #fef2f2 0%, #ffffff 32%);
            border-color: #ef4444;
        }

        .duo-card.neutral {
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 32%);
            border-color: #3b82f6;
        }

        /* 1. 卡片頂部標題 */
        .duo-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid rgba(0, 0, 0, 0.06);
            padding-bottom: 12px;
        }

        .duo-card-title {
            font-size: 28px;
            font-weight: 900;
            line-height: 1.25;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .duo-card.positive .duo-card-title { color: #15803d; }
        .duo-card.negative .duo-card-title { color: #b91c1c; }
        .duo-card.neutral .duo-card-title { color: #1d4ed8; }

        /* 2. Hero 數據指標橫條 (Badge / Metric Banner) */
        .duo-card-hero-metric {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 20px;
            border-radius: 12px;
            font-weight: 800;
        }
        .duo-card.positive .duo-card-hero-metric {
            background: #dcfce7;
            border: 1px solid #86efac;
            color: #14532d;
        }
        .duo-card.negative .duo-card-hero-metric {
            background: #fee2e2;
            border: 1px solid #fca5a5;
            color: #7f1d1d;
        }
        .duo-card.neutral .duo-card-hero-metric {
            background: #dbeafe;
            border: 1px solid #93c5fd;
            color: #1e3a8a;
        }
        .metric-badge-label {
            font-size: 18px;
            letter-spacing: 0.5px;
            opacity: 0.95;
        }
        .metric-badge-val {
            font-size: 25px;
            font-weight: 900;
        }

        /* 3. 結構化論點模組列表 (3 個立體要點卡，完全填滿空間) */
        .duo-card-items-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
            flex: 1;
            justify-content: space-between;
        }

        .duo-card-item {
            background: #f8fafc;
            border-left: 5px solid #cbd5e1;
            border-radius: 10px;
            padding: 12px 18px;
            font-size: 19px;
            line-height: 1.45;
            color: #1e293b;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
        }
        .duo-card.positive .duo-card-item {
            background: rgba(240, 253, 244, 0.7);
            border-left-color: #22c55e;
        }
        .duo-card.negative .duo-card-item {
            background: rgba(254, 242, 242, 0.7);
            border-left-color: #ef4444;
        }
        .duo-card.neutral .duo-card-item {
            background: rgba(239, 246, 255, 0.7);
            border-left-color: #3b82f6;
        }

        .duo-item-title {
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 4px;
            font-size: 21px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .duo-item-desc {
            font-size: 18px;
            color: #334155;
            line-height: 1.45;
        }

        /* 4. 底部機制警訊/政策引申條 (Callout Pill) */
        .duo-card-callout {
            border-radius: 10px;
            padding: 12px 18px;
            font-size: 18px;
            font-weight: 800;
            line-height: 1.4;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .duo-card.positive .duo-card-callout {
            background: #ecfdf5;
            border: 1px dashed #10b981;
            color: #065f46;
        }
        .duo-card.negative .duo-card-callout {
            background: #fff1f2;
            border: 1px dashed #f43f5e;
            color: #881337;
        }
        .duo-card.neutral .duo-card-callout {
            background: #eff6ff;
            border: 1px dashed #3b82f6;
            color: #1e40af;
        }"""

html = re.sub(old_css_pattern, new_css, html)

# 2. 定義 8 個頁面的新內容
pages_replacement = {}

# Page 9
pages_replacement[9] = """<!-- Page 9: 殘酷的婚姻斜坡 (性別不對稱) -->
    <div class="slide-page" id="p-9">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道一：婚配結構・性別不對稱</div>
                <div class="header-headline">殘酷的婚姻斜坡：薪水越高，男人越好結、女人越難嫁！</div>
            </div>
            <div class="header-section-indicator">02 / MARRIAGE BARRIERS</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">♂️ 男性結婚機率：隨經濟增長直線上升</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">清華 PSFD 計量模型實證</span>
                        <span class="metric-badge-val">初婚勝算 ＋18.2%</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">💵 薪資正向拉動力度顯著</div>
                            <div class="duo-item-desc">每月個人薪資每上升 1 萬元，初婚勝算顯著提升 <b>+18%</b>，薪資是男性在婚配市場最強通行證。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">⏰ 每週加班工時具溢價認同</div>
                            <div class="duo-item-desc">每週工時增加被社會常態認知為「勤奮、事業有成、具備供養家庭能力」，初婚勝算持續增長。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🏛️ 傳統家庭分工角色錨定</div>
                            <div class="duo-item-desc">文化與制度依舊預設男性為「家庭經濟主力承擔者」，男性的經濟實力能 100% 順暢轉化為婚配競爭力。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>機制總結</b>：男性的經濟優勢能無縫轉化為婚姻勝率，在階梯上越爬越高。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">♀️ 女性結婚機率：隨經濟自主反而下降</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">性別不對稱懲罰效應</span>
                        <span class="metric-badge-val">初婚勝算 －14.4%</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">📉 高薪女性遭受逆向擠壓</div>
                            <div class="duo-item-desc">每月個人薪資每增加 1 萬元，結婚機率逆向暴跌 <b>-14%</b>，高學歷高所得女性在婚姻市場面臨嚴苛處罰。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🛡️ 經濟自主建立「參考點門檻」</div>
                            <div class="duo-item-desc">女性以自身經濟條件為擇偶下限門檻，堅決拒絕傳統「經濟下嫁」，不願承擔婚後生活品質滑坡風險。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🚧 傳統「男高女低」觀念未變</div>
                            <div class="duo-item-desc">社會文化滯後於女性經濟崛起，高社經女性與中低薪男性雙向被擠出婚姻市場，造成結構性配對大失靈。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>結構警訊</b>：私領域文化停滯於舊時代，使得女性的經濟獨立反而成為走入婚姻的阻礙。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：女性經濟獨立了，婚配文化卻停留在舊時代，導致現代婚姻市場嚴重配對失靈！</div>
            <div class="footer-banner-source">計量實證：清華大學經濟學研究所 PSFD 追蹤資料 Logit 模型分析</div>
        </div>
    </div>
"""

# Page 12
pages_replacement[12] = """<!-- Page 12: 房價雙面刃 -->
    <div class="slide-page" id="p-12">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">爭議辨析一・因果機制拆解</div>
                <div class="header-headline">房價是雙面刃：它讓有房族更富，卻把無房青年徹底掏空！</div>
            </div>
            <div class="header-section-indicator">03 / HOUSING DEBATE</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">🏠 已購屋擁房族 ➜ 財富效果 (Wealth Effect)</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">資產淨值暴增・借貸容易</span>
                        <span class="metric-badge-val">二胎意願 顯著微升 (+)</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">📈 房產升值帶來淨資產溢價</div>
                            <div class="duo-item-desc">房價大漲使得擁房家庭紙面財富激增，房屋抵押轉貸極為容易，實質家庭流動資金大增。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🍼 充裕預算支持第二胎撫育</div>
                            <div class="duo-item-desc">住房資產鎖定了長期安居安全感，使既有家庭有餘裕負擔私托、保母與補習教育支出，提早生育第二胎。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">📊 跨國實證支持正向彈性</div>
                            <div class="duo-item-desc">韓國與台灣計量分析均顯示：在控制所得後，房產升值對既有擁房已婚夫妻之生育率呈現正向係數。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>資本收益</b>：房地產成為有產階級的安全網，資產增值轉化為抵禦育兒開銷的底氣。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">🚫 無房青年租屋族 ➜ 排擠效應 (Crowding-out)</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">頭期款儲蓄期延宕 15+ 年</span>
                        <span class="metric-badge-val">初婚成家 斷崖暴跌 (-)</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">⏳ 首付累積時間拉長 3 倍</div>
                            <div class="duo-item-desc">全國房價所得比突破歷史新高，無房青年籌措頭期款的時間從原本 5 年被極限拉長至 15 年以上。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">💸 高租金與房貸極限擠壓</div>
                            <div class="duo-item-desc">每月居住支出吃掉青年薪資 40% 以上，根本無力負擔結婚聘禮、蜜月婚宴與初生兒嬰幼兒開銷。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">💥 成家首要門檻遭到直接封死</div>
                            <div class="duo-item-desc">台灣「先有房再結婚」文化剛性極強，買不起房導致青年直接延後甚至永久放棄初婚，阻斷源頭。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>階級鴻溝</b>：房價狂飆實質拉大了資產階級與無產青年之間的「階級生育不平等」。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：房價上漲實質拉大了資產階級與無產青年之間的「階級生育不平等」！</div>
            <div class="footer-banner-source">實證文獻：台灣縣市面板資料分析 & 韓國住房資產實證研究</div>
        </div>
    </div>
"""

# Page 15
pages_replacement[15] = """<!-- Page 15: 爭議辨析三：因果評估 DID -->
    <div class="slide-page" id="p-15">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">爭議辨析三・因果評估 DID</div>
                <div class="header-headline">因果計量戳破謊言：生育津貼沒多生一個小孩，只造成「戶籍大風吹」！</div>
            </div>
            <div class="header-section-indicator">04 / POLICY ASSESSMENT</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">👻 跨區幽靈戶籍遷徙（Migration Bias）</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">各縣市跨區搶人零和賽局</span>
                        <span class="metric-badge-val">全國總量淨增 ＝ 0</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">📍 戶籍套利大風吹現象</div>
                            <div class="duo-item-desc">某縣市一旦宣布加碼 3～5 萬元津貼，鄰近縣市育齡夫妻立即辦理戶籍遷移，領完補助再遷回。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">📉 鄰近縣市出生數等量銳減</div>
                            <div class="duo-item-desc">加碼縣市新生兒看似微幅增加，但相鄰行政區出生數同步等量暴跌，雙重差分法（DID）證實全國總數毫無起色。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">💸 虛耗數十億地方公帑財政</div>
                            <div class="duo-item-desc">地方政府陷入盲目競標式的「津貼軍備競賽」，消耗龐大預算卻未實質多生任何一個健康胎兒。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>計量戳破</b>：雙重差分模型證實：所謂政策成效高達 85% 純屬跨區戶籍流動的統計偏誤。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">⏳ 生育時程微幅提早（Timing Effect）</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">受孕時程提前幾個月</span>
                        <span class="metric-badge-val">終身總胎數 毫無增加</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">⏱️ 僅刺激既有受孕計畫者提前</div>
                            <div class="duo-item-desc">現金補助僅僅讓原本就打算生小孩的已婚家庭，為了搶在補助截止日前受孕，將生育時程提前 3～6 個月。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🚫 未能動搖不婚不育核心阻力</div>
                            <div class="duo-item-desc">面對高房價、長工時與高昂撫養成本，幾萬元現金完全無法改變不願成家或不敢生二胎者的行為決策。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🛑 完育年齡總胎數完全停滯</div>
                            <div class="duo-item-desc">合成控制法（SCM）追蹤育齡婦女至 45 歲完育期，發現終身累積總生育數（Completed Fertility）統計上零增長。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>因果真相</b>：津貼只是預支了未來的出生配額，換來短暫回升幻象，隨後迎來更嚴重的雪崩。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：地方現金津貼淪為毫無意義的跨區搶人零和賽局，白白虛耗數十億國家財政！</div>
            <div class="footer-banner-source">評估模型：台灣縣市生育津貼雙重差分法（DID）與合成控制法（SCM）</div>
        </div>
    </div>
"""

# Page 16
pages_replacement[16] = """<!-- Page 16: 津貼陷阱 (冰山成本) -->
    <div class="slide-page" id="p-16">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">政策工具比較・成本結構</div>
                <div class="header-headline">幾萬元津貼如杯水車薪：平價公共托育才是真正的定心丸！</div>
            </div>
            <div class="header-section-indicator">04 / POLICY ASSESSMENT</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">🧊 水面上的微小冰山：一次性現金津貼</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">補助 3~5 萬 / 總養育成本 800 萬</span>
                        <span class="metric-badge-val">總開銷佔比 ＜ 1%</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">🪙 象徵性補助難抵長期沈重負擔</div>
                            <div class="duo-item-desc">幾萬元現金津貼相較於撫養一名孩子至大學畢業平均 800 萬元的總開銷，補助佔比連 1% 都不到。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">📉 極低且不可持續的拉動彈性</div>
                            <div class="duo-item-desc">公共經濟學實證估算：一次性現金津貼對總和生育率的拉動彈性僅 0.02～0.05，發放完畢效應即刻歸零。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🛑 無法分擔長達 18 年的育兒精力</div>
                            <div class="duo-item-desc">金錢無法解決雙薪家庭「誰來接送、生病誰請假、下班托育真空」的每日焦慮，無法解除不敢生二胎的恐懼。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>政策短視</b>：發放現金是一次性政治買票的捷徑，卻完全無法解決年輕父母長期的後顧之憂。
                    </div>
                </div>
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">🏔️ 水面下的龐大冰山：托育全面公共化</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">OECD 國際文獻實證效果</span>
                        <span class="metric-badge-val">政策彈性為現金的 6~8 倍</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">🛡️ 每月實質減輕雙薪支出 1.5~2 萬</div>
                            <div class="duo-item-desc">0～6 歲公托與準公幼將私立保母每月高達 2.5 萬元的費用壓低至數千元，6 年實質為家庭注入上百萬購買力。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">💼 保障女性職場發展與薪資曲線</div>
                            <div class="duo-item-desc">完善的日間托育讓新手媽媽無需在育嬰假結束後被迫辭職，阻斷「母職薪資懲罰」，維持家庭雙薪安全。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">📈 實證證明是唯一能提振二胎的解方</div>
                            <div class="duo-item-desc">新時代生育經濟學（Doepke et al., 2022）證實：高覆蓋公托是雙薪女性願意生第二胎的最關鍵制度支柱。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>長效治本</b>：生小孩不是一瞬間，而是 18 年的長跑；穩定的托育公共服務才是真正的定心丸。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：生小孩不是一瞬間，而是 18 年的長跑；只有平價公托才能分擔雙薪父母的未來！</div>
            <div class="footer-banner-source">理論支持：新時代生育經濟學（Doepke et al., 2022）</div>
        </div>
    </div>
"""

# Page 19
pages_replacement[19] = """<!-- Page 19: 質性訪談：姻親焦慮差距 -->
    <div class="slide-page" id="p-19">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道二：家庭文化・質性深入訪談</div>
                <div class="header-headline">零位男性擔心姻親，女性卻視為夢魘：傳統文化成了推力！</div>
            </div>
            <div class="header-section-indicator">05 / DOMESTIC WORK GAP</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">👨 受訪適婚男性：0 人擔憂姻親關係</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">台灣人口學刊質性訪談實證</span>
                        <span class="metric-badge-val">姻親焦慮比例 ＝ 0%</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">🏠 生活重心完全錨定原生家庭</div>
                            <div class="duo-item-desc">男性婚後多以男方家庭為中心或獨立居住，日常生活習慣、社交網絡與人際邊界幾乎感受不到任何衝擊。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🛋️ 零家務考核與長輩規訓壓力</div>
                            <div class="duo-item-desc">女方家屬對女婿普遍客氣尊重，極少要求男性適應女方家族生活習慣或承擔頻繁侍奉義務。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🚪 感受不到任何婚姻的「外推力」</div>
                            <div class="duo-item-desc">對男性而言，婚姻主要帶來生活照顧與情感伴侶的「向內拉力」，完全不存在來自姻親關係的逃避推力。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>結構盲區</b>：男性生活秩序不受擾動，因此常難以理解女性對走入傳統婚姻體系的深層恐懼。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">👩 受訪適婚女性：普遍視姻親為「最大恐懼」</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">質性訪談普遍反映強烈推力</span>
                        <span class="metric-badge-val">婚姻逃避率 顯著攀升</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">⛓️ 從父居同住與私領域邊界剝奪</div>
                            <div class="duo-item-desc">與公婆同住面臨日常作息被干預、家事標準受考核與個人隱私全面受限，生活秩序遭遇劇烈動盪。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🏮 節慶祭祀與長媳道德枷鎖</div>
                            <div class="duo-item-desc">年節繁重的宗族祭祀、孝道奉養期待與生育男嗣壓力，絕大部分仍單方面落在媳婦肩上，形成窒息式束縛。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🔥 堅決拒絕重蹈母親的委屈人生</div>
                            <div class="duo-item-desc">目睹上一代母親當全職家庭主婦受盡委屈看人臉色，現代高學歷經濟自主女性堅定拒絕跳入同一個火坑。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>文化推力</b>：女性在公共領域早已平權，但家庭私領域仍停滯於舊體制，直接將女性推離婚姻。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：女性經濟獨立後，有能力對不平等的傳統家庭制度說不；私領域文化停滯正在將女性推離家庭！</div>
            <div class="footer-banner-source">質性訪談：臺灣適婚年齡者進入婚姻與否的考量因素《人口學刊》</div>
        </div>
    </div>
"""

# Page 21
pages_replacement[21] = """<!-- Page 21: 破除單身刻板印象 -->
    <div class="slide-page" id="p-21">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">單身社會學・生活樣態</div>
                <div class="header-headline">單身女性活出高自主性，但單身男性面臨結構性邊緣化！</div>
            </div>
            <div class="header-section-indicator">06 / SINGLEHOOD REALITY</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">👩 中年中產單身女性：高社經、高自主與強連結</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">全國 40-59 歲始終單身女性調查</span>
                        <span class="metric-badge-val">專業白領比例 70.8%</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">💼 卓越的經濟實力與資產積累</div>
                            <div class="duo-item-desc">七成以上為高階主管與專業技術白領，平均月薪與自購房產比例顯著超越同齡曾婚女性，經濟毫無匱乏。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">☕ 活躍多元且自主的社交支持網絡</div>
                            <div class="duo-item-desc">每日上網 4.5 小時，朋友聚會、進修旅行頻繁；已婚女性走入家庭後社交圈暴跌至 22%，單身女性維持充沛人脈。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🧘‍♀️ 高生活滿意度與清晰自我價值</div>
                            <div class="duo-item-desc">徹底打破「敗犬」社會污名標籤，單身女性在免除傳統家庭勞務後，展現出極高的生活掌控感與幸福感。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>破除迷思</b>：單身絕非「被迫剩下」，而是現代高自主女性理性評估後所選擇的生活典範。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-header">
                        <div class="duo-card-title">👨 中年單身男性：面臨結構性風險與就業邊緣化</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">底層勞動力與社交支持真空</span>
                        <span class="metric-badge-val">無工作者比例 22.6%</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">📉 顯著的就業中斷與低薪困境</div>
                            <div class="duo-item-desc">無工作者比例達 <b>22.6%</b>（遠高於曾婚男性的 7.4%），收入階梯停滯於底層，經濟自我保障能力薄弱。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🏚️ 極度依賴年邁父母之原生家庭</div>
                            <div class="duo-item-desc">多數仍與年邁父母同住並仰賴父母照料生活，一旦父母離世，生活自理與財務將立刻陷入重大危機。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🧊 情感網絡狹窄與社會疏離危機</div>
                            <div class="duo-item-desc">男性缺乏深層社交網絡與互助團體，面臨退休後的社會孤立風險，成為孤獨死與長照未爆彈。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        ⚠️ <b>國安警訊</b>：社會過度聚焦高學歷未婚女性，卻嚴重忽視了低社經未婚男性的生存與長照危機。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：走入婚姻反而限縮了女性生活圈；但單身男性的就業與社會疏離是未來的隱形危機。</div>
            <div class="footer-banner-source">實證文獻：《人口學刊》中年單身者研究</div>
        </div>
    </div>
"""

# Page 24
pages_replacement[24] = """<!-- Page 24: 政策突圍一：社會住宅與托育 -->
    <div class="slide-page" id="p-24">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">政策典範轉移・結構突圍</div>
                <div class="header-headline">停止發錢催生！千億預算全面轉向「拆除成家障礙」！</div>
            </div>
            <div class="header-section-indicator">07 / POLICY BREAKTHROUGH</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">🏹 第一支箭：新婚青年社宅長租保障</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">公共住宅資源精準對接成家關鍵期</span>
                        <span class="metric-badge-val">5~10 年 平價安心長租</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">🏘️ 打破「先有房才配成家」魔咒</div>
                            <div class="duo-item-desc">中央與地方社宅保留 30% 配額專供登記新婚與育兒家庭，大幅降低青年步入婚姻的心理居住門檻。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🔐 5～10 年穩定租期免於被房東驅趕</div>
                            <div class="duo-item-desc">租金依所得級距給予市價 5～7 折優惠，並保障育兒期間免抽籤續約，打造安穩養育子女的環境。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">💡 解除青年首付累積的延宕阻礙</div>
                            <div class="duo-item-desc">青年無需被迫背負 30 年巨額房貸，直接將購屋首付轉化為家庭安家與育兒準備金，促成早婚早育。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>居住解套</b>：唯有國家主動保障平價長租，才能拆除橫亙在結婚路上的第一道高房價壁壘。
                    </div>
                </div>
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">🏹 第二支箭：0-6 歲公共托育普及率 80%+</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">千億津貼全數轉向托育公共化</span>
                        <span class="metric-badge-val">家長自負額 封頂 3,000 元/月</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">🏫 公托涵蓋率直攻 OECD 40%+ 標準</div>
                            <div class="duo-item-desc">盤點閒置公有建物與校舍，廣設社區公托與準公幼，終結搶抽籤托育排隊噩夢，保障人人有學位。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">💵 現金津貼收攏轉入服務給付</div>
                            <div class="duo-item-desc">停止無效的跨區軍備競賽現金撒幣，將百億經費全數補貼教保員薪資待遇與托育軟硬體設施。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">⏰ 普及彈性延托與夜間臨托機制</div>
                            <div class="duo-item-desc">配合現代雙薪家庭工時，設立平價延托至晚間 7 點與假日臨托，給予職業父母毫無顧慮的生育勇氣。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>服務為本</b>：唯有國家接住育兒的日常重擔，才能真正釋放已婚家庭生育第二胎的潛能。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：唯有國家主動分擔居住與育兒的長期成本，年輕人才有勇氣走入婚姻！</div>
            <div class="footer-banner-source">政策建議：公共經濟學與家庭福利典範轉移</div>
        </div>
    </div>
"""

# Page 25
pages_replacement[25] = """<!-- Page 25: 政策突圍二：鬆綁婚育包裹 -->
    <div class="slide-page" id="p-25">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">制度創新・包容性社會</div>
                <div class="header-headline">讓生育不再被單一婚姻綁架：鬆綁婚育包裹，邁向多元！</div>
            </div>
            <div class="header-section-indicator">07 / POLICY BREAKTHROUGH</div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">⚖️ 鬆綁《人工生殖法》：還原生殖自主權</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">生殖醫學平權・打破異性婚約壟斷</span>
                        <span class="metric-badge-val">開放 單身女性 & 多元伴侶</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">🧬 解除「唯合法異性夫妻」嚴苛門檻</div>
                            <div class="duo-item-desc">現行法規強制將人工生殖與傳統一夫一妻婚約綁定，實質剝奪了大量具撫養能力自主女性的生育權利。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">👩 釋放高社經單身女性生育潛能</div>
                            <div class="duo-item-desc">台灣有大量經濟獨立、渴望養育下一代但未進入婚姻的單身女性，開放人工生殖能直接帶動新生人口。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🌈 完備同志家庭人工生殖配套法制</div>
                            <div class="duo-item-desc">同婚合法化後應儘速補齊生殖醫療近用權，消除制度壁壘，讓渴望孩子的同志配偶能合法生兒育女。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>權利還原</b>：生育是基本人權，不該被一紙結婚證書所壟斷；法律應賦予願意撫養者溫暖支持。
                    </div>
                </div>
                <div class="duo-card positive">
                    <div class="duo-card-header">
                        <div class="duo-card-title">👶 非婚生子女與多元伴侶全方位平權</div>
                    </div>
                    <div class="duo-card-hero-metric">
                        <span class="metric-badge-label">西歐先進國家超低生育率逆轉關鍵</span>
                        <span class="metric-badge-val">推動 PACS 民事伴侶法</span>
                    </div>
                    <div class="duo-card-items-list">
                        <div class="duo-card-item">
                            <div class="duo-item-title">📜 建立彈性法律伴侶關係（PACS）</div>
                            <div class="duo-item-desc">借鏡法國經驗，在傳統高門檻婚姻之外，設立具備共同撫養、稅務減免但身分更自由的民事伴侶協約制度。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🍼 100% 抹除非婚生子女行政歧視</div>
                            <div class="duo-item-desc">在戶政登記、醫療健保與教育津貼申請上，全面抹除婚生與非婚生標籤，提供無差別國家保護。</div>
                        </div>
                        <div class="duo-card-item">
                            <div class="duo-item-title">🌍 借鏡法國 (62%) 與瑞典 (55%) 經驗</div>
                            <div class="duo-item-desc">歐洲實證顯示：成功擺脫超低生育率陷阱的國家，無一例外皆依靠包容非婚生育與多元家庭型態達成。</div>
                        </div>
                    </div>
                    <div class="duo-card-callout">
                        📌 <b>包容社會</b>：面對少子化國安危機，國家沒有本錢挑剔家庭型態；只要有愛與責任，就是國家的希望。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：借鏡西歐成功經驗：打破陳舊枷鎖，讓每一種充滿愛的家庭型態都能獲得國家的溫暖支持！</div>
            <div class="footer-banner-source">法制借鏡：法國 PACS 伴侶法與北歐政策</div>
        </div>
    </div>
"""

# 逐一精確替換頁面 HTML（從 <!-- Page X: 到下一個 <!-- Page X+1:）
for p, p_new_content in pages_replacement.items():
    next_p = p + 1
    pattern = r'(<!-- Page ' + str(p) + r':[\s\S]*?)(?=<!-- Page ' + str(next_p) + r':)'
    m = re.search(pattern, html)
    if m:
        html = html[:m.start()] + p_new_content + html[m.end():]
        print(f"Replaced page {p} with exact boundary successfully!")
    else:
        print(f"ERROR: Could not find page {p} with boundary!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished updating SL-FER-TaiwanFertilityDecline.html successfully!")
