user_input = input("Enter name, age, and id in the format 'name:value,age:value,id:value :")
pairs = user_input.split(',')

result_dict = {}

for pair in pairs:
    key, value = pair.split(':')
    result_dict[key] = value

print(result_dict)

