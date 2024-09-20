emp={'eno':[1,2,3], 'ename':['A','B','C'], 'esal':[10000,22000,30000]}
print("\n the employee data is:")
print(emp)
print("------------------------------------------")
print("\n the employee Name are :",emp['ename'])
print("---------------------------------------")
print("\n the employee salaries are:")
print("---------------------------------------")
for i in emp['esal']:
    print(i)