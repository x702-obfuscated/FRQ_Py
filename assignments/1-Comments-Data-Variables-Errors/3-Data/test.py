identity='508eff0788a14ca27ce90cdb0ecb0875fb020dca85ad8243fba5d22568e050fc13ea134b2baea85b8bc2ba6ad04b2101fd2f9bcb0770f350c9bb780d8b298b5f'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

assignment = "3-Data"
path = Path(__file__).parent
thispath = Path(__file__)
filepath = "main.py"
filecontent = ""
numpassed = 0
numfailed = 0
num = 0
report = []
alltests = []

def maketests():
    global filecontent

    @test()
    def tq1():
        # [1.]    Write a Python code statement that represents nothing or having no value.
        assert re.search(r"(?<![\"'])None",filecontent), "Expected a null value, but was not found. What data type represents 'Nothing' or 'Null'."

    @test()
    def tq2():
        # [2.]    Write a Python code statement for the 2 possible boolean data values.
        assert re.search(r"(?<![\"'])True",filecontent), "Expected a true value, but was not found. How do you represent true in Python?"
        assert re.search(r"(?<![\"'])False",filecontent), "Expected a false value, but was not found. How do you represent false in Python?"
    

    @test()
    def tq3():
        # [3.]    Write a Python code statement that represents the number --> 100 
        assert re.search(r"(?<![\"'])100",filecontent), "Expected an integer value of 100, but was not found. How do you represent an integer in Python?"
  
    @test()
    def tq4():
        # [4.]    Write a Python code statement that represents the number --> 3.14159  
        assert re.search(r"(?<![\"'])3.14159",filecontent), "Expected a float value of 3.14159, but was not found. How do you represent a float in Python?"

    @test()
    def tq5():
    #    [5.]    Write a Python code statement that represents the character --> a
        assert re.search(r"[\"']a[\"']",filecontent), "Expected the character a, but was not found. How do you represent a character in Python?"

    @test()
    def tq6():
    #   [6.]    Write a Python code statement that represents the text --> The quick brown fox jumps over the lazy dog. 
        assert re.search(r"[\"']The quick brown fox jumps over the lazy dog.[\"']",filecontent), "Expected the string --> The quick brown fox jumps over the lazy dog. , but was not found. How do you represent a string in Python?"


    @test()
    def tq7():
    #    [7.]    Write a Python code statement that represents the text --> 01234567890
        assert re.search(r"[\"']01234567890[\"']", filecontent), "Expected the string --> 0123456789 , but was not found. How do you represent a string in Python?" 

    @test()
    def tq8():
    #    [8.]    Write a Python code statement that represents a list of the following characters --> a b c
        assert re.search(r"\[\s*[\"']a[\"']\s*,\s*[\"']b[\"']\s*,\s*[\"']c[\"']\s*\]", filecontent), "Expected a list of characters --> a b c , but was not found. How do you represent a character in Python? How do you represent a list in Python?" 

    @test()
    def tq9():
    #    [9.]    Write a Python code statement that represents a list of the following characters --> 1 2 3
        assert re.search(r"\[\s*[\"']1[\"']\s*,\s*[\"']2[\"']\s*,\s*[\"']3[\"']\s*\]", filecontent), "Expected a list of characters --> 1 2 3 , but was not found. How do you represent a character in Python? How do you represent a list in Python?" 

    @test()
    def tq10():
    #    [10.]   Write a Python code statement that represents a list of the following numbers --> 4 5 6
        assert re.search(r"\[\s*4\s*,\s*5\s*,\s*6\s*\]", filecontent), "Expected a list of integers --> 4 5,6 but was not found. How do you represent an integer in Python? How do you represent a list in Python?" 

    @test()
    def tq11():
    #    [11.]   Write a Python code statement that prints out the type of the following data --> "3.14"
        assert re.search(r"print\s*\(\s*type\s*\(\s*[\"']3.14[\"']\s*\)\s*\)", filecontent), "Expected print() call containing a type() call with an argument of \"3.14\" , but was not found.  What do quotes mean in Python?"


    @test()
    def tq12():
    #    [12.]   Write a Python code statement that prints out the type of the following data --> 101
        assert re.search(r"print\s*\(\s*type\s*\(\s*101\s*\)\s*\)", filecontent), "Expected print() call containing a type() call with an argument of 101 , but was not found."



    alltests.append(tq1)
    alltests.append(tq2)
    alltests.append(tq3)
    alltests.append(tq4)
    alltests.append(tq5)
    alltests.append(tq6)
    alltests.append(tq7)
    alltests.append(tq8)
    alltests.append(tq9)
    alltests.append(tq10)
    alltests.append(tq11)
    alltests.append(tq12)

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
    maketests()

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
    






    




   
