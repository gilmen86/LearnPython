# def plus(a,b):
#     return a+b
# def minus (a,b):
#     return a-b
# if __name__=='__main__':
#     print(plus(2,2))
#     print(minus(2, 2))
# print('Вроде все')

# 2.8
# number_pi = 3.141592653589793
# print(f'{number_pi:.6f}')

# i=float(input())
# print(f'{i:.2f}')

# i=int(input())
# print(f'{i:010d}')

# Выравниванеи, заполнение
# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_сheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_сheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')

text = input()
print(f"|{text:&^20}|")
print(f"|{text:&>20}|")
print(f"|{text:&<20}|")