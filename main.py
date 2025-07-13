# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_char_code(line):
    print([f"{c} -> {ord(c)}" for c in line])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_char_code("# 1 Stock Market")
    print_char_code("# 2 Stock Market")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
