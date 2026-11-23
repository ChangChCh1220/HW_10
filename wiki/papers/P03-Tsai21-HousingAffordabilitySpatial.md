---
id: "P03"
title: "臺灣住宅負擔能力對生育率之影響：空間計量模型之應用 (The Impact of Housing Affordability on Fertility Rate in Taiwan: Application of Spatial Econometrics Models)"
authors: ["蔡善明 (Shan-Ming Tsai)", "指導教授：黃智聰 (Chi-Chung Huang)"]
year: 2021
venue: "國立政治大學行政管理碩士學程學位論文"
source_type: "pdf"
file_or_link: "raw/papers/P03-Tsai21-HousingAffordabilitySpatial.pdf"
tags: [paper, 住宅負擔能力, 生育率, 空間杜賓模型, 空間外溢效果, 台灣縣市]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P03] 臺灣住宅負擔能力對生育率之影響：空間計量模型之應用

## 核心摘要 (Executive Summary)
* **研究核心**：探討台灣縣市層級住宅負擔能力（房價所得比與房貸負擔率）對粗出生率之影響，運用空間杜賓模型（SDM）分解直接效果與鄰近縣市空間外溢效果。
* **實證發現（總體直接與間接）**：房價所得比直接效果為 1.184***、空間間接溢出效果為 1.452***、總效果為 2.636***；顯示在特定總體控制下，經濟熱絡帶動的房市指標與生育存在複雜的區域共動性。
* **社會人口變數的決定性衝擊**：女性勞動參與率總效果達 -0.731***、扶老比總效果為 -4.840***、人口密度為 -0.040***；而粗結婚率總效果高達 +4.454***。
* **核心意涵**：婚姻與照護負擔對台灣生育率具壓倒性影響，且人口與經濟變數在縣市地理空間上呈現高度正向空間自相關。

## 研究背景與動機 (Background & Motivation)
台灣各縣市之間由於高鐵、捷運與國道路網發達，形成了緊密的區域一日生活圈。某一縣市的房價暴漲（例如雙北市），可能促使年輕人口外溢遷移至鄰近縣市（例如桃園市或新竹縣市）成家育兒。若傳統計量模型忽視空間自相關（Spatial Autocorrelation）與空間溢出（Spatial Spillover），將導致估計係數偏誤。本研究運用空間計量模型，完整捕捉台灣縣市間生育率與房市負擔的空間外溢結構。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構空間杜賓面板模型（Spatial Durbin Model, SDM），模型對接概念頁 [[C-SDM-SpatialDurbin]]：

$$
Y_{it} = \rho \sum_{j=1}^N W_{ij} Y_{jt} + \beta X_{it} + \sum_{j=1}^N W_{ij} X_{jt} \theta + \mu_i + \lambda_t + \varepsilon_{it}
$$

### 效應分解矩陣 (Direct, Indirect, Total Effects)
$$
\mathbf{S}_r(\mathbf{W}) = (\mathbf{I}_N - \rho \mathbf{W})^{-1} (\mathbf{I}_N \beta_r + \mathbf{W} \theta_r)
$$
* 直接效果（Direct Effect）：矩陣對角線元素之平均值，代表本縣市自變數變動對本縣市生育率之影響。
* 間接效果（Indirect / Spillover Effect）：矩陣非對角線元素橫列或直行之平均值，代表鄰近縣市外溢至本縣市之影響。
* 總效果（Total Effect）= 直接效果 + 間接效果。

### 變數與符號定義
* $Y_{it}$：縣市 $i$ 於第 $t$ 期之粗出生率（Crude Birth Rate, CBR）。
* $\mathbf{W}$：空間權重矩陣（以地理相鄰鄰接矩陣 Contiguity Matrix 或反距離平方矩陣 Inverse Distance Matrix 設定並進行列標準化）。
* $\rho$：空間自回歸係數（Spatial Autoregressive Coefficient），檢驗生育率是否存在空間群聚。
* $X_{it}$：住宅負擔指標（房價所得比 PIR、貸款負擔率）與社會經濟控制變數。
* $\theta$：外生空間滯後項係數（Spatially Lagged Independent Variables）。
* $\mu_i, \lambda_t$：縣市與年度雙向固定效果。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：內政部不動產資訊平台、內政部戶政司人口統計資料、主計總處縣市總體統計資料庫。
* **研究樣本**：台灣本島 20 縣市（含直轄市與一般縣市），涵蓋 2006 年至 2019 年之年度空間面板數據，共計 280 筆縣市-年度觀測值。

## 主要實證發現 (Key Empirical Findings)
空間杜賓模型效果分解實證結果如下表：

| 變數名稱 | 直接效果 (Direct) | 間接效果 (Indirect/Spillover) | 總效果 (Total Effect) | 顯著性水準 |
| :--- | :--- | :--- | :--- | :--- |
| **粗結婚率 ($\text{CMR}$)** | **+2.135*** | **+2.319*** | **+4.454*** | $p < 0.001$ (最關鍵正向拉力) |
| **房價所得比 ($\text{PIR}$)** | +1.184*** | +1.452*** | +2.636*** | $p < 0.001$ (區域繁榮與選樣聯動) |
| **女性勞參率 ($\text{FLFP}$)** | -0.320** | -0.411*** | **-0.731*** | $p < 0.001$ (工作家庭雙重壓力) |
| **扶老比 ($\text{OldRatio}$)** | -2.140*** | -2.700*** | **-4.840*** | $p < 0.001$ (高齡少子化結構沉重) |
| **人口密度 ($\text{Density}$)** | -0.018** | -0.022** | **-0.040*** | $p < 0.01$ (都會擁擠排擠生育) |
| **空間滯後係數 $\rho$** | — | — | **+0.342*** | $p < 0.001$ (顯著空間正向自相關) |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：突破傳統面板模型假設各縣市相互獨立之盲點，證明台灣生育率具有強烈的區域空間外溢效應（$\rho = +0.342^{***}$）。
* **政策意涵**：
  * 少子化對策不能「各自為政」：都會核心區（如台北市）的高生活成本會直接外溢衝擊周邊蛋白區。
  * 應推動跨縣市區域生活圈育兒合作平台，統籌托育、社宅與捷運通勤月票。
* 關聯議題：本篇歸屬於議題 [[T-HOU-HousingFertility]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **空間權重矩陣設定敏感性**：地理鄰接矩陣無法完全捕捉跨縣市高鐵通勤等非實體相鄰之「經濟距離」。
* 可進一步導入動態空間面板模型（Dynamic Spatial Panel Model）以納入時間遞延落後項。

## 關聯文獻與引用 (Related Works)
* [[P01-Yao24-HousePriceFertility]]：台灣縣市房價所得比之固定效果模型分析。
* [[P07-Wu25-TaiwanCityFertility]]：都市化、密度與台灣縣市生育率之系統 GMM 估計。
* [[P15-Chien24-TaiwanPronatalistPolicies]]：六都行政區生育補貼與托育政策評估。
