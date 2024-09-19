
# import os
# import subprocess
# from pathlib import Path
# import hashlib
# from datetime import datetime
# import base64
# import json

# #installed libraries
# from colorama import Fore, Style


# file_name = "main.py"
# test_name = "test_main.py"
# result_name = "results.txt"
# cipher_name = "cipher.txt"
# grader_name = "grader.py"
# runner_name = "run_test.py"
# hash_name = "hashes.json"
# log_name = "log.txt"

# quiz_name = "quiz.py"
# mcq_name = "mcq.py"


# runner_hash = ""
# cipher_hash = ""
# grader_hash = ""

# quiz_hash = ""
# mcq_hash = ""



# try:
#   #Gets necessary filepaths
#   project_dir = Path.cwd()
#   util_dir= project_dir / "utils"
#   log_dir = project_dir / "logs"


#   src_path = project_dir / file_name
#   runner_path = project_dir / runner_name
#   test_path = project_dir / test_name
#   result_path = log_dir / result_name
#   cipher_path = log_dir / cipher_name
#   grader_path = util_dir/ grader_name

#   quiz_path = project_dir / quiz_name
#   mcq_path = util_dir / mcq_name
#   log_path = log_dir / log_name

#   hash_path = log_dir / hash_name

#   paths = []
#   paths.append(runner_path)
#   paths.append(cipher_path)
#   paths.append(grader_path)
#   paths.append(quiz_path)
#   paths.append(mcq_path)

  

#   with open(src_path, "r") as file:
#     file_content= file.read()
#     file_lines = file.readlines()

#   if not result_path.exists():
#     with open(result_path,"w") as file:
#       file.write("")

# except FileNotFoundError as e:
#   print(f"Not Found {e}")
#   exit()

# except Exception as e:
#   print(f"An error occured: {e}")
#   exit()

# def change_inputfunction(path,inp = "'TEST INPUT'"):
#   global src_path, file_content, file_lines

#   if("input(" in file_content):
#     try:
#       with open(path, "r+") as file:
#         lines = file.readlines()
#         if(not lines[0] or "input = lambda _ = None :" in lines[0]):
#           lines[0] = f"input = lambda _ = None : {inp} \n"
#         else:
#           lines.insert(0,f"input = lambda _ = None : {inp} \n")
        
#         file.seek(0)
#         file.truncate()
#         file.writelines(lines)
#         file_content = file.read()
#         file_lines = file.readlines()

#     except Exception as e:
#       print(f"An error occured while making input changes: {e}")
#       exit()

#   else:
#     return

# def remove_inputchange(path):
#   try:
#     with open(path, "r+") as file:
#       lines = file.readlines()
#       if("input = lambda _ = None :" in lines[0]):
#         lines.pop(0)

#         file.seek(0)
#         file.truncate()
#         file.writelines(lines)
#         file_content = file.read()
#         file_lines = file.readlines()
#   except Exception as e:
#     print(f"An error occured while removing input changes: {e}")
#     exit()

# def hash_files():
#   hash_dict = {}
#   for path in paths:
#     # For Unix/Linux
#     if os.name == 'posix':
#       file = str(path).split("/")[-1]
#     # For Windows
#     elif os.name == 'nt':
#       file = str(path).split("\\")[-1]
    
#     hash_dict[file] = get_file_hash(path)

#     try:
#       with open(hash_path, "w") as file:
#         json.dump(hash_dict,file)
#     except Exception as e:
#       print(f"An error occured while writing hashes: {e}")

#   return hash_dict
    
# def get_file_hash(path, algorithm = "sha256"):
#   hasher = hashlib.new(algorithm)
#   with open(path, "rb") as file:
#     while chunk := file.read(4096):
#       hasher.update(chunk)
#   return hasher.hexdigest()

# def check_hashes():
#   try:
#     with open(hash_path,"r") as file:
#       hashes = json.load(file)

#     for path in paths:
#       if os.name == 'posix':
#         file = str(path).split("/")[-1]
#       # For Windows
#       elif os.name == 'nt':
#         file = str(path).split("\\")[-1]
      
#       if(hashes[file] != get_file_hash(path)):
#         try: 
#           with open(log_path,"a") as file:
#             file.write(f"{datetime.now()}\nA file was altered: {path}\n\n")
#         except Exception as e:
#           print(f"An error occured while logging: {e}")
#         print(f"A file has been altered and must be fixed before you may continue.\n{path}")
#         exit()
#   except FileNotFoundError as e:
#     print(f"An Error Occured: {e}\nHash File has been deleted and must be fixed before you can continue.")

#   except Exception as e:
#     print(f"An error has occured while reading hashes: {e}")

# def rewrite_results(student_name):
#   lines_to_remove = ("#strip","grader.py","platform", "cachedir", "rootdir","collecting ... ", "where ", "self = <","def ","assert ", " = ","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

#   skipline_counter = 0


#   try:
#     with open(result_path, "r+") as f:
#       lines = f.readlines() #reads the whole file
#       f.seek(0,0) #resets file pointer to beginning

#       #Write student information
#       f.write(f"Name: {student_name}\n")
#       f.write(f"Date/Time: {datetime.now():%Y-%m-%d (%H:%M:%S)}\n")
#       f.write(f"File Path: {src_path}\n\n")


#       for line in lines:
#         write = True

#         #skip lines
#         if skipline_counter != 0:
#           skipline_counter -= 1
#           continue

#         for text in lines_to_remove:
#           if text in line or line == "\n" or line == "    \n":
#             write = False
         
#         if(write):
#           newline = line

#           #Line Replacement
#           if "test_main.py::Tests::" in newline:
#             newline = newline[21:]

#           if "test_main.py::" in newline:
#             newline = newline.replace("test_main.py::","")
           
#           elif "test_main.py:" in newline:
#             newline = ""
#             continue
            
#           if "Tests::" in newline:
#             newline = newline.replace("Tests::","")

#           # if("grader.py:" in newline):
#           #   newline = ""

#           if "Captured stdout call" in newline:
#             newline = f"      {Fore.RED}Expected function to return, not to print out: {Style.RESET_ALL}"

#           if "FAILED" in newline:
#             newline = newline.replace("FAILED", "INCORRECT")

#           if "AssertionError:" in newline:
#             newline = newline.replace("AssertionError:","ResultError:")
#             newline = Fore.RED + newline + Style.RESET_ALL

#           if "FAILURES" in newline:
#             newline = newline.replace("FAILURES", "INCORRECT QUESTIONS")
#             newline = "\n" + Style.BRIGHT +  newline + Style.RESET_ALL

#           # if(after_missed_questions_line):
#           #   i = newline.find(" - ")
#           #   newline = newline[0:i] + "\n"
#           #   #needs to occur on the next loop after the missed question line is taken care of..

#           if " short test summary info " in newline:
#             newline = newline.replace(" short test summary info ", " MISSED QUESTIONS ")
#             newline = "\n" + Style.BRIGHT +  newline + Style.RESET_ALL
#             # after_missed_questions_line = True

#           # if "test_main.py:" in newline:
#           #   newline = ""
#           #   continue

#           if ("PASSED" in newline or "INCORRECT" in newline) and "%]" in newline:
#             newline = newline[0:newline.index("%]")-4] + "\n"

#           if(">       raise OSError(" in newline):
#             skip = 2
#             continue

#           if ("pytest: reading from stdin while output is captured!  Consider using `-s`." in newline):
#             skip = 2
#             newline = newline.replace("pytest: reading from stdin while output is captured!  Consider using `-s`.",
#             "Detected the use of the input() function. Please remove the input() function from your code.")
          

#           if("TypeError:" in newline and  "takes" in newline and  "positional" in newline and "were given" in newline) or ("missing" in newline and "required" in newline and "positional " in newline):
#             newline = "E     ParameterError: You are not using the correct number of parameters.\n"

#           if("UnboundLocalError:" in newline):
#             newline = newline.replace("UnboundLocalError:", "VariableError:")
#             newline = newline.replace("referenced before assignment", "is used before assigning it a value.")


#           if("RecursionError:" in newline):
#             newline = newline.replace("maximum recursion depth exceeded", "The function was called inside of its own definition.")

#           if("NameError:" in newline):
#             newline = newline.replace("NameError:","VariableError:")
#             newline = newline.replace("name","variable")
#             newline = newline.replace("is not defined", "has not been assigned a value")

#           if("main.py:" in newline and ": in " in newline):
#             continue

#           #Line Coloring++++++++++++++++++++++++++++++++++++++++++++++++++++#
#           if " PASSED " in newline:
#             newline = Fore.GREEN + newline + Style.RESET_ALL

#           if "INCORRECT " in newline:
#             newline = Fore.RED + newline + Style.RESET_ALL

#           if "Tests.test_" in newline or " passed in " in newline :
#             newline = "\n" + Fore.YELLOW +  newline + Style.RESET_ALL

#           if "E " in newline or "Error: " in newline:
#             newline = Fore.RED +  newline + Style.RESET_ALL


#           f.write(newline)
#           #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
#       f.truncate() #cut the rest of the file off
    

   
#     # For Unix/Linux
#     if os.name == 'posix':
#      result = subprocess.run(["cat", f"{result_path}"], stdout=subprocess.PIPE, text=True)
#     # For Windows
#     elif os.name == 'nt':
#       result = subprocess.run(f"type {result_path}", stdout=subprocess.PIPE, shell=True, text=True)
#     print(result.stdout)
#     print(f"Finished")
          
#   except Exception as e:
#     print(f"An Error Occured: {e}")

# def decode_test():
#   with open(cipher_path, "rb") as file:
#     cipher_text = file.read()
  

#   with open(test_path, "wb") as file:
#     file.write(base64.b64decode(cipher_text))

# def encode_test():
#   with open(test_path,"rb") as file:
#     content = file.read()
  
#   with open(cipher_path,"wb") as file:
#     file.write(base64.b64encode(content))

# def del_test():
#    os.remove(test_path)



  











    
