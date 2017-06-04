help("modules")
from tevist.context.context import persistent_locals

def demo_func(a,b):
    result = a+b
    return result

def test_simple_context():

    wrapped_function = persistent_locals(demo_func)
    func_result = wrapped_function(2,2)
    assert(func_result == 4)
    assert(wrapped_function.locals["result"]==4)
