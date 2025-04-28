identity='d89e987626657e52cc270b3cfa9ebe33a1f4faca9674b4143d0c6616102c103c175c5fb5f4f236e6a15dc57f30fa4503eae9666c3e25045809ff1bc1beef43d1'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

assignment = "14-Variables"
path = Path(__file__).parent
thispath = Path(__file__)
filepath = "main.py"
filecontent = ""
numpassed = 0
numfailed = 0
num = 0
report = []
alltests = []

def maketests(m=None):
    global filecontent

    @test(
        ("nothing", None),
        ("switch", True),
        ("num", 42),
        ("percent",0.75),
        ("name","Alice"),
        ("fruits",["apple","banana","cherry"]),
        ("coordinates",(10,20)),
        ("person", {"name":"Bob","age":30})
    )
    def t1(var,val):
        assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
        assert getattr(m,var) == val, f"Expected '{var}' to point to {val} , but it does not."

    @test(
        ("one","abc"),
        ("two","abc"),
        ("three","abc")
    )
    def t2(var,val):
        assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
        assert getattr(m,var) == val, f"Expected '{var}' to point to \"{val}\" , but it does not."
        
    @test()
    def t3():
        assert re.search(r"one\s*=\s*two\s*=\s*three\s*=\s*[\"']abc[\"']",filecontent), f"Expected variables 'one', 'two', and 'three' to be assigned on the same line to the same value without using semicolons(;) or commas(,), but was not found."


    @test(
        ("source","text"),
        ("byte","bytes"),
        ("machine","binary")
    )
    def t4(var,val):
        assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
        assert getattr(m,var) == val, f"Expected '{var}' to point to \"{val}\" , but it does not."

    @test()
    def t5():
        assert re.search(r"source\s*=\s*[\"']text[\"']\s*;\s*byte\s*=\s*[\"']bytes[\"']\s*;\s*machine\s*=\s*[\"']binary[\"']",filecontent), f"Expected variables 'source', 'byte', and 'machine' to be assigned on the same line to the values \"text\", \"bytes\", and \"binary\" without using commas(,), but was not found."

    @test(
        ("pi",3.14),
        ("euler",2.718),
        ("phi",1.618),
        ("mol",6.022E23)
    )
    def t6(var,val):
        assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
        assert getattr(m,var) == val, f"Expected '{var}' to point to \"{val}\" , but it does not."


    @test()
    def t7():
        assert re.search(r"pi\s*,\s*euler\s*,\s*phi\s*,\s*mol\s*=\s*3.14\s*,\s*2.718\s*,\s*1.618\s*,\s*6.022[eE]23\s*",filecontent), f"Expected variables 'pi', 'euler', 'phi', 'mol' to  3.14 , 2.718 , 1.618 , and 6.022E23 repectively on the same line without using semicolons(;)"

    @test()
    def t8():
        # Define a variable named 'changeme' to the value True. Then reassign 'changme' to the value False.
        assert hasattr(m,"changeme"), f"Expected a defined variable named 'changeme', but was not found."
        assert getattr(m,"changeme") == False, f"Expected 'changeme' to point to False, but it does not."
        assert re.search(r"changeme\s*=\s*True",filecontent), f"Expected 'changeme' to previously be assigned to the value True, but this assignment was not found."

    @test(
        ("message","Hello World")
    )
    def t9(var,val):
        assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
        assert getattr(m,var) == val, f"Expected '{var}' to point to \"{val}\" , but it does not."
        assert re.search(r"print\s*\(\s*message\s*\)",filecontent), f"Expected a print() call that prints out the value of '{var}', but was not found."

    # @test(
    #     ("this",["same",2,3]),
    #     ("that",["same",2,3]),
    #     ("other",["same",2,3])
    # )
    # def t10(var,val):
    #     assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
    #     assert getattr(m,var) == val, f"Expected '{var}' to point to \"{val}\" , but it does not."
        
    # @test(
    #     ("this","that","other")
    # )
    # def t11(*val):
    #     for i in range(len(val)):
    #         assert hasattr(m,val[i]), f"Expected '{val[i]}' to be defined, but was not found."
    #     assert getattr(m,val[0]) is getattr(m,val[1]) is getattr(m,val[2]), f"Expected '{val[0]}', '{val[1]}', and '{val[2]}' to be aliases, but they are not."

    #     assert re.search(r"other\[0\]\s*=\s*[\"']same[\"']",filecontent), "Expected the statement other[0] = \"same\" in the source code, but was not found"

    #     for i in range(len(val)):
    #         assert re.search(rf"print\s*\(\s*{val[i]}\s*\)",filecontent), f"Expected a print() call with {val[i]} as an argument, but was not found."


    @test(("this","that","other"))
    def t10(*vars):
        for var in vars:
            assert hasattr(m,var), f"Expected '{var}' to be defined, but it was not found. Did you define '{var}'?"
        
        assert getattr(m,vars[0]) is getattr(m,vars[1]) is getattr(m,vars[2]), f"Expected 'this', 'that', and 'other to be aliases. How are aliases defined?"
        assert getattr(m,vars[2]) == ["same",2,3], f"Expected 'other' to point to the value [\"same\",2,3] . Did you reassign the value of other[0] correctly?"

        for var in vars:
            assert re.search(rf"print\s*\(\s*{var}\s*\)",filecontent), f"Expected a print() call containing the argrument '{var}' but it was not found. Did you print out '{var}'?"


    alltests.append(t1)
    alltests.append(t2)
    alltests.append(t3)
    alltests.append(t4)
    alltests.append(t5)
    alltests.append(t6)
    alltests.append(t7)
    alltests.append(t8)
    alltests.append(t9)
    alltests.append(t10)
    # alltests.append(t11)
    # alltests.append(t12)

def checkintegrity():
    hasher = hashlib.sha512()
    with open(thispath, 'rb') as f:
        f.readline()
        chunk = f.read(8192)
        while chunk:
            hasher.update(chunk)
            chunk = f.read(8192)
    hasher.hexdigest()
    try:
        if(sys.argv[1] == "set"):
            with open(thispath,"r") as f:
                lines = f.readlines()
            
            lines[0] = f"identity='{hasher.hexdigest()}'\n"

            with open(thispath, "w") as f:
                f.writelines(lines)
            sys.exit()
    except IndexError as e:
        pass

    if hasher.hexdigest() != identity:
        print(b'\x54\x65\x73\x74\x73\x20\x66\x69\x6c\x65\x20\x68\x61\x73\x20\x62\x65\x65\x6e\x20\x61\x6c\x74\x65\x72\x65\x64\x20\x77\x69\x74\x68\x6f\x75\x74\x20\x70\x65\x72\x6d\x69\x73\x73\x69\x6f\x6e\x2e\x20\x59\x6f\x75\x20\x77\x69\x6c\x6c\x20\x6e\x65\x65\x64\x20\x74\x6f\x20\x67\x65\x74\x20\x61\x20\x63\x6c\x65\x61\x6e\x20\x63\x6f\x70\x79\x20\x74\x6f\x20\x63\x6f\x6e\x74\x69\x6e\x75\x65\x2e\x0a\x45\x78\x69\x74\x69\x6e\x67\x2e\x2e\x2e'.decode())
        sys.exit()

def checkforsyntaxerrors():
    change_inputfunction()
    if os.name == 'posix':
        command = ["python3",filepath]

    elif os.name == 'nt':
        command = ["python",filepath]

    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE,stdin = subprocess.DEVNULL, text = True)
    stdout,stderr = process.communicate()

    if(stderr):
        txt = f"\u2757Before the test could run your code resulted in an error:\u2757".upper()
        print("-"*len(txt),txt,"-"*len(txt),sep="\n",end="\n\n")
        print(stderr)
        print("-"*len(txt))
        print("Look for 'line' in the text above, and the 'Error' on the last line.\n")
        print("Read the traceback and figure out what is wrong.".upper())
        print("-"*len(txt))
        remove_inputchange()
        sys.exit()
    remove_inputchange()

def readcontent():
    global filecontent
    try:
        with open(filepath,"r") as file:
            filecontent = file.read()
    except FileNotFoundError as e:
        print(f"{filepath} not found.\nCreating {filepath}...")
        open(filepath, "w").close()
        filecontent = ""
    
def test(*params):
    def decorator(function):
        def wrapper():
            global num,numpassed,numfailed,report
            if not params:
                num+=1
                try:
                    function()
                    numpassed += 1
                    report.append(f"\u2705 Test {num} Passed\n")
                except AssertionError as e:
                    numfailed +=1
                    report.append(f"\u274C Test {num} Failed :\n {str(e)}\n")
            
            for param in params:
                num+=1
                try:
                    function(*param)
                    numpassed += 1
                    report.append(f"\u2705 Test {num} Passed\n")
                except AssertionError as e:
                    numfailed +=1
                    report.append(f"\u274C Test {num} Failed :\n {str(e)}\n")
        return wrapper
    return decorator

def runtests():
    checkintegrity()
    try:
        change_inputfunction()
        import main
    except (ModuleNotFoundError,FileNotFoundError):
        print("File not found. 'main.py' does not exist.")
        print("Creating 'main.py'...")
        open("main.py","w").close()
        print("'main.py' created. Please try again.")
    except Exception as e:
        try:
            checkforsyntaxerrors()
        except Exception as e:
            print(e)
    
    change_inputfunction()
    maketests(main)

    for test in alltests:
        test()

    remove_inputchange()
    assess()
    printreport()

def assess():
    if not identity or not checkintegrity:
        sys.exit()
    checkintegrity()
    try:
        passpercent = round(numpassed / num * 100)
        failpercent = round(numfailed / num * 100)
    except ZeroDivisionError as e:
        passpercent = 0
        failpercent = 0

    report.append("\n")
    if numpassed:
        report.insert(0,f"Tests Passed \u2705: {numpassed} : {passpercent}%\n")
    if numfailed:
        report.insert(0,f"Tests Failed \u274C: {numfailed} : {failpercent}%\n")

    report.insert(0,"\n")

    report.insert(0,f"[ TIME: {str(datetime.now())} ]\n")
    report.insert(0,f"[ ASSIGNMENT: {assignment} ]\n")
    try:
        report.insert(0,f"[ USER: {getuser().upper()} ]\n")
    except KeyError as e:
        report.insert(0,str(path))

    if not(num > 0):
        report.insert(0,f"\u2757 No tests found for this module. \u2757\n")
    elif numpassed == num:
        report.insert(0,f"\u2705 ALL TESTS PASSED \u2705\n")
    else:
        report.insert(0,f"\u274C THERE ARE FAILING TESTS \u274C\n")

def printreport():
    clear()
    for r in report:
        if "Failed" in r:
            print(r)
        else:
            print(r.replace("\n",""))

def change_inputfunction(inp=None):
  global filepath,filecontent
  readcontent()

  if("input(" in filecontent):
    try:
      with open(filepath, "r+") as file:
        lines = file.readlines()
        if(not lines[0] or "input = lambda _ = None :" in lines[0]):
          lines[0] = f"input = lambda _ = None : {inp} \n"
        else:
          lines.insert(0,f"input = lambda _ = None : {inp} \n")
        
        file.seek(0)
        file.truncate()
        file.writelines(lines)

      readcontent()

    except Exception as e:
      print(f"An error occured while making input changes: {e}")
      exit()

  else:
    return

def remove_inputchange():
  global filepath, filecontent
  try:
    with open(filepath, "r+") as file:
      lines = file.readlines()
      if(len(lines)>0 and "input = lambda _ = None :" in lines[0]):
        lines.pop(0)

        file.seek(0)
        file.truncate()
        file.writelines(lines)
    readcontent()
  except Exception as e:
    print(f"An error occured while removing input changes: {e}")
    exit()

def clear():
    # For Unix/Linux
    if os.name == 'posix':
      os.system('clear')
    # For Windows
    elif os.name == 'nt':
      os.system('cls')

if __name__ == "__main__":
    runtests()
    






    




   
