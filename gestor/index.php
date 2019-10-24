<?php

    session_start();

    $servidor = "localhost";
    $usuario = "root";
    $contraseña = "";
    $baseDeDatos = "gestor";

    //crear conexión
    $con = new mysqli($servidor, $usuario, $contraseña, $baseDeDatos);

    //revisar la conexión
    if ($con->connect_error) {
        if($con->connect_error == "Unknown database 'gestor'") {
            header("Location: acceso.php");
        } 
        die("Fallo en la conexión: " . $con->connect_error);
    } 

    //obtener token de accesso
    $sql = "SELECT * FROM token";
    $result = $con->query($sql);

    if ($result->num_rows > 0) {
        // obtener datos de cada fila
        while($row = $result->fetch_assoc()) {
            $token = $row["token_de_acceso"];
            break;
        }
    } else {
        echo "0 resultados";
        header("Location: acceso.php");
    }

    //cerrar conexión
    $con->close();

    //guardar el token de acceso en la sesión y redirigir a gestor.html
    $_SESSION["token_de_acceso"] = json_decode($token, true);
    header("Location: gestor.html");

?>