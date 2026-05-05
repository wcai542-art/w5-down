# 流程圖設計 (Flowchart)

根據 `docs/PRD.md` 與 `docs/ARCHITECTURE.md`，以下是「任務管理系統」的使用者操作流程圖。您可以在 VS Code 中安裝 Mermaid Preview 擴充功能，或是將以下語法貼到 GitHub 或 [Mermaid Live Editor](https://mermaid.live/) 中查看圖表。

## 使用者操作流程

```mermaid
graph TD
    %% 節點定義
    Start([進入系統])
    Login{是否已登入?}
    LoginPage[登入 / 註冊頁面]
    Dashboard[任務列表首頁 Dashboard]
    
    Action{選擇操作}
    CreateTask[新增任務]
    EditTask[編輯任務]
    DeleteTask[刪除任務]
    ToggleStatus[切換完成狀態]
    
    SaveDB[(寫入/更新資料庫)]
    
    %% 流程線
    Start --> Login
    Login -- 否 --> LoginPage
    LoginPage -- 登入成功 --> Dashboard
    Login -- 是 --> Dashboard
    
    Dashboard --> Action
    
    Action -- 點擊「新增」 --> CreateTask
    Action -- 點擊「編輯」 --> EditTask
    Action -- 點擊「刪除」 --> DeleteTask
    Action -- 勾選完成 --> ToggleStatus
    
    CreateTask --> SaveDB
    EditTask --> SaveDB
    DeleteTask --> SaveDB
    ToggleStatus --> SaveDB
    
    SaveDB --> Dashboard
```

## 流程說明
1. **進入系統**：使用者存取網站首頁。
2. **驗證身份**：系統檢查 Session 確認使用者是否已登入，若無則導向登入/註冊頁面。
3. **任務列表首頁**：登入成功後，使用者會看到自己建立的所有任務。
4. **選擇操作**：
   - **新增任務**：填寫任務名稱、截止日期並提交。
   - **編輯任務**：修改現有的任務內容。
   - **刪除任務**：將不需要的任務從系統移除。
   - **切換完成狀態**：將任務標記為已完成或未完成。
5. **資料庫更新**：任何操作都會更新到 SQLite 資料庫中，更新完成後畫面會重新導向回任務列表首頁，顯示最新狀態。
