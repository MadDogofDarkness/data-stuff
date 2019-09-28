syntax = ["the syntax of the language is each operation is on a single line",
        "each operation can have one or more operators",
        "no one function name or operator can be longer than 4 characters",
        "new functions can be defined"]

functions = ["low", "big", "add", "sub", "mult", "div", "deff"]

def deff(funcname, operators):
    if len(funcname) <= 4:
        functions.append(funcname)
        return 0
    else:
        return 1

def div(operator1, operator2):
    return operator1 / operator2

def mult(operator1, operator2):
    return operator1 * operator2

def sub(operator1, operator2):
    return operator1 - operator2

def add(operator1, operator2):
    return operator1 + operator2

def big(operator1, operator2):
    #returns the bigger of the two operators
    #if they are the same, returns operator1
    if operator2 > operator1:
        return operator2
    else:
        return operator1

def low(operator1, operator2):
    #returns the lower of two operators
    #if they are the same, returns operator1
    if operator2 >= operator1:
        return operator1
    else:
        return operator2

def convert_to_record(data):
    tostore = None
    '''this takes in a data which is a list, or tuple, and converts it to the correct format for storage in the database'''
    '''if type is a list, array or tuple, will treat as a block of data'''
    '''if type is an object, will assume the data is presented in the following format'''
    '''[classname: name_of_object, attr1: value, ..., attr_n: value_n]'''
    tostore = "["
    for entry in data:
        print(entry) # debug
        tostore += str(data)
        tostore += ','
    tostore += ']'
    print(len(tostore)) # debug
    print(tostore) # debug
    return tostore

def delimit(data, delimiter):
    formatted = []
    store = ""
    for c in data:
        if c == delimiter:
            formatted.append(store)
            store = ""
        else:
            store += c
    formatted.append(store)
    #print(formatted)#debug
    return formatted


if __name__ == "__main__":
    print(syntax)
    ebin = input("enter here: ")
    #convert_to_record2(ebin)
    delimit(ebin, '%')