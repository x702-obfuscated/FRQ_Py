from pathlib import Path
import sys,os

import importlib.util
try:
    path = Path(__file__).parts
    path = path[:path.index("frq")+1]

    importpath = Path(path[0]).joinpath(*path[1:]) / "testing" / "testing.py"

    module_name = "testing"

    spec = importlib.util.spec_from_file_location(module_name, importpath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # Load the module

    testing = module
except Exception as e:
    print(e)
    sys.exit()

try:
    if __name__ == "__main__":
        import temp as m
    else:
        import main as m
except ModuleNotFoundError as e:
    print("Tests cannot be executed because 'main.py' does not exist.")
    sys.exit()

testing.clear()

alltests = []
t = testing.TestPy(Path(__file__).parent / "main.py", m)



def runtests():
    for test in alltests:
        test()

    t.assess()
    t.showreport()
#Tests###########################################################################################################
'''Write test questions below'''















#Tests###########################################################################################################



