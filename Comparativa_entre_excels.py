import openpyxl
import os
import subprocess

class inventarios_N:

    def __init__(self):
        pass
    def introducir_directorio(self):
        try:
            self.ask_directory = str(input("quieres moverte a un directorio ? (y/n): ")) # si seleccionas que no directamente dice que no se encuentra así que lo mejor es pulsar si
            if self.ask_directory.lower() == "y": # .lower() porque si pone mayusculas sin querer..., lo rebaja a minusculas
                self.directory = str(input(r"a que directorio quieres ir ej: 'C:\Users\...': ")) # importante sin cd porque os.chdir ya cambia de directorio solamente poner la ruta
                os.chdir(self.directory)

        except OSError as Directory_Error_system:
            print(f"no se ha podido encontrar o moverse a este diorectorio: {Directory_Error_system}")

    def introducir_excel(self):
        try:    
            self.tabla1 = openpyxl.load_workbook(input("introduce una tabla de excel [ej: nombre.xlsx + extensión]: ")) # esta función 'openpyxl.load_workbook' abre directamente el documento esta función no admite otro tipo de documento que no sea excels
            self.ask_save_directory = str(input("quieres crear una carpeta para guardarlo? (y/n): "))
            if self.ask_save_directory.lower() == "y":
                self.ask_name_directory = str(input("que nombre le quieres poner al directorio ?: "))
                os.mkdir(self.ask_name_directory)
                archive_name = str(input("cual es el nombre de tu archivo xlsx [incluie nombre + extensión]: "))
                self.new_rute = os.path.join(self.ask_name_directory, archive_name) # os.path.join() a parte de unir rutas como hace con el nuevo directorio lo que hace es que independientemente del sistema operativo lo que hace es diferenciar las rutas (separadores '\' '/') de otras maneras para que basicamente pueda leerlas el programa
                self.tabla1.save(self.new_rute)     # ponemos la ruta que especifica el user y el nombre del archivo que tiene que ser el mismo ya que si no se crea uno nuevo pero si lo pones bien se ponen los cambios en el nuevo directorio
            else:
                if self.ask_save_directory.lower == "n": # si eliges que 'no' lo guarda directamente en el directorio raíz
                    second_archive_name = str(input("cual es el nombre de tu archivo xlsx [incluie nombre + extensión]: "))
                    self.tabla1.save(second_archive_name) 
                

        except Exception as except_by_excels:
            print(f"{except_by_excels}")
            


if "__main__" == __name__:
    N = inventarios_N()
    N.introducir_directorio()
    N.introducir_excel()