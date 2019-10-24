<?php

include "autenticar.php";

$archivoParaSubir = $_FILES["archivoParaSubir"];
$tituloDeDoc = $_POST["tituloDeDoc"];
$tituloDeDocPartes = explode(".", $tituloDeDoc);
array_pop($tituloDeDocPartes);
$tituloDeDoc = implode(".", $tituloDeDocPartes);


function subirArchivo($archivoParaSubir, $tituloDeDoc){

    $tokenDeAccesso = $_SESSION["token_de_acceso"];

    $cliente = inicarCliente();
    refrescarToken($cliente, $tokenDeAccesso);

    $tokenDeAccesso = $_SESSION['token_de_acceso'];

    $cliente->setAccessToken($tokenDeAccesso);
    $servicio = new Google_Service_Drive($cliente);

    $info = new finfo(FILEINFO_MIME);
    $tipoDeDoc = $info->file($archivoParaSubir["tmp_name"]);
    $mimeType = explode(";", $tipoDeDoc)[0];

    $metaDatos = new Google_Service_Drive_DriveFile(array('name' => $tituloDeDoc, "parents" => ["1l6H7zNvRz9N9qyTpZJdi2N_OhIpl6efm"])); // normalmente es algo así 1HeqmBX-1Lsy8dMAjmUY-Bjufvfsadf
    switch ($mimeType) {

        case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        case "application/vnd.openxmlformats-officedocument.wordprocessingml.template":     
        case "application/vnd.ms-word.document.macroEnabled.12":
        case "application/vnd.ms-word.template.macroEnabled.12":
        case "application/msword":
            $metaDatos->setMimeType("application/vnd.google-apps.document");
            break;

        case "application/vnd.openxmlformats-officedocument.spreadsheetml.template":
        case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":   
        case "application/vnd.ms-excel.sheet.binary.macroEnabled.12":   
        case "application/vnd.ms-excel.template.macroEnabled.12":
        case "application/vnd.ms-excel.sheet.macroEnabled.12":
        case "application/vnd.ms-excel.addin.macroEnabled.12":
        case "application/vnd.ms-excel":
            $metaDatos->setMimeType("application/vnd.google-apps.spreadsheet");
            break;  

        case "application/vnd.openxmlformats-officedocument.presentationml.presentation":
        case "application/vnd.openxmlformats-officedocument.presentationml.slideshow":  
        case "application/vnd.openxmlformats-officedocument.presentationml.template":   
        case "application/vnd.ms-powerpoint.presentation.macroEnabled.12":
        case "application/vnd.ms-powerpoint.slideshow.macroEnabled.12":
        case "application/vnd.ms-powerpoint.template.macroEnabled.12":
        case "application/vnd.ms-powerpoint.addin.macroEnabled.12":
        case "application/vnd.ms-powerpoint":
            $metaDatos->setMimeType("application/vnd.google-apps.presentation");
            break;  

        default:
            break;
    }

    $contenido = file_get_contents($archivoParaSubir["tmp_name"]);
    $archivo = $servicio->files->create($metaDatos, array(
        "data" => $contenido,
        "mimeType" => $mimeType,
        "uploadType" => "multipart",
        "fields" => "id")
    );

    $permiso = new Google_Service_Drive_Permission(array(
        'type' => 'anyone',
        'role' => 'writer',
    ));
    $compartir = $servicio->permissions->create(
        $archivo->id, $permiso, array('fields' => 'id'));

    return $archivo->id;
}

echo subirArchivo($archivoParaSubir, $tituloDeDoc);

?><br>