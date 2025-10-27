identity='6ffc3776cf0a63f1774899c5667d4e6d25bd9ebf35426cae11f30c0b6a36150527489b60719e410c85730d523e5eef808a8423b0ee1335a760fa68af33bef052'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re,sys,io

assignment = "42-For-Loops"
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

def assessfun(
    module,name,*args:tuple,
    returnval=None,outval=None,
    returntype=None
):
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

    if returnval is not None or returntype is not None:
        if isinstance(returnval, str):
            returnval = f"\"{returnval}\""
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

        
        if returntype is not None:
            assert isinstance(result,returntype), f"Q{qnum}: Expected '{name}' to store a {returntype} type value, but instead it references a {type(result)} type value."
        if returnval is not None:
            assert result == returnval, f"Q{qnum}: {name}({arg_str}) was called.\nThe test expected a result of: {returnval} :, but got: {result} :instead."

    if outval is not None:
        assert hasattr(module,name), f"'{name}' function definition not found. Did you define '{name}'?" #strip


        try:
            fun(*args) 
        except TypeError as e:
            if "positional arguments" in str(e) and "were given" in str(e):
                raise AssertionError(f"Q{qnum}: Expected '{name}' to have {len(args)} parameters, but it does not. How many parameters are there in the parenthesis ()?")
            else:
                raise AssertionError(f"Q{qnum}: {name}({arg_str}) was called. But a runtime error occured and you need to fix your code --> {e}\nTry copying {name}({arg_str}) into your code and running it.")
        except Exception as e:
            raise AssertionError(f"Q{qnum}: {name}({arg_str}) was called. But a runtime error occured and you need to fix your code --> {e}\nTry copying {name}({arg_str}) into your code and running it.")
        
        captured_output = io.StringIO() 
        sys.stdout = captured_output 
        fun(*args)
        sys.stdout = sys.__stdout__ 

        
        assert captured_output.getvalue().strip() == str(outval).strip(), \
        f"{name}({arg_str}) was called.\nThe test expected a result of \"{outval}\" , but got \"{captured_output.getvalue()}\" instead."



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
            (0, 16, 1),
            (5, 26, 5),
            (-10, -3, 2),
            (-50, -11, 10),
            (-5, 6, 1),
            (-100, 101, 20),
            (10, -11, -5),
            (50, -51, -10),
            (-3, 10, 3),
            (20, -5, -2)
        ]

    
        assessvar(m,"ranges",dtype=list,size=len(tests))

        ranges = [range(*t) for t in tests]

        for i,r in enumerate(ranges):
            mr = m.ranges[i]
            assert isinstance(mr,range), f"Q{qnum}: Expected ranges[{i}] to be of type <class 'range'> but instead was of type {type(mr[i])} ."
            if(tests[i][1] < 0):
                stop = tests[i][1] + 1
            else:
                stop = tests[i][1] - 1

            if(mr.stop < 0):
                stopsat = mr.stop + 1
            else:
                stopsat = mr.stop - 1

            assert m.ranges[i] == r, f"Q{qnum}: Expected ranges[{i}] to equal a range from {tests[i][0]} to {stop} by {tests[i][2]}s. But the range starts at {mr.start}; stops at {stopsat}; steps by {mr.step} ."



    @test()
    def t2():
        global qnum
        qnum += 1

        
        assessvar(m,"default_step",range(50,71,1))
        assessvar(m,"default_start_step",range(0,101,1))
        ismatch(
            r"range\(\s*50\s*,\s*71\s*\)",
            "Did you use the default step parameter value?"
        )

        ismatch(
            r"range\(\s*101\s*\)",
            "Did you use the default step parameter value? Did you use the default start parameter value?"
        )


    @test()
    def t3():
        global qnum
        qnum += 1 

        tests = [
            (1, 10, 2, "1 3 5 7 9 "),
            (0, 5, 1, "0 1 2 3 4 5 "),
            (3, 18, 3, "3 6 9 12 15 18 "),
            (10, 20, 5, "10 15 20 "),
            (1, 5, 1, "1 2 3 4 5 "),
            (0, 10, 3, "0 3 6 9 "),
            (10, 20, 4, "10 14 18 "),
            (5, 5, 1, "5 "),
            (1, 9, 2, "1 3 5 7 9 "),
            (0, 4, 2, "0 2 4 "),
            (-5, 5, 3, "-5 -2 1 4 "),
            (-10, -1, 2, "-10 -8 -6 -4 -2 "),
            (-20, -10, 3, "-20 -17 -14 -11 "),
            (-5, 5, 1, "-5 -4 -3 -2 -1 0 1 2 3 4 5 "),
            (-1, 4, 2, "-1 1 3 "),
            (-10, 10, 5, "-10 -5 0 5 10 "),
            (-15, -5, 4, "-15 -11 -7 "),
            (-30, -10, 10, "-30 -20 -10 "),
            (-6, 2, 2, "-6 -4 -2 0 2 "),
            (-9, 1, 3, "-9 -6 -3 0 ")
        ]

        for e in tests:
            assessfun(m,"upcount",*e[:3],outval=e[3])

    @test()
    def t4():
        global qnum
        qnum += 1 

        tests = [
            (10, 1, 2, "10 8 6 4 2 "),
            (5, 0, 1, "5 4 3 2 1 0 "),
            (18, 3, 3, "18 15 12 9 6 3 "),
            (20, 10, 5, "20 15 10 "),
            (5, 1, 1, "5 4 3 2 1 "),
            (10, 0, 3, "10 7 4 1 "),
            (20, 10, 4, "20 16 12 "),
            (5, 5, 1, "5 "),
            (9, 1, 2, "9 7 5 3 1 "),
            (4, 0, 2, "4 2 0 "),
            (5, -5, 2, "5 3 1 -1 -3 -5 "),
            (10, -10, 4, "10 6 2 -2 -6 -10 "),
            (3, -6, 2, "3 1 -1 -3 -5 "),
            (0, -5, 1, "0 -1 -2 -3 -4 -5 "),
            (10, -1, 3, "10 7 4 1 "),
            (6, -3, 2, "6 4 2 0 -2 "),
            (10, 0, 2, "10 8 6 4 2 0 ")
        ]

        for e in tests:
            assessfun(m,"downcount",*e[:3],outval=e[3])


    @test()
    def t5():
        global qnum
        qnum += 1

        tests = [
            ([1, 2, 3, 4, 5], "1 3 5 "),
            ([10, 12, 14, 16], ""),
            ([5, 7, 9, 11], "5 7 9 11 "),
            ([0, 2, 4, 6], ""),
            ([1], "1 "),
            ([2], ""),
            ([], ""),
            ([0, 1, 2, 3, 4, 5, 6, 7], "1 3 5 7 "),
            ([-1, -2, -3, -4], "-1 -3 "),
            ([10, 21, 34, 57, 60], "21 57 ")
        ]

        for e in tests:
            assessfun(m,"onlyodds",e[0],outval=e[1])


    @test()
    def t6():
        global qnum
        qnum += 1

        tests = [
            ([1, 2, 3, 4, 5], 15),
            ([10, -5, 3], 8),
            ([0, 0, 0, 0], 0),
            ([100, 200, 300], 600),
            ([-1, -2, -3, -4], -10),
            ([5], 5),
            ([], 0),
            ([1, -1, 1, -1], 0),
            ([7, 8, 9], 24),
            ([2, 3, 10, 1], 16)
        ]

        for e in tests:
            assessfun(m,"total",e[0],returnval=e[1])

    @test()
    def t7():
        global qnum
        qnum += 1

        tests = [
            ("hello", 2),
            ("world", 1),
            ("aeiou", 5),
            ("", 0),
            ("AEIOU", 5),
            ("programming", 3),
            ("Python", 1),
            ("count the vowels", 5),
            ("rhythm", 0),
            ("supercalifragilisticexpialidocious", 16),
            ("pneumonoultramicroscopicsilicovolcanoconiosis", 20),
            ("HELLO", 2),
            ("WORLD", 1),
            ("AEIOUaeiou", 10)
        ]


        for e in tests:
            assessfun(m,"num_vowels",e[0],returnval=e[1])


    @test()
    def t8():
        global qnum 
        qnum += 1
        
        tests = [
            ([1, 2, 3, 2, 4, 2], 2, [1, 3, 5]),
            (['a', 'b', 'a', 'c', 'a'], 'a', [0, 2, 4]),
            ([10, 20, 30, 40], 25, []),
            ([], 5, []),
            ([True, False, True, True], True, [0, 2, 3]),
            (['x', 'y', 'z'], 'y', [1]),
            ([0, 0, 0, 0], 0, [0, 1, 2, 3]),
            ([1.1, 2.2, 3.3, 2.2], 2.2, [1, 3]),
            (['apple', 'banana', 'apple', 'pear'], 'pear', [3]),
            (['cat', 'dog', 'bird'], 'fish', []),
            ([1, 1, 2, 1, 3, 1, 4], 1, [0, 1, 3, 5]),
            (['A', 'B', 'C', 'A', 'D'], 'A', [0, 3]),
            (['red', 'green', 'blue', 'red'], 'green', [1]),
            ([9, 8, 7, 9, 9], 9, [0, 3, 4]),
            ([None, None, 1, None], None, [0, 1, 3]),
            ([True, True, False, False], False, [2, 3]),
            (['one', 'two', 'three', 'four'], 'five', []),
            ([3.14, 2.71, 3.14, 1.61], 3.14, [0, 2]),
            ([100, 200, 300, 400, 500], 100, [0]),
            ([7, 8, 9, 10, 7, 7, 8], 8, [1, 6])
        ]

        for e in tests:
            assessfun(m,"search",*e[:2],returnval=e[2])
            


    @test()
    def t9():
        global qnum
        qnum += 1
        matches = re.findall(r"for", filecontent)
        if not len(matches) >= 5:
            raise AssertionError(f"Expected a for loop for each question. Did you use a for loop for each question?")


    alltests.append(t1)
    alltests.append(t2)
    alltests.append(t3)
    alltests.append(t4)
    alltests.append(t5)
    alltests.append(t6)
    alltests.append(t7)
    alltests.append(t8)
    alltests.append(t9)
    # alltests.append(t10)
    # alltests.append(t11)
    # alltests.append(t12)
    # alltests.append(t13)


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
    






    




   
