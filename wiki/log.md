# 知識庫操作日誌 (Wiki Operations Log)

> 本日誌為純追加（Append-only）的歷史紀錄。
> 每次執行 Ingest（攝取）、Query（重大查詢回寫）、Lint（健檢修復）或 Slide（簡報生成）後，Agent 均會在此追加一行標準前綴紀錄。
> 格式：`## [YYYY-MM-DD] <操作類型> | <簡述>`

---

## [2026-11-18] init | 建立知識庫架構與初始化目錄
- 建立 `raw/`, `wiki/` 目錄及其子目錄 (`papers/`, `concepts/`, `topics/`, `syntheses/`, `slides/`)。
- 初始化 `index.md` 與 `log.md`。
- 配置完成 `AGENTS.md`。

## [2026-11-18] config | 更新命名體系代號前綴與標準 LaTeX 數學規範
- `papers/` 採用 `P[編號或作者年份]-[簡稱]` 前綴體系。
- `concepts/` 採用 `C-[縮寫]-[簡稱]` 前綴體系。
- `topics/` 採用 `T-`，`syntheses/` 採用 `S-`，`slides/` 採用 `SL-`。
- 明確規定保留核心計量模型與數學推導，一律使用標準 LaTeX 公式表示並檢附變數定義對照表。

## [2026-11-19] maintain | 依使用者授權規範化 raw/papers/ PDF 檔名
- 將 `raw/papers/` 內全部 16 篇論文原始檔名重命名為標準 `P01-` 至 `P16-` 前綴格式，與 Wiki 命名空間完全一致。

## [2026-11-19] ingest | 批次攝取並標準化新加入之 7 篇論文 (P17-P23)
- 標準化檔名重命名：
  - `P17-Yen24-TaiwanMarriageLogit.pdf`：顏世昇（2024），PSFD 計量分析薪資、工時與房價對初婚之性別不對稱影響。
  - `P18-Lin23-HousingBeforeMarriage.pdf`：林佩萱、許碧純（2023），未婚男女「先有房再結婚」之態度與婚姻斜坡。
  - `P19-Chen26-MarriageMandatesParentalPressure.pdf`：Chen & Huang（2026, JMF），台灣青年受父母催婚壓力與初婚成效。
  - `P20-Cheng23-PremaritalRelationships.pdf`：Cheng（2023, JMF），同居率激增但與婚姻、生育脫鉤之少子化困境。
  - `P21-Liu26-MarriageIntentionsGenderRoles.pdf`：Liu（2026），未婚成人性別角色態度、個人自主性與結婚意願。
  - `P22-Yuan22-TaiwanMarriagePushPull.pdf`：袁詠蓁、孔祥明（2022），適婚青年進入婚姻之推離力與拉入單身力質性分析。
  - `P23-Yang23-MiddleAgedAlwaysSingle.pdf`：楊靜利、黃于珊、翁康容（2023），中年始終單身者之個人特徵、居住安排與家庭社會網絡。

## [2026-11-19] slide | 依通用 Graph 生產引擎重構 26 頁全圖表化互動簡報
- 確立通用生產引擎規範：雙軌並行因果架構（前端不婚 82% ＋ 後端不敢生 18%）。
- 嚴格落實四大核心改進：
  1. 徹底清除所有 `[[P..]]` 草稿代號，替換為優雅學術腳註。
  2. 100% 全圖表化（長條圖生長、橫條進場、動態天平傾斜、Y字型分流、冰山圖、雙軌 Master Graph）。
  3. 母片每頁右上角固定常駐三款去背 Logo（陽明交大 NYCU、學院所系徽、實驗室 Logo）。
  4. 實作 Kitagawa 公式動態分步點燈變色互動器（點擊 $\Delta M_a$ 亮金光連動 82% 長條生長，點擊 $\Delta F_a$ 亮藍光連動 18% 長條）。
- 產出自包含 HTML 檔案 `wiki/slides/SL-FER-TaiwanFertilityDecline.html` 與 Marp Markdown `wiki/slides/SL-FER-TaiwanFertilityDecline.md`。

## [2026-11-19] slide | 修正 HTML 簡報版面適配、長條標籤外置與移除全部 Logo
- 100% 視窗安全適配：CSS 設置 `top: 50%; left: 50%; transform-origin: center center;`，搭配 JS 向量縮放 `scale = Math.min(windowW / 1920, windowH / 1080) * 0.96`，保證所有螢幕解析度與全螢幕下均完整顯示、絕不超出或被邊框裁切。
- 徹底修復文字被切問題：將橫向長條排行（非婚生育率、未婚原因等）之百分比數值抽離至長條外側獨立容器 `.rank-val-outer`，解決台灣非婚生育率「3.8%」因長條過窄被切成「8%」之顯示錯誤。
- 依指示完全移除所有 Logo：全數移除 NYCU 校徽、學院徽與實驗室標誌，整體風格回歸純粹、極簡、大器之現代學術簡報美學。

## [2026-11-23] slide | 徹底消除雙象限對比頁面之巨大空白留白（重構第 9、12、15、16、19、21、24、25 頁）
- 重構雙象限卡片架構（`.duo-card`）：針對使用者指出的第 9、12、15、16、19、21、24、25 頁綠色/紅色卡片內留白過大、視覺空洞問題，進行全面升級。
- 引入「四層立體資訊圖表組件」：
  1. 卡片頂部標題（`.duo-card-header` 與 `.duo-card-title`）：清晰標註性別/族群/政策主題與圖示。
  2. 醒目核心數據橫條（`.duo-card-hero-metric`）：搭配淡色背景與粗體高對比數值標籤（如「初婚勝算 +18.2%」、「初婚勝算 -14.4%」、「頭期款延宕 15+ 年」等）。
  3. 三層次結構化論點模組（`.duo-card-items-list` 與 `.duo-card-item`）：將原先乾扁的 bullet 條列改為獨立卡片條塊，包含小標題與深入因果解析，自然均勻充盈垂直高度。
  4. 底部機制警訊與政策引申框（`.duo-card-callout`）：虛線邊框突顯核心結論與關鍵警訊。
- 徹底消除下半部巨大空洞，視覺平衡、大氣且資訊密度高，維持 100% 視窗自適應與無 Logo 極簡風格。

## [2026-11-23] slide | 精煉雙象限卡片文字並置中對齊，修復第 18 頁時間標籤斷行
- 修正第 18 頁排版：將長條圖容器寬度 `.bar-col` 自 260px 擴展至 380px，並加上 `white-space: nowrap`，徹底根除「時間」之「間」字被擠到下一行的斷行缺陷。
- 雙象限對比頁面精煉置中（第 9、12、15、16、19、21、24、25 頁）：
  1. 大幅精簡內文：去蕪存菁，改以「圖示 ＋ 粗體關鍵字 ＋ 單句精煉重點」呈現，字數精準節奏明快。
  2. 垂直水平絕對居中：設定 `.duo-card-grid` 採用 `max-width: 1480px; margin: 0 auto; align-items: center;`，讓兩側卡片以黃金比例置於畫面正中央，徹底消除上下空洞留白感與視覺壓迫。

## [2026-11-23] slide | 全面回歸「乾淨簡潔、大字大氣、無雜亂邊框」之極簡主義設計風格
- 升級雙象限對比版面（第 9、12、15、16、19、21、24、25 頁）：
  1. 徹底去除「框中套框、虛線、廉價底色」等雜亂裝飾，回歸 Swiss Minimalist 極簡設計。
  2. 放大版面尺度：卡片寬度擴大至 1560px 氣派展現，卡片內部 padding 擴至 36px 44px，邊框改為 2px 精緻微漸層淡色（#bbf7d0 / #fecdd3 / #e2e8f0），高雅大氣。
  3. 巨幅核心指標（Hero Stat）：採用 68px 超大粗體數字，第一秒直擊核心結論。
  4. 放大字體至 22-28px：標題 28px、要點 22px，採用乾淨簡潔的 `•` 無框條列，閱讀極為清晰舒適。
  5. 底部單線收尾：簡潔線條搭配 18px 重點小結，無多餘外框。

## [2026-11-23] config | 將本次驗證成功之頂級極簡簡報流程固化為系統規範 (AGENTS.md 工作流 D)
- 正式將「自適應視窗縮放引擎、極簡大字美學、無雜亂邊框、標籤防斷行機制、零 Logo 原則、公式分步點燈互動」固化為專案的標準簡報生成管線。
- 不論未來輸入任何主題的論文文獻，皆嚴格遵循此六階段標準化 Graph 流程與六維門禁檢驗執行。

## [2026-11-23] ingest | 完成全部 23 篇論文 Wiki 筆記建置 (P01-P23) 與概念/議題/綜述全庫體系
- 依據 `AGENTS.md` 第 4.1 節規範，在 `wiki/papers/` 完整建置 23 篇高規格單篇 Markdown 論文筆記：
  - 嚴格落實 9 大必要結構區塊（核心摘要、研究背景動機、理論框架與計量模型、資料來源樣本、實證表格、政策貢獻、限制未來方向、關聯引用）。
  - 核心計量回歸模型完整保留標準 LaTeX 數學公式（包含雙向固定效果、空間杜賓 SDM、多期 DID、合成控制 SCM、隨機效果 Logit、順序 Logit、雙變量 Probit、動態結構離散選擇 Bellman 方程式等），並逐一列明變數與符號定義。
  - 每篇均附完整實證估計表格（係數、標準誤、顯著性與經濟意涵）與 Obsidian 雙向鏈結（`[[C-...]]`, `[[T-...]]`, `[[P...]]`）。
- 同步建置 9 篇核心概念筆記（`wiki/concepts/`）：`C-FE-FixedEffects`, `C-SDM-SpatialDurbin`, `C-DID-DiffInDiff`, `C-SCM-SyntheticControl`, `C-LOGIT-RandomEffectsLogit`, `C-HWT-HouseworkDivision`, `C-MBP-MarriagePackage`, `C-HLM-HierarchicalLinearModel`, `C-SEM-StructuralFertility`。
- 同步建置 5 篇核心研究議題筆記（`wiki/topics/`）：`T-FER-FertilityDecline`, `T-HOU-HousingFertility`, `T-MAR-EastAsiaMarriageDecline`, `T-POL-PronatalistSubsidies`, `T-WFC-WorkFamilyConflict`。
- 同步撰寫 2 篇跨文獻橫向對比綜述（`wiki/syntheses/`）：
  - `S-FER-DualTrackCausality`：台灣超低生育率雙軌因果網絡全景綜述（含 Mermaid 因果流動圖與政策典範轉移）。
  - `S-SUB-ChildcareSubsidiesComparison`：地方現金生育津貼 vs. 托育公共化因果評估全景對照矩陣。
- 全面更新 `wiki/index.md` 分類導航與索引，知識庫實現 100% 雙向互聯與零斷鏈。
