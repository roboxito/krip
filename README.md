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

Puede cambiar la Llave de encriptamiento generando una nueva y colocandokla en el codigo fuente.

#key=Fernet.generate_key()
#print(key)
key=b'B69FxcWQKd5CCsaWTtxB4vkCiw3nZn09nSU3stgPqsg='

Copyleft (C) 2022 Jorge Lopez
