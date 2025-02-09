from pathlib import Path
import subprocess,os

# import sys,os
# import importlib.util
PACKAGE = Path(__file__).parent
parts = PACKAGE.parts; parts = parts[:parts.index("frq")+1]
ROOT = Path(parts[0]).joinpath(*parts[1:])

mainname = "main"
testname ="t11"
modpath = f"frq.testlib.tests.{testname}"
filepath = PACKAGE/f"{mainname}.py"


if os.name == "posix":
    command = ["python3","-m", modpath, filepath]

elif os.name == "nt":
    command = ["python", "-m", modpath, filepath]

else: 
    raise  OSError

process = subprocess.Popen(
    command, cwd = str(ROOT.parent),
    stdout = subprocess.PIPE,stderr=subprocess.PIPE,
    text=True
)
stdout, stderr = process.communicate()

if stderr:
    print(stderr)

if stdout:
    print(stdout)


# imp = importlib.util
# TESTLIB = ROOT/"testlib"
# path = TESTLIB/"testlib.py"
# spec = imp.spec_from_file_location("testlib",path)
# testlib = imp.module_from_spec(spec)
# spec.loader.exec_module(testlib)

# tpath = TESTLIB/testfile
# tspec = imp.spec_from_file_location("test",tpath)
# tmod = imp.module_from_spec(tspec)
# tspec.loader.exec_module(tmod)

# import main as m

# tmod.run(PACKAGE/"main.py",m)


# try:
#     path = Path(__file__).parts
#     path = path[:path.index("frq")+1]

#     importpath = Path(path[0]).joinpath(*path[1:]) / "testing" / "testing.py"

#     module_name = "testing"

#     spec = importlib.util.spec_from_file_location(module_name, importpath)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)  # Load the module

#     testing = module
# except Exception as e:
#     print(e)
#     sys.exit()

# try:
#     if __name__ == "__main__":
#         import temp as m
#         t = testing.TestPy(Path(__file__).parent / "temp.py", m)
#     else:
#         import main as m
#         t = testing.TestPy(Path(__file__).parent / "main.py", m)

# except ModuleNotFoundError as e:
#     print("Tests cannot be executed because 'main.py' does not exist.")
#     sys.exit()

# testing.clear()

# alltests = []





# def runtests():
#     alltestnames = [attr for attr in globals() if attr.startswith("test_")]

#     this = sys.modules[__name__]

#     for functn in alltestnames:
#         alltests.append(getattr(this,functn))
    
#     for test in alltests:
#         test()

#     t.assess()
#     t.showreport()
# #Tests###########################################################################################################



# 'Comments and Hello World'
# ' 1 Write a single line comment that includes your full name.'
# def test_Q1():
#   t.isin("#", t.content,"A single line comment was expect, but not found." )
# #   assert "#" in t.content, "A single line comment was expect, but not found."

# ' 2 Write a multi-line commend with your name, class hour, and graduating class on seperate lines'
# def test_Q2():
# #   t.ismatch()
# #   assert re.search(r"(?:'''|\"\"\")(.*?)(?:'''|\"\"\")",t.content,re.DOTALL), "A multi line comment was expected, but not found."
#     pass

# ' 3 Write a statement that outputs "Hello World!" to the console.'
# def test_Q3():
#   t.ismatch(r"print\(\s*[\"']Hello World![\"']\s*\)",t.content, "A print() call with the argument 'Hello World!' was expected, but not found.")
# #   assert re.search(r"print\(\s*[\"']Hello World![\"']\s*\)",t.content), "A print() call was expected, but not found."
  

# ' 4 Write a statement that only accepts user input.'
# def test_Q4():
#   t.ismatch(r"input\(\s*\)",t.content,"An input() call was expected, but not found.")
# #   assert re.search(r"input\(\s*\)",t.content), "An input() call was expected, but not found."
  

# ' 5 Write a statement that prompts the user to enter their name.'
# def test_Q5():
#   t.ismatch(r"input\(\s*[\"']Enter\s*Your\s*Name[\"']\s*\)", t.content, 'Expected an input() call with prompt "Enter Your Name", but it was not found. Check spaces and capitalization.')
# #   assert re.search(r"input\(\s*[\"']Enter\s*Your\s*Name[\"']\s*\)", t.content), 'Expected an input() call with "Enter Your Name", but it was not found.'
 

# ' 6 Write a statement that accepts input from the user and prints it to the console.'
# def test_Q6():
#   t.ismatch(r"print\(\s*input\(\s*\)\s*\)",t.content, 'Expected print() call containing an input() call, but it was not found.')
# #   assert re.search(r"print\(\s*input\(\s*\)\s*\)",t.content), 'Expected print() call containing an input() call, but it was not found.'
  
# ' 7 Write a statement that prompts the user to: "Enter Your Password", then prints the entered password to the console.' 
# def test_Q7():
#   t.ismatch(r"print\(\s*input\(\s*[\"']Enter\s*Your\s*Password[\"']\)\s*\)",t.content, 'Expected print() call containing an input() call with "Enter Your Password", but it was not found.')
# #   assert re.search(r"print\(\s*input\(\s*[\"']Enter\s*Your\s*Password[\"']\)\s*\)",t.content), 'Expected print() call containing an input() call with "Enter Your Password", but it was not founc.'
  


# # @t.parameterize(
# #     ("x",5),
# #     ("y",6),
# #     ("z",10),
# #     ("add",4,2,2)
# # )
# # def q1(attr,exp,*args):
# #     t.isequal(attr,exp,*args) 

# # def q2():
# #     t.ismatch("def",feedback = "Expected to find function definition, but was not found. Did you define your function?")

# # def q3():
# #     t.isin("print()")





# #Tests###########################################################################################################
# if __name__ == "__main__":
#     print(t.content)
#     input()
#     runtests()


























