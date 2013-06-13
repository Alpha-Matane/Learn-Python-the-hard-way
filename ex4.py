cars = 100                               #assign 100 to var 'cars'
space_in_a_car = 4                       #assign 4.0 to var 'space_in_a_car' 
drivers = 30                             #assign 30 to var'drivers'
passengers = 90
cars_not_driven = cars - drivers         #assign 100-30 to var 'cars_not_driven'
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven # typo in variable on line 8

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "THere will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# 1. No. It will use integer division, which makes sense because
# we are talking about indivisible passengers anyway.
