''' This Module creates a database of all Yugioh Speed duel cards '''
from yugiohGameObjects import YugiohSet

#          Speed Duels 2019 Sets
list_of_product=["arena_of_souls", 
                 "destiny_masters",
                ]
cards=[]
for product_name in list_of_product:
    cards+=YugiohSet(product_name).cards
