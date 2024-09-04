import os

# Caminho para o arquivo que você deseja deletar
caminho = 'C:/Users/UserTI/Documents/Codes/Python/testeDeDelete.txt'

pasta = 'C:/Users/UserTI/Documents/Codes/Python'
temp = 'C:/Users/UserTI/Documents/Codes/Python/TEMP'

itens = os.listdir(pasta)
tempItens = os.listdir(temp)

num_arquivos = sum(1 for item in itens if os.path.isfile(os.path.join(pasta, item)))

num_arquivos += 1

if num_arquivos > 10:
    print(f"\nTeste de arquivos: {tempItens}\n")
    try:
        os.remove(tempItens)
        print(f"Arquivo '{tempItens}' deletado com sucesso.")
    except FileNotFoundError:
        print(f"Arquivo '{tempItens}' não encontrado.")
    except PermissionError:
        print(f"Você não tem permissão para deletar o arquivo '{tempItens}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
else:
    print(f"\nDeu errado\n")
    
