from colorama import Fore
from json import dumps as json_dumps

todos = []



def print_message(message:object, color=Fore.YELLOW) -> None:
    message = str(message)
    print(color + message + Fore.RESET)


def print_green(message:object) -> None:
    print_message(message = message, color = Fore.GREEN)


def print_red(message:object) -> None:
    print_message(message = message, color = Fore.RED)


def print_blue(message:object) -> None:
    print_message(message = message, color = Fore.BLUE)


def main_menu() -> str:
    print_blue('Create Todo -> 1')
    print_blue('Delete Todo -> 2')
    print_blue('Update Todo -> 3')
    print_blue('View Todo   -> 4')
    print_blue('All Todos   -> 5')
    print_blue('Quit        -> 6')
    return input(Fore.YELLOW + '?:')


def check_input_to_valid_str(data:str) -> bool:
    return data.__len__() > 0


def check_input_to_valid_int(data:str) -> bool:
    return data.__len__() > 0 and data.isdigit


def create_todo():
    todo = {}
    
    data = input('title : ')
    if not check_input_to_valid_str(data):
        print_red(f'input not valid for title = > {data}')
        return
    todo['title'] = data

    data = input('description : ')
    if not check_input_to_valid_str(data):
        print_red(f'input not valid for description = > {data}')
        return
    todo['description'] = data

    data = input('dead line(in minutes (12,45,55)) : ')
    if not check_input_to_valid_int(data):
        print_red(f'input not valid for dead line = > {data}')
        return
    todo['dead_line'] = data

    todo['completed'] = False
    todos.append(todo)


def delete_todo():
    max_index = len(todos)
    if max_index == 0:
        print_message('You dont have any todos')
        return
    for index, todo in enumerate(todos, start = 1):
        print(f"{todo.get('title')} -> {index}")
    else:
        choosen_index = int(input("enter index : "))
        if choosen_index < 1 or choosen_index > max_index:
            print_red('Wrong Choice')
            delete_todo()
        else:
            del todos[choosen_index - 1]
            print_green('successfully deleted')


def update_todo():
    pass


def view_todo():
    max_index = len(todos)
    for index, todo in enumerate(todos, start = 1):
        print(f"{todo.get('title')} -> {index}")
    else:
        choosen_index = int(input("enter index : "))
        if choosen_index < 1 or choosen_index > max_index:
            print_red('Wrong Choice')
            delete_todo()
        else:
            print(json_dumps(todos[choosen_index - 1]))


def all_todos():
    print_green(json_dumps(todos, indent=3))
    


def main():
    _continue = True
    while _continue:        
        choice = main_menu()
        if  choice == '1':
             create_todo()
        elif choice == '2':
            delete_todo()
        elif choice == '3':
            update_todo()
        elif choice == '4':
            view_todo()
        elif choice == '5':
            all_todos()
        elif choice == '6':
            print_message("Bye Man ..... ")
            return
        else:
            print_red('Wrong choice')
    _continue = input('quit(yes/no)').startswith('y')

    
def run():
    main()
    print('Gonna talk again')
    


if __name__ == '__main__':
    run()