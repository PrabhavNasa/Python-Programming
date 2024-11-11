print('Creating and Modifying:'.upper())
dic = {'name': 'NASA', 'age': 21}
dic['age'] = 22
dic['city'] = 'New Delhi'
print(dic)

print('\nAccessing and Removing Elements:'.upper())
print('Name:',dic.get('name'))
dic.pop('name')
print(dic)

print('\nIterating Through Dictionary Items:'.upper())
for key, value in dic.items():
    print(f"{key}: {value}")

print("\nThis program is written by Prabhav. \nERPID: 0221BCA011")
