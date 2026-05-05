# 路由設計 (API & Route Design)

本文件定義系統中所有的 URL 路由，並指定每個路由負責的視圖模板或邏輯操作。

## 1. 身份驗證路由 (Auth Routes)
前綴: `/auth`

| HTTP Method | URL | 處理函數 | 說明 | 對應模板/動作 |
| ----------- | --- | -------- | ---- | ------------- |
| GET         | `/login` | `login_page()` | 顯示登入與註冊頁面 | `login.html` |
| POST        | `/login` | `process_login()` | 處理登入表單資料 | 成功: 導向 `/`, 失敗: 返回 `login.html` |
| POST        | `/register`| `process_register()`| 處理註冊表單資料 | 成功: 導向 `/login` |
| GET         | `/logout` | `logout()` | 登出使用者，清除 Session | 導向 `/auth/login` |

## 2. 任務管理路由 (Task Routes)
前綴: `/`

| HTTP Method | URL | 處理函數 | 說明 | 對應模板/動作 |
| ----------- | --- | -------- | ---- | ------------- |
| GET         | `/` | `index()` | 顯示使用者的所有任務列表 | `index.html` |
| POST        | `/tasks` | `create_task()` | 接收表單並新增任務 | 導向 `/` |
| GET         | `/tasks/<id>/edit`| `edit_task_page()`| 顯示特定任務的編輯頁面 | `edit.html` |
| POST        | `/tasks/<id>/update`| `update_task()`| 接收表單並更新特定任務 | 導向 `/` |
| POST        | `/tasks/<id>/delete`| `delete_task()`| 刪除特定任務 | 導向 `/` |
| POST        | `/tasks/<id>/toggle`| `toggle_task()`| 切換任務的完成狀態 | 導向 `/` |
