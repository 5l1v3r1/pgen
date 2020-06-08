import string
import random

print("__________    fb.com/virusarham     ________               ")
print("\______   \_____    ______ ______  /  _____/  ____   ____  ")
print(" |     ___/\__  \  /  ___//  ___/ /   \  ____/ __ \ /    \ ")
print(" |    |     / __ \_\___ \ \___ \  \    \_\  \  ___/|   |  \ ")
print(" |____|    (____  /____  >____  >  \______  /\___  >___|  /")
print("                \/     \/     \/          \/     \/     \/ BY Arham Khan\n")

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
    plen = int(input("Enter Password length You want :: "))
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    #print(s)
 
    print("\n------------------------------------\n")
    print("".join(s[0:plen]))
    print("\n------------------------------------\n")

print("\nGood Luck to Hacker Who want to Crack Your password :V \n")