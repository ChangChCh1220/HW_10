---
id: "P07"
title: "都市化、居住密度與區域生育率變遷：台灣縣市縱橫分析 (Urbanization, Residential Density, and Regional Fertility Changes in Taiwan)"
authors: ["吳宗憲 (Tsung-Hsien Wu)", "黃淑玲 (Shu-Ling Huang)"]
year: 2025
venue: "《都市與計劃》(City and Planning), 52(1), 1-32"
source_type: "pdf"
file_or_link: "raw/papers/P07-Wu25-TaiwanCityFertility.pdf"
tags: [paper, 都市化, 人口密度, 系統GMM, 空間集聚, 台灣縣市]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P07] 都市化、居住密度與區域生育率變遷：台灣縣市縱橫分析

## 核心摘要 (Executive Summary)
* **研究核心**：運用 2000 至 2023 年台灣 22 縣市跨越 24 年之總體縱橫面板數據，採用動態系統 GMM 模型（System GMM）探討都市空間密度與生活成本對生育率之長期動態影響。
* **高密度之抑制效應**：實證確認居住人口密度對總和生育率具有長期負向衝擊（長期乘數達 -0.215**），高密度都市生活引發的生活空間狹隘與高競爭壓力形成天然避孕器。
* **慣性滯後性**：前期總和生育率係數達 +0.648***，說明生育行為具有強烈的代際文化慣性與路徑依賴（Path Dependency）。
* **國土規劃啟示**：過度集中於雙北等超級大都會區的單核發展模式，是加劇少子化的空間結構元兇。

## 研究背景與動機 (Background & Motivation)
傳統人口經濟學多關注個人所得或政府補貼，但都市地理學指出「空間型態（Spatial Form）」本身即對生育行為產生決定性制約。都會區雖然聚集了最優質的就業機會與醫療教育資源，但也伴隨極高的人口密度、微型化的居住坪數、擁擠的交通與極高的生活競賽焦慮。本研究運用長達 24 年的縣市平衡面板數據，克服時間序列自相關與內生性問題，評估台灣都市化進程對生育率的長期擠壓代價。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建立動態面板系統 GMM 模型（System GMM，Blundell-Bond 估計量），模型對接概念頁 [[C-FE-FixedEffects]]：

$$
\text{TFR}_{it} = \alpha \text{TFR}_{i,t-1} + \beta_1 \ln(\text{Density}_{it}) + \beta_2 \ln(\text{HP}_{it}) + \beta_3 \text{FLFP}_{it} + \mathbf{Z}_{it}'\boldsymbol{\gamma} + \mu_i + \lambda_t + \varepsilon_{it}
$$

### 長期乘數計算 (Long-Run Multiplier)
因模型包含被解釋變數落後一期 $\text{TFR}_{i,t-1}$，各變數之長期邊際效應計算公式為：
$$
\text{Long-Run Effect of } X = \frac{\beta_k}{1 - \alpha}
$$

### 變數與符號定義
* $\text{TFR}_{it}$：縣市 $i$ 於年度 $t$ 之總和生育率（Total Fertility Rate）。
* $\text{TFR}_{i,t-1}$：落後一期生育率，捕捉生育決策的動態調整與社會慣性。
* $\text{Density}_{it}$：人口密度（每平方公里人口數，取對數）。
* $\text{HP}_{it}$：都市平均房價水準。
* $\text{FLFP}_{it}$：女性勞動力參與率。
* $\mathbf{Z}_{it}$：控制變數，包括每人可支配所得、幼兒托育機構數、失業率等。
* 檢定統計量：Arellano-Bond AR(2) 殘差無二階自相關檢定，以及 Hansen 儀校過度識別限制檢定。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：內政部戶政司人口統計年報、主計總處都市與縣市重要統計指標、內政部國土測繪中心。
* **研究樣本**：涵蓋台灣 22 縣市（含直轄市、縣與省轄市），時間範圍為 2000 年至 2023 年，總計 528 筆跨年面板觀測值。

## 主要實證發現 (Key Empirical Findings)
系統 GMM 估計結果如下表所示：

| 變數名稱 | 短期係數 ($\beta$) | 長期邊際乘數 ($\frac{\beta}{1-\alpha}$) | 統計顯著性 |
| :--- | :--- | :--- | :--- |
| **落後一期生育率 ($\text{TFR}_{t-1}$)** | **+0.648*** | — | $p < 0.001$ (強大動態慣性) |
| **人口密度 ($\ln \text{Density}$)** | **-0.076** | **-0.215** | **$p < 0.01$ (高密度顯著抑制生育)** |
| **房價水準 ($\ln \text{HP}$)** | -0.038* | -0.108* | $p < 0.05$ |
| **女性勞動參與率 ($\text{FLFP}$)** | -0.024* | -0.068* | $p < 0.05$ |
| **每萬人托育機構數** | +0.019** | +0.054** | $p < 0.01$ |
| Hansen J 檢定 $p$ 值 | 0.285 (無過度識別問題) | — | 儀校變數設定有效 |
| AR(2) 自相關檢定 $p$ 值 | 0.412 (無二階序列相關) | — | 殘差無自相關 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：以 24 年跨度的大型動態面板，成功分離出人口密度對生育率的長期乘數效應（-0.215**）。
* **政策意涵**：
  * 改善少子化必須跳脫單一補助思維，融入「國土多核心均衡發展」與「都會降密度」策略。
  * 透過遠距辦公支持、高鐵生活圈衛星城市打造與宜居綠帶規劃，舒緩年輕家庭在超大型核心都市的生存窒息感。
* 關聯議題：本篇歸屬於議題 [[T-HOU-HousingFertility]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **鄉鎮尺度異質性**：以縣市為單位可能平滑化了都會區核心（如大安區、板橋區）與外圍偏鄉的極端密度落差。

## 關聯文獻與引用 (Related Works)
* [[P01-Yao24-HousePriceFertility]]：台灣縣市房價與生育率固定效果實證。
* [[P03-Tsai21-HousingAffordabilitySpatial]]：台灣住宅負擔能力之空間杜賓模型分析。
* [[P09-VanWijk25-TenureGroupsHousing]]：不同居住權屬在都市中的婚育階層化。
