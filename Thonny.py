car=['model','type','colour']
for i in car:
    print(i)
    
user= {'Name':'Gladys','Age':35,'nationality': 'Kenya'}
print(user.get('Name'))
print(user.values())
print(user.keys())
print(user.items())
print(user.copy())
user['age']=30
print(user.items())
user['sex']='Female'
print(user.copy())
user.update({'sex':'female'})


