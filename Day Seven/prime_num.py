def prime_number(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print("This is not a prime number")
                break
        else:
            print("This is a prime number")
    else:
        print("This is not a prime number")

prime_number(2)
