<?php

include "autenticar.php";

function obtenerListaDeArchivos(){

    $tokenDeAccesso = $_SESSION["token_de_acceso"];

    $cliente = inicarCliente();
    refrescarToken($cliente, $tokenDeAccesso);

    $tokenDeAccesso = $_SESSION['token_de_acceso'];

    $opcionesDeHtml = "<option value=''>Seleccionar archivo...</option>";

    $cliente->setAccessToken($tokenDeAccesso);
    $servicio = new Google_Service_Drive($cliente);

    $tokenDePagina = null;
    $paramsOpcionales = array(
        "pageSize" => 100,
        "pageToken" => $tokenDePagina,
        "q" => "'1l6H7zNvRz9N9qyTpZJdi2N_OhIpl6efm' in parents and trashed != true" // normalmente es algo como 1HeqmJX-1Lsy89CXljmUY-BjubbjfkpsSm
    );

    try {

        do {

            $optParams["pageToken"] = $tokenDePagina;
            $archivos = $servicio->files->listFiles($paramsOpcionales);
            $tokenDePagina = $archivos->nextPageToken;

            foreach ($archivos as $archivo ) {
                $opcionesDeHtml .= "<option value='".$archivo->id.",".$archivo->mimeType."'>".$archivo->name."</option>";
            }

        } while($tokenDePagina);

    } catch(Exception $e) {

        $msjDeError = $e->getMessage();

        if(strpos($msjDeError, "Internal Error") !== false) {
            sleep(2);
            $archivos = $servicio->files->listFiles($paramsOpcionales);
            $tokenDePagina = $driveFiles->nextPageToken;
            foreach ($drivefiles as $file ) {
                $opcionesDeHtml .= "<option value='".$archivo->id."'>".$archivo->name."</option>";
            }
        } else {
            print $msjDeError;
        }
    }

    return $opcionesDeHtml;

}

echo obtenerListaDeArchivos();

?>