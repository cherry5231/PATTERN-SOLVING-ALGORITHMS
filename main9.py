#Mirror Star
num = int(input("Enter num of rows: "))

for i in range(1 ,num+1):
 for k in range (num-i,0,-1):
       print(" ",end = "")
 for j in range (i):
       print("*", end = "")
   
 print("")
     