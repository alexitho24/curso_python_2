# ENTORNO VIRTUAL EN PYTHON
 
1. Abre una ventana de git
2. Instala la herramienta virtualenv si aún no la tienes instalada. Puedes hacerlo ejecutando el siguiente comando:
 
plaintext

pip install virtualenv
 
3.  Crea un nuevo directorio para tu proyecto y navega hasta él en la ventana de comandos utilizando el comando  cd  (por ejemplo,  cd C:\Users\tu_usuario\proyecto ).
4. Crea un nuevo entorno virtual ejecutando el siguiente comando:
 
plaintext

virtualenv nombre_del_entorno
 
 
Por ejemplo:
 
plaintext

virtualenv mi_entorno
 
5.  Activa el entorno virtual. Para ello, ejecuta el script de activación correspondiente en la carpeta  Scripts  del entorno virtual. El comando para activar el entorno virtual es:
 
plaintext

nombre_del_entorno\Scripts\activate
 
 
Utilizando el ejemplo anterior:
 
plaintext

mi_entorno\Scripts\activate
 
6.  Una vez activado el entorno virtual, verás que el prompt de la ventana de comandos cambia para indicar que estás dentro del entorno virtual.
 
