list1 = [1,2,3,4,5,6,7,8,9]

#with map function
squre = list(map(lambda x : x**2,list1))
print(squre)
#with filter function
even_number = list(filter(lambda x : x%2==0,list1))
print(even_number)

#with sorted method
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
sorted_student = sorted(students,key=lambda x:x[2] )
print(sorted_student)