identity='4b3525b461dbab2cb5b0b6ae73e1895d4ccf5bd65585aad862344316fb47e79e8a22fc49a99449a2271ce0382681609491cca827509f62a71497a7474e2f8300'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

assignment = "32-Conditionals"
inputval = "2"
path = Path(__file__).parent
thispath = Path(__file__)
filepath = "main.py"
filecontent = ""
numpassed = 0
numfailed = 0
num = 0
qnum = 0
report = []
alltests = []

def assessvar(module,name,value=None,dtype=None,size=None,size_operator = "=="):
    global qnum
    
    assert hasattr(module,name), f"Q{qnum}: Did you define a variable named '{name}'?"
    var = getattr(module,name)
    if dtype is not None:
        assert isinstance(var, dtype), f"Q{qnum}: Expected '{name}' to store a {dtype} type value, but instead it references a {type(var)} type value."

    if size:
        operation = "AN ERROR OCCURED"
        feedback = f"Q{qnum}: Expected '{name}' name to be {operation} length {size}, but instead it has a length of {len(var)}." 
        if size_operator == "==":
            operation = "equal to"
            assert len(var) == size, feedback
        elif size_operator == ">=":
            operation = "greater than or equal to"
            assert len(var) >= size, feedback
        elif size_operator == "<=":
            operation = "less than or equal to"
            assert len(var) <= size, feedback
        elif size_operator == ">":
            operation = "greater than"
            assert len(var) > size, feedback
        elif size_operator == "<":
            operation = "less than"
            assert len(var) < size, feedback
        elif size_operator == "!=":
            operation = "not equal to"
            assert len(var) !=  size, feedback

    if value is not None:
        if isinstance(value, str):
            value = f"{value}"
        if isinstance(var,str):
            var = f"{var}"
        assert var == value, f"Q{qnum}: Expected '{name}' to reference {value}, but instead it references {var}."

def assessfun(module,name,*args,value=None,dtype=None):
    global qnum

    assert hasattr(module,name), f"Q{qnum}: Did you define a function named '{name}'? Did you use the 'def' keyword? Did you use parenthesis?"
    fun = getattr(module,name)
    assert callable(fun), f"Q{qnum}: Expected '{name}' to reference a function, but instead it references {fun} ." 

    arg_str = "" 
    for i,arg in enumerate(args): 
        if i == len(args)-1:
            if isinstance(arg,str):
                arg_str += f"\"{arg}\""
            else:
                arg_str += f"{arg}" 
        else:
            if isinstance(arg,str):
                arg_str += f"\"{arg}\","
            else:
                arg_str += f"{arg},"

    if value or dtype:
        if isinstance(value, str):
            value = f"\"{value}\""
        try: 
            result = fun(*args)
            if isinstance(result,str):
                result = f"\"{result}\""
        except TypeError as e:
            if "positional arguments" in str(e) and "were given" in str(e):
                raise AssertionError(f"Q{qnum}, Expected '{name}' to have {len(args)} parameters, but it does not. How many parameters are there in the parenthesis ()?")
            else:
                raise AssertionError(f"Q{qnum}: {name}({arg_str}) was called. But a runtime error occured and you need to fix your code --> {e}\nTry copying {name}({arg_str}) into your code and running it.")
        except Exception as e:
            raise AssertionError(f"Q{qnum}: {name}({arg_str}) was called. But a runtime error occured and you need to fix your code --> {e}\nTry copying {name}({arg_str}) into your code and running it.")

        if dtype:
            assert isinstance(result,dtype), f"Q{qnum}: Expected '{name}' to store a {dtype} type value, but instead it references a {type(result)} type value."
        if value:
            assert result == value, f"Q{qnum}: {name}({arg_str}) was called.\nThe test expected a result of: {value} :, but got: {result} :instead."

def ismatch(pattern,feedback):
    global filecontent,qnum
    assert re.search(pattern, filecontent), f"Q{qnum}: {feedback}. Check character case (lower/upper), spaces, and specificity."


def maketests(m=None):
    global qnum

    @test()
    def t1():
        global qnum
        qnum += 1
        
        tests = [
            (True, True),
            (False, False),
            (1, True),
            (0, False),
            ("True", True),
            (None, False),
            ([], False),
            ([True], True),
            (42, False),
            (-1, False)
        ]
        for e in tests:
            assessfun(m,"is_True",e[0],value=e[1])
    
    @test()
    def t2():
        global qnum
        qnum += 1

        tests = [
            (10, "POSITIVE"),
            (-5, "NEGATIVE"),
            (1, "POSITIVE"),
            (-1, "NEGATIVE"),
            (1000, "POSITIVE"),
            (-1000, "NEGATIVE"),
            (0.1, "POSITIVE"),
            (-0.1, "NEGATIVE"),
            (999999, "POSITIVE"),
            (-999999, "NEGATIVE"),
            (0,"ZERO")
        ]
        for e in tests:
            assessfun(m,"get_sign",e[0],value=e[1])

    @test()
    def t3():
        global qnum
        qnum += 1

        tests = [
            (2, "EVEN"),
            (3, "ODD"),
            (0, "EVEN"),
            (-2, "EVEN"),
            (-3, "ODD"),
            (100, "EVEN"),
            (101, "ODD"),
            (99998, "EVEN"),
            (99999, "ODD"),
            (-100000, "EVEN")
        ]

        for e in tests:
            assessfun(m,"is_even",e[0],value=e[1])

    @test()
    def t4():
        global qnum
        qnum += 1

        tests = [
            (10, 2, "10 is divisible by 2"),
            (10, 3, "10 is NOT divisible by 3"),
            (15, 5, "15 is divisible by 5"),
            (17, 4, "17 is NOT divisible by 4"),
            (0, 1, "0 is divisible by 1"),
            (9, 3, "9 is divisible by 3"),
            (8, 2, "8 is divisible by 2"),
            (7, 2, "7 is NOT divisible by 2"),
            (100, 25, "100 is divisible by 25"),
            (99, 10, "99 is NOT divisible by 10"),
            (0,0,"Division by 0 is UNDEFINED")
        ] 
        
        
        for e in tests:
            assessfun(m,"is_divisible",e[0],e[1],value=e[2])

    @test()
    def t5():
        global qnum
        qnum += 1

        tests = [
            ("green", "GO"),
            ("yellow", "CAUTION"),
            ("red", "STOP"),
            ("blue", "ERROR"),
            ("", "ERROR"),
            (None, "ERROR"),
            (123, "ERROR"),
            ("purple", "ERROR"),
            ("orange", "ERROR"),
            ("black", "ERROR")
        ]

        for e in tests:
            # if isinstance(e[0],str):
            #     assessfun(m,"stoplight",*e[0],value=e[1])
            # else:
            assessfun(m,"stoplight",e[0],value=e[1])

    @test()
    def t6():
        global qnum
        qnum += 1

        tests = [
            (0, "SLEEP"),
            (1, "SLEEP"),
            (7, "SLEEP"),
            (8, "WAKEUP"),
            (9, "WAKEUP"),
            (12, "WAKEUP"),
            (15, "WAKEUP"),
            (22, "WAKEUP"),
            (23, "SLEEP"),
            (6, "SLEEP")
        ]

        for e in tests:
            assessfun(m,"alarm",e[0],value=e[1])

    @test()
    def t7():
        global qnum
        qnum += 1

        tests = [
            ('a', "VOWEL"),
            ('e', "VOWEL"),
            ('i', "VOWEL"),
            ('o', "VOWEL"),
            ('u', "VOWEL"),
            ('b', "CONSONANT"),
            ('c', "CONSONANT"),
            ('d', "CONSONANT"),
            ('z', "CONSONANT"),
            ('y', "CONSONANT")
        ]

        for e in tests:
            assessfun(m,"is_vowel",e[0],value=e[1])

    @test()
    def t8():
        global qnum
        qnum += 1

        tests = [
            (3, 5, 1, 5),
            (1, 3, 5, 5),
            (7, 7, 7, 7),
            (10, 5, 5, 10),
            (0, 0, 0, 0),
            (10, 10, 5, 10),
            (-1, -5, -3, -1),
            (2, 2, 2, 2),
            (8, 4, 6, 8),
            (4, 9, 7, 9)
        ]

        for e in tests:
            assessfun(m,"get_max",*e[0:3],value=e[3])

    @test()
    def t9():
        global qnum
        qnum += 1
        tests = [
            (0, 0, "ORIGIN"),
            (0, 5, "X-AXIS"),
            (5, 0, "Y-AXIS"),
            (3, 2, "QI"),
            (-3, 2, "QII"),
            (-3, -2, "QIII"),
            (3, -2, "QIV"),
            (0, -5, "X-AXIS"),
            (4, 0, "Y-AXIS"),
            (-5, 0, "Y-AXIS")
        ]
        for e in tests:
            assessfun(m,"get_quadrant",*e[0:2],value=e[2])

    @test()
    def t10():
        global qnum
        qnum += 1
        tests = [
            (3, 5, "+", 8),
            (10, 2, "-", 8),
            (6, 3, "*", 18),
            (10, 2, "/", 5),
            (10, 0, "/", "UNDEFINED"),
            (3, 5, "/", 0.6),
            (5, 2, "?", "Operation Not Supported"),
            (0, 0, "+", 0),
            (7, 3, "-", 4),
            (-2, 5, "*", -10),
            (8, 2, "/", 4)
        ]
        for e in tests:
            assessfun(m,"calculate",*e[0:3],value=e[3])
    

    @test()
    def t11():
        matches = re.findall(r"if",filecontent)
        if not len(matches) >= 10:
            raise AssertionError("Expected an if statement for each function. Did you use and if statment in each question?")

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
    






    




   
