# Definición de la clase base Recibo
class Recibo:
    def __init__(self, emisor, fecha, monto):
        self.emisor = emisor
        self.fecha = fecha
        self.monto = monto

    def calcular_impuestos(self):
        pass

    def calcular_monto_bruto(self):
        return self.monto

# Definición de la clase Factura, que hereda de Recibo
class Factura(Recibo):
    def calcular_impuestos(self):
        return self.monto * 0.19

# Definición de la clase Boleta, que hereda de Recibo
class Boleta(Recibo):
    def calcular_impuestos(self):
        return 0  # No se considera IGV en las Boletas

# Definición de la clase ReciboHonorarios, que hereda de Recibo
class ReciboHonorarios(Recibo):
    def calcular_impuestos(self):
        return self.monto * 0.10

# Función para calcular el resumen de montos
def calcular_resumen(recibos):
    monto_total_neto = sum(recibo.calcular_monto_bruto() for recibo in recibos)
    monto_total_impuestos = sum(recibo.calcular_impuestos() for recibo in recibos)
    monto_total_bruto = monto_total_neto + monto_total_impuestos
    return monto_total_neto, monto_total_impuestos, monto_total_bruto

# Función para ingresar datos de un recibo desde el usuario
def ingresar_recibo():
    emisor = input("Ingrese el nombre del emisor: ")
    fecha = input("Ingrese la fecha del recibo (DD-MM-AAAA): ")
    monto = float(input("Ingrese el monto del recibo: "))
    tipo_recibo = input("Ingrese el tipo de recibo (Factura/Boleta/Honorarios): ")
    
    if tipo_recibo.lower() == "factura":
        return Factura(emisor, fecha, monto)
    elif tipo_recibo.lower() == "boleta":
        return Boleta(emisor, fecha, monto)
    elif tipo_recibo.lower() == "honorarios":
        return ReciboHonorarios(emisor, fecha, monto)
    else:
        print("Tipo de recibo no válido. Se creará un Recibo genérico.")
        return Recibo(emisor, fecha, monto)

# Ejemplo de uso
if __name__ == "__main__":
    recibos = []

    while True:
        opcion = input("¿Desea ingresar un recibo? (si/no): ")
        if opcion.lower() == "si":
            nuevo_recibo = ingresar_recibo()
            recibos.append(nuevo_recibo)
        elif opcion.lower() == "no":
            break
        else:
            print("Opción no válida. Por favor, ingrese 'si' o 'no'.")

    neto, impuestos, bruto = calcular_resumen(recibos)

    print(f"Monto Total Neto: {neto}")
    print(f"Monto Total de Impuestos: {impuestos}")
    print(f"Monto Total Bruto: {bruto}")
