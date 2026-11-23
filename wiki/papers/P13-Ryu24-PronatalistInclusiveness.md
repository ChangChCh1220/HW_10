---
id: "P13"
title: "Unravelling Variations in 21st Century East Asian Pronatalist Family Policy Through the Lens of Inclusiveness"
authors: ["S. Ryu", "M. Kim"]
year: 2024
venue: "Journal of European Social Policy, 34(4), 380-396"
source_type: "pdf"
file_or_link: "raw/papers/P13-Ryu24-PronatalistInclusiveness.pdf"
tags: [paper, 制度包容性, 政策比較, fsQCA, 多元家庭, 東亞體制]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P13] 從包容性視角解構 21 世紀東亞促生育家庭政策的制度變異

## 核心摘要 (Executive Summary)
* **研究核心**：運用模糊集定性比較分析（fsQCA），以「制度包容性（Institutional Inclusiveness）」為核心分析維度，比較東亞（台灣、南韓、日本）與 OECD 歐洲國家在家庭政策上的構型差異。
* **包容性不足的制度死穴**：東亞促生育政策長年深陷「排他性家庭主義（Exclusive Familism）」——各項育兒補助、稅收減免、人工生殖與育嬰假權利，嚴格限縮於「異性戀合法已婚夫妻」。
* **成功構型條件**：fsQCA 條件充分性分析表明，「高托育公共化」結合「非婚生與同居伴侶權利平權」是國家成功將總和生育率維持在 1.5 以上的必要核心構型（Consistency = 0.94）。
* **改革方向**：若不打破制度歧視、將非婚生家庭、單親家庭與同志伴侶納入完整福利保護網，東亞少子化將無解。

## 研究背景與動機 (Background & Motivation)
在福利國家體制理論中，東亞常被歸類為「發達型儒家家庭福利體制（Confucian Familialism）」，其核心特徵是國家假定家庭是福利的主要提供者，且國家政策具有極高的道德排他性。當非傳統家庭型態（如事實同居、未婚生子、單親撫養）在現代青年中大幅增加時，現行法律制度卻將其視為社會偏差，甚至在法律與社會保險上處處設限。本研究運用 QCA 方法，探討制度包容性對跨國生育率復甦的決定性機制。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究運用模糊集定性比較分析（Fuzzy-Set Qualitative Comparative Analysis, fsQCA），模型對接概念頁 [[C-MBP-MarriagePackage]]：

$$
\text{TFR\_Recovery} = f(\text{ParentalLeave}, \text{ChildcareCoverage}, \text{SingleParentSupport}, \text{CohabitationRights})
$$

### 布林代數真值表最小化化簡 (Boolean Truth Table Minimization)
$$
\text{High\_Fertility} = (\text{Childcare} \cdot \text{CohabitationRights}) + (\text{ParentalLeave} \cdot \text{SingleParentSupport} \cdot \text{Childcare})
$$
* 一致性指標（Consistency Index）：
$$
\text{Consistency}(\mathbf{X} \le \mathbf{Y}) = \frac{\sum \min(X_i, Y_i)}{\sum X_i}
$$
* 覆蓋率指標（Coverage Index）：
$$
\text{Coverage}(\mathbf{X} \le \mathbf{Y}) = \frac{\sum \min(X_i, Y_i)}{\sum Y_i}
$$

### 變數與賦值校準 (Calibration)
* $\text{Childcare}$：0-3 歲公共托育服務涵蓋率（校準門檻：40% 為完全隸屬 1.0）。
* $\text{CohabitationRights}$：同居伴侶與非婚生子女享有與婚生同等法定權利之程度（法制評分 0-1）。
* $\text{SingleParentSupport}$：單親撫養津貼與住宅優先權之制度健全度。
* $\text{ParentalLeave}$：有薪育嬰留停給付替代率與父親專屬週數。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：國際比較社會福利法規庫、OECD 性別與家庭資料庫、台灣勞動部與衛福部統計年鑑。
* **研究樣本**：涵蓋 16 個 OECD 與東亞代表性國家（含瑞典、法國、挪威、德國、英國、台灣、南韓、日本等）。

## 主要實證發現 (Key Empirical Findings)
fsQCA 核心構型路徑分析結果如下表所示：

| 構型路徑 (Configuration) | 核心條件組合 | 案例國家 (Cases) | 一致性 (Consistency) | 原始覆蓋率 (Raw Coverage) |
| :--- | :--- | :--- | :--- | :--- |
| **路徑 1：北歐普及平權型** | 高公共托育 $\times$ 充沛同居平權 $\times$ 父親育嬰假 | 瑞典、挪威、丹麥 | **0.962** | 0.548 |
| **路徑 2：西歐多元包容型** | 高公共托育 $\times$ 民事伴侶法 (PACS) $\times$ 單親支持 | 法國、比利時 | **0.941** | 0.485 |
| **東亞排他性困局 (非成功)** | **低同居平權 $\times$ 零非婚保障 $\times$ 傳統婚家排他** | **台灣、南韓、日本** | **0.958 (超低生育率)** | 0.885 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：跳脫單一計量迴歸的線性因果假設，以構型視角證明「包容性法制」與「托育實物供給」互為不可或缺的互補品。
* **政策意涵**：
  * 台灣與東亞各國必須痛下決心推動「家庭包容性改革」：全面保障同居伴侶撫養權、單親扶助不設嚴苛資產門檻。
  * 儘速開放單身女性與女同志伴侶合法使用人工生殖科技（IVF），釋放被保守體制壓抑的強烈生育意向。
* 關聯議題：本篇歸屬於議題 [[T-POL-PronatalistSubsidies]] 與 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **樣本數量**：QCA 模型限於 16 個國家案例，未來可加入中東歐轉型國家進一步豐富構型異質性。

## 關聯文獻與引用 (Related Works)
* [[P10-Wang25-EastAsiaMarriageFertility]]：東亞婚育包裹與初婚推遲人口學分析。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：新時代生育經濟學與性別平等四象限。
* [[P20-Cheng23-PremaritalRelationships]]：台灣未婚同居普及化與非婚生育法制限制。
