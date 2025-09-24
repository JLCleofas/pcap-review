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
            self.tasks = todo_list.readlines()
            if len(self.tasks) == 0:
                print('Empty list\n\n')
            else:
                for task in self.tasks:
                    print(' | '.join(task.split(';')), end='')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            todo_list.close()

    def add_task(self):
        try:
            todo_list = open('todo-list.txt', 'a')
            task_input = input('What is the task? ')
            task_deadline = input('When is the deadline? ')
            todo_list.write(
                f'{str(uuid.uuid4())};{task_input};{task_deadline}\n')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            todo_list.close()

    def complete_task(self):
        try:
            # Read all tasks from the file
            with open('todo-list.txt', 'r') as todo_list:
                self.tasks = todo_list.readlines()

            # Show tasks
            self.show_tasks()

            # Get the ID to complete
            task_id = input('Enter id to complete: ').strip()

            # Find and remove the task with matching ID
            updated_tasks = []
            task_found = False
            for task in self.tasks:
                if task.startswith(task_id + ';'):
                    task_found = True
                else:
                    updated_tasks.append(task)

            if task_found:
                # Write the updated list back to the file
                with open('todo-list.txt', 'w') as todo_list:
                    todo_list.writelines(updated_tasks)
                print('Task completed and removed.')
            else:
                print('Task ID not found.')
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
