import platform
from datetime import datetime
import psutil
import time


def mostrar_recursos():
    cpu = psutil.cpu_percent()
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage("C:\\")
    

    print("Uso da CPU:", cpu, "%")
    print("Uso da RAM:", memoria.percent, "%")
    print("RAM total:", round(memoria.total / (1024 ** 3), 2), "GB")
    print("RAM disponível:", round(memoria.available / (1024 ** 3), 2), "GB")
    print("Uso do disco:", disco.percent, "%")
    print("Espaço total do disco:", round(disco.total / (1024 ** 3), 2), "GB")
    print("Espaço livre:", round(disco.free / (1024 ** 3), 2), "GB")

def monitorar_tempo_real():
    print("\nMonitoramento em tempo real")
    print("Pressione CTRL + C para voltar ao menu.\n")

    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            memoria = psutil.virtual_memory()

            print(f"CPU: {cpu}% | RAM: {memoria.percent}%")

    except KeyboardInterrupt:
        print("\nVoltando ao menu...")


print("================================")
print("      MONITOR DE SISTEMA")
print("================================")

print("Sistema operacional:", platform.system())
print("Computador:", platform.node())
print("Processador:", platform.processor())
print("Data e hora:", datetime.now())

def menu():
    while True:
        print("\n===== MONITOR DE SISTEMA =====")
        print("1 - Informações do computador")
        print("2 - Monitorar recursos")
        print("3 - Monitoramento em tempo real")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nSistema operacional:", platform.system())
            print("Computador:", platform.node())
            print("Processador:", platform.processor())

        elif opcao == "2":
            mostrar_recursos()

        elif opcao == "3":
            monitorar_tempo_real()

        elif opcao == "4":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")


menu()


    