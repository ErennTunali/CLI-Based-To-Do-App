from database import *

databasePath = '/Users/erentunali/repos/CLI-Based-To-Do-App/tasks.db'
initDB(databasePath)


print('Welcome to the task manager\n\n')
print('''
Commands:
          init: Create Database
          add: Add task
          done: complete task
          list: List tasks
          reset(use with caution): resets database
          q: Exit
        







\n\n''')

while (True):
    
    command = input('Enter Command: ')
    if (command == 'q'):
        break
    elif command == 'add':
        task = input('Enter task: ')
        addTask(databasePath, task)
    elif command == 'list':
        tasks = listTasks(databasePath)
        print(tasks)
    elif command == 'done':
        tasks = listTasks(databasePath)
        print(tasks)
        task = input('Enter task id to be updated: ')
        completeTask(databasePath, task)
    elif command == 'reset':
        confirmation = input('Are you sure(y/n): ')
        if confirmation == 'y':
            reset(databasePath)
            print('Table dropped, exiting...')
            break
        

    