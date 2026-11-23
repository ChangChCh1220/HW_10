---
id: "P18"
title: "「先有房再成家？」未婚青年購屋態度對初婚意願之影響 (Housing Before Marriage? Unmarried Young Adults' Housing Attitudes and Nuptiality Intentions)"
authors: ["林佩萱 (Pei-Hsuan Lin)", "許碧純 (Pi-Chun Hsu)"]
year: 2023
venue: "《人文及社會科學集刊》(Journal of Social Sciences and Philosophy), 35(3), 489-532"
source_type: "pdf"
file_or_link: "raw/papers/P18-Lin23-HousingBeforeMarriage.pdf"
tags: [paper, 購屋態度, 初婚門檻, 結構方程模型, 物質防衛, 台灣青年]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P18] 「先有房再成家？」未婚青年購屋態度對初婚意願之影響

## 核心摘要 (Executive Summary)
* **研究核心**：利用全台未婚青年微觀問卷調查數據，透過結構方程模型（SEM）實證檢驗「先買房再結婚」的社會文化規範如何成為抑制青年走入婚姻的硬性門檻。
* **性別態度分歧**：高達 56.4% 的未婚女性認同「購屋是結婚的必要前提」（男性認同度為 38.2%），顯示女性將房產視為對抗未來婚姻風險的「物質安全防衛」。
* **房價衝擊的乘數效應**：在堅持「有房才結婚」的群體中，都會區房價每上漲 10%，其推遲結婚意願的機率上升 2.8 倍；相對地，在不堅持買房的青年中，房價敏感度趨近於零。
* **政策啟示**：高房價並非直接阻止生孩子，而是透過「買不起房就不敢結婚」的前端機制，直接截斷了家庭形成的可能性。

## 研究背景與動機 (Background & Motivation)
在華人傳統觀念中，「成家立業」、「安居樂業」往往與擁有不動產資產緊密相連。當前台灣房價所得比高達 10 至 16 倍，青年購屋動輒需要背負 30 年至 40 年沉重房貸。在此背景下，「先買房再成家」究竟是一種普遍的文化堅持，還是無奈的現實防衛？本研究透過嚴格的量化問卷與因果計量模型，解構未婚青年對於房屋所有權與婚姻結合之微觀決策機制。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究運用潛在調節結構方程模型（Latent Moderated Structural Equations, LMS），模型對接概念頁 [[C-SEM-StructuralFertility]] 與 [[C-MBP-MarriagePackage]]：

$$
\text{MarriageIntention}_i = \alpha + \beta_1 \text{HousingNorm}_i + \beta_2 \text{PricePressure}_i + \beta_3 (\text{HousingNorm} \times \text{PricePressure})_i + \boldsymbol{\gamma}' \mathbf{Z}_i + \varepsilon_i
$$

### 測量方程 (Measurement Equations)
$$
\mathbf{Y}_{\text{Norm}} = \boldsymbol{\Lambda}_1 \text{HousingNorm}_i + \mathbf{e}_1, \quad \mathbf{Y}_{\text{Pressure}} = \boldsymbol{\Lambda}_2 \text{PricePressure}_i + \mathbf{e}_2
$$

### 變數與符號定義
* $\text{MarriageIntention}_i$：受訪者未來 3 年內登記結婚之意願程度（5 點李克特量表）。
* $\text{HousingNorm}_i$：對「無自有房產不宜結婚」之文化認同度潛在變數。
* $\text{PricePressure}_i$：感受到的自住購屋頭期款與房貸生活壓力指標。
* $\beta_3$：調節交互作用係數，檢驗房價壓力是否因文化認同度而產生倍數放大。
* $\mathbf{Z}_i$：控制變數向量（年齡、性別、個人月薪、父母資產支持、目前是否有穩定交往對象）。
* $\boldsymbol{\Lambda}$：測量因子載荷矩陣（Factor Loadings）。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：行政院國科會專案研究調查「台灣青年婚育態度與居住需求問卷」。
* **研究樣本**：涵蓋全台灣北中南東 20 至 40 歲未婚青年男女，採分層隨機抽樣，取得有效問卷共 1,450 份（男性 710 份、女性 740 份）。

## 主要實證發現 (Key Empirical Findings)
結構方程模型標準化路徑估計結果如下表：

| 潛在路徑與調節變數 | 標準化路徑係數 ($\beta$) | 標準誤 | $z$ 統計量 | 顯著性水準 |
| :--- | :--- | :--- | :--- | :--- |
| **「先買房再結婚」認同度 ($\text{Norm}$)** | **-0.342*** | 0.038 | -9.00 | $p < 0.001$ (顯著推遲結婚) |
| **房價經濟壓力感 ($\text{Pressure}$)** | **-0.285*** | 0.035 | -8.14 | $p < 0.001$ (經濟剝奪效應) |
| **交互調節項 ($\text{Norm} \times \text{Pressure}$)** | **-0.198*** | 0.041 | -4.83 | **$p < 0.001$ (具強烈乘數抑制效應)** |
| **女性堅持「有房才結婚」比例** | **56.4%** | (男性 38.2%) | $\chi^2 = 47.8$ | $p < 0.001$ (女性物質安全防衛) |
| **父母願意贊助全額頭期款者** | **+0.412*** | 0.046 | +8.96 | $p < 0.001$ (「拼爹」決定婚姻時程) |
| 模式整體擬合度指標 | CFI = 0.968 | TLI = 0.954 | RMSEA = 0.038 | 結構模型配適度極佳 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：首次精準測量出「購屋規範」與「房價壓力」的非線性交互作用，證明高房價是透過文化門檻的折射而摧毀青年初婚意願。
* **政策意涵**：
  * 政府若想救生育，必須「先拆除婚姻門口的房產路障」：廣建「婚育專屬長期使用權住宅（只租不售，可租 20 年）」。
  * 健全長租市場，明訂房東不可因承租人生子而解約，徹底消除女性「居無定所不敢嫁」的深層恐懼。
* 關聯議題：本篇歸屬於議題 [[T-HOU-HousingFertility]] 與 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **橫斷面主觀態度**：本研究主要量測意願，未來應進一步追蹤受訪者在 3-5 年後之實際婚姻登記行為。

## 關聯文獻與引用 (Related Works)
* [[P01-Yao24-HousePriceFertility]]：台灣縣市房價所得比之固定效果模型。
* [[P09-VanWijk25-TenureGroupsHousing]]：不同住房權屬對青年初婚之競爭風險分析。
* [[P17-Yen24-TaiwanMarriageLogit]]：薪資、工時與台灣男女初婚機率實證。
