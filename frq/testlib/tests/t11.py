import sys,re
from pathlib import Path
import importlib.util as imp

import frq.testlib.testlib as tlib

mainpath = Path(sys.argv[1])

spec = imp.spec_from_file_location("main",mainpath)
main = imp.module_from_spec(spec)
spec.loader.exec_module(main)


t = tlib.TestPy(mainpath,main,__import__(__name__))


'Comments and Hello World'
' 1 Write a single line comment that includes your full name.'
@t.test()
def test_Q1():
  assert "#" in t.content, "A single line comment was expect, but not found."

' 2 Write a multi-line commend with your name, class hour, and graduating class on seperate lines'
@t.test()
def test_Q2():
  assert re.search(r"(?:'''|\"\"\")(.*?)(?:'''|\"\"\")",t.content,re.DOTALL), "A multi line comment was expected, but not found."

' 3 Write a statement that outputs "Hello World!" to the console.'
@t.test()
def test_Q3():
  assert re.search(r"print\(\s*[\"']Hello World![\"']\s*\)",t.content), "A print() call was expected, but not found."
  

' 4 Write a statement that only accepts user input.'
@t.test()
def test_Q4():
  assert re.search(r"input\(\s*\)",t.content), "An input() call was expected, but not found."
  

' 5 Write a statement that prompts the user to enter their name.'
@t.test()
def test_Q5():
  assert re.search(r"input\(\s*[\"']Enter\s*Your\s*Name[\"']\s*\)", t.content), 'Expected an input() call with "Enter Your Name", but it was not found.'
 

' 6 Write a statement that accepts input from the user and prints it to the console.'
@t.test()
def test_Q6():
  assert re.search(r"print\(\s*input\(\s*\)\s*\)",t.content), 'Expected print() call containing an input() call, but it was not found.'
  
' 7 Write a statement that prompts the user to: "Enter Your Password", then prints the entered password to the console.'
@t.test() 
def test_Q7():
  assert re.search(r"print\(\s*input\(\s*[\"']Enter\s*Your\s*Password[\"']\)\s*\)",t.content), 'Expected print() call containing an input() call with "Enter Your Password", but it was not founc.'
  






t.runtests()