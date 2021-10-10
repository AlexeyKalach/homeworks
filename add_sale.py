import sys
price = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as c:
    c.write(price + '\n')