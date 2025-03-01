keep_going = True
while keep_going:
    n = input("Enter a number: ")
    if n.isnumeric():
        n = int(n)
        for i in range(1, n+1, 1):
            if n%i == 0:
                print(i)
        answer = input("Do you want to keep going?\n").lower() 
        if answer == "yes":
            continue
        else:
            print("Goodbye.")
            break
    else:
        print("Input has to be an integer.")
        continue