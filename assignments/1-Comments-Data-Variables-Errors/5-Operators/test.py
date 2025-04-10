identity='40efe5455ae9fef52fcdecb110a67f7fa5a622a7a1f94babc81bd934f8ad66f9029dabe0feeca5ab449223a1c8e6f83afeb703b5a18813470cd07f6d958edd21'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

assignment = "5-Operators"
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

    # @test(
    #     ("nothing", None),
    #     ("switch", True),
    #     ("num", 42),
    #     ("percent",0.75),
    #     ("name","Alice"),
    #     ("fruits",["apple","banana","cherry"]),
    #     ("coordinates",(10,20)),
    #     ("person", {"name":"Bob","age":30})
    # )
    # def t1(var,val):
    #     assert hasattr(m,var), f"Expected a defined variable named '{var}', but was not found."
    #     assert getattr(m,var) == val, f"Expected '{var}' to point to {val} , but it does not."

    def check_var(var,value,q):
        assert hasattr(m,var), f"Q{q}: Expected to find a variable named '{var}', but it was not found."
        assert getattr(m,var) == value, f"Q{q}: Expected '{var}' to reference the value '{value}', instead it references '{getattr(m,var)}'"

    @test()
    def t1():
        check_var("joined","helloworld",1)
        assert re.search(r"[\"']hello[\"']\s*\+\s*[\"']world[\"']",filecontent), 'Q1: Expected "hello" and "world" concatenated using +, but was not found.'

    @test()
    def t2():
        check_var("duped","appleappleapple",2)
        assert re.search(r"[\"']apple[\"']\s*\*\s*3", filecontent), "Q2: Expected 'apple' duplicated with *, but it was not found." 

    @test()
    def t3():
        check_var("int_to_str","8",3)
        assert re.search(r"str\(\s*8\s*\)",filecontent), "Q3: Expected a str() call with the argument 8, but was not found."
        assert re.search(r"print\(\s*type\(\s*int_to_str\s*\)\s*\)",filecontent), "Q3: Expected a print() containing type() with the argument 'int_to_str', but was not found."

    @test() 
    def t4():
        check_var("str_to_int", 90, 4)
        assert re.search(r"int\(\s*[\"']90[\"']\s*\)",filecontent), "Q4: Expected an int() call with the argument \"90\", but was not found. Is 90 in quotes? Did you cast with int()?"
        assert re.search(r"print\(\s*type\(\s*str_to_int\s*\)\s*\)",filecontent), "Q4: Expected a print() containing type() with the argument 'str_to_int', but was not found."
    
    @test()
    def t5():
        check_var("int_to_float",2.0,5)
        assert re.search(r"float\(\s*2\s*\)",filecontent), "Q5: Expected a float() call with the arguemnt 2, but was not found."
        assert re.search(r"print\(\s*type\(\s*int_to_float\s*\)\s*\)",filecontent), "Q5: Expected a print() containing type() with the argument 'int_to_float', but was not found."

    @test(
        ("addition", 897 + 548, 6,r"897\s*\+\s*548", "addition"),
        ("subtraction", 3209-1120, 7, r"3209\s*\-\s*1120", "subtraction"),
        ("product", 1200*34, 8, r"1200\s*\*\s*34", "multiplication"),
        ("quotient",612/9, 9, r"612\s*/\s*9", "division"),
        ("floor",429//17, 10, r"429\s*//\s*17", "floor/integer division"),
        ("remainder",429%17,11, r"429\s*\%\s*17", "remainder/modulo"),
        ("exponents",2**8, 12, r"2\s*\*\*\s*8", "exponentiation"),
    )
    def t6(var, value, q, pattern, operation):
        check_var(var, value, q)
        assert re.search(pattern, filecontent), f"Q{q}: Expected to find the {operation} operator, but it was not found."

    @test(
        ("alpha",100),
        ("beta", 200),
        ("gamma", 300)
    )
    def t7(var, value):
        check_var(var, value,"13-18")

    
    @test(
        (13, "thirteen", False, "greater than", r"alpha\s*\>\s*beta"),
        (14, "fourteen", True, "less than", r"alpha\s*\<\s*beta"),
        (15, "fifteen", False, "greater than or equal to", r"beta\s*\>=\s*gamma"),
        (16, "sixteen", True, "less than or equal to", r"beta\s*\<=\s*gamma"),
        (17, "seventeen", False, "equal to", r"alpha\s*==\s*gamma"),
        (18, "eighteen", True, "not equal to", r"gamma\s*\!=\s*alpha")
    )
    def t8(q,var, value,operation, pattern):
        check_var(var,value,q)
        assert re.search(pattern, filecontent), f"Q{q}: Did you use the {operation} operator. Did you use the right variables?"


    @test()
    def t9():
        check_var("list1d",["a","e","i","o","u"],"19-20")

        assert hasattr(m,"character"), "Q19-20: Expected to find a variable named 'character', but it was not found."
        c = getattr(m,"character")
        try:
            assert (c.isalpha() and len(c) == 1), f"Q19-20: Expected 'character' to point to a single character of the alphabet, but instead it points to '{c}'"
        except AttributeError as e:
            raise AssertionError("Expected 'character' to reference a value of type <class 'str'> (String), but it does not.")


    @test()
    def t10():
        try:
            c = getattr(m,"character")
            l = getattr(m,"list1d")
        except:
            raise AssertionError("This test requires Test 22 to be passing.")
        
        check_var("nineteen", c in l, 19)
        assert re.search(r"character\s*in\s*list1d", filecontent), "Q19: Did you use the correct variable names? Did you use the member of (apart of) operator?"
        check_var("twenty", c not in l, 20)
        assert re.search(r"character\s*not\s*in\s*list1d",filecontent),"Q20: Did you use the correct variable names, Did you use the not a member of (not apart of) operator?"
        
        
    
    @test()
    def t11():
        assert re.search(r"up\s*\+=\s*1", filecontent), "Q21: Did you use the  compound addition and assignment operator? Did you increase by 1? Did you use the 'up' variable?"
        check_var("up", 1, "21")
        
        assert re.search(r"down\s*\-=\s*1", filecontent), "Q22: Did you use the 'down' variable? Did you use the compound subtraction and assignment operator? Did you decrease by 1?"
        check_var("down",9,"22")

    @test(
        ("yes", True),
        ("no", False),
        ("one", True),
        ("zero", False)
    )
    def t12(var, value):
        check_var(var, value, "23-25")

    @test(
        (23, r"print\(\s*not\s*yes\s*\)","Did you use the NOT operator? Did you print? Did you use the correct variable?"),
        (23, r"print\(\s*not\s*no\s*\)","Did you use the NOT operator? Did you print? Did you use the correct variable?"), 
        (23, r"print\(\s*not\s*one\s*\)","Did you use the NOT operator? Did you print? Did you use the correct variable?"), 
        (23, r"print\(\s*not\s*zero\s*\)","Did you use the NOT operator? Did you print? Did you use the correct variable?"), 
        (24, r"print\(\s*yes\s*and\s*one\s*\)","Did you use the AND operator? Did you print? Did you use the correct variables?"), 
        (24, r"print\(\s*yes\s*and\s*no\s*\)","Did you use the AND operator? Did you print? Did you use the correct variables?"),   
        (24, r"print\(\s*no\s*and\s*one\s*\)","Did you use the AND operator? Did you print? Did you use the correct variables?"), 
        (24, r"print\(\s*no\s*and\s*zero\s*\)","Did you use the AND operator? Did you print? Did you use the correct variables?"),
        (25, r"print\(\s*yes\s*or\s*one\s*\)","Did you use the OR operator? Did you print? Did you use the correct variables?"), 
        (25, r"print\(\s*yes\s*or\s*no\s*\)","Did you use the OR operator? Did you print? Did you use the correct variables?"),   
        (25, r"print\(\s*no\s*or\s*one\s*\)","Did you use the OR operator? Did you print? Did you use the correct variables?"), 
        (25, r"print\(\s*no\s*or\s*zero\s*\)","Did you use the OR operator? Did you print? Did you use the correct variables?"),
    )
    def t13(q,pattern, feedback):
        assert re.search(pattern, filecontent), f"Q{q}: {feedback}"
    

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
    






    




   
