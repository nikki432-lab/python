num = int(input("Enter the number for the multiplication table: "))
 
print(f"\n multiplication table for {num}:")
for i in range (1,11):
 print(f"{num}*{i} = {num*i}")
