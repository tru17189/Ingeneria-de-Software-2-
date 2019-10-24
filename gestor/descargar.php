<?php

include "autenticar.php";

$idDeDoc = $_POST["idDeDoc"];
$tituloDeDoc = $_POST["tituloDeDoc"];
$tipoDeDoc = $_POST["tipoDeDoc"];

function descargarArchivo($idDeDoc, $tipoDeDoc, $tituloDeDoc){

    $tokenDeAccesso = $_SESSION["token_de_acceso"];

    $cliente = inicarCliente();
    refrescarToken($cliente, $tokenDeAccesso);

    $tokenDeAccesso = $_SESSION['token_de_acceso'];

    $cliente->setAccessToken($tokenDeAccesso);
    $servicio = new Google_Service_Drive($cliente);

    if($tipoDeDoc == "application/vnd.google-apps.document") {

        $ext = ".docx";
        $format = "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
        $googleDoc = true;

    } else if($tipoDeDoc == "application/vnd.google-apps.spreadsheet"){

        $ext = ".xlsx";
        $format = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";
        $googleDoc = true;

    } else if($tipoDeDoc == "application/vnd.google-apps.presentation"){

        $ext = ".pptx";
        $format = "application/vnd.openxmlformats-officedocument.presentationml.presentation";
        $googleDoc = true;

    } else {

        $ext = ".".explode("/", $tipoDeDoc)[1];
        $googleDoc = false;

    }

    if($googleDoc){
        $archivo = $servicio->files->export($idDeDoc, $format, array('alt' => 'media'));
    } else {
        $archivo = $servicio->files->get($idDeDoc, array('alt' => 'media'));
    }

    $exportacion = fopen($tituloDeDoc.$ext, "w+");
    fwrite($exportacion, $archivo->getBody());
    fclose($exportacion);

    return dirname($tituloDeDoc.$ext)."/".$tituloDeDoc.$ext;
}

echo descargarArchivo($idDeDoc, $tipoDeDoc, $tituloDeDoc);

?>