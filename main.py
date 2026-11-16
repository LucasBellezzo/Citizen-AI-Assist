import sys
from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    base = BaseConhecimento("data/base_conhecimento.json")
    if not base.carregar():
        print("Nao foi possivel iniciar o sistema devido a erro na base de conhecimento.")
        sys.exit(1)

    assistente = Assistente("Citizen Assist AI", base)

    while True:
        print("\n" + "*" * 65)
        print(f"  BEM-VINDO AO {assistente.nome.upper()}")
        print("  Orientacao Cidada, Direitos e Eficiencia Energetica")
        print("*" * 65)
        print("1. Fazer uma pergunta em texto livre")
        print("2. Navegar por categorias")
        print("3. Ver indicadores de atendimento")
        print("4. Exportar atendimentos para CSV")
        print("0. Sair")

        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == "1":
            assistente.perguntar()
        elif opcao == "2":
            assistente.navegar()
        elif opcao == "3":
            assistente.indicadores()
        elif opcao == "4":
            assistente.exportar_csv()
        elif opcao == "0":
            assistente.avaliar_facilidade()
            assistente.exportar_csv()
            print("\nEncerrando o Citizen Assist AI. Ate logo!")
            break
        else:
            print("Opcao invalida. Digite um numero entre 0 e 4.")


if __name__ == "__main__":
    main()
