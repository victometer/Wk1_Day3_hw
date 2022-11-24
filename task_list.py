tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1.Print a list of uncompleted tasks
def make_list ():
    for task in tasks:
        uncompleted_tasks = task['completed']
        if uncompleted_tasks == False:
    return(task)   
print(make_list(task['description']))

# 2. Print a list of completed tasks
# for task in tasks:
#     completed_tasks = task['completed']
#     if completed_tasks == True:
#         print(task['description'])

# 3. Print a list of all task descriptions
# for task in tasks:
#     print(task["description"])

# 4.Print a list of tasks where time_taken is at least a given time
# time_given = 15
# for task in tasks:
#     as_it_happened = task['time_taken']
#     if as_it_happened >= time_given:
#         print(task['description'])

# 5. Print any task with a given description
# description_given = 'Feed Cat'
# for task in tasks:
#     if task['description'] == description_given:
#         print(task)


# 6. Given a description update that task to mark it as complete.
# description_given = 'Feed Cat'
# for task in tasks:
#     if task['description'] == description_given:
#         task['completed'] = True
#         print(task)

# 7. Add a task to the list
# tasks.append ({'description' : 'Train', 'completed' : True, 'time_taken' : 90})
# print(tasks)

# menu_options = [
#     {
#     "1: Display All Tasks",
#     "2: Display Uncompleted Tasks",
#     "3: Display Completed Tasks",
#     "4: Mark Task as Complete",
#     "5: Get Tasks Which Take Longer Than a Given Time",
#     "6: Find Task by Description",
#     "7: Add a new Task to list",
#     "M or m: Display this menu",
#     "Q or q: Quit"
#     }
# ] #make a list-dictionary
# while menu_options True:
#     print("1: Display All Tasks")
#     print("2: Display Uncompleted Tasks")
#     print("3: Display Completed Tasks")
#     print("4: Mark Task as Complete")
#     print("5: Get Tasks Which Take Longer Than a Given Time")
#     print("6: Find Task by Description")
#     print("7: Add a new Task to list")
#     print("M or m: Display this menu")
#     print("Q or q: Quit")

#     print()
#     user_input = input("Choose an option ") # ah! it doesn't recognise that 1-7, m and q are options
#     #and that they can return an menu_option, so I might need 2 different things:
#     # one that defines what can the user input (i.e 1,2 3,4) and what does users' input relate to in code
#     print("You chose: " + user_input) #print menu_options[], but the index [] will be decided by the user
