def modify_string(string, index, char):
    return string[:index] + char + string[index+1:]

print(modify_string("hello", 1, "a"))
