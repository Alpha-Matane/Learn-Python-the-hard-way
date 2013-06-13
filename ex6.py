x = "There are %d types of people." % 10 # 1
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 2

print x
print y

print "I said: %r." % x  # 3
print "I also said: '%s'." %y # 4

got_it = False
joke_evaluation = "Isn't that joke so funny?! %r" # 5 (str(False) ?)

print joke_evaluation % got_it 

w = "This is the left side of..."
e = "a string with a right side."

print w + e # It's concatenation, e is glued to the end of w.
