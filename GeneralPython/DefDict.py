## https://www.accelebrate.com/blog/using-defaultdict-python/
'''
class collections.defaultdict([default_factory[, ...]])
Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class.
It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.

The first argument provides the initial value for the default_factory attribute; it defaults to None.
All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.

'''
from collections import defaultdict

def fun1():
    ice_cream = defaultdict(lambda : "vanilla")
    ice_cream['Sarah'] = 'Chunkey'
    ice_cream['Abdul']= 'Butter'

    print(ice_cream['Sarah'])
    print("###############")

    for name, flavour in ice_cream.items():
        print("Name:{} :: Flavour:{}".format(name,flavour))

    print(ice_cream['prashanta'])

'''When called fun1(), the output is ::
Chunkey
###############
Name:Sarah :: Flavour:Chunkey
Name:Abdul :: Flavour:Butter
vanilla

'''

def fun2():
    food_list = 'spam spam spam egg rice egg spam'.split()
    food_count = defaultdict(int)  # default value of int is zero  ## Note: “lambda: 0″ would also work in this situation
    for food in food_list:
        food_count[food] +=1

    print(food_count)

    for k,v in food_count.items():
        print(k,v)

'''when calles fun2(), the output is :
defaultdict(<class 'int'>, {'spam': 4, 'egg': 2, 'rice': 1})
spam 4
egg 2
rice 1
'''

def fun3():
    city_list = [('TX', 'Austin'), ('TX', 'Houston'), ('NY', 'Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'),
                 ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA', 'Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
    cities_by_state = defaultdict(list)

    for state, city in city_list:
        cities_by_state[state].append(city)

    print(cities_by_state)
    print("###############")
    for state, cities in cities_by_state.items():
        print(state,":",",".join(cities))

'''when called fun3(), the output is ::
defaultdict(<class 'list'>, {'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'], 'CA': ['Sacramento', 'Palo Alto'],
 'GA': ['Atlanta']})
###############
TX : Austin,Houston,Dallas
NY : Albany,Syracuse,Buffalo,Rochester
CA : Sacramento,Palo Alto
GA : Atlanta
'''

if __name__ == '__main__':
    fun3()

'''
Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):

>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...     d[k] += 1
...
>>> d.items()
[('i', 4), ('p', 2), ('s', 4), ('m', 1)]

'''


