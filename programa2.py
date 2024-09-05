
#Importação dos módulos de acesso a modificação de arquivos
import os
import shutil
import time

#Criação da função que irá verificar os arquivos da pasta e exclui-lo
def excluir_arquivos(pasta):
    if not os.path.exists(pasta):
        print(f"\nA pasta {pasta} não existe\n")
        return
    
    for item in os.listdir(pasta):
        caminho_item = os.path.join(pasta, item)

        if os.path.isdir(caminho_item):
            shutil.rmtree(caminho_item)
        else:
            os.remove(caminho_item)

    print("Todos os arquivos foram excluídos!")

#Diretório que será verificado e o que será excluido 
pastaTemp = 'C:/Users/TI/Documents/PASTA TEMPORARIA'
pastaRaiz = 'C:/Users/TI/Documents/PASTA RAIZ'

#Executa o codigo em loop
while True:

    #Lista todos os itens na pasta raiz em seguida realiza a contagem
    itens = os.listdir(pastaRaiz)
    num_arqui = sum(1 for item in itens if os.path.isfile(os.path.join(pastaRaiz, item)))

    #Verifica a quantidade de arquivos para exlcluir
    if num_arqui > 10:
        excluir_arquivos(pastaTemp)
    else:
        print(f"\nA pasta {pastaRaiz} está funcionando bem.\n")

    #Cria um delay
    time.sleep(5)