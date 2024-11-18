def tuple_hash():
    n = int(input("Enter number of elements in the tuple: "))
    elements = tuple(map(int, input("Enter the elements separated by space: ").split()))
    print(hash(elements))

# Example
tuple_hash()
# Input: 2
#        1 2
# Output: 3713081631934410656