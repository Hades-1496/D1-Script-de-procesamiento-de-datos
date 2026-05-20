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
    """Devuelve el nombre y el ingreso del producto con mayor ingreso total."""
    mejor_producto = None
    max_ingreso = 0
    
    for venta in ventas:
        ingreso_actual = calcular_total_venta(venta)
        
        if ingreso_actual > max_ingreso:
            max_ingreso = ingreso_actual
            mejor_producto = venta["producto"]
            
    return mejor_producto, max_ingreso

def ventas_en_fecha(ventas, fecha_str):
    """Filtra ventas de una fecha específica (formato YYYY-MM-DD)."""
    ventas_filtradas = []
    for venta in ventas:
        if venta["fecha"] == fecha_str:
            ventas_filtradas.append(venta)
    return ventas_filtradas

def formatear_moneda(valor):
    """Formatea un número a moneda europea (ej. 1.234,56 €)."""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " €" # Reemplazamos las , de los múltiplos
                                                                                        # que usan los estadounidenses para los
                                                                                        # múltiplos de 10^3 por una X antes de
                                                                                        # reemplazar la X, sustituye los . por ,
                                                                                        # y las X por .


def guardar_informe(datos, ruta):

    """Guarda un diccionario en formato JSON."""
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

    
def main():
    ventas = cargar_ventas("ventas.json")
    informe = "============================\n   INFORME DE VENTAS\n============================"
    informe +=f"\nTotal de ventas: {len(ventas)}"
    
    ingresos_totales = sum(calcular_total_venta(v) for v in ventas)
    informe +=f"\nIngresos totales: {formatear_moneda(ingresos_totales)}"
    
    print("\n--- Por categoría ---")
    for cat, total in ventas_por_categoria(ventas).items():
        # Alineamos el texto a la izquierda (<12) y el número a la derecha (>11)
        informe+=f"\n{cat + ':':<12} {formatear_moneda(total):>11}" # La reserva de caracteres es algo totalmente nuevo para mí.
        
    prod, max_ingreso = producto_mas_vendido(ventas)
    informe+=f"\n\nProducto más rentable: {prod} ({formatear_moneda(max_ingreso)})"
    
    fecha_busqueda = "2026-01-16"
    fecha_str = datetime.strptime(fecha_busqueda, "%Y-%m-%d").strftime("%d/%m/%Y") # Convierte la fecha en el dato 'datetime' y luego
                                                                                    #vuelve a convertirlo en string ocn un orden distinto. 
    informe+=f"\n\n--- Ventas del {fecha_str} ---"
    for venta in ventas_en_fecha(ventas, fecha_busqueda):
        informe+=f"\n- {venta['producto']+':':<10} {formatear_moneda(calcular_total_venta(venta)):>11}"


    print(informe)
    
    # Para no complicarnos la vida, simplificaremos el informe a unos datos con la ayuda 
    # de los datos extraidos antes de convertirlo en un sólo string
    datos_json = {
        "generado_en": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "total_ventas": len(ventas),
        "ingresos_totales": round(ingresos_totales, 2),
        "por_categoria": {cat: round(total, 2) for cat, total in ventas_por_categoria(ventas).items()},
        "producto_top": prod
    }
    guardar_informe(datos_json, "informe.json")

# Bloque de prueba
if __name__ == "__main__":
    main()
