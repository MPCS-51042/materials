def mock(call, to_return):
    def decorator(func):
        def wrapper(testobject):
            module = eval('.'.join(call.split('.')[:-1]))
            module_function_name = call.split('.')[-1]
            module_function_body = getattr(module, module_function_name)
            setattr(module, module_function_name, lambda: to_return)

            func(testobject)

            setattr(module, module_function_name, module_function_body)

        return wrapper

    return decorator