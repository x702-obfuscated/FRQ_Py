identity='1cfe22920ef0043cfc8c5f3c203b5287428c64b849b2fff0b9e9494a17ebf818a97dbb298db459099f15d21fa1c98d46c59c857facf78ceac09a9d3ff8de0f10'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

assignment = "6-Simple-Functions-and-Calls"
inputval = "2"
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

    def isfunction(qnum,name):

        assert hasattr(m,name), f"Q{qnum}: Did you define a function named '{name}'? Did you use the 'def' keyword? Did you use parenthesis?"
        assert callable(getattr(m,name)), f"Q{qnum}: Expected '{name}' to be a function, but it is not." 

        return True

    def ismatch(pattern,feedback):
        global filecontent
        assert re.search(pattern, filecontent), feedback

    @test((
    (3, 1, 2),
    (0, 0, 0),
    (4, -1, 5),
    (300, 100, 200),
    (-75, -50, -25),
    ))
    def t1(*tests):
        n = 1; fun = "add"
        isfunction(n,fun)
        ismatch(
            r"def\s*add\s*\(\s*a\s*,\s*b\s*\):", 
            f"Q{n}: Is your definition written correctly? Does '{fun}' have parameters 'a' and 'b'?"
        )

        for t in tests:
            assert t[0] == getattr(m,fun)(t[1],t[2]), f"Q{n}: Called {fun}({t[1]},{t[2]}). Expected {t[0]}, but got {getattr(m,fun)(t[1],t[2])} instead."

        
    @test()
    def t2():
        n = 2; fun = "add"; var = "twosum"; p1 = "a"; p2 ="b"; a1 = 6 ; a2 = 4
        ismatch(
            rf"{var}\s*=\s*{fun}\(\s*{a1}\s*,\s*{a2}\s*\)",
            f"Q{n}: Did you call '{fun}' with the arguments {a1} and {a2}? Are {a1} and {a2} inside the parenthesis and separated by a comma? "
            f"Did you assign '{var}' to the '{fun}' call?"
        )

        ismatch(
            rf"print\(\s*{var}\s*\)",
            f"Q{n}: Did you print '{var}'?"
        )

    @test((
    (1, 3, 2),
    (0, 5, 5),
    (-3, 2, 5),
    (100, 300, 200),
    (-25, -50, -25),
    ))
    def t3(*tests):
        n = 3; fun = "subtract"; p1 = "minuend"; p2="subtrahend"
        isfunction(n,fun)
        ismatch(
            rf"def\s*{fun}\s*\(\s*{p1}\s*,\s*{p2}\s*\):", 
            f"Q{n}: Is your definition written correctly? Does '{fun}' have parameters '{p1}' and '{p2}'?"
        )

        for t in tests:
            assert t[0] == getattr(m,fun)(t[1],t[2]), f"Q{n}: Called {fun}({t[1]},{t[2]}). Expected {t[0]}, but got {getattr(m,fun)(t[1],t[2])} instead."

    @test()
    def t4():
        n = 4; fun = "subtract"; var = "twodiff"; p1 = "minuend"; p2 ="subtrahend"; a1 = 1024 ; a2 = 512
        ismatch(
            rf"{var}\s*=\s*{fun}\(\s*{a1}\s*,\s*{a2}\s*\)",
            f"Q{n}: Did you call '{fun}' with the arguments {a1} and {a2}? Are {a1} and {a2} inside the parenthesis and separated by a comma? "
            f"Did you assign '{var}' to the '{fun}' call?"
        )

        ismatch(
            rf"print\(\s*{var}\s*\)",
            f"Q{n}: Did you print '{var}'?"
        )


    
    @test((
    (6, 3, 2),
    (25, 5, 5),
    (10, 2, 5),
    (60000, 300, 200),
    (1250, -50, -25),
    ))
    def t5(*tests):
        n = 5; fun = "multiply"; p1 = "x"; p2="y"
        isfunction(n,fun)
        ismatch(
            rf"def\s*{fun}\s*\(\s*{p1}\s*,\s*{p2}\s*\):", 
            f"Q{n}: Is your definition written correctly? Does '{fun}' have parameters '{p1}' and '{p2}'?"
        )

        for t in tests:
            assert t[0] == getattr(m,fun)(t[1],t[2]), f"Q{n}: Called {fun}({t[1]},{t[2]}). Expected {t[0]}, but got {getattr(m,fun)(t[1],t[2])} instead."

    @test()
    def t6():
        n = 6; fun = "multiply"; var = "twoproduct"; p1 = "x"; p2 ="y"; a1 = 128 ; a2 = 8
        ismatch(
            rf"{var}\s*=\s*{fun}\(\s*{a1}\s*,\s*{a2}\s*\)",
            f"Q{n}: Did you call '{fun}' with the arguments {a1} and {a2}? Are {a1} and {a2} inside the parenthesis and separated by a comma? "
            f"Did you assign '{var}' to the '{fun}' call?"
        )

        ismatch(
            rf"print\(\s*{var}\s*\)",
            f"Q{n}: Did you print '{var}'?"
        )

    @test((
    (2, 4, 2),
    (1, 5, 5),
    (0, 0, 5),
    (1.5, 300, 200),
    (2, -50, -25),
    ))
    def t7(*tests):
        n = 7; fun = "divide"; p1 = "dividend"; p2="divisor"
        isfunction(n,fun)
        ismatch(
            rf"def\s*{fun}\s*\(\s*{p1}\s*,\s*{p2}\s*\):", 
            f"Q{n}: Is your definition written correctly? Does '{fun}' have parameters '{p1}' and '{p2}'?"
        )

        for t in tests:
            assert t[0] == getattr(m,fun)(t[1],t[2]), f"Q{n}: Called {fun}({t[1]},{t[2]}). Expected {t[0]}, but got {getattr(m,fun)(t[1],t[2])} instead."

    @test()
    def t8():
        n = 8; fun = "divide"; var = "twoquotient"; p1 = "dividend"; p2 ="divisor"; a1 = 65536 ; a2 = 1024
        ismatch(
            rf"{var}\s*=\s*{fun}\(\s*{a1}\s*,\s*{a2}\s*\)",
            f"Q{n}: Did you call '{fun}' with the arguments {a1} and {a2}? Are {a1} and {a2} inside the parenthesis and separated by a comma? "
            f"Did you assign '{var}' to the '{fun}' call?"
        )
        ismatch(
            rf"print\(\s*{var}\s*\)",
            f"Q{n}: Did you print '{var}'?"
        )

    @test((
    ("hello world", "hello ", "world"),
    ("123abc", "123", "abc"),
    ("testcase", "test", "case"),
    ("foobar", "foo", "bar"),
    ("2025-04-09", "2025-", "04-09"),
    ))
    def t9(*tests):
        n = 9; fun = "concatenate"; p1 = "front_half"; p2="back_half"
        isfunction(n,fun)
        ismatch(
            rf"def\s*{fun}\s*\(\s*{p1}\s*,\s*{p2}\s*\):", 
            f"Q{n}: Is your definition written correctly? Does '{fun}' have parameters '{p1}' and '{p2}'?"
        )

        for t in tests:
            assert t[0] == getattr(m,fun)(t[1],t[2]), f"Q{n}: Called {fun}({t[1]},{t[2]}). Expected {t[0]}, but got {getattr(m,fun)(t[1],t[2])} instead."

    @test()
    def t10():
        n = 10; fun = "concatenate"; var = "joined"; p1 = "front_half"; p2 ="back_half"; a1 = "\"It means \"" ; a2 = "\"to join together.\""
        ismatch(
            rf"{var}\s*=\s*{fun}\(\s*{a1}\s*,\s*{a2}\s*\)",
            f"Q{n}: Did you call '{fun}' with the arguments {a1} and {a2}? Are {a1} and {a2} inside the parenthesis and separated by a comma? "
            f"Did you assign '{var}' to the '{fun}' call?"
        )

        ismatch(
            rf"print\(\s*{var}\s*\)",
            f"Q{n}: Did you print '{var}'?"
        )


    @test()
    def t11():
        ismatch(
            r"print\(\s*[\"']Its[\"']\s*,\s*[\"']not[\"']\s*,\s*[\"']a[\"']\s*,\s*[\"']bug[\"']\s*,\s*[\"']its[\"']\s*,\s*[\"']a[\"']\s*,\s*[\"']feature[\"']\s*\)",
            f"Q11: Did you use only one print call? Did you use commas (,) ? Make sure you are not using 'sep'. Check capitalization and spaces."
                
        )
    
    @test()
    def t12():
        words = ("Its ", "a ", "twist ", "ENDing.")

        for word in words:
            ismatch(
                r"print\(\s*[\"']"f"{word}"r"[\"']\s*,\s*end\s*=\s*"r"[\"'][\"']\s*\)",
                f"Q12: Did you use a separate print call? Did you use commas (,) ? Are you setting the 'end' parameter? Check capitalization and spaces." 
            )

    @test()
    def t13():
        ismatch(
            r"print\(\s*[\"']First[\"']\s*,\s*[\"']Second[\"']\s*,\s*[\"']Third[\"']\s*,\s*[\"']Fourth[\"']\s*,\s*sep\s*=\s*[\"']\|[\"']\s*\)",
            f"Q13: Did you use only one print call? Did you use commas (,) ? Are you setting the 'sep' parameter? Check capitalization and spaces."
        )

    @test()
    def t14():
        ismatch(
            r"int\(\s*input\(\s*[\"']Enter a number:\\n[\"']\s*\)\s*\)",
            f"Q14: Did you use input()? Did you include the correct prompt 'Enter a number:\\n'? Did you convert to an integer with int()? Check capitalization and spaces."
        )

        assert hasattr(m, "num"), "Q14: Did you define a variable named 'num'?"
        assert getattr(m, "num") == 2 , "Q14: Did you assign 'num' to your nested int(input()) call?"
        
        ismatch(
            r"print\(\s*num\s*\*\s*5\s*\)",
            "Q14: Did you print 'num' multiplied by 5? Did you use the multiplication operator? Don't use quotes(\" or ')."
        )

    @test()
    def t15():
        ismatch(
            r"float\(\s*input\(\s*[\"']Enter a number:\\n[\"']\s*\)\s*\)",
            f"Q15: Did you use input()? Did you include the correct prompt 'Enter a number:\\n'? Did you convert to a float with float()? Check capitalization and spaces."
        )

        assert hasattr(m, "num"), "Q15: Did you define a variable named 'flo'?"
        assert getattr(m, "num") == 2.0 , "Q15: Did you assign 'flo' to your nested float(input()) call?"
        
        ismatch(
            r"print\(\s*flo\s*\*\s*3.14\s*\)",
            "Q15: Did you print 'flo' multiplied by 3.14? Did you use the multiplication operator? Don't use quotes(\" or ')."
        )
    

    @test()
    def t16():
        ismatch(
            r"print\(\s*len\(\s*[\"']abcdefghijklmnopqrstuvwxyz[\"']\s*\)\s*\)",
            "Q16: Did you print? Did you use the correct length function call? Did you use quotes (\" or ')? Did you use \"abcdefghijklmnopqrstuvwxyz\" as an argument for the length function call?"
        )
        ismatch(
            r"print\(\s*len\(\s*[\"']a b c d e f g h i j k l m n o p q r s t u v w x y z [\"']\s*\)\s*\)",
            "Q16: Did you print? Did you use the correct length function call? Did you use quotes (\" or ')? Did you use \"a b c d e f g h i j k l m n o p q r s t u v w x y z \" as an argument for the length function call?"
        )

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
    alltests.append(t11)
    alltests.append(t12)
    alltests.append(t13)
    alltests.append(t14)
    alltests.append(t15)
    alltests.append(t16)

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
    change_inputfunction(inputval)
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
                    # report.append(f"\u2705 Test {num} Passed\n")
                except AssertionError as e:
                    numfailed +=1
                    # report.append(f"\u274C Test {num} Failed :\n {str(e)}\n")
                    report.append(f"\u274C Test Failed :\n {str(e)}\n")
            
            for param in params:
                num+=1
                try:
                    function(*param)
                    numpassed += 1
                    # report.append(f"\u2705 Test {num} Passed\n")
                except AssertionError as e:
                    numfailed +=1
                    # report.append(f"\u274C Test {num} Failed :\n {str(e)}\n")
                    report.append(f"\u274C Test Failed :\n {str(e)}\n")
        return wrapper
    return decorator

def runtests():
    checkintegrity()
    try:
        change_inputfunction(inputval)
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
    
    change_inputfunction(inputval)
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

    report.insert(0,"\n")
    if numpassed:
        report.insert(0,f"[ Tests Passed \u2705: {numpassed} : {passpercent}% ]\n")
    if numfailed:
        report.insert(0,f"[ Tests Failed \u274C: {numfailed} : {failpercent}% ]\n")

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
        if "Test Failed" in r:
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
    






    




   
