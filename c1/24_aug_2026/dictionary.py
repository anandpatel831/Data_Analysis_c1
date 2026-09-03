# a={101:'Aman',105:'Sheat',110:'zomato',120:'uncle lays'}
# print(a)
# print(type(a))
# a[105]

na={}
e=int(input("Give the number of students"))
i=1
while i<=e:
   name=input("Student Name")
   marks=input("marks of students")
   na[name]=marks
   i=i+1
print("Name of student","\t","marks")
for x in na:
       print("\t",x,"\t\t",na[x])