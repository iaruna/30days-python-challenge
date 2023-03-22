import logging


def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(
            f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated


@log_function_call
def my_function(a, b):
    return a + b


"""In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before
and after the original function is called."""
