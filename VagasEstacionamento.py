class vagasEstacionamento():
    
    def show_menu(self):
        
        print("1. Exibir painel de vagas")
        print("2. Selecionar vaga automaticamente")
        print("3. Selecionar vaga manualmente")
        print("4. Cancelar vaga")
        print("5. Sair")
        
    def exibir_vagas(self):
        print("Bloco/vaga   1   2   3   4   5")
        vagas = {
            'A': ['-'] *5,
            'B': ['-'] *5,
            'C': ['-'] *5,
            'D': ['-'] *5
        }
        
        for bloco, v in vagas.items():
            print("{:<12}".format(bloco), end=' ')
            for vaga in v:
                print("{:<3}".format(vaga), end= ' ')
            print()
            

        
    def main(self):
        opcao = 0
        while opcao != 5:
            self.show_menu()
            opcao = int(input("Selecione uma opção: "))
            
            if opcao == 1:
                self.exibir_vagas()
                
            elif opcao == 5:
                print("saindo...")
                break
            else:
                print("Opção inválida! ")
 
        
if __name__ == "__main__":
    service = vagasEstacionamento()
    service.main()