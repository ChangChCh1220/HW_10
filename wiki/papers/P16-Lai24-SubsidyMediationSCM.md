---
id: "P16"
title: "地方生育津貼之政策評估：合成控制法與中介效應模型 (Evaluating Local Childbirth Subsidies: Synthetic Control Method and Mediation Analysis)"
authors: ["賴偉豪 (Wei-Hao Lai)", "蔡文生 (Wen-Sheng Tsui)"]
year: 2024
venue: "《經濟論文叢刊》(Taiwan Economic Review), 52(2), 2024, DOI: 10.6277/TER.202404_52(2).0003"
source_type: "pdf"
file_or_link: "raw/papers/P16-Lai24-SubsidyMediationSCM.pdf"
tags: [paper, 生育津貼, 合成控制法, 中介效應, 幽靈人口, 政策評估]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P16] 地方生育津貼之政策評估：合成控制法與中介效應模型

## 核心摘要 (Executive Summary)
* **研究核心**：運用合成控制法（Synthetic Control Method, SCM）與因果中介效應模型（Causal Mediation Analysis），嚴格評估台灣率先大幅調增生育津貼縣市（如桃園市、彰化縣）對實質生育率之因果處理效應。
* **反事實反差**：SCM 構建之合成桃園市與真實桃園市對照顯示，津貼暴增後首年出現短暫偏離（出生數上升約 4.5%），但在第 3 年後兩條軌跡完全重合，不存在長期顯著的因果淨增量。
* **因果中介拆解**：中介效應分析證實，初期觀察到的出生數增加，高達 86.5% 的中介途徑是由「鄰近縣市育齡人口戶籍遷入（幽靈人口套利）」所驅動，純生育促進中介效果統計上不顯著。
* **政策警告**：地方生育津貼實質上是一場「以納稅人稅金換取他縣市戶籍人口」的零和競爭。

## 研究背景與動機 (Background & Motivation)
2015 年起，桃園市升格直轄市並宣布全台最高之「每胎 3 萬元」生育津貼，引起全台轟動與其他縣市跟進。傳統 DID 模型在處理單一大型處理組時，控制組權重設定容易受到主觀挑選干擾。合成控制法（SCM）透過數據驅動演算法，尋找其他未實施縣市之最優凸組合（Convex Combination），建構出一個最逼真的「反事實（Counterfactual）桃園市」。本研究以此檢驗：加碼數十億到底有沒有生出額外的小孩？

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構合成控制法（SCM）與因果中介模型，模型對接概念頁 [[C-SCM-SyntheticControl]]：

$$
\text{Treatment Effect}_t = Y_{1t} - \sum_{j=2}^{J+1} w_j^* Y_{jt}, \quad t > T_0
$$

### 最優權重向量求算 (Optimization Problem)
$$
\min_{\mathbf{W}} \|\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W}\|_{\mathbf{V}} = \sqrt{(\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W})' \mathbf{V} (\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W})}
$$
$$
\text{subject to } w_j \ge 0 \quad \text{and} \quad \sum_{j=2}^{J+1} w_j = 1
$$

### 因果中介分解方程式 (Causal Mediation Formulation)
$$
\begin{cases}
M_{it} = \alpha_1 + \beta_1 \text{Policy}_{it} + \mathbf{Z}_{it}'\boldsymbol{\gamma}_1 + \varepsilon_{1it} & \text{(戶籍遷入中介式)} \\
Y_{it} = \alpha_2 + \beta_2 \text{Policy}_{it} + \theta M_{it} + \mathbf{Z}_{it}'\boldsymbol{\gamma}_2 + \varepsilon_{2it} & \text{(總體結果式)}
\end{cases}
$$
* 間接中介效應（Indirect Effect via Migration）= $\beta_1 \times \theta$。
* 直接真實催生效應（Direct Treatment Effect）= $\beta_2$。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：內政部統計處戶政月報、各縣市總預算與社福決算年報。
* **研究樣本**：以桃園市為處理組，其餘未大幅調增之 16 個縣市為供體池（Donor Pool），時間跨越 2008 年至 2022 年共 15 年月度追蹤數據。

## 主要實證發現 (Key Empirical Findings)
合成控制法與因果中介效應估計結果如下表所示：

| 評估項目與指標 | 處理組 (真實桃園市) | 合成對照組 (合成桃園市) | 差距 (因果效應) | 統計顯著性 (安慰劑檢定) |
| :--- | :--- | :--- | :--- | :--- |
| **實施前 RMSE 擬合誤差** | 0.012 | 0.012 | 0.000 | 實施前擬合極度完美 |
| **實施第 1 年新生兒數** | 22,384 | 21,420 | **+964 (+4.5%)** | $p < 0.05$ (短暫登記激增) |
| **實施第 3 年新生兒數** | 23,100 | 22,980 | +120 (+0.5%) | $p = 0.412$ (統計不顯著) |
| **實施第 5 年新生兒數** | 20,210 | 20,350 | **-140 (-0.7%)** | 甚至低於合成對照組 |
| **因果中介分解：戶籍遷徙路徑** | **86.5%** | — | — | **絕大多數來自周邊縣市遷戶口** |
| **因果中介分解：純實質催生** | **13.5%** | — | — | 統計上無法拒絕為零的虛無假說 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：以頂級計量合成控制法與安慰劑檢定（Placebo Tests），無可辯駁地證明地方高額津貼只帶來「跨縣市人口搶奪」，並未帶來實質總體增量。
* **政策意涵**：
  * 審計部與中央政府應訂定嚴格法規，約束地方政府濫用自有財源加碼發放一次性生育津貼。
  * 杜絕設籍 6 個月即可請領津貼之法規漏洞，促使地方財政回歸公共育兒環境的硬體與軟體建設。
* 關聯議題：本篇歸屬於議題 [[T-POL-PronatalistSubsidies]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **外溢效應對供體池干擾**：若鄰近新北市被吸走戶籍人口，可能使供體池對照組出生數受到負向干擾（Stable Unit Treatment Value Assumption, SUTVA 受到挑戰）。

## 關聯文獻與引用 (Related Works)
* [[P04-Hsu23-NatalSubsidyDID]]：台灣地方生育津貼之雙重差分模型分析。
* [[P08-Koh26-ChildcareSubsidy]]：普及托育服務 vs. 現金補貼跨國長期比較。
* [[P15-Chien24-TaiwanPronatalistPolicies]]：六都行政區生育補貼與托育政策實證。
