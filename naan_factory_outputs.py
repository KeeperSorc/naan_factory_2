#Print naan factory
import naan_factory_functions as nff
naan_amount = nff.bake_naan(nff.make_dough(30,30))
naan_delivery_time = nff.deliver_naan(20)

print("You ordered " + naan_amount + " amount of naan.")
print("Your naan will take " + naan_delivery_time + " minutes to deliver.")