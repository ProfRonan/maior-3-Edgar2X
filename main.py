"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    var_1 = float(input("Digite a primeira variável:"))
    var_2 = float(input("Digite a segunda variável:"))
    var_3 = float(input("Digite a terceira variável:"))
    maior_3 = {var_1,var_2,var_3}
    print(f'{max(maior_3)}')

if __name__ == '__main__':
    main()
