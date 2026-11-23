# 東亞婚育包裹假說 (The East Asian Marriage-Childbearing Package)

## 定義與理論機制 (Definition & Mechanism)
東亞婚育包裹假說（Marriage Package Hypothesis）由社會學家 James Raymo 等人提出，指在東亞儒家文化圈（台灣、日本、南韓、新加坡）中，性生活、合法登記婚姻、購屋置產、生育繁衍、侍奉公婆與家族祭祀，被制度與社會輿論緊密捆綁成一個不可分割的「不可分大禮包（Indivisible Bundle）」。在歐美社會，婚姻與生育已經在法律與文化上高度脫鉤（非婚生子女超過 40-60%）；但在東亞，非婚生育受到民法、醫療特許（如人工生殖法嚴苛限制）與社會道德的嚴厲排擠（非婚生育率始終低於 4%）。因此，青年若因高房價、經濟低迷或恐懼姻親壓力而無法承擔婚姻，就等於「完全失去了生育的合法特許證」。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
Kitagawa 人口學因果分解數學模型：
$$
\text{CBR}_t = \sum_{a} M_{a,t} \cdot F_{a,t}^{\text{Mar}} + \sum_{a} (1 - M_{a,t}) \cdot F_{a,t}^{\text{NonMar}}
$$
在東亞體制下，因 $F_{a,t}^{\text{NonMar}} \approx 0$，模型退化為：
$$
\text{CBR}_t \approx \sum_{a} M_{a,t} \cdot F_{a,t}^{\text{Mar}}
$$
跨期變動分解公式：
$$
\Delta \text{CBR} = \underbrace{\sum_{a} \Delta M_{a} \cdot \bar{F}_{a}^{\text{Mar}}}_{\text{初婚推遲貢獻項 (82%)}} + \underbrace{\sum_{a} \bar{M}_{a} \cdot \Delta F_{a}^{\text{Mar}}}_{\text{婚內生育變動貢獻項 (18%)}}
$$

## 優點與適用情境 (Strengths & Use Cases)
* 清楚識別出東亞少子化的第一號病因不是「婚內夫妻不肯生」，而是「青年無法跨入婚姻大門」。
* 精準診斷出政府政策將資源全數放在已婚津貼的根本性錯配。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 鬆綁婚育包裹涉及民法親屬編、民事伴侶法、單身人工生殖等高度道德與宗教爭議之法案，推動難度極高。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P10-Wang25-EastAsiaMarriageFertility]]：東亞婚育包裹與初婚推遲跨國人口學分析。
* [[P12-Tan26-NuptialityPolicyMismatch]]：超低生育體制下的家庭政策錯配與初婚忽視。
* [[P13-Ryu24-PronatalistInclusiveness]]：促生育政策包容性與多元家庭制度障礙。
* [[P20-Cheng23-PremaritalRelationships]]：台灣同居率暴增 4 倍但非婚生育徹底脫鉤。
* [[P22-Yuan22-TaiwanMarriagePushPull]]：適婚男女走入婚姻之推拉力與考量因素。
