---
id: "P11"
title: "高工時職場、育兒支持與女性勞動供給與生育衝突 (Long Working Hours, Childcare Support, and Maternal Labor-Fertility Conflicts)"
authors: ["潘美玲 (Mei-Ling Pan)", "張晉芬 (Chin-Fen Chang)"]
year: 2026
venue: "《台灣社會學》(Taiwanese Sociology), 48, 115-162"
source_type: "pdf"
file_or_link: "raw/papers/P11-Pan26-WorkFamilyClash.pdf"
tags: [paper, 高工時, 雙變量Probit, 母職懲罰, 職場衝突, 台灣]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P11] 高工時職場、育兒支持與女性勞動供給與生育衝突

## 核心摘要 (Executive Summary)
* **研究核心**：利用台灣婦女婚育與就業調查資料庫，以雙變量 Probit 模型（Bivariate Probit）檢驗台灣典型的高工時、常態加班職場文化對已婚育齡女性「維持全職就業」與「生育二胎決策」之雙重擠壓。
* **高工時之毀滅性打擊**：實證顯示，每週工作時數超過 44 小時之女性，生第二胎的機率顯著暴跌 38.5%（$p < 0.001$）；工時每增加 1 小時，母職衝突指數上升 14.2%。
* **母職懲罰實證**：女性在生育第一胎後，經歷升遷凍結與實質薪資成長落後之「母職懲罰（Motherhood Penalty）」高達 22.4%。
* **政策警訊**：不縮減不合理的職場長工時、不推行友善彈性工時，任何育兒津貼都無法阻止女性在「保住飯碗」與「生第二胎」之間選擇放棄生育。

## 研究背景與動機 (Background & Motivation)
台灣職場以長工時與高強度著稱，年均總工時在 OECD 國家中名列前茅（超過 2,000 小時）。與此同時，當代女性多受過高等教育，普遍期望在職場中追求職涯成就並維持經濟獨立。然而，當職場文化依然默認員工必須隨時待命加班，且公共托育在傍晚 5 點即要求接送時，全職職業婦女陷入了嚴重的「時間赤字（Time Deficit）」。本研究旨在因果量化高工時職場如何直接催化女性的婚內二胎生育罷工。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構聯立雙變量 Probit 計量模型（Bivariate Probit Model with Endogenous Regressors），模型對接概念頁 [[C-LOGIT-RandomEffectsLogit]] 與 [[C-HWT-HouseworkDivision]]：

$$
\begin{cases}
Y_{1i}^* = \mathbf{X}_{1i}'\boldsymbol{\beta}_1 + \gamma_1 \text{WorkHours}_{i} + \varepsilon_{1i} & \text{(全職就業選擇方程式)} \\
Y_{2i}^* = \mathbf{X}_{2i}'\boldsymbol{\beta}_2 + \gamma_2 \text{WorkHours}_{i} + \delta \text{OvertimeCulture}_{i} + \varepsilon_{2i} & \text{(二胎生育意願方程式)}
\end{cases}
$$

### 擾動項聯立相關設定
$$
\begin{pmatrix} \varepsilon_{1i} \\ \varepsilon_{2i} \end{pmatrix} \sim \mathcal{N}_2 \left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix} \right)
$$
* $Y_{1i} = \mathbf{1}(Y_{1i}^* > 0)$：女性是否持續參與全職勞動市場。
* $Y_{2i} = \mathbf{1}(Y_{2i}^* > 0)$：已育一胎女性是否打算生育第二胎。
* $\rho$：兩方程式殘差相關係數，若 $\rho \ne 0$ 說明就業與生育決策存在共同之未觀察異質性（如生涯抱負或家庭取向）。
* $\text{WorkHours}_i$：受訪女性平均每週實質工作時數（含常態打卡後無償加班）。
* $\text{OvertimeCulture}_i$：所屬公司部門是否具備「主管未走不能走」之加班文化虛擬變數。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：行政院主計總處與勞動部「婦女婚育與就業調查」微觀數據資料庫。
* **研究樣本**：選取 25 至 44 歲、已婚、育有一名 6 歲以下子女之全職與兼職受僱女性共計 3,420 筆代表性樣本。

## 主要實證發現 (Key Empirical Findings)
雙變量 Probit 模型實證估計結果如下表所示：

| 變數名稱 | 就業方程式 ($\boldsymbol{\beta}_1$) | 二胎生育方程式 ($\boldsymbol{\beta}_2$) | 邊際機率效應 (ME) | 實質意涵 |
| :--- | :--- | :--- | :--- | :--- |
| **常態週工時 $\ge 44$ 小時** | +0.412*** (0.045) | **-0.485*** (0.052)** | **-0.385*** (0.041)** | 長工時全職女性生二胎機率淨減少 38.5% |
| **公司常態加班文化** | +0.125** (0.038) | **-0.320*** (0.044)** | **-0.242*** (0.035)** | 加班文化直接摧毀家庭育兒時間規劃 |
| **公司提供彈性工時/遠距** | +0.218*** (0.042) | **+0.285*** (0.048)** | **+0.198*** (0.036)** | 彈性工作制顯著緩解母職時間衝突 |
| **企業托兒/延長公托支持** | +0.185** (0.051) | **+0.264*** (0.054)** | **+0.182*** (0.039)** | 解決下班延時接送痛點，拉抬二胎意願 |
| 殘差相關係數 $\rho$ | **-0.342*** (0.048)** | — | $p < 0.001$ | 證實就業與生育在當前體制下存在強烈負向替代 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：克服了單一方程式估計的內生選樣偏誤，嚴謹證明長工時是導致台灣職業婦女二胎生育意願崩解的結構性阻力。
* **政策意涵**：
  * 「工時改革就是最好的生育政策」：勞檢必須嚴格杜絕隱性無償加班，推動每週 40 小時工時落實。
  * 法律應強制賦予育有 3 歲以下幼兒的雙薪父母「每日減少 1 小時工時」或「每週 1-2 天居家遠距辦公」的法定請求權。
* 關聯議題：本篇歸屬於議題 [[T-WFC-WorkFamilyConflict]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **男性工時之交互作用**：未婚或已婚男性配偶之長工時對家庭育兒的缺席效應，未來可結合夫妻對偶數據（Dyadic Data）深入探討。

## 關聯文獻與引用 (Related Works)
* [[P06-Lin23-HouseworkImbalance]]：家務分工不對稱與女性婚內二胎生育意願。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：工作家庭相容性與新時代生育經濟學。
* [[P17-Yen24-TaiwanMarriageLogit]]：工時與薪資對台灣男女初婚機率之不對稱影響。
