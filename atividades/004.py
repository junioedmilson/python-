# Atividade 004
# Recebe um valor do usuário e imprime informações sobre o tipo primitivo
algo = input('digite algo: ')
print(f'o tipo primitivo desse valor é {type(algo)}')
print(f'so tem espaços? {algo.isspace()}')
print(f'e um numero? {algo.isnumeric()}')
print(f'e alfabetico? {algo.isalpha()}')
print(f'e alfanumerico? {algo.isalnum()}')
print(f'esta em maiusculas? {algo.isupper()}')
print(f'esta em minusculas? {algo.islower()}')
print(f'esta capitalizada? {algo.istitle()}')
print(f'é imprimível? {algo.isprintable()}')
print(f'é decimal? {algo.isdecimal()}')
print(f'é dígito? {algo.isdigit()}')