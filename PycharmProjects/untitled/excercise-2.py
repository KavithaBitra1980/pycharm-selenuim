# working with if/Else excercise from Linux academy

user = {'admin': True, 'active': False, 'name': "kavitha"}

if user['admin'] and user['active']:
    print("ACTIVE ADMIN is %s" %user['name'])
elif user['admin'] :
    print("The admin is %s" %user['name'])
elif user['active'] :
    print("the active admin is %s" %user['name'])
else:
    print(user['name'])

