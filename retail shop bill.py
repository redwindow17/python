tprice = 0
tup = [['apple', '100', '2'], ['blackberry', '100', '23']]
myformat = "{:<10}{:<25}{:<5}{}"
print(myformat.format('S.no', 'Product', 'Unit', 'Price'))
for i in range(len(tup)):
    if len(tup[i][0]) <= 7:
        print(myformat.format(str([i + 1]), tup[i][0], tup[i][2], tup[i][1]))
    else:
        print(myformat.format(str([i + 1]), tup[i][0], tup[i][2], tup[i][1]))
    price = int(tup[i][1])
    tprice += price
print('\t\t\tTotal price:',tprice)

