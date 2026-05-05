from flask import render_template, request, redirect, url_for, session
from . import task_bp

@task_bp.route('/')
def index():
    # TODO: 取得目前登入使用者的任務列表，並渲染 index.html
    return render_template('index.html')

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    # TODO: 接收表單資料，新增任務到資料庫
    pass

@task_bp.route('/tasks/<int:task_id>/edit', methods=['GET'])
def edit_task_page(task_id):
    # TODO: 根據 task_id 取得特定任務，渲染 edit.html
    return render_template('edit.html')

@task_bp.route('/tasks/<int:task_id>/update', methods=['POST'])
def update_task(task_id):
    # TODO: 接收表單資料，更新特定任務
    pass

@task_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    # TODO: 從資料庫中刪除特定任務
    pass

@task_bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    # TODO: 切換特定任務的完成狀態
    pass
