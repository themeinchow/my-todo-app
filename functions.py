FILEPATH = "../web_app1/todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list
    of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write to-do items list in the text file"""
    with open(filepath, 'w') as file_local:
        todos_local = file_local.writelines(todos_arg)


# __name__ == __main__ when running that specific code, when ran under a from a
#different code it appears as the name of this file.


if __name__ == '__main__':
    print('Hello')
    print(get_todos())
