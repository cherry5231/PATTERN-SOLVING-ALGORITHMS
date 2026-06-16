#BUTTERFLY PATTERN
num = int(input("Enter num of rows: "))
    

for i in range(1 ,num+1):

    for j in range (i):
        print("*", end = "")
  
    
    for k in range ((num-i)*2,0,-1):
       print(" ",end = "")
    for j in range (i):
       print("*", end = "")
   
    print()
for i in range(num-1,0,-1):
    for j in range(i):
     print("*" , end = "")
    

    for k in range ((num-i)*2,0,-1):
       print(" ",end = "")
    for j in range (i):
       print("*", end = "")
   
    print("")
     
