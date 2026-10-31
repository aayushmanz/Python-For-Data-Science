if __name__ == "__main__":

    """
    This is my code and i m testing it.

    """

    a = []
    try:
        n = int(input("Enter the Number : "))
        assert n > 0

        print("")
        print("insert the value : ")
        print("-" * 20)
        stop = ""
        while True:
            stop = input("Wanna continue ? (y/n) : ")
            if stop == "n":
                break
            else:
                for i in range(n):
                    num = input("Enter the value : ")
                    a.append(num)

                print("")
                print("This is our inserted value : ")
                print("-" * 20)
                for i in range(n):
                    print(f"index {i} : ", a[i])

                print("")
                print("Remove the element : ")
                print("-" * 20)
                remove = int(input("Enter the remove element : "))
                for i in range(n):
                    if remove == a[i]:
                        a.remove(remove)
                print(f"{remove} is successfully removed !")
                print(a)

                print("")
                print("insert the element : ")
                print("-" * 20)
                pos = int(input("Enter the position : "))
                val = input("Enter the value : ")
                a.insert(pos, val)
                print(a)

    except AssertionError:
        print("Please Enter the Greater value than Zero !")
    finally:
        print("Thanks For using My code ! ")
