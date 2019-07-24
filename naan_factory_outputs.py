#Print naan factory outputs
#Assume you start with 30 units of wheat and water
#Assume the driver will travel at 10 miles per hour
import naan_factory_functions as nff
naan_amount = nff.bake_naan(nff.make_dough(30,30))
naan_delivery_time = nff.deliver_naan(20)

print("You ordered " + str(naan_amount) + " amount of naan.")
print("Your naan will take " + str(naan_delivery_time) + " minutes to deliver.")