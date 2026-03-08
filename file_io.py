


import json
with open('mac.txt', 'w') as f:
    name = 'Abbos'
    surname = 'Zoirov'
    age = 20
    is_married = False
    has_degree = False
    has_job = True
    man = [name, surname, age, is_married, has_degree, has_job]
    json.dump(man, f)


with open('mac.txt', 'r') as f2:
    deserialized_data = json.load(f2)

    print(deserialized_data)
