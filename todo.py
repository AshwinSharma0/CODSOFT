import os
from datetime import datetime

class Todolist:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        task_dict = {
            'task': task,
            'completed': False,
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'date_completed': None
        }
        self.tasks.append(task_dict)
        print("\n Task added successfully!")
        
    def view_tasks(self):
        if not self.tasks:
            print("\n No tasks in your to-do list!")
            return
            
        print("\n Your To-Do List:")
        
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else " "
            print(f"{i}. [{status}] {task['task']}")
            print(f"   Added: {task['date_added']}")
            if task['completed'] and task['date_completed']:
                print(f"   Completed: {task['date_completed']}")
       
        
    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            if not task['completed']:
                task['completed'] = True
                task['date_completed'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\n Task marked as completed!")
            else:
                print("\n Task is already completed!")
        else:
            print("\n Invalid task number!")
            
    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"\n Task '{removed_task['task']}' deleted successfully!")
        else:
            print("\n Invalid task number!")
            
    def update_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['task'] = new_task
            print("\n Task updated successfully!")
        else:
            print("\n Invalid task number!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_number(value):
    if value.isdigit():
        number = int(value)
        if number > 0:
            return True
    return False

def main():
    todo_list = Todolist()
    
    while True:
        clear_screen()
        print("\n To-Do List Application")
       
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            task = input("\nEnter the task: ")
            todo_list.add_task(task)
            
        elif choice == '2':
            todo_list.view_tasks()
            
        elif choice == '3':
            todo_list.view_tasks()
            task_input = input("\nEnter the task number to mark as completed: ")
            if is_valid_number(task_input):
                task_index = int(task_input)
                todo_list.mark_completed(task_index)
            else:
                print("\n Please enter a valid number!")
                
        elif choice == '4':
            todo_list.view_tasks()
            task_input = input("\nEnter the task number to delete: ")
            if is_valid_number(task_input):
                task_index = int(task_input)
                todo_list.delete_task(task_index)
            else:
                print("\n Please enter a valid number!")
                
        elif choice == '5':
            todo_list.view_tasks()
            task_input = input("\nEnter the task number to update: ")
            if is_valid_number(task_input):
                task_index = int(task_input)
                new_task = input("Enter the new task: ")
                todo_list.update_task(task_index, new_task)
            else:
                print("\n Please enter a valid number!")
                
        elif choice == '6':
            print("\n Thank you for using the To-Do List Application!")
            break
            
        else:
            print("\n Invalid choice! Please try again")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
