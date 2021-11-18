def fib(term):
    if term<=1:
        return(term)
    else:
        return(fib(term-1)+fib(term-2))
number_of_term=int(input("Enter the number:"))
for i in range(number_of_term):
    print(fib(i))
