print ("Hello world!")
print ('hello world!')
print (10)

print (10 + 10)
print ('hello' + 'world!')
print ('hello ' + 'world!')

# >>> str(10)
# '10'

print ('hello' + str(10))
print ('hello'+'10')

print('hello, Soma')
print('hello, ' + 'Soma')

name = input("what's your name?")
print('hello, ' + name)

year_of_birth = input("what year were you born?")
age = 2016 - int(year_of_birth)
print("you are roughly " + str(age) + " years old")
#or
print("you are roughly", age, "years old")

if age >= 30 or age > 100:
    print("cool")
elif age >= 21:
    print("here is your beer")
elif age < 0:
    print("you are an idiot")
else:
    print("nope, sorry")
    print("goodbye")
