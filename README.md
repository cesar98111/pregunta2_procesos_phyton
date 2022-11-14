### generacion de procesos en phyton

* En primer lugar cree un main en el cual tengo un if que ejecutara un codigo segun el sistema operativo gracias a platform

* En ambos caso cree un proceso con subprocess pasandolo como parametro el comando ping y lanzandolo con start

* para poder capturar la salida ejecutamos la funcion stdout pero como nos la devuelve en bytes la decodificamos con la funcion decode

* para leerla mejor hacemos los tratamientos necesarios con el String resultante para que podamos leer la informacion mas comodamente

* tanto window como linux el codigo es identico lo unico que cambia es que en el comando ping para decirle el numero de paquetes en
linux es -c y windows -n
