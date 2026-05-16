movies = []

print("add a movie by saying add (movie name)")
print("print the list by saying print list")
print("type 'exit' to quit")
print("type remove (movie name )")
while True:
    x = input("\nWhat would you like to do? ")

    if x == "print list":
        print("Your list: " + ", ".join(movies))
    
    elif x == "exit":
        break

    elif x == "add dr strange":
        print("movie added")
        movies.append("dr strange")

    elif x == "add the wild robot":
        print("movie added")
        movies.append("the wild robot")

    elif x == "add paddington in peru":
        print("movie added")
        movies.append("paddington in peru")

    elif x == "add dog man":
        print("movie added")
        movies.append("dog man")

    elif x == "add monsters university":
        print("movie added")
        movies.append("monsters university")

    elif x == "add toy story":
        print("movie added")
        movies.append("toy story")

    elif x == "add epic":
        print("musical added")
        movies.append("epic the musical")

    elif x == "add diary of a wimpy kid":
        print("movie added")
        movies.append("diary of a wimpy kid")

    elif x == "add school of rock":
        print("movie added")
        movies.append("school of rock")

    elif x == "add beetlejuice":
        print("movie added")
        movies.append("beetlejuice")

    elif x == "remove dr strange":
        print("movie removed")
        movies.remove("dr strange")

    elif x == "remove the wild robot":
        print("movie removed")
        movies.remove("the wild robot")

    elif x == "remove paddington in peru":
        print("movie removed")
        movies.remove("paddington in peru")

    elif x == "remove dog man":
        print("movie removed")
        movies.remove("dog man")

    elif x == "remove monsters university":
        print("movie removed")
        movies.remove("monsters university")

    elif x == "remove toy story":
        print("movie removed")
        movies.remove("toy story")

    elif x == "remove epic":
        print("musical removed")
        movies.remove("epic the musical")

    elif x == "remove diary of a wimpy kid":
        print("movie removed")
        movies.remove("diary of a wimpy kid")

    elif x == "remove school of rock":
        print("movie removed")
        movies.remove("school of rock")

    elif x == "remove beetlejuice":
        print("movie removed")
        movies.remove("beetlejuice")
    else:
        print("movie not found")