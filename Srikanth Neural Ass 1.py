# Question 1(a) Reversing a string
input_str = list(input("enter a string:")) #user defined string
if len(input_str)>= 2:
 del input_str[:2] # deleting two characters from the string
 print(input_str)  # printing the output after deletion
 res_str=input_str[::-1] # Reversing the string after deletion
 print("".join(res_str)) # printing the final reversed String
#question 1(b) operations on Two Numbers
num1=int(input("First number"))      # user defined numbers
num2=int(input("Second number"))
sum=num1+num2           #addition of numbers
difference=num1-num2    # subtraction of numbers
product=num1*num2       # Product of two Numbers
quotient=num1/num2      # Divison of two numbers
print(sum)
print(difference)
print(product)
print(quotient)
# Question 2(replacing the sentence)
sentence = ("i love playing with python")
print(sentence)          # printing the sentence which is given
output_sentence= sentence.replace('python','pythons') # Replacing the given "python" with "Pythons"
print(output_sentence)
# Question 3 (Printing the Grades)
cls_score=int(input("Enter the score:"))
if cls_score>=90:   # if class score is greater than or equal to 90 then the grade is A
  grade='A'
elif 80<=cls_score<90:  # if class score is greater than or equal to 80 and  <90 then the grade is B
  grade='B'
elif 70<=cls_score<80: # if class score is greater than or equal to 70 and  <80 then the grade is C
  grade='C'
elif 60<=cls_score<70: # if class score is greater than or equal to 60 and  <70 then the grade is D
  grade='D'
else:
  grade='F'   # if score <60 then grade F means Fail

print(f"The grade is:{grade}") #printing the Grade
                               # "f string " is used to include variable values in the printed output

