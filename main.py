import datetime
from decimal import Decimal

def add(items, title, amount, expiration_date=None):
    DATE_FORMAT = '%Y-%m-%d'
    if expiration_date == None:
        item_dict = {'amount': amount, 'expiration_date': None}
    else:
        date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
        item_dict = {'amount': amount, 'expiration_date': date}
    item_list = [item_dict]
    if title in items:
        items[title].append(item_dict)
    else:
        items[title] = item_list
    return items

def add_by_note(items, note):
    note_list = note.split()
    if '-' in note_list[-1]:
        expiration_date = note_list[-1]
        amount = Decimal(note_list[-2])
        title = ''
        for i in range(len(note_list) - 2):
            title += note_list[i] + ' '
    else:
        expiration_date = None
        amount = Decimal(note_list[-1])
        title = ''
        for i in range(len(note_list) - 1):
            title += note_list[i]
    if title[-1] == ' ':
        title = title[:-1]
    DATE_FORMAT = '%Y-%m-%d'
    if expiration_date == None:
        item_dict = {'amount': amount, 'expiration_date': None}
    else:
        date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
        #date = expiration_date
        item_dict = {'amount': amount, 'expiration_date': date}
    item_list = [item_dict]
    if title in items:
        items[title].append(item_dict)
    else:
        items[title] = item_list
    return items


def find(items, needle):
    matched_items = []
    for key in items.keys():
        if needle.lower() in key.lower():
            matched_items.append(key)
    return matched_items


def amount(items, needle):
    keys = find(items, needle)
    amount = Decimal('0')
    for key in keys:
        if needle.lower() in key.lower():
            for item in items[key]:
                amount += item['amount']
    return amount


def expire(items, in_advance_days=0):
    DATE_FORMAT = '%Y-%m-%d'
    current_date = datetime.date.today()
    list_of_goods = []
    for item, food in items.items():
        amounts = Decimal('0')
        for one_food in food:
            if one_food['expiration_date']:
                check_expiration = one_food['expiration_date'] - current_date
                if check_expiration <= datetime.timedelta(days = in_advance_days):
                    amounts += one_food['amount']
        tuple_of_food = (item, amounts)
        if amounts != 0:
            list_of_goods.append(tuple_of_food)
    return list_of_goods
    
    
goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {'amount': Decimal('1'), 'expiration_date': datetime.date(2024, 11, 22)}
    ],
    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2024, 11, 23)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2024, 11, 24)}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}

#add(goods, 'Пельмени Универсальные', Decimal('2'), '2024-11-23')
#add(goods, 'Пельмени Универсальные', Decimal('0.5'), '2024-12-10')
#add(goods, 'Яйца Фабрики №1', Decimal('4'), '2023-07-15')
#add(goods, 'Вода', Decimal('1.5'))
#add(goods, 'Яблоки', Decimal('2'), '2024-12-1')

#add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
#add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15')

#print(find(goods, 'Яйца'))

#print(amount(goods, 'Яйца'))
#print(amount(goods, 'Хлеб'))
#print(amount(goods, 'Яйца'))
#print(amount(goods, 'вода'))

#print(expire(goods))    # Вывод: [('Хлеб', Decimal('1'))]
#print(expire(goods, 1)) # Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
#print(expire(goods, 2)) # Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))] 

#print(goods)
