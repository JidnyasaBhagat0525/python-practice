# program to check palindrome number

num = int(input("Enter a number: "))
temp = num
rev = o
 while num > 0:
   digit = num % 10
   rev = rev * 10 + digit
   num = num // 10

if temp == rev:
  print("Palindrome Number")
else:
  print("Not a Palindrome Number")
