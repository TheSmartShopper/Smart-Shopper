def Customer_required():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            print("custom_decorator")
            return func(request, *args, **kwargs)

        return wrapper

    return decorator

def StoreAdmin_required():
    pass
