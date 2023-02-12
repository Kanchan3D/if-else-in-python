sub1=int(input("enter marks in 1st sub"))
sub2=int(input("enter marks in 2nd sub"))
sub3=int(input("enter marks in 3rd sub"))
sub4=int(input("enter marks in 4th sub"))
sub5=int(input("enter marks in 5th sub"))
avg = (sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("grade A")
elif(avg>=80&avg<90):
    print("grade B")
elif(avg>=70&avg<80):
    print("grade C")
elif(avg>=60&avg<50):
    print("grade D")
