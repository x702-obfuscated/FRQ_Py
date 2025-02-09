import sys
from pathlib import Path
import importlib.util as imp

import frq.testlib.testlib as tlib

mainpath = Path(sys.argv[1])

spec = imp.spec_from_file_location("main",mainpath)
main = imp.module_from_spec(spec)
spec.loader.exec_module(main)


t = tlib.TestPy(mainpath,main,__import__(__name__))




@t.test(
    (5, 5),
    (6, "6"),
    (8, 6)
)
def test1(a,b):
    assert a == b, f"{a} does not equal {b}"
    
@t.test()
def test2():
    t.assertin("asdfasdfasdf")

@t.test()
def test3():
    assert "a" == "A", "a does not equal A"







# def test(*test_cases):
#     def decorator(func):
#         def wrapper():
#             for args in test_cases:
#                 try:
#                     func(*args)  # Pass test case arguments to the function
#                     t.results.append((func.__name__, args, "✅ Passed"))
#                 except AssertionError as e:
#                     t.results.append((func.__name__, args, f"❌ Failed: {e}"))
#                 except Exception as e:
#                     t.results.append((func.__name__, args, f"⚠️ Error: {e}"))
#         return wrapper
#     return decorator







t.runtests()