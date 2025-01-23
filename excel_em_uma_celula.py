import re
from colorama import init, Style, Fore

# Inicializa o colorama para estilizar a saída no terminal
init(autoreset=True)

def extract_references(formula: str) -> list:
    return re.findall(r"[A-Z]+[0-9]+", formula.upper())

def resolve_cell(cell_ref: str, dynamic_cell: str, cache: dict) -> str:

    # 1. Se a referência é a célula dinâmica, retorna o próprio nome
    if cell_ref == dynamic_cell:
        return dynamic_cell  # Não substituímos nada além de manter "A1" ou o que for
    
    # 2. Se já resolvemos antes, retorne do cache
    if cell_ref in cache:
        return cache[cell_ref]

    # 3. Perguntar ao usuário
    user_input = input(
        f"{Fore.WHITE}O que há na célula {Fore.RED}{cell_ref}{Style.RESET_ALL}? {Fore.CYAN}"
    ).lstrip('=').strip()


    if not extract_references(user_input):
        # É um valor puro. Ex.: 100, "ABC", etc.
        cache[cell_ref] = user_input
        return user_input

    # Caso contrário, o usuário digitou uma fórmula (sem "=")
    expanded_formula = expand_formula(user_input, dynamic_cell, cache)
    cache[cell_ref] = expanded_formula
    return expanded_formula

def expand_formula(formula: str, dynamic_cell: str, cache: dict) -> str:
    # Encontrar todas as referências na fórmula
    refs = extract_references(formula)
    # Para cada referência, substituir pela expressão expandida
    for ref in refs:
        # Resolve cada célula e retorna algo que só contenha
        # (1) valores ou (2) a célula dinâmica
        expansion = resolve_cell(ref, dynamic_cell, cache)
        # Substitui todas as ocorrências daquela referência na fórmula
        formula = formula.replace(ref, f"({expansion})")
    return formula

def synthesize_formula():
    print("Bem-vindo ao sintetizador de fórmulas!")
    
    # 1. Solicita ao usuário a célula dinâmica
    dynamic_cell = input(
        f"Digite o endereço da {Fore.YELLOW}CÉLULA DINÂMICA{Style.RESET_ALL} (ex.: {Fore.BLUE}A1{Style.RESET_ALL}): {Fore.CYAN}"
    ).lstrip('=').strip().upper()
    
    # 2. Solicita a fórmula inicial (sem o '=' no input)
    # Obs.: se a fórmula copiada vier com "=", podemos removê-lo com .lstrip('=').strip()
    formula = input(
        f"{Fore.WHITE}Copie aqui a fórmula inicial (ex: {Fore.BLUE}=B2 + C3 * 2{Style.RESET_ALL}): {Fore.CYAN}"
    ).lstrip('=').strip()

    print(f"{Style.RESET_ALL}----------------------------------------")

    # 3. Dicionário para armazenar (cache) as expansões de cada célula
    cache = {}

    # 4. Expandir a fórmula principal
    final_formula = expand_formula(formula, dynamic_cell, cache)

    print(f"\n{Fore.WHITE}Fórmula final simplificada:")
    print(f"{Fore.BLUE}={final_formula}{Style.RESET_ALL}")

if __name__ == "__main__":
    synthesize_formula()
