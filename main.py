def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        string = "asdasd"
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        if i % 3 != 0 and i % 5 != 0:
            print(i)





n = int(input("Podaj liczbę: "))
fizzBuzz(n)






