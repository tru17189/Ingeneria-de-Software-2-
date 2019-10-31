Característica: Verificar un usuario 
    Reglas:

    - Un nombre que se relaciona con una contraseña.
    - La contraseña es el numero de carné.
    - Una contraseña unica 

    Antecedentes:
        -Tu número de carné dado por Iger, el cual no se deberia estar
        compartiendo con los demas. 

    Escenario: Nombre equivocado y número de carné correcto
        Dado a que en la base de datos no existen dos carnets iguales,
        no se continuara el proceso normal y se dara otra oportunidad
        al usuario de ingresar bien su nombre. 

    Escenario: Nombre y número de carné correcto 
        Se cargara la vista de libros que sea del mismo de grado del carné
        del usuario, por ejemplo "4to segundo semestre" y se obtendra la vista
        en donde el usuario puede escoger que libro desea leer. 

    Escenario: Nombre correcto y Número de carné equivocado
        Dado a que el carné es la parte mas importante en el proceso de
        autentificación, se obtendra una pantalla de error y se regresara
        al principio del proceso para que el usuario lo pueda volver a
        intentar.

    Escenario: Nombre Equivocado y Número de carné equivocado
        Dado a que el carné es la parte mas importante en el proceso de
        autentificación, se obtendra el mismo resultado que en el escenario
        anterior. 


