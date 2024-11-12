# Initialize an empty list
lst = []

# Read the number of commands
n = int(input())

# Loop through each command
for _ in range(n):
    # Read the command and split it into parts
    command = input().split()
    cmd = command[0]
    
    # Execute the appropriate command based on input
    if cmd == "insert":
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)
    elif cmd == "print":
        print(lst)
    elif cmd == "remove":
        e = int(command[1])
        lst.remove(e)
    elif cmd == "append":
        e = int(command[1])
        lst.append(e)
    elif cmd == "sort":
        lst.sort()
    elif cmd == "pop":
        lst.pop()
    elif cmd == "reverse":
        lst.reverse()
