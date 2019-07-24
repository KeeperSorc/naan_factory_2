##Testing
import naan_factory_functions as nff

#Test 1 - test make_dough function
#spec - when called, should return int dough_amount
print("test make_dough function, when called, should take in the amount of wheat and water, and return the dough amount")
setup_result = nff.make_dough(10,20)
print(setup_result)

#Test 2 - test bake_naan function
#spec -
print("test bake_naan function, when called, should take in the amount of dough, and return the naan amount")
setup_result = nff.bake_naan(setup_result)
print(setup_result)

#Test 3 - deliver_naan function
#spec -
print("test deliver_naan function, when called, should take in the distance for the delivery, and return delivery time")
setup_result = nff.deliver_naan(30)
print(setup_result)