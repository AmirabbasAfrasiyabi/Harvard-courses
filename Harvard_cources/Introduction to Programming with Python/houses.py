name = input("what is your name?")

match name:
    case "Harry"| "Amirabbas" | "atiye" :
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who")
