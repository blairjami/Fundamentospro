def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento y el total a pagar.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def main():
    # Primera llamada a la función
    monto1 = 100
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Monto total: ${monto1}, Descuento: ${descuento1}, Total a pagar: ${total1}")

    # Segunda llamada a la función con un porcentaje de descuento diferente
    monto2 = 200
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total2 = monto2 - descuento2
    print(f"Monto total: ${monto2}, Descuento: ${descuento2}, Total a pagar: ${total2}")

if __name__ == "__main__":
    main()
