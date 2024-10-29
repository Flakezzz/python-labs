def findLetter(x):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = alphabet.index(x[0])
    for k in x:
        if alphabet[i] == k:
            i += 1
        else:
            return alphabet[i]
    return "All letters are in order"

userList = input("Enter the order: (enter 'stop' to cancel)")
for i in userList:
    if i.isdigit():
        print(f"Value: {i} is incorrect!")
        
print(f"{userList} -> {findLetter(userList)}")
