'''
keys = ['name','age','city']
values = ['John', 25, 'New York']

my_dict = dict(zip(keys,values))

print(my_dict)
'''

def dict_values_to_list(input_dict):
    values_list = list(input_dict.values())
    return values_list

example_dict = {'a':1,'b':2,'c':3,'d':4}
result_list = dict_values_to_list(example_dict)

print('Original Dictionary:', example_dict)
print('Values as List:', result_list)
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
'''