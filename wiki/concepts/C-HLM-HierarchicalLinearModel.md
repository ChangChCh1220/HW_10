# 階層線性回歸模型 (Hierarchical Linear Modeling, HLM)

## 定義與理論機制 (Definition & Mechanism)
階層線性模型（Hierarchical Linear Model, HLM，或稱多層次模型 Multilevel Model）用於處理具有巢狀階層結構（Nested Data Structure）的資料體系（例如：微觀家庭巢狀於行政區，行政區巢狀於直轄市縣市）。若直接使用一般 OLS 回歸，會忽視同群體內部觀測值之間的群聚相關（Clustering），低估標準誤而導致型一偏誤（Type I Error）。HLM 透過將微觀方程式的截距與斜率進一步設定為宏觀區域特徵之函數，精確分離出「個體層級特質」與「結構環境脈絡」的交互影響。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
### 第一層次：微觀個體/行政區模型 (Level 1 Model)
$$
Y_{ij} = \beta_{0j} + \beta_{1j} X_{ij} + \varepsilon_{ij}, \quad \varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)
$$

### 第二層次：宏觀城市/政策模型 (Level 2 Model)
$$
\begin{cases}
\beta_{0j} = \gamma_{00} + \gamma_{01} W_j + u_{0j} & \text{(隨機截距式)} \\
\beta_{1j} = \gamma_{10} + \gamma_{11} W_j + u_{1j} & \text{(隨機斜率式)}
\end{cases}
$$
其中：
$$
\begin{pmatrix} u_{0j} \\ u_{1j} \end{pmatrix} \sim \mathcal{N}_2 \left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} \tau_{00} & \tau_{01} \\ \tau_{01} & \tau_{11} \end{pmatrix} \right)
$$

### 複合回歸全模型 (Combined Model)
$$
Y_{ij} = \gamma_{00} + \gamma_{10} X_{ij} + \gamma_{01} W_j + \gamma_{11} (X_{ij} W_j) + [u_{0j} + u_{1j} X_{ij} + \varepsilon_{ij}]
$$
* $W_j$：直轄市層級政策變數（例如各市生育津貼加碼金額）。
* $X_{ij}$：行政區層級變數（例如公辦民營托育中心名額比率）。
* $\gamma_{11}$：跨層次交互作用係數（Cross-Level Interaction）。

## 優點與適用情境 (Strengths & Use Cases)
* 適用於評估地方政策與中央政策在微觀行政區尺度上的分層傳導機制。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 宏觀第二層次的群體數（$J$）若過少（如僅有六都 6 個單位），可能導致第二層次隨機變異數估計不穩定。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P15-Chien24-TaiwanPronatalistPolicies]]：六都 158 行政區之面板回歸與階層線性模型分析。
