# 家務分工與第二輪性別革命理論 (Housework Division & The Second Gender Revolution)

## 定義與理論機制 (Definition & Mechanism)
由著名人口學家 Frances Goldscheider 與 Peter McDonald 等人提出。該理論指出，現代社會在過去半世紀經歷了「第一輪性別革命（The First Gender Revolution）」——女性大規模進入高等教育體系與公共就業市場，實現公領域的經濟賦權。然而，「第二輪性別革命（The Second Gender Revolution）」——即男性大規模進入私領域家庭內部，實質平等分擔無償家務勞動、育兒料理與長輩照護——在東亞與南歐等傳統體制中嚴重停滯。公領域平權與私領域停滯的劇烈脫節，使得全職職業婦女面臨沉重的「雙重輪班（The Second Shift）」，進而以「拒絕婚姻」與「生了一胎後拒生第二胎」作為理性防衛。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
McDonald 性別平等與生育率 U 型關係模型：
$$
\text{Fertility} = f(\text{GenderEquity}_{\text{Public}}, \text{GenderEquity}_{\text{Private}})
$$

### 家庭內部時間談判博弈 (Household Nash Bargaining)
$$
\max_{(h_f, h_m)} \left[ U^f(w_f, h_f, h_m) - V^f(w_f, \text{Single}) \right]^\alpha \cdot \left[ U^m(w_m, h_f, h_m) - V^m(w_m, \text{Single}) \right]^{1-\alpha}
$$
* $h_f, h_m$：妻子與丈夫投入無償家務的時間。
* $V^f, V^m$：雙方在談判破裂（維持單身或離婚）時的保留效用（Threat Points）。
* 當女性市場工資 $w_f$ 提高時，其單身保留效用 $V^f$ 上升；若婚姻體制強制要求 $h_f \gg h_m$（私領域極度不平等），則女性的理性最優解為不進入婚姻（或二胎生育意願 $\to 0$）。

## 優點與適用情境 (Strengths & Use Cases)
* 完美解釋了為何在女性受教育水準最高的東亞發達經濟體中，生育率反而全球最低。
* 為育嬰假改革、男性陪產假與公托政策提供深厚社會學理論支撐。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 私領域文化規範改變極其緩慢，政策介入往往面臨社會既定性別刻板印象的深層阻抗。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P06-Lin23-HouseworkImbalance]]：台灣雙薪家庭家務時間差（3.8小時 vs. 1.1小時）對女性二胎意願的壓抑實證。
* [[P11-Pan26-WorkFamilyClash]]：長工時職場與全職就業女性的母職時間衝突。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：新時代生育經濟學與雙薪家庭支持四大支柱。
* [[P21-Liu26-MarriageIntentionsGenderRoles]]：未婚女性性平意識與個人自主性威脅感。
