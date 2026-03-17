import time
from datetime import datetime
#Sistema Bancario para transferencias con delay
# 1. Configuracion inicial de las cuentas
cuenta_A = {"titular": "Marlon", "saldo": 5000.0, "historial": []}
cuenta_B = {"titular": "Samuel", "saldo": 80000.0, "historial": []}

def registrar_movimiento(cuenta,tipo,monto):
    # Se guarda la fecha y hora exacta de la transferencia
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    movimiento = f"{fecha_actual} | {tipo}: ${monto: .2f}"
    cuenta["historial"].append(movimiento)

while True:
    print("\n--- SIMULADOR BANCARIO ---")
    print("1. Ver saldos ({cuenta_A['titular']} vs {cuenta_B['titular']}).")
    print("2. Transferir de Marlon a Samuel.")
    print("3. Transferir de Samuel a Marlon.")
    print("4. Ver historial de movimientos.")
    print("5. Salir")

    opcion = input("\n Bienvenido, seleccione una opcion porfavor: ")

    if opcion in ["2", "3"]:
        # Se define quien envia y quien recibe segun la opcion
        origen = cuenta_A if opcion == "2" else cuenta_B
        destino = cuenta_B if opcion == "2" else cuenta_A

        try:
            monto = float(input(f" ¿Cuanto desea transferir desde {origen ['titular']}?: "))

            # Validar si el saldo es suficiente
            if monto < 0:
                print(" EL monto debe ser mayor a 0 ")
            elif monto > origen["saldo"]:
                print(f" Fondos insuficientes. Saldo actual: $ {origen['saldo']}")
            else:
                # --- PROCESO DE TRANSFERENCIA ---
                print(f"\n Conectando con el servidor de {origen['titular']}...")
                time.sleep(4) # Simulacion de delay

                origen["saldo"] -= monto
                destino["saldo"] += monto

                # Registrar la transferencia en ambos historiales
                registrar_movimiento(origen, f" Envio a {destino['titular']}",monto)
                registrar_movimiento(destino, f" Recepcion de {origen['titular']}",monto)

                print(f" ¡Transferencia exitosa de ${monto}! ")

        except ValueError:
            print(" Error: Por favor, ingrese un numero valido para el monto ")

    elif opcion == "1":
        print(f"\n SALDOS ACTUALES: ")
        print(f"{cuenta_A['titular']}: ${cuenta_A['saldo']:.2f}")
        print(f"{cuenta_B['titular']}: ${cuenta_B['saldo']:.2f}")
    
    elif opcion == "4":
        titular = input(" ¿De que titular desea ver el historial? (Marlon/Samuel): ")
        cuenta = cuenta_A if titular == "Marlon" else cuenta_B

        print(f"\n HISTORIAL DE {cuenta['titular'].upper()}: ")
        if not cuenta["historial"]:
            print(" No hay movimientos registrados. ")
        for mov in cuenta["historial"]:
            print(mov)

    elif opcion == "5":
        print(" Saliendo del Banco, buen dia.")
        break

    else:
        print(" Opcion no valida. ")




