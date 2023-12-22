import time


# Decorador para medir el tiempo de ejecución de una función
def timing_decorator(enabled=False):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if enabled:
                start_time = time.time()
                result = func(self, *args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"La función '{func.__name__}' de la clase '{self.__class__.__name__}' se demoro {elapsed_time:.4f} segundos.")
                return result
            else:
                # If the decorator is disabled, just call the original function without any timing measurement
                return func(self, *args, **kwargs)
        return wrapper
    return decorator
