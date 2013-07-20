http://stackoverflow.com/questions/16043797/python-passing-variables-between-functions

list_one=["a", "b", "c"]
list_two=list(list_one)
list_three=list(list_one)
print list_one
print list_two
print list_three


def a_function():
    list_two=[list_three[2], list_three[1], list_three[0]]
    print list_two
    list_four=list(list_two)
    print list_three
    print list_four


def function_two():
    a_function()
    print list_two
    print list_three
    print list_four
    
function_two()