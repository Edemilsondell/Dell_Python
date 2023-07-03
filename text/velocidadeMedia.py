""" distancia = 30  # distância em quilômetros
velocidade_y = 60  # velocidade do carro Y em Km/h

tempo = distancia / velocidade_y  # tempo em horas
tempo_em_minutos = tempo * 60  # tempo em minutos

print("O carro Y leva", tempo_em_minutos, "minutos para alcançar o carro X.")
 """

distancia = 30
# distancia = input("\nDigite a distância a ser percorrida:\n")
velocidade = input("\nDigite a velocida do carro:\n")

""" v= velocidade
d= distancia  """
d= float(distancia)
v= float(velocidade)

tempo = (v / d) * 60
casas_decimais = 0
resultado_formatado = "{:.{}f}".format(tempo, casas_decimais)
# print(tempo, "Minutos.")
print(resultado_formatado, "Minutos.")

distance = int(input("\nDigite a velocida do carro:\n"))

time = distance * 2  # Calculate the time in minutes

print(time, "minutos")
# print(f"{time} minutos")
