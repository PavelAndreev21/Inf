# Программа, которая выводит текст песенки 99 бутылок пива.
i = 99
while i > 2:
    print(i, 'bottles of beer on the wall,', i, 'bottles of beer.')
    i = i - 1
    print('Take one down and pass it around,',
          i, 'bottles of beer on the wall.')
while i > 1:
    print(i, 'bottles of beer on the wall,', i, 'bottles of beer.')
    i = i - 1
    print('Take one down and pass it around, bottle of beer on the wall.')
print('Take one down and pass it around, no more bottles of beer on the wall.')
print('Go to the store and buy some more, 99 bottles of beer on the wall.')
