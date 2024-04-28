import pyfiglet
from colorama import init, Fore, Style
import time
import sys

# ------------------------- Banner --------------------------------
init()
art = pyfiglet.figlet_format("Password Analyser", font='mono9')
print(Fore.YELLOW + art)
print(Style.RESET_ALL)  # Reset color to default
time.sleep(2)

msg = "Loading..."
for i in msg:
	print(Fore.BLUE + i,end="")
	time.sleep(0.1)	
print(Style.RESET_ALL)
time.sleep(1)

#============================== Main Code =============================

alphabets= "abcdefghijklmnopqrstuvwxyz"
numbers= "0123456789"
symbols="~`! @#$%^&*()_-+={[}]|\\:;\"\'<,>.?/"
strength_flag=""
weakness_points=0
reverse_flag= "aAns"



password = sys.argv[1]
for i in alphabets:
    if i in password:
        strength_flag=strength_flag + "a"
        break
for i in alphabets.upper():
    if i in password:
        strength_flag=strength_flag + "A"
        break    
for i in numbers:
    if i in password:
        strength_flag=strength_flag + "n"
        break

for i in symbols:
    if i in password:
        strength_flag=strength_flag + "s"
        break  

#-------------------- Checking the password strength ------------------------
for i in strength_flag:
    if i == "a":
        msg = "Lower alphabet........found"
        for m in msg:
            time.sleep(0.1)
            print(m,end="")
        print()

    elif i == "A":
        msg = "Upper alphabet........found"
        for m in msg:
            time.sleep(0.1)
            print(m,end="")

        print()

    elif i == "n":
        msg = "Number................found"
        for m in msg:
            time.sleep(0.1)
            print(m,end="")
        print()
        
            
    elif i == "s":
        msg = "Symbol................found"
        for m in msg:
            time.sleep(0.1)
            print(m,end="")
        print()
        
    #creating reverse flag ------------------
    for i in strength_flag:
        reverse_flag.replace(i,"")
    
else:
        #creating reverse flag ------------------
        for i in strength_flag:
            reverse_flag = reverse_flag.replace(i,"")
    
        if "a" in reverse_flag:
            msg = "Lower alphabets........Not found"
            for m in msg:
                for j in range(50):
                    print("",end="")
                print(m,end="")
            print()
            reverse_flag = reverse_flag.replace("a","")
            weakness_points=weakness_points + 1

        if "A" in reverse_flag:
            msg = "Upper alphabets........Not found"
            for m in msg:
                for j in range(50):
                    print("",end="")
                print(m,end="")
            print()
            weakness_points=weakness_points + 1
            reverse_flag = reverse_flag.replace("A","")
            
        if "n" in reverse_flag:
            msg = "Numbers................Not found"
            for m in msg:
                for j in range(50):
                    print("",end="")
                print(m,end="")
            print()
            weakness_points=weakness_points + 1
            reverse_flag.replace("n","")
            
                
        if "s" in reverse_flag:
            msg = "Symbols................Not found"
            for m in msg:
                for j in range(50):
                    print("",end="")
                print(m,end="")
            print()
            weakness_points=weakness_points + 1
            reverse_flag = reverse_flag.replace("s","")
            

#----------------------- Overall Evaluation -----------------------
"""
Excellent        length = 12+ flags = 4
Good		 length = 8-12  flags = 4 
Weak		 any one flag missing  
Very weak	 more than one flag missing
"""
length = len(password)

if length > 12 and weakness_points == 0:
    print("Password strength: Excellent")
elif length <= 12 and length >= 8  and weakness_points == 0:
    print("Password strength: Good")
elif weakness_points == 1:
    print("Password strength: Weak")
elif weakness_points >= 1:
    print("Password strength: Very weak")


#========================================================================

print(Fore.CYAN + "Done!")
print(Style.RESET_ALL)
