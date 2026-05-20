# # Python
# nombre = "Ada"
# edad = 28
# precio = 9.99
# activo = True
# nada = None
 
# print(type(nombre))  # <class 'str'>
# print(type(edad))    # <class 'int'>

# nombre = "Claude"
# apellido = "AI"

# # Concatenación
# saludo = nombre + " " + apellido

# # Template literals → f-strings
# mensaje = f"Hola, soy {nombre} {apellido}"

# # Métodos comunes
# print(nombre.upper())       # CLAUDE
# print(nombre.lower())       # claude
# print(nombre.replace("C", "K"))  # Klaude
# print(len(nombre))          # 6
# print("Clau" in nombre)    # True // Importan las mayúsculas.

# frutas = ["manzana", "pera", "naranja"]

# # Acceso por índice
# print(frutas[0])    # manzana
# print(frutas[-1])   # naranja (desde el final)

# # Slicing (no existe en JS)
# print(frutas[0:2])  # ["manzana", "pera"]

# # Métodos
# frutas.append("fresa")     # .push()
# frutas.pop()               # .pop()
# frutas.insert(1, "uva")    # .splice(1, 0, "uva")
# print(len(frutas))         # .length

# # Iterar
# for fruta in frutas:
#     print(fruta)

# # JavaScript: const persona = { nombre: "Ana", edad: 30 }
# persona = {
#     "nombre": "Ana",
#     "edad": 30,
#     "activo": True
# }
 
# # Acceso
# print(persona["nombre"])       # Ana = persona.nombre
# print(persona.get("ciudad", "desconocido"))  # valor por defecto
 
# # Modificar
# persona["edad"] = 31
# persona["ciudad"] = "Madrid"
 
# # Iterar
# for clave, valor in persona.items():
#     print(f"{clave}: {valor}")
 
# # Comprobar existencia
# if "nombre" in persona:
#     print("tiene nombre")

# # JavaScript                    # Python
# # if (x > 5) {                  if x > 5:
# #   console.log("mayor")            print("mayor")
# # } else if (x === 5) {         elif x == 5:
# #   console.log("igual")            print("igual")
# # } else {                      else:
# #   console.log("menor")            print("menor")
# # }

# # Operadores lógicos
# # JS: && || !
# # Python: and or not

# edad = 25
# if edad >= 18 and edad < 65:
#     print("adulto en activo")


# # for...of → for in
# colores = ["rojo", "verde", "azul"]
# for color in colores:
#     print(color)
 
# # range (equivalente a for con índice)
# for i in range(5):        # 0, 1, 2, 3, 4
#     print(i)
 
# for i in range(1, 6):    # 1, 2, 3, 4, 5
#     print(i)
 
# # while (igual que en JS)
# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1
 
# # List comprehension (muy pythónico, no existe en JS)
# cuadrados = [x**2 for x in range(10)]
# # Equivale a: const cuadrados = Array.from({length:10}, (_,i) => i**2)

# # Definición
# def saludar(nombre, saludo="Hola"):  # parámetro con valor por defecto
#     return f"{saludo}, {nombre}!"
 
# print(saludar("Ana"))           # Hola, Ana!
# print(saludar("Bob", "Hey"))   # Hey, Bob!
 
# # Argumentos con nombre (keyword arguments)
# print(saludar(saludo="Buenos días", nombre="Carlos"))
 
# # *args y **kwargs (como ...rest y objetos en JS)
# def suma(*numeros):
#     return sum(numeros)
 
# print(suma(1, 2, 3, 4))  # 10

