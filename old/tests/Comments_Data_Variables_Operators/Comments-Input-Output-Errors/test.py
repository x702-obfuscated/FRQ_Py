'''Write your tests in this file'''
import pytest
import re


from ....utils.grader_tools import * 
from ....utils.file_tools import *

try:
    from ....assignments.A_Comments_Data_Variables_Operators.A_Intro_Comments_and_HelloWorld import assignment
    module = assignment

except Exception as e:
    print(f"An error occured while loading module:\n{e}")



'Comments and Hello World'
' 1 Write a single line comment that includes your full name.'
def test_Q1():
  assert "#" in file_content, "A single line comment was expect, but not found."

' 2 Write a multi-line commend with your name, class hour, and graduating class on seperate lines'
def test_Q2():
  assert re.search(r"(?:'''|\"\"\")(.*?)(?:'''|\"\"\")",file_content,re.DOTALL), "A multi line comment was expected, but not found."

' 3 Write a statement that outputs "Hello World!" to the console.'
def test_Q3():
  assert re.search(r"print\(\s*[\"']Hello World![\"']\s*\)",file_content), "A print() call was expected, but not found."
  

' 4 Write a statement that only accepts user input.'
def test_Q4():
  assert re.search(r"input\(\s*\)",file_content), "An input() call was expected, but not found."
  

' 5 Write a statement that prompts the user to enter their name.'
def test_Q5():
  assert re.search(r"input\(\s*[\"']Enter\s*Your\s*Name[\"']\s*\)", file_content), 'Expected an input() call with "Enter Your Name", but it was not found.'
 

' 6 Write a statement that accepts input from the user and prints it to the console.'
def test_Q6():
  assert re.search(r"print\(\s*input\(\s*\)\s*\)",file_content), 'Expected print() call containing an input() call, but it was not found.'
  
' 7 Write a statement that prompts the user to: "Enter Your Password", then prints the entered password to the console.' 
def test_Q7():
  assert re.search(r"print\(\s*input\(\s*[\"']Enter\s*Your\s*Password[\"']\)\s*\)",file_content), 'Expected print() call containing an input() call with "Enter Your Password", but it was not founc.'
  
