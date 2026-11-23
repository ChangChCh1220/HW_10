# 雙向固定效果面板模型 (Two-Way Fixed Effects Panel Model, TWFE)

## 定義與理論機制 (Definition & Mechanism)
雙向固定效果面板模型是實證計量經濟學中處理多個個體（如縣市、家戶、國家）在多個時期縱橫資料（Panel Data）的基準工具。其核心機制在於透過虛擬變數或「個體內部去均值變換（Within Transformation）」，同時控制：
1. **個體不隨時間變動之不可觀測異質性（Time-Invariant Individual Heterogeneity, $\mu_i$）**：例如縣市的天然地理區位、初始文化稟賦或歷史都市規模。
2. **總體不隨個體變動之不可觀測時間趨勢（Individual-Invariant Time Effects, $\lambda_t$）**：例如全國總體經濟繁榮/衰退、通貨膨脹衝擊或央行基準利率循環。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
$$
Y_{it} = \beta_0 + \mathbf{X}_{it}'\boldsymbol{\beta} + \mu_i + \lambda_t + \varepsilon_{it}
$$

### 變數定義與去均值運算
* $Y_{it}$：個體 $i$ 於時間 $t$ 之被解釋變數（例如一般生育率、粗出生率）。
* $\mathbf{X}_{it}$：隨時間與個體變動的外生解釋變數向量（例如房價所得比、家戶所得）。
* $\mu_i$：個體固定效果；$\lambda_t$：時間固定效果；$\varepsilon_{it}$：外生隨機誤差項，假定 $\mathbb{E}[\varepsilon_{it} \mid \mathbf{X}_{i1}, \dots, \mathbf{X}_{iT}, \mu_i, \lambda_t] = 0$。
* 消除 $\mu_i$ 之個體內部變換（Within Transformation）：
$$
(Y_{it} - \bar{Y}_i) = (\mathbf{X}_{it} - \bar{\mathbf{X}}_i)'\boldsymbol{\beta} + (\lambda_t - \bar{\lambda}) + (\varepsilon_{it} - \bar{\varepsilon}_i)
$$

## 優點與適用情境 (Strengths & Use Cases)
* **消除遺漏變數偏誤**：只要遺漏的混雜因子（Confounder）是不隨時間變動的個體特質，固定效果即可徹底剔除其內生性偏差。
* **標準面板分析**：廣泛應用於區域總體計量、勞動經濟學與公共政策評估。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* **無法估計時間固定特徵之係數**：若某些變數不隨時間改變（如地理面積），將在去均值運算中被完全消去。
* **無法控制隨時間動態變化的個體專屬衝擊**。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P01-Yao24-HousePriceFertility]]：以台灣 19 縣市雙向固定效果模型評估房價所得比對一般生育率之因果衝擊。
* [[P07-Wu25-TaiwanCityFertility]]：結合動態面板 GMM 控制固定效果與動態滯後項。
* [[P15-Chien24-TaiwanPronatalistPolicies]]：六都 158 行政區之雙向固定效果面板回歸。
