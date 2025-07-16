# krip
Encriptar, desencriptar y visualizar cadenas o archivos

Utileria para encriptar, desencriptar y visualizar cadenas o archivos de texto de forma visual y sencilla, multiplataforma.

## Ejecución en Linux: (ubuntu 24.x)
* sudo apt install python3-tk
* sudo apt install venv
* python3 -m venv krip
* cd krip
* source bin/activate
* pip install cryptography
* python krip.py

Compatible con python en windows

![image](https://github.com/user-attachments/assets/626acf9d-ca35-4d8c-9285-e4784d31d582)

### Puede cambiar la Llave de encriptamiento generando una nueva y colocandola en el codigo fuente.

* key=Fernet.generate_key()
* print(key)
* key=b'B69FxcWQKd5CCsaWTtxB4vkCiw3nZn09nSU3stgPqsg='

# krip-cli
Se agregaron parametros para su ejecución desde la linea de comandos:

$ krip --help
Copyleft (C) 2022 Jorge Lopez roboxito@gmail.com 
python3 /home/krip/krip.py [comando] 
  comandos: 
     e "<cadena>" - Encripta la cadena y la convierte a base64 
     d "<cadena>" - Decodifica la cadena de base64, y la desencripta 
     a <archivo> - Encripta el archivo y le agregar la extension .enc 
     u <archivo.enc> - Desencripta el archivo .enc y le remueve la entension .enc 
     l <archivo.enc> - Desencripta el archivo .enc, y lo despliega en la salida estandar de consola 
Uso con docker: $ mkdir app  
                $ docker run -it -v ./app:/app krip-cli bash 
                krip@eq:/app$ krip --help 

Ejemplos:
krip@7d270401e81b:/app$ krip e "hola mundo" 

Encriptado: 
gAAAAABodztaCLOjH23TvQXC5CqNtKtxkRK66sHaHpJWXl4uQ4oiT9Yhn7aN1-byj4WRb53mTdC7oT9AAgOOtwyOF2LPwGEuww==  

krip@7d270401e81b:/app$ krip d "gAAAAABodztaCLOjH23TvQXC5CqNtKtxkRK66sHaHpJWXl4uQ4oiT9Yhn7aN1-byj4WRb53mTdC7oT9AAgOOtwyOF2LPwGEuww== " 

Desencriptado: 
hola mundo  


Copyleft (C) 2022 Jorge Lopez
