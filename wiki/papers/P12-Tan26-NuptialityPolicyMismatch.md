---
id: "P12"
title: "Policy Mismatch in Ultra-Low Fertility Regimes: When Family Policies Ignore Nuptiality"
authors: ["P. Tan", "R. Chia"]
year: 2026
venue: "Demographic Research, 54, Article 12"
source_type: "pdf"
file_or_link: "raw/papers/P12-Tan26-NuptialityPolicyMismatch.pdf"
tags: [paper, 政策錯配, 反事實分解, 預算分配, 初婚障礙, 東亞比較]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P12] 超低生育體制下的政策錯配：當家庭政策忽視婚姻

## 核心摘要 (Executive Summary)
* **研究核心**：針對東亞四個極低生育率經濟體（台灣、南韓、新加坡、香港）2000 至 2024 年之政府家庭政策預算結構進行審計與反事實人口分解模擬（Counterfactual Decomposition）。
* **嚴重的資源錯配實證**：研究發現，政府平均將 85% 以上的少子化預算投入於「已婚育兒津貼與托育補助」，但實質貢獻了 80% 少子化成因的「青年初婚障礙（未婚率飆升）」所獲得的政策資源不足 15%。
* **邊際效應反差**：反事實模擬指出，若將現有 30% 的育兒津貼預算轉移至「青年初婚成家扶助基金（成家低利免息房貸、租屋安家補助、婚戀公共設施）」，總和生育率的提升潛力將高出 2.8 倍。
* **政策總結**：政策制定者嚴重混淆了「症狀」與「病根」，陷入「在沒有魚的池塘裡猛撒魚飼料」的政策自嗨。

## 研究背景與動機 (Background & Motivation)
東亞各國政府在面對少子化危機時，往往直覺性地認為「因為生育率下降，所以要給生小孩的人發錢」。這種政策思維在歐美等非婚生育率高的國家或許有效，但在東亞「婚育包裹」體制下，生育的先決條件是「結婚」。當未婚青年因為高房價、低起薪、長工時與性別不平等等因素而被大規模阻絕於婚姻之外時，只補貼已婚家庭根本無法解決少子化的真正根源。本研究旨在以量化實證揭開這場巨大的公共資源錯配。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構三階段反事實人口政策模擬模型（Three-Stage Nuptiality-Fertility Policy Simulation Model），模型對接概念頁 [[C-MBP-MarriagePackage]]：

$$
\text{TFR}_t = \sum_{a=15}^{49} \left( M_{a,t} \cdot F_{a,t}^{\text{Mar}} + (1 - M_{a,t}) \cdot F_{a,t}^{\text{NonMar}} \right)
$$

### 預算彈性反事實優化模型
$$
\max_{\{B_{\text{Marr}}, B_{\text{Child}}\}} \Delta \text{TFR} \quad \text{s.t.} \quad B_{\text{Marr}} + B_{\text{Child}} \le \bar{B}
$$
$$
M_{a}(B_{\text{Marr}}) = M_{a}^0 \cdot \left( 1 + \varepsilon_M \frac{B_{\text{Marr}}}{B_{\text{Marr}}^0} \right), \quad F_{a}^{\text{Mar}}(B_{\text{Child}}) = F_a^{\text{Mar}, 0} \cdot \left( 1 + \varepsilon_F \frac{B_{\text{Child}}}{B_{\text{Child}}^0} \right)
$$

### 變數與符號定義
* $M_{a,t}$：年齡組 $a$ 女性於年度 $t$ 之有偶率（Proportion Married）。
* $F_{a,t}^{\text{Mar}}$：有偶女性年齡別生育率（Marital Age-Specific Fertility Rate）。
* $F_{a,t}^{\text{NonMar}}$：未婚女性年齡別生育率（在東亞體制下幾乎為零）。
* $B_{\text{Marr}}$：政府投入於拆除青年成家與初婚門檻之財政預算。
* $B_{\text{Child}}$：政府投入於已婚者育兒現金補貼與津貼之預算。
* $\varepsilon_M, \varepsilon_F$：婚姻率與婚內生育率對相應政策預算之反應彈性。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：台灣行政院主計總處預算決算統計、南韓企劃財政部、新加坡社會及家庭發展部、香港統計處官方人口與財政審計數據（2000-2024 年）。
* **研究樣本**：東亞 4 大經濟體、長達 25 年的年度政府家庭政策預算支出明細與年齡別初婚/生育動態數據。

## 主要實證發現 (Key Empirical Findings)
預算分配現狀與反事實模擬效益比較如下表所示：

| 評估維度與政策範疇 | 現狀政策配置 (Baseline Status Quo) | 最優反事實配置 (Counterfactual Optimal) | 邊際政策成效差異 |
| :--- | :--- | :--- | :--- |
| **已婚育兒與現金津貼預算 ($B_{\text{Child}}$)** | **86.4%** (約 1,200 億台幣) | **55.0%** (合理精簡聚焦公托) | 消除過度補貼與死重損失 |
| **青年成家與初婚支持預算 ($B_{\text{Marr}}$)** | **13.6%** (嚴重不足) | **45.0%** (大幅加碼社會投資) | 資源回歸少子化真正痛點 |
| **預估初婚率變動 ($\Delta \text{CMR}$)** | +0.02 ‰ (微乎其微) | **+1.25 ‰*** (青年婚姻門檻降低) | 提高青年成家可行性 |
| **總和生育率模擬變動 ($\Delta \text{TFR}$)** | +0.02 (幾乎無效) | **+0.16*** (跨越超低陷阱) | **成效高出 2.8 倍** |
| 財政每增加一名新生兒成本 | 380 萬台幣 / 嬰 | **135 萬台幣 / 嬰** | **財政效率大幅提升 64%** |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：首度從公共財政審計視角，以數理模擬量化揭發東亞超低生育率政策中的「資源錯配假象」。
* **政策意涵**：
  * 政府少子化預算必須進行戰略性典範轉移：停止只向後端（已婚育兒）發放邊際效應極低的現金。
  * 將近半數預算前移至前端：建立青年成家特惠基金、平價成家住宅、單身聯誼公共平臺與婚禮簡約支持，幫助青年跨過殘酷的結婚門檻。
* 關聯議題：本篇歸屬於議題 [[T-POL-PronatalistSubsidies]] 與 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **政治經濟學阻力**：預算重新配置在實務上容易遭到既有補貼利益團體的政治反彈，未來需納入政治經濟學博弈模型。

## 關聯文獻與引用 (Related Works)
* [[P04-Hsu23-NatalSubsidyDID]]：台灣生育津貼之 DID 評估與套利現象。
* [[P10-Wang25-EastAsiaMarriageFertility]]：東亞婚育包裹與初婚推遲因果機制。
* [[P15-Chien24-TaiwanPronatalistPolicies]]：台灣直轄市生育津貼與托育政策實證。
