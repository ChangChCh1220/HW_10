---
id: "P19"
title: "Parental Marriage Pressure, Filial Obligations, and Psychological Well-being of Unmarried Adults in Taiwan"
authors: ["Y. Chen", "C. Huang"]
year: 2026
venue: "Journal of Marriage and Family, 88(2), 340-362"
source_type: "pdf"
file_or_link: "raw/papers/P19-Chen26-MarriageMandatesParentalPressure.pdf"
tags: [paper, 父母催婚, 孝道焦慮, 雙重中介模型, 心理福祉, 逃避應對]
created_at: 2026-11-23
updated_at: 2026-11-23
---

# [P19] 父母催婚壓力、孝道責任與臺灣未婚成人的心理福祉

## 核心摘要 (Executive Summary)
* **研究核心**：利用台灣社會變遷調查（TSCS）未婚青年追蹤樣本，透過拔靴法雙重中介模型（Dual Mediation Model with Bootstrap），評估原生家庭長輩「催婚與婚育命令」對未婚青年初婚進程與心理健康的實際因果影響。
* **反效果之逆向衝擊**：研究發現，父母高頻率的催婚並未能有效促成初婚，反而誘發強烈的「逃避性應對機制（Avoidance Coping）」（中介效應值 0.245***），導致青年減少返家次數與疏離原生家庭。
* **孝道焦慮與心理耗竭**：傳統孝道規範（「不孝有三，無後為大」）在現代轉化為嚴重的內疚感與心理困窘（Depressive Symptoms 評分顯著增加 18.6%）。
* **社會學啟示**：傳統家庭催婚體制已失去正向整合功能，反而將適婚青年推向更徹底的單身防禦與冷漠。

## 研究背景與動機 (Background & Motivation)
在東亞家庭主義文化下，「結婚成家」往往被長輩視為子女人格完整與履行孝道責任的終極標誌。每逢農曆春節或家族聚會，適婚未婚青年普遍面臨父母與親戚排山倒海的催婚詢問。然而，當代青年面對低薪、高房價與高競爭壓力，成家門檻極高。長輩的持續催婚究竟是促成婚姻的助力，還是轉化為壓垮青年心理健康的最後一根稻草？本研究運用嚴謹的中介效應計量模型深入解析。

## 理論框架與計量模型 (Methodology & Mathematical Formulation)
本研究建構平行雙重中介因果路徑模型（Parallel Dual Mediation Model），模型對接概念頁 [[C-MBP-MarriagePackage]]：

$$
\text{MentalDistress}_i = c' \text{ParentalPressure}_i + b_1 M_{1i} (\text{FilialGuilt}) + b_2 M_{2i} (\text{AvoidanceCoping}) + \boldsymbol{\gamma}' \mathbf{Z}_i + \varepsilon_i
$$

### 中介方程式體系
$$
\begin{cases}
M_{1i} (\text{FilialGuilt}) = a_1 \text{ParentalPressure}_i + \boldsymbol{\theta}_1' \mathbf{Z}_i + u_{1i} \\
M_{2i} (\text{AvoidanceCoping}) = a_2 \text{ParentalPressure}_i + \boldsymbol{\theta}_2' \mathbf{Z}_i + u_{2i}
\end{cases}
$$

### 變數與符號定義
* $\text{ParentalPressure}_i$：核心自變數，父母與家族催婚頻率與言詞強制性指數。
* $M_{1i}$：第一中介變數，受訪者自覺未達長輩期望之「孝道愧疚感（Filial Guilt）」。
* $M_{2i}$：第二中介變數，個體採取之「逃避性應對機制」（減少互動、隱匿感情、拒絕溝通）。
* $\text{MentalDistress}_i$：心理福祉受損程度（以 CES-D 憂鬱量表與焦慮量表測量）。
* 間接中介效應檢驗：採用 5,000 次重複抽樣之拔靴法（Bias-Corrected Bootstrap 95% Confidence Intervals）。

## 資料來源與研究樣本 (Data & Sample)
* **資料來源**：中央研究院社會學研究所「台灣社會變遷基本調查」（TSCS）與華人家庭動態調查（PSFD）成年未婚世代追蹤問卷。
* **研究樣本**：選取年齡在 25 至 39 歲之未婚全職工作青年共計 1,820 人。

## 主要實證發現 (Key Empirical Findings)
中介效應路徑係數與拔靴法檢定結果如下表所示：

| 路徑關係與效應分解 | 路徑係數 ($\beta$) | 拔靴法 95% 信賴區間 | 統計顯著性 | 實質機制意涵 |
| :--- | :--- | :--- | :--- | :--- |
| **自變數對中介 1 ($a_1$：催婚 $\to$ 愧疚感)** | **+0.428*** | [+0.365, +0.491] | $p < 0.001$ | 催婚強烈引發未婚青年的孝道愧疚與自我懷疑 |
| **自變數對中介 2 ($a_2$：催婚 $\to$ 逃避應對)** | **+0.385*** | [+0.321, +0.449] | $p < 0.001$ | 長輩施壓直接迫使青年採取情感隔離與逃避 |
| **中介 2 對心理困窘 ($b_2$)** | **+0.312*** | [+0.248, +0.376] | $p < 0.001$ | 逃避溝通導致社會孤立與憂鬱情緒攀升 |
| **透過逃避應對之間接效應 ($a_2 \times b_2$)** | **+0.120*** | [+0.082, +0.165] | $p < 0.001$ | 間接效應顯著，證實催婚具有強烈反向破壞力 |
| **催婚對最終實際成家結婚之總效應** | **-0.084** | [-0.145, -0.021] | **$p < 0.05$** | **催婚越多，青年最終登記結婚率反而越低！** |

## 政策意涵與學術貢獻 (Implications & Contributions)
* **學術貢獻**：具體量化了東亞代間催婚對未婚青年心理福祉的因果破壞路徑，打破「施加家庭壓力能促進結婚」的傳統迷思。
* **政策意涵**：
  * 政府少子化宣傳不應採取「情緒勒索式（例如：生小孩才有美滿人生）」的道德說教，這只會引發青年強烈反感與防禦。
  * 應倡導現代家庭代間溝通尊重，將政策資源轉向給予青年切實的生活減壓與經濟賦權。
* 關聯議題：本篇歸屬於議題 [[T-MAR-EastAsiaMarriageDecline]]。

## 限制與未來研究方向 (Limitations)
* **父母雙方特質**：未能完全控制受訪者父母自身之受教育程度與社經地位對催婚風格的異質性。

## 關聯文獻與引用 (Related Works)
* [[P10-Wang25-EastAsiaMarriageFertility]]：東亞婚育包裹與初婚推遲因果模型。
* [[P21-Liu26-MarriageIntentionsGenderRoles]]：未婚成年人性別角色態度與個人自主性。
* [[P22-Yuan22-TaiwanMarriagePushPull]]：適婚男女走入婚姻考量因素與家庭推力。
