import random
ITEMS=["a","b","c"]

for i in range(15):
    se=[]
    print("FOLLOW ALONG if you can")
    numberstoadd = random.randint(1, 15)
    for i in range(numberstoadd):
        new = random.choice(ITEMS)
        se.append(new)
    
    print(f"{" ".join(se)}")
    print("type it back")
    x = input()

    if x==(f"{" ".join(se)}"):
        print ("cool do it again")
    else:
        print("you suck")
        break


