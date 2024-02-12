# from functions import get_todos, write_todos
import functions as func

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = func.get_todos("todos.txt")
        todos.append(todo + '\n')
        func.write_todos(todos)

    elif user_action.startswith("show"):

        todos = func.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = func.get_todos("todos.txt")
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'
            func.write_todos(filepath="todos.txt", todos_arg=todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        number = int(input("Number of the todo to complete: "))

        todos = func.get_todos()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        func.write_todos(todos)

        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")
