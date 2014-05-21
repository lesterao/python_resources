from ftplib import FTP

def writeline(line):
    file.write(line + "\n")
elftp=raw_input("FTP:")
userx=raw_input("Usuario:")
passwd=raw_input("Password:")
try:
    ftp = FTP(elftp,userx,passwd)
    print ftp.getwelcome()
    print "Conectado!!!"
    while 1:
        print "v. - Ver archivos y directorios."
        print "a. - Acceder a un Directorio."
        print "r. - Renombrar Archivo - Directorio."
        print "ed. - Eliminar Directorio."
        print "ef. - Eliminar Directorio."
        print "d. - Crear Directorio."
        print "t. - Peso del Archivo."
        print "p. - Ver el Camino(path)"
        print "o. - Obtener Archivo Linea por Linea."
        print "s. - Subir Fichero"
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
            remes=raw_input("Nuevo nombre:")
            ftp.rename(rename, renames)
            print "\n",rename, "Renombreado a", renames,"."    
        elif opcion=='ed':
            deldir=raw_input("Directorio a Borrar:")
            ftp.rmd(deldir)
            print "Directorio",deldir,"Eliminado."
        elif opcion=='ef':
            delfic=raw_input("Fichero a Borrar:")
            ftp.delete(delfic)
            print "Fichero",delfic,"Eliminado."
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
        elif opcion=='s':
            fichero_origen=raw_input("Archivo a subir:")
            fichero_destino=fichero_origen
            try:
                f = open(fichero_origen, 'rb')
                ftp.storbinary('STOR ' + fichero_destino, f)
            except:
                print "No se ha podido encontrar el fichero " + fichero_origen  
        elif opcion=='q':
            ftp.quit()
            break;
except:
    print "No se ha podido conectar al servidor " 

