---
id: "P08"
title: "Long-term Fertility Responses to Universal Childcare Services vs. Cash Subsidies"
authors: ["Y. Koh", "J. Sung"]
year: 2026
venue: "Review of Economics and Statistics, 108(2), 2026"
source_type: "pdf"
file_or_link: "raw/papers/P08-Koh26-ChildcareSubsidy.pdf"
tags: [paper, 公共托育, 現金補貼, 事件研究法, 面板IV, 經合組織]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P08] 普及托育服務與現金補貼之長期生育反應比較

## 核心摘要 (Executive Summary)
* **研究核心**：利用跨國 OECD 國家與東亞主要城市 2005 至 2024 年之政策改革，以事件研究法與面板工具變數法（Panel IV-2SLS）嚴格對比「普及公立托育」與「純現金育兒津貼」對長期總和生育率的影響路徑。
* **托育服務之持久推升力**：公共托育涵蓋率每提高 10 個百分點，總和生育率在 5 年內穩定提升 0.082***，且該正面效應持續超過 10 年不衰減。
* **現金津貼之短暫與遞減**：純現金補貼雖然在政策宣布後第 1 年帶來短暫的微幅上升（+0.015*），但在第 3 年後即衰減至零，呈現典型的邊際效用遞減與死重損失。
* **政策總結**：實物托育服務直接降低育兒的跨期時間成本，是唯一具備長期制度韌性的催生工具。

## 研究背景與動機 (Background & Motivation)
各國政府在對抗少子化時，政策工具常分化為兩大流派：一派偏好直接發放現金津貼（如台灣發放育兒津貼、韓國各地方津貼），因其行政成本低、政治選票效果立竿見影；另一派則主張重金投資公共托育設施與幼兒教育機構（如北歐模式、法國模式）。究竟哪一種工具能夠真正改變家庭的長期跨期生育規劃？本研究透過 20 年的跨國多中心準實驗政策改革進行權威檢驗。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究設定面板事件研究法（Event Study Design）與工具變數二階段最小平方法（IV-2SLS），模型對接概念頁 [[C-DID-DiffInDiff]] 與 [[C-FE-FixedEffects]]：

$$
\text{Fertility}_{ct} = \alpha_c + \delta_t + \sum_{k=-5}^5 \theta_k^{\text{Care}} \mathbf{1}(t - T_c^{\text{Care}} = k) + \sum_{k=-5}^5 \theta_k^{\text{Cash}} \mathbf{1}(t - T_c^{\text{Cash}} = k) + \mathbf{Z}_{ct}'\boldsymbol{\Gamma} + \nu_{ct}
$$

### 工具變數設定 (IV Specification)
為克服托育設施建設選址的潛在內生性，採用中央財政轉移支付改革法規作為外生工具變數 $Z_{ct}$：
$$
\text{CareCoverage}_{ct} = \pi_0 + \pi_1 Z_{ct} + \mathbf{Z}_{ct}'\boldsymbol{\Pi} + \mu_c + \tau_t + \xi_{ct}
$$

### 變數與符號定義
* $\text{Fertility}_{ct}$：國家/都會區 $c$ 於年份 $t$ 之總和生育率（TFR）。
* $T_c^{\text{Care}}$：大規模普及公共托育改革實施元年。
* $T_c^{\text{Cash}}$：大規模現金育兒津貼加碼實施元年。
* $\theta_k^{\text{Care}}, \theta_k^{\text{Cash}}$：政策實施後第 $k$ 年之動態累積處理效應。
* $\mathbf{Z}_{ct}$：跨國總體控制變數向量（人均 GDP、女性勞動力參與率、平均受教育年數、產假週數等）。
* $\alpha_c, \delta_t$：國家固定效果與年度時間固定效果。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：經合組織家庭資料庫（OECD Family Database）、世界銀行世界發展指標（WDI）、各國教育部托育統計年報。
* **研究樣本**：涵蓋 28 個 OECD 會員國及東亞 4 大經濟體（台灣、南韓、日本、新加坡），跨越 2005 年至 2024 年，共計 640 筆國家-年度觀測值。

## 主要實證發現 (Key Empirical Findings)
實證估計動態效果如下表所示：

| 實施相對期數 ($k$) | 公共托育服務處理效應 ($\theta_k^{\text{Care}}$) | 現金補貼處理效應 ($\theta_k^{\text{Cash}}$) | 統計檢定差異 |
| :--- | :--- | :--- | :--- |
| **$k = -1$ (基準前期)** | 0.000 (基準) | 0.000 (基準) | 通過事前平行趨勢檢定 |
| **$k = 0$ (實施當期)** | +0.021* (0.010) | +0.015* (0.008) | 兩者皆有初期微幅反應 |
| **$k = +1$ (實施後 1 年)** | +0.045** (0.014) | +0.012 (0.009) | 托育效應開始放大，現金減弱 |
| **$k = +3$ (實施後 3 年)** | **+0.078*** (0.018)** | **+0.003 (0.011)** | **現金效應完全歸零，托育持續增長** |
| **$k = +5$ (實施後 5 年)** | **+0.082*** (0.020)** | **-0.005 (0.012)** | **托育建立長期平衡，現金無長期效果** |
| **$k = +10$ (長期乘數)** | **+0.091*** (0.022)** | **-0.008 (0.015)** | **公共托育展現制度性穩固效果** |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：以長期跨國事件研究明確證實：「現金是一次性補償，托育是 18 年的夥伴」。現金補貼無助於降低家庭跨期育兒的不確定性。
* **政策意涵**：
  * 國家預算配置應果斷轉向，將數百億甚至千億的發錢預算，全數轉移至 0-6 歲公共托育中心、非營利幼兒園與公幼延托班。
  * 唯有將母親從全天候育兒勞動中解放出來，實現「工作與育兒相容」，才能拯救生育率。
* 關聯議題：本篇歸屬於議題 [[T-POL-PronatalistSubsidies]] 與 [[T-WFC-WorkFamilyConflict]]。

## 限制與未來研究方向 (Limitations)
* **托育品質變數**：國際聚合數據難以完全量化托育機構之師生比、評鑑等級與照護品質細節。

## 關聯文獻與引用 (Related Works)
* [[P04-Hsu23-NatalSubsidyDID]]：台灣地方生育津貼之雙重差分模型。
* [[P05-Lee25-StructuralFertilityKorea]]：韓國結構模型模擬托育服務 vs. 現金津貼。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：新時代生育經濟學與雙薪家庭支持。
* [[P15-Chien24-TaiwanPronatalistPolicies]]：台灣直轄市生育津貼與托育政策實證。
