import uuid


class ToDo:
    def __init__(self):
        try:
            todo_list = open('todo-list.txt', 'a')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            todo_list.close()

    def show_main_menu(self):
        # add while True:
        print('''== TODO LIST ==
[1] Show tasks
[2] add task
[3] complete task
[4] exit''')
        self.choice = input('Your choice: ').strip()

    def show_tasks(self):
        try:
            print('[ YOUR TASKS ]')
            todo_list = open('todo-list.txt')
            tasks = todo_list.readlines()
            if len(tasks) == 0:
                print('Empty list\n\n')
            else:
                for task in tasks:
                    print(' | '.join(task.split(';')))
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            todo_list.close()

    def add_task(self):
        try:
            todo_list = open('todo-list.txt', 'a')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            todo_list.close()

    def complete_task(self):
        try:
            todo_list = open('todo-list.txt', 'a')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            todo_list.close()

    def run(self):
        while True:
            self.show_main_menu()
            if self.choice == '4':
                return
            if self.choice in ('1', '2', '3'):
                if self.choice == '1':
                    self.show_tasks()
                if self.choice == '2':
                    self.add_task()
                if self.choice == '3':
                    self.complete_task()


todo = ToDo()
todo.run()
print(str(uuid.uuid4()))
