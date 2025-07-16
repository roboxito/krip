# Elegir la base de imagen 
FROM debian:12-slim 

# Actualizar paquetes y limpiar cache 
RUN apt update && \ 
    apt -y upgrade && \ 
    apt -y install python3 python3-cryptography python3-tk && \ 
    apt clean && \ 
    rm -rf /var/lib/apt/lists/* 

# Hacer que el usuario no sea root (opcional pero recomendado) 
RUN useradd -m krip
# Crear un directorio para tu aplicación 
RUN mkdir -p /app 
RUN chown krip:krip /app

# Cambiar al usuario creado 
USER krip 
# Copiar fuente 
COPY --chown=krip:krip krip.py /home/krip
COPY --chown=krip:krip inicia.sh /home/krip
COPY --chown=krip:krip .bash_aliases /home/krip

RUN chmod +x /home/krip/inicia.sh

#COPY . . 
#COPY krip.py . 

WORKDIR /app 

# Expresar el puerto si es necesario 
# EXPOSE 80 

#ENTRYPOINT ["bash","/home/krip/inicia.sh"]

# Comando para ejecutar tu aplicación 
#CMD ["python3", "/home/krip/krip.py","--help"] 
#CMD ["bash"]
CMD ["bash","/home/krip/inicia.sh"]
