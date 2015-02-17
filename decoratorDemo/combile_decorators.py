class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args, **kwargs)

        return warp

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

@Trace(True)
@escape_unicode     #decorate sequence from escape_unicode then Trace
def use_unicode():
    return 'hello'
