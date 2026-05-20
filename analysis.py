import json
from datetime import datetime


def cargar_ventas(ruta_archivo):
    """Lee el archivo JSON y devuelve la lista de ventas."""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos_ventas = json.load(archivo)

    return datos_ventas

def calcular_total_venta(venta):
    """Devuelve precio * cantidad para una venta."""
    return venta["precio"]*venta["cantidad"]

def ventas_por_categoria(ventas):
    """
    Agrupa las ventas por categoría.
    Devuelve un dict: { "categoria": total_euros }
    """
    ventas_agrupadas = {}
    for venta in ventas:
        categoria = venta["categoria"]
        total = calcular_total_venta(venta)
        
        ventas_agrupadas[categoria] = ventas_agrupadas.get(categoria, 0) + total
            
    return ventas_agrupadas

def producto_mas_vendido(ventas):
    """Devuelve el nombre del producto con mayor ingreso total."""
    mejor_producto = None
    max_ingreso = 0
    
    for venta in ventas:
        ingreso_actual = calcular_total_venta(venta)
        
        if ingreso_actual > max_ingreso:
            max_ingreso = ingreso_actual
            mejor_producto = venta["producto"]
            
    return mejor_producto

def ventas_en_fecha(ventas, fecha_str):
    """Filtra ventas de una fecha específica (formato YYYY-MM-DD)."""
    for venta in ventas:
        if venta["fecha"] == fecha_str:
            return venta

# Bloque de prueba
if __name__ == "__main__":      # Todavía me queda por entenderlo.
    
    ventas = cargar_ventas("ventas.json")
    
    print("Ventas por categoría:", ventas_por_categoria(ventas))

    print("Producto más vendido: ", producto_mas_vendido(ventas))

    print("Venta filtrada en una fecha, por ejemplo 2026-01-18 ", ventas_en_fecha(ventas, "2026-01-18"))
