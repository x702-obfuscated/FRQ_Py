'''TODO:
functions to test:
module out
function out
equality


1. Test File that contains defined functions
2. Way to Parameterize Tests
3. Report Generation

'''

import os,re,io,subprocess,sys
from getpass import getuser
from datetime import datetime

from functools import wraps


class TestPy:

    def __init__(self,path,module,testmodule):
        self.path = path
        self.parent = self.path.parent
        self.reportpath = self.parent/"report.txt"
        self.module = module
        self.testmodule = testmodule
        self.content = ""
        self.num = 0
        self.report = []
        
        self.numpassed = 0
        self.numfailed = 0

        self.alltests = []

        self.__readcontent()

    def __readcontent(self):
        with open(self.path,"r") as file:
            self.content = file.read()
    
    def assess(self):  
        try:
            passpercent = round(self.numpassed / self.num * 100)
            failpercent = round(self.numfailed / self.num * 100)
        except ZeroDivisionError as e:
            passpercent = 0
            failpercent = 0

        self.report.append("\n")
        if self.numpassed:
            self.report.insert(0,f"Tests Passed \u2705: {self.numpassed} : {passpercent}%\n")
        if self.numfailed:
            self.report.insert(0,f"Tests Failed \u274C: {self.numfailed} : {failpercent}%\n")

        self.report.insert(0,"\n")

        self.report.insert(0,f"[ TIME: {str(datetime.now())} ]\n")

        try:
            self.report.insert(0,f"[ USER: {getuser().upper()} ]\n")
        except KeyError as e:
            self.report.insert(0,str(self.path))

        if not(self.num > 0):
            self.report.insert(0,f"\u2757 No tests found for this module. \u2757\n")
        elif self.numpassed == self.num:
            self.report.insert(0,f"\u2705 ALL TESTS PASSED \u2705\n")
        else:
            self.report.insert(0,f"\u274C THERE ARE FAILING TESTS \u274C\n")
 
    def test(self, *params):
        def decorator(function):
            def wrapper():
                if not params:
                    self.num +=1
                    try:
                        function()
                        self.numpassed += 1
                        self.report.append(f"\u2705 Test {self.num} Passed\n")
                    except AssertionError as e:
                        self.numfailed +=1
                        self.report.append(f"\u274C Test {self.num} Failed : {str(e)}\n")
                
                for param in params:
                    self.num+=1
                    try:
                        function(*param)
                        self.numpassed += 1
                        self.report.append(f"\u2705 Test {self.num} Passed\n")
                    except AssertionError as e:
                        self.numfailed +=1
                        self.report.append(f"\u274C Test {self.num} Failed : {str(e)}\n")
            return wrapper
        return decorator

    def encode(self):
        for i,_ in enumerate(self.report):
            self.report[i] = self.report[i].encode("utf-8")

    def writereport(self):
        self.encode()
        if os.path.exists(self.reportpath):
            os.chmod(self.reportpath,0o644)

        with open(self.reportpath, "wb") as file:
            file.writelines(self.report)

        os.chmod(self.reportpath,0o444)

    def showreport(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        # with open(self.reportpath, "rb") as file:
        #     print(file.read().decode("utf-8"))
        self.encode()
        for r in self.report:
            print(r.decode("utf-8").replace("\n",""))

    def assertin(self,value,txt=None,feedback=None):

        if txt is None:
            txt = self.content

        if feedback is None:
            feedback = f"{value} was expected in contents, but was not found."

        assert value in txt, feedback

    def assertmatch(self,pattern,txt=None, feedback=None):


        if txt is None:
            txt = self.content

        if feedback is None:
            feedback = "Expected pattern not found in content."

        assert re.search(pattern,txt), feedback

    def assertequal(self, attribute, expected_out, *args):
        exptype = type(expected_out)
        try:
            strattr = attribute
            attribute = getattr(self.module,attribute)
        except AttributeError as e:
            raise AssertionError(f"'{attribute}' is not defined. Did you define '{attribute}' in your source code?")
        
        
        if(callable(attribute)):
            result = attribute(*args)
            restype = type(result)
            strargs = (str(arg) for arg in args)

            assert exptype == restype, f"'{attribute.__name__}({",".join(strargs)})' was called. Expected data of type {exptype}, but got {restype}. Check your data types."

            assert result == expected_out,f"'{attribute.__name__}({",".join(strargs)})' was called. The test expected a value of '{expected_out}', but got '{result}'instead."

        else:
            restype = type(attribute)
            assert exptype == restype, f"While checking value of '{strattr}' expected data of type '{exptype}', but got '{restype}'. Check your data types."
            assert attribute == expected_out,f"While checking value of '{strattr}' expected value of '{expected_out}', but got '{attribute}'."

    def outisequal(self, out, expout):
        assert out == expout,f"Expected output to be '{expout}', but got '{out}' instead."

    def getfunctnout(self,functn, *args):

        try:
            strfun = functn
            functn= getattr(self.module,functn)
        except AttributeError as e:
            raise AssertionError(f"'{strfun}' is not defined. Did you define '{strfun}' in your source code?")

        captured_output = io.StringIO() 
        sys.stdout = captured_output 

        functn(*args) 
    
        sys.stdout = sys.__stdout__ 

        result = captured_output.getvalue()
        captured_output.close()

        return result

    def runtests(self):
        alltestnames = [test for test in vars(self.testmodule)  if test.startswith("test")]
        for functn in alltestnames:
            self.alltests.append(getattr(self.testmodule,functn))
        

        for test in self.alltests:
            test()

        
        self.assess()
        # self.writereport()
        self.showreport()




def clear():
    if os.name == "posix":
        os.system("clear")

    elif os.name == "nt":
        os.system("cls")

def openfile(filepath):
    try:
        if sys.platform == "win32":
            os.startfile(filepath)  # Windows
        elif sys.platform == "darwin":
            subprocess.run(["open", filepath])  # macOS
        else:
            subprocess.run(["xdg-open", filepath])  # Linux
    except Exception as e:
        print(f"Error opening file: {e}")

