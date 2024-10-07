# Escritura en el archivo 'my_notes.txt'
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("1. Estudiar Python es interesante.\n")
    file.write("2. Quiero mejorar en programación todos los días.\n")
    file.write("3. Disfruto aprendiendo nuevas tecnologías.\n")

    # El archivo se cierra automáticamente al salir del bloque 'with'

# Lectura del archivo 'my_notes.txt'
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea utilizando readline()
    line = file.readline()  # Leer la primera línea
    while line:
        print(line.strip())  # Mostramos la línea en consola sin saltos de línea adicionales
        line = file.readline()  # Leer la siguiente línea

    # El archivo se cierra automáticamente al salir del bloque 'with'
