__author__ = 'igorpodobnik'
import random
prestolnice = {
"Slovenija":"Ljubljana",
"Hrvaska" : "Zagreb"
}
random.choice(prestolnice.keys())
print prestolnice


#random.sample()
#random.choice()
#dist.keys()
#dist.value()
random_key = random.sample(prestolnice, 1)[0]
print random_key