from flask import render_template, request, redirect, url_for, session
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # TODO: 實作登入驗證邏輯
        pass
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    # TODO: 實作註冊邏輯
    pass

@auth_bp.route('/logout')
def logout():
    # TODO: 實作登出邏輯 (清除 session)
    pass
