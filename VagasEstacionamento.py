class vagasEstacionamento():
    
    def __init__(self):
        self.vagas = {
            'A': ['-'] *5,
            'B': ['-'] *5,
            'C': ['-'] *5,
            'D': ['-'] *5
        }

        
    def show_menu(self):
        # print("\n")
        print("1. Exibir painel de vagas")
        print("2. Selecionar vaga automaticamente")
        print("3. Selecionar vaga manualmente")
        print("4. Cancelar vaga")
        print("5. Sair")
        
    def exibir_vagas(self, vagas):
        print("Bloco/vaga   1   2   3   4   5")

        for bloco, v in vagas.items():
            
            print("{:<12}".format(bloco), end=' ')
            
            for vaga in v:
                
                print("{:<3}".format(vaga), end= ' ')
                
            print()
            
    def preench_automatic(self, vagas):
        
        qtd_vaga_disp = {}
        
        for bloco, vaga_disp in vagas.items():
            qtd_vaga_disp[bloco] = vaga_disp.count('-')
            
        ordem_bloco = sorted(qtd_vaga_disp, key= qtd_vaga_disp.get, reverse=True)
        
        for bloco in ordem_bloco:
            
            for i, vaga in enumerate(vagas[bloco]):
                
                if vaga == '-':
                    
                    vagas[bloco][i] ='X'
                    
                    return True
                
        return False
    
    def preench_manual(self, vagas, bloco, numero):
        
        if vagas.get(bloco) is None:
            print("nao existe esse bloco")
            return False
        
        if numero > len(vagas[bloco]):
            print("nao existe essa vaga")
            return False

        
        if vagas[bloco][numero-1] != 'X':
            vagas[bloco][numero-1] = 'X'
            print("preenchido com sucesso")
        else:
            print("Vaga já estava preenchida")

                    
    def main(self):
        vagas = self.vagas
        opcao = 0
        while opcao != 5:
            self.show_menu()
            opcao = int(input("Selecione uma opção: "))
            
            if opcao == 1:
                self.exibir_vagas(vagas)
                
            elif opcao == 2:
                
                if self.preench_automatic(vagas):
                    print("reserva feita automaticamente")
                    
                else:
                    print("nao ha vagas disponiveis")
                    
            elif opcao == 3:
                bloco = input("Informe o bloco: ").upper()
                numero = int(input("Informe a vaga: "))
                
                self.preench_manual(vagas, bloco, numero)
                
            elif opcao == 4:
                print("opcao 4")
                
            elif opcao == 5:
                print("saindo...")
                break
            else:
                print("Opção inválida! ")
 
        
if __name__ == "__main__":
    service = vagasEstacionamento()
    service.main()