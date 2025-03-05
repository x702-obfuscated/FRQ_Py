identity='58c820bb547500d7fdb527402545b4dea00049711265f3e68a76ae207c64311f8892677124a8af8faf96e3543d4cc2a580b2df0004797f80f89a6411e4eb4cf7'
import subprocess,os,sys,hashlib
from datetime import datetime
from getpass import getuser
from pathlib import Path
import re

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
    
    # @test()
    # def tq1():
    #     # [1.]    Write a single line comment that includes your full name.
    #     assert "#" in filecontent, "A single line comment was expect, but not found. Did you use the right symbol?"

    # @test()
    # def tq2():
    #     # [2.]    Write a multi-line comment with your name, class hour, and graduating class on seperate lines.
    #     assert re.search(r"(?:'''|\"\"\")(.*?)(?:'''|\"\"\")",filecontent,re.DOTALL), "A multi line comment was expected, but not found. Did you use the correct symbol?"

    # @test()
    # def tq3():
    #     # [3.]    Write a Python code statement that outputs "Hello World!" to the console. 
    #     #         The output text must match the exact text in quotes. 
    #     assert re.search(r"print\(\s*[\"']Hello World![\"']\s*\)",filecontent), \
    #         "A print() call containing 'Hello World!' was expected, but not found. Does your text match the exact text in quotes?"
    
    # @test()
    # def tq4():
    #     # [4.]    Write a Python code statement that ONLY accepts user input.
    #     assert re.search(r"(?<=\n)input\(\s*\)",filecontent), "An input() call was expected, but not found. Did you call input() with nothing in the parenthesis?"
    

    # @test()
    # def tq5():
    #     # [5.]    Write a Python code statement that prompts the user with "Enter Your Name". 
    #     #         The prompt must match the exact text in quotes. 
    #     assert re.search(r"input\(\s*[\"']Enter\s*Your\s*Name[\"']\s*\)", filecontent), 'Expected an input() call with "Enter Your Name", but it was not found. Did you call input()? Does the text match exactly?'
    
    # @test()
    # def tq6():
    #     # [6.]    Write a Python code statement that accepts input from the user and prints it to the console in the same statement.
    #     assert re.search(r"print\(\s*input\(\s*\)\s*\)",filecontent), 'Expected print() call containing an input() call, but it was not found.'
    
    # @test()
    # def tq7():
    #     # [7.]    Write a Python code statement that prompts the user with "Enter Your Password", then prints the password they entered to the console.
    #     #         The prompt must match the exact text in quotes. 
    #     assert re.search(r"print\(\s*input\(\s*[\"']Enter\s*Your\s*Password[\"']\)\s*\)",filecontent), \
    #         'Expected print() call containing an input() call with "Enter Your Password", but it was not found. Did you call print()? input()? Does the text match exactly?'

    # @test()
    # def tq8():
    #     # [8.]    Write a Python code statement that prints out "Username: ". Then on the next line write a code statement to accept user input and print it to the console. 
    #     # The printed text must match the exact text in quotes. 
    #     assert re.search(r"print\(\s*[\"']Username:\s[\"']\s*\)\s*print\(\s*input\(\s*\)\s*\)",filecontent,re.DOTALL), \
    #         "Expected a print() call containing 'Username: '. Expected a print() call containing input() on the next line. Did you call print()? input()? Does the text match exactly?" 

    # @test()
    # def tq9():
    #     # [9.]    Write a Python code statement that prompts the user with "First Name: " and prints out their input in the same statement. 
    #     # On the next line write a code statement the prompts the user with "Last Name: " and prints out their input input in the same statement.
    #     # On the next line write a code statement the prompts the user with "Date of Birth: " and prints out their input input in the same statement.
    #     # The prompt text must match the exact text in quotes.
    #     assert re.search(r"print\(\s*[\"']First Name:\s[\"']\s*\)\s*print\(\s*input\(\s*\)\s*\)",filecontent,re.DOTALL), "Expected a print() call containing 'First Name: '. Expected a print() call containing input() on the next line. Did you call print()? input()? Does the text match exactly?"
    #     assert re.search(r"print\(\s*[\"']Last Name:\s[\"']\s*\)\s*print\(\s*input\(\s*\)\s*\)",filecontent,re.DOTALL),"Expected a print() call containing 'Last Name: '. Expected a print() call containing input() on the next line. Did you call print()? input()? Does the text match exactly?"
    #     assert re.search(r"print\(\s*[\"']Date of Birth:\s[\"']\s*\)\s*print\(\s*input\(\s*\)\s*\)",filecontent,re.DOTALL),"Expected a print() call containing 'Date of Birth: '. Expected a print() call containing input() on the next line. Did you call print()? input()? Does the text match exactly?"
        
    # @test()
    # def tq10():
    #     # [10.]   Write a Python code statement that prints out " 0 1 a B ! ".
    #     # The printed text must match the exact text in quotes.
    #     assert re.search(r"[\"']\s0\s1\sa\sB\s!\s[\"']", filecontent),"Expected a print() call containing \" 0 1 a B ! \". Did you call print? Does the text match exactly? Remember that spaces are characters."
    
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

    # @test("a","b","c")
    # def tq1(a):
    #     assert 1 == 1, "One does not equal"
    # alltests.append(tq1)

    # @test()
    # def tq2():
    #     assert 1 == 1, "1 does not equal a"
    # alltests.append(tq2)

    # @test()
    # def tq3():
    #     assert "input()" in filecontent, "Expected input(), but found none."
    # alltests.append(tq3)

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
    






    




   
