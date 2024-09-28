import random
import string
"""
uma função criada para gerar uma senha, caso o usuário não entre com o 
tamanho da senha, por padrão cria-se uma senha de tamanho 12
"""
def gerador_senha(tamanho=12):
    """Gera uma senha aleatória com o tamanho especificado."""
    # Combinações de caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    """retorna a senha erado na função"""
    return senha

"""
criação do método main com as chamadas da função 'gerador_senha' e solicita 
o tamanho da senha a ser gerado 
"""
def main():
    print("Bem-vindo ao Gerador de Senhas!")
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    senha = gerador_senha(tamanho)
    print(f"Sua senha gerada é: {senha}")

"""função main"""
if __name__ == "__main__":
    main()
