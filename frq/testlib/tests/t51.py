import sys,re
from pathlib import Path
import importlib.util as imp

import frq.testlib.testlib as tlib

mainpath = Path(sys.argv[1])

spec = imp.spec_from_file_location("main",mainpath)
main = imp.module_from_spec(spec)
spec.loader.exec_module(main)


t = tlib.TestPy(mainpath,main,__import__(__name__))

'''-----Write tests below----------------------------------------------------------------'''






t.runtests()