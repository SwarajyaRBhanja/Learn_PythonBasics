
#dictionary is a set of key-value pairs
#It is unordered
#It is mutable
#It is indexed
#can't contain duplicate keys

my_Dict= {
    "name": "Anurag Sahoo",
    "company": "Yes Bank",
    "Marks": [79,67,99],
    "dict_inside_myDict":{"name_0":"Swarajya"}

}
print(my_Dict)
print(my_Dict["name"]) #Anurag Sahoo
print(my_Dict["Marks"]) #[79, 67, 99]
print(my_Dict["dict_inside_myDict"]["name_0"]) #Swarajya
my_Dict["Marks"]= [76,89,97]
print(my_Dict["Marks"])

print(my_Dict.keys()) #it will give me all the key names inside the dict..dict_keys(['name', 'company', 'Marks', 'dict_inside_myDict'])
print(my_Dict.values()) #it will give me all the value names inside the dict... dict_values(['Anurag Sahoo', 'Yes Bank', [76, 89, 97], {'name_0': 'Swarajya'}])
print(my_Dict.items()) #it will give me dict contents in key-value pair.. dict_items([('name', 'Anurag Sahoo'), ('company', 'Yes Bank'), ('Marks', [76, 89, 97]), ('dict_inside_myDict', {'name_0': 'Swarajya'})])
update_Dict= {"name2":"Swapnil Agarwal"}
my_Dict.update(update_Dict) #you can update the my_dict with another new key-value pairs
print(my_Dict) #{'name': 'Anurag Sahoo', 'company': 'Yes Bank', 'Marks': [76, 89, 97], 'dict_inside_myDict': {'name_0': 'Swarajya'}, 'name2': 'Swapnil Agarwal'}

my_Dict.update({"company":"Natioanl payment corporation of India"}) #updating existing value
print(my_Dict) #{'name': 'Anurag Sahoo', 'company': 'Natioanl payment corporation of India', 'Marks': [76, 89, 97], 'dict_inside_myDict': {'name_0': 'Swarajya'}, 'name2': 'Swapnil Agarwal'}

print(my_Dict.get("company")) #Natioanl payment corporation of India
print(my_Dict["company"]) 
#in above 2 lines will return same output if company is there in dict, bu if company is not there in dict then .get() will return "None" & [] will throw error keyerror:




