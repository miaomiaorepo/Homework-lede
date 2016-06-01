# Shuyao Xiao
# 5/25/2016
# Homework 2

#Lists
numbers = [22, 90, 0, -10, 3, 22, 48]
#1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
print(numbers)
#1) Display the number of elements in the list
print(len(numbers))
#2) Display the 4th element of this list.
print(numbers[3])
#3) Display the sum of the 2nd and 4th element of the list.
print(int(numbers[1]) + int(numbers[3]))
#4) Display the 2nd-largest value in the list.
print(sorted(numbers)[5])
#5) Display the last element of the original unsorted list
print(numbers[6])

#if your original number is less than 10, multiply it by thirty
#If it's also even, add six.
for number in numbers:
    if number < 10:
        print(number*30)
    if number < 10 and number%2  == 0:
        print(number + 6)
#If it's greater than 50 subtract ten.
for number in numbers:
    if number > 50:
        print(number - 10)
#If it's not negative ten, subtract one.
for number in numbers:
    if number > -10 or number < -10:
        print(number - 1)
#7) Sum the result of each of the numbers divided by two
print sum(numbers)/2

#DICTIONARIES
#print "My favorite movie is", movie['title'], "which was released in",
# movie['year'], "and was directed by", movie['director']

movie = { 'title': 'Before Sunset', 'year': 2004, 'director':
          'Richard Linklater', 'budget': 2, 'revenue': 22 }
print("My favorite movie is", movie['title'], ", which was released in",
      movie['year'], ", and was directed by", movie['director'])
# add budget and revenue, print out the difference
print(movie['revenue'] - movie['budget'], "million")

if movie['revenue'] / movie['budget'] > 5:
    print("That was a good investment.")
if movie['revenue'] < movie['budget']:
    print("It was a flop.")

#the population of the boroughs of NYC
#Manhattan 1.6 million, Brooklyn 2.6m, Bronx 1.4m, Queens 2.3m,Staten Island 0.47m
population = {'Manhattan': 1.6, 'Brooklyn': 2.6, 'Bronx': 1.4, 'Queens': 2.3,
              'Staten Island': 0.47 }
#12) Display the population of Brooklyn.
print('There are', population['Brooklyn'], 'million people in Brooklyn.' )
#13) Display the combined population of all five boroughs.
print('The combined population is', population['Manhattan'] + population['Brooklyn'] + population['Bronx']
      + population['Queens'] + population['Staten Island'], 'million')
#14) Display what percent of NYC's population lives in Manhattan.
total = population['Manhattan'] + population['Brooklyn'] + population['Bronx']+ population['Queens'] + population['Staten Island']
# print total
print str(round(population['Manhattan'] / total*100,2)) + '%',"of NYC's population lives in Manhattan."
