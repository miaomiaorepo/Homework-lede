#Shuyao Xiao
#05/23/2016
#Homework1

year_of_birth = input("what year were you born?")
age = 2016 - int(year_of_birth)
heart_beaten = 80*60*24*365*int(age)
blue_whales_heart = 10*60*24*365*int(age)
rabbits_heart = 150*60*24*365*int(age)/1000000000
Venus_years = 2030 - int(year_of_birth)
Neptune_years = int(age) - 164.79
age_difference = 26 - int(age)
age_difference2 = int(age) - 26

if int(year_of_birth) >2016:
    print("Are you from future? If not, please enter the right year.")
    year_of_birth = input("what year were you born?")


print("You are roughly ", age, " years old.")
print("Your heart has beaten ", heart_beaten, " times in your lifetime.")
print("A blue whale's would have beaten ", blue_whales_heart, "times.")
print("A rabbit's heart has beaten ", rabbits_heart, " billion times.")
print("On Venus you are ", Venus_years, " years old.")
print("On Neptune you are ", Neptune_years, "years old.")

if age == 26:
    print("Oh! We are in the same age. Nice to see you!")
elif age < 26:
    print("You are ", age_difference, " years younger than me!")
else:
    print("Your are ", age_difference2, " years older than me!" )

if int(year_of_birth) % 2 == 0:
    print("You were born in the even year.")
else:
    print("You were born in the odd year.")

if int(year_of_birth) > 2008:
    print("Pittsburgh Steelers have not won Super Bowl yet since you were born.")
elif int(year_of_birth) > 2005:
    print("Pittsburgh Steelers have won Super Bowl one time only since you were born.")
elif int(year_of_birth) > 1979:
    print("Pittsburgh Steelers have won Super Bowl for 2 times only since you were born!")
elif int(year_of_birth) > 1978:
    print("Pittsburgh Steelers have won Super Bowl for 3 times since you were born!")
elif int(year_of_birth) > 1975:
    print("Pittsburgh Steelers have won Super Bowl for 4 times since you were born!")
elif int(year_of_birth) > 1974:
    print("Pittsburgh Steelers have won Super Bowl for 5 times since you were born!")
else:
    print("Pittsburgh Steelers have won Super Bowl for 6 times since you were born!")

if int(year_of_birth) > 2009:
    print("President BO was in office when you were born.")
elif int(year_of_birth) > 2001:
    print("President GWB was in office when you were born.")
elif int(year_of_birth) > 1993:
    print("President BC was in office when you were born.")
elif int(year_of_birth) > 1989:
    print("President GHWB was in office when you were born.")
elif int(year_of_birth) > 1981:
    print("President RR was in office when you were born.")
elif int(year_of_birth) > 1977:
    print("President JC was in office when you were born.")
elif int(year_of_birth) > 1974:
    print("President GF was in office when you were born.")
elif int(year_of_birth) > 1969:
    print("President RN was in office when you were born.")
elif int(year_of_birth) > 1963:
    print("President LBJ was in office when you were born.")
elif int(year_of_birth) > 1961:
    print("President JFK was in office when you were born.")
elif int(year_of_birth) > 1953:
    print("President DDE was in office when you were born.")
elif int(year_of_birth) > 1945:
    print("President HST was in office when you were born.")
else:
    print("Sorry.I don't know which president was in the office. ")
