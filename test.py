from tkinter import *
import json

class Project:
    def __init__(self, name):
        self.name = name
        self.databases = []

class Database:
    def __init__(self, name):
        self.name = name
        self.buckets = []

class Bucket:
    def __init__(self, name):
        self.name = name
        self.data = {}

class App:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()
        self.projects = []
        self.current_project = None
        self.current_database = None

        self.sidebar = Frame(self.frame, width=200, bg='white')
        self.sidebar.pack(side=LEFT, fill=Y)

        self.add_project_button = Button(self.sidebar, text='+ Project', command=self.add_project)
        self.add_project_button.pack(side=TOP, pady=10)

        self.project_list = Listbox(self.sidebar, width=20, height=25)
        self.project_list.pack(side=TOP)
        self.project_list.bind('<<ListboxSelect>>', self.select_project)

        self.view = Frame(self.frame, width=600, height=400)
        self.view.pack(side=RIGHT)

        self.add_database_button = Button(self.view, text='+ Database', command=self.add_database)
        self.add_database_button.pack(side=TOP, pady=10)

        self.database_list = Listbox(self.view, width=60, height=25)
        self.database_list.pack(side=TOP)
        self.database_list.bind('<<ListboxSelect>>', self.select_database)

        self.bucket_list = Listbox(self.view, width=60, height=25)
        self.bucket_list.pack(side=TOP)
        self.bucket_list.bind('<<ListboxSelect>>', self.select_bucket)

        self.load_projects()

    def add_project(self):
        name = simpledialog.askstring('Name', 'Project name:')
        if name:
            project = Project(name)
            self.projects.append(project)
            self.project_list.insert(END, name)
            self.save_projects()

    def delete_project(self):
        for project in self.projects:
            if project.name == self.current_project:
                self.projects.remove(project)
                break
        self.current_project = None
        self.load_projects()
        self.save_projects()

    def rename_project(self):
        name = simpledialog.askstring('Name', 'Project name:')
        if name:
            for project in self.projects:
                if project.name == self.current_project:
                    project.name = name
                    break
            self.current_project = name
            self.load_projects()
            self.save_projects()

    def add_database(self):
        name = simpledialog.askstring('Name', 'Database name:')
        if name:
            database = Database(name)
            for project in self.projects:
                if project.name == self.current_project:
                    project.databases.append(database)
                    break
            self.load_databases()
            self.save_projects()

    def delete_database(self):
        for project in self.projects:
            if project.name == self.current_project:
                for database in project.databases:
                    if database.name == self.current_database:
                        project.databases.remove(database)
                        break
                break
        self.current_database = None
        self.load_databases()
        self.save_projects()

    def rename_database(self):
        name = simpledialog.askstring('Name', 'Database name:')
        if name:
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        if database.name == self.current_database:
                            database.name = name
                            break
                    break
            self.current_database = name
            self.load_databases()
            self.save_projects()

    def add_bucket(self):
        name = simpledialog.askstring('Name', 'Bucket name:')
        if name:
            bucket = Bucket(name)
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        if database.name == self.current_database:
                            database.buckets.append(bucket)
                            break
                    break
            self.load_buckets()
            self.save_projects()

    def delete_bucket(self):
        for project in self.projects:
            if project.name == self.current_project:
                for database in project.databases:
                    if database.name == self.current_database:
                        for bucket in database.buckets:
                            if bucket.name == self.current_bucket:
                                database.buckets.remove(bucket)
                                break
                        break
                break
        self.current_bucket = None
        self.load_buckets()
        self.save_projects()

    def rename_bucket(self):
        name = simpledialog.askstring('Name', 'Bucket name:')
        if name:
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        if database.name == self.current_database:
                            for bucket in database.buckets:
                                if bucket.name == self.current_bucket:
                                    bucket.name = name
                                    break
                            break
                    break
            self.current_bucket = name
            self.load_buckets()
            self.save_projects()

    def add_data(self):
        key = simpledialog.askstring('Key', 'Data key:')
        if key:
            value = simpledialog.askstring('Value', 'Data value:')
            if value:
                for project in self.projects:
                    if project.name == self.current_project:
                        for database in project.databases:
                            if database.name == self.current_database:
                                for bucket in database.buckets:
                                    if bucket.name == self.current_bucket:
                                        bucket.data[key] = value
                                        break
                                break
                        break
                self.load_data()
                self.save_projects()

    def delete_data(self):
        for project in self.projects:
            if project.name == self.current_project:
                for database in project.databases:
                    if database.name == self.current_database:
                        for bucket in database.buckets:
                            if bucket.name == self.current_bucket:
                                del bucket.data[self.current_key]
                                break
                        break
                break
        self.load_data()
        self.save_projects()

    def rename_data(self):
        key = simpledialog.askstring('Key', 'Data key:')
        if key:
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        if database.name == self.current_database:
                            for bucket in database.buckets:
                                if bucket.name == self.current_bucket:
                                    value = bucket.data[self.current_key]
                                    del bucket.data[self.current_key]
                                    bucket.data[key] = value
                                    break
                            break
                    break
            self.load_data()
            self.save_projects()

    def select_project(self, event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        self.current_project = picked
        self.load_databases()

    def select_database(self, event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        self.current_database = picked
        self.load_buckets()

    def select_bucket(self, event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        self.current_bucket = picked
        self.load_data()

    def load_projects(self):
        self.project_list.delete(0, END)
        for project in self.projects:
            self.project_list.insert(END, project.name)
        self.clear_view()

    def load_databases(self):
        self.database_list.delete(0, END)
        if self.current_project:
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        self.database_list.insert(END, database.name)
                    break
        self.clear_buckets()

    def load_buckets(self):
        self.bucket_list.delete(0, END)
        if self.current_database:
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        if database.name == self.current_database:
                            for bucket in database.buckets:
                                self.bucket_list.insert(END, bucket.name)
                            break
                    break
        self.clear_data()

    def load_data(self):
        self.data_list.delete(0, END)
        if self.current_bucket:
            for project in self.projects:
                if project.name == self.current_project:
                    for database in project.databases:
                        if database.name == self.current_database:
                            for bucket in database.buckets:
                                if bucket.name == self.current_bucket:
                                    for key in bucket.data:
                                        self.data_list.insert(END, key)

    def clear_view(self):
        self.add_database_button.pack_forget()
        self.database_list.pack_forget()
        self.bucket_list.pack_forget()
        self.data_list.pack_forget()

    def clear_buckets(self):
        self.bucket_list.delete(0, END)
        self.bucket_list.pack_forget()
        self.data_list.delete(0, END)
        self.data_list.pack_forget()

    def clear_data(self):
        self.data_list.delete(0, END)
        self.data_list.pack_forget()

    def save_projects(self):
        with open('projects.json', 'w') as file:
            json.dump([project.__dict__ for project in self.projects], file)

root = Tk()
root.title('GUI Database App')
app = App(root)
root.mainloop()