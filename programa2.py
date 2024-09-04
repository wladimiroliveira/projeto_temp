import os
import shutil

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

pastaTemp = 'C:/Users/UserTI/Documents/Codes/Python/TEMP'
pastaRaiz = 'C:/Users/UserTI/Documents/Codes/Python'

itens = os.listdir(pastaRaiz)
num_arqui = sum(1 for item in itens if os.path.isfile(os.path.join(pastaRaiz, item)))

if num_arqui > 10:
    excluir_arquivos(pastaTemp)
else:
    print(f"\nA pasta {pastaRaiz} está fnucionando bem.\n")