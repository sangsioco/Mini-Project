# Task and to-do list with specified feature
class Task:
    def __init__(self, title="Incomplete"):
        self.title = title
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. Title: {task.title}, Status: {task.status}")

    def mark_task_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")

# UI display
def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# User interaction
def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the title of the task: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as complete: "))
            todo_list.mark_task_complete(task_index)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
