from class_dict import Owner
import json


def get_owner_info():
    with open('Owner_dict.json') as input_file:
        return json.load(input_file)


print(get_owner_info())
print('Owner undo update')
print('-'*20)

owner = Owner(age=28, name="Kate", description='pretty girl')
owner.update_owner(['name', 'sex', 'age', 'description'])
print(get_owner_info())
print('Owner after update')

default_owner = {
    "name": "Max",
    "age": 31,
    "description": "Owner's name is Max and ages is 31"
}
