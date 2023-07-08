print()

""" def converter_para_minutos_segundos(numero):
    minutos = numero % 60  # Divide o número inteiro pela quantidade de segundos em um minuto
    segundos = numero // numero % 60  # Obtém o resto da divisão para determinar os segundos restantes
    
    return minutos, segundos

# Exemplo de uso
numero_inteiro = 556
minutos, segundos = converter_para_minutos_segundos(numero_inteiro)
print(f'{numero_inteiro} segundos é igual a {minutos} minutos e {segundos} segundos.')

 """

""" seconds = input()

seg = int(seconds)

hrs = seg // 3600
seconds_rest = seg % 3600
min = seconds_rest // 60
seconds_final = seconds_rest % 60
print()
print(f'Total de minutos {seg}')
print()

print(hrs, "Horas")
print(min, "Minutos")
print(seconds_final, "Segundos")
print()
print(f'{hrs}h {min}min {seconds_final}s')
print(f'{hrs}:{min}:{seconds_final}')
print() """

seconds = input("Digite um número inteiro.")

seg = int(seconds)

hrs = seg // 3600
seconds_rest = seg % 3600
min = seconds_rest // 60
seconds_final = seconds_rest % 60
print()
print(f'Total de minutos {seg}')
print()

print(hrs, "Horas")
print(min, "Minutos")
print(seconds_final, "Segundos")
print()
print(f'{hrs}h {min}min {seconds_final}s')
print(f'{hrs}:{min}:{seconds_final}')
print()


##############################################################

def converter_segundos(segundos):
    horas = segundos // 3600
    segundos_rest = segundos % 3600
    minutos = segundos_rest // 60
    segundos_final = segundos_rest % 60
    return horas, minutos, segundos_final

segundos_totais = seg
horas, minutos, segundos = converter_segundos(segundos_totais)
print(f'{horas}h {minutos}min {segundos}s\n')