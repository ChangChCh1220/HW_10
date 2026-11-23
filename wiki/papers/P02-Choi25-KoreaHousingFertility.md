---
id: "P02"
title: "Housing Wealth and Fertility Decisions in South Korea: Stratification and Crowding Out"
authors: ["I. Choi", "S. Kim"]
year: 2025
venue: "Asian Journal of Social Science, 53, 100221"
source_type: "pdf"
file_or_link: "raw/papers/P02-Choi25-KoreaHousingFertility.pdf"
tags: [paper, 住房資產, 財富效果, 排擠效應, 韓國, 階層分化]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P02] 韓國住房資產與生育決策：階層分化與排擠效應

## 核心摘要 (Executive Summary)
* **研究核心**：利用韓國勞動與所得面板研究（KLIPS），深入剖析房價飆漲對不同住房權屬（自有房產 vs. 全租/月租無房者）家庭生育決策的對稱與不對稱衝擊。
* **資產階級分化**：實證發現顯著的「雙峰分化」現象——有房家庭享有顯著的「財富效果」（房價上漲促進生育），而無房青年家庭面臨嚴重的「生活成本排擠效應」（房價上漲顯著推遲婚育）。
* **機制分解**：高房價實質擴大了家庭間的財富階級差距，將婚育機會向資產階層集中，加劇未婚青年的結婚絕望感。
* **政策啟示**：單純補貼難以翻轉階層差距，急需改革青年首購信用支持與長期租賃居住安定制度。

## 研究背景與動機 (Background & Motivation)
南韓總和生育率近年跌至全球最低的 0.7 左右，首爾等都會區房價高漲被指為主要禍首。然而，總體數據往往掩蓋了微觀家戶間的結構性差異。房價上升對資產階級而言是淨資產擴張與信用借貸抵押力提升；但對尚未購屋的青年世代而言，則是不可逾越的購屋障礙。本研究旨在解構韓國居住權屬如何形塑階級生育不平等。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
研究採用微觀離散選擇模型與邊際效果分解，模型對接概念頁 [[C-SEM-StructuralFertility]] 與 [[C-FE-FixedEffects]]：

$$
\Pr(\text{Birth}_{it} = 1 \mid \mathbf{X}_{it}) = \Phi\left(\alpha + \beta_1 \text{Owner}_{it} + \beta_2 \Delta \text{Price}_{ct} + \beta_3 (\Delta \text{Price}_{ct} \times \text{NonOwner}_{it}) + \mathbf{Z}_{it}'\boldsymbol{\theta} + \eta_i + \tau_t\right)
$$

### 變數與符號定義
* $\text{Birth}_{it}$：家戶 $i$ 於年度 $t$ 是否有新生兒出生之二元變數（$1 = \text{是}, 0 = \text{否}$）。
* $\text{Owner}_{it}$：家戶是否自有住宅（Homeownership Status）。
* $\Delta \text{Price}_{ct}$：縣市都會區 $c$ 之住宅價格年增率。
* $\beta_2$：測量自有住宅家庭之房產財富效果（預期 $\beta_2 > 0$）。
* $\beta_3$：交互項係數，測量無房家庭相對於有房家庭在面臨房價上漲時的排擠效應（預期 $\beta_3 < 0$）。
* $\mathbf{Z}_{it}$：微觀控制變數，包括夫妻年齡、教育程度、勞動所得、非房產金融資產與既有子女數。
* $\eta_i$：家戶個體隨機/固定效應；$\tau_t$：年度時間效應。

## 資料來源與研究樣本 (Data & Sample)
* **資料庫**：韓國勞動與所得面板研究（Korean Labor & Income Panel Study, KLIPS）第 13 至 25 次調查（2010-2022 年）。
* **分析樣本**：選取戶長或配偶年齡在 20 至 45 歲之育齡家戶，共計 4,820 個家戶、28,450 筆家戶-年度觀察值。

## 主要實證發現 (Key Empirical Findings)
實證估計結果整理如下：

| 家戶分組與變數 | 估計係數 ($\beta$) | 邊際機率效果 (ME) | 統計顯著性 | 實質經濟意涵 |
| :--- | :--- | :--- | :--- | :--- |
| **自有住房財富效果 ($\Delta \text{Price}$)** | +0.038 | +0.014 | $p < 0.05$ | 房價每漲 10%，有房夫妻生育機率微幅上升 1.4% |
| **無房家庭交互項 ($\Delta \text{Price} \times \text{NonOwner}$)** | **-0.092** | **-0.036** | **$p < 0.001$** | 無房青年面臨嚴峻生活成本排擠，生育機率顯著暴跌 |
| **無房租屋者淨效應 (Net Effect)** | **-0.054** | **-0.022** | **$p < 0.01$** | 房價每上漲 10%，無房青年家庭生子機率淨減少 2.2% |
| **教育程度（大學以上）** | +0.045 | +0.018 | $p < 0.01$ | 具人力資本與穩定就業支撐生育決策 |
| **配偶全職就業** | -0.061 | -0.024 | $p < 0.001$ | 雙薪女性在缺乏托育下產生工作家庭衝突 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：清楚驗證了東亞超低生育率體制下，房地產資產如何造成「階級生育鴻溝（Fertility Class Divide）」。
* **政策意涵**：
  * 政府在制定打炒房政策時，必須同步保護無房青年的首購平價住宅供給與全租貸款安全網。
  * 房產不平等已直接侵蝕婚姻市場，促使青年因無法負擔購屋而推遲甚至永久放棄婚姻。
* 關聯議題：本篇歸屬於議題 [[T-HOU-HousingFertility]] 與 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **全租制度獨特性**：韓國特有的全租房（Jeonse）體制與一般國家的租賃市場結構有所差異，跨國推論至台灣時需調整流動性約束假設。
* **主觀婚育期望**：KLIPS 面板數據較缺乏對未婚者「擇偶門檻期待」之直接心理測量。

## 關聯文獻與引用 (Related Works)
* [[P01-Yao24-HousePriceFertility]]：台灣縣市房價所得比對一般生育率之負向衝擊。
* [[P09-VanWijk25-TenureGroupsHousing]]：歐洲住房權屬對青年初婚與生育門檻的階級影響。
* [[P18-Lin23-HousingBeforeMarriage]]：台灣青年「先買房再成家」之門檻觀念實證。
