# 合成控制法 (Synthetic Control Method, SCM)

## 定義與理論機制 (Definition & Mechanism)
合成控制法由 Abadie 等人提出，被著名計量經濟學家 Athey 與 Imbens 譽為「政策評估領域近二十年來最重要的計量創新」。當政策介入發生在單一或少數大型聚合單元（如特定縣市、州或國家）時，傳統 DID 往往難以找到單一完美的對照個體。合成控制法透過凸組合優化演算法，將未受政策影響的多個「供體池（Donor Pool）」單元賦予最優權重，建構出一個在政策實施前各項預測特徵與結果軌跡高度擬合的「反事實合成個體（Synthetic Counterpart）」，以此作為政策評估的客觀比較基準。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
假設有 $J+1$ 個單元，單元 1 為處理組，單元 $2, \dots, J+1$ 為供體池。

$$
\text{Treatment Effect}_t = Y_{1t} - \sum_{j=2}^{J+1} w_j^* Y_{jt}, \quad \text{for } t > T_0
$$

### 最優權重向量求算 (Constrained Convex Optimization)
$$
\min_{\mathbf{W}} \|\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W}\|_{\mathbf{V}} = \sqrt{(\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W})' \mathbf{V} (\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W})}
$$
約束條件：
$$
w_j \ge 0 \quad (\forall j \in \{2, \dots, J+1\}), \quad \sum_{j=2}^{J+1} w_j = 1
$$
* $\mathbf{X}_1$：處理組在政策實施前的預測變數向量（包含結果變數歷史軌跡與外生經濟特徵）。
* $\mathbf{X}_0$：供體池矩陣。
* $\mathbf{V}$：對角正半定權重矩陣，用於反映各預測變數對結果變數預測能力之相對重要性。

### 推論與假說檢定 (Placebo Tests)
* **時間安慰劑 (Time Placebo)**：將政策實施時間點虛擬提前，檢驗模型是否在假想處理期產生顯著效應。
* **空間安慰劑 (In-Space Placebo / Permutation Test)**：對供體池中每一個未受政策影響的單元依次運行 SCM，計算偽處理效應比率（RMSPE Ratio），建立精確的 $p$ 值分布。

## 優點與適用情境 (Strengths & Use Cases)
* 避免主觀挑選控制組，杜絕外推偏誤（Extrapolation Bias），權重透明且可直觀解釋。
* 極度適用於特定縣市獨立宣布大型政策改革（如桃園市加碼 3 萬生育津貼）。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 需具備足夠長的事前觀察期（Pre-intervention Periods）以確保擬合精度，且供體池不能受到外溢效應污染。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P16-Lai24-SubsidyMediationSCM]]：桃園市率先加碼高額生育津貼之合成控制反事實軌跡與中介機制評估。
