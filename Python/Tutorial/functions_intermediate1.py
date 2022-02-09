x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['first_name'] = 'billy'
students[1]['first_name'] = 'bob'
sports_directory[1]['first_name'] = 'Andres'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for x in students:
        print("First Name: - " + x['first_name'], "|Last Name: - " + x['last_name'])
print(iterateDictionary(students))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

#Get Values From a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(first_name, students):
    for x in students:
        print(x[first_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for k, v in dojo.items():
        if ( len(v) == 7):
            print (len(v), "Locations")
        else:
            print(len(v), "instructors")
        for value in range(0, len(v)):
            if( k == 'locations'):
                print(v[value])
                if( k == 'instructors'):
                    print(v[value])
printInfo(dojo)


#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
