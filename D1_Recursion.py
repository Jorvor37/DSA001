    """
    Recursion is the function that call itself to breakdown the problem for solving
    """
    #Structure of recursion
    def recursion_function(parameters):
        if base_case:
            return result
        recursive_case = recursion_function(modidied_parameters)
        return combine(recursive_case)
    
    #Example use case
    #Factorial
    # 4! = 4*3*2*1 -> n! = n*(n-1)*(n-2)*...*2*1
    def factorial(n):
        if n==0:                        #base case
            return 1
        else:
            return n* factorial(n-1)    #recursive case
        
    #Fibonacci
    def fib(n):
        if n<= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)

    #Greatest Common Divisor
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
        
    #Tower of Hanoi
    def tower_of_hanoi(n, source, helper, target):
        if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, helper)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, helper, source, target)