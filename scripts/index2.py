'''
keys = ['name','age','city']
values = ['John', 25, 'New York']

my_dict = dict(zip(keys,values))

print(my_dict)
'''

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return 1
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

n = 10
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")