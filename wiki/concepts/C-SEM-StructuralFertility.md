# 動態結構生育離散選擇模型 (Dynamic Structural Discrete Choice Model)

## 定義與理論機制 (Definition & Mechanism)
動態結構離散選擇模型（Dynamic Programming Discrete Choice Model，源自 Rust 1987 及 Keane & Wolpin 1997）是計量經濟學中結合動態規劃與微觀計量的最前端技術。傳統簡約式計量（Reduced-form）只能估計既有政策下的事後統計相關，無法評估未曾實施過的新政策，且易受到盧卡斯批判（Lucas Critique）挑戰。結構模型直接從家庭之偏好效用函數、時間機會成本與預算限制出發，透過跨期貝爾曼方程式（Bellman Equation）逆向求解最適動態路徑，進而能夠進行嚴格的「反事實政策模擬（Counterfactual Policy Simulations）」。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
跨期值函數（Value Function）與貝爾曼方程式：
$$
V_t(S_t) = \max_{d_t \in \mathcal{D}} \left\{ U(C_t, N_t, d_t; \boldsymbol{\theta}) + \beta \mathbb{E}\left[ V_{t+1}(S_{t+1}) \mid S_t, d_t \right] \right\}
$$

### 狀態轉移方程式 (State Transitions)
$$
\begin{cases}
N_t = N_{t-1} + d_t^{\text{birth}} & \text{(累積子女數演化)} \\
\text{Wage}_{t+1} = \text{Wage}_t (1 + g(d_t^{\text{work}})) & \text{(人力資本與薪資成長)} \\
\text{Asset}_{t+1} = (1+r) \text{Asset}_t + w_t d_t^{\text{work}} - C_t - p_{\text{care}}(d_t^{\text{birth}}, \text{CarePolicy}) & \text{(資產累積動態)}
\end{cases}
$$

### 結構估計演算法 (Nested Fixed Point, NFXP)
* 內層循環（Inner Loop）：給定深層結構參數 $\boldsymbol{\theta}$，運用值迭代（Value Function Iteration）求解動態規劃不動點。
* 外層循環（Outer Loop）：將導出的選擇機率代入微觀縱向面板數據，以最大概似法（Maximum Likelihood）更新估計深層參數 $\boldsymbol{\theta}$。

## 優點與適用情境 (Strengths & Use Cases)
* 能夠預測全新政策工具（如發放未曾有過的高額育嬰津貼或普及托育）的反事實反應，並精確計算政府每促成一個新生兒的財政邊際成本。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 運算複雜度極高（維度災難 Curse of Dimensionality），且模型結果高度依賴效用函數形式之理論假設。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P05-Lee25-StructuralFertilityKorea]]：韓國動態生育抉擇與家庭津貼結構模型反事實模擬。
* [[P02-Choi25-KoreaHousingFertility]]：住房資產與微觀離散選擇模型。
* [[P09-VanWijk25-TenureGroupsHousing]]：青年成家生命週期競爭風險模型。
* [[P14-Doepke22-EconomicsOfFertilityNewEra]]：總體動態家庭協商模型理論基礎。
