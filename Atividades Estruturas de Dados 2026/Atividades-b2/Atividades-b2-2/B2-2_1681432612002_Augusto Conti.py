"""
---------------------------------------------------------
FATEC - São Caetano do Sul
RA: 1681432612006
Finalidade: Controle de fila de impressão com prioridade
Data: 28/04/2026
---------------------------------------------------------
"""

fila_geral = []
fila_prioritaria = []

fila_geral.extend([
    {"nome_arquivo": "math_exam.pdf", "paginas": 3, "eh_admin": True},
    {"nome_arquivo": "world_map_image.png", "paginas": 1, "eh_admin": False},
    {"nome_arquivo": "english_text.pdf", "paginas": 23, "eh_admin": True},
    {"nome_arquivo": "history_homework.pdf", "paginas": 2, "eh_admin": False}
])

def mostrar_menu():
    print("\n[1] Solicitar impressão")
    print("[2] Organizar fila por prioridade")
    print("[3] Imprimir próximo arquivo")
    print("[4] Mostrar filas")
    print("[5] Contar arquivos")
    print("[6] Sair")

while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida!")
        continue

    if opcao == 1:
        nome = input("Nome do arquivo: ")

        try:
            paginas = int(input("Quantidade de páginas: "))
            admin = int(input("É administrador? (1=sim / 0=não): "))
        except ValueError:
            print("Erro nos dados.")
            continue

        if paginas <= 0 or admin not in (0, 1):
            print("Dados inválidos!")
            continue

        fila_geral.append({
            "nome_arquivo": nome,
            "paginas": paginas,
            "eh_admin": bool(admin)
        })

    elif opcao == 2:
        fila_prioritaria = sorted(
            fila_geral,
            key=lambda item: not item["eh_admin"]
        )

    elif opcao == 3:
        if not fila_prioritaria:
            print("Fila vazia!")
            continue

        item = fila_prioritaria.pop(0)
        tipo = "Administrador" if item["eh_admin"] else "Aluno"
        print(f"Imprimindo ({tipo}): {item['nome_arquivo']} - {item['paginas']} páginas")

    elif opcao == 4:
        print("\nFila geral:")
        if not fila_geral:
            print("Vazia")
        else:
            for item in fila_geral:
                tipo = "Administrador" if item["eh_admin"] else "Aluno"
                print(f"{tipo}: {item['nome_arquivo']} ({item['paginas']} páginas)")

        print("\nFila prioritária:")
        if not fila_prioritaria:
            print("Vazia")
        else:
            for item in fila_prioritaria:
                tipo = "Administrador" if item["eh_admin"] else "Aluno"
                print(f"{tipo}: {item['nome_arquivo']} ({item['paginas']} páginas)")

    elif opcao == 5:
        total_admin = sum(1 for item in fila_prioritaria if item["eh_admin"])
        total_aluno = sum(1 for item in fila_prioritaria if not item["eh_admin"])
        print(f"Administradores: {total_admin} | Alunos: {total_aluno}")

    elif opcao == 6:
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")

    print("=" * 40)