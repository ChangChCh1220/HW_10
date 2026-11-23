# 論文知識庫系統規範 (AGENTS.md)

本檔案為本知識庫的核心系統規範（The Schema）。任何 LLM Agent 進入本專案時，皆必須嚴格遵守本文件所定義的架構、語意原則與操作工作流程。

---

## 1. 核心哲學與架構 (Core Philosophy & Architecture)

本專案實踐 **Karpathy LLM Wiki** 模式：知識庫不是單純的檢索增強生成（RAG），而是一個**持續累積、主動互聯、滾動更新的複利型知識資產（Persistent, Compounding Wiki）**。

系統包含三個層級：
1. **原始資料層 (`raw/`)**：不可變的客觀事實來源（Source of Truth）。包含 `raw/papers/`（PDF 或文件檔案）與 `raw/links.md`（論文網址或 DOI 清單）。**Agent 絕對不可修改或刪除此處的原始檔案。**
2. **知識庫層 (`wiki/`)**：由 LLM Agent 完全維護的結構化 Markdown 檔案。Agent 負責摘要、提煉概念、維護雙向鏈結、橫向對比與記錄日誌。使用者負責閱讀、探索與指引方向。
3. **規範層 (`AGENTS.md`)**：定義知識庫標準、命名規則與自動化工作流程。

---

## 2. 語言與格式標準 (Language & Formatting Conventions)

### 2.1 語意與語言標準
* **主要語言**：一律使用**繁體中文（台灣習慣用語）**撰寫（例如：「資料」、「演算法」、「資訊」、「脈絡」、「模型」、「計量」）。
* **專有名詞原則**：專有名詞、演算法名稱、理論框架、資料庫或專有指標，**保留英文原文**或採用**中英對照**。
  * 範例：`雙重差分法 (Difference-in-Differences, DID)`、`合成控制法 (Synthetic Control Method, SCM)`、`思維鏈 (Chain-of-Thought, CoT)`、`內生性 (Endogeneity)`。
  * 論文標題與引用文獻保持原文，重要結論與概念則用流暢精準的繁體中文解釋。

### 2.2 Obsidian 相容性規範
* **雙向鏈結**：一律採用 Obsidian 雙中括號格式 `[[檔案名稱]]` 或 `[[檔案名稱|顯示別名]]`。
* **數學推導與 LaTeX 標準**：
  * 若論文涉及**核心計量模型、回歸設定 (Regression Specification)、識別策略 (Identification Strategy)、數理推導或演算法公式**，必須**完整保留**，不可草率略過。
  * 一律使用標準 LaTeX 語法：行內公式 `$ ... $`，獨立區塊公式 `$$ ... $$`。
  * 重要模型或推導下方，必須逐項附上清晰的變數與符號定義（Variable Definitions）。
    * 範例：
      $$Y_{it} = \alpha_i + \lambda_t + \beta \text{Policy}_{it} + \mathbf{X}_{it}'\boldsymbol{\gamma} + \varepsilon_{it}$$
      * $Y_{it}$：個體 $i$ 在時間 $t$ 的生育率或勞動參與指標。
      * $\text{Policy}_{it}$：政策介入虛擬變數。
      * $\mathbf{X}_{it}$：外生控制變數向量。
* **YAML Frontmatter**：每個 Wiki 頁面頂部必須包含標準 YAML 區塊，以利 Obsidian Dataview 查詢與 Graph View 關聯。

---

## 3. 目錄結構與職責 (Directory Structure)

```text
HW_10/
├── AGENTS.md                  # 核心規範文件（本檔案）
├── raw/
│   ├── papers/                # 原始論文 PDF 或文字（唯讀）
│   └── links.md               # 外部論文網址與來源登記表
└── wiki/
    ├── index.md               # 知識庫全景目錄（分類導航）
    ├── log.md                 # 追加式操作日誌（時間戳歷史）
    ├── papers/                # 單篇論文結構化精讀筆記
    ├── concepts/              # 核心理論、架構、計量方法與機制
    ├── topics/                # 研究議題、政策領域、評測任務
    ├── syntheses/             # 跨論文橫向比較矩陣、爭議辨析與綜述
    └── slides/                # Marp / HTML 投影片檔案
```

---

## 4. 檔案命名體系與 Frontmatter 規範

為了在 Obsidian 鍵入雙括號時能快速自動補全、分類明確且視覺簡潔，全庫採用**「代號前綴 + 簡稱」**的結構化命名方式：

| 分類資料夾 | 命名規範 | 範例 | 說明 |
| :--- | :--- | :--- | :--- |
| `wiki/papers/` | `P[編號或作者年份]-[簡稱].md` | `P01-Yao24-FertilityPolicy.md`<br>`P02-Koh26-ChildcareSubsidy.md` | 輸入 `[[P` 即可列出所有論文卡片 |
| `wiki/concepts/` | `C-[簡短縮寫]-[概念簡稱].md` | `C-SCM-SyntheticControl.md`<br>`C-DID-DiffInDiff.md`<br>`C-HWT-HouseworkDivision.md` | 輸入 `[[C-` 即可查閱所有方法與理論 |
| `wiki/topics/` | `T-[領域縮寫]-[議題簡稱].md` | `T-FER-FertilityDecline.md`<br>`T-POL-FamilyPolicy.md` | 輸入 `[[T-` 即可檢索所有研究領域 |
| `wiki/syntheses/`| `S-[主題縮寫]-[綜述簡稱].md` | `S-SUB-SubsidyEffectiveness.md` | 輸入 `[[S-` 即可查閱所有文獻對比綜述 |
| `wiki/slides/` | `SL-[主題縮寫]-[簡報簡稱].md` | `SL-FER-FertilityOverview.md` | 輸入 `[[SL-` 即可找到所有演講簡報 |

---

### 4.1 單篇論文頁面 (`wiki/papers/`)
* **命名格式**：`P[編號或作者年份]-[簡稱].md`（如 `P01-Yao24-FertilityPolicy.md`）。
* **Frontmatter 格式**：
```yaml
---
id: "P01"
title: "論文完整標題"
authors: ["第一作者", "第二作者"]
year: 2024
venue: "發變化期刊/會議名稱"
source_type: "pdf" # 或 "url"
file_or_link: "raw/papers/xxx.pdf" # 或網址
tags: [paper, 關鍵字1, 關鍵字2]
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
```
* **正文必要區塊**：
  1. `# [代號] 論文標題`
  2. `## 核心摘要 (Executive Summary)`（3-5 點精華要點）
  3. `## 研究背景與動機 (Background & Motivation)`
  4. `## 理論框架與計量模型 (Methodology & Mathematical Formulation)`
     * 必須連結至對應的 `[[C-...]]` 概念頁。
     * **核心數學公式與推導**：若論文有回歸式、識別條件或數理推導，一律使用標準 LaTeX 區塊 `$$...$$` 完整保留，並逐一列明變數意涵。
  5. `## 資料來源與研究樣本 (Data & Sample)`
  6. `## 主要實證發現 (Key Empirical Findings)`（鼓勵使用 Markdown 表格摘要各項估計值、顯著性與經濟意涵）
  7. `## 政策意涵與學術貢獻 (Implications & Contributions)`（連結至對應的 `[[T-...]]` 議題頁）
  8. `## 限制與未來研究方向 (Limitations)`
  9. `## 關聯文獻與引用 (Related Works)`（使用 `[[P...]]` 連接庫內其他相關論文）

### 4.2 概念與方法頁面 (`wiki/concepts/`)
* **命名格式**：`C-[簡短縮寫]-[概念簡稱].md`（例如：`C-SCM-SyntheticControl.md`、`C-HWT-HouseworkDivision.md`）。
* **內容應包含**：
  1. `# 概念名稱 (中英對照)`
  2. `## 定義與理論機制 (Definition & Mechanism)`
  3. `## 關鍵數學推導或模型形式 (Mathematical Formulation)`（使用 LaTeX 公式）
  4. `## 優點與適用情境 (Strengths & Use Cases)`
  5. `## 局限性與常見挑戰 (Limitations & Pitfalls)`
  6. `## 庫內應用論文 (Applied Papers in Wiki)`（以雙向鏈結列表 `[[P...]]` 並註記各篇應用方式）

### 4.3 研究議題頁面 (`wiki/topics/`)
* **命名格式**：`T-[領域縮寫]-[議題簡稱].md`（例如：`T-FER-FertilityDecline.md`）。
* **內容應包含**：議題現狀、核心研究問題、學界主要爭議分歧點、各論文的論證觀點對照表（使用 Markdown 表格並連結 `[[P...]]`）。

---

## 5. Agent 核心工作流程 (Workflows)

### 工作流 A：論文攝取 (Ingest - 半自動批次模式)
當使用者發出 Ingest 請求（例如：「請分析 `raw/papers/` 中的論文」或「請攝取此 URL 論文」）：

1. **辨識與讀取**：
   - 若為 PDF，逐一檢視文件內容、提取元數據（作者、年份、標題、期刊/會議）。
   - 若為 URL，讀取網頁內容或 ArXiv 摘要。
2. **生成論文頁面**：
   - 在 `wiki/papers/` 建立對應 Markdown 檔案，嚴格按照 4.1 範本填寫。
3. **萃取與更新概念/議題 (Cross-referencing)**：
   - 識別該論文涉及的 2~4 個核心方法或概念（如特定的計量模型、社會學假說）。
   - 若 `wiki/concepts/` 或 `wiki/topics/` 尚無該頁面，則新建頁面；若已有該頁面，則將本篇論文的發現補充進該頁面的應用清單或實證對比中。
4. **檢查矛盾與理論演進**：
   - 檢查新論文的結論是否與庫內已有論文存在矛盾或提供新的反例，並在雙方頁面與議題頁面中標註（如：`[[P01-...]] 認為 X 顯著，但 [[P02-...]] 在控制 Y 後發現不顯著`）。
5. **更新目錄與日誌**：
   - 在 `wiki/index.md` 相應區塊加入新條目與簡短一句話摘要。
   - 在 `wiki/log.md` 追加一筆日誌：
     `## [YYYY-MM-DD] ingest | 攝取論文：[[P01-Yao24-FertilityPolicy]]`

### 工作流 B：查詢與知識複利 (Query & Compound)
當使用者針對知識庫提出跨論文研究問題（例如：「比較各篇對於生育津貼成效的研究結論」）：

1. **多面向檢索**：先檢視 `wiki/index.md` 與相關的 `wiki/topics/`、`wiki/concepts/`。
2. **綜合回答**：提供包含論證脈絡、對比矩陣與文獻引用（標註 `[[P...]]`）的繁體中文深度分析。
3. **主動知識回寫 (Compounding)**：
   - 若該問題的回答具備長期參考價值或為重要綜述，**主動將其寫入 `wiki/syntheses/`**（例如：`wiki/syntheses/S-SUB-ChildcareSubsidiesComparison.md`）。
   - 將新綜述登記至 `wiki/index.md` 並在 `wiki/log.md` 留下記錄。

### 工作流 C：知識庫健檢 (Lint)
定期或由使用者觸發維護作業：
1. **檢查斷鏈 (Broken Links)**：確保所有 `[[...]]` 指向的頁面皆存在。
2. **孤島頁面 (Orphans)**：尋找沒有任何入站鏈結（Inbound Links）的筆記，為其建立與主題或概念的連結。
3. **未索引頁面**：檢查是否有漏列於 `wiki/index.md` 的檔案。
4. **日誌記錄**：在 `wiki/log.md` 記錄 `## [YYYY-MM-DD] lint | 完成知識庫健檢與修復`。

### 工作流 D：高質感獨立 HTML 簡報生成規範 (Standardized Presentation Pipeline)
使用者需要簡報時（無論輸入何種主題之論文集，皆必須遵循本套固定標準流程與極簡大氣視覺體系）：

1. **核心美學守則（極簡主義 Swiss Minimalist & Apple 質感）**：
   - **大字大氣、格局開闊**：拒絕小家子氣的擁擠框框，中央舞台卡片寬度預設達 `1480px ~ 1560px`，內部間距大氣舒展。
   - **核心焦點巨型化（Hero Metric 68px+）**：每頁或每板塊之關鍵數值採用 `68px ~ 78px` 超大粗體展示，第一秒抓住聽眾眼球。
   - **去除廉價雜亂邊框**：**嚴禁框中套框、嚴禁虛線框、嚴禁高飽和刺眼粗框**。一律採用 `2px` 極淡精緻邊框（搭配純白與高雅微光漸層底色）。
   - **文字精煉、大字清晰**：標題 `28px`、要點 `22px`，採用純粹無框條列（`•`），每點一句話加粗關鍵詞，絕不放冗長段落。
   - **零 Logo 原則**：不放置任何校徽、學院徽或組織 Logo，回歸純粹專注於數據與因果論證之學術極簡大氣風格。

2. **核心技術規範（自包含、向量等比自適應、動態互動）**：
   - **100% 畫面等比適配引擎**：
     CSS 設定 `top: 50%; left: 50%; transform-origin: center center;`，搭配 JS 向量縮放演算法：
     `scale = Math.min(windowW / 1920, windowH / 1080) * 0.96; vp.style.transform = "translate(-50%, -50%) scale(" + scale + ")";`
     確保在任何解析度與全螢幕（`F` 鍵）下 100% 完整容納於視窗中央，四周留有舒適安全黑邊，永不跑版、永不被瀏覽器切邊。
   - **文字斷行保護機制**：
     - 長條圖或特定指標標籤若字數較多，一律加入 `white-space: nowrap;` 並給予充裕容器寬度（`width: >= 360px`），杜絕如「時間」之「間」字落單斷行之瑕疵。
     - 極端小比例長條圖（如數值 < 10%），數值標籤一律獨立抽離置於長條外側右端，絕不被容器裁切。
   - **公式動態分步點燈（Step-by-step Interactive Formula）**：
     若論文涉及核心數理分解公式，一律實作原生點燈互動器（點擊特定代號變色發光、連動對應貢獻度長條增長），完全自包含，不依賴外部脆弱 CDN。
   - **草稿代號清零**：投影片內嚴禁出現 `[[P01]]`、`[[P23]]` 等 Wiki 內部代號，一律轉換為權威機構或學者年份之正式學術引用標記。

3. **產出雙格式規範**：
   - 同步產出獨立無依賴之互動 HTML 簡報（`wiki/slides/SL-[主題]-[簡報名].html`）與 Marp Markdown 原始檔（`wiki/slides/SL-[主題]-[簡報名].md`）。
4. **日誌與索引登記**：更新 `wiki/index.md` 的簡報區塊，並追加 `wiki/log.md`。

---

## 6. Agent 行為守則與品質底線
- **事實準確性**：嚴格忠於 `raw/` 論文原意，嚴禁臆造未在論文出現的數據或結論。
- **簡潔直觀**：說明力求精準條理，多利用 Markdown 表格與分類條列。
- **自我更新**：每次修改維護後，務必同步維持 `index.md` 與 `log.md` 的即時性與乾淨度。
