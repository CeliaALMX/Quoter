#    Diagrama de flujo del proyecto "COTIZADOR 1.0".

En este apartado se mostrará el proceso que se llevó a cabo para poder desarrollar el diagrama de flujo del proyecto cotizador con la versión 1.0.

##  Descripción del diagrama de flujo.

El diagrama que se mostrará a continuación fue desarrollado en Lucidchart, el objetivo de este diagrama de flujo es visualizar las funciones que se planea que haga el programa que desarrollaremos.

### 🚩 Inicio. 

Este es el comienzo del diagrama de flujo y lo primero que hace es solicitar al usuario "persona que este usando el programa" que le solicite al comprador "persona que esté interesado en una cotización" los datos que se muestran en el proceso "rectángulo".


![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.0.PNG)


Posteriormente el diagrama de flujo arroja una decisión lo cual quiere decir que dependiendo de su respuesta arrojara otro procedimiento y otras indicaciones. La decisión es la siguiente "verificar que en la base de datos no exista un comprador" esto lo va a hacer por medio de una búsqueda, buscando los campos de:
#Nombre 
#Apellido
#Dirección
#Empresa 
#Correo electrónico 
Una vez que se hay verificado esos datos el usuario "persona que este usando el programa" se le aparece un mensaje según sea el resultado de la búsqueda que realizo el programa, si no encontró algún usuario con esos datos arrojara un mensaje diciendo que no existe un usuario con esos datos. Posteriormente indica que puede guardar al usuario nuevo.
Por otro lado, si en la búsqueda arroja que si existe un usuario con esos datos le solicitara al usuario "persona que este usando el programa" que debe rectificar los datos que coloco debido a que ya hay un usuario con esos datos.


![](https://github.com/CeliaALMX/Quote/blob/main/IMAGEN_1.1.PNG)


Después de esa decisión el programa va a generar una orden de compra la cual va a llevar un folio con la finalidad de ver cuantas cotizaciones se han creador.


![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.2.PNG)


Posteriormente el usuario "persona que este usando el programa" le solicitara al comprador "persona que esté interesada en una cotización" los datos que se muestran en el proceso "rectángulo" con la finalidad de que se pueda ir creando una cotización y una lista de precios.


![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.3.PNG)


Una vez que el usuario finalice, se le mostrara una tabla en la que le aparecerán todas las piezas seleccionadas junto con su precio.


![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.4.PNG)


Posteriormente a eso se nos aparecerá la segunda decisión del diagrama de flujo en donde nos dirá que tendrá que verificar que cada pieza seleccionada este en existencia en el inventario del almacén. 
Si la respuesta es sí, restara “-N restara la cantidad de piezas que haya seleccionado el usuario" al producto seleccionado de las piezas totales que haya en almacén.
Y si la respuesta fue no, lo cual significa que no hay ninguna pieza en almacén, el programa tendrá que mandar un mensaje al usuario "persona que este usando el programa" diciendo lo siguiente "esa "t pieza" pieza seleccionada", por el momento no está disponible" y el usuario "persona que este usando el programa" tendrá que decirle al comprador "persona que esté interesada en una cotización" y que se maneja sobre pedido.
Posterior a eso aparece otra decisión en el diagrama e indica que se le debe preguntar al comprador "persona que esté interesada en una cotización" si aun así la quiere, dependiendo de su respuesta será el siguiente paso por hacer.
Si la respuesta fue si, el programa hará una orden de pedido y pasará al siguiente paso.
De lo contrario el programa mandara un mensaje al usuario para indicarle que le ofrezca las piezas que haya en almacén.


![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.5.PNG)


Una vez finalizado eso el usuario "persona que este usando el programa" deberá colocar el porcentaje de descuento o incremento sobre el precio de todos y cada una de las piezas seleccionadas.

![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.6.PNG)

Luego el programa levantara una orden de compra.


![](https://github.com/CeliaALMX/Quote/blob/main/imagen_1.7.PNG)


Finalmente, en la siguiente imagen se muestra la ultima parte del diagrama de flujo el cual es una decisión e indica que se debe esperar la autorización del comprador "persona interesada en la cotización". 
Si la respuesta del comprador fue si se procederá a seguir al siguiente paso.
De lo contrario con base a su respuesta se vera si se pasa al siguiente paso o si se archiva su cotización del comprador "persona interesada en una cotización". Posterior a eso se dará un lapso de 30 días como tiempo de espera para que el comprador "persona interesada en la cotización" envíe una respuesta y una vez terminado los 30 días se archivara su cotización.


![](https://github.com/CeliaALMX/Quote/blob/VENTURA-Eduar-patch-1/imagen_1.9.PNG)
