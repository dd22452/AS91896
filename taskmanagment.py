import easygui
tasks = {
    "T1" : {
        "Title": "Design Homepage",
        "Description": "Create a mockup of the homepage",
        "Assignee": "JSM",
        "Priority": "3",
        "Status": "In Progress"
    },
    "T2": {
        "Title": "Implement Login page",
        "Description": "Create the login page for the website",
        "Assignee": "JSM",
        "Priority": "3",
        "Status": "Blocked"
    },
    "T3": {
        "Title": "Fix navigation menu",
        "Description": "Fix the navigation menu to be more user-friendly",
        "Assignee": "None",
        "Priority": "1",
        "Status": "Not Started"
    },
    "T4": {
          "Title": "Add payment processing",
        "Description": "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": "2",
        "Status": "In Progress"
    },
    "T5": {
          "Title": "Create an About Us page",
        "Description": "Create a page with information about the company ",
        "Assignee": "BDI",
        "Priority": "1",
        "Status": "Blocked"
    }
}

Team_members = {
    "JSM": {
        "Name": "John Smith",
        "Email": "Jhon@techvision.com",
        "Tasks Assigned": "T1, T2",
    },
    "JLO": {
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Tasks Assigned": "T4",
    },
    "BDI": {
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Tasks Assigned": "T5",
    }
}

def main_menu():
    options = {
    "Edit task": edit_task,
    "Print All Tasks": print_all,
    "Add task": add_tasks,
    "Search": task_search,
    "Generate Report": generate_report,
    "Exit": lambda: "N",
    }
    while True:
        msg = "What would you like to do?"
        title = "task Menu"
        choice = easygui.buttonbox(msg, title, list(options.keys()))
        get_input = options[choice]()
        if choice == None:
            break
        elif choice == "Exit":
            break

def task_search():
    """Allows the user to search for a task"""

    output =""
    search_task = []
    for titles in tasks:
         search_task.append(titles)

    msg = "What tasks would you like to search for?"
    title = "Task Search"

    search_choice = easygui.choicebox(msg, title, search_task)

    output = ""

    task_info = tasks[search_choice]

    for key, info in task_info.items():
        output += f"{key}:{info}\n"

    easygui.msgbox(output)

def member_search():
    """Search for a team member"""

    members = []
    for member in Team_members:
        members.append(member)

    msg = "What member do you want to search for?"
    title = "Member Search"
    choice = easygui.choicebox(msg, title, members)

    if choice == None:
        return

    member_info = Team_members[choice]
    output = ""



    for key, info in member_info.items():
        output += f"{key}:{info}\n"

    # info = Team_members[choice]

    easygui.msgbox(output)

def edit_task():
    """Allows the user to edit tasks"""

    output = ""
    task_titles = []
    for titles in tasks:
            task_titles.append(titles)

    msg = "What tasks would you like to edit in the details off?"
    title = "Tasks CHOICE"

    tasks_choice = easygui.choicebox(msg, title, task_titles )
    if tasks_choice is None:
        return

    task_info = []

    for task_information in tasks[tasks_choice]:
        task_info.append(task_information)

    msg = f"What detail of {tasks_choice} would you like to edit?"
    title = "EDIT CHOICE"

    edit_choice = easygui.choicebox(msg, title, task_info)

    msg = f"Enter the new {edit_choice} for  {tasks_choice}"
    title = f"ENTER NEW INFORMATION"


    tasks[tasks_choice][edit_choice] = easygui.enterbox(msg, title)

def add_tasks():
    title = easygui.enterbox("Enter the new title for your task:", "Add task")
    if title == None:
        return
   
    Description = easygui.enterbox("Enter your new task description "
    "for your new task", "Add task")
    if Description == None:
        return

    Assignee = easygui.enterbox("Enter the new Assignee for your new task",
                                 "Add task")
    if Assignee == None:
        return

    Priority = easygui.enterbox("Enter the priority of the new task", 
                                "Add new task")
    if Priority == None:
        return
    try:
        Priority = int(Priority)
    except ValueError:
            easygui.msgbox("Priority must be a valid number")

    status = easygui.enterbox("Enter the status of the new task", "Add task")
    if status == None:
        return

    new_task = {
    "Title": title,
    "Description": Description,
    "Assignee": Assignee,
    "Priority": Priority,
    "status": status,
               }

    new_task_id = f"T{len(tasks) + 1}"
   
    tasks[new_task_id] = new_task

    easygui.msgbox(f"Game '{title}' added successfully with rank{new_task_id}"
                   , "Success")
    return "Y"

def generate_report():
    not_started = 0
    blocked = 0
    in_progress = 0
    completed = 0

    for task_id, task in tasks.items():

        for key, value in task.items():

            if key == "Status":
               
                if value == "Not Started":
                    not_started += 1
                elif value == "Blocked":
                    blocked += 1
                elif value == "In Progress":
                    in_progress += 1
                elif value == "Completed":
                    completed += 1
                   
    easygui.msgbox(f"Not Started: {not_started}\n\
Blocked: {blocked}\nIn progress: {in_progress}\n\
Completed: {completed}", title="Progress Report")

    



def print_all():
    output = "Tasks:\n"
    for tasks_name, task_info in sorted(tasks.items()):
        output += f"\n{tasks_name}\n"
        for key in task_info:
            output += f"{key}: {task_info[key]}\n"
    easygui.msgbox(output, "All Tasks")
    return "Y"

    

    
def generate_report():
    """Generates a report of tasks"""

    task_count ={}

    for task, tasks in tasks:
        task = task [task]["tasks"]
        if task in task_count:
            task_count[task] = []
        task_count[task]

    output = "Tasks by Task:\n"
    for task, task_names in task_count.items():
        output += f"{task}: {','.join(task_names)}\n"
    generated_task ={"tasks completed": 0 ,"Number od tasks": 0 ,"Number of "
    "tasks blocked": 0 ,"Number of taks not started": 0}
main_menu()
