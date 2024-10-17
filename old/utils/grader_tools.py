import sys 
import os
import subprocess
import io

def check_module_output(path, expected_output): #strip
  #note calls main.py causing a recursion... #strip
  if os.name == 'posix':#strip
    result = subprocess.run(["python3", path], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True) #strip
  elif os.name == 'nt':#strip
    result = subprocess.run(["python", path], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True) #strip

  assert str(expected_output).strip() in result.stdout.strip(), f"Expected {expected_output}, but got {result.stdout}" #strip


def get_module_output(path, expected_output): #strip
  #note calls main.py causing a recursion... #strip
  if os.name == 'posix':#strip
    result = subprocess.run(["python3", path], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True) #strip
  elif os.name == 'nt':#strip
    result = subprocess.run(["python", path], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True) #strip

  return result.stdout


def check_function_output(module, func, expected_output,*args): #strip
  assert hasattr(module,func.__name__), f"'{func}' function definition not found" #strip

  captured_output = io.StringIO() #strip
  sys.stdout = captured_output #strip

  func(*args) #strip
  sys.stdout = sys.__stdout__ #strip

  arg_str = "" #strip
  for i,arg in enumerate(args): #strip
    if i == len(args)-1:#strip
      arg_str += f"{arg}" #strip
    else:#strip
      arg_str += f"{arg},"#strip
  
  assert captured_output.getvalue().strip() == str(expected_output).strip(), f"{func.__name__}({arg_str}) was called.\nThe test expected a result of '{expected_output}', but got '{captured_output.getvalue()}' instead."#strip


def get_function_output(module, func, *args): #strip
  assert hasattr(module,func.__name__), f"'{func}' function definition not found" #strip

  captured_output = io.StringIO() #strip
  sys.stdout = captured_output #strip

  func(*args) #strip
  sys.stdout = sys.__stdout__ #strip

  arg_str = "" #strip
  for i,arg in enumerate(args): #strip
    if i == len(args)-1:#strip
      arg_str += f"{arg}" #strip
    else:#strip
      arg_str += f"{arg},"#strip
  
  return captured_output


def check_equal(module, func, expected_output, *args): #strip
  assert hasattr(module, func.__name__), f'"{func.__name__}" function definition could not be found.' #strip

  arg_str = "" #strip
  for i,arg in enumerate(args): #strip
    if i == len(args)-1:#strip
      arg_str += f"{arg}" #strip
    else:#strip
      arg_str += f"{arg},"#strip

  assert func(*args) == expected_output, f"{func.__name__}({arg_str}) was called. The test expected a result of {expected_output}, but got {func(*args)} instead."#strip

  #Examples++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  

  # @pytest.mark.parametrize("n1,n2,a",[(2,2,4),(4,3,7),(5,3,8),]) #strip
  # def test_Q1(self, n1, n2, a):
  #   assert hasattr(module, "add"), f'"add()b" function definition could not be found.' #strip
  #   Tests.check_equal(module.add, a, n1, n2) #strip

  # def test_Q2(self):
  #   assert hasattr(module, "say_hello"), f'"say_hello()" function definition could not be found.' #strip
  #   Tests.check_function_output(module.say_hello,"Hello World")
    

  # def test_with_input(self,monkeypatch):
  #   module.input = lambda _ : "test in"
  #   Tests.check_module_output("test in")



  # def test_Q3(self):
  #   ...

  # def test_Q4(self):
  #   ...

  # def test_Q5(self):
  #   ...

  # def test_Q6(self):
  #   ...

  # def test_Q7(self):
  #   ...

  # def test_Q8(self):
  #   ...

  # def test_Q9(self):
  #   ...

  # def test_Q10(self):
  #   ...

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

