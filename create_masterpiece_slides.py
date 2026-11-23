import os
import base64

def get_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

nycu = get_b64('wiki/slides/assets/NYCU.png')
logo2 = get_b64('wiki/slides/assets/logo2.png')
image = get_b64('wiki/slides/assets/image.png')

# 產出完全離線、1920x1080 向量等比縮放、具備現代商業簡報質感的 HTML
html_str = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>倒數第一的真相：到底是什麼影響了台灣的生育率？</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: #030712;
            color: #0f172a;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            user-select: none;
        }

        /* 1920x1080 固定畫布，透過 JS 向量等比縮放至視窗 */
        #slide-viewport {
            width: 1920px;
            height: 1080px;
            position: absolute;
            transform-origin: center center;
            background-color: #ffffff;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8);
            overflow: hidden;
        }

        .slide-page {
            width: 1920px;
            height: 1080px;
            position: absolute;
            top: 0;
            left: 0;
            padding: 70px 100px 80px 100px;
            display: none;
            flex-direction: column;
            justify-content: space-between;
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
            background-color: #ffffff;
        }

        .slide-page.active {
            display: flex;
            opacity: 1;
            z-index: 10;
        }

        /* 母片 Header */
        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-bottom: 3px solid #e2e8f0;
            padding-bottom: 20px;
        }

        .header-title-box {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .header-tag {
            font-size: 16px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #2563eb;
        }

        .header-headline {
            font-size: 42px;
            font-weight: 900;
            color: #0f172a;
            line-height: 1.2;
            letter-spacing: -0.5px;
        }

        .header-logos {
            display: flex;
            align-items: center;
            gap: 24px;
            padding: 6px 16px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.95);
        }

        .header-logos img {
            height: 42px;
            object-fit: contain;
        }

        /* 內容視覺主舞台 (佔比 65%+) */
        .stage-area {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px 0;
            position: relative;
        }

        /* 底部結論橫條 */
        .page-footer-banner {
            background: linear-gradient(90deg, #f8fafc 0%, #eff6ff 100%);
            border-left: 8px solid #2563eb;
            padding: 18px 30px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        }

        .footer-banner-text {
            font-size: 24px;
            font-weight: 800;
            color: #0f2b5c;
        }

        .footer-banner-source {
            font-size: 16px;
            font-weight: 600;
            color: #64748b;
        }

        /* ================= 特殊風格頁面 ================= */

        /* 封面頁 Cover */
        .cover-page {
            background: linear-gradient(135deg, #070d1e 0%, #0f2b5c 50%, #1e3a8a 100%);
            color: #ffffff;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 80px 140px;
        }

        .cover-pill {
            display: inline-block;
            background: rgba(59, 130, 246, 0.2);
            border: 1.5px solid rgba(96, 165, 250, 0.4);
            color: #93c5fd;
            padding: 8px 24px;
            border-radius: 40px;
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 30px;
        }

        .cover-main-title {
            font-size: 64px;
            font-weight: 900;
            line-height: 1.25;
            color: #ffffff;
            margin-bottom: 24px;
            text-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }

        .cover-sub-title {
            font-size: 30px;
            color: #cbd5e1;
            font-weight: 400;
            margin-bottom: 50px;
            max-width: 1400px;
            line-height: 1.5;
        }

        .cover-logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 60px;
            background: rgba(255, 255, 255, 0.98);
            padding: 24px 60px;
            border-radius: 16px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
            margin-bottom: 40px;
        }

        .cover-logo-container img {
            height: 68px;
            object-fit: contain;
        }

        .cover-credit {
            font-size: 22px;
            font-weight: 700;
            color: #e2e8f0;
        }

        /* 提問懸念頁 Hook */
        .hook-page {
            background: linear-gradient(135deg, #0b132b 0%, #1e3a8a 100%);
            color: #ffffff;
            justify-content: center;
            padding: 100px 140px;
        }

        .hook-badge {
            font-size: 22px;
            font-weight: 900;
            color: #f59e0b;
            letter-spacing: 3px;
            margin-bottom: 25px;
            text-transform: uppercase;
        }

        .hook-question-text {
            font-size: 52px;
            font-weight: 900;
            line-height: 1.35;
            color: #ffffff;
            margin-bottom: 50px;
        }

        .hook-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            width: 100%;
        }

        .hook-card {
            padding: 35px 40px;
            border-radius: 12px;
            font-size: 26px;
            line-height: 1.6;
        }

        .hook-card.intuition {
            background: rgba(255, 255, 255, 0.08);
            border-left: 8px solid #94a3b8;
            color: #e2e8f0;
        }

        .hook-card.fact {
            background: rgba(37, 99, 235, 0.25);
            border-left: 8px solid #f59e0b;
            color: #ffffff;
            font-weight: 700;
        }

        /* ================= 專業向量圖表元件 (Infographics) ================= */

        /* 巨型指標卡片 */
        .metric-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            width: 100%;
            height: 100%;
            align-items: center;
        }

        .metric-card {
            background: #f8fafc;
            border: 2px solid #e2e8f0;
            border-radius: 16px;
            padding: 40px 50px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.03);
            position: relative;
        }

        .metric-card.accent {
            background: #fef2f2;
            border-color: #f87171;
        }

        .metric-val {
            font-size: 76px;
            font-weight: 900;
            color: #0f2b5c;
            line-height: 1;
            margin-bottom: 15px;
        }

        .metric-card.accent .metric-val {
            color: #dc2626;
        }

        .metric-title {
            font-size: 28px;
            font-weight: 800;
            color: #1e293b;
            margin-bottom: 12px;
        }

        .metric-desc {
            font-size: 20px;
            color: #64748b;
            line-height: 1.5;
        }

        /* 雙柱長條對比圖 */
        .bar-chart-stage {
            width: 100%;
            height: 480px;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            border-bottom: 3px solid #cbd5e1;
            padding: 0 60px 20px 60px;
        }

        .bar-col {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 260px;
        }

        .bar-col .val {
            font-size: 44px;
            font-weight: 900;
            margin-bottom: 12px;
            color: #0f2b5c;
        }

        .bar-col.alert .val { color: #dc2626; }

        .bar-body {
            width: 110px;
            border-radius: 12px 12px 0 0;
            height: 0;
            transition: height 1s cubic-bezier(0.34, 1.56, 0.64, 1);
            background: linear-gradient(180deg, #3b82f6 0%, #1e3a8a 100%);
        }

        .bar-body.alert {
            background: linear-gradient(180deg, #f87171 0%, #dc2626 100%);
        }

        .bar-body.gray {
            background: linear-gradient(180deg, #94a3b8 0%, #475569 100%);
        }

        .slide-page.active .bar-body.h-22 { height: 130px; }
        .slide-page.active .bar-body.h-64 { height: 380px; }
        .slide-page.active .bar-body.h-50 { height: 280px; }
        .slide-page.active .bar-body.h-15 { height: 100px; }
        .slide-page.active .bar-body.h-72 { height: 410px; }

        .bar-col .label {
            margin-top: 15px;
            font-size: 22px;
            font-weight: 800;
            color: #1e293b;
            text-align: center;
            line-height: 1.4;
        }

        /* 橫向長條排行 */
        .rank-list {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 24px;
            padding: 0 40px;
        }

        .rank-row {
            display: flex;
            align-items: center;
            gap: 25px;
        }

        .rank-name {
            width: 240px;
            font-size: 24px;
            font-weight: 800;
            text-align: right;
            color: #0f2b5c;
        }

        .rank-bar-wrap {
            flex: 1;
            height: 52px;
            background: #f1f5f9;
            border-radius: 8px;
            overflow: hidden;
            position: relative;
        }

        .rank-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #3b82f6 0%, #1d4ed8 100%);
            width: 0%;
            transition: width 1s cubic-bezier(0.25, 1, 0.5, 1);
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 20px;
            color: #ffffff;
            font-weight: 900;
            font-size: 24px;
        }

        .rank-bar-fill.red {
            background: linear-gradient(90deg, #f87171 0%, #dc2626 100%);
        }

        .slide-page.active .rank-bar-fill.w-62 { width: 62.2%; }
        .slide-page.active .rank-bar-fill.w-55 { width: 55.2%; }
        .slide-page.active .rank-bar-fill.w-40 { width: 40.5%; }
        .slide-page.active .rank-bar-fill.w-03 { width: 3.8%; }
        .slide-page.active .rank-bar-fill.w-64 { width: 64.2%; }
        .slide-page.active .rank-bar-fill.w-47 { width: 47.5%; }
        .slide-page.active .rank-bar-fill.w-33 { width: 33.8%; }
        .slide-page.active .rank-bar-fill.w-75 { width: 75%; }
        .slide-page.active .rank-bar-fill.w-25 { width: 25%; }

        /* 公式分步變色互動器 */
        .formula-box {
            width: 100%;
            background: #f8fafc;
            border: 3px solid #e2e8f0;
            border-radius: 16px;
            padding: 35px 50px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .formula-math-line {
            font-size: 48px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 30px;
            font-family: Cambria, "Times New Roman", serif;
        }

        .math-seg {
            padding: 8px 20px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            border: 3px solid transparent;
        }

        .math-seg.active-gold {
            background: #fef3c7;
            border-color: #f59e0b;
            color: #b45309;
            box-shadow: 0 0 25px rgba(245, 158, 11, 0.4);
            transform: scale(1.08);
        }

        .math-seg.active-blue {
            background: #e0f2fe;
            border-color: #0284c7;
            color: #0369a1;
            box-shadow: 0 0 25px rgba(2, 132, 199, 0.4);
            transform: scale(1.08);
        }

        .formula-actions {
            display: flex;
            gap: 20px;
            margin-bottom: 25px;
        }

        .action-pill {
            background: #ffffff;
            border: 2px solid #cbd5e1;
            padding: 12px 28px;
            border-radius: 30px;
            font-size: 20px;
            font-weight: 800;
            color: #0f172a;
            cursor: pointer;
            transition: all 0.2s;
        }

        .action-pill:hover, .action-pill.selected {
            background: #0f2b5c;
            color: #ffffff;
            border-color: #0f2b5c;
        }

        .formula-card-detail {
            width: 100%;
            background: #ffffff;
            border: 2px solid #cbd5e1;
            border-radius: 12px;
            padding: 24px 35px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* 雙象限分流對比圖 */
        .duo-card-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            width: 100%;
            height: 100%;
        }

        .duo-card {
            border-radius: 16px;
            padding: 35px 40px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.04);
        }

        .duo-card.positive {
            background: #f0fdf4;
            border: 3px solid #22c55e;
        }

        .duo-card.negative {
            background: #fef2f2;
            border: 3px solid #ef4444;
        }

        .duo-card-title {
            font-size: 32px;
            font-weight: 900;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .duo-card.positive .duo-card-title { color: #15803d; }
        .duo-card.negative .duo-card-title { color: #b91c1c; }

        .duo-card-body {
            font-size: 24px;
            line-height: 1.6;
            color: #1e293b;
        }

        /* 全景 Master Graph 大圖 */
        .master-graph-canvas {
            width: 100%;
            background: #f8fafc;
            border: 3px solid #cbd5e1;
            border-radius: 16px;
            padding: 30px 40px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .mg-row {
            display: flex;
            align-items: center;
            gap: 20px;
            background: #ffffff;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px 24px;
        }

        .mg-row.r1 { border-left: 10px solid #2563eb; }
        .mg-row.r2 { border-left: 10px solid #a855f7; }

        .mg-title-badge {
            font-size: 20px;
            font-weight: 900;
            color: #ffffff;
            padding: 10px 18px;
            border-radius: 8px;
            white-space: nowrap;
        }

        .mg-row.r1 .mg-title-badge { background: #2563eb; }
        .mg-row.r2 .mg-title-badge { background: #a855f7; }

        .mg-steps {
            display: flex;
            align-items: center;
            gap: 15px;
            flex: 1;
            font-size: 22px;
            font-weight: 800;
            color: #0f172a;
        }

        .mg-node {
            background: #f1f5f9;
            border: 1.5px solid #cbd5e1;
            padding: 8px 16px;
            border-radius: 8px;
        }

        .mg-node.alert {
            background: #fee2e2;
            border-color: #ef4444;
            color: #dc2626;
        }

        .mg-sep {
            color: #2563eb;
            font-weight: 900;
        }

        .mg-bottom-impact {
            background: linear-gradient(90deg, #070d1e 0%, #b91c1c 100%);
            color: #ffffff;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            font-size: 28px;
            font-weight: 900;
            box-shadow: 0 10px 30px rgba(185, 28, 28, 0.3);
        }

        /* 導航控制列 */
        .controls-bar {
            position: absolute;
            bottom: 20px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 50px;
            font-size: 18px;
            font-weight: 700;
            color: #64748b;
            z-index: 100;
            pointer-events: none;
        }

        .controls-btns {
            display: flex;
            gap: 15px;
            pointer-events: auto;
        }

        .ctrl-pill-btn {
            background: #ffffff;
            border: 2px solid #cbd5e1;
            padding: 8px 20px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 800;
            color: #0f172a;
            cursor: pointer;
            transition: all 0.2s;
        }

        .ctrl-pill-btn:hover {
            background: #0f2b5c;
            color: #ffffff;
        }

        .progress-track {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 6px;
            background: #e2e8f0;
            z-index: 100;
        }

        .progress-indicator {
            height: 100%;
            background: #2563eb;
            width: 0%;
            transition: width 0.25s ease;
        }
    </style>
</head>
<body>

<div id="slide-viewport">

    <!-- Page 1: Cover -->
    <div class="slide-page cover-page active" id="p-1">
        <div class="cover-pill">科普學術演講・當代人口學與公共經濟學分析</div>
        <h1 class="cover-main-title">倒數第一的真相：到底是什麼影響了台灣的生育率？</h1>
        <h2 class="cover-sub-title">從 23 篇國內外實證論文看「結不了婚」與「不敢生二胎」的雙軌困局與制度解方</h2>
        
        <div class="cover-logo-container">
            <img src="###NYCU###" alt="國立陽明交通大學">
            <img src="###LOGO2###" alt="學院系所">
            <img src="###IMAGE###" alt="專題實驗室">
        </div>

        <div class="cover-credit">國立陽明交通大學 專題研究團隊</div>
        <div style="font-size: 18px; color: #94a3b8; margin-top: 8px;">以微觀追蹤資料（PSFD、TYP、社會變遷基本調查）與計量因果模型為實證基石</div>
    </div>

    <!-- Page 2: Hook 01 -->
    <div class="slide-page hook-page" id="p-2">
        <div class="hook-badge">HOOK 01・直擊矛盾</div>
        <div class="hook-question-text">政府年年狂砸千億補貼，為什麼台灣生育率依舊跌到全球墊底？</div>
        <div class="hook-grid">
            <div class="hook-card intuition">
                <div style="font-size: 20px; font-weight: 800; color: #94a3b8; margin-bottom: 12px;">大眾常見直覺：</div>
                「現在年輕人愛享受、自私不想承擔家庭責任？多發錢、多送禮，大家就會樂意生孩子了？」
            </div>
            <div class="hook-card fact">
                <div style="font-size: 20px; font-weight: 800; color: #f59e0b; margin-bottom: 12px;">硬核數據真相：</div>
                2024 年全台少子化預算突破 <b>1,100 億元</b>，總和生育率卻一路墜崖至 <b>0.865</b>！<br>
                <b>病因診斷錯誤，再多的補貼也只是向大海撒錢！</b>
            </div>
        </div>
    </div>

    <!-- Page 3: 數據震撼 (雙柱長條生長圖) -->
    <div class="slide-page" id="p-3">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">人口統計真相・數據說話</div>
                <div class="header-headline">已婚夫妻依然在生，崩盤的其實是「結婚率」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="bar-chart-stage">
                <div class="bar-col">
                    <div class="val">22.7%</div>
                    <div class="bar-body h-22 gray"></div>
                    <div class="label">1990 年<br>30-34歲男性未婚率</div>
                </div>
                <div class="bar-col alert">
                    <div class="val">64.3%</div>
                    <div class="bar-body h-64 alert"></div>
                    <div class="label" style="color: #dc2626;">2020 年<br>30-34歲男性未婚率</div>
                </div>
                <div class="bar-col">
                    <div class="val">1.62 個</div>
                    <div class="bar-body h-50 gray"></div>
                    <div class="label">2000 年<br>有偶婦女生育數</div>
                </div>
                <div class="bar-col">
                    <div class="val">1.58 個</div>
                    <div class="bar-body h-50 gray"></div>
                    <div class="label">2020 年<br>有偶婦女生育數</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：已婚夫妻平均仍生育 1.6 個孩子，少子化的真兇是「青年被大規模阻絕於婚姻之外」！</div>
            <div class="footer-banner-source">數據出處：內政部戶籍統計資料與人口住宅普查報告</div>
        </div>
    </div>

    <!-- Page 4: 核心數學 (公式互動分步變色點燈) -->
    <div class="slide-page" id="p-4">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">人口學因果分解・核心公式</div>
                <div class="header-headline">Kitagawa 分解法揭秘：82% 的少子化是由「不婚」貢獻的！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="formula-box">
                <div class="formula-math-line">
                    <span>ΔTFR = </span>
                    <span class="math-seg active-gold" id="seg-m" onclick="switchMath('m')">∑ ΔM_a · F̄_a</span>
                    <span> + </span>
                    <span class="math-seg" id="seg-f" onclick="switchMath('f')">∑ M̄_a · ΔF_a</span>
                </div>
                <div class="formula-actions">
                    <button class="action-pill selected" id="btn-seg-m" onclick="switchMath('m')">步驟 1：檢視「未婚率上升效應」</button>
                    <button class="action-pill" id="btn-seg-f" onclick="switchMath('f')">步驟 2：檢視「婚內少生效應」</button>
                    <button class="action-pill" onclick="switchMath('all')">還原完整公式</button>
                </div>
                <div class="formula-card-detail">
                    <div>
                        <div style="font-size: 28px; font-weight: 900; color: #b45309;" id="math-title">婚姻結構變動效應 (ΔM_a)：貢獻度高達 82%！</div>
                        <div style="font-size: 20px; color: #64748b; margin-top: 8px;" id="math-desc">人口學實證分解指出：每下降 1 點生育率，超過八成來自「大家結不了婚或延後初婚」！</div>
                    </div>
                    <div style="font-size: 54px; font-weight: 900; color: #b45309;" id="math-val">82%</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：少子化的真正本質是「不婚化」！忽視成家門檻的任何催生政策，都是隔靴搔癢。</div>
            <div class="footer-banner-source">計量方法：Kitagawa 人口因果分解法</div>
        </div>
    </div>

    <!-- Page 5: 東亞婚育包裹 -->
    <div class="slide-page" id="p-5">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">跨國制度對照・婚育包裹</div>
                <div class="header-headline">台灣制度死穴：在台灣，不結婚就是「完全不准生」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="rank-list">
                <div class="rank-row">
                    <div class="rank-name">法國 (France)</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill w-62">62.2%</div></div>
                </div>
                <div class="rank-row">
                    <div class="rank-name">瑞典 (Sweden)</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill w-55">55.2%</div></div>
                </div>
                <div class="rank-row">
                    <div class="rank-name">美國 (USA)</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill w-40">40.5%</div></div>
                </div>
                <div class="rank-row">
                    <div class="rank-name" style="color: #dc2626;">台灣 (Taiwan)</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill red w-03">3.8%</div></div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：歐美同居生子享有完整法律與托育平權；但在台灣，婚姻是生育的唯一合法特許證！</div>
            <div class="footer-banner-source">數據出處：OECD 人口資料庫 & 中央研究院社會學研究所</div>
        </div>
    </div>

    <!-- Page 6: Hook 02 -->
    <div class="slide-page hook-page" id="p-6">
        <div class="hook-badge">HOOK 02・破除刻板印象</div>
        <div class="hook-question-text">長輩常嘆「現代年輕人崇尚單身、自私不想成家」，真的嗎？</div>
        <div class="hook-grid">
            <div class="hook-card intuition">
                <div style="font-size: 20px; font-weight: 800; color: #94a3b8; margin-bottom: 12px;">社會刻板偏見：</div>
                「現在年輕人只想吃喝玩樂、愛自由、討厭家庭束縛，把婚姻當作洪水猛獸？」
            </div>
            <div class="hook-card fact">
                <div style="font-size: 20px; font-weight: 800; color: #f59e0b; margin-bottom: 12px;">全國問卷實證：</div>
                30 歲以前的未婚男女中，有超過 <b>85%</b> 明確表示「未來希望走入婚姻」！<br>
                <b>年輕人不是不想結，而是面臨極度嚴峻的現實障礙！</b>
            </div>
        </div>
    </div>

    <!-- Page 7: 想婚卻結不了 -->
    <div class="slide-page" id="p-7">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道一：成家障礙・微觀調查</div>
                <div class="header-headline">未婚青年不是拒絕婚姻，而是選擇「寧缺勿濫」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="rank-list">
                <div class="rank-row">
                    <div class="rank-name" style="width: 320px;">尚未遇到合適對象</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill w-64">64.2%（重視心靈契合與價值觀）</div></div>
                </div>
                <div class="rank-row">
                    <div class="rank-name" style="width: 320px;">經濟基礎尚未就緒</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill w-47">47.5%（自認低薪、買不起房）</div></div>
                </div>
                <div class="rank-row">
                    <div class="rank-name" style="width: 320px;">恐懼婚後生活品質降低</div>
                    <div class="rank-bar-wrap"><div class="rank-bar-fill w-33">33.8%（長輩爭吵與離婚陰影）</div></div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：面對高昂的生活成本，現代青年對婚姻慎重以對，沒有把握寧可維持單身，拒絕湊合！</div>
            <div class="footer-banner-source">實證來源：臺灣華人家庭動態調查（PSFD）1,714 位未婚樣本</div>
        </div>
    </div>

    <!-- Page 8: 婚姻特許考 (天平) -->
    <div class="slide-page" id="p-8">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道一：成家門檻・物質防衛</div>
                <div class="header-headline">成家先買房：逾半數女性堅持「有房才結婚」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="metric-grid">
                <div class="metric-card accent">
                    <div class="metric-val">55.3%</div>
                    <div class="metric-title">未婚女性堅持婚前買房</div>
                    <div class="metric-desc">女性預期婚後將承擔家務、生育與職涯中斷風險，要求男方備房作為「制度防衛補償」與財產底線。</div>
                </div>
                <div class="metric-card">
                    <div class="metric-val">43.1%</div>
                    <div class="metric-title">未婚男性認為租屋亦可</div>
                    <div class="metric-desc">男性傾向先求有再求好，但面對女方與岳父母的買房剛需，普遍自認未達標而延後求婚。</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：當「成家」綁定「買房」，高房價直接升級為剝奪青年成家資格的無情篩漏！</div>
            <div class="footer-banner-source">實證文獻：《人文及社會科學集刊》未婚男女買房態度調查</div>
        </div>
    </div>

    <!-- Page 9: 婚姻斜坡 -->
    <div class="slide-page" id="p-9">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道一：婚配結構・性別不對稱</div>
                <div class="header-headline">殘酷的婚姻斜坡：薪水越高，男人越好結、女人越難嫁！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-title">♂️ 男性結婚機率：隨經濟增長直線上升</div>
                    <div class="duo-card-body">
                        • <b>每月薪資每上升 1 萬元</b> ➜ 結婚勝算顯著提升 <b>+18%</b>！<br>
                        • <b>每週工時加班增加</b> ➜ 被視為事業有成，結婚機率顯著增加！<br>
                        • 社會傳統依舊將男性綁定為「家庭經濟主力責任」。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-title">♀️ 女性結婚機率：隨經濟自主反而下降</div>
                    <div class="duo-card-body">
                        • <b>每月薪資每上升 1 萬元</b> ➜ 結婚機率逆向暴跌 <b>-14%</b>！<br>
                        • <b>女性以自身經濟為「參考點門檻」</b>，堅決拒絕下嫁！<br>
                        • 傳統「男高女低」觀念未變，高社經女性與中低薪男性雙雙被擠壓。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：女性經濟獨立了，婚配文化卻停留在舊時代，導致現代婚姻市場嚴重配對失靈！</div>
            <div class="footer-banner-source">計量實證：清華大學經濟學研究所 PSFD 追蹤資料 Logit 模型分析</div>
        </div>
    </div>

    <!-- Page 10: 同居假象 -->
    <div class="slide-page" id="p-10">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道一：親密關係・同居現狀</div>
                <div class="header-headline">同居暴增 4 倍但生育為零：台灣同居只是「合租單身」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="metric-val" style="color: #2563eb;">40%</div>
                    <div class="metric-title">青年未婚同居普及率</div>
                    <div class="metric-desc">同居率自早期不到 10% 快速翻倍攀升至近 40%，成為普遍的親密關係模式。</div>
                </div>
                <div class="metric-card accent">
                    <div class="metric-val" style="color: #dc2626;">30%</div>
                    <div class="metric-title">同居者具備成家結婚規劃</div>
                    <div class="metric-desc">過去有 70% 同居者打算結婚，如今腰斬至 30%；且同居生育率低於 3%，完全無法催生。</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：缺乏法制與托育保障，台灣的同居只是單身生活的延長，完全無法如歐洲般轉化為新生兒！</div>
            <div class="footer-banner-source">權威研究：美國婚姻與家庭期刊（Journal of Marriage and Family, 2023）</div>
        </div>
    </div>

    <!-- Page 11: Hook 03 -->
    <div class="slide-page hook-page" id="p-11">
        <div class="hook-badge">HOOK 03・學術爭議辨析</div>
        <div class="hook-question-text">「高房價是最好的避孕藥」人人皆知……<br>為什麼有些學者卻發現：<b>「房價越漲，生育率反而上升」</b>？</div>
        <div class="hook-grid">
            <div class="hook-card intuition">
                <div style="font-size: 20px; font-weight: 800; color: #94a3b8; margin-bottom: 12px;">學界爭議焦點：</div>
                「難道是經濟學者做研究與現實脫節？還是房價其實對生小孩沒有負面影響？」
            </div>
            <div class="hook-card fact">
                <div style="font-size: 20px; font-weight: 800; color: #f59e0b; margin-bottom: 12px;">微觀因果真相：</div>
                房價是一把無情的雙面刃！它對<b>「已擁房家庭」</b>與<b>「無房青年」</b>的因果作用徹底相反！
            </div>
        </div>
    </div>

    <!-- Page 12: 爭議辨析一：財富 vs 負擔 -->
    <div class="slide-page" id="p-12">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">爭議辨析一・因果機制拆解</div>
                <div class="header-headline">房價是雙面刃：它讓有房族更富，卻把無房青年徹底掏空！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-title">🏠 已購屋擁房族 ➜ 財富效果 (+)</div>
                    <div class="duo-card-body">
                        • 房價大漲 ➜ 房屋淨資產暴增、低利轉貸融資容易。<br>
                        • 家庭財務安全感倍增，促使其提早生育第二胎！<br>
                        • <b>實證效應：對擁房者呈現微幅正向拉動</b>。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-title">🚫 無房青年租屋族 ➜ 排擠效應 (-)</div>
                    <div class="duo-card-body">
                        • 房價飛天 ➜ 首付儲蓄期從 5 年暴拉至 15 年以上。<br>
                        • 高房租與高房貸極限掏空青年所得，直接放棄成家！<br>
                        • <b>實證效應：對無房者造成毀滅性生育打擊</b>。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：房價上漲實質拉大了資產階級與無產青年之間的「階級生育不平等」！</div>
            <div class="footer-banner-source">實證文獻：台灣縣市面板資料分析 & 韓國住房資產實證研究</div>
        </div>
    </div>

    <!-- Page 13: 爭議辨析二：房價箭靶是婚姻 -->
    <div class="slide-page" id="p-13">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">爭議辨析二・因果衝擊彈性</div>
                <div class="header-headline">實證彈性揭秘：房價沒有阻止已婚者生，而是摧毀了初婚！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="bar-chart-stage">
                <div class="bar-col">
                    <div class="val" style="color: #475569;">-1.5%</div>
                    <div class="bar-body h-15 gray"></div>
                    <div class="label">已婚婦女生育率<br>受房價衝擊彈性</div>
                </div>
                <div class="bar-col alert">
                    <div class="val" style="color: #dc2626;">-7.2%</div>
                    <div class="bar-body h-72 alert"></div>
                    <div class="label" style="color: #dc2626;">未婚青年初婚機率<br>受房價衝擊彈性</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：已婚夫妻具備親職韌性，房價衝擊溫和；高房價的致命死穴是「直接關閉了青年的婚姻大門」！</div>
            <div class="footer-banner-source">計量實證：台灣住宅負擔能力與空間擴散計量模型</div>
        </div>
    </div>

    <!-- Page 14: Hook 04 -->
    <div class="slide-page hook-page" id="p-14">
        <div class="hook-badge">HOOK 04・政策成效質疑</div>
        <div class="hook-question-text">各縣市狂砸真金白銀加碼生育津貼，真的催生出了小孩嗎？</div>
        <div class="hook-grid">
            <div class="hook-card intuition">
                <div style="font-size: 20px; font-weight: 800; color: #94a3b8; margin-bottom: 12px;">地方首長最愛政績：</div>
                「台北發 2 萬、桃園給 3 萬、花蓮開 5 萬！只要發錢夠大方，年輕人就會樂意增產報國？」
            </div>
            <div class="hook-card fact">
                <div style="font-size: 20px; font-weight: 800; color: #f59e0b; margin-bottom: 12px;">因果計量模型檢驗：</div>
                雙重差分法（DID）與合成控制法（SCM）揭露驚人事實：<br>
                <b>地方生育津貼對全國總出生數的淨貢獻值，實質等於零！</b>
            </div>
        </div>
    </div>

    <!-- Page 15: 爭議辨析三：幽靈遷徙 -->
    <div class="slide-page" id="p-15">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">爭議辨析三・因果評估 DID</div>
                <div class="header-headline">因果計量戳破謊言：生育津貼沒多生一個小孩，只造成「戶籍大風吹」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card negative">
                    <div class="duo-card-title">👻 跨區幽靈戶籍遷徙（Migration Bias）</div>
                    <div class="duo-card-body">
                        • 某縣市加碼補助 ➜ 鄰近縣市夫妻短期「遷戶籍領錢」。<br>
                        • 該縣市出生數看似微升，鄰縣同步暴跌 ➜ <b>全國總量淨增為 0</b>！
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-title">⏳ 生育時程微幅提早（Timing Effect）</div>
                    <div class="duo-card-body">
                        • 僅促使本來就打算生小孩的家庭「提早幾個月受孕」。<br>
                        • 完全沒有增加婦女一生中的「終身總生育胎數」！
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：地方津貼淪為毫無意義的跨區搶人零和賽局，白白虛耗數十億國家財政！</div>
            <div class="footer-banner-source">評估模型：台灣縣市生育津貼雙重差分法（DID）與合成控制法（SCM）</div>
        </div>
    </div>

    <!-- Page 16: 津貼陷阱 (冰山成本) -->
    <div class="slide-page" id="p-16">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">政策工具比較・成本結構</div>
                <div class="header-headline">幾萬元津貼如杯水車薪：平價公共托育才是真正的定心丸！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card negative">
                    <div class="duo-card-title">🧊 水面上的微小冰山：一次性津貼</div>
                    <div class="duo-card-body">
                        • 補助 3～5 萬元，佔撫養至成年的 800 萬開銷<b>不到 1%</b>！<br>
                        • 生育率拉動彈性係數接近於零，發完即無效。
                    </div>
                </div>
                <div class="duo-card positive">
                    <div class="duo-card-title">🏔️ 水面下的龐大冰山：托育公共化</div>
                    <div class="duo-card-body">
                        • 0-6 歲公托與準公幼，每月實質為雙薪家庭減負 1.5～2 萬元！<br>
                        • <b>國際文獻證實：托育服務供給彈性是一次性現金的 6 至 8 倍！</b>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：生小孩不是一瞬間，而是 18 年的長跑；只有平價公托才能分擔雙薪父母的未來！</div>
            <div class="footer-banner-source">理論支持：新時代生育經濟學（Doepke et al., 2022）</div>
        </div>
    </div>

    <!-- Page 17: Hook 05 -->
    <div class="slide-page hook-page" id="p-17">
        <div class="hook-badge">HOOK 05・軌道二：後端婚內困局</div>
        <div class="hook-question-text">走進了婚姻的媽媽，為什麼生了一個就嚇到「不敢生第二胎」？</div>
        <div class="hook-grid">
            <div class="hook-card intuition">
                <div style="font-size: 20px; font-weight: 800; color: #94a3b8; margin-bottom: 12px;">傳統社會期待：</div>
                「既然都結了婚、生了一胎，順理成章再生第二個作伴，有何困難？」
            </div>
            <div class="hook-card fact">
                <div style="font-size: 20px; font-weight: 800; color: #f59e0b; margin-bottom: 12px;">已婚母親的真實痛點：</div>
                步入婚姻的家庭生第一胎比例高達 80%，但生第二胎驟降至 <b>不到 35%</b>！<br>
                <b>是什麼力量讓婚內媽媽在生完第一胎後，緊急踩下煞車？</b>
            </div>
        </div>
    </div>

    <!-- Page 18: 家務 3.2 倍差距 -->
    <div class="slide-page" id="p-18">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">爭議辨析四・制度性不協調</div>
                <div class="header-headline">白天拼業績，晚上做家務：已婚女性的「雙重輪班」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="bar-chart-stage">
                <div class="bar-col alert">
                    <div class="val">3.8 小時</div>
                    <div class="bar-body h-64 alert"></div>
                    <div class="label" style="color: #dc2626;">已婚女性每日家務育兒時間<br>承擔全家 75% 無償勞動</div>
                </div>
                <div class="bar-col">
                    <div class="val">1.1 小時</div>
                    <div class="bar-body h-22 gray"></div>
                    <div class="label">已婚男性每日家務育兒時間<br>差距高達 3.2 倍！</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：職場講求高工時績效，家庭內部女性卻全包家務；當婚姻意味著勞動加倍，女性的理性防衛就是不生二胎！</div>
            <div class="footer-banner-source">數據出處：行政院性平處性別統計資料 & 台灣家務分工與生育意願研究</div>
        </div>
    </div>

    <!-- Page 19: 姻親文化焦慮 -->
    <div class="slide-page" id="p-19">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">軌道二：家庭文化・質性深入訪談</div>
                <div class="header-headline">零位男性擔心姻親，女性卻視為夢魘：傳統文化成了推力！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-title">👨 受訪男性：0 人擔憂姻親</div>
                    <div class="duo-card-body">
                        • 婚後生活以男方家庭為中心，幾乎感受不到生活秩序的變動。<br>
                        • 很少需要適應女方親戚生活習慣，毫無婚姻外推力。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-title">👩 受訪女性：普遍深感焦慮</div>
                    <div class="duo-card-body">
                        • 從父居生活干預、過年過節儀式義務、婆家規訓。<br>
                        • 「看著母親當全職家庭主婦受盡委屈看臉色，我何必跳入火坑重複一樣的人生？」
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：女性經濟獨立後，有能力對不平等的傳統家庭制度說不；私領域文化停滯正在將女性推離家庭！</div>
            <div class="footer-banner-source">質性訪談：臺灣適婚年齡者進入婚姻與否的考量因素《人口學刊》</div>
        </div>
    </div>

    <!-- Page 20: Hook 06 -->
    <div class="slide-page hook-page" id="p-20">
        <div class="hook-badge">HOOK 06・打破單身標籤</div>
        <div class="hook-question-text">不結婚的單身世代，老了真的像社會說的那樣孤苦淒涼嗎？</div>
        <div class="hook-grid">
            <div class="hook-card intuition">
                <div style="font-size: 20px; font-weight: 800; color: #94a3b8; margin-bottom: 12px;">社會污名標籤：</div>
                「單身就是敗犬、羅漢腳、魯蛇，老了沒人理、成為社會家庭負擔？」
            </div>
            <div class="hook-card fact">
                <div style="font-size: 20px; font-weight: 800; color: #f59e0b; margin-bottom: 12px;">全國抽樣調查揭曉：</div>
                40-59 歲始終單身女性高達 <b>70.8% 為白領階層</b>，月收入與社交活躍度全面超越已婚女性！<br>
                <b>打破刻板印象：單身早已成為一種具備自主性的現代生活選擇！</b>
            </div>
        </div>
    </div>

    <!-- Page 21: 破除單身刻板印象 -->
    <div class="slide-page" id="p-21">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">單身社會學・生活樣態</div>
                <div class="header-headline">單身女性活出高自主性，但單身男性面臨結構性邊緣化！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-title">👩 中年中產單身女性：高社經與高連結</div>
                    <div class="duo-card-body">
                        • <b>70.8% 為白領階層</b>，平均月收入顯著高於曾婚女性！<br>
                        • 每日上網 4.5 小時、朋友聚餐最頻繁（已婚女性走入家庭後社交圈暴跌至 22%）。
                    </div>
                </div>
                <div class="duo-card negative">
                    <div class="duo-card-title">👨 中年單身男性：結構性風險攀升</div>
                    <div class="duo-card-body">
                        • <b>無工作者比例達 22.6%</b>，收入低於曾婚男性。<br>
                        • 社交網絡極度狹窄，過度依賴原生家庭，退休後易陷入社會孤立。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：走入婚姻反而限縮了女性生活圈；但單身男性的就業與社會疏離是未來的隱形危機。</div>
            <div class="footer-banner-source">實證文獻：《人口學刊》中年單身者研究</div>
        </div>
    </div>

    <!-- Page 22: 單身長照負擔 -->
    <div class="slide-page" id="p-22">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">代間關係・隱形負擔</div>
                <div class="header-headline">沒成家的代價：近半數單身者同住長輩，默默扛下全家長照！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="bar-chart-stage">
                <div class="bar-col">
                    <div class="val">48.5%</div>
                    <div class="bar-body h-50 gray"></div>
                    <div class="label">40-59歲單身男性<br>與高齡父母同住</div>
                </div>
                <div class="bar-col">
                    <div class="val">45.4%</div>
                    <div class="bar-body h-50 gray"></div>
                    <div class="label">40-59歲單身女性<br>與高齡父母同住</div>
                </div>
                <div class="bar-col alert">
                    <div class="val" style="color: #dc2626;">71.1%</div>
                    <div class="bar-body h-72 alert"></div>
                    <div class="label" style="color: #dc2626;">單身女性向父母提供<br>日常生活與失能照料</div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：「反正你沒家室，長輩由你照顧」——未婚青年逃離了育兒，卻在中年提前被吸入長照泥淖！</div>
            <div class="footer-banner-source">資料來源：臺灣社會變遷基本調查與人口住宅普查</div>
        </div>
    </div>

    <!-- Page 23: Master Causal Graph (全景大圖) -->
    <div class="slide-page" id="p-23">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">終極因果網絡・全景大圖</div>
                <div class="header-headline">台灣低生育率立體因果圖：雙軌扣殺下的理性抵抗！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="master-graph-canvas">
                <div class="mg-row r1">
                    <div class="mg-title-badge">軌道一：前端成家鎖死 (82%)</div>
                    <div class="mg-steps">
                        <div class="mg-node">高房價與買房剛需</div>
                        <div class="mg-sep">➔</div>
                        <div class="mg-node">婚姻斜坡配對失靈</div>
                        <div class="mg-sep">➔</div>
                        <div class="mg-node alert">未婚率暴飆至 64%</div>
                        <div class="mg-sep">➔</div>
                        <div class="mg-node">婚育包裹 (非婚僅3.8%)</div>
                    </div>
                </div>
                <div class="mg-row r2">
                    <div class="mg-title-badge">軌道二：後端家庭撕裂 (18%)</div>
                    <div class="mg-steps">
                        <div class="mg-node">高壓超長工時</div>
                        <div class="mg-sep">➔</div>
                        <div class="mg-node">私領域家務全包 (3.2倍)</div>
                        <div class="mg-sep">➔</div>
                        <div class="mg-node alert">雙重輪班母職懲罰</div>
                        <div class="mg-sep">➔</div>
                        <div class="mg-node">已婚媽媽不敢生二胎</div>
                    </div>
                </div>
                <div class="mg-bottom-impact">
                    💥 雙軌連環扣殺 ➔ 台灣總和生育率跌破 0.865（全球倒數第一的真正因果！）
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：少子化是青年面對殘酷生存壓力與不平等家庭體制時，所做出的最沉重、最理性的非暴力抵抗！</div>
            <div class="footer-banner-source">本簡報 23 篇實證文獻因果統合模型</div>
        </div>
    </div>

    <!-- Page 24: 政策突圍一 -->
    <div class="slide-page" id="p-24">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">政策典範轉移・結構突圍</div>
                <div class="header-headline">停止發錢催生！千億預算全面轉向「拆除成家障礙」！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-title">🏹 第一支箭：新婚青年社宅長租保障</div>
                    <div class="duo-card-body">
                        • 提供 5-10 年平價社宅長租保障，打破「買得起房才配結婚」的致命魔咒！<br>
                        • 將居住正義直接對接成家關鍵期。
                    </div>
                </div>
                <div class="duo-card positive">
                    <div class="duo-card-title">🏹 第二支箭：0-6 歲托育全面公共化</div>
                    <div class="duo-card-body">
                        • 停止發放無效的一次性幾萬元津貼，全面投入公托與準公幼。<br>
                        • 實質減輕父母長達 18 年的經濟與托育機會成本。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：唯有國家主動分擔居住與育兒的長期成本，年輕人才有勇氣走入婚姻！</div>
            <div class="footer-banner-source">政策建議：公共經濟學與家庭福利典範轉移</div>
        </div>
    </div>

    <!-- Page 25: 政策突圍二 -->
    <div class="slide-page" id="p-25">
        <div class="page-header">
            <div class="header-title-box">
                <div class="header-tag">制度創新・包容性社會</div>
                <div class="header-headline">讓生育不再被單一婚姻綁架：鬆綁婚育包裹，邁向多元！</div>
            </div>
            <div class="header-logos">
                <img src="###NYCU###" alt="NYCU">
                <img src="###LOGO2###" alt="系所">
                <img src="###IMAGE###" alt="Lab">
            </div>
        </div>
        <div class="stage-area">
            <div class="duo-card-grid">
                <div class="duo-card positive">
                    <div class="duo-card-title">⚖️ 鬆綁《人工生殖法》</div>
                    <div class="duo-card-body">
                        • 開放單身女性與未婚伴侶合法使用生殖醫學技術，還原自主生殖權利！<br>
                        • 讓具備撫養意願與經濟能力的個體不再受限於一紙婚約。
                    </div>
                </div>
                <div class="duo-card positive">
                    <div class="duo-card-title">👶 非婚生子女與多元伴侶平權</div>
                    <div class="duo-card-body">
                        • 消除福利、稅務與戶政登記上對非婚生子女的隱形歧視。<br>
                        • 法律承認穩定同居伴侶之撫養與家庭照顧權益。
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer-banner">
            <div class="footer-banner-text">💡 核心真相：借鏡西歐成功經驗：打破陳舊枷鎖，讓每一種充滿愛的家庭型態都能獲得國家的溫暖支持！</div>
            <div class="footer-banner-source">法制借鏡：法國 PACS 伴侶法與北歐政策</div>
        </div>
    </div>

    <!-- Page 26: 結語與 Q&A -->
    <div class="slide-page cover-page" id="p-26">
        <h1 class="cover-main-title" style="font-size: 50px; line-height: 1.4; margin-bottom: 30px;">
            唯有當社會真正容得下生活、自由與尊嚴，<br>
            生育才可能再次成為被期待的幸福。
        </h1>
        <div class="cover-sub-title" style="font-size: 24px; max-width: 1200px; line-height: 1.8; margin-bottom: 50px;">
            少子化從來不是年輕世代對未來的冷漠或自私，<br>
            而是個體在面對高房價、長工時、私領域不平等與制度枷鎖時，所做出的最沉重、最理性的非暴力抵抗。
        </div>

        <div class="cover-logo-container">
            <img src="###NYCU###" alt="國立陽明交通大學">
            <img src="###LOGO2###" alt="學院系所">
            <img src="###IMAGE###" alt="專題實驗室">
        </div>

        <div style="font-size: 28px; font-weight: 800; color: #ffffff;">感謝聆聽・敬請指教 (Q&A)</div>
        <div style="font-size: 18px; color: #94a3b8; margin-top: 10px;">完整 23 篇文獻解析與計量模型已收錄於 Karpathy LLM Wiki 知識庫</div>
    </div>

    <!-- 底部控制導航 -->
    <div class="controls-bar">
        <div>
            <span id="label-cur" style="font-size: 22px; font-weight: 900; color: #2563eb;">1</span> / <span id="label-tot">26</span>
        </div>
        <div class="controls-btns">
            <button class="ctrl-pill-btn" onclick="goPrev()">◀ 上一頁 (Left)</button>
            <button class="ctrl-pill-btn" onclick="goNext()">下一頁 (Right) ▶</button>
            <button class="ctrl-pill-btn" onclick="toggleFull()">全螢幕放映 (F)</button>
        </div>
    </div>
    <div class="progress-track">
        <div class="progress-indicator" id="prog-bar"></div>
    </div>

</div>

<script>
    let curIndex = 1;
    const totalPages = 26;

    // 核心引擎：自適應等比縮放 (Scale to Fit Viewport)
    function fitViewport() {
        const vp = document.getElementById('slide-viewport');
        const targetW = 1920;
        const targetH = 1080;
        const windowW = window.innerWidth;
        const windowH = window.innerHeight;

        const scale = Math.min(windowW / targetW, windowH / targetH);
        vp.style.transform = `scale(${scale})`;
        vp.style.left = `${(windowW - targetW * scale) / 2}px`;
        vp.style.top = `${(windowH - targetH * scale) / 2}px`;
    }

    window.addEventListener('resize', fitViewport);
    window.addEventListener('load', fitViewport);

    function showPage(n) {
        if (n < 1) n = 1;
        if (n > totalPages) n = totalPages;

        document.querySelectorAll('.slide-page').forEach(p => p.classList.remove('active'));
        const target = document.getElementById('p-' + n);
        if (target) {
            target.classList.add('active');
            curIndex = n;
            document.getElementById('label-cur').innerText = n;
            const pct = ((n - 1) / (totalPages - 1)) * 100;
            document.getElementById('prog-bar').style.width = pct + '%';
        }
    }

    function goNext() {
        if (curIndex < totalPages) showPage(curIndex + 1);
    }

    function goPrev() {
        if (curIndex > 1) showPage(curIndex - 1);
    }

    function toggleFull() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(e => {});
        } else {
            if (document.exitFullscreen) document.exitFullscreen();
        }
    }

    // 鍵盤切頁
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
            goNext();
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
            goPrev();
        } else if (e.key === 'Home') {
            showPage(1);
        } else if (e.key === 'End') {
            showPage(totalPages);
        } else if (e.key === 'f' || e.key === 'F') {
            toggleFull();
        }
    });

    // 點擊翻頁
    document.getElementById('slide-viewport').addEventListener('click', function(e) {
        if (e.target.tagName !== 'BUTTON' && !e.target.closest('button') && !e.target.closest('.math-seg')) {
            const rect = this.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            if (clickX > rect.width * 0.7) {
                goNext();
            } else if (clickX < rect.width * 0.3) {
                goPrev();
            }
        }
    });

    // 公式分步點燈互動函數
    function switchMath(type) {
        const segM = document.getElementById('seg-m');
        const segF = document.getElementById('seg-f');
        const btnM = document.getElementById('btn-seg-m');
        const btnF = document.getElementById('btn-seg-f');
        const title = document.getElementById('math-title');
        const desc = document.getElementById('math-desc');
        const val = document.getElementById('math-val');

        segM.classList.remove('active-gold', 'active-blue');
        segF.classList.remove('active-gold', 'active-blue');
        btnM.classList.remove('selected');
        btnF.classList.remove('selected');

        if (type === 'm') {
            segM.classList.add('active-gold');
            btnM.classList.add('selected');
            title.style.color = '#b45309';
            val.style.color = '#b45309';
            title.innerText = '婚姻結構變動效應 (ΔM_a)：貢獻度高達 82%！';
            desc.innerText = '人口學實證分解指出：每下降 1 點生育率，超過八成來自「大家結不了婚或延後初婚」！';
            val.innerText = '82%';
        } else if (type === 'f') {
            segF.classList.add('active-blue');
            btnF.classList.add('selected');
            title.style.color = '#0284c7';
            val.style.color = '#0284c7';
            title.innerText = '婚內生育率下降效應 (ΔF_a)：貢獻度僅佔 18%！';
            desc.innerText = '夫妻結婚之後少生的影響力，其實只有不到兩成，並非少子化的主要源頭！';
            val.innerText = '18%';
        } else {
            segM.classList.add('active-gold');
            segF.classList.add('active-blue');
            title.style.color = '#0f2b5c';
            val.style.color = '#0f2b5c';
            title.innerText = 'Kitagawa 總和生育率完全分解模型';
            desc.innerText = '左項婚姻結構效應 (82%) ＋ 右項婚內生育效應 (18%) ＝ 總生育率完全變動 (100%)';
            val.innerText = '100%';
        }
    }

    // 初始化縮放與第一頁
    fitViewport();
    showPage(1);
</script>

</body>
</html>
"""

final_html = html_str.replace("###NYCU###", nycu).replace("###LOGO2###", logo2).replace("###IMAGE###", image)

with open('wiki/slides/SL-FER-TaiwanFertilityDecline.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Masterpiece Presentation HTML generated successfully!")
