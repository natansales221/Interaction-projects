class passagemOnibus():
    
    def __init__(self, capacidade):
        
        self.capacidade = capacidade
        self.lugares = [0] * capacidade

    def cancelar_reserva(self, num):
        if num < 1 or num > self.capacidade:
                
            return "\nLugar inválido!"

        if self.lugares[num - 1] == 1:
            self.lugares[num - 1] = 0
            
            return f"\nLugar {num} cancelado com sucesso!"
        else:
            return f"\nLugar {num} já estava vazio!"

        
    def exibir_menu(self):
        
        print("\n1. Exibir mapa de lugares ")
        print("2. Fazer Reserva ")
        print("3. Cancelar Reserva ")
        print("4. Sair ")
        
    def fazer_reserva(self, num):
        
        if num < 1 or num > self.capacidade:
            
            return "\nLugar inválido!"

        if self.lugares[num - 1] == 0:
            
            self.lugares[num - 1] = 1
            return f"\nLugar {num} reservado com sucesso!"
        
        else:
            
            return f"\nLugar {num} indisponível!"
        
    def exibir_mapa(self):
        
        for i in range(0, self.capacidade, 2):
            
            esq = i+1
            dir = i+2
            status_esq = "X" if self.lugares[i] == 1 else " "
            status_dir = "X" if dir <= self.capacidade and self.lugares[i+1] == 1 else " "
            
            print(f"Lugar {esq}  [{status_esq}]  Lugar {dir}  [{status_dir}]")
               
    def main(self):    
        
        opcao = 0
        
        while opcao !=4 :
            
            self.exibir_menu()

            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                
                self.exibir_mapa()

            elif opcao == 2:
                
                num = int(input("Digite o assento que voce quer escolher: "))
                print(self.fazer_reserva(num))
                self.fazer_reserva(num)
            
            elif opcao == 3:
                
                num = int(input("Digite o assento que voce quer cancelar: "))
                print(self.cancelar_reserva(num))
                self.cancelar_reserva(num)

            elif opcao == 4:
                
                print("saindo...")
                
                break
                
            else:
                
                print("Digite a opção certa: ")

if __name__ == '__main__':
    service=passagemOnibus(10)
    service.main()          
