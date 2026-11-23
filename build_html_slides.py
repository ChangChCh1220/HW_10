import os
import base64

def get_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_nycu = get_b64('wiki/slides/assets/NYCU.png')
b64_logo2 = get_b64('wiki/slides/assets/logo2.png')
b64_image = get_b64('wiki/slides/assets/image.png')

slides_data = [
    # Slide 1: Cover
    {
        "type": "cover",
        "title": "倒數第一的真相：到底是什麼影響了台灣的生育率？",
        "subtitle": "從 23 篇國內外實證論文看婚育因果、學術爭議與制度突圍",
        "badge": "科普學術講座・公共政策思辨",
        "author": "國立陽明交通大學 專題研究團隊",
        "scope": "文獻範疇：涵蓋 23 篇計量回歸、微觀追蹤資料與質性深度訪談研究",
        "logos": True
    },
    # Slide 2: Hook 1
    {
        "type": "hook",
        "number": "01",
        "question": "如果狂發津貼、放育嬰假就能拯救少子化……<br>為什麼台灣的總和生育率還是一路跌到 0.865，全球墊底？",
        "intuition": "「現在年輕人愛享受、不想承擔責任？房價太高、養不起小孩？」",
        "reveal": "實證研究告訴我們：大眾直覺診斷錯了病因，政策也就開錯了藥方！"
    },
    # Slide 3: Fact 1
    {
        "type": "content",
        "title": "數據震撼：生得少？還是根本「結不了婚」？",
        "tag": "人口結構真相",
        "cards": [
            {
                "style": "alert",
                "title": "關鍵真相：婚內生育率平穩，崩盤的是「結婚率」！",
                "text": "大眾總以為是「生得少」，實證數據卻指出真正致命的元兇是「大批適婚人口根本走不進婚姻」。"
            }
        ],
        "bullets": [
            "<b>30-34 歲男性未婚率</b>：從 1990 年的 <b>22.7%</b> 暴升至 2020 年的 <b>64.3%</b>（成長近 3 倍）！",
            "<b>30-34 歲女性未婚率</b>：從 1990 年的 <b>12.3%</b> 飆升至 2020 年的 <b>49.7%</b>（近半數未婚）！",
            "<b>已婚家庭的生育力</b>：近 20 年來，台灣已婚婦女平均生育數仍維持在 <b>1.5～1.7 個</b>，降幅極小。",
            "<b>核心結論</b>：不是夫妻結婚後不願意生，而是青年在婚姻的大門外被集體阻絕！"
        ]
    },
    # Slide 4: Math 1
    {
        "type": "math",
        "title": "核心數學：人口學 Kitagawa 總和生育率分解法",
        "tag": "計量因果分解",
        "formula": r"\Delta TFR = \sum_{a} \Delta M_a \cdot \bar{F}_a + \sum_{a} \bar{M}_a \cdot \Delta F_a",
        "vars": [
            ("M_a", "第 a 年齡組之有偶率（Marriage Proportion）"),
            ("F_a", "第 a 年齡組有偶婦女生育率（Marital Fertility Rate）")
        ],
        "decomposition": [
            {"label": "婚姻結構變動效應 (未婚率攀升)", "value": "82%", "desc": "每下降 1 點生育率，超過八成來自「結不了婚或初婚推遲」"},
            {"label": "婚內生育率變動效應 (夫妻少生)", "value": "18%", "desc": "婚內夫妻生育意願下降的解釋力不到兩成"}
        ],
        "summary": "少子化的核心本質是「不婚化」！任何忽視前端成家門檻的政策，都只是隔靴搔癢。"
    },
    # Slide 5: Mechanism 1
    {
        "type": "content",
        "title": "東亞特殊的制度枷鎖：「婚育包裹 (Marriage Package)」",
        "tag": "跨國制度對照",
        "cards": [
            {
                "style": "navy",
                "title": "歐美 vs. 台灣：非婚生育率的巨大鴻溝",
                "text": "<b>北歐與法國</b>：非婚生育率達 <b>50%～60%</b>，同居生子享有完全同等托育補助與法律權利。<br><b>台灣與東亞</b>：非婚生育率長年死守 <b>3.8%</b> 左右（[[P10-Wang25]], [[P20-Cheng23]]）。"
            }
        ],
        "bullets": [
            "在台灣，「婚姻」是合法生養子女的<b>唯一特許入場券</b>。",
            "非婚生子女與未婚生子面臨社會輿論、醫療法規限制與行政福利上的多重隱形阻礙。",
            "<b>連帶因果</b>：在「婚育高度綑綁」下，一旦婚姻市場失靈，生育率便會直接墜入深淵！"
        ]
    },
    # Slide 6: Hook 2
    {
        "type": "hook",
        "number": "02",
        "question": "長輩常嘆：「現在年輕人太有想法、太享受自由，根本不想結婚成家？」",
        "intuition": "「年輕世代崇尚單身主義，把婚姻當作洪水猛獸？」",
        "reveal": "深入調查顯示：青年不是排斥婚姻，而是深陷「想婚卻結不了」的現實泥淖！"
    },
    # Slide 7: Marriage Intention
    {
        "type": "content",
        "title": "想婚卻結不了：意願與現實的殘酷鴻溝",
        "tag": "微觀意願調查",
        "cards": [
            {
                "style": "navy",
                "title": "實證調查數據（[[P21-Liu26]], [[P22-Yuan22]], [[P23-Yang23]]）",
                "text": "30 歲以前的未婚男女中，有超過 <b>85%</b> 明確表示「未來希望走入婚姻」。"
            }
        ],
        "bullets": [
            "<b>為什麼年屆適婚依然單身？</b>",
            "<b>1. 尚未遇到合適對象（>60%）</b>：重視心靈契合與情感品質，拒絕為結而結、將就湊合。",
            "<b>2. 經濟條件未就緒（>45%）</b>：低薪、工作不穩定、自認無法承擔家庭生活開銷。",
            "<b>3. 寧缺勿濫的謹慎態度</b>：目睹父母婚姻爭吵或同儕離婚，對婚姻品質抱持更高要求。"
        ]
    },
    # Slide 8: Housing Requirement
    {
        "type": "content",
        "title": "婚姻的入學特許證：婚前必須先有房？",
        "tag": "成家物質門檻",
        "cards": [
            {
                "style": "alert",
                "title": "林佩萱、許碧純（2023）實證調查 [[P18-Lin23]]",
                "text": "<b>55% 未婚女性</b> 堅持「婚前必須先買房子」，顯著高於男性的 <b>43%</b>！"
            }
        ],
        "bullets": [
            "<b>資源交換理論與母職補償</b>：女性預期婚後將承擔家務、生育與職涯中斷風險，因而要求「男方備房」作為制度防衛。",
            "<b>女性參考點門檻（Reference Point）</b>：高收入與高學歷女性將自身社經地位作為底線，要求男方必須持平或更優。",
            "<b>殘酷代價</b>：房價飆漲直接將買房變成了「婚姻的入學特許資格」，大幅拉長未婚青年的蓄資年限！"
        ]
    },
    # Slide 9: Marriage Gradient
    {
        "type": "table_slide",
        "title": "性別不對稱的婚姻斜坡（Marriage Gradient）",
        "tag": "PSFD 計量實證",
        "subtitle": "顏世昇（2024）[[P17-Yen24]] PSFD 追蹤資料 Logit 模型估計結果",
        "table": {
            "headers": ["自變數指標", "對男性初婚機率之影響", "對女性初婚機率之影響", "背後社會學機制"],
            "rows": [
                ["個人每月薪資收入", "顯著正向 (+0.18**)", "顯著負向 (-0.14**)", "傳統「男主外」養家期待 vs. 女性經濟自主不願下嫁"],
                ["每週工作工時長度", "顯著正向 (+0.08*)", "顯著負向 (-0.11**)", "男性加班被視為事業有成；女性工時長被認為難以兼顧家庭"],
                ["縣市房價所得比", "顯著負向 (-0.23***)", "顯著負向 (-0.19***)", "高房價摧毀男女成家意願，形成跨性別成家阻礙"]
            ]
        },
        "summary": "傳統「男高女低」婚姻斜坡未解，導致高學歷女性與中低收入男性同時深陷「配對不能」的雙重擠壓！"
    },
    # Slide 10: Cohabitation Myth
    {
        "type": "content",
        "title": "破解迷思：同居能拯救生育率嗎？",
        "tag": "婚前親密關係變遷",
        "cards": [
            {
                "style": "alert",
                "title": "鄭雁馨（2023, JMF）實證震撼 [[P20-Cheng23]]",
                "text": "台灣青年同居率激增近 <b>40%</b>，但同居且打算結婚者自 <b>70% 暴跌至 30%</b>！"
            }
        ],
        "bullets": [
            "<b>同居性質的徹底質變</b>：同居在台灣不再是「試婚跳板」，而成為「單身生活的合租延長與替代」。",
            "<b>極度缺乏生育意願</b>：台灣同居伴侶中生育小孩的比例低於 3%，極少人在同居階段生育。",
            "<b>結論</b>：若無配套的法制賦權與社會包容，同居不僅無法彌補少子化，反而進一步延遲初婚！"
        ]
    },
    # Slide 11: Parental Pressure
    {
        "type": "content",
        "title": "逼婚的代間拉扯：父母催婚有用嗎？",
        "tag": "代間關係與成婚",
        "cards": [
            {
                "style": "navy",
                "title": "Chen & Huang（2026, JMF）[[P19-Chen26]] & 袁詠蓁、孔祥明（2022）[[P22-Yuan22]]",
                "text": "<b>49%</b> 未婚青年長期面臨父母逼婚催婚壓力，被逼婚者結婚機率顯著較高（Hazard Ratio = 2.15）。"
            }
        ],
        "bullets": [
            "<b>逼婚的邊際效益遞減</b>：逼婚主要受父母自身世代經驗驅動，但年輕一代母親已開始逐步放棄逼婚。",
            "<b>長輩的策略妥協</b>：面對居高不下的成家門檻，部分長輩甚至退守「先抱孫沒結婚沒關係」。",
            "<b>青年的抗拒與防衛</b>：過度的家族規訓反而引發青年對婚姻的強烈反感，選擇拉長單身戰線。"
        ]
    },
    # Slide 12: Hook 3
    {
        "type": "hook",
        "number": "03",
        "question": "「高房價是最好的避孕藥」幾乎是社會共識……<br>為什麼國內外部分經濟學實證卻發現：<b>「房價越漲，生育率反而上升」</b>？",
        "intuition": "「學者做研究跟現實脫節？還是數據算錯了？」",
        "reveal": "深入檢驗才發現：房價是把雙面刃，它極端分化了「資產族」與「無產青年」！"
    },
    # Slide 13: Debate 1 Housing
    {
        "type": "content",
        "title": "爭議辨析（一）：房價的財富效果 vs. 負擔排擠效果",
        "tag": "經濟機制矛盾拆解",
        "cards": [
            {
                "style": "navy",
                "title": "學術矛盾的關鍵根源：取決於家庭的「住房權屬（Tenure Status）」！",
                "text": "同一個房價上漲信號，在不同階級家庭中產生截然相反的因果效應。"
            }
        ],
        "bullets": [
            "<b>已購屋擁房家庭（[[P01-Yao24]], [[P02-Choi25]]） $\implies$ 財富效果（+）</b>：<br>房價上漲帶來資產增值與抵押借貸空間，家庭安全感提升，促使其提早生育二胎。",
            "<b>無房青年與租屋族（[[P03-Tsai21]], [[P09-VanWijk25]]） $\implies$ 負擔排擠效果 (-)</b>：<br>購屋自備款儲蓄期拉長 10 年以上，高房租與高房貸極限擠壓育兒預算，直接放棄生育。",
            "<b>核心啟示</b>：房價並非對所有人都「避孕」，它實質拉大了台灣世代與階級之間的生育不平等！"
        ]
    },
    # Slide 14: Debate 2 Marriage Target
    {
        "type": "content",
        "title": "爭議辨析（二）：房價打擊的真正死穴是「前端婚姻」",
        "tag": "因果傳導途徑",
        "cards": [
            {
                "style": "alert",
                "title": "巨觀計量彈性比較（[[P03-Tsai21]], [[P07-Wu25]], [[P17-Yen24]]）",
                "text": "房價每上升 10%，已婚婦女生育率微跌 <b>1.5%</b>，但未婚青年的初婚率卻劇跌 <b>7.2%</b>！"
            }
        ],
        "bullets": [
            "<b>已婚家庭的韌性</b>：已步入婚姻的夫妻，生養決策受親職承諾支撐，房價衝擊相對溫和。",
            "<b>未婚青年的致命打擊</b>：高房價將「購屋門檻」前置為結婚的必要篩選條件，直接消滅青年的成家能力。",
            "<b>空間擴散效應</b>：雙北房價高漲外溢至桃竹與台中，青年初婚年齡全面推遲至 32 歲以上。"
        ]
    },
    # Slide 15: Hook 4
    {
        "type": "hook",
        "number": "04",
        "question": "全台縣市瘋狂加碼生育津貼：兩萬、三萬、五萬甚至十萬……<br>發放百億真金白銀，到底催生出了多少嬰兒？",
        "intuition": "「只要政府給的錢夠多，年輕人就會願意生？」",
        "reveal": "雙重差分法（DID）與合成控制法（SCM）戳破了現金發放的虛假幻覺！"
    },
    # Slide 16: Debate 3 Subsidy DID
    {
        "type": "content",
        "title": "爭議辨析（三）：生育津貼是「真實增產」還是「幽靈遷徙」？",
        "tag": "嚴謹因果評估",
        "cards": [
            {
                "style": "alert",
                "title": "DID 與 SCM 計量實證（[[P04-Hsu23]], [[P15-Chien24]], [[P16-Lai24]]）",
                "text": "縣市加碼生育津貼後，新生兒總數在全國層次<b>實質淨增量為 0</b>！"
            }
        ],
        "bullets": [
            "<b>虛假的繁榮：中介遷移動機（Migration Bias）</b>：<br>某縣市加碼津貼，該縣市出生數微幅增加，但鄰近縣市同步銳減——家庭只是「為了領錢遷戶籍」，並非真實增產。",
            "<b>生育時程微幅提早（Timing Effect）</b>：<br>政策僅促使原本就計畫生育的夫妻提早幾個月受孕，並未提高終身總生育胎數。",
            "<b>政策警訊</b>：地方政府陷入競相撒錢的「零和賽局」，巨額財政資源遭到嚴重錯配與虛耗！"
        ]
    },
    # Slide 17: Cash vs Service
    {
        "type": "content",
        "title": "津貼陷阱：一次性現金 vs. 長期托育公共化",
        "tag": "育兒成本結構比較",
        "cards": [
            {
                "style": "navy",
                "title": "撫養成本結構的殘酷算術（[[P08-Koh26]], [[P14-Doepke22]]）",
                "text": "一次性津貼 3-5 萬元，佔撫養一名子女至成年（500-800 萬元）的成本<b>不到 1%</b>！"
            }
        ],
        "bullets": [
            "<b>現金津貼的極限</b>：一次性補助屬於短期移轉性支付，無法降低家長長達 18 年的育兒機會成本。",
            "<b>托育公共化的長期威力</b>：<br>0-2 歲平價公托與 2-6 歲準公幼，每月能實質減輕家庭 1.5～2 萬元負擔，大幅解放母親就業。",
            "<b>國際文獻彈性</b>：托育服務供給的擴充對生育率的拉動彈性，是一次性現金津貼的 <b>6 至 8 倍</b>！"
        ]
    },
    # Slide 18: Hook 5
    {
        "type": "hook",
        "number": "05",
        "question": "台灣性別平等指標位居亞洲第一……<br>為什麼高學歷、經濟獨立的當代女性，反而最不敢踏入婚姻？",
        "intuition": "「女性學歷越高眼光越高、不願意相夫教子？」",
        "reveal": "制度性錯配告訴我們：當公領域走向平等，私領域卻依然傳統，女性的理性最優解只能是「撤退」！"
    },
    # Slide 19: Debate 4 Gender Incoherence
    {
        "type": "content",
        "title": "爭議辨析（四）：公領域前進 vs. 私領域父系束縛",
        "tag": "制度性不協調 (Institutional Incoherence)",
        "cards": [
            {
                "style": "alert",
                "title": "Doepke et al. (2022) [[P14-Doepke22]] & 林書妤等（2023）[[P06-Lin23]]",
                "text": "<b>公領域邁向現代化</b>（女性高教率 63%、白領佔比七成、講求職場績效）<br><b>私領域高度停滯</b>（婚內家務育兒女性仍承擔 75% 以上，男性分擔僅佔零頭）"
            }
        ],
        "bullets": [
            "<b>母親的「雙重輪班（Second Shift）」</b>：白天在職場打拼，晚上下班繼續面對沉重無償家務。",
            "<b>母職懲罰（Motherhood Penalty）</b>：生育中斷職涯，重返職場薪資折損達 20% 以上。",
            "<b>結論</b>：當婚姻對女性而言意味著「勞動加倍、地位矮化」，女性選擇不婚不育正是最理性的自我保護！"
        ]
    },
    # Slide 20: In-law Push Force
    {
        "type": "content",
        "title": "身分枷鎖與姻親焦慮：當代女性的婚姻推力",
        "tag": "質性訪談深度剖析",
        "cards": [
            {
                "style": "navy",
                "title": "袁詠蓁、孔祥明（2022）《人口學刊》[[P22-Yuan22]]",
                "text": "訪談中<b>無任何男性</b>擔憂婚後姻親關係；但<b>幾乎所有受訪女性</b>均視姻親關係為最大夢魘！"
            }
        ],
        "bullets": [
            "<b>從父居文化與婆媳磨合</b>：過年過節的儀式義務、被婆家當作「外人」卻要求承擔媳婦責任的雙重矛盾。",
            "<b>母職創傷的世代傳承</b>：<br>「看著媽媽當全職家庭主婦，用錢看臉色、受盡委屈，我為什麼要重複一樣的人生？」",
            "<b>自主性的覺醒</b>：當女性具備經濟獨立能力，不再需要靠婚姻過活，傳統不平等的家庭結構直接將她們推離婚姻門口。"
        ]
    },
    # Slide 21: Hook 6
    {
        "type": "hook",
        "number": "06",
        "question": "不結婚的單身者，老了真的會孤苦無依、成為社會負擔嗎？",
        "intuition": "「單身就是敗犬、魯蛇、老了沒人照顧的社會問題？」",
        "reveal": "楊靜利等（2023）全國調查打破偏見：中年單身女性活出極高自主性，但家庭長照卻成了新隱憂！"
    },
    # Slide 22: Always Single Reality
    {
        "type": "content",
        "title": "破除刻板印象：中年始終單身者的真實樣態",
        "tag": "全國人口抽樣調查",
        "cards": [
            {
                "style": "success",
                "title": "楊靜利、黃于珊、翁康容（2023）[[P23-Yang23]]",
                "text": "分析 40-59 歲始終未婚者（Always-Single）：打破「敗犬與魯蛇」單一標籤！"
            }
        ],
        "bullets": [
            "<b>單身女性的高社經樣態</b>：40-59 歲單身女性高達 <b>70.8% 為白領</b>，平均工作月收入顯著高於曾婚女性。",
            "<b>活躍的社交網絡</b>：單身女性每日上網 4.5 小時、線上線下聚餐參與率最高；反觀曾婚女性走入家庭後社交圈大幅縮減至 22%。",
            "<b>單身男性的結構性風險</b>：單身男性無工作者比例達 22.6%，社交網絡狹窄，面臨較高的孤立風險。"
        ]
    },
    # Slide 23: Single Elder Care
    {
        "type": "content",
        "title": "單身世代的新負擔：未婚成了「家庭長照主力」？",
        "tag": "代間照顧新困境",
        "cards": [
            {
                "style": "alert",
                "title": "殘酷的代間照顧轉移（[[P23-Yang23]]）",
                "text": "40-59 歲單身者近半數與父母同住（男 48.5%、女 45.4%），單身女性承擔了不成比例的長照重擔！"
            }
        ],
        "bullets": [
            "<b>隱形道德綁架</b>：「反正你沒家室、沒小孩，照顧年邁父母的責任就歸你。」",
            "<b>雙重夾擊的單身世代</b>：青年時因高房價與性別分工未婚，中年後卻直接被吸入高齡長照的泥淖。",
            "<b>政策呼籲</b>：少子化與超高齡化並行下，政府若不推動「長照全面公共化」，單身人口將面臨照護貧窮與長照悲劇。"
        ]
    },
    # Slide 24: Holistic Model
    {
        "type": "content",
        "title": "台灣低生育率的立體因果鏈條全景圖",
        "tag": "23 篇論文實證共識",
        "cards": [
            {
                "style": "navy",
                "title": "因果系統全景整合矩陣",
                "text": "少子化不是單一原因，而是四重制度障礙連環扣殺的結果："
            }
        ],
        "bullets": [
            "<b>1. 前端婚姻門檻</b>：高房價與成家物質要求 + 男高女低婚姻斜坡 $\implies$ <b>初婚年齡推遲、未婚率突破 64%</b>",
            "<b>2. 制度包裹枷鎖</b>：非婚生育率僅 3.8%（制度與文化全面排斥未婚生育） $\implies$ <b>不婚直接等於不育</b>",
            "<b>3. 私領域性別失衡</b>：職場高壓長工時 + 私領域家務母職全包 $\implies$ <b>育齡女性理性撤退</b>",
            "<b>4. 政策工具錯配</b>：地方撒錢發放一次性津貼，缺乏長期公共托育與居住保障 $\implies$ <b>百億補貼淪為空轉</b>"
        ]
    },
    # Slide 25: Policy Shift 1
    {
        "type": "content",
        "title": "政策突圍（一）：從「發錢催生」到「拆除婚姻障礙」",
        "tag": "政策典範轉移",
        "cards": [
            {
                "style": "navy",
                "title": "重置政策戰場（[[P12-Tan26]], [[P14-Doepke22]]）",
                "text": "停止將重心放在婚後的零星發錢，全面轉向解決前端成家門檻！"
            }
        ],
        "bullets": [
            "<b>1. 居住正義直接對接新婚成家</b>：<br>大舉擴建長期租期（5-10年）青年社宅，將成家從「先買得起房」的沉重枷鎖中鬆綁。",
            "<b>2. 托育全面公共化與準公托普及</b>：<br>將千億發錢預算轉入 0-6 歲平價高品質公托，徹底解決雙薪家庭後顧之憂。",
            "<b>3. 強制落實男性育嬰假（Use-it-or-lose-it）</b>：<br>法制化保障男性育兒參與，強制分擔家庭無償勞動，消除女性母職就業懲罰。"
        ]
    },
    # Slide 26: Policy Shift 2
    {
        "type": "content",
        "title": "政策突圍（二）：鬆綁「婚育包裹」，邁向包容性制度",
        "tag": "多元制度重構",
        "cards": [
            {
                "style": "navy",
                "title": "讓生育不再被單一傳統婚姻形式綁架（[[P10-Wang25]], [[P20-Cheng23]], [[P22-Yuan22]]）",
                "text": "借鏡西歐成功經驗：賦予多元伴侶與個人平等的生育權利。"
            }
        ],
        "bullets": [
            "<b>1. 《人工生殖法》實質鬆綁</b>：<br>保障單身女性、未婚伴侶與同性伴侶合法使用人工生殖技術之權利，實現生育自主。",
            "<b>2. 非婚生子女全面平權</b>：<br>消除戶籍登記、法律地位、社會保險與稅務減免上對非婚生子女的一切歧視。",
            "<b>3. 多元家屬法律保障</b>：<br>法制化承認穩定同居伴侶之撫養、醫療探視與照護權益，營造友善育兒生態。"
        ]
    },
    # Slide 27: Conclusion
    {
        "type": "conclusion",
        "title": "結語：少子化是年輕人對僵化體制的理性反抗",
        "quote": "「少子化從來不是年輕世代對未來的冷漠或自私，<br>而是他們在面對高房價、長工時、私領域不平等與僵化制度時，<br>所做出的最沉重、最理性的非暴力抵抗。」",
        "takeaway": "唯有當社會制度願意共同分擔成家與照護的成本，真正容得下個體的生活、自由與尊嚴，生育才可能再次成為被期待的幸福。"
    },
    # Slide 28: Closing
    {
        "type": "closing",
        "title": "感謝聆聽・敬請指教",
        "team": "國立陽明交通大學 專題研究團隊",
        "database": "本簡報實證基礎：收錄於 Karpathy LLM Wiki 知識庫（23 篇論文解析、Kitagawa 模型與實證矩陣）",
        "qa": "歡迎交流與提問 (Q&A)",
        "logos": True
    }
]

# 生成 HTML 簡報
html_template = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>到底是什麼影響了台灣的生育率？——23篇實證論文的因果拆解</title>
    <!-- KaTeX CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body);"></script>
    <style>
        :root {
            --primary: #0f172a;       /* 深石板藍 */
            --navy-dark: #0b132b;     /* 極致深海軍藍 */
            --navy-primary: #1e3a8a;  /* 經典海軍藍 */
            --navy-accent: #3b82f6;   /* 亮藍點綴 */
            --navy-light: #eff6ff;    /* 極淡海軍藍背景 */
            --text-dark: #0f172a;     /* 深黑文字 */
            --text-muted: #475569;    /* 次要文字 */
            --card-bg: #f8fafc;       /* 卡片背景 */
            --border-color: #cbd5e1;  /* 邊框線 */
            --alert-red: #ef4444;     /* 警示紅 */
            --alert-bg: #fef2f2;
            --success-green: #10b981; /* 成功綠 */
            --success-bg: #f0fdf4;
            --gold: #f59e0b;          /* 琥珀金 */
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
            background-color: var(--navy-dark);
            color: var(--text-dark);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            user-select: none;
        }

        /* 投影片主容器 (16:9 比例) */
        #deck-container {
            width: 95vw;
            max-width: 1440px;
            aspect-ratio: 16 / 9;
            background-color: #ffffff;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border-radius: 12px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .slide {
            width: 100%;
            height: 100%;
            padding: 50px 70px;
            display: none;
            flex-direction: column;
            justify-content: flex-start;
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
            background-color: #ffffff;
        }

        .slide.active {
            display: flex;
            opacity: 1;
            z-index: 10;
        }

        /* 頁首標籤與標題 */
        .slide-header {
            margin-bottom: 25px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 15px;
        }

        .slide-tag {
            font-size: 14px;
            font-weight: 700;
            color: var(--navy-accent);
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 6px;
        }

        .slide-title {
            font-size: 34px;
            font-weight: 800;
            color: var(--primary);
            line-height: 1.25;
        }

        /* 卡片設計 */
        .card {
            border-radius: 8px;
            padding: 20px 25px;
            margin-bottom: 22px;
        }

        .card-navy {
            background-color: var(--navy-light);
            border-left: 6px solid var(--navy-primary);
        }

        .card-alert {
            background-color: var(--alert-bg);
            border-left: 6px solid var(--alert-red);
        }

        .card-success {
            background-color: var(--success-bg);
            border-left: 6px solid var(--success-green);
        }

        .card-title {
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 8px;
            color: var(--navy-primary);
        }

        .card-alert .card-title {
            color: var(--alert-red);
        }

        .card-success .card-title {
            color: var(--success-green);
        }

        .card-text {
            font-size: 19px;
            line-height: 1.6;
            color: #334155;
        }

        /* 列點樣式 */
        .bullet-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .bullet-list li {
            font-size: 20px;
            line-height: 1.6;
            color: #1e293b;
            position: relative;
            padding-left: 30px;
        }

        .bullet-list li::before {
            content: "•";
            position: absolute;
            left: 5px;
            color: var(--navy-accent);
            font-size: 28px;
            line-height: 1;
        }

        /* 封面 Slide */
        .slide-cover {
            background: linear-gradient(135deg, #0b132b 0%, #1c2541 100%);
            color: #ffffff;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 60px 80px;
        }

        .slide-cover .badge {
            display: inline-block;
            background: rgba(59, 130, 246, 0.2);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.4);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 15px;
            font-weight: 600;
            letter-spacing: 1px;
            margin-bottom: 24px;
        }

        .slide-cover h1 {
            font-size: 46px;
            font-weight: 900;
            line-height: 1.25;
            margin-bottom: 18px;
            color: #ffffff;
        }

        .slide-cover h2 {
            font-size: 24px;
            font-weight: 400;
            color: #94a3b8;
            margin-bottom: 40px;
            max-width: 900px;
        }

        .logo-row {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 45px;
            margin-bottom: 35px;
            background: rgba(255, 255, 255, 0.95);
            padding: 16px 36px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        }

        .logo-row img {
            height: 52px;
            object-fit: contain;
        }

        .cover-meta {
            font-size: 16px;
            color: #cbd5e1;
            margin-top: 5px;
        }

        /* 懸念提問 Slide */
        .slide-hook {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
            color: #ffffff;
            justify-content: center;
            padding: 60px 90px;
        }

        .hook-number {
            font-size: 20px;
            font-weight: 800;
            color: #60a5fa;
            letter-spacing: 3px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hook-number::after {
            content: "";
            flex: 1;
            height: 2px;
            background: rgba(96, 165, 250, 0.4);
        }

        .hook-question {
            font-size: 38px;
            font-weight: 800;
            line-height: 1.4;
            color: #ffffff;
            margin-bottom: 35px;
        }

        .hook-box {
            background: rgba(255, 255, 255, 0.1);
            border-left: 6px solid var(--gold);
            padding: 20px 25px;
            border-radius: 6px;
            margin-bottom: 20px;
        }

        .hook-box-title {
            font-size: 18px;
            font-weight: 700;
            color: var(--gold);
            margin-bottom: 6px;
        }

        .hook-box-text {
            font-size: 22px;
            color: #f1f5f9;
        }

        .hook-reveal {
            font-size: 22px;
            font-weight: 600;
            color: #38bdf8;
            margin-top: 15px;
        }

        /* 數學分解 Slide */
        .math-container {
            background: #f1f5f9;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 25px;
            font-size: 24px;
            border: 1px solid #cbd5e1;
        }

        .math-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }

        .math-card {
            background: #ffffff;
            border: 2px solid var(--navy-primary);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }

        .math-card.alt {
            border-color: #94a3b8;
        }

        .math-val {
            font-size: 48px;
            font-weight: 900;
            color: var(--navy-primary);
            margin-bottom: 8px;
        }

        .math-card.alt .math-val {
            color: #64748b;
        }

        .math-label {
            font-size: 20px;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 6px;
        }

        .math-desc {
            font-size: 15px;
            color: #64748b;
        }

        /* 表格 Slide */
        .slide-table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0 20px 0;
            font-size: 17px;
        }

        .slide-table th {
            background-color: var(--navy-primary);
            color: #ffffff;
            padding: 12px 16px;
            text-align: left;
            font-weight: 700;
        }

        .slide-table td {
            padding: 12px 16px;
            border-bottom: 1px solid #e2e8f0;
            color: #1e293b;
        }

        .slide-table tr:nth-child(even) {
            background-color: #f8fafc;
        }

        /* 結尾 Slide */
        .slide-conclusion {
            background: linear-gradient(135deg, #0b132b 0%, #1e3a8a 100%);
            color: #ffffff;
            justify-content: center;
            text-align: center;
            padding: 60px 80px;
        }

        .conclusion-quote {
            font-size: 30px;
            font-weight: 700;
            line-height: 1.6;
            color: #ffffff;
            margin-bottom: 30px;
            position: relative;
            padding: 0 40px;
        }

        .conclusion-takeaway {
            font-size: 22px;
            color: #93c5fd;
            max-width: 900px;
            margin: 0 auto;
            line-height: 1.6;
            background: rgba(255, 255, 255, 0.08);
            padding: 20px 30px;
            border-radius: 8px;
        }

        /* 導航控制欄 */
        .nav-controls {
            position: absolute;
            bottom: 12px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 35px;
            font-size: 14px;
            color: var(--text-muted);
            z-index: 100;
            pointer-events: none;
        }

        .nav-info {
            font-weight: 600;
        }

        .btn-controls {
            display: flex;
            gap: 10px;
            pointer-events: auto;
        }

        .btn {
            background: rgba(15, 23, 42, 0.08);
            border: 1px solid rgba(15, 23, 42, 0.15);
            padding: 6px 14px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-dark);
            transition: all 0.2s;
        }

        .btn:hover {
            background: var(--navy-primary);
            color: #ffffff;
        }

        .progress-bar-container {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: #e2e8f0;
            z-index: 100;
        }

        .progress-bar {
            height: 100%;
            background: var(--navy-primary);
            width: 0%;
            transition: width 0.2s ease;
        }
    </style>
</head>
<body>

<div id="deck-container">
'''

for idx, s in enumerate(slides_data):
    slide_no = idx + 1
    total_slides = len(slides_data)
    stype = s.get("type", "content")
    
    if stype == "cover":
        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide slide-cover {"active" if idx == 0 else ""}" id="slide-{slide_no}">
        <div class="badge">{s.get("badge", "")}</div>
        <h1>{s.get("title", "")}</h1>
        <h2>{s.get("subtitle", "")}</h2>
        <div class="logo-row">
            <img src="{b64_nycu}" alt="國立陽明交通大學">
            <img src="{b64_logo2}" alt="學院系所">
            <img src="{b64_image}" alt="專題研究室">
        </div>
        <div class="cover-meta">{s.get("author", "")}</div>
        <div class="cover-meta" style="color: #94a3b8; font-size: 14px; margin-top: 4px;">{s.get("scope", "")}</div>
    </div>
'''
    elif stype == "hook":
        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide slide-hook" id="slide-{slide_no}">
        <div class="hook-number">HOOK {s.get("number", "01")}・提問懸念</div>
        <div class="hook-question">{s.get("question", "")}</div>
        <div class="hook-box">
            <div class="hook-box-title">大眾普遍直覺：</div>
            <div class="hook-box-text">{s.get("intuition", "")}</div>
        </div>
        <div class="hook-reveal">💡 {s.get("reveal", "")}</div>
    </div>
'''
    elif stype == "math":
        math_cards_html = ""
        for m in s.get("decomposition", []):
            is_alt = "alt" if "少生" in m.get("label", "") else ""
            math_cards_html += f'''
            <div class="math-card {is_alt}">
                <div class="math-val">{m.get("value", "")}</div>
                <div class="math-label">{m.get("label", "")}</div>
                <div class="math-desc">{m.get("desc", "")}</div>
            </div>
'''
        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide" id="slide-{slide_no}">
        <div class="slide-header">
            <div class="slide-tag">{s.get("tag", "核心計量模型")}</div>
            <div class="slide-title">{s.get("title", "")}</div>
        </div>
        <div class="math-container">
            $${s.get("formula", "")}$$
        </div>
        <div class="math-grid">
            {math_cards_html}
        </div>
        <div class="card card-navy" style="margin-top: 5px; padding: 14px 20px;">
            <div class="card-text" style="font-weight: 600; font-size: 18px;">📌 核心結論：{s.get("summary", "")}</div>
        </div>
    </div>
'''
    elif stype == "table_slide":
        headers_html = "".join([f"<th>{h}</th>" for h in s["table"]["headers"]])
        rows_html = ""
        for row in s["table"]["rows"]:
            rows_html += "<tr>" + "".join([f"<td>{col}</td>" for col in row]) + "</tr>"
        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide" id="slide-{slide_no}">
        <div class="slide-header">
            <div class="slide-tag">{s.get("tag", "實證矩陣")}</div>
            <div class="slide-title">{s.get("title", "")}</div>
        </div>
        <div style="font-size: 16px; color: var(--navy-primary); font-weight: 600; margin-bottom: 8px;">{s.get("subtitle", "")}</div>
        <table class="slide-table">
            <thead>
                <tr>{headers_html}</tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        <div class="card card-navy" style="margin-top: 10px; padding: 14px 20px;">
            <div class="card-text" style="font-size: 17px; font-weight: 600;">📌 {s.get("summary", "")}</div>
        </div>
    </div>
'''
    elif stype == "conclusion":
        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide slide-conclusion" id="slide-{slide_no}">
        <div class="badge" style="background: rgba(255,255,255,0.15); color: #93c5fd; padding: 6px 18px; border-radius: 20px; font-size: 15px; margin-bottom: 25px;">總結與反思</div>
        <div class="conclusion-quote">{s.get("quote", "")}</div>
        <div class="conclusion-takeaway">{s.get("takeaway", "")}</div>
    </div>
'''
    elif stype == "closing":
        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide slide-cover" id="slide-{slide_no}">
        <h1 style="font-size: 48px; margin-bottom: 20px;">{s.get("title", "")}</h1>
        <div class="logo-row" style="margin: 30px 0;">
            <img src="{b64_nycu}" alt="國立陽明交通大學">
            <img src="{b64_logo2}" alt="學院系所">
            <img src="{b64_image}" alt="專題研究室">
        </div>
        <div class="cover-meta" style="font-size: 20px; font-weight: 700; color: #ffffff;">{s.get("team", "")}</div>
        <div class="cover-meta" style="font-size: 16px; color: #94a3b8; margin: 15px auto; max-width: 800px;">{s.get("database", "")}</div>
        <div class="badge" style="margin-top: 20px; background: rgba(59,130,246,0.25); color: #93c5fd; padding: 10px 24px; font-size: 18px;">{s.get("qa", "")}</div>
    </div>
'''
    else: # normal content
        cards_html = ""
        for c in s.get("cards", []):
            style = c.get("style", "navy")
            cards_html += f'''
        <div class="card card-{style}">
            <div class="card-title">{c.get("title", "")}</div>
            <div class="card-text">{c.get("text", "")}</div>
        </div>
'''
        bullets_html = ""
        if "bullets" in s:
            items = "".join([f"<li>{b}</li>" for b in s["bullets"]])
            bullets_html = f'<ul class="bullet-list">{items}</ul>'

        html_template += f'''
    <!-- Slide {slide_no} -->
    <div class="slide" id="slide-{slide_no}">
        <div class="slide-header">
            <div class="slide-tag">{s.get("tag", "研究實證")}</div>
            <div class="slide-title">{s.get("title", "")}</div>
        </div>
        {cards_html}
        {bullets_html}
    </div>
'''

html_template += f'''
    <!-- 導航控制與進度條 -->
    <div class="nav-controls">
        <div class="nav-info">
            <span id="slide-num">1</span> / <span id="total-slides">{len(slides_data)}</span>
        </div>
        <div class="btn-controls">
            <button class="btn" onclick="prevSlide()">◀ 上一頁 (Left)</button>
            <button class="btn" onclick="nextSlide()">下一頁 (Right) ▶</button>
            <button class="btn" onclick="toggleFullScreen()">全螢幕 (F)</button>
        </div>
    </div>
    <div class="progress-bar-container">
        <div class="progress-bar" id="progress-bar"></div>
    </div>
</div>

<script>
    let currentSlide = 1;
    const totalSlides = {len(slides_data)};

    function showSlide(n) {{
        if (n < 1) n = 1;
        if (n > totalSlides) n = totalSlides;
        
        document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
        const active = document.getElementById('slide-' + n);
        if (active) {{
            active.classList.add('active');
            currentSlide = n;
            document.getElementById('slide-num').innerText = n;
            const progress = ((n - 1) / (totalSlides - 1)) * 100;
            document.getElementById('progress-bar').style.width = progress + '%';
        }}
    }}

    function nextSlide() {{
        if (currentSlide < totalSlides) showSlide(currentSlide + 1);
    }}

    function prevSlide() {{
        if (currentSlide > 1) showSlide(currentSlide - 1);
    }}

    function toggleFullScreen() {{
        if (!document.fullscreenElement) {{
            document.documentElement.requestFullscreen().catch(err => {{}});
        }} else {{
            if (document.exitFullscreen) {{
                document.exitFullscreen();
            }}
        }}
    }}

    document.addEventListener('keydown', function(e) {{
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
            nextSlide();
        }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
            prevSlide();
        }} else if (e.key === 'Home') {{
            showSlide(1);
        }} else if (e.key === 'End') {{
            showSlide(totalSlides);
        }} else if (e.key === 'f' || e.key === 'F') {{
            toggleFullScreen();
        }}
    }});

    // 點擊投影片切換
    document.getElementById('deck-container').addEventListener('click', function(e) {{
        if (e.target.tagName !== 'BUTTON' && !e.target.closest('button')) {{
            const rect = this.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            if (clickX > rect.width * 0.7) {{
                nextSlide();
            }} else if (clickX < rect.width * 0.3) {{
                prevSlide();
            }}
        }}
    }});

    // 初始化
    showSlide(1);
</script>

</body>
</html>
'''

with open('wiki/slides/SL-FER-TaiwanFertilityDecline.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('SL-FER-TaiwanFertilityDecline.html created successfully!')
