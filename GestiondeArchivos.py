class Archivo:
    def __init__(self, nombre_archivo, contenido):
        """
        Constructor: Se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos y abre un archivo para escribir.
        """
        self.nombre_archivo = nombre_archivo
        self.contenido = contenido
        self.archivo = open(self.nombre_archivo, 'w')  # Abrimos el archivo para escribir
        print(f"[INFO] Archivo '{self.nombre_archivo}' creado.")
        self.archivo.write(self.contenido)  # Escribimos el contenido en el archivo

    def mostrar_info(self):
        """
        Método que muestra información del archivo.
        """
        print(f"Archivo: {self.nombre_archivo}")
        print(f"Contenido: {self.contenido}")

    def __del__(self):
        """
        Destructor: Se ejecuta automáticamente cuando el objeto es eliminado.
        Se usa para cerrar el archivo y liberar recursos.
        """
        if self.archivo:
            self.archivo.close()
            print(f"[INFO] Archivo '{self.nombre_archivo}' cerrado correctamente.")

# Uso del programa
if __name__ == "__main__":
    archivo1 = Archivo("ejemplo.txt", "Este es el contenido del archivo.")
    archivo1.mostrar_info()

    # Eliminamos el objeto manualmente (en la práctica, esto sucede automáticamente al final del programa)
    del archivo1

