---
id: "P09"
title: "Housing Tenure, Wealth Accumulation, and Family Formation among Young Adults"
authors: ["D. Van Wijk", "C. Bolt"]
year: 2025
venue: "Housing Studies, 40(3), 412-435"
source_type: "pdf"
file_or_link: "raw/papers/P09-VanWijk25-TenureGroupsHousing.pdf"
tags: [paper, 住宅權屬, 青年成家, 競爭風險模型, 租屋貧窮, 歐洲調查]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P09] 住房權屬、財富積累與青年家庭形成

## 核心摘要 (Executive Summary)
* **研究核心**：利用歐盟所得與生活狀況調查（EU-SILC）縱向追蹤微觀數據，以競爭風險生存分析模型（Competing Risks Cox Model）探討青年時期不同的住房權屬（自有、私人租賃、社會住宅）如何制約初婚與初育之時程。
* **租屋族的成家劣勢**：實證顯示，相較於擁有自有產權的青年，長期處於私人租賃市場的青年進入初婚的風險比（Hazard Ratio）僅為 0.58***，初育風險比為 0.62***。
* **居住不穩定性的心理抑制**：高昂租金支出造成青年財富累積停滯，加上不穩定的租約與房東任意驅離風險，形成嚴重的「成家防禦機制」。
* **政策啟示**：租屋黑市合法化、長期租約保障以及充足的社會住宅，是解決青年遲婚不可或缺的制度基石。

## 研究背景與動機 (Background & Motivation)
在當代已開發國家中，房價相對於青年實質薪資大幅飆漲，使得「購屋成家」成為越來越難企及的夢想。越來越多千禧世代與 Z 世代被迫長期滯留於租賃市場，被學界稱為「租屋世代（Generation Rent）」。傳統社會學認為成家需要一定的物質基礎與居住安定感。本研究透過追蹤不同歐洲福利體系下的青年生命歷程，檢驗居住權屬的階級分化如何重塑現代婚姻與生育門檻。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構原因特定競爭風險比例風險模型（Cause-Specific Competing Risks Cox Proportional Hazards Model），模型對接概念頁 [[C-SEM-StructuralFertility]]：

$$
h_m(t \mid \mathbf{X}_{it}) = h_{0m}(t) \exp\left( \boldsymbol{\beta}_m' \mathbf{X}_{it} + \gamma_m \text{Tenure}_{it} + \delta_m \text{HousingCostBurden}_{it} \right), \quad m \in \{\text{Marriage}, \text{Childbirth}\}
$$

### 變數與符號定義
* $h_m(t \mid \mathbf{X}_{it})$：個體 $i$ 在時間 $t$ 發生第 $m$ 種家庭形成事件（初婚或首次生育）之條件風險率（Hazard Rate）。
* $h_{0m}(t)$：未指定的基準風險函數（Baseline Hazard Function）。
* $\text{Tenure}_{it}$：核心解釋變數，包含：
  * 自有產權（Homeownership，基準組）。
  * 私人市場租賃（Private Renting）。
  * 社會住宅/公共租賃（Social Housing）。
  * 與父母同住（Living with Parents）。
* $\text{HousingCostBurden}_{it}$：住房負擔過重指標（租金或房貸支出佔家戶所得超過 40% 之虛擬變數）。
* $\mathbf{X}_{it}$：隨時間變動之協變量向量（年齡、教育程度、勞動就業狀態、伴侶關係狀態）。
* 估計方法：偏概似估計法（Partial Likelihood Estimation），並以 Robust 標準誤處理家戶群聚。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：歐盟所得與生活狀況調查（EU Statistics on Income and Living Conditions, EU-SILC）縱向面板資料庫（2012-2022 年）。
* **研究樣本**：選取初次進入樣本時年齡在 20 至 35 歲之未婚且無子女青年共 18,650 人，累計追蹤超過 72,000 個人-年度觀測值。

## 主要實證發現 (Key Empirical Findings)
生存分析風險比（Hazard Ratios, HR）估計結果如下表：

| 住房狀態與指標 | 初婚事件風險比 (HR) | 首次生育事件風險比 (HR) | 統計顯著性 | 實質意涵說明 |
| :--- | :--- | :--- | :--- | :--- |
| **自有產權住宅 (基準參照組)** | 1.000 | 1.000 | — | 基準對照組 |
| **私人租賃市場青年** | **0.582*** (0.038) | **0.621*** (0.041) | **$p < 0.001$** | 私人租屋者初婚風險比大減 42%，初育減 38% |
| **社會住宅承租者** | 0.814** (0.052) | 0.845** (0.055) | $p < 0.01$ | 具租約穩定保障，抑制程度遠小於私人租屋 |
| **與父母同住者** | **0.421*** (0.031) | **0.315*** (0.028) | **$p < 0.001$** | 缺乏獨立生活空間，婚育進程最為遲緩 |
| **房租負擔過重 (>40% 所得)** | **0.695*** (0.045) | **0.648*** (0.042) | **$p < 0.001$** | 嚴重租金排擠造成儲蓄赤字，延後成家 |
| **全職穩定就業** | 1.450*** (0.062) | 1.380*** (0.058) | $p < 0.001$ | 穩定經濟就業對成家具顯著促進效果 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：以多國微觀長程追蹤數據，實證揭示住房權屬如何成為當代青年成家的「第一道階級分水嶺」。
* **政策意涵**：
  * 房價過高推升租屋需求，若租賃市場缺乏租期保障（如台灣租屋黑市普遍、租約一年一簽、禁止設籍與報稅），青年便不敢貿然成家。
  * 解決青年少子化，必須將「租屋權利法制化」與「普及社會住宅」列為與育兒津貼同等重要的國家級人口政策。
* 關聯議題：本篇歸屬於議題 [[T-HOU-HousingFertility]] 與 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **制度脈絡差異**：歐洲社會福利國家（如德國、荷蘭）之租屋保障體系較健全，若將模型置於台灣或韓國等東亞高自有率社會，租屋青年的邊緣化程度恐更為嚴重。

## 關聯文獻與引用 (Related Works)
* [[P01-Yao24-HousePriceFertility]]：台灣房價所得比對一般生育率之負向效應。
* [[P02-Choi25-KoreaHousingFertility]]：韓國住房資產財富效果與無房者排擠效應。
* [[P18-Lin23-HousingBeforeMarriage]]：台灣青年「先有房再結婚」之社會態度調查。
