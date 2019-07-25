##Testing
import naan_factory_functions as nff

#Test 1 - test make_dough function
#spec - when called, should return int dough_amount
print("test make_dough function, when called, should take in the amount of wheat and water, and return the dough amount")
setup_result = nff.make_dough(10,20)
print(type(setup_result)==int)

#Test 2 - test bake_naan function
#spec - when called, should return int naan amount
print("test bake_naan function, when called, should take in the amount of dough, and return the naan amount")
setup_result = nff.bake_naan(setup_result)
print(type(setup_result)==int)

#Test 3 - deliver_naan function
#spec - when called, should return int delivery time
print("test deliver_naan function, when called, should take in the distance for the delivery, and return delivery time")
setup_result = nff.deliver_naan(30)
print(type(setup_result)==int)

#Test 4 - test naan_factory function
setup_result = nff.naan_factory(10,20)
print(type(setup_result)==int)