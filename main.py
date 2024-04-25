import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class CafeManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cafe Management System")
        self.master.geometry("800x600")
        self.current_page = None
        self.waiter_tasks = []
        self.current_waiter = None

        self.show_main_page()

    def show_main_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text="Welcome to Restaurant Management "
                                         "System", font=("Arial", 20)).pack(pady=20)

        manager_button = tk.Button(self.current_page, text="Manager", font=("Arial", 14), width=15, height=2, command=self.show_manager_page)
        manager_button.pack(pady=20)
        bartender_button = tk.Button(self.current_page, text="Waiter", font=("Arial", 14), width=15, height=2, command=self.show_waiter_selector)
        bartender_button.pack(pady=20)

    def show_manager_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text="Manager Page", font=("Arial", 20)).pack(pady=20)

        home_button = tk.Button(self.current_page, text="Home", font=("Arial", 14), width=15,
                                command=self.show_main_page)
        home_button.pack(pady=10)

        assign_button = tk.Button(self.current_page, text="Add Assignment",
                                  font=("Arial", 14), width=15,
                                  command=self.assign_task)
        assign_button.pack(pady=5)

        delete_button = tk.Button(self.current_page, text="Delete Assignment",
                                  font=("Arial", 14), width=15,
                                  command=self.delete_task)
        delete_button.pack(pady=5)

        add_waiter_button = tk.Button(self.current_page, text="Add Waiter", font=("Arial", 14), width=15,
                                         command=self.add_waiter)
        add_waiter_button.pack(pady=5)

        delete_waiter_button = tk.Button(self.current_page,
                                            text="Delete Waiter",
                                            font=("Arial", 14), width=15,
                                            command=self.delete_waiter)
        delete_waiter_button.pack(pady=5)

        view_button = tk.Button(self.current_page, text="View Tasks", font=("Arial", 14), width=15,
                                command=self.view_tasks)
        view_button.pack(pady=5)

        view_checkins_button = tk.Button(self.current_page, text="View Check-Ins", font=("Arial", 14), width=15,
                                         command=self.view_checkins)
        view_checkins_button.pack(pady=5)

        view_checkouts_button = tk.Button(self.current_page,
                                         text="View Check-Outs",
                                         font=("Arial", 14), width=15,
                                         command=self.view_checkouts)
        view_checkouts_button.pack(pady=5)

    def add_waiter(self):
        waiter_window = tk.Toplevel(self.master)
        tk.Label(waiter_window, text="Add Waiter", font=("Arial", 16)).pack(pady=10)
        waiter_entry = tk.Entry(waiter_window, width=30)
        waiter_entry.pack(pady=5)

        def add():
            waiter = waiter_entry.get().strip()
            if not waiter:
                messagebox.showwarning("Empty Waiter", "Please enter the full name of the waiter.")
                return

            with open("waiters.txt", "a") as file:
                file.write(f"{waiter}\n")
            messagebox.showinfo("Waiter Added", f"Waiter '{waiter}' added successfully.")
            waiter_window.destroy()

        tk.Button(waiter_window, text="Add", font=("Arial", 14), command=add).pack(pady=5)

    def show_waiter_selector(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text="Select Waiter", font=("Arial", 20)).pack(pady=20)

        with open("waiters.txt", "r") as file:
            waiters = [waiter.strip() for waiter in file.readlines()]

        waiter_var = tk.StringVar(self.current_page)
        waiter_var.set(waiters[0])
        waiter_dropdown = tk.OptionMenu(self.current_page, waiter_var, *waiters)
        waiter_dropdown.pack(pady=10)

        def select_waiter():
            self.current_waiter = waiter_var.get()
            self.show_waiter_page()

        tk.Button(self.current_page, text="Select", font=("Arial", 14), command=select_waiter).pack(pady=10)

    def show_waiter_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text=f"Waiter: {self.current_waiter}", font=("Arial", 20)).pack(pady=20)

        home_button = tk.Button(self.current_page, text="Home", font=("Arial", 14), width=15, command=self.show_main_page)
        home_button.pack(pady=10)

        checkin_button = tk.Button(self.current_page, text="Check-In",
                                   font=("Arial", 14), width=15,
                                   command=self.check_in)
        checkin_button.pack(pady=5)

        checkout_button = tk.Button(self.current_page, text="Check-Out",
                                    font=("Arial", 14), width=15,
                                    command=self.check_out)
        checkout_button.pack(pady=5)

        view_tasks_button = tk.Button(self.current_page, text="View All Tasks", font=("Arial", 14), width=15, command=self.view_all_tasks)
        view_tasks_button.pack(pady=5)

        mark_completed_button = tk.Button(self.current_page, text="Mark Task Completed", font=("Arial", 14), width=20, command=self.mark_task_completed)
        mark_completed_button.pack(pady=5)

    def check_out(self):
        checkout_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("checkouts.txt", "a") as file:
            file.write(
                f"{self.current_waiter} checked out at {checkout_time}\n")
        messagebox.showinfo("Check-Out", f"Checked out at {checkout_time}")

    def assign_task(self):
        task_window = tk.Toplevel(self.master)
        tk.Label(task_window, text="Add Assignment", font=("Arial", 16)).pack(
            pady=10)
        task_entry = tk.Entry(task_window, width=30)
        task_entry.pack(pady=5)

        with open("waiters.txt", "r") as file:
            waiters = [waiter.strip() for waiter in
                       file.readlines()]  # Eliminăm spațiile și caracterele de nouă linie în plus

        waiter_var = tk.StringVar(task_window)
        waiter_var.set(waiters[0])  # Nu mai avem nevoie de strip() aici
        waiter_dropdown = tk.OptionMenu(task_window, waiter_var, *waiters)
        waiter_dropdown.pack(pady=5)

        def assign():
            task = task_entry.get()
            waiter = waiter_var.get()
            if not task:
                messagebox.showwarning("Empty Assignment", "Please enter a "
                                                     "assignment.")
                return
            with open("tasks.txt", "a") as file:
                file.write(f"{task} (Waiter: {waiter}) (Pending)\n")
            task_window.destroy()

        tk.Button(task_window, text="Assign", font=("Arial", 14), command=assign).pack(pady=5)

    def delete_task(self):
        task_window = tk.Toplevel(self.master)
        tk.Label(task_window, text="Delete Assignment", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(task_window, width=50, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
        task_listbox.pack(pady=5)

        def delete():
            selected_task = task_listbox.curselection()
            if selected_task:
                task = task_listbox.get(selected_task)
                with open("tasks.txt", "r") as file:
                    lines = file.readlines()
                with open("tasks.txt", "w") as file:
                    for line in lines:
                        if task not in line:
                            file.write(line)
                messagebox.showinfo("Task Deleted", "Task deleted successfully.")
                task_window.destroy()
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to delete.")

        tk.Button(task_window, text="Delete", font=("Arial", 14), command=delete).pack(pady=5)

    def view_tasks(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="All Pending Tasks", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(view_window, width=50, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if "(Pending)" in task:
                    task_listbox.insert(tk.END, task.strip())
        task_listbox.pack(pady=5)

    def view_checkins(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="Check-Ins", font=("Arial", 16)).pack(pady=10)
        checkins_listbox = tk.Listbox(view_window, width=50, font=("Arial", 12))
        with open("checkins.txt", "r") as file:
            checkins = file.readlines()
            for checkin in checkins:
                checkins_listbox.insert(tk.END, checkin.strip())
        checkins_listbox.pack(pady=5)

    def view_checkouts(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="Check-Outs", font=("Arial", 16)).pack(
            pady=10)
        checkouts_listbox = tk.Listbox(view_window, width=50, font=("Arial",
                                                                  12))
        with open("checkouts.txt", "r") as file:
            checkouts = file.readlines()
            for checkout in checkouts:
                checkouts_listbox.insert(tk.END, checkout.strip())
        checkouts_listbox.pack(pady=5)

    def delete_waiter(self):
        waiter_window = tk.Toplevel(self.master)
        tk.Label(waiter_window, text="Delete Waiter", font=("Arial", 16)).pack(pady=10)
        waiter_listbox = tk.Listbox(waiter_window, width=50, font=("Arial", 12))
        with open("waiters.txt", "r") as file:
            waiters = file.readlines()
            for waiter in waiters:
                waiter_listbox.insert(tk.END, waiter.strip())
        waiter_listbox.pack(pady=5)

        def delete():
            selected_waiter = waiter_listbox.curselection()
            if selected_waiter:
                waiter = waiter_listbox.get(selected_waiter)
                with open("waiters.txt", "r") as file:
                    lines = file.readlines()
                with open("waiters.txt", "w") as file:
                    for line in lines:
                        if waiter not in line:
                            file.write(line)
                messagebox.showinfo("Waiter Deleted", f"Waiter '{waiter}' deleted successfully.")
                waiter_window.destroy()
            else:
                messagebox.showwarning("No Waiter Selected", "Please select a waiter to delete.")

        tk.Button(waiter_window, text="Delete", font=("Arial", 14), command=delete).pack(pady=5)

    def view_all_tasks(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="All Tasks", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(view_window, width=70, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if "(Completed)" in task:
                    task_listbox.insert(tk.END, task.strip())
                else:
                    task_listbox.insert(tk.END, task.strip() + " (Not Completed)")
        task_listbox.pack(pady=5)

    def mark_task_completed(self):
        task_window = tk.Toplevel(self.master)
        tk.Label(task_window, text="Mark Task Completed", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(task_window, width=50, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if self.current_waiter in task and "(Pending)" in task:
                    task_listbox.insert(tk.END, task.strip())
        task_listbox.pack(pady=5)

        def mark_completed():
            selected_task = task_listbox.curselection()
            if selected_task:
                task = task_listbox.get(selected_task)
                with open("tasks.txt", "r") as file:
                    lines = file.readlines()
                with open("tasks.txt", "w") as file:
                    for line in lines:
                        if task in line:
                            file.write(line.replace(" (Pending)", " (Completed)"))
                        else:
                            file.write(line)
                messagebox.showinfo("Task Completed", "Task marked as completed successfully.")
                task_window.destroy()
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

        tk.Button(task_window, text="Mark Completed", font=("Arial", 14), command=mark_completed).pack(pady=5)

    def check_in(self):
        checkin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("checkins.txt", "a") as file:
            file.write(f"{self.current_waiter} checked in at {checkin_time}\n")
        messagebox.showinfo("Check-In", f"Checked in at {checkin_time}")

def main():
    root = tk.Tk()
    app = CafeManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
