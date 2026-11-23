# 面板隨機效果 Logit 模型 (Panel Random Effects Logit Model)

## 定義與理論機制 (Definition & Mechanism)
在分析個體微觀決策（如是否進入初婚、是否全職就業、是否生育下一胎）時，因變數為二元離散變數（$0$ 或 $1$）。當資料具備多期追蹤結構（Longitudinal/Panel Data）時，個體內部在不同年份的決策存在持續性且不隨時間變化的個人稟賦（如社交外向度、人格特質、對家庭的偏好）。面板隨機效果 Logit 模型假定個體特定未觀察效應服從常態分配，透過邊際概似函數（Marginal Likelihood）積分，精確估計外生協變量對潛在勝算比（Odds Ratio）的真實影響。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
潛在連續傾向方程式（Latent Index Specification）：
$$
Y_{it}^* = \alpha + \mathbf{X}_{it}'\boldsymbol{\beta} + u_i + \varepsilon_{it}
$$
觀測二元變數：
$$
Y_{it} = \begin{cases} 1, & \text{if } Y_{it}^* > 0 \\ 0, & \text{if } Y_{it}^* \le 0 \end{cases}
$$

### 條件機率與勝算比形式 (Logistic Cumulative Distribution)
$$
\Pr(Y_{it} = 1 \mid \mathbf{X}_{it}, u_i) = \Lambda(\alpha + \mathbf{X}_{it}'\boldsymbol{\beta} + u_i) = \frac{\exp(\alpha + \mathbf{X}_{it}'\boldsymbol{\beta} + u_i)}{1 + \exp(\alpha + \mathbf{X}_{it}'\boldsymbol{\beta} + u_i)}
$$
$$
\ln\left( \frac{\Pr(Y_{it} = 1 \mid \mathbf{X}_{it}, u_i)}{1 - \Pr(Y_{it} = 1 \mid \mathbf{X}_{it}, u_i)} \right) = \alpha + \mathbf{X}_{it}'\boldsymbol{\beta} + u_i
$$

### 隨機效果分佈與邊際概似函數 (Gauss-Hermite Quadrature)
$$
u_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma_u^2), \quad L = \prod_{i=1}^N \int_{-\infty}^{\infty} \left[ \prod_{t=1}^{T_i} \Lambda(\mathbf{X}_{it}'\boldsymbol{\beta} + u)^{Y_{it}} (1 - \Lambda(\mathbf{X}_{it}'\boldsymbol{\beta} + u))^{1 - Y_{it}} \right] \frac{1}{\sqrt{2\pi}\sigma_u} e^{-\frac{u^2}{2\sigma_u^2}} du
$$
* 組內相關係數（Intra-class Correlation Coefficient）：
$$
\rho_{\text{panel}} = \frac{\sigma_u^2}{\sigma_u^2 + \pi^2/3}
$$

## 優點與適用情境 (Strengths & Use Cases)
* 能夠同時估計不隨時間變化的協變量效應（如性別、原生家庭背景、特定學歷）。
* 適合追蹤樣本中離散婚育事件之動態估計。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 嚴格要求個體隨機效果 $u_i$ 與所有自變數 $\mathbf{X}_{it}$ 正交獨立（若不獨立需採用 Mundlak 修正或條件固定效果 Logit）。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P17-Yen24-TaiwanMarriageLogit]]：以 PSFD 追蹤微觀數據檢驗男女薪資與工時對初婚勝算之非對稱影響。
* [[P20-Cheng23-PremaritalRelationships]]：離散時間事件史轉換機率分析。
* [[P23-Yang23-MiddleAgedAlwaysSingle]]：中年單身生活樣態之多項式 Logit 模型。
