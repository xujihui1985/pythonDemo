class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args, **kwargs)

        return warp

@Trace(True)
def rotate_list(l):
    return l[1:] + [l[0]]
