import sqlite3

def get_db_connection():
    # 這裡的連線字串後續可以在系統整合時設定為動態路徑
    conn = sqlite3.connect('database/tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

class TaskModel:
    @staticmethod
    def get_all_tasks(user_id):
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC', (user_id,)).fetchall()
        conn.close()
        return tasks

    @staticmethod
    def create_task(user_id, title, description, due_date):
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (user_id, title, description, due_date) VALUES (?, ?, ?, ?)',
                     (user_id, title, description, due_date))
        conn.commit()
        conn.close()

    @staticmethod
    def update_task(task_id, title, description, due_date, is_completed):
        conn = get_db_connection()
        conn.execute('''
            UPDATE tasks 
            SET title = ?, description = ?, due_date = ?, is_completed = ?
            WHERE id = ?
        ''', (title, description, due_date, is_completed, task_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def toggle_status(task_id):
        conn = get_db_connection()
        task = conn.execute('SELECT is_completed FROM tasks WHERE id = ?', (task_id,)).fetchone()
        if task:
            new_status = not bool(task['is_completed'])
            conn.execute('UPDATE tasks SET is_completed = ? WHERE id = ?', (new_status, task_id))
            conn.commit()
        conn.close()
