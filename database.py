import sqlite3


def connect(path):
    connection = sqlite3.connect(path)
    return connection



def initDB(path):
    conn = connect(path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, done BOOL DEFAULT 0)')
    conn.commit()
    conn.close()

def addTask(path, title):
    conn = connect(path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES(?)', (title, ))
    conn.commit()
    conn.close()
    
def listTasks(path):
    conn = connect(path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE done = 0')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def completeTask(path, taskID):
    conn = connect(path)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET done = 1 WHERE ID = ?', (taskID, ))
    conn.commit()
    conn.close()

def reset(path):
    conn = connect(path)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE tasks')
    conn.commit()
    conn.close



    


    