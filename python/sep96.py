#input functions input()
#input optional argument is input request string

#input1 = input("Please say hi")
#print(input1)

#change string input to another type
#use a type conversion func, such as int(), float(), str()

#conditionals
#   if <condition>:
#       <indented code block>
# <non indented statement>

temp = int(input())
if temp > 86:
    print("It is hot")

#elif is else if equivalent

else:
    print("Goodbye.")

#can functions return functions? YES
#functions are objects with a specific type

#map requires one-arg function as first parameter, note it is applied to every item in the sequence passed as second parameters

#list slicing
#M[2]
#M[0:2]
#LIST SLICING ALWAYS RETURNS A LIST, EVEN IF A SINGLE ELEMENT

#pythontutor.com

#recursion
#base case

#factorial(n):
# if n==0: return 1
# else return n*factorial(n-1)
