def decorator(function_to_decorate):
    def wrapper(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return wrapper

@decorator
def function(t):
    print("args :", t)

try:
    decorator(function("t"))
except:
    pass