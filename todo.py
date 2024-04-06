from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1
TextArea = None
enterTaskField = None
taskNumberField = None

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return False
    return True

def clear_taskField():
    enterTaskField.delete(0, END)

def clear_taskNumberField():
    taskNumberField.delete(0, END)

def insertTask():
    global counter, enterTaskField
    if inputError():
        content = enterTaskField.get() + "\n"
        tasks_list.append(content)
        TextArea.insert(END, "[ " + str(counter) + " ] " + content)
        counter += 1
        clear_taskField()

def delete():
    global counter, taskNumberField
    if len(tasks_list) == 0:
        messagebox.showerror("No Task", "No task to delete")
        return
    number = taskNumberField.get()
    if number == "":
        messagebox.showerror("Input Error", "Please enter task number")
        return
    else:
        task_no = int(number)
    clear_taskNumberField()
    if task_no <= 0 or task_no > len(tasks_list):
        messagebox.showerror("Invalid Task Number", "Task number does not exist")
        return
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert(END, "[ " + str(i + 1) + " ] " + tasks_list[i])

def openToDoListWindow():
    global TextArea, enterTaskField, taskNumberField
    todo_window = Tk()
    todo_window.title("To-Do List")
    todo_window.geometry("250x300")

    enterTask = Label(todo_window, text="Enter Your Task", bg="light green")
    enterTaskField = Entry(todo_window)
    Submit = Button(todo_window, text="Submit", fg="Black", bg="Red", command=insertTask)
    TextArea = Text(todo_window, height=5, width=25, font="lucida 13")
    taskNumber = Label(todo_window, text="Delete Task Number", bg="blue")
    taskNumberField = Entry(todo_window)
    deleteButton = Button(todo_window, text="Delete", fg="Black", bg="Red", command=delete)
    exitButton = Button(todo_window, text="Exit", fg="Black", bg="Red", command=todo_window.destroy)

    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=50)
    Submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    deleteButton.grid(row=6, column=2, pady=5)
    exitButton.grid(row=7, column=2)

    for task in tasks_list:
        TextArea.insert(END, task)

    todo_window.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Main Window")

    openTodoButton = Button(root, text="Open To-Do List", command=openToDoListWindow)
    openTodoButton.pack()

    root.mainloop()
