#Functions to be used in the naan factory

#make_dough function - takes in the amounts of wheat and water, then returns the approximate amount of dough
def make_dough(wheat_arg,water_arg):
    dough_amount = wheat_arg + water_arg
    return dough_amount

#bake_naan function - takes in the amount of dough, then returns the approximate amount of baked naan
def bake_naan(dough_arg):
    naan_amount = float(dough_arg/2)
    return naan_amount

#deliver_naan function - takes in distance in miles, returns approx delivery time in minutes, assuming delivery speed is 10 miles per hour
def deliver_naan(distance_arg):
    delivery_time = (distance_arg/10)*60
    return delivery_time