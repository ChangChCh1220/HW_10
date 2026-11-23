---
id: "P06"
title: "家務分工不對稱與女性婚內二胎生育意願之實證分析 (Gender Asymmetry in Housework Division and Second-Child Intentions Among Married Women)"
authors: ["林書妤 (Shu-Yu Lin)", "陳玉華 (Yu-Hua Chen)"]
year: 2023
venue: "《人口學刊》(Journal of Population Studies), 66, 45-88"
source_type: "pdf"
file_or_link: "raw/papers/P06-Lin23-HouseworkImbalance.pdf"
tags: [paper, 家務分工, 二胎意願, 第二輪性別革命, 雙重負擔, 台灣]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P06] 家務分工不對稱與女性婚內二胎生育意願之實證分析

## 核心摘要 (Executive Summary)
* **研究核心**：利用台灣社會變遷基本調查微觀數據，探討已育一胎之已婚雙薪女性，其家庭內部家務與育兒分工不平等如何抑制「生第二胎」的意願。
* **殘酷的分工差距**：調查顯示台灣已婚全職就業女性平均每週承擔 26.6 小時家務（平日每天約 3.8 小時），而其配偶僅承擔 8.2 小時（平日每天約 1.1 小時），差距達 3.2 倍。
* **邊際提升效果**：配偶每週家務與育兒時間每增加 1 小時，已婚女性生育第二胎的勝算比（Odds Ratio）顯著提高 16.4%（$p < 0.01$）。
* **核心意涵**：在婚內，阻礙生第二胎的最大障礙不是生第一胎的經驗，而是女性陷入「白天拼業績、晚上做家務」的極度身心耗竭。

## 研究背景與動機 (Background & Motivation)
台灣社會少子化的第二個致命軌道是「生了一胎後嚇到，不敢再生第二胎」。儘管台灣女性受教育水準與職場勞動參與率大幅提升（完成「第一輪性別革命」），但在私領域的家庭內部，家務勞動與育兒照顧依然被傳統性別角色高度綁定在女性身上（「第二輪性別革命」嚴重卡關）。本研究旨在以實證計量檢驗，丈夫的分擔是否為開啟二胎生育意願的決定性鑰匙。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究運用順序多項 Logit 模型（Ordered Logit Model），模型對接概念頁 [[C-HWT-HouseworkDivision]]：

$$
Y_i^* = \mathbf{X}_i'\boldsymbol{\beta} + \gamma (\text{Housework\_F}_i - \text{Housework\_M}_i) + \delta \text{Childcare\_M}_i + \varepsilon_i
$$

$$
Y_i = \begin{cases} 
1 \text{ (完全無意願)}, & \text{if } Y_i^* \le \kappa_1 \\
2 \text{ (不太有意願)}, & \text{if } \kappa_1 < Y_i^* \le \kappa_2 \\
3 \text{ (有意願)}, & \text{if } \kappa_2 < Y_i^* \le \kappa_3 \\
4 \text{ (非常有意願)}, & \text{if } Y_i^* > \kappa_3
\end{cases}
$$

### 變數與符號定義
* $Y_i^*$：受訪女性生第二胎之潛在連續意願程度；$Y_i$ 為觀測到的四分級順序意願。
* $\text{Housework\_F}_i - \text{Housework\_M}_i$：夫妻家務勞動時間差距（週小時數），預期係數 $\gamma < 0$。
* $\text{Childcare\_M}_i$：丈夫每週專注於子女陪伴與照顧之時間，預期係數 $\delta > 0$。
* $\mathbf{X}_i$：控制變數向量，包含受訪者年齡、現有小孩年齡、家庭總所得、居住地區、居住安排（是否與公婆同住）等。
* $\kappa_1, \kappa_2, \kappa_3$：順序模型待估計之截切門檻參數（Cut Points）。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：中央研究院社會學研究所「台灣社會變遷基本調查」（Taiwan Social Change Survey, TSCS）家庭組調查資料。
* **分析樣本**：選取年齡在 25 至 44 歲、全職就業且已育有一名子女之已婚女性，共計 1,280 位受訪者。

## 主要實證發現 (Key Empirical Findings)
實證估計結果如下表所示：

| 解釋變數 | 勝算比 (Odds Ratio) | 95% 信賴區間 | 統計顯著性 | 實質意涵 |
| :--- | :--- | :--- | :--- | :--- |
| **夫妻家務時間差 ($\text{F} - \text{M}$)** | **0.862** | [0.812, 0.915] | **$p < 0.001$** | 家務差距每大 1 小時，生二胎機率顯著下降 13.8% |
| **丈夫每週育兒時間** | **1.164** | [1.065, 1.272] | **$p < 0.01$** | 丈夫每多參與 1 小時育兒，二胎意願提升 16.4% |
| **與公婆同住 (與否)** | **0.684** | [0.521, 0.898] | **$p < 0.01$** | 與公婆同住顯著壓抑女性二胎意願（傳統媳婦角色壓力） |
| **家庭年所得 (每增加 10 萬)** | 1.042 | [1.011, 1.074] | $p < 0.05$ | 經濟充裕度對二胎具有正面助益 |
| **現有一胎年齡為 0-3 歲** | 0.725 | [0.584, 0.901] | $p < 0.01$ | 幼兒照顧最繁重階段，女性二胎疲勞度達最高點 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：具體量化了台灣雙薪家庭私領域家務不對稱對婚內二胎生育的「因果剎車效應」，為 McDonald 的性別平等理論提供台灣實證依據。
* **政策意涵**：
  * 政府催生政策不應只著眼於發錢，必須強力推廣「強制性、不可轉讓的父親專屬育嬰假（Daddy Quota）」。
  * 唯有將男性真正拉回家庭日常家務與育兒現場，打破女性「蠟燭兩頭燒」的困局，才能挽救二胎生育率。
* 關聯議題：本篇對接核心議題 [[T-WFC-WorkFamilyConflict]] 與 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **橫斷面資料侷限**：TSCS 為橫斷面調查，無法持續追蹤受訪女性最終是否實際生下第二胎。
* 丈夫家務時間為妻子主觀填報，未來可搭配時間日誌（Time-Use Diaries）雙向記錄驗證。

## 關聯文獻與引用 (Related Works)
* [[P11-Pan26-WorkFamilyClash]]：高工時職場、母職懲罰與女性勞動-生育衝突。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：性別平等、雙薪家庭與新時代生育經濟學。
* [[P22-Yuan22-TaiwanMarriagePushPull]]：台灣適婚青年進入婚姻之推拉力與公婆同住夢魘。
