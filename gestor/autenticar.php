<?php session_start(); 

function inicarCliente(){

    //incluir la liberería de php de Google API
    require_once "../google-api-php-client-2.1.3/vendor/autoload.php"; 

    //definir los permisos necesarios 
    $scopes = array("https://www.googleapis.com/auth/drive");

    //crear el objeto de cliente de Google
    $cliente = new Google_Client(); 
    $cliente->setRedirectUri('http://' . $_SERVER['HTTP_HOST'] . '/gestor/acceso.php');
    $cliente->setAuthConfig("client_secret.json");
    $cliente->addScope($scopes);
    $cliente->setAccessType('offline');

    return $cliente;

}

function refrescarToken($cliente, $tokenDeAccesso){

    $tokenExpirado = $cliente->isAccessTokenExpired();
    if($tokenExpirado){
        $cliente->refreshToken($tokenDeAccesso["refresh_token"]);
    }

    $_SESSION["token_de_acceso"] = $cliente->getAccessToken(); 
}

?>