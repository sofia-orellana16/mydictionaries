person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

#print out of the name of the second child
print(person["children"][1])
print()
#print out the name of the cat
print(person["pets"]["cat"])
print()
#iterate throguh all childer and print out each child 
# for child in person["children"]
#print out the pets in this fomrat:
# type of pet: dog name of pet: Fido
print('Type of pet: dog name of pet:', person["pets"]['dog'])