identity='3602e22e1b954bea09c9728a8bf9475a67be6e11f2f3ce082e7fbc3ae970163cf2e4b74069964682fd1b19b678e89ba370df34cfd1567c5d2d742ed2491a755c'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

assignment = "21-Lists"
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

def assessfun(module,name,*params,value=None,dtype=None):
    global qnum

    assert hasattr(module,name), f"Q{qnum}: Did you define a function named '{name}'? Did you use the 'def' keyword? Did you use parenthesis?"
    fun = getattr(module,name)
    assert callable(fun), f"Q{qnum}: Expected '{name}' to reference a function, but instead it references {fun} ." 

    if value or dtype:
        if isinstance(value, str):
            value = f"{value}"
        try: 
            result = fun(*params)
            if isinstance(result,str):
                result = f"{result}"
        except TypeError as e:
            raise AssertionError(f"Q{qnum}, Expected '{name}' to have {len(params)} parameters, but it does not. How many parameters are there in the parenthesis ()?")
        
        if dtype:
            assert isinstance(result,dtype), f"Q{qnum}: Expected '{name}' to store a {dtype} type value, but instead it references a {type(result)} type value."
        if value:
            assert result == value, f"Q{qnum}: Expected '{name}' to return {value} but instead it returns {result} "

def ismatch(pattern,feedback):
    global filecontent,qnum
    assert re.search(pattern, filecontent), f"Q{qnum}: {feedback}. Check character case (lower/upper), spaces, and specificity."


def maketests(m=None):
    global qnum
    @test()
    def t1():
        global qnum
        qnum += 1
        assessvar(m,"empty",[], list)

    @test()
    def t2():
        global qnum
        qnum += 1
        assessvar(m,"my_letters",dtype = list,size = 0, size_operator= ">")


    @test()
    def t3():
        global qnum
        qnum += 1
        assessvar(m,"arabic_numerals",list("0123456789"),list)
    
    @test()
    def t4():
        from string import ascii_uppercase,ascii_lowercase,digits
        global qnum
        qnum += 1
        assessvar(m,"upper_alpha",list(ascii_uppercase),list)
        assessvar(m,"lower_case",list(ascii_lowercase),list)
        assessvar(m,"numerals", [int(x) for x in list(digits)],list)

        tvals = [
                (True, 3, [1, 2, 3, 4]),
                (False, 5, [1, 2, 3, 4]),
                (True, 'a', ['a', 'b', 'c']),
                (False, 'z', ['x', 'y', 'w']),
                (True, None, [None, 0, False]),
                (False, True, [False, 0, None]),
                (True, 2.5, [1.1, 2.5, 3.3]),
                (False, 7, []),
                (True, (1, 2), [(1, 2), (3, 4)]),
                (False, [1, 2], [[3, 4], [5, 6]])
        ]

        for val in tvals:
            assessfun(m,"is_apart",val[1],val[2],value=val[0],dtype=bool)


    
    @test()
    def t5():
        global qnum
        qnum += 1
        assessvar(m,"character",dtype = str,size=1)
        
        for e in ["upper_alpha","lower_alpha","numerals"]:
            ismatch(
                rf"print\(\s*is_apart\(\s*character\s*,\s*{e}\s*\)\s*\)",
                f"Did you call 'is_apart'? Did you pass 'character' and '{e}' as arguments? Did you print?"
            )


    @test()
    def t6():
        from string import ascii_uppercase,ascii_lowercase,digits
        global qnum
        qnum += 1
        assessvar(m,"upper_alpha",list(ascii_uppercase),list)
        assessvar(m,"lower_case",list(ascii_lowercase),list)
        assessvar(m,"numerals", [int(x) for x in list(digits)],list)

        joined = getattr("upper_alpha") + getattr("lower_alpha") + getattr("numerals")
        assessvar(m,"alphanumeric",joined, list)

    @test()
    def t7():
        global qnum
        qnum += 1
        assessvar(m,"front",dtype=list)
        assessvar(m,"back",dtype=list)
        joined = getattr(m,"front") + getattr(m,"back")
        assessvar(m,"joined",joined,list)
        ismatch(
            r"joined\s*=\s*front\s*\+\s*back",
            f"Did you assign 'joined' and concatenate 'front' to 'back' in the same statement?" 
        )

    @test()
    def t8():
        from string import ascii_uppercase,ascii_lowercase,digits
        global qnum
        qnum += 1
        assessvar(m,"upper_alpha",list(ascii_uppercase),list)
        assessvar(m,"lower_case",list(ascii_lowercase),list)
        assessvar(m,"numerals", [int(x) for x in list(digits)],list)

        grouped = getattr(m,"upper_alpha") + getattr(m,"lower_alpha") + getattr(m,"numerals")
        assessvar(m,"grouped",grouped,list)
        ismatch(
            r"grouped\s*\+=",
            "Did you concatenate and assign 'grouped' in the same statement?"
        )
        ismatch(
            r"print\(\s*grouped\s*\)",
            "Did you print out grouped?"
        )

    @test()
    def t9():
        global qnum
        qnum += 1
        assessvar(m,"zeros",dtype=list)
        assert getattr(m,"zeros") == [0]* 1000, f"Q{qnum}: 'zeros' does not match the expected value."
        ismatch(
            r"zeros\s*\=\s*[0]\s*1000",
            f"Did you create a list with single 0 inside? Did you multiply? Did you assign the result to 'zeros'?"
        )

    @test()
    def t10():
        global qnum
        qnum += 1
        assessvar(m,"binary",dtype=list)
        assert getattr(m,"binary") == [int(x) for x in "10001101"]*500, f"Q{qnum}: 'binary' does not match the expected value."
        ismatch(
            r"binary\s*\*=\s*500",
            f"Did you duplicate and assign to 'binary' in the same statement?"
        )

    @test()
    def t11():
        global qnum
        qnum += 1
        
        for e in [("first","0"),("last","-1"),("43rd","42"),("16th to last","-16")]:
            ismatch(
                rf"print\(\s*alphanumeric\[\s*{e[1]}\s*\]\)",
                f"Did you print the {e[0]} index? Did you use the correct index(what number do indexes start with)?"
            )

    @test()
    def t12():
        global qnum
        qnum += 1
        assessvar(m,"pylist",dtype=list,size=100)
        assert getattr(m,"pylist")[49] == "PYTHON", f"Q{qnum} Expected the 50th element of 'pylist' to store \"PYTHON\", but instead it stores {getattr(m,"pylist")[49]}"
        assert getattr(m,"pylist")[-19] == "PROGRAMMING", f"Q{qnum} Expected the 19th to last element of 'pylist' to store \"PROGRAMMING\", but instead it stores {getattr(m,"pylist")[-19]}"

    @test()
    def t13():
        global qnum
        qnum += 1
        assessvar(m,"alphanumeric",dtype=list)

        ismatch(
            r"print\(\s*alphanumeric\[\s*\:\s*26\s*\])",
            f"Did you print the first 26 characters? What number do indexes start at? What is different about stop indexes? What are the default values?"
        )
        ismatch(
            r"print\(\s*alphanumeric\[\s*\-10\s*:\s*\])",
            f"Did you print the last 10 characters? What number do indexes start at? What is different about stop indexes? What are the default values?"
        )
        ismatch(
            r"print\(\s*alphanumeric\[\s*26\s*:\s*52\])",
            f"Did you print the 27th through 52nd characters? What number do indexes start at? What is different about stop indexes? What are the default values?"
        )
        ismatch(
            r"print\(\s*alphanumeric\[\s*:\s*:\s*3\s*\])",
            f"Did you print every 3rd character? What number do indexes start at? What is different about stop indexes? What are the default values?"
        )
        ismatch(
            r"print\(\s*alphanumeric\[\s*:\s*:\s*-1\s*\])",
            f"Did you print the whole list in reverse? What number do indexes start at? What is different about stop indexes? What are the default values?"
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
    






    




   
