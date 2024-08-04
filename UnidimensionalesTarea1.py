def obtener_temperaturas():
    
    cantidad = int(input("¿Cuántas temperaturas desea ingresar? "))
   
    temperaturas = []
   
    for i in range(cantidad):
        temp = float(input(f"Ingresa la temperatura #{i + 1}: "))
        temperaturas.append(temp)
    
    return temperaturas

def calcular_media(temperaturas):
   
    return sum(temperaturas) / len(temperaturas)

def contar_superiores_o_iguales_a_media(temperaturas, media):
    
    return sum(1 for temp in temperaturas if temp >= media)

def main():
    temperaturas = obtener_temperaturas()
    media = calcular_media(temperaturas)
    cantidad_superiores_o_iguales = contar_superiores_o_iguales_a_media(temperaturas, media)
    
    
    print(f"\nLa media de las temperaturas es: {media:.2f}")
    print(f"Cantidad de temperaturas superiores o iguales a la media: {cantidad_superiores_o_iguales}")

if __name__ == "__main__":
    main()