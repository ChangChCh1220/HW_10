---
id: "P17"
title: "經濟能力、工時與臺灣青年初婚決策之實證研究：隨機效果 Logit 模型 (Economic Capacity, Working Hours, and Nuptiality in Taiwan: A Random Effects Logit Approach)"
authors: ["顏世昇 (Shih-Sheng Yen)", "指導教授：盧姝璇 (Shu-Hsuan Lu)"]
year: 2024
venue: "國立清華大學經濟學系碩士學位論文"
source_type: "pdf"
file_or_link: "raw/papers/P17-Yen24-TaiwanMarriageLogit.pdf"
tags: [paper, 初婚決策, 隨機效果Logit, 婚姻斜坡, 薪資不對稱, 台灣青年]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P17] 經濟能力、工時與臺灣青年初婚決策之實證研究：隨機效果 Logit 模型

## 核心摘要 (Executive Summary)
* **研究核心**：運用中研院家庭動態調查（PSFD）長達 12 年的微觀追蹤資料，以面板隨機效果 Logit 模型（Random Effects Logit）探討薪資水準、工作時數與資產狀況對台灣男女初婚機率之不對稱因果衝擊。
* **男女薪資之相反效應**：實證發現極具衝擊力的性別不對稱性——男性個人月薪每增加 1 萬元，進入初婚的勝算比（Odds Ratio）顯著提升 18.2%（$p < 0.001$）；相反地，女性個人月薪每增加 1 萬元，進入初婚的勝算比反而顯著下降 14.1%（$p < 0.01$）。
* **殘酷的婚姻斜坡**：女性在職場上追求高薪，在傳統「男高女低」的擇偶婚姻斜坡文化制約下，反而面臨更嚴峻的配對市場縮小與自我防衛。
* **工時之性別分歧**：男性的長工時並未顯著阻礙其結婚（視為事業投入），但女性的長工時則直接降低其初婚機率。

## 研究背景與動機 (Background & Motivation)
台灣總和生育率暴跌的核心病根在於「未婚率大幅飆升」（30-34 歲女性未婚率已超過 50%）。究竟是什麼因素阻礙了青年走入婚姻？經濟學的傳統婚姻搜尋理論認為，男女雙方經濟條件改善應有助於家庭成立。然而，在東亞儒家文化與現代女性高等教育普及的交織下，婚姻市場上的男女經濟期待可能呈現截然相反的走向。本研究運用微觀長期追蹤資料庫，精確檢驗薪資與工時在男女婚姻市場中的非對稱機制。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構面板隨機效果 Logit 計量模型（Panel Random Effects Logit Model），模型對接概念頁 [[C-LOGIT-RandomEffectsLogit]]：

$$
\ln\left( \frac{P_{it}}{1 - P_{it}} \right) = \alpha + \beta_1 \text{Wage}_{it} + \beta_2 \text{WorkHours}_{it} + \beta_3 \text{Asset}_{it} + \mathbf{X}_{it}'\boldsymbol{\gamma} + u_i
$$

### 潛在未觀察效應假定
$$
u_i \mid \mathbf{X}_{it} \sim \mathcal{N}(0, \sigma_u^2), \quad \rho_{\text{panel}} = \frac{\sigma_u^2}{\sigma_u^2 + \pi^2/3}
$$

### 變數與符號定義
* $P_{it} = \Pr(\text{Marry}_{it} = 1 \mid \text{Unmarried}_{i,t-1} = 1)$：前期處於未婚狀態之個體 $i$ 在年度 $t$ 登記進入初婚之條件機率。
* $\text{Wage}_{it}$：核心解釋變數，受訪者個人月薪（單位：萬元新台幣）。
* $\text{WorkHours}_{it}$：每週實質工作時數。
* $\text{Asset}_{it}$：個人或直系尊親屬名下是否有不動產房屋之虛擬變數。
* $\mathbf{X}_{it}$：微觀控制變數（年齡、教育程度、居住地區、同住長輩健康狀況）。
* $u_i$：個人層級不可觀測之隨機效果（捕捉個體社交外向度、原生家庭背景等天生稟賦）。
* $\rho_{\text{panel}}$：個體內組內相關係數（Intra-class Correlation）。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：中央研究院社會學研究所「華人家庭動態資料庫」（Panel Study of Family Dynamics, PSFD）2010 年至 2022 年追蹤樣本。
* **研究樣本**：選取受訪時年齡在 22 至 42 歲之間、基期未婚之受訪者共 1,714 人，累計追蹤超過 10,200 個人-年度觀測值。

## 主要實證發現 (Key Empirical Findings)
性別分組之隨機效果 Logit 模型估計結果如下表所示：

| 解釋變數 (每單位變動) | 男性次樣本勝算比 (OR) | 女性次樣本勝算比 (OR) | 性別係數差異檢定 $p$ 值 | 實質社會意涵說明 |
| :--- | :--- | :--- | :--- | :--- |
| **個人月薪 (每增 1 萬元)** | **1.182*** (0.045)** | **0.859** (0.048)** | **$p < 0.001$** | **薪水越高，男人越好結，女人越難嫁** |
| **每週工時 (每增 5 小時)** | 1.025 (0.021) | **0.912** (0.032)** | $p < 0.05$ | 女性長工時顯著剝奪社交與成家時間 |
| **自有住房/父母有房** | **1.542*** (0.125)** | 1.105 (0.088) | $p < 0.01$ | 男方有房是強大婚配資本，女方則否 |
| **大學及以上高等學歷** | **1.320** (0.098)** | **0.785** (0.076)** | $p < 0.001$ | 高學歷女性在婚姻市場面臨嚴重大齡排擠 |
| 面板隨機效應 $\sigma_u$ | 0.842*** | 0.915*** | — | 個體未觀察異質性顯著存在 |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：以扎實的追蹤計量模型證明：台灣婚姻市場仍然被嚴苛的「婚姻斜坡（Marriage Gradient）」文化鎖死。
* **政策意涵**：
  * 政府如果只單純推動「促婚活動」，卻不致力於打破傳統性別擇偶框架（如要求男方薪水一定要高於女方、男方必須買房買車），高薪高學歷女性的未婚率將持續居高不下。
  * 應引導社會打破「男強女弱」的婚配刻板印象，鼓勵平等伴侶關係與雙薪共營思維。
* 關聯議題：本篇歸屬於議題 [[T-MAR-EastAsiaMarriageDecline]] 與 [[T-FER-FertilityDecline]]。

## 限制與未來研究方向 (Limitations)
* **擇偶主觀偏好缺乏**：PSFD 資料庫較少直接測量受訪者對「理想伴侶經濟門檻」之具體數值期待。

## 關聯文獻與引用 (Related Works)
* [[P18-Lin23-HousingBeforeMarriage]]：台灣未婚青年購屋態度與初婚意願。
* [[P21-Liu26-MarriageIntentionsGenderRoles]]：未婚成年人性別角色態度與自主性實證。
* [[P23-Yang23-MiddleAgedAlwaysSingle]]：中年始終單身者之階層特徵（高學歷女 vs. 低收男）。
