from datetime import datetime, time


reservas = []


def verif_conflito(hora_inic, hora_fim):
    for reserva in reservas:
        if hora_inic <= reserva[1] and hora_fim >= reserva[0]:
            return True

    
    return False

def fazer_reserva():
    while True:
        min_h = time(9, 0)
        max_h = time(23, 0)
        hora_inic = input("Digite a hora inicial da reserva (entre 09:00 e 23:00): ")
        hora_fim = input("Digite a hora final da reserva (entre 09:00 e 23:00): ")
        hora_inic = datetime.strptime(hora_inic, "%H:%M").time()
        hora_fim = datetime.strptime(hora_fim, "%H:%M").time()

        if (min_h > hora_inic) or (hora_fim >= max_h) or (hora_inic >= hora_fim):
            print("Horário inválido! Favor escolher um entre 09:00 e 23:00")
            break
        if verif_conflito(hora_inic, hora_fim):
            print("Já há reserva neste horário, favor escolher outro")
            break
        
        str_hora_inic = hora_inic.hour
        str_minute_inic = hora_inic.minute
        str_hora_fim = hora_fim.hour
        str_minute_fim = hora_fim.minute
        
        duracao = ((int(str_hora_fim) * 60 + int(str_minute_fim)) - (int(str_hora_inic) * 60 + int(str_minute_inic)))
        valor = duracao *8/60
        
        reservas.append((hora_inic, hora_fim))
        print(f"A reserva inicia às {hora_inic} e finaliza às {hora_fim}")
        print(f"O valor total das reservas é R${valor:.2f}")
        
        break
    
    
def ver_reserva():
    print("Reservas: ")
    for reserva in reservas:
        print(f"\n * {reserva[0]} às {reserva[1]}")
        


    
    
opcao = 0
while opcao !=3 :
    print("\n1. Fazer Reserva ")
    print("2. Ver Reserva ")
    print("3. Sair ")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        fazer_reserva()

    elif opcao == 2:
        ver_reserva()

    elif opcao == 3:
        print("saindo...")
        break
        
    else:
        print("Digite a opção certa: ")
        

