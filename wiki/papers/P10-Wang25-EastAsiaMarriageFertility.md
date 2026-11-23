---
id: "P10"
title: "The East Asian Marriage Package and Delayed Nuptiality: A Comparative Demography"
authors: ["F. Wang", "H. Saito"]
year: 2025
venue: "Population and Development Review, 51(1), 89-118"
source_type: "pdf"
file_or_link: "raw/papers/P10-Wang25-EastAsiaMarriageFertility.pdf"
tags: [paper, 婚育包裹, 初婚推遲, 結構方程模型, 東亞人口學, 非婚生育]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P10] 東亞婚育包裹與初婚推遲：比較人口學研究

## 核心摘要 (Executive Summary)
* **研究核心**：透過跨國結構方程模型（SEM）與跨國人口調查，深入檢驗東亞（台灣、日本、南韓）特有的「婚育包裹（Marriage-Childbearing Package）」制度如何造成當代少子化危機。
* **婚育強捆綁特徵**：在東亞文化與法制體制下，非婚生子女率極低（台灣僅約 3.8%、南韓 2.5%、日本 2.4%，而 OECD 平均達 41.5%），使生育幾乎 100% 必須以合法婚姻為前提。
* **因果鏈分解**：路徑分析證實，少子化總變異量中高達 82% 是由「初婚推遲與不婚化」直接解釋，婚內生育率下降僅貢獻 18%。
* **制度反思**：單一傳統異性戀婚姻家庭制度的僵化包裝，已成為東亞青年逃避生育的最主要結構性制度陷阱。

## 研究背景與動機 (Background & Motivation)
西方國家在經歷第二人口轉型（Second Demographic Transition, SDT）時，雖然傳統婚姻率下降，但伴隨同居普及、伴侶法制化（如法國 PACS）與非婚生育的廣泛接受（北歐非婚生育超過 50%），生育率得以在雙軌支持下維持在 1.5 至 1.8 的平穩區間。然而東亞各國在社會轉型過程中，文化規範與法律體制依然將性行為、合法婚姻、買房置產、繁衍育兒與贍養長輩全部綑綁在「婚育大禮包」中。青年若無法承受其中任何一項（如買不起房或恐懼侍奉公婆），只能選擇「整包拒絕」。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究運用多群組結構方程模型（Multi-Group Structural Equation Modeling, MG-SEM）與因果路徑分析，模型對接概念頁 [[C-MBP-MarriagePackage]]：

$$
\begin{cases}
\eta_{\text{Marriage}} = \boldsymbol{\Gamma}_1 \mathbf{X}_{\text{Econ}} + \boldsymbol{\Gamma}_2 \mathbf{X}_{\text{Culture}} + \zeta_1 \\
\eta_{\text{Fertility}} = \beta_{21} \eta_{\text{Marriage}} + \boldsymbol{\Gamma}_3 \mathbf{X}_{\text{FamilyPolicy}} + \zeta_2
\end{cases}
$$

### 因果分解公式 (Kitagawa-Style Rate Decomposition)
$$
\Delta \text{CBR} = \underbrace{\sum_x \Delta M_x \cdot \bar{F}_x}_{\text{結婚率變動貢獻 (82.4%)}} + \underbrace{\sum_x \bar{M}_x \cdot \Delta F_x}_{\text{婚內生育率變動貢獻 (17.6%)}}
$$

### 變數與符號定義
* $\eta_{\text{Marriage}}$：初婚意願與實踐之潛在變數（由適婚年齡未婚率、初婚年齡測量）。
* $\eta_{\text{Fertility}}$：終身生育率與生育意願潛在變數。
* $\mathbf{X}_{\text{Econ}}$：經濟門檻指標（包含青年購屋負擔、薪資中位數與就業穩定度）。
* $\mathbf{X}_{\text{Culture}}$：文化性別期待指標（傳統家父長孝道期待、侍奉公婆壓力、性別角色刻板印象）。
* $\beta_{21}$：婚姻對生育的路徑傳導係數（在東亞估計值高達 +0.89***，在北歐僅 +0.24）。
* $\zeta_1, \zeta_2$：結構方程式擾動項。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：東亞社會調查（East Asian Social Survey, EASS）家庭模組、台日韓各國官方戶政與人口普查統計資料庫。
* **研究樣本**：涵蓋台灣（$N=2,150$）、日本（$N=2,300$）與南韓（$N=2,050$）20 至 44 歲成年男女，總樣本數達 6,500 份。

## 主要實證發現 (Key Empirical Findings)
結構方程路徑係數與跨國對照結果如下表所示：

| 潛在結構路徑與指標 | 東亞模型 (台日韓統合) | 歐美對照組 (OECD 典型) | 統計檢定差異 | 結構意涵 |
| :--- | :--- | :--- | :--- | :--- |
| **婚姻對生育的直接路徑 ($\beta_{21}$)** | **+0.892*** (0.024)** | **+0.245*** (0.035)** | $p < 0.001$ | 東亞生育高度依存於婚姻；歐美已實質脫鉤 |
| **經濟門檻對婚姻的負向路徑** | **-0.458*** (0.031)** | -0.182** (0.028) | $p < 0.001$ | 買房成家門檻對東亞青年的打擊尤為致命 |
| **性別傳統期待對婚姻的推力** | **-0.384*** (0.029)** | -0.065 (0.032) | $p < 0.001$ | 傳統婆媳與照護規範強烈勸退現代獨立女性 |
| **非婚生子女率 (Out-of-Wedlock Birth)** | **3.8% (台灣)** | **41.5% (OECD 平均)** | $p < 0.001$ | 東亞非婚生育受到社會與法制嚴厲排斥 |
| Kitagawa 分解：不婚對少子化之貢獻 | **82.4%** | 35.6% | $p < 0.001$ | 東亞少子化本質就是「大規模不婚化」 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：具體以跨國實證將東亞超低生育率定位為「婚育包裹制度與青年經濟/文化自主性之間的劇烈碰撞」。
* **政策意涵**：
  * 政府所有圍繞著「合法已婚夫妻」設計的生育補貼，完全無法觸及造成 82% 少子化成因的「未婚青年群體」。
  * 唯有從法制層面打破婚育包裹：承認多元伴侶關係（如民事結合法）、保障非婚生子女與單身女性合法使用人工生殖技術（IVF），才能從根本打開少子化活水。
* 關聯議題：本篇歸屬於議題 [[T-MAR-EastAsiaMarriageDecline]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **文化規範演化延遲**：本研究證實法制改革之必要性，但東亞社會對「非婚生育」之污名化觀念仍需長時間教育引導。

## 關聯文獻與引用 (Related Works)
* [[P12-Tan26-NuptialityPolicyMismatch]]：超低生育體制下的政策錯配與初婚忽視。
* [[P13-Ryu24-PronatalistInclusiveness]]：東亞促生育政策之包容性與多元制度障礙。
* [[P20-Cheng23-PremaritalRelationships]]：台灣同居率飆升但非婚生育脫鉤實證。
