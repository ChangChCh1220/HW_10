---
id: "P14"
title: "The Economics of Fertility: A New Era"
authors: ["Matthias Doepke", "Anne Hannusch", "Fabrice Sorrenti", "Fabrizio Zilibotti"]
year: 2022
venue: "NBER Working Paper No. 29948 / Annual Review of Economics, 15, 2023"
source_type: "pdf"
file_or_link: "raw/papers/P14-Doepke22-EconomicsOfFertilityNewEra.pdf"
tags: [paper, 新時代生育經濟學, 工作家庭相容性, 總體家庭協商, 性別平等, NBER]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P14] 新時代生育經濟學：雙薪社會下的典範轉移

## 核心摘要 (Executive Summary)
* **理論劃時代貢獻**：NBER 權威文獻，正式宣告傳統貝克（Becker）生育經濟學模型（婦女工資上升因機會成本增加而必然降低生育率）在當代雙薪社會徹底過時。
* **U 型反轉現象**：跨國數據證實，在 OECD 國家中，女性勞動參與率與總和生育率之間的跨國相關性已從 1980 年代的「強烈負相關（$-0.55$）」反轉為當代的「顯著正相關（$+0.68$）」。
* **四大支柱理論**：現代高生育率國家的共通特徵為建立在四大支柱上：(1) 平價公共托育、(2) 父親實質分擔家務、(3) 彈性友善職場、(4) 社會規範與合作性協商文化。
* **東亞定性**：東亞國家（台韓日）深陷「傳統性別分工規範」與「高女性教育水準」的巨大撕裂中，是現代低生育率的最極端反面案例。

## 研究背景與動機 (Background & Motivation)
在過去半個世紀中，Gary Becker 的新家庭經濟學（New Home Economics）統治了生育理論。該理論認為在「男主外、女主內」的單薪體制下，母親的市場工資提高會增加養育子女的機會成本，進而壓抑生育。然而進入 21 世紀後，北歐與法國出現了「女性高就業率、高生育率」並存的現象，而南歐與東亞等傳統維持男尊女卑家務分工的國家，生育率卻徹底崩盤。這標誌著生育經濟學必須迎來新時代的典範轉移。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構總體動態家庭協商模型（Macroeconomic Household Bargaining Model），模型對接概念頁 [[C-HWT-HouseworkDivision]] 與 [[C-SEM-StructuralFertility]]：

$$
\max_{\{c, n, h_f, h_m, l_f, l_m\}} U(c, n, h_f, h_m) = \ln c + \phi \ln n - \frac{\psi_f}{1+\sigma} (l_f + h_f)^{1+\sigma} - \frac{\psi_m}{1+\sigma} (l_m + h_m)^{1+\sigma}
$$

### 家庭時間與預算限制式
$$
c + p_c \cdot (n \cdot \theta_{\text{care}} - s_{\text{public}}) \le w_f l_f + w_m l_m
$$
$$
n \cdot \theta_{\text{care}} \le h_f + h_m + s_{\text{public}}
$$

### 變數與符號定義
* $n$：家庭生育子女數量；$c$：家庭總消費。
* $w_f, w_m$：男女市場時薪；$l_f, l_m$：男女市場工作時數。
* $h_f, h_m$：男女投入育兒與家務的時間。
* $s_{\text{public}}$：政府提供的公共托育補貼時數（Public Childcare Subsidies）。
* $p_c$：私人托育市場價格。
* $\phi$：對子女之偏好參數；$\sigma$：勞動供給之弗里希彈性（Frisch Elasticity）。
* 理論命題：當 $s_{\text{public}}$ 充足且丈夫分擔家務比率 $h_m / (h_f + h_m) \to 0.5$ 時，$\frac{\partial n}{\partial w_f} > 0$（工資上升帶動生育率上升，實現 U 型反轉）。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：跨 OECD 國家總體經濟數據庫（1970-2020 年縱橫面板）、歐盟時間運用調查（HETUS）、多國家庭人口調查。
* **分析範圍**：涵蓋 34 個已開發國家半世紀的人口與勞動總體趨勢。

## 主要實證發現 (Key Empirical Findings)
新舊時代實證關聯性對照與機制矩陣如下表：

| 時代與國家群組 | 女性勞參率與 TFR 之相關性 | 制度支撐特徵 | 典型國家 |
| :--- | :--- | :--- | :--- |
| **舊時代 (1980 年代以前)** | **$r = -0.55***$ (強負相關)** | 單薪家庭為尊、男主外女主內、無公托 | 舊時代全美、傳統歐陸 |
| **新時代 (2000 年代以降)** | **$r = +0.68***$ (顯著正相關)** | **雙薪家庭、普及公托、父親育嬰假** | 瑞典、挪威、法國、冰島 |
| **東亞失衡型 (當代台韓)** | **極端分離陷阱 ($r \to -0.72$)** | **女性職場高參與，但家務全包、公托匱乏** | **台灣、南韓、新加坡** |
| 跨國回歸：男性家務每增 10% | $\Delta \text{TFR} = +0.15***$ | 顯著緩解女性職涯中斷恐懼 | 全球 OECD 面板檢驗 |
| 跨國回歸：公托涵蓋率每增 20% | $\Delta \text{TFR} = +0.18***$ | 根本消除女性育兒機會成本 | 全球 OECD 面板檢驗 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：建立了 21 世紀生育經濟學的嶄新理論架構，徹底推翻了「女性就業必然妨礙生育」的陳舊教條。
* **政策意涵**：
  * 「工作與家庭相容性（Work-Family Compatibility）」是當代提升生育率的唯一核心法則。
  * 催生政策不能要求女性「回歸家庭」，而是要透過制度讓女性「既能全職就業，又能安心育兒」——關鍵解方就是充足的平價公共托育與男性平權分擔。
* 關聯議題：本篇為核心理論奠基文獻，對接議題 [[T-WFC-WorkFamilyConflict]]、[[T-POL-PronatalistSubsidies]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **宏觀總體理論外推**：本理論模型主要立足於已婚雙薪家庭，對東亞特有的「極端初婚障礙與不婚化」之微觀配對摩擦仍需進一步擴充。

## 關聯文獻與引用 (Related Works)
* [[P06-Lin23-HouseworkImbalance]]：台灣家務分工不對稱與二胎意願微觀實證。
* [[P08-Koh26-ChildcareSubsidy]]：普及托育服務 vs. 現金津貼之長期效果比較。
* [[P11-Pan26-WorkFamilyClash]]：高工時職場與女性勞動供給衝突。
