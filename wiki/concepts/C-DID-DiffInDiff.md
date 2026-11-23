# 雙重差分法 (Difference-in-Differences, DID)

## 定義與理論機制 (Definition & Mechanism)
雙重差分法是現代準實驗因果推論（Causal Inference）中最經典且廣泛應用的識別策略。透過比較「處理組（Treatment Group）」與「控制組（Control Group）」在政策介入前後的雙重差異，消除兩組之間不隨時間改變的固有特徵差異，以及所有組別共同經歷的時間自然趨勢，從而精確估計出政策或干預措施的因果處理效應（Average Treatment Effect on the Treated, ATT）。

## 關鍵數學推導或模型形式 (Mathematical Formulation)
基準 DID 迴歸模型形式：
$$
Y_{it} = \beta_0 + \beta_1 \text{Treat}_i + \beta_2 \text{Post}_t + \beta_3 (\text{Treat}_i \times \text{Post}_t) + \mathbf{X}_{it}'\boldsymbol{\gamma} + \varepsilon_{it}
$$

### 雙重差分算子定義
$$
\hat{\beta}_3^{\text{DID}} = \left( \mathbb{E}[Y_{i1} \mid \text{Treat}=1] - \mathbb{E}[Y_{i0} \mid \text{Treat}=1] \right) - \left( \mathbb{E}[Y_{i1} \mid \text{Treat}=0] - \mathbb{E}[Y_{i0} \mid \text{Treat}=0] \right)
$$

### 多期交錯 DID 與事件研究法 (Event Study)
$$
Y_{it} = \alpha_i + \lambda_t + \sum_{\tau = -K, \tau \ne -1}^M \beta_\tau \mathbf{1}(t - T_i^* = \tau) + \mathbf{X}_{it}'\boldsymbol{\delta} + \varepsilon_{it}
$$
* **平行趨勢假說 (Parallel Trends Assumption)**：要求在政策實施之前（$\tau < 0$），處理組與控制組的結果變數必須維持平行的時間軌跡（即所有事前係數 $\beta_\tau$ 統計上均不顯著異於零）。

## 優點與適用情境 (Strengths & Use Cases)
* 直觀且具備強大的因果說服力，特別適用於地方政府分階段實施法規改革（如各縣市在不同年份加碼生育津貼）。

## 局限性與常見挑戰 (Limitations & Pitfalls)
* 在交錯實施（Staggered DID）情境下，若存在異質性處理效應（Heterogeneous Treatment Effects），傳統雙向固定效果 OLS 估計量可能因「以早處理組作為晚處理組對照」而產生負權重偏誤（Negative Weighting Bias）。

## 庫內應用論文 (Applied Papers in Wiki)
* [[P04-Hsu23-NatalSubsidyDID]]：以台灣 368 鄉鎮市區月度行政面板評估地方生育津貼之動態因果效應與幽靈戶籍套利。
* [[P08-Koh26-ChildcareSubsidy]]：跨國大規模事件研究比較托育服務與現金補貼之長期反應。
