# Grade: 12.5 / 14

# Shuyao Xiao
# 5/31/2016
# Homework 3

# TA-COMMENT: (-1) A lot of your print statements in the code below don't have the proper (). When submitting a script, you should first try to run that script on the command line -- you can use the command `python3 [filename]` -- to double check that it works.

# LISTS
# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['France', 'Japan', 'China', 'America', 'India', 'Germany']
# 2) Using a for loop, print each element of the list
for country in countries:
    print(country)
# 3) Sort the list permanently.
countries.sort() # TA-COMMENT: Nice!
print(countries)
# 4) Display the first element of the list
print(countries[0])
# 5) Display the second-to-last element of the list using a line of code that
    # will work no matter what the size of the list is (hint: len will be helpful)
print(countries[-2])
# 6) Delete one of the countries from the list using its name (we didn't learn this in class).
countries.remove('China')
print countries
# 7) Using a for loop, print each element of the list again, which should now be one element shorter.
for country in countries:
    print country

# DICTIONARIES
# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'.
tree = {'name': 'Tree of Life', 'species': 'Mesquite', 'age': 400,
        'location': 'Bahrain', 'latitude':26.066700 ,'longitude':50.557700}
# 2) Print the sentence "{name} is a {years old} tree that is in {location_name}"
print tree['name'], 'is a', tree['age'], 'years old tree that is in', tree['location']
# 3) compare NYC
if tree['latitude'] < 40.7128:
    print 'The tree', tree['name'], 'in', tree['location'], 'is south of NYC'
else:
    print 'The tree', tree['name'], 'in', tree['location'], 'is north of NYC'
# 4) ask for age
age = input("How old are you?")
difference = int(age) - 400
if difference > 0:
    print 'you are', int(difference), 'years older than', tree['name']
else:
    difference2 = 400 - int(age)
    print tree['name'], 'was', int(difference2), 'years old when you were born.'

#LISTS OF DICTIONARIES
#1) Make a list of dictionaries of five places across the world
#   (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago
city_info = [
    {'name':'Moscow', 'latitude':55.755826, 'longitude':37.617300 },
    {'name':'Tehran', 'latitude':35.689197, 'longitude':51.388974 },
    {'name':'Falkland Islands', 'latitude':-51.796253, 'longitude':-59.523613 },
    {'name':'Seoul', 'latitude':37.566535, 'longitude':126.977969 },
    # TA-COMMENT: Soma meant Santiago, Chile! I think you grabbed another city located in Spain.
    {'name':'Santiago', 'latitude':42.878213, 'longitude':-8.544844 }
]
# 2) whether it is above or below the equator
# TA-COMMENT: (-0.5) The question actually asks you to print out "The Falkland Islands are a biogeographical part of the mild Antarctic zone" when your for loop reaches the Falkland Islands. You needed to have added a separate conditional for it below.

for city in city_info:
    if city['latitude'] > 0:
        print city['name'], 'is above the equator.'
    else:
        print city['name'], 'is below the equator.'
# 3) whether each city is north of south of your tree
for city in city_info:
    if city['latitude'] > tree['latitude']:
        print city['name'], 'is north of', tree['name']
    else:
        print city['name'], 'is south of', tree['name']
