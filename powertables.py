while True:
    userNum = int(input("Enter an integer: "))

    print("Number")
    print("======")
    for n in range(0, userNum):
        n += 1
        print(n)

    print("Squared")
    print("=======")
    for n in range(0, userNum):
        n += 1
        print(n * n)

    print("Cubed")
    print("=====")
    for n in range(0, userNum):
        n += 1
        print(n * n * n)

    keepGoing = input("Would you like to continue? (y/n)")
    if keepGoing == "y":
        continue
    elif keepGoing == "n":
        print("Goodbye!")
        break
    else:
        print("Enter either y/n")
