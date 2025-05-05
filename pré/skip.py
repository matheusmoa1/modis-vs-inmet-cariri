import pandas as pd

# Teste sem definir cabeçalho, só pra ver as linhas
with open('dados_82792_D_1980-01-01_2019-01-01.csv', 'r', encoding='utf-8-sig') as f:
    for i in range(20):
        print(i, f.readline().strip())
