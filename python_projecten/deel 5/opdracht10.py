from fruitmand import fruitmand
from operator import itemgetter

sorted_fruitmand = sorted(fruitmand, key=itemgetter('weight'), reverse=True)
  
for fruit in sorted_fruitmand:
    print(fruit['name'], fruit['weight'])
