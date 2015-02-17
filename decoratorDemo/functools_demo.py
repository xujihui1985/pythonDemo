import functools

def noop(f):
    # functools.wraps itself is a decorator, it set the meta data of the original function
    # to the wrapper function so, the wrapper function keep the meta data of the original function
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper


@noop
def hello():
    "print a message"
    print('hello, world')
