identity='ff4d806c991a6120b5fef64186624bcca6224b38c138de9889f4a1809d4dd1dff712eff077c6c6bded06701982fc24c5f72a86e8a31bb312affd888dd4fe295f'
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
report = []
alltests = []

def assessvar(module,qnum,name,value=None,dtype=None,size=None,size_operator = "=="):

    assert hasattr(module,name), f"Q{qnum}: Did you define a variable named '{name}'?"
    var = getattr(module,name)
    if dtype:
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

    if value:
        if isinstance(value, str):
            value = f"{value}"
        if isinstance(var,str):
            var = f"{var}"
        assert var == value, f"Q{qnum}: Expected '{name}' to reference {value}, but instead it references {var}."

def assessfun(module,qnum,name,*params,value=None,dtype=None):
    assert hasattr(m,name), f"Q{qnum}: Did you define a function named '{name}'? Did you use the 'def' keyword? Did you use parenthesis?"
    fun = getattr(m,name)
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
    global filecontent
    assert re.search(pattern, filecontent), f"Q{qnum}: {feedback}. Check character case (lower/upper), spaces, and specificity."


def maketests(m=None):
    qnum = 0




    @test()
    def t1():
        ismatch(
            r"print\(\s*[\"']ONE\\nTWO\\nTHREE[\"']\s*\)",
            "Q1: Did you replace the spaces with newline characters? Did you use a single string? Did you print? Check capitalization and spacing."
        )
   
    @test()
    def t2():
        ismatch(
            r"print\(\s*[\"']C:\\\\Users\\\\USERNAME\\\\Desktop[\"']\s*\)",
            "Q2: Did you use the correct escape character in order to use \\ in a string? Did you print? Did you use a single string? Check capitilization and spacing."
        )

    @test()
    def t3():
        ismatch(
            r"print\(\s*[\"']\\[\"']Where there\\?'s code. There\\?'s a bug.\\[\"'][\"']\s*\)",
            "Q3, Did you use the correct escape character? Do the quotation marks print out? DId you use a single string? Check capitilization and spacing."
        )

    @test()
    def t4():
        assert hasattr(m, "character"), "Q4: Is 'character' defined?"
        assert isinstance(getattr(m,"character"),str), "Q4: 'character' should reference a string, but it does not." 
        assert len(getattr(m,"character")) == 1, "Q4: 'character' should reference a single symbol, but it does not."

        ismatch(
            r"int_value\s*\=\s*ord\(\s*character\s*\)",
            "Q4: Did you use the ord() function call? Did you use 'character'? Did you assign the result to 'int_value'."
        )

        assert hasattr(m,"int_value"), "Q4: Is 'int_value' defined?"
        assert getattr(m,"int_value") == ord(getattr(m,"character")), "Q4:'int_value' does not store the correct value, did you convert with ord()?"

        ismatch(
            r"print\(\s*int_value\s*\)",
            "Q4: Did you print out 'int_value'? Did you use the variable name? Make sure 'int_value' is not in quotes. Check capitalization and spaces."
        )

    @test()
    def t5():
        assert hasattr(m, "int_value"), "Q5: Is 'int_value' defined?"
        assert isinstance(getattr(m,"int_value"),int), "Q5: 'int_value' should reference an integer, but it does not."

        ismatch(
            r"bin_value\s*=\s*bin\(\s*int_value\s*\)",
            "Q5: Did you use the bin() function call? Did you use 'int_value'? Did you assign the result to 'bin_value'."
        )

        assert hasattr(m,"bin_value"), "Q5: Is 'bin_value' defined?"
        assert getattr(m,"bin_value") == bin(getattr(m,"int_value")), "Q5:'bin_value' does not store the correct value, did you convert with bin()?"

        ismatch(
            r"print\(\s*bin_value\s*\)",
            "Q5: Did you print out 'bin_value'? Did you use the variable name? Make sure 'bin_value' is not in quotes. Check capitalization and spaces."
        )


    @test()
    def t6():
        assert hasattr(m, "int_value"), "Q6: Is 'int_value' defined?"
        assert isinstance(getattr(m,"int_value"),int), "Q6: 'int_value' should reference an integer, but it does not."

        ismatch(
            r"hex_value\s*=\s*hex\(\s*int_value\s*\)",
            "Q6: Did you use the hex() function call? Did you use 'int_value'? Did you assign the result to 'hex_value'."
        )

        assert hasattr(m,"hex_value"), "Q6: Is 'hex_value' defined?"
        assert getattr(m,"hex_value") == hex(getattr(m,"int_value")), "Q6: 'hex_value' does not store the correct value, did you convert with bin()?"

        ismatch(
            r"print\(\s*hex_value\s*\)",
            "Q6: Did you print out 'hex_value'? Did you use the variable name? Make sure 'hex_value' is not in quotes. Check capitalization and spaces."
        )

    
    @test()
    def t7():
        assert hasattr(m, "int_value"), "Q7: Is 'int_value' defined?"
        assert isinstance(getattr(m,"int_value"),int), "Q7: 'int_value' should reference an integer, but it does not."

        ismatch(
            r"char_value\s*=\s*chr\(\s*int_value\s*\)",
            "Q7: Did you use the chr() function call? Did you use 'int_value'? Did you assign the result to 'char_value'."
        )

        assert hasattr(m,"char_value"), "Q7: Is 'char_value' defined?"
        assert getattr(m,"char_value") == chr(getattr(m,"int_value")), "Q7: 'char_value' does not store the correct value, did you convert with chr()?"

        ismatch(
            r"print\(\s*char_value\s*\)",
            "Q7: Did you print out 'char_value'? Did you use the variable name? Make sure 'char_value' is not in quotes. Check capitalization and spaces."
        )


    @test()
    def t8():
        n = "Q8:"
        for elem in ['first', 'second', 'third']:
            assert hasattr(m,elem), f"{n} '{elem}' is not defined."
            assert isinstance(getattr(m,elem),str), f"{n} '{elem}' should reference a string, but it does not."
        
        ismatch(
            r"print\(\s*first\s*\+\s*[\"'] [\"']\s*\+\s*second\s*\)",
            f"{n} Did you use the variables 'first' and 'second'? Did you concatenate inside the print() call? Did you use the correct operator?"
        )

    @test()
    def t9():
        n = "Q9:"
        for elem in ['first', 'second', 'third']:
            assert hasattr(m,elem), f"{n} '{elem}' is not defined."
            assert isinstance(getattr(m,elem),str), f"{n} '{elem}' should reference a string, but it does not."
        
        ismatch(
            r"print\(\s*third\s*\*\s*10\s*\)",
            f"{n} Did you use the variable 'third'? Did you duplicate inside the print() call? Did you duplicate 10 times? Did you use the correct operator?"
        )

    
    @test()
    def t10():
        n = "Q10:" 
        assert hasattr(m,"text"), f"{n} 'text' is not defined."
        assert isinstance(getattr(m,"text"),str), f"{n} 'text' should reference a string, but it does not."
        
        ismatch(
            r"text\s*\+=\s*[\"']abcde[\"']",
            f"{n} Did you use the correct operator? Did you only use 'text' once when concatenating and assigning? Did you concatenate and assign in the same statement? Check capitalization, spelling, and spaces."
        )

    @test()
    def t11():
        n="Q11:"
        assert hasattr(m,"strang"), f"{n} 'stang' is not defined."
        assert isinstance(getattr(m,"strang"),str), f"{n} 'strang' should reference a string, but it does not."
        ismatch(
            r"strang\s*\*=\s*5",
            f"{n} Did you use the correct operator? Did you only use 'strang' once when concatenating and assigning? Did you concatenate and assign in the same statement? Check capitalization, spelling, and spaces."
        )


    @test()
    def t12():
        n = "Q12:"
        ismatch(
            r"print\(\s*[\"']hello[\"']\s*==\s*[\"']Hello[\"']\s*\)",
            f"{n} Did you use the equality comparision operator? Is \"hello\" on the left and \"Hello\" on the right of the operator? Did you print?"
        )

    @test()
    def t13():
        n = "Q13:"
        for elem in ['alpha', 'beta', 'gamma']:
            assert hasattr(m,elem), f"{n} '{elem}' is not defined."
            assert isinstance(getattr(m,elem),str), f"{n} '{elem}' should reference a string, but it does not."
        
        ismatch(
            r"print\(\s*alpha\s*\!=\s*beta\s*\)",
            f"{n} Did you use the not equal comparision operator? Is 'alpha' on the left and 'beta' on the right of the operator? Did you print?"
        )

    @test()
    def t14():
        n = "Q14:"
        for elem in ['alpha', 'beta', 'gamma']:
            assert hasattr(m,elem), f"{n} '{elem}' is not defined."
            assert isinstance(getattr(m,elem),str), f"{n} '{elem}' should reference a string, but it does not."
        
        ismatch(
            r"print\(\s*beta\s*\>\s*gamma\s*\)",
            f"{n} Did you use the greater than comparision operator? Is 'beta' on the left and 'gamma' on the right of the operator? Did you print?"
        )

    
    @test()
    def t15():
        n = "Q15:"
        for elem in ['alpha', 'beta', 'gamma']:
            assert hasattr(m,elem), f"{n} '{elem}' is not defined."
            assert isinstance(getattr(m,elem),str), f"{n} '{elem}' should reference a string, but it does not."
        
        ismatch(
            r"print\(\s*beta\s*\<\s*gamma\s*\)",
            f"{n} Did you use the less than comparision operator? Is 'beta' on the left and 'gamma' on the right of the operator? Did you print?"
        )   


    @test()
    def t16():
        n="Q16:"
        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*alphabet\[\s*3\s*\]\s*\)",
            f"{n} Did you use subscripting []? Did you use the correct positive index? What number do indexes start with? Did you print?"
        )

    @test()
    def t17():
        n = "Q17:"
        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*alphabet\[\s*\-3\s*\]\s*\)",
            f"{n} Did you use subscripting []? Did you use the negative correct index? What number do indexes start with? Did you print?"
        )  

    @test()
    def t18():
        n = "Q18:"
        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*alphabet\[\s*\:\s*7\s*\]\s*\)",
            f"{n} Did you use subscripting []? Did you use slicing [:]? Did you use the positive correct index? What number do indexes start with? Did you print?"
        ) 

    @test()
    def t19():
        n = "Q19:"
        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*alphabet\[\s*\-8\s*:\s*\]\s*\)",
            f"{n} Did you use subscripting []? Did you use slicing [:]? Did you use the negative correct index? What number do indexes start with? Did you print?"
        ) 

    
    @test()
    def t20():
        n = "Q20:"
        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*alphabet\[\s*11\s*:\s*18\s*\]\s*\)",
            f"{n} Did you use subscripting []? Did you use slicing [:]? Did you use the  correct positive indexes? What number do indexes start with? Did you print?"
        ) 

    @test()
    def t21():
        n = "Q21:"

        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*len\(\s*alphabet\s*\)\s*\)",
            f"{n} Did you use the variable 'alphabet'. Did you use the len() function? Did you print?"
        ) 

    @test()
    def t22():
        n = "Q22:"
        assert hasattr(m,"alphabet"), f"{n} 'alphabet' is not defined."
        assert isinstance(getattr(m,"alphabet"),str), f"{n} 'alphabet' should reference a string, but it does not."
        assert getattr(m,"alphabet") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", f"{n} 'alphabet' should reference \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\""
        ismatch(
            r"print\(\s*len\(\s*alphabet\s*\)\s*-\s*1s*\)",
            f"{n} Did you use the variable 'alphabet'. Did you use the len() function? Did you subtract 1? Did you print?"
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
    alltests.append(t17)
    alltests.append(t18)
    alltests.append(t19)
    alltests.append(t20)
    alltests.append(t21)
    alltests.append(t22)

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
    






    




   
