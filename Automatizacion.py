import os
import telnetlib
from ftplib import FTP
from time import sleep

def generarArchivo():
    usuario = "rcp";
    password = "rcp";
    direccionIP = input("Ingresa la dirección IP del router: ");
    # Se realiza la comunicación por medio del protocolo TELNET
    tn = telnetlib.Telnet(direccionIP);
    tn.read_until(b"User:");
    tn.write(usuario.encode('ascii') + b"\n");
    tn.read_until(b"Password:");
    tn.write(password.encode('ascii') + b"\n");
    # Se hacen los ajustes de la configuración
    tn.write(b"en\n");
    tn.write(b"config\n");
    tn.write(b"copy run start\n");
    tn.write(b"service ftp\n");
    tn.write(b"exit\n");
    tn.write(b"exit\n");
    tn.write(b"exit\n");
    print(tn.read_all().decode('ascii'));
    print("Se generó el archivo de configuración correctamente");
    sleep(2);

def descargarArchivo():
    direccionIP = input("Ingresa la dirección IP del router: ");
    ftp = FTP(direccionIP);
    ftp.login(user="rcp",passwd="rcp");
    try:
        file = open("startup-config.txt", 'wb');
        ftp.retrbinary('RETR %s' % "startup-config", file.write); #Se descarga el archivo de configuración
        print("Se ha descargado el archivo de configuración correctamente");
        sleep(2);
    except:
        print("Ocurrió un error al descargar el archivo");
    ftp.quit();

def mandarArchivo():
    direccionIP = input("Ingresa la dirección IP del router: ");
    ftp = FTP(direccionIP);
    ftp.login(user="rcp",passwd="rcp");
    file = open('startup-config.txt', 'rb');
    ftp.storbinary('STOR startup-config', file);
    file.close();
    print("Se envio el archivo correctamente");
    sleep(2);
    ftp.quit();

while(True):
    os.system("clear");
    print("Practica 4. ");
    print("Muñoz Carbajal Carlos Eduardo")
    print("4CM13");
    print("1. Generar archivo de configuración");
    print("2. Descargar documento de configuración");
    print("3. Enviar documento de configuración");
    opt = input("Selecciona una opción: ");
    match opt:
        case "1":
            generarArchivo();
        case "2":
            descargarArchivo();
        case "3":
            mandarArchivo();


