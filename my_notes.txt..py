# Escritura de Archivo de Texto
# Creamos un archivo llamado my_notes.txt en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: Este es un recordatorio importante.\n")
    file.write("Nota 2: No olvidar comprar leche en el supermercado.\n")
    file.write("Nota 3: Reunión programada a las 3 PM mañana.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # Utilizamos strip() para eliminar el carácter de nueva línea al final de cada línea

# Cierre de Archivo
# No es necesario cerrar explícitamente el archivo ya que estamos utilizando el bloque 'with',
# que se encarga automáticamente de cerrar el archivo una vez se sale del bloque
