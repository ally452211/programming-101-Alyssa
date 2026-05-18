
while True:
    
    phone_numbers={
        "alyssa":6477080286,
        "daniel": 6471234567,
        "yoyo": 6470987654,
        "joseph": 4169997601,
        "billan": 6472345678
    }

    name= input ("who are you looking for? or you can leave (type exit)").lower()

    if name=="exit":
        print("baiiii")
        break

    if name in phone_numbers:
        print(f"{name.capitalize}'s phone number is {phone_numbers[name]}")

    else:
        print("contact not found (sorry!)")
        


