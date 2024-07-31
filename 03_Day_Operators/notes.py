name_list = list("peter griffin")
peter = input("type 'peter griffin'")

'''
if 'g' in name_list : print("g in name")
elif 'm' in name_list: print("m in name")
else : print("no m or g") 
'''

if list(peter) != name_list : print("incorrect name entered")
else : print("correct")

#'is' keyword compares addresses? -> yes
print(peter is peter)                     #true, because same addr
print(name_list is list("peter griffin")) #false, because diff address but same value

p1 = (2,3)
p2 = (6,10)

slope = ((p2[1] - p1[1]) / (p2[0] - p1[0]))
print(p2[1], "-", p1[1], "/", p2[0], "-", p1[0])
print(slope)


x = 0
y = (x**2) + (6*x) + 9
print(y)

x = -3
y = (x**2) + (6*x) + 9
print(y)

p = "python"
d = "dragon"
print(len(p) == len(d))
if "on" in d and "on" in p : print("yes on.")
else : print("no on.")

print(type(str(float(len("python")))))
print(int(float('9.8'))) #int doesn't round up, only down - truncation

salary = input("Enter salary: ")
hours = input("Enter avg hours worked per week: ")

total_hours_per_year = int(hours) * 52
hourly_rate =  int(salary) / int(total_hours_per_year) 
print("$",round(hourly_rate, 2), "/ hour")


x = 1
print(x, x**0, x**1, x**2, x**3)
x = 2
print(x, x**0, x**1, x**2, x**3)   
x = 3
print(x, x**0, x**1, x**2, x**3)
x = 4
print(x, x**0, x**1, x**2, x**3)
x = 5
print(x, x**0, x**1, x**2, x**3)