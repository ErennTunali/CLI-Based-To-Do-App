from database import *

databasePath = '/Users/erentunali/repos/CLI-Based-To-Do-App/tasks.db'

while (True):
    print('Welcome to the task manager\n\n')
    print('''
Commands:
          init: Create Database
          q: Exit
        







\n\n''')
    command = input('Enter Command: ')
    if (command == 'q'):
        break
    elif command == 'init':
        initDB(databasePath)
        print('DB initiliazed')
    elif command == 'add':
        task = input('Enter task: ')
        addTask(databasePath, task)
    elif command == 'list':
        tasks = listTasks(databasePath)
        print(tasks)
    
    