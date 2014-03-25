from ftplib import FTP
def writeline(line):
    file.write(line + "\n")
elftp=raw_input("FTP:")
userx=raw_input("Usuario:")
passwd=raw_input("Password:")
ftp = FTP(elftp,userx,passwd)
print ftp.getwelcome()
print "Conectado !"
while 1:
    print "v. - Ver archivos y directorios."
    print "a. - Acceder a un Directorio."
    print "r. - Renombrar Archivo - Directorio."
    print "e. - Eliminar Directorio."
    print "d. - Crear Directorio."
    print "t. - Peso del Archivo."
    print "p. - Ver el Camino(path)"
    print "o. - Obtener Archivo Linea por Linea."
    print "c. - Cambiar Directorio /dir/dir"
    print "q. - Quit"   
    opcion=raw_input("Opcion:")
    if opcion=='v':
        ftp.dir()
    elif opcion=='a':
        dire=raw_input("Directorio:")
        ftp.cwd(dire)
        print "Dentro de:", dire
    elif opcion=='r':
            rename=raw_input("Nombre:")
            renames=raw_input("Nuevo nombre:")
            ftp.rename(rename, renames)
            print "\n",rename, "Renombreado a", renames,"."    
    elif opcion=='e':
        deldir=raw_input("Directorio a Borrar:")
        ftp.rmd(deldir)
        print "Directorio",deldir,"Eliminado."
    elif opcion=='d':
        credir=raw_input("Nuevo Directorio:")
        ftp.mkd(credir)
        print "Directorio",credir,"Creado."
    elif opcion=='t':
        fel=raw_input("Archivo:")
        print "Peso:", ftp.size(fel), "KB"
    elif opcion=='p':
         print ftp.pwd();
    elif opcion=='c':
         fel=raw_input("Path:")     
         ftp.cwd(fel)
    elif opcion=='o':
         fel=raw_input("Archivo:")
         file = open(fel, "w")
         ftp.retrlines("retr " + fel, writeline)
    elif opcion=='q':
         ftp.quit()
         break;
