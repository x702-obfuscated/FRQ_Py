'Comments and Hello World'

' 1 Write a single line comment that includes your full name.'

' 2 Write a multi-line comment with your name, class hour, and graduating class on seperate lines'

' 3 Write a statement that outputs "Hello World!" to the console.'

' 4 Write a statement that only accepts user input.'

' 5 Write a statement that prompts the user to: "Enter Your Name".'

' 6 Write a statement that accepts input from the user and prints it to the console.'

' 7 Write a statement that prompts the user to: "Enter Your Password", then prints the entered password to the console.' 






# DO NOT EDIT PAST THIS POINT ###########################
if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0,str(Path(__file__).parent.parent.parent.parent.parent.resolve()))
    print(sys.path[0])


    from Python_Assignments_with_Autograder.tests import run_test
    run_test.main(Path(__file__).resolve())

#########################################################