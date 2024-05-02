import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        # Label
        self.label = tk.Label(root, text="Welcome to the To-Do List App!")
        self.label.pack()

        # Entry field for adding tasks
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        # Button to add task
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Listbox to display tasks
        self.task_list = tk.Listbox(root)
        self.task_list.pack()

        # Button to mark task as completed
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack()

        # Button to edit task
        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        # Button to delete task
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.itemconfig(selected_index, {'bg': 'light green'})
            # You can add logic to actually mark task as completed here

    def edit_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.task_list.get(selected_index)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task)

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    app.run()
