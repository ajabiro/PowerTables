while True:
    userNum = int(input("Enter an integer: "))

    print("Number\t Squared\t Cubed")
    print("======\t =======\t =====")

    for n in range(1, userNum + 1):
        print(f"{n}\t\t {n ** 2}\t\t\t {n ** 3}")

    keepGoing = input("Would you like to continue? (y/n)")
    if keepGoing == "y":
        continue
    elif keepGoing == "n":
        print("Goodbye!")
        break
    else:
        print("Enter either y/n")


