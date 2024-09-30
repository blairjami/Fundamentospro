# Crear un diccionario llamado 'informacion_personal'
informacion_personal = {
    "nombre": "Blair Jami",   # Nombre ficticio de la persona
    "edad": 19,               # Edad de la persona
    "ciudad": "Quito",       # Ciudad inicial de la persona
    "profesion": "Estudiante"  # Profesión inicial de la persona
}

# Acceder al valor de la clave 'ciudad' y modificarla
informacion_personal["ciudad"] = "Cuenca"  # Cambiar la ciudad a 'Cuenca'

# Agregar una nueva clave-valor 'profesion'
# En este caso, actualizamos el valor de la profesión
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizar la profesión

# Verificar si la clave 'telefono' existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"  # Agregar un número de teléfono ficticio

# Eliminar la clave 'edad' ya que no es necesaria
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave 'edad' del diccionario

# Imprimir el diccionario final

print("Diccionario final:", informacion_personal)
