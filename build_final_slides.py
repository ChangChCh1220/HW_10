import os
import base64

def get_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_nycu = get_b64('wiki/slides/assets/NYCU.png')
b64_logo2 = get_b64('wiki/slides/assets/logo2.png')
b64_image = get_b64('wiki/slides/assets/image.png')

html_content_raw = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>倒數第一的真相：到底是什麼影響了台灣的生育率？——從23篇實證論文看雙軌因果與突圍</title>
    <!-- KaTeX -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body);"></script>
    <style>
        :root {{
            --navy-dark: #070d1e;      /* 極深海軍藍底 */
            --navy-primary: #0f2b5c;   /* 經典海軍藍 */
            --navy-deep: #1e3a8a;      /* 寶藍色調 */
            --blue-accent: #2563eb;    /* 亮藍主調 */
            --blue-light: #eff6ff;     /* 淺藍底色 */
            --blue-glow: #60a5fa;      /* 霓虹藍光 */
            --text-main: #0f172a;      /* 深石板主文字 */
            --text-muted: #475569;     /* 次要說明灰 */
            --gold: #f59e0b;           /* 琥珀金點綴 */
            --gold-light: #fef3c7;
            --red-alert: #dc2626;      /* 警示紅 */
            --red-light: #fee2e2;
            --green-success: #16a34a;  /* 成功綠 */
            --green-light: #dcfce7;
            --card-border: #e2e8f0;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
            background-color: var(--navy-dark);
            color: var(--text-main);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            user-select: none;
        }}

        /* 16:9 主畫布容器 */
        #deck-container {{
            width: 95vw;
            max-width: 1440px;
            aspect-ratio: 16 / 9;
            background-color: #ffffff;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7);
            border-radius: 12px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        /* 投影片基礎樣式 */
        .slide {{
            width: 100%;
            height: 100%;
            padding: 40px 60px 45px 60px;
            display: none;
            flex-direction: column;
            justify-content: flex-start;
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            background-color: #ffffff;
            transition: opacity 0.35s ease-in-out;
        }}

        .slide.active {{
            display: flex;
            opacity: 1;
            z-index: 10;
        }}

        /* 母片 Header：三大去背 Logo 固定常駐右上角 */
        .master-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }}

        .slide-tag {{
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: var(--blue-accent);
            margin-bottom: 4px;
        }}

        .slide-headline {{
            font-size: 32px;
            font-weight: 900;
            color: var(--text-main);
            line-height: 1.25;
            letter-spacing: -0.5px;
        }}

        .master-logos {{
            display: flex;
            align-items: center;
            gap: 18px;
            background: rgba(255, 255, 255, 0.9);
            padding: 4px 12px;
            border-radius: 8px;
        }}

        .master-logos img {{
            height: 30px;
            object-fit: contain;
            filter: drop-shadow(0 1px 2px rgba(0,0,0,0.05));
        }}

        /* 頁面主體視覺區 (佔比 65%+) */
        .visual-stage {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            padding: 10px 0;
        }}

        /* 底部金句橫條 (Takeaway Footer Banner) */
        .takeaway-banner {{
            background: linear-gradient(90deg, #f8fafc 0%, #eff6ff 100%);
            border-left: 5px solid var(--blue-accent);
            padding: 12px 20px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 15px;
        }}

        .takeaway-text {{
            font-size: 18px;
            font-weight: 700;
            color: var(--navy-primary);
        }}

        .takeaway-source {{
            font-size: 13px;
            color: var(--text-muted);
            font-weight: 500;
        }}

        /* ================= 特殊頁面設計 ================= */

        /* 封面頁 Cover */
        .slide-cover {{
            background: linear-gradient(135deg, #070d1e 0%, #0f2b5c 50%, #1e3a8a 100%);
            color: #ffffff;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 50px 80px;
        }}

        .cover-badge {{
            display: inline-block;
            background: rgba(59, 130, 246, 0.2);
            border: 1px solid rgba(96, 165, 250, 0.4);
            color: #93c5fd;
            padding: 6px 18px;
            border-radius: 30px;
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 24px;
        }}

        .cover-title {{
            font-size: 44px;
            font-weight: 900;
            line-height: 1.25;
            color: #ffffff;
            margin-bottom: 16px;
            text-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}

        .cover-subtitle {{
            font-size: 22px;
            color: #cbd5e1;
            font-weight: 400;
            margin-bottom: 35px;
            max-width: 950px;
        }}

        .cover-logo-box {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            background: rgba(255, 255, 255, 0.98);
            padding: 16px 40px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            margin-bottom: 25px;
        }}

        .cover-logo-box img {{
            height: 50px;
            object-fit: contain;
        }}

        .cover-team {{
            font-size: 17px;
            font-weight: 600;
            color: #e2e8f0;
        }}

        /* 懸念提問頁 Hook */
        .slide-hook {{
            background: linear-gradient(135deg, #0b132b 0%, #1e3a8a 100%);
            color: #ffffff;
            justify-content: center;
            padding: 60px 80px;
        }}

        .hook-header {{
            font-size: 16px;
            font-weight: 800;
            color: var(--gold);
            letter-spacing: 2px;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}

        .hook-headline {{
            font-size: 38px;
            font-weight: 900;
            line-height: 1.35;
            color: #ffffff;
            margin-bottom: 35px;
        }}

        .hook-card-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            width: 100%;
        }}

        .hook-card {{
            padding: 24px;
            border-radius: 8px;
            font-size: 19px;
            line-height: 1.6;
        }}

        .hook-card-intuition {{
            background: rgba(255, 255, 255, 0.08);
            border-left: 5px solid #94a3b8;
            color: #e2e8f0;
        }}

        .hook-card-reveal {{
            background: rgba(37, 99, 235, 0.2);
            border-left: 5px solid var(--gold);
            color: #ffffff;
            font-weight: 700;
        }}

        /* ================= 核心動態圖表樣式 ================= */

        /* 1. 雙柱對比長條圖 (生長動態) */
        .chart-barchart {{
            width: 100%;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            height: 280px;
            border-bottom: 2px solid #cbd5e1;
            padding: 0 40px;
            margin-top: 15px;
        }}

        .bar-group {{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 180px;
        }}

        .bar-val {{
            font-size: 32px;
            font-weight: 900;
            margin-bottom: 8px;
            color: var(--navy-primary);
        }}

        .bar-pill {{
            width: 70px;
            background: linear-gradient(180deg, var(--blue-accent) 0%, var(--navy-primary) 100%);
            border-radius: 8px 8px 0 0;
            height: 0;
            transition: height 1s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}

        .bar-pill.alert {{
            background: linear-gradient(180deg, #f87171 0%, #dc2626 100%);
        }}

        .bar-pill.stable {{
            background: linear-gradient(180deg, #94a3b8 0%, #475569 100%);
        }}

        .slide.active .bar-pill.p64 {{ height: 210px; }}
        .slide.active .bar-pill.p22 {{ height: 75px; }}
        .slide.active .bar-pill.p50 {{ height: 165px; }}
        .slide.active .bar-pill.p12 {{ height: 40px; }}
        .slide.active .bar-pill.p82 {{ height: 240px; }}
        .slide.active .bar-pill.p18 {{ height: 55px; }}

        .bar-label {{
            margin-top: 10px;
            font-size: 16px;
            font-weight: 700;
            color: var(--text-main);
            text-align: center;
        }}

        /* 2. 橫向橫條進場圖 */
        .hbar-list {{
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 16px;
            padding: 10px 30px;
        }}

        .hbar-item {{
            display: flex;
            align-items: center;
            gap: 20px;
            font-size: 18px;
            font-weight: 700;
        }}

        .hbar-label {{
            width: 150px;
            text-align: right;
            color: var(--navy-primary);
        }}

        .hbar-track {{
            flex: 1;
            height: 34px;
            background: #f1f5f9;
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        }}

        .hbar-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--blue-accent) 0%, var(--navy-primary) 100%);
            width: 0%;
            transition: width 1s cubic-bezier(0.25, 1, 0.5, 1);
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 12px;
            color: #ffffff;
            font-weight: 800;
            font-size: 17px;
        }}

        .hbar-fill.highlight {{
            background: linear-gradient(90deg, #ef4444 0%, #b91c1c 100%);
        }}

        .slide.active .hbar-fill.w62 {{ width: 62.2%; }}
        .slide.active .hbar-fill.w55 {{ width: 55.2%; }}
        .slide.active .hbar-fill.w40 {{ width: 40.5%; }}
        .slide.active .hbar-fill.w03 {{ width: 3.8%; }}
        .slide.active .hbar-fill.w65 {{ width: 64.2%; }}
        .slide.active .hbar-fill.w48 {{ width: 47.5%; }}
        .slide.active .hbar-fill.w34 {{ width: 33.8%; }}
        .slide.active .hbar-fill.w55f {{ width: 55.3%; }}
        .slide.active .hbar-fill.w43m {{ width: 43.1%; }}
        .slide.active .hbar-fill.w75 {{ width: 75%; }}
        .slide.active .hbar-fill.w25 {{ width: 25%; }}

        /* 3. 公式動態點亮互動器 */
        .math-interactive-box {{
            width: 100%;
            background: #f8fafc;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            padding: 24px;
            text-align: center;
            margin-bottom: 20px;
        }}

        .formula-display {{
            font-size: 34px;
            margin-bottom: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            font-family: KaTeX_Math, serif;
        }}

        .formula-part {{
            padding: 6px 14px;
            border-radius: 6px;
            transition: all 0.3s ease;
            cursor: pointer;
            border: 2px solid transparent;
        }}

        .formula-part.lit-gold {{
            background: var(--gold-light);
            border-color: var(--gold);
            color: #b45309;
            box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
            transform: scale(1.06);
            font-weight: bold;
        }}

        .formula-part.lit-blue {{
            background: #e0f2fe;
            border-color: #0284c7;
            color: #0369a1;
            box-shadow: 0 0 15px rgba(2, 132, 199, 0.4);
            transform: scale(1.06);
            font-weight: bold;
        }}

        .formula-btn-row {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }}

        .formula-btn {{
            background: #ffffff;
            border: 2px solid #cbd5e1;
            padding: 8px 18px;
            border-radius: 6px;
            font-size: 15px;
            font-weight: 700;
            color: var(--text-main);
            cursor: pointer;
            transition: all 0.2s;
        }}

        .formula-btn:hover, .formula-btn.active {{
            background: var(--navy-primary);
            color: #ffffff;
            border-color: var(--navy-primary);
        }}

        .formula-explain-card {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 16px 24px;
            text-align: left;
            margin-top: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        /* 4. 天平傾斜圖 (Balance Scale) */
        .scale-box {{
            width: 100%;
            height: 250px;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .scale-beam {{
            width: 550px;
            height: 10px;
            background: var(--navy-primary);
            border-radius: 5px;
            position: relative;
            transform-origin: center center;
            transition: transform 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}

        .scale-fulcrum {{
            width: 0;
            height: 0;
            border-left: 30px solid transparent;
            border-right: 30px solid transparent;
            border-bottom: 60px solid var(--navy-dark);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, 0);
        }}

        .slide.active .scale-beam {{
            transform: rotate(-10deg);
        }}

        .scale-pan {{
            position: absolute;
            top: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .scale-pan.left {{ left: -20px; }}
        .scale-pan.right {{ right: -20px; }}

        .pan-plate {{
            background: #ffffff;
            border: 3px solid var(--blue-accent);
            padding: 14px 20px;
            border-radius: 8px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center;
            min-width: 170px;
        }}

        .pan-plate.heavy {{
            border-color: var(--red-alert);
        }}

        /* 5. 分流與冰山圖 */
        .branch-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            width: 100%;
            padding: 10px 20px;
        }}

        .branch-card {{
            border-radius: 8px;
            padding: 22px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}

        .branch-card.up {{
            background: var(--green-light);
            border: 2px solid var(--green-success);
        }}

        .branch-card.down {{
            background: var(--red-light);
            border: 2px solid var(--red-alert);
        }}

        .branch-title {{
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .branch-card.up .branch-title {{ color: var(--green-success); }}
        .branch-card.down .branch-title {{ color: var(--red-alert); }}

        .branch-desc {{
            font-size: 17px;
            line-height: 1.6;
            color: #1e293b;
        }}

        /* 6. 全景 Master Graph 樣式 */
        .master-graph-box {{
            width: 100%;
            background: #f8fafc;
            border: 2px solid #cbd5e1;
            border-radius: 10px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}

        .mg-track {{
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 12px 18px;
            border-radius: 8px;
            background: #ffffff;
            border: 2px solid #e2e8f0;
        }}

        .mg-track.t1 {{ border-left: 8px solid var(--blue-accent); }}
        .mg-track.t2 {{ border-left: 8px solid #a855f7; }}

        .mg-badge {{
            font-size: 14px;
            font-weight: 800;
            padding: 6px 12px;
            border-radius: 6px;
            color: #ffffff;
            white-space: nowrap;
        }}

        .mg-track.t1 .mg-badge {{ background: var(--blue-accent); }}
        .mg-track.t2 .mg-badge {{ background: #a855f7; }}

        .mg-chain {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex: 1;
            font-size: 16px;
            font-weight: 700;
            color: #1e293b;
        }}

        .mg-chain span.node {{
            background: #f1f5f9;
            padding: 6px 12px;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
        }}

        .mg-arrow {{
            color: var(--blue-accent);
            font-weight: 900;
        }}

        .mg-final-bar {{
            background: linear-gradient(90deg, #0f172a 0%, #dc2626 100%);
            color: #ffffff;
            padding: 14px 20px;
            border-radius: 8px;
            text-align: center;
            font-size: 20px;
            font-weight: 800;
            box-shadow: 0 4px 15px rgba(220, 38, 38, 0.25);
        }}

        /* 導航控制欄 */
        .deck-footer {{
            position: absolute;
            bottom: 10px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            font-size: 13px;
            color: var(--text-muted);
            z-index: 100;
            pointer-events: none;
        }}

        .deck-btn-group {{
            display: flex;
            gap: 10px;
            pointer-events: auto;
        }}

        .ctrl-btn {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 5px 14px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            font-weight: 700;
            color: var(--text-main);
            transition: all 0.2s;
        }}

        .ctrl-btn:hover {{
            background: var(--navy-primary);
            color: #ffffff;
        }}

        .progress-bar-wrap {{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: #e2e8f0;
            z-index: 100;
        }}

        .progress-bar-fill {{
            height: 100%;
            background: var(--blue-accent);
            width: 0%;
            transition: width 0.25s ease;
        }}
    </style>
</head>
<body>

<div id="deck-container">

    <!-- Slide 1: Cover (Brand Cover) -->
    <div class="slide slide-cover active" id="slide-1">
        <div class="cover-badge">科普學術演講・當代人口學實證分析</div>
        <h1 class="cover-title">倒數第一的真相：到底是什麼影響了台灣的生育率？</h1>
        <h2 class="cover-subtitle">從 23 篇國內外實證論文看「結不了婚」與「不敢生二胎」的雙軌困局與解方</h2>
        
        <div class="cover-logo-box">
            <img src="###NYCU###" alt="國立陽明交通大學">
            <img src="###LOGO2###" alt="學院系所">
            <img src="###IMAGE###" alt="專題實驗室">
        </div>

        <div class="cover-team">國立陽明交通大學 專題研究團隊</div>
        <div style="font-size: 14px; color: #94a3b8; margin-top: 6px;">以微觀追蹤資料（PSFD、TYP、社會變遷調查）與計量因果模型為實證基石</div>
    </div>

    <!-- Slide 2: Hook 1 (數字對決) -->
    <div class="slide slide-hook" id="slide-2">
        <div class="hook-header">HOOK 01・直擊矛盾</div>
        <div class="hook-headline">政府年年狂砸千億補貼，為什麼台灣生育率依舊跌到全球墊底？</div>
        <div class="hook-card-grid">
            <div class="hook-card hook-card-intuition">
                <div style="font-size: 15px; font-weight: 800; color: #94a3b8; margin-bottom: 8px;">大眾常見直覺：</div>
                「現在年輕人愛享受、自私不想承擔家庭責任？發錢補貼、送禮物育兒，大家就會生了？」
            </div>
            <div class="hook-card hook-card-reveal">
                <div style="font-size: 15px; font-weight: 800; color: var(--gold); margin-bottom: 8px;">硬核數據真相：</div>
                2024 年全台少子化預算突破 <b>1,100 億元</b>，總和生育率卻一路墜崖至 <b>0.865</b>！<br>
                <b>病因診斷錯誤，再多的補貼也只是向大海撒錢！</b>
            </div>
        </div>
    </div>

    <!-- Slide 3: 數據直擊 (雙柱長條圖生長動態) -->
    <div class="slide" id="slide-3">
        <div class="master-header">
            <div>
                <div class="slide-tag">人口統計真相・數據說話</div>
                <div class="slide-headline">已婚夫妻依然在生，崩盤的其實是「結婚率」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="chart-barchart">
                <div class="bar-group">
                    <div class="bar-val">22.7%</div>
                    <div class="bar-pill p22"></div>
                    <div class="bar-label">1990 年<br>30-34歲男性未婚率</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val" style="color: var(--red-alert);">64.3%</div>
                    <div class="bar-pill alert p64"></div>
                    <div class="bar-label" style="color: var(--red-alert);">2020 年<br>30-34歲男性未婚率</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val">1.62 個</div>
                    <div class="bar-pill stable p50"></div>
                    <div class="bar-label">2000 年<br>有偶婦女生育數</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val">1.58 個</div>
                    <div class="bar-pill stable p50"></div>
                    <div class="bar-label">2020 年<br>有偶婦女生育數</div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：已婚夫妻平均仍生育 1.6 個孩子，少子化的真兇是「青年被大規模阻絕於婚姻之外」！</div>
            <div class="takeaway-source">數據來源：內政部戶籍統計資料與人口普查報告</div>
        </div>
    </div>

    <!-- Slide 4: 核心數學 (公式互動變色點亮器) -->
    <div class="slide" id="slide-4">
        <div class="master-header">
            <div>
                <div class="slide-tag">人口學因果分解・核心公式</div>
                <div class="slide-headline">Kitagawa 分解法揭秘：82% 的少子化是由「不婚」貢獻的！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="math-interactive-box">
                <div class="formula-display">
                    $$\Delta TFR = $$
                    <span class="formula-part lit-gold" id="part-m" onclick="highlightFormula('m')">\sum \Delta M_a \cdot \bar{F}_a</span>
                    $$ + $$
                    <span class="formula-part" id="part-f" onclick="highlightFormula('f')">\sum \bar{M}_a \cdot \Delta F_a</span>
                </div>
                <div class="formula-btn-row">
                    <button class="formula-btn active" id="btn-m" onclick="highlightFormula('m')">步驟 1：檢視「未婚率上升效應」</button>
                    <button class="formula-btn" id="btn-f" onclick="highlightFormula('f')">步驟 2：檢視「婚內少生效應」</button>
                    <button class="formula-btn" onclick="highlightFormula('all')">還原完整公式</button>
                </div>
                <div class="formula-explain-card" id="formula-desc">
                    <div>
                        <div style="font-size: 20px; font-weight: 800; color: #b45309;" id="desc-title">婚姻結構變動效應 (ΔM_a)：貢獻度高達 82%！</div>
                        <div style="font-size: 16px; color: #475569; margin-top: 4px;" id="desc-text">實證分解指出：每下降 1 點生育率，超過八成來自「大家結不了婚或延後初婚」！</div>
                    </div>
                    <div style="font-size: 38px; font-weight: 900; color: #b45309;" id="desc-val">82%</div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：少子化的真正本質是「不婚化」！忽視成家門檻的任何催生政策，都是隔靴搔癢。</div>
            <div class="takeaway-source">計量方法：Kitagawa 人口因果分解法</div>
        </div>
    </div>

    <!-- Slide 5: 東亞制度枷鎖 (跨國非婚生育對比) -->
    <div class="slide" id="slide-5">
        <div class="master-header">
            <div>
                <div class="slide-tag">跨國制度對照・婚育包裹</div>
                <div class="slide-headline">台灣制度死穴：在台灣，不結婚就是「完全不准生」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="hbar-list">
                <div class="hbar-item">
                    <div class="hbar-label">法國 (France)</div>
                    <div class="hbar-track"><div class="hbar-fill w62">62.2%</div></div>
                </div>
                <div class="hbar-item">
                    <div class="hbar-label">瑞典 (Sweden)</div>
                    <div class="hbar-track"><div class="hbar-fill w55">55.2%</div></div>
                </div>
                <div class="hbar-item">
                    <div class="hbar-label">美國 (USA)</div>
                    <div class="hbar-track"><div class="hbar-fill w40">40.5%</div></div>
                </div>
                <div class="hbar-item">
                    <div class="hbar-label" style="color: var(--red-alert);">台灣 (Taiwan)</div>
                    <div class="hbar-track"><div class="hbar-fill highlight w03">3.8%</div></div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：歐美同居生子享有完整法律與托育平權；但在台灣，婚姻是生育的唯一合法特許證！</div>
            <div class="takeaway-source">數據出處：OECD 人口統計與中央研究院社會學研究所調查</div>
        </div>
    </div>

    <!-- Slide 6: Hook 2 (青年意願) -->
    <div class="slide slide-hook" id="slide-6">
        <div class="hook-header">HOOK 02・破除刻板印象</div>
        <div class="hook-headline">長輩常嘆「現代年輕人崇尚單身、自私不想成家」，真的嗎？</div>
        <div class="hook-card-grid">
            <div class="hook-card hook-card-intuition">
                <div style="font-size: 15px; font-weight: 800; color: #94a3b8; margin-bottom: 8px;">社會刻板指責：</div>
                「現在年輕人只想吃喝玩樂、愛自由、討厭家庭束縛，把婚姻當作洪水猛獸？」
            </div>
            <div class="hook-card hook-card-reveal">
                <div style="font-size: 15px; font-weight: 800; color: var(--gold); margin-bottom: 8px;">全國問卷實證：</div>
                30 歲以前的未婚男女中，有超過 <b>85%</b> 明確表示「未來希望走入婚姻」！<br>
                <b>年輕人不是不想結，而是面臨極度嚴峻的現實障礙！</b>
            </div>
        </div>
    </div>

    <!-- Slide 7: 想婚卻結不了 (原因排行橫條圖) -->
    <div class="slide" id="slide-7">
        <div class="master-header">
            <div>
                <div class="slide-tag">軌道一：成家障礙・微觀調查</div>
                <div class="slide-headline">未婚青年不是拒絕婚姻，而是選擇「寧缺勿濫」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="hbar-list">
                <div class="hbar-item">
                    <div class="hbar-label">尚未遇到合適對象</div>
                    <div class="hbar-track"><div class="hbar-fill w65">64.2%（重視心靈契合與價值觀）</div></div>
                </div>
                <div class="hbar-item">
                    <div class="hbar-label">經濟基礎尚未就緒</div>
                    <div class="hbar-track"><div class="hbar-fill w48">47.5%（自認低薪、買不起房）</div></div>
                </div>
                <div class="hbar-item">
                    <div class="hbar-label">恐懼婚後生活品質降低</div>
                    <div class="hbar-track"><div class="hbar-fill w34">33.8%（長輩爭吵與離婚陰影）</div></div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：面對高昂的生活成本，現代青年對婚姻慎重以對，沒有把握寧可維持單身，拒絕湊合！</div>
            <div class="takeaway-source">實證來源：臺灣華人家庭動態調查（PSFD）1,714 位未婚樣本</div>
        </div>
    </div>

    <!-- Slide 8: 婚姻特許考 (性別動態天平) -->
    <div class="slide" id="slide-8">
        <div class="master-header">
            <div>
                <div class="slide-tag">軌道一：成家門檻・物質防衛</div>
                <div class="slide-headline">成家先買房：逾半數女性堅持「有房才結婚」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="scale-box">
                <div class="scale-beam">
                    <div class="scale-pan left">
                        <div class="pan-plate heavy">
                            <div style="font-size: 15px; font-weight: 700; color: #dc2626;">女性受訪者</div>
                            <div style="font-size: 32px; font-weight: 900; color: #dc2626;">55.3%</div>
                            <div style="font-size: 13px; color: #475569;">堅持婚前必須買房</div>
                        </div>
                    </div>
                    <div class="scale-pan right">
                        <div class="pan-plate">
                            <div style="font-size: 15px; font-weight: 700; color: var(--navy-primary);">男性受訪者</div>
                            <div style="font-size: 32px; font-weight: 900; color: var(--navy-primary);">43.1%</div>
                            <div style="font-size: 13px; color: #475569;">認為租屋亦可成家</div>
                        </div>
                    </div>
                </div>
                <div class="scale-fulcrum"></div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：女性預期婚後承擔母職與家務風險，要求男方備房作為「制度防衛補償」，高房價成了婚姻特許考！</div>
            <div class="takeaway-source">實證文獻：《人文及社會科學集刊》未婚男女買房態度調查</div>
        </div>
    </div>

    <!-- Slide 9: 婚姻斜坡 (Logit 估計係數對抗圖) -->
    <div class="slide" id="slide-9">
        <div class="master-header">
            <div>
                <div class="slide-tag">軌道一：婚配結構・性別不對稱</div>
                <div class="slide-headline">殘酷的婚姻斜坡：薪水越高，男人越好結、女人越難嫁！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card up">
                    <div class="branch-title">♂️ 男性結婚機率：隨經濟增長直線上升</div>
                    <div class="branch-desc">
                        • <b>每月薪資每上升 1 萬元</b> ➜ 結婚勝算顯著提升 <b>+18%</b>！<br>
                        • <b>每週工時加班增加</b> ➜ 被視為事業有成，結婚機率顯著增加！<br>
                        • 社會傳統依舊將男性綁定為「養家經濟主力」。
                    </div>
                </div>
                <div class="branch-card down">
                    <div class="branch-title">♀️ 女性結婚機率：隨經濟自主反而下降</div>
                    <div class="branch-desc">
                        • <b>每月薪資每上升 1 萬元</b> ➜ 結婚機率逆向暴跌 <b>-14%</b>！<br>
                        • <b>女性以自身經濟為「參考點門檻」</b>，堅決拒絕下嫁！<br>
                        • 傳統「男高女低」觀念未變，高社經女性與中低薪男性雙雙被擠壓。
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：女性經濟獨立了，婚配文化卻停留在舊時代，導致現代婚姻市場嚴重配對失靈！</div>
            <div class="takeaway-source">計量實證：清華大學經濟學研究所 PSFD 追蹤資料 Logit 模型分析</div>
        </div>
    </div>

    <!-- Slide 10: 同居假象 (趨勢斷裂折線) -->
    <div class="slide" id="slide-10">
        <div class="master-header">
            <div>
                <div class="slide-tag">軌道一：親密關係・同居現狀</div>
                <div class="slide-headline">同居暴增 4 倍但生育為零：台灣同居只是「合租單身」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card down">
                    <div class="branch-title">📈 同居普及率暴衝</div>
                    <div class="branch-desc">
                        • 台灣青年同居率由 10% 狂飆至 <b>近 40%</b>。<br>
                        • 年輕世代普遍接受婚前共同生活。
                    </div>
                </div>
                <div class="branch-card down">
                    <div class="branch-title">📉 想婚與生育率崩跌</div>
                    <div class="branch-desc">
                        • 同居者中有結婚計畫者自 70% 驟降至 <b>僅剩 30%</b>！<br>
                        • 台灣同居生育比例長年低於 <b>3%</b>（完全不生）。
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：缺乏法制與托育保障，台灣的同居只是單身生活的延長，完全無法如歐洲般轉化為新生兒！</div>
            <div class="takeaway-source">權威研究：美國婚姻與家庭期刊（Journal of Marriage and Family, 2023）</div>
        </div>
    </div>

    <!-- Slide 11: Hook 3 (房價爭議) -->
    <div class="slide slide-hook" id="slide-11">
        <div class="hook-header">HOOK 03・學術爭議辨析</div>
        <div class="hook-headline">「高房價是最好的避孕藥」人人皆知……<br>為什麼有些學者卻發現：<b>「房價越漲，生育率反而上升」</b>？</div>
        <div class="hook-card-grid">
            <div class="hook-card hook-card-intuition">
                <div style="font-size: 15px; font-weight: 800; color: #94a3b8; margin-bottom: 8px;">學界爭議焦點：</div>
                「難道是經濟學者做研究與現實脫節？還是房價其實對生小孩沒有負面影響？」
            </div>
            <div class="hook-card hook-card-reveal">
                <div style="font-size: 15px; font-weight: 800; color: var(--gold); margin-bottom: 8px;">微觀因果真相：</div>
                房價是一把無情的雙面刃！它對<b>「已擁房家庭」</b>與<b>「無房青年」</b>的因果作用徹底相反！
            </div>
        </div>
    </div>

    <!-- Slide 12: 爭議辨析一：財富 vs 負擔 (Y字型分流圖) -->
    <div class="slide" id="slide-12">
        <div class="master-header">
            <div>
                <div class="slide-tag">爭議辨析一・因果機制拆解</div>
                <div class="slide-headline">房價是雙面刃：它讓有房族更富，卻把無房青年徹底掏空！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card up">
                    <div class="branch-title">🏠 已購屋擁房族 ➜ 財富效果 (+)</div>
                    <div class="branch-desc">
                        • 房價大漲 ➜ 房屋淨資產暴增、低利轉貸融資容易。<br>
                        • 家庭財務安全感倍增，促使其提早生育第二胎！<br>
                        • <b>實證效應：對擁房者呈現微幅正向拉動</b>。
                    </div>
                </div>
                <div class="branch-card down">
                    <div class="branch-title">🚫 無房青年租屋族 ➜ 排擠效應 (-)</div>
                    <div class="branch-desc">
                        • 房價飛天 ➜ 首付儲蓄期從 5 年暴拉至 15 年以上。<br>
                        • 高房租與高房貸極限掏空青年所得，直接放棄成家！<br>
                        • <b>實證效應：對無房者造成毀滅性生育打擊</b>。
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：房價上漲實質拉大了資產階級與無產青年之間的「階級生育不平等」！</div>
            <div class="takeaway-source">實證文獻：台灣縣市面板資料分析 & 韓國住房資產實證研究</div>
        </div>
    </div>

    <!-- Slide 13: 爭議辨析二：房價箭靶是婚姻 (彈性重擊長條圖) -->
    <div class="slide" id="slide-13">
        <div class="master-header">
            <div>
                <div class="slide-tag">爭議辨析二・因果衝擊彈性</div>
                <div class="slide-headline">實證彈性揭秘：房價沒有阻止已婚者生，而是摧毀了初婚！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="chart-barchart">
                <div class="bar-group">
                    <div class="bar-val" style="color: #475569;">-1.5%</div>
                    <div class="bar-pill stable p18"></div>
                    <div class="bar-label">已婚婦女生育率<br>受房價衝擊彈性</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val" style="color: var(--red-alert);">-7.2%</div>
                    <div class="bar-pill alert p82"></div>
                    <div class="bar-label" style="color: var(--red-alert);">未婚青年初婚機率<br>受房價衝擊彈性</div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：已婚夫妻具備親職韌性，房價衝擊溫和；高房價的致命死穴是「直接關閉了青年的婚姻大門」！</div>
            <div class="takeaway-source">計量實證：台灣住宅負擔能力與空間擴散計量模型</div>
        </div>
    </div>

    <!-- Slide 14: Hook 4 (津貼質疑) -->
    <div class="slide slide-hook" id="slide-14">
        <div class="hook-header">HOOK 04・政策成效質疑</div>
        <div class="hook-headline">各縣市狂砸真金白銀加碼生育津貼，真的催生出了小孩嗎？</div>
        <div class="hook-card-grid">
            <div class="hook-card hook-card-intuition">
                <div style="font-size: 15px; font-weight: 800; color: #94a3b8; margin-bottom: 8px;">地方政客最愛政績：</div>
                「台北發 2 萬、桃園給 3 萬、花蓮開 5 萬！只要發錢夠大方，年輕人就會樂意增產報國？」
            </div>
            <div class="hook-card hook-card-reveal">
                <div style="font-size: 15px; font-weight: 800; color: var(--gold); margin-bottom: 8px;">因果計量模型檢驗：</div>
                雙重差分法（DID）與合成控制法（SCM）揭露驚人事實：<br>
                <b>地方生育津貼對全國總出生數的淨貢獻值，實質等於零！</b>
            </div>
        </div>
    </div>

    <!-- Slide 15: 爭議辨析三：幽靈遷徙 (DID 空間地圖) -->
    <div class="slide" id="slide-15">
        <div class="master-header">
            <div>
                <div class="slide-tag">爭議辨析三・因果評估 DID</div>
                <div class="slide-headline">因果計量戳破謊言：生育津貼沒多生一個小孩，只造成「戶籍大風吹」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card down">
                    <div class="branch-title">👻 跨區幽靈戶籍遷徙（Migration Bias）</div>
                    <div class="branch-desc">
                        • 某縣市加碼補助 ➜ 鄰近縣市夫妻短期「遷戶籍領錢」。<br>
                        • 該縣市出生數看似微升，鄰縣同步暴跌 ➜ <b>全國總量淨增為 0</b>！
                    </div>
                </div>
                <div class="branch-card down">
                    <div class="branch-title">⏳ 生育時程微幅提早（Timing Effect）</div>
                    <div class="branch-desc">
                        • 僅促使本來就打算生小孩的家庭「提早幾個月受孕」。<br>
                        • 完全沒有增加婦女一生中的「終身總生育胎數」！
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：地方現金津貼淪為毫無意義的跨區搶人零和賽局，白白虛耗數十億國家財政！</div>
            <div class="takeaway-source">因果推論：台灣各縣市生育津貼雙重差分法（DID）與合成控制法（SCM）評估</div>
        </div>
    </div>

    <!-- Slide 16: 津貼陷阱 (撫養成本冰山圖) -->
    <div class="slide" id="slide-16">
        <div class="master-header">
            <div>
                <div class="slide-tag">政策工具比較・成本結構</div>
                <div class="slide-headline">幾萬元津貼如杯水車薪：平價公共托育才是真正的定心丸！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card down">
                    <div class="branch-title">🧊 水面上的微小冰山：一次性津貼</div>
                    <div class="branch-desc">
                        • 補助 3～5 萬元，佔撫養至成年的 800 萬開銷<b>不到 1%</b>！<br>
                        • 生育率拉動彈性係數接近於零，發完即無效。
                    </div>
                </div>
                <div class="branch-card up">
                    <div class="branch-title">🏔️ 水面下的龐大冰山：托育公共化</div>
                    <div class="branch-desc">
                        • 0-6 歲公托與準公幼，每月實質為雙薪家庭減負 1.5～2 萬元！<br>
                        • <b>國際文獻證實：托育服務擴充彈性是一次性現金的 6 至 8 倍！</b>
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：生小孩不是一瞬間，而是 18 年的承諾；唯有長期平價公共托育，才能解放雙薪父母！</div>
            <div class="takeaway-source">理論支持：新時代生育經濟學（Doepke et al., 2022）</div>
        </div>
    </div>

    <!-- Slide 17: Hook 5 (已婚媽媽不敢生二胎) -->
    <div class="slide slide-hook" id="slide-17">
        <div class="hook-header">HOOK 05・軌道二：後端婚內困局</div>
        <div class="hook-headline">走進了婚姻的媽媽，為什麼生了一個就嚇到「不敢生第二胎」？</div>
        <div class="hook-card-grid">
            <div class="hook-card hook-card-intuition">
                <div style="font-size: 15px; font-weight: 800; color: #94a3b8; margin-bottom: 8px;">傳統社會期待：</div>
                「既然都結了婚、生了一胎，順理成章再生第二個作伴，有何困難？」
            </div>
            <div class="hook-card hook-card-reveal">
                <div style="font-size: 15px; font-weight: 800; color: var(--gold); margin-bottom: 8px;">已婚母親的真實痛點：</div>
                步入婚姻的家庭生第一胎比例高達 80%，但生第二胎驟降至 <b>不到 35%</b>！<br>
                <b>是什麼力量讓婚內媽媽在生完第一胎後，緊急踩下煞車？</b>
            </div>
        </div>
    </div>

    <!-- Slide 18: 爭議辨析四：家務 3.2 倍差距 (雙重輪班柱狀圖) -->
    <div class="slide" id="slide-18">
        <div class="master-header">
            <div>
                <div class="slide-tag">爭議辨析四・制度性不協調</div>
                <div class="slide-headline">白天拼業績，晚上做家務：已婚女性的「雙重輪班」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="chart-barchart">
                <div class="bar-group">
                    <div class="bar-val" style="color: var(--red-alert);">3.8 小時</div>
                    <div class="bar-pill alert p82"></div>
                    <div class="bar-label" style="color: var(--red-alert);">已婚女性每日家務育兒時間<br>承擔全家 75% 無償勞動</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val" style="color: #475569;">1.1 小時</div>
                    <div class="bar-pill stable p22"></div>
                    <div class="bar-label">已婚男性每日家務育兒時間<br>差距高達 3.2 倍！</div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：職場講求高工時績效，家庭內部女性卻全包家務；當婚姻意味著勞動加倍，女性的理性防衛就是不生二胎！</div>
            <div class="takeaway-source">數據來源：行政院性平處性別統計資料 & 台灣家務分工與生育意願研究</div>
        </div>
    </div>

    <!-- Slide 19: 姻親文化焦慮 (性別心聲對照) -->
    <div class="slide" id="slide-19">
        <div class="master-header">
            <div>
                <div class="slide-tag">軌道二：家庭文化・質性深入訪談</div>
                <div class="slide-headline">零位男性擔心姻親，女性卻視為夢魘：傳統文化成了推力！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card up">
                    <div class="branch-title">👨 受訪男性：0 人擔憂姻親</div>
                    <div class="branch-desc">
                        • 婚後生活以男方家庭為中心，幾乎感受不到生活秩序的變動。<br>
                        • 很少需要適應女方親戚生活習慣，毫無婚姻外推力。
                    </div>
                </div>
                <div class="branch-card down">
                    <div class="branch-title">👩 受訪女性：普遍深感焦慮</div>
                    <div class="branch-desc">
                        • 從父居摩擦、過年過節儀式義務、婆家規訓。<br>
                        • 「看著母親當全職家庭主婦受盡委屈看臉色，我何必跳入火坑重複一樣的人生？」
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：女性經濟獨立後，有能力對不平等的傳統家庭制度說不；私領域文化停滯正在將女性推離家庭！</div>
            <div class="takeaway-source">質性研究：臺灣適婚年齡者進入婚姻與否的考量因素《人口學刊》</div>
        </div>
    </div>

    <!-- Slide 20: Hook 6 (單身社會樣態) -->
    <div class="slide slide-hook" id="slide-20">
        <div class="hook-header">HOOK 06・打破單身標籤</div>
        <div class="hook-headline">不結婚的單身世代，老了真的像社會說的那樣孤苦淒涼嗎？</div>
        <div class="hook-card-grid">
            <div class="hook-card hook-card-intuition">
                <div style="font-size: 15px; font-weight: 800; color: #94a3b8; margin-bottom: 8px;">社會污名標籤：</div>
                「單身就是敗犬、羅漢腳、魯蛇，老了沒人理、成為社會家庭負擔？」
            </div>
            <div class="hook-card hook-card-reveal">
                <div style="font-size: 15px; font-weight: 800; color: var(--gold); margin-bottom: 8px;">全國抽樣調查揭曉：</div>
                40-59 歲始終單身女性高達 <b>70.8% 為白領階層</b>，月收入與社交活躍度全面超越已婚女性！<br>
                <b>打破刻板印象：單身早已成為一種具備自主性的現代生活選擇！</b>
            </div>
        </div>
    </div>

    <!-- Slide 21: 破除刻板印象 (單身社經對比圖) -->
    <div class="slide" id="slide-21">
        <div class="master-header">
            <div>
                <div class="slide-tag">單身社會學・生活樣態</div>
                <div class="slide-headline">單身女性活出高自主性，但單身男性面臨結構性邊緣化！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card up">
                    <div class="branch-title">👩 中年中產單身女性：高社經與高連結</div>
                    <div class="branch-desc">
                        • <b>70.8% 為白領階層</b>，平均月收入顯著高於曾婚女性！<br>
                        • 每日上網 4.5 小時、朋友聚餐最頻繁（已婚女性走入家庭後社交圈暴跌至 22%）。
                    </div>
                </div>
                <div class="branch-card down">
                    <div class="branch-title">👨 中年單身男性：結構性風險攀升</div>
                    <div class="branch-desc">
                        • <b>無工作者比例達 22.6%</b>，收入低於曾婚男性。<br>
                        • 社交網絡極度狹窄，過度依賴原生家庭，退休後易陷入社會孤立。
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：婚姻反而限縮了女性生活圈；但單身男性的就業與社會疏離，是未來急需關注的隱形危機。</div>
            <div class="takeaway-source">實證文獻：中年單身者的個人特徵、家庭關係與社會參與《人口學刊》</div>
        </div>
    </div>

    <!-- Slide 22: 單身長照新負擔 (代間長照圖) -->
    <div class="slide" id="slide-22">
        <div class="master-header">
            <div>
                <div class="slide-tag">代間關係・隱形負擔</div>
                <div class="slide-headline">沒成家的代價：近半數單身者同住長輩，默默扛下全家長照！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="chart-barchart">
                <div class="bar-group">
                    <div class="bar-val" style="color: var(--blue-accent);">48.5%</div>
                    <div class="bar-pill p50"></div>
                    <div class="bar-label">40-59歲單身男性<br>與高齡父母同住</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val" style="color: #a855f7;">45.4%</div>
                    <div class="bar-pill stable p50"></div>
                    <div class="bar-label">40-59歲單身女性<br>與高齡父母同住</div>
                </div>
                <div class="bar-group">
                    <div class="bar-val" style="color: var(--red-alert);">71.1%</div>
                    <div class="bar-pill alert p82"></div>
                    <div class="bar-label" style="color: var(--red-alert);">單身女性向父母提供<br>日常生活與失能照顧</div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：「反正你沒家室，長輩由你照顧」——未婚青年逃離了育兒，卻在中年提前被吸入長照泥淖！</div>
            <div class="takeaway-source">資料來源：臺灣社會變遷基本調查與人口住宅普查</div>
        </div>
    </div>

    <!-- Slide 23: Master Causal Graph (全景大圖) -->
    <div class="slide" id="slide-23">
        <div class="master-header">
            <div>
                <div class="slide-tag">終極因果網絡・全景大圖</div>
                <div class="slide-headline">台灣低生育率立體因果圖：雙軌扣殺下的理性抵抗！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="master-graph-box">
                <div class="mg-track t1">
                    <div class="mg-badge">軌道一：前端成家鎖死 (82%)</div>
                    <div class="mg-chain">
                        <span class="node">高房價與買房剛需</span>
                        <span class="mg-arrow">➔</span>
                        <span class="node">婚姻斜坡配對失靈</span>
                        <span class="mg-arrow">➔</span>
                        <span class="node" style="color: #dc2626;">未婚率暴飆至 64%</span>
                        <span class="mg-arrow">➔</span>
                        <span class="node">婚育包裹 (非婚僅3.8%)</span>
                    </div>
                </div>
                <div class="mg-track t2">
                    <div class="mg-badge">軌道二：後端家庭撕裂 (18%)</div>
                    <div class="mg-chain">
                        <span class="node">高壓超長工時</span>
                        <span class="mg-arrow">➔</span>
                        <span class="node">私領域家務全包 (3.2倍)</span>
                        <span class="mg-arrow">➔</span>
                        <span class="node" style="color: #dc2626;">雙重輪班母職懲罰</span>
                        <span class="mg-arrow">➔</span>
                        <span class="node">已婚媽媽不敢生二胎</span>
                    </div>
                </div>
                <div class="mg-final-bar">
                    💥 雙軌連環扣殺 ➔ 台灣總和生育率跌破 0.865（全球倒數第一的真正因果！）
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：少子化是青年面對殘酷生存壓力與不平等家庭體制時，所做出的最沉重、最理性的非暴力抵抗！</div>
            <div class="takeaway-source">本簡報 23 篇實證文獻因果統合模型</div>
        </div>
    </div>

    <!-- Slide 24: 政策突圍一 (三支箭) -->
    <div class="slide" id="slide-24">
        <div class="master-header">
            <div>
                <div class="slide-tag">政策典範轉移・結構突圍</div>
                <div class="slide-headline">停止發錢催生！千億預算全面轉向「拆除成家障礙」！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card up">
                    <div class="branch-title">🏹 第一支箭：新婚青年社宅長租保障</div>
                    <div class="branch-desc">
                        • 提供 5-10 年平價社宅長租保障，打破「買得起房才配結婚」的致命魔咒！<br>
                        • 將居住正義直接對接成家關鍵期。
                    </div>
                </div>
                <div class="branch-card up">
                    <div class="branch-title">🏹 第二支箭：0-6 歲托育全面公共化</div>
                    <div class="branch-desc">
                        • 停止發放無效的一次性幾萬元津貼，全面投入公托與準公幼。<br>
                        • 實質減輕父母長達 18 年的經濟與托育機會成本。
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：唯有國家主動分擔居住與育兒的長期成本，年輕人才有勇氣走入婚姻！</div>
            <div class="takeaway-source">政策建議：公共經濟學與家庭福利典範轉移</div>
        </div>
    </div>

    <!-- Slide 25: 政策突圍二 (制度鬆綁) -->
    <div class="slide" id="slide-25">
        <div class="master-header">
            <div>
                <div class="slide-tag">制度創新・包容性社會</div>
                <div class="slide-headline">讓生育不再被單一婚姻綁架：鬆綁婚育包裹，邁向多元！</div>
            </div>
            <div class="master-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="visual-stage">
            <div class="branch-grid">
                <div class="branch-card up">
                    <div class="branch-title">⚖️ 鬆綁《人工生殖法》</div>
                    <div class="branch-desc">
                        • 開放單身女性與未婚伴侶合法使用生殖醫學技術，還原自主生殖權利！<br>
                        • 讓具備撫養意願與經濟能力的個體不再受限於一紙婚約。
                    </div>
                </div>
                <div class="branch-card up">
                    <div class="branch-title">👶 非婚生子女與多元伴侶平權</div>
                    <div class="branch-desc">
                        • 消除福利、稅務與戶政登記上對非婚生子女的隱形歧視。<br>
                        • 法律承認穩定同居伴侶之撫養與家庭照顧權益。
                    </div>
                </div>
            </div>
        </div>
        <div class="takeaway-banner">
            <div class="takeaway-text">💡 核心真相：借鏡西歐成功經驗：打破陳舊枷鎖，讓每一種充滿愛的家庭型態都能獲得國家的溫暖支持！</div>
            <div class="takeaway-source">法制借鏡：法國 PACS 伴侶法與北歐多元家庭政策</div>
        </div>
    </div>

    <!-- Slide 26: 結語與 Q&A (Closing) -->
    <div class="slide slide-cover" id="slide-26">
        <h1 class="cover-title" style="font-size: 38px; line-height: 1.4; margin-bottom: 25px;">
            唯有當社會真正容得下生活、自由與尊嚴，<br>
            生育才可能再次成為被期待的幸福。
        </h1>
        <div class="cover-subtitle" style="font-size: 19px; max-width: 850px; line-height: 1.8; margin-bottom: 35px;">
            少子化從來不是年輕世代對未來的冷漠或自私，<br>
            而是個體在面對高房價、長工時、私領域不平等與制度枷鎖時，所做出的最沉重、最理性的非暴力抵抗。
        </div>

        <div class="cover-logo-box">
            <img src="###NYCU###" alt="國立陽明交通大學">
            <img src="###LOGO2###" alt="學院系所">
            <img src="###IMAGE###" alt="專題實驗室">
        </div>

        <div style="font-size: 20px; font-weight: 800; color: #ffffff;">感謝聆聽・敬請指教 (Q&A)</div>
        <div style="font-size: 14px; color: #94a3b8; margin-top: 8px;">完整 23 篇文獻解析與計量模型已收錄於 Karpathy LLM Wiki 知識庫</div>
    </div>

    <!-- 底部控制列與進度條 -->
    <div class="deck-footer">
        <div>
            <span id="cur-slide" style="font-weight: 800; color: var(--navy-primary);">1</span> / <span id="total-slide">26</span>
        </div>
        <div class="deck-btn-group">
            <button class="ctrl-btn" onclick="prevSlide()">◀ 上一頁 (Left)</button>
            <button class="ctrl-btn" onclick="nextSlide()">下一頁 (Right) ▶</button>
            <button class="ctrl-btn" onclick="toggleFullScreen()">全螢幕放映 (F)</button>
        </div>
    </div>
    <div class="progress-bar-wrap">
        <div class="progress-bar-fill" id="prog-fill"></div>
    </div>

</div>

<script>
    let currentSlide = 1;
    const totalSlides = 26;

    function showSlide(n) {{
        if (n < 1) n = 1;
        if (n > totalSlides) n = totalSlides;

        document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
        const target = document.getElementById('slide-' + n);
        if (target) {{
            target.classList.add('active');
            currentSlide = n;
            document.getElementById('cur-slide').innerText = n;
            const pct = ((n - 1) / (totalSlides - 1)) * 100;
            document.getElementById('prog-fill').style.width = pct + '%';
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

    // 鍵盤導航
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

    // 點擊翻頁 (左右半邊點擊)
    document.getElementById('deck-container').addEventListener('click', function(e) {{
        if (e.target.tagName !== 'BUTTON' && !e.target.closest('button') && !e.target.closest('.formula-part')) {{
            const rect = this.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            if (clickX > rect.width * 0.7) {{
                nextSlide();
            }} else if (clickX < rect.width * 0.3) {{
                prevSlide();
            }}
        }}
    }});

    // 公式分步點燈互動函數
    function highlightFormula(type) {{
        const partM = document.getElementById('part-m');
        const partF = document.getElementById('part-f');
        const btnM = document.getElementById('btn-m');
        const btnF = document.getElementById('btn-f');
        const title = document.getElementById('desc-title');
        const text = document.getElementById('desc-text');
        const val = document.getElementById('desc-val');

        partM.classList.remove('lit-gold', 'lit-blue');
        partF.classList.remove('lit-gold', 'lit-blue');
        btnM.classList.remove('active');
        btnF.classList.remove('active');

        if (type === 'm') {{
            partM.classList.add('lit-gold');
            btnM.classList.add('active');
            title.style.color = '#b45309';
            val.style.color = '#b45309';
            title.innerText = '婚姻結構變動效應 (ΔM_a)：貢獻度高達 82%！';
            text.innerText = '實證分解指出：每下降 1 點生育率，超過八成來自「大家結不了婚或延後初婚」！';
            val.innerText = '82%';
        }} else if (type === 'f') {{
            partF.classList.add('lit-blue');
            btnF.classList.add('active');
            title.style.color = '#0284c7';
            val.style.color = '#0284c7';
            title.innerText = '婚內生育率下降效應 (ΔF_a)：貢獻度僅佔 18%！';
            text.innerText = '夫妻結婚之後少生的影響力，其實只有不到兩成，並非少子化的主要源頭！';
            val.innerText = '18%';
        }} else {{
            partM.classList.add('lit-gold');
            partF.classList.add('lit-blue');
            title.style.color = 'var(--navy-primary)';
            val.style.color = 'var(--navy-primary)';
            title.innerText = 'Kitagawa 總和生育率完全分解模型';
            text.innerText = '左項婚姻結構效應 (82%) ＋ 右項婚內生育效應 (18%) ＝ 總生育率完全變動 (100%)';
            val.innerText = '100%';
        }}
    }}

    // 初始化
    showSlide(1);
</script>

</body>
</html>
'''

html_content = html_content_raw.replace('###NYCU###', b64_nycu).replace('###LOGO2###', b64_logo2).replace('###IMAGE###', b64_image)
with open('wiki/slides/SL-FER-TaiwanFertilityDecline.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SL-FER-TaiwanFertilityDecline.html constructed successfully with full specs!")
