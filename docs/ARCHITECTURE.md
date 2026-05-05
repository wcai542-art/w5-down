# 系統架構設計 (Architecture Design)

## 1. 專案概述
本專案為一個「任務管理系統」，基於 Python Web 開發技術棧構建，主要用於提供使用者任務的 CRUD（新增、讀取、更新、刪除）功能。

## 2. 技術棧 (Tech Stack)
* **後端框架**：Flask (Python)
* **前端模板**：Jinja2 (HTML/CSS)
* **資料庫**：SQLite

## 3. 目錄結構設計
根據 Flask 的最佳實踐，專案目錄結構設計如下：

```
flask-task-manager/
├── app/
│   ├── __init__.py      # Flask 應用程式工廠與初始化
│   ├── models/          # 資料庫模型 (Models)
│   │   └── task.py      # 任務資料表設計
│   ├── routes/          # 路由與控制器 (Controllers)
│   │   └── task_routes.py
│   ├── templates/       # HTML 模板 (Views)
│   │   ├── base.html
│   │   ├── index.html
│   │   └── edit.html
│   └── static/          # 靜態檔案 (CSS, JS, 圖片)
│       └── style.css
├── database/
│   └── schema.sql       # 資料庫建表語法
├── docs/                # 專案設計文件
│   ├── PRD.md
│   └── ARCHITECTURE.md
├── requirements.txt     # Python 依賴套件清單
└── run.py               # 應用程式啟動檔
```

## 4. 架構運作流程 (MVC Pattern)
1. **使用者 (Client)** 透過瀏覽器發送 HTTP 請求（例如：`GET /tasks`）。
2. **路由 (Routes/Controller)** 接收請求，並呼叫對應的邏輯處理函數。
3. **模型 (Models)** 與 SQLite 資料庫互動，執行資料查詢或更新。
4. **視圖 (Templates/View)** 路由取得資料後，將其傳遞給 Jinja2 模板引擎進行渲染。
5. 渲染完成的 HTML 返回給使用者。
