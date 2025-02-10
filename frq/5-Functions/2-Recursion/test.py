from pathlib import Path
import subprocess,os,sys

testname ="t52"
mainname = "main"

PACKAGE = Path(__file__).parent
parts = PACKAGE.parts; parts = parts[:parts.index("frq")+1]
ROOT = Path(parts[0]).joinpath(*parts[1:])

modpath = f"frq.testlib.tests.{testname}"
filepath = PACKAGE/f"{mainname}.py"


def noerrors():

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
        print("Look for 'line' in the text above, and the 'Error' on the last line.")
        print("Read the traceback and figure out what is wrong.".upper())
               
        sys.exit()
    

def run():
    if os.name == "posix":
        command = ["python3","-m", modpath, filepath]

    elif os.name == "nt":
        command = ["python", "-m", modpath, filepath]

    else: 
        raise OSError

    process = subprocess.Popen(
        command, cwd = str(ROOT.parent),
        stdout = subprocess.PIPE,stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if stderr:
        print(stderr.decode("utf-8"))
        

    if stdout:
        print(stdout.decode("utf-8"))

noerrors()
run()



























