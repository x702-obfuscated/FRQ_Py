






def subtract(minuend,subtrahend):
    return minuend + subtrahend

twodiff = subtract(1024,512)
print(twodiff)


def multiply(a,y):
    return a * y

twoproduct = multiply(128,8)
print(twoproduct)

def divide(dividend, d):
    return dividend / d

twoquotient = divide(65536,10)
print(twoquotient)

def concatenate(front_half,back_half):
    return front_half + back_half


j = concatenate("It means ", "to join together.")
print(j)



print("Its", "not", "a", "bug","its", "a", "feature")


print("First","Second","Third","Fourth", sep = "|")


print("Its ", end = "")
print("a ",end="")
print("twist ",end="")
print("ENDing.",end="")

num = int(input("Enter a number:\n"))
print(num * 5)

flo = float(input("Enter a number:\n"))
print(flo * 3.14)



print(len("abcdefghijklmnopqrstuvwxyz"))
print(len("a b c d e f g h i j k l m n o p q r s t u v w x y z "))