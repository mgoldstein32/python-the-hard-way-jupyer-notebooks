x = "There are %d types of people." % 10 #assigns string to x
binary = "binary" #assigns string
do_not = "don't" #assigns string
y = "Those who know %s and those who %s" % (binary, do_not) #assigns string with other formatted strings within it

print x #prints string x
print y #prints string y

print "I said: %r." % x #does so again with additional words
print "I also said: '%s'." % y

hilarious = False #creates boolean with a value of false
joke_evaluation = "Isn't that joke so funny?! %r" #creates string with an insertible value

print joke_evaluation % hilarious #prints string alongside previously-made boolean

w = "This is the left side of..." #creates two strings
e = "a string with a right side."

print w + e #concatenates strings
