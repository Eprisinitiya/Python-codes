def check_number(n):
    if n % 2 != 0: 
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:  
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:  
        print("Weird")
    elif n % 2 == 0 and n > 20: 
        print("Not Weird")

check_number(3)   # -> "Weird"
check_number(4)   # -> "Not Weird"
check_number(18)  # -> "Weird"
check_number(22)  # -> "Not Weird"