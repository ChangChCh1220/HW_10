# 空間杜賓模型 (Spatial Durbin Model, SDM)

## 定義與理論機制 (Definition & Mechanism)
空間杜賓模型是空間計量經濟學（Spatial Econometrics）的核心架構。傳統計量學常假定各個觀測單元相互獨立（Stable Unit Treatment Value Assumption, SUTVA），但在地理與區域經濟現實中，相鄰地區之間存在高度的要素流動、通勤生活圈與政策示範模仿。空間杜賓模型同時納入了「被解釋變數之空間滯後項（$W Y$）」以及「解釋變數之空間滯後項（$W X$）」，是唯一能同時捕捉內生空間外溢（Endogenous Interaction）與外生空間外溢（Exogenous Interaction）的全面性巢狀模型。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
$$
Y_{it} = \rho \sum_{j=1}^N W_{ij} Y_{jt} + \beta X_{it} + \sum_{j=1}^N W_{ij} X_{jt} \theta + \mu_i + \lambda_t + \varepsilon_{it}
$$

### 矩陣形式與效應分解 (Direct, Indirect, Total Effects)
$$
\mathbf{Y}_t = (\mathbf{I}_N - \rho \mathbf{W})^{-1} (\mathbf{X}_t \boldsymbol{\beta} + \mathbf{W} \mathbf{X}_t \boldsymbol{\theta}) + (\mathbf{I}_N - \rho \mathbf{W})^{-1} (\boldsymbol{\mu} + \lambda_t \boldsymbol{\iota}_N + \boldsymbol{\varepsilon}_t)
$$
偏微分邊際效應矩陣為：
$$
\mathbf{S}_r(\mathbf{W}) = \frac{\partial \mathbf{Y}}{\partial X_{r}} = (\mathbf{I}_N - \rho \mathbf{W})^{-1} \begin{bmatrix} \beta_r & W_{12}\theta_r & \cdots & W_{1N}\theta_r \\ W_{21}\theta_r & \beta_r & \cdots & W_{2N}\theta_r \\ \vdots & \vdots & \ddots & \vdots \\ W_{N1}\theta_r & W_{N2}\theta_r & \cdots & \beta_r \end{bmatrix}
$$
* **直接效果 (Direct Effect)**：對角線元素之平均值，測量本縣市自變數變動對本縣市生育率之衝擊（含反饋回流）。
* **間接效果 (Indirect/Spillover Effect)**：非對角線元素之和平均值，測量本縣市變動對鄰近所有縣市之空間外溢影響。
* **總效果 (Total Effect)** = 直接效果 + 間接效果。

## 優點與適用情境 (Strengths & Use Cases)
* 避免空間遺漏偏誤，具備模型檢定巢狀特質（可退化為 SAR 或 SEM 模型）。
* 適合分析交通網絡發達地區（如北北基桃生活圈）的房價外溢與生育人口遷徙。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 空間權重矩陣 $\mathbf{W}$ 的設定需嚴格的外生性論證，且點估計值不能直接解讀為邊際效應，必須透過矩陣求逆分解。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P03-Tsai21-HousingAffordabilitySpatial]]：評估台灣 20 縣市住宅負擔對粗出生率之直接、間接與總體空間效應。
