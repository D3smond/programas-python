##Jogo da velha, criado em 06/05/2018##
##By: Rafael DSS

class Main():
    
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        pass

    def imprimetab(self):
        tab = self.tabuleiro
        print(f'{tab[0][0]}|{tab[0][1]}|{tab[0][2]}')
        print(5 * '-')
        print(f'{tab[1][0]}|{tab[1][1]}|{tab[1][2]}')
        print(5 * '-')
        print(f'{tab[2][0]}|{tab[2][1]}|{tab[2][2]}')

    def coordenada(self, posicao):
        coord = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0],8:[2,1],9:[2,2]}
        return coord[posicao]

    
    def ganha(self, j):
        t = lambda x, y: self.tabuleiro[x][y] == j
        return t(0,0) and t(1,1) and t(2,2)\
               or t(0,2) and t(1,1) and t(2,0)\
               or t(0,0) and t(0,1) and t(0,2)\
               or t(1,0) and t(1,1) and t(1,2)\
               or t(2,0) and t(2,1) and t(2,2)\
               or t(0,0) and t(1,0) and t(2,0)\
               or t(0,1) and t(1,1) and t(2,1)\
               or t(0,2) and t(1,2) and t(2,2)


    def validar(self,num):
        coo = self.coordenada(num)
        if not self.tabuleiro[coo[0]][coo[1]] == 'X' or self.tabuleiro[coo[0]][coo[1]] == 'O':
            return True
        else:
            False


    def main(self):
        jogadas = 0

        saida = True
        while saida:
            jogadores = ['X','O']
            for jogador in jogadores:

                
                if self.ganha('X'):
                    self.imprimetab()
                    print('O X ganhou')
                    saida = False
                    break
                elif self.ganha('O'):
                    self.imprimetab()
                    print('O O ganhou')
                    saida = False
                    break
                elif jogadas == 9:
                    self.imprimetab()
                    print('Empate')
                    saida = False
                    break
                
                self.imprimetab()
                
                posicao = int(input(f'Quer jogar o {jogador} em que posição?: '))
                if self.validar(posicao):
                    jogadas = 1
                    c = self.coordenada(posicao)
                    self.tabuleiro[c[0]][c[1]] = jogador
                else:
                    print('Posição inválida')

tab = [[1,2,3],
       [4,5,6],
       [7,8,9]]

Main(tab).main()                
            
        
        

    
