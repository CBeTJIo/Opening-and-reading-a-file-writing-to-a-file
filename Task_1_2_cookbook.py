num_list = []
name_idx = []
ingr_idx = []
my_list = []

with open('recipes.txt', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        line = line.replace("\n", "")
        my_list.append(line)
        if len(line) < 2 and line != '':
            num_list.append(int(line))
            name_idx.append(idx - 1)
            ingr = int(line)
            check = idx + 1
            while ingr > 0:
                ingr_idx.append(check)
                check += 1
                ingr -= 1

cook_book = dict()

ingrid = []
counter_1 = 0
counter_2 = 0


for idx, x in enumerate(my_list):
    if idx in name_idx:
        qty = num_list[counter_1]
        counter_1 += 1
        while qty > 0:
            a, b, c = my_list[ingr_idx[counter_2]].split(' | ')
            new_dict = {'ingredient_name': a, 'quantity': int(b), 'measure': c}
            ingrid.append(new_dict)
            counter_2 += 1
            qty -= 1
        cook_book[x] = ingrid
        ingrid = []

    else:
        continue

def get_shop_list_by_dishes(dishes, person_count):
    list_ingredients = []
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                m = [ingr['ingredient_name'], ingr['measure'], ingr['quantity'] * person_count]
                list_ingredients.append(m)
    last_count = 0
    teeeeest = []

    for test in list_ingredients:
        for gf in list_ingredients:
            if gf[0] in test:
                last_count += 1

        if last_count > 1:
            test[2] = test[2]*last_count
            teeeeest.append(test)
        else:
            teeeeest.append(test)

        last_count = 0
    my_result = dict()
    for last_ing in teeeeest:
        my_result[last_ing[0]] = {'measure': last_ing[1], 'quantity': last_ing[2]}
    return my_result
    #return teeeeest
    #return list_ingredients


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))

