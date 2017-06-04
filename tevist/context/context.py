import sys



class persistent_locals(object):
    """
    Class decorator to store test context when the test is over
    """

    def __init__(self, func):
        self.test_context = {}
        self.func = func

    def __call__(self, *args, **kwargs):

        def context_store_tracer(frame, event, arg):
            if event=='return':
                self.test_context = frame.f_locals.copy()

        # tracer is activated on next call, return or exception. It is thread specific.
        # Multi threading shouldn't create conflicts
        sys.setprofile(context_store_tracer)
        try:
            res = self.func(*args, **kwargs)
        finally:
            # restoring tracer
            sys.setprofile(None)
        return res

    @property
    def locals(self):
        return self.test_context
