# Program that produces a fibonacci series
def fib_sequence(n):
   if n <= 1:
       return n
   else:
       return(fib_sequence(n-1) + fib_sequence(n-2))