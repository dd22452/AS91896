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
    "Print All task": print_all,
    "Add task": add_tasks,
    "search": search,
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
       
       

def generate_report():
    generated_task ={"tasks completed": 0 ,"Number od tasks": 0 ,"Number of tasks blocked": 0 ,"Number of taks not started": 0}
main_menu()
