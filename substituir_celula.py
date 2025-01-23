from colorama import init, Fore, Style

init(autoreset=True)

def substituir_na_formula():
    # Solicitar ao usuário a fórmula inicial
    formula_inicial = input(f"Digite a fórmula do Excel: {Fore.BLUE}").upper()
    print()

    # Solicitar o valor que será substituído
    valor_para_substituir = input(f"Digite o valor que deseja substituir: {Fore.BLUE}").upper()
    print()
    
    # Solicitar o novo valor para substituir
    novo_valor = input(f"Digite o novo valor: {Fore.BLUE}").upper()
    print()
    
    # Substituir o valor na fórmula
    formula_final = formula_inicial.replace(valor_para_substituir, f"{Fore.RED}{novo_valor}{Fore.CYAN}")
    
    # Exibir a fórmula final
    print("Fórmula com a substituição feita: ")
    print(f"{Fore.CYAN}{formula_final}\n")


if __name__ == "__main__":
    substituir_na_formula()
