import easygui

Tasks = {
    "T1" : {
        "Title": "Design Homepage",
        "Description":"Create a mockup of the homepage",
        "Asignee":"JSM",
        "Priority":"3",
        "Status":"In progress",
    },

    "T2": {
        "Title": "Implement Login page",
        "Description":"Create the login page for the website",
        "Asignee":"JSM",
        "Priority":"3",
        "Status":"Blocked",
    },

    "T3": {
        "Title": "Fix Navigation menu",
        "Description":"Fix the naviation menu to be more user-friendly",
        "Asignee":"None",
        "Priority":"1",
        "Status":"Not Started",
    },

    "T4": {
        "Title": "Add payment processing",
        "Description":"Implement payment processing for the website",
        "Asignee":"JLO",
        "Priority":"2",
        "Status":"In Progress",
    },

    "T5": {
        "Title": "Create an About Us page",
        "Description":"Create a page with information about the company",
        "Asignee":"BDI",
        "Priority":"1",
        "Status":"Blocked",
    }
}

TeamMembers = {
    "JSM" :{
       "Name": "John Smith",
          "Email":  "John@techvision.com",
          "Tasks Assigned": "T1, T2",
    },
    "JLO":{
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Tasks Assigned": "T4",
    },
    "BDI":{
        "Name": "Bob Dillion",
        "Email":"Bob@techvision.com",
        "Tasks Assigned": "T4",  
    }

}

def add_tasks():
    """"Allows the user to add a new task to the dictionary"""

    title = easygui.enterbox("Enter new task title.")
    desc = easygui.enterbox("Enter task description.")
    assignee = easygui.enterbox("Enter team member ID (or leave empty):")
    priority = int(easygui.enterbox("Enter priority (1-5):"))
    status = easygui.choicebox("Select status", choices=["Not started", "In progress", "Blocked"])
    add_tasks =(title, desc, assignee, if assignee else None, priority, status)

def create_task():
    """Allows the user to create a new profile"""

    title = easygui.buttonbox ("Create task.")
    desc = easygui.choicebox ("Create task information.")
    assignee = easygui.choicebox ("Yes \n No")
    priority = easygui.ccbox ("Create a new description")
    Status = easygui.enterbox ("Create new box")

def remove_task()
    "Allows the user to remove a task from the dictionary"

    title = easygui.enterbox("Remove the new task (str)")
    desc = easygui.codebox("Remove the description")
    str in desc
    assignee = easygui.diropenbox

def Search_Member():
    """Allows the user to edit aspects of the task from their dictionary"""

    member_id = easygui.enterbox("Enter member ID:")
    result = display_member_info(member_id)
    easygui.msgbox(result)


def Update_tasks():
    """Allows the user to edit aspects of the task from their dictionary"""

    task_id = easygui.enterbox("Enter task title")