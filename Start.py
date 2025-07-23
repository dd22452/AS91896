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

def create_task():
    """Allows the user to create a new profile"""

    title = easygui.buttonbox ("Create task.")
    desc = easygui.choicebox ("Create task information.")
    assignee = easygui.choicebox ("Yes \n No")
    priority = easygui.ccbox ("Create a new description")
    Status = easygui.enterbox ("Create new box")

def remove_task():
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

def print():
    """
    Prints all tasks.
    """

    output = ""

    for task_id, task_info in Tasks.items():
        output += f"\n{task_id}\n"

        for key in task_info:
            output += f"{key}: {task_info[key]}\n"


    easygui.msgbox(output)


def show_menu():
    """
    Shows the user the main menu and returns the users choice.
    """

    options = {
        "Create Task": create_task,
        "Print all tasks": print,
        "Exit": exit
    }

    get_input = "Y"

    while get_input == "Y":
        msg = "What would you like to do?"
        title = "sda"
        choices = []

        for items in options:
            choices.append(items)

        selection = easygui.buttonbox(msg, title, choices)

        get_input = options[selection]()

show_menu()