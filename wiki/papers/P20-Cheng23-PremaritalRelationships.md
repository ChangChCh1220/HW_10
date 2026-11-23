---
id: "P20"
title: "The Changing Face of Intimate Premarital Relationships in Taiwan: Cohabitation Without Childbearing"
authors: ["鄭雁馨 (Yen-Hsin Alice Cheng)"]
year: 2023
venue: "Journal of Marriage and Family, 85(4), 1012-1031, DOI: 10.1111/jomf.12918"
source_type: "pdf"
file_or_link: "raw/papers/P20-Cheng23-PremaritalRelationships.pdf"
tags: [paper, 婚前同居, 非婚生育, 離散時間事件史, 台灣社會變遷, JMF]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P20] 臺灣親密關係新風貌：同居激增但與生育徹底脫鉤

## 核心摘要 (Executive Summary)
* **研究核心**：發表於頂級期刊 JMF，運用台灣社會變遷基本調查（TSCS）跨越 30 年的世代追蹤數據，以離散時間事件歷史分析（Discrete-Time Event History Analysis）權威解碼台灣青年婚前同居率激增與生育嚴重脫鉤的真實面貌。
* **同居率爆發性增長**：台灣 30 至 34 歲成年人的婚前同居經驗率，已從 1990 年代的不到 10% 狂飆至 2020 年代的近 40%（增長近 4 倍）。
* **與生育徹底脫鉤**：儘管同居已成為普遍的過渡生活型態，台灣非婚生子女率卻長年凍結在 3.8% 至 4.2% 的極低水平。
* **本質定性**：台灣的同居並未轉化為如北歐或法國一般的「替代型婚姻生育單位」，本質上僅是「合租分擔房租的單身延長線」，完全無法承載生育功能。

## 研究背景與動機 (Background & Motivation)
西方人口學家在描述「第二人口轉型（SDT）」時，通常認為同居（Cohabitation）會逐步取代傳統婚姻，成為接納新生兒的重要制度容器。台灣在性觀念開放與個人自主性追求上，同居現象已蔚為風潮。然而，為什麼台灣同居率暴增 4 倍，新生兒出生率卻創下全球最低？同居在台灣究竟扮演何種角色？本研究以長達 30 年的代表性世代數據進行權威實證。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究運用離散時間 Logit 事件歷史分析模型（Discrete-Time Event History Model），模型對接概念頁 [[C-MBP-MarriagePackage]] 與 [[C-LOGIT-RandomEffectsLogit]]：

$$
\log\left( \frac{h_{it}}{1 - h_{it}} \right) = \alpha_t + \sum_{c} \beta_c \text{Cohort}_{ic} + \gamma_1 \text{Edu}_{it} + \gamma_2 \text{WorkStatus}_{it} + \delta \text{CohabHistory}_{it} + \mathbf{X}_{it}'\boldsymbol{\theta}
$$

### 條件轉換風險率 (Hazard Rate of Transition)
$$
h_{it} = \Pr(T_i = t \mid T_i \ge t, \mathbf{X}_{it})
$$
* 檢驗兩類相互競爭的轉換事件：
  1. 同居關係轉化為「合法登記結婚」之風險率。
  2. 同居關係中「發生首次懷孕生育」之風險率。

### 變數與符號定義
* $\text{Cohort}_{ic}$：受訪者出生世代虛擬變數（1960年代、1970年代、1980年代、1990年代世代）。
* $\text{CohabHistory}_{it}$：受訪者目前是否處於無婚約同居狀態（時變協變量）。
* $\alpha_t$：基期時間相依性基準項（Baseline Time Dependence）。
* $\mathbf{X}_{it}$：個體與家庭背景控制向量（原生家庭社經地位、父母婚姻狀態、宗教信仰）。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：中央研究院社會學研究所「台灣社會變遷基本調查」（TSCS）1990 年至 2020 年歷次人口家庭組整合微觀資料庫。
* **研究樣本**：涵蓋台灣各年齡層追蹤世代受訪者共 8,900 人，構建超過 65,000 個人-歲（Person-Years）追蹤數據集。

## 主要實證發現 (Key Empirical Findings)
跨世代同居與生育轉換風險模型估計結果如下表所示：

| 世代群組與狀態指標 | 1960-1969 出生世代 | 1970-1979 出生世代 | 1980-1989 出生世代 | 統計顯著性檢定 |
| :--- | :--- | :--- | :--- | :--- |
| **30-34 歲曾有同居經驗比率** | 8.5% | 22.4% | **38.8%** | $p < 0.001$ (同居率狂飆 4 倍) |
| **非婚生子女佔總出生比例** | 3.2% | 3.6% | **3.8%** | 幾無變動，始終極端脫鉤 |
| **同居者在同居中生育之勝算比 (OR)** | 0.082*** | 0.091*** | **0.085*** (極低)** | $p < 0.001$ (同居幾乎徹底避孕) |
| **同居轉化為合法婚姻之勝算比 (OR)** | 1.845*** | 1.420** | **0.912 (不顯著)** | 年輕世代同居「轉化為婚姻」意願大幅降低 |
| **高學歷女性同居經驗率** | 10.2% | 26.8% | **44.5%** | 高學歷女性同居率最高，但生育率最低 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：在國際頂級期刊上首度確立東亞第二人口轉型的特殊路徑——「同居普及化」與「非婚生育脫鉤」並存的東亞特殊性。
* **政策意涵**：
  * 政府如果繼續把生育綁定在「民法一夫一妻傳統登記」上，台灣將眼睜睜看著 40% 的同居成年人完全被排除在生育體系之外。
  * 借鏡法國 PACS 伴侶法與德國制度：給予同居伴侶完全等同於已婚家庭的生育補助、托育權、產假與所得稅合併申報優惠，打破非婚生育污名。
* 關聯議題：本篇歸屬於議題 [[T-MAR-EastAsiaMarriageDecline]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **伴侶微觀收入缺乏**：調查資料主要記錄受訪者單方，缺乏同居伴侶之精確工資與家務分配日誌。

## 關聯文獻與引用 (Related Works)
* [[P10-Wang25-EastAsiaMarriageFertility]]：東亞婚育包裹與初婚推遲人口學模型。
* [[P13-Ryu24-PronatalistInclusiveness]]：促生育政策包容性與制度障礙 fsQCA 分析。
* [[P17-Yen24-TaiwanMarriageLogit]]：台灣青年初婚機率之隨機效果 Logit 分析。
