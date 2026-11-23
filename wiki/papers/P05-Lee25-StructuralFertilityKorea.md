---
id: "P05"
title: "Structural Estimation of Dynamic Fertility Choices and Family Allowances in South Korea"
authors: ["S. Lee", "M. Park"]
year: 2025
venue: "Journal of Population Economics, 38(1), 2025"
source_type: "pdf"
file_or_link: "raw/papers/P05-Lee25-StructuralFertilityKorea.pdf"
tags: [paper, 動態結構模型, 反事實模擬, 現金津貼, 托育服務, 韓國]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P05] 韓國動態生育抉擇與家庭津貼之結構計量估計

## 核心摘要 (Executive Summary)
* **研究核心**：建構女性跨期生命週期動態結構離散選擇模型（Dynamic Structural Discrete Choice Model），評估各類促生育政策在韓國的反事實模擬（Counterfactual Simulations）成效。
* **政策彈性估計**：結構估計顯示，現金補貼對長期生育率的彈性僅為 +0.038；政府每促成一個額外「邊際新生兒」的財政代價高達 8,400 萬韓元。
* **托育可近性之高乘數**：相對地，將公立托育設施可近性提高 20%，能使總和生育率顯著上升 0.12 個單位，且能有效維持女性就業率與人力資本累積。
* **政策核心結論**：只有能分擔女性長期育兒時間成本的制度設計，才能發揮實質反轉超低生育率之效果。

## 研究背景與動機 (Background & Motivation)
南韓政府在過去 15 年間投入超過 200 兆韓元推行促生育對策，但生育率仍逆勢崩跌至 0.72。傳統簡約式計量回歸（Reduced-form Regressions）常難以進行外推預測與反事實政策模擬，且容易受到盧卡斯批判（Lucas Critique）的挑戰。本研究透過建立並估計包含家務勞動、女性勞動供給與跨期生育決策的動態結構模型，量化評估「給錢（Cash）」與「給服務（In-kind Services）」的深層結構差異。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究奠基於动态规划逆向求解（Dynamic Programming Backward Induction），模型對接概念頁 [[C-SEM-StructuralFertility]]：

$$
V_t(S_t) = \max_{d_t \in \mathcal{D}} \left\{ U(C_t, N_t, d_t; \boldsymbol{\theta}) + \beta \mathbb{E}\left[ V_{t+1}(S_{t+1}) \mid S_t, d_t \right] \right\}
$$

### 狀態變數與抉擇集合
* 抉擇集合 $d_t \in \{0, 1\} \times \{0, 1\}$：同時決定當期是否受孕懷孕，以及女性是否參與全職就業。
* 狀態變數向量 $S_t = (\text{Age}_t, \text{Wage}_t, \text{Experience}_t, N_{t-1}, \text{ChildAge}_t, \text{HousingDebt}_t)$。
* 當期效用函數設定：
$$
U(C_t, N_t, d_t) = \frac{C_t^{1-\sigma}}{1-\sigma} + \alpha_n N_t - \psi_f \cdot \mathbf{1}(\text{Work}_t=1) - \gamma_{\text{care}} \cdot \text{ChildAge}_t \cdot \mathbf{1}(\text{PublicCare}_t=0) + \varepsilon_t(d_t)
$$
* 透過廣義極值（Generalized Extreme Value）與嵌套不動點演算法（Nested Fixed Point, NFXP）估計結構深層參數 $\boldsymbol{\theta}$。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：韓國家庭與生育調查追蹤資料庫（Korean Longitudinal Survey of Women and Families, KLoWF）2012 至 2023 年追蹤微觀數據。
* **研究樣本**：選取初次受訪時未滿 40 歲之已婚與未婚女性共 3,250 人，構建多期跨年面板路徑。

## 主要實證發現 (Key Empirical Findings)
結構模型反事實政策模擬結果如下表：

| 政策模擬情境 (Counterfactual Policy) | 總和生育率變化 ($\Delta \text{TFR}$) | 女性勞動參與率變化 | 每增加一名新生兒之政府成本 |
| :--- | :--- | :--- | :--- |
| **基準現狀 (Baseline)** | 0.78 (基準值) | 58.2% | — |
| **情境 A：現金津貼翻倍 (Double Child Allowance)** | +0.03 (微增至 0.81) | -1.8% (輕微退出職場) | 8,400 萬韓元 (約 6 萬美元) |
| **情境 B：公立托育名額增加 20%** | **+0.12 (升至 0.90)** | **+4.6% (顯著提升)** | **2,800 萬韓元 (成本效益高 3 倍)** |
| **情境 C：落實法定男性 1 個月有薪陪產育嬰假** | +0.07 (升至 0.85) | +2.1% (緩解母職中斷) | 3,200 萬韓元 |
| **情境 D：綜合方案 (B + C 組合)** | **+0.19 (升至 0.97)** | **+6.3%** | 綜合最佳化財政路徑 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：以嚴格的微觀計量結構動態模型，證實東亞育齡女性在決策時高度重視「時間機會成本」遠甚於「一次性金錢補助」。
* **政策意涵**：
  * 政府補貼現金只會造成嚴重的「死重損失（Deadweight Loss）」，錢被原本就打算生育的家庭領走，卻無法打動邊際上的猶豫族群。
  * 唯有大規模建設平價、優質、延長托育時間的公共托育體系，才能釋放女性生育潛能並穩定勞動力市場。
* 關聯議題：本篇對接核心議題 [[T-POL-PronatalistSubsidies]] 與 [[T-WFC-WorkFamilyConflict]]。

## 限制與未來研究方向 (Limitations)
* **婚姻內生化**：本模型主要關注已婚女性之生育邊際，未將未婚青年的「結婚搜尋與配對市場（Marriage Search Market）」納入完全均衡。

## 關聯文獻與引用 (Related Works)
* [[P04-Hsu23-NatalSubsidyDID]]：台灣地方生育津貼之雙重差分因果評估。
* [[P08-Koh26-ChildcareSubsidy]]：長期托育服務與現金補貼之國際跨國比較。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：新時代生育經濟學理論框架。
