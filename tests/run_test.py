import os,sys
import re
import subprocess
from datetime import datetime 
from pathlib import Path

from ..utils.config import *
from ..utils.file_tools import *
 


def main_executes(file_path):
    try:

      if os.name == 'posix':
        command = ["python3",file_path]

      elif os.name == 'nt':
        command = ["python",file_path]
      
 
      process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE,stdin = subprocess.DEVNULL, text = True)
      stdout,stderr = process.communicate()

      if(stderr):
        print(f"Before the test could run your code resulted in an error:".upper())
        print("Look for 'line' in the text below, and the 'Error' on the last line.\n")
        print(stderr)
        remove_inputchange(file_path)
        exit()

      if(stdout):
        print(stdout)
      
    except Exception as e:
      print(f"An Error Occured: {e}")
      remove_inputchange(file_path)
      exit()

def get_testpath(src_path):
    test_path = list(src_path.parts)
    test_path[-1]="test.py"
    test_path[-4] = "tests"
    test_path = Path(*test_path)

    return(test_path)

def get_reportpath(test_path):
   report_path = list(test_path.parts)
   report_path[-1] = "report.log"
   report_path = Path(*report_path)

   return report_path

def run_pytests(src_path):
  test_path = get_testpath(src_path)
  report_path = get_reportpath(test_path)

  if(os.name == 'posix'):
    switch = False
  else:
    switch = True

  command = ["pytest", "-vv", test_path, src_path]
 
  print(f"Checking Answers... ", end = "")
  try:
    process = subprocess.Popen(command, shell = switch, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
    stdout,stderr = process.communicate()
  except Exception as e:
    print(f"An error occured while running pytest:\n{e}")

  try:
    with open(report_path,"w") as file:
      file.write(stdout)

  except Exception as e:
    print(f"An error occured writing results:\n{e}")





















def main(path):  
    get_testpath(path)
    # check_hashes()
    # change_inputfunction(path)
    # main_executes(path)
    # decode_test()
    # run_pytests()
    # del_test()
    # remove_inputchange(path)
    # rewrite_results(get_name())





if __name__ == "__main__":
    if(len(sys.argv)>1):
        if("encode" in sys.argv):
            encode_test()

        if("set_hash" in sys.argv):
            hashes = hash_files()
            for file in hashes.keys():
                print(f"{file} : {hashes[file]}")
