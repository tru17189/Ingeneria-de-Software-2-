function listarArchivos(){

  var solicitud = new XMLHttpRequest();
  solicitud.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("listaDeArchivos").innerHTML = this.responseText;
        document.getElementById("listaDeArchivos").disabled = false;
    }
  };
  solicitud.open("GET", "listar.php", true);
  solicitud.send();

}

function editarArchivo(){

    var elDoc = document.getElementById("listaDeArchivos").value;
    var idDeDoc = elDoc.split(",")[0];
    var tipoDeDoc = elDoc.split(",")[1];
    if(idDeDoc){
        document.getElementById("descargar").disabled = false;
    } else{
        document.getElementById("descargar").disabled = true;
    }

    var altura = (window.innerHeight / 3);
    altura = altura * 2;

    var url;
    if(tipoDeDoc === "application/vnd.google-apps.document"){

        url = "https://docs.google.com/document/d/"+idDeDoc+"?rm=demo";

    } else if(tipoDeDoc === "application/vnd.google-apps.spreadsheet"){

        url = "https://docs.google.com/spreadsheets/d/"+idDeDoc+"?rm=demo";

    } else if(tipoDeDoc === "application/vnd.google-apps.presentation"){

        url = "https://docs.google.com/presentation/d/"+idDeDoc+"?rm=demo";

    } else {

        url = "https://drive.google.com/file/d/"+idDeDoc+"/preview";

    }
    document.getElementById("editarArchvio").setAttribute("src", url);  
}

function descargarArchivo(){

    document.getElementById("descargar").style.display = "none";
    document.getElementById("circuloEspera").style.display = "initial";

    var elDoc = document.getElementById("listaDeArchivos").value;
    var idDeDoc = elDoc.split(",")[0];
    var tipoDeDoc = elDoc.split(",")[1];
    var tituloDeDoc = document.getElementById("listaDeArchivos").options[document.getElementById("listaDeArchivos").selectedIndex].text;

    var solicitud = new XMLHttpRequest();   
    solicitud.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

            console.log(this.responseText);
            document.getElementById("descargar").style.display = "initial";
            document.getElementById("circuloEspera").style.display = "none";

            var a = document.createElement('a');
            a.href = this.responseText;
            a.download = (this.responseText).substr(2);
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }
    };
    solicitud.open("POST", "descargar.php", true);
    solicitud.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    solicitud.send("idDeDoc="+idDeDoc+"&tipoDeDoc="+tipoDeDoc+"&tituloDeDoc="+tituloDeDoc);

}

function subirArchivo(){

    document.getElementById("nombreDeArchivo").style.display = "none";
    document.getElementById("circuloEsperaDos").style.display = "block";

    var elDoc = document.getElementById("nuevoArchivoInput");
    var path = elDoc.value.split("\\"); 
    var tituloDeDoc = path[path.length -1];

    var formData = new FormData();
    formData.append("archivoParaSubir", elDoc.files[0]);
    formData.append("tituloDeDoc", tituloDeDoc);

    var solicitud = new XMLHttpRequest();   
    solicitud.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

            console.log(this.responseText);
            document.getElementById("nombreDeArchivo").style.display = "block";
            document.getElementById("nombreDeArchivo").innerHTML = "Archvio subido";
            document.getElementById("circuloEsperaDos").style.display = "none";
            listarArchivos();
        }
    };
    solicitud.open("POST", "subir.php", true);
    solicitud.send(formData);
}

document.addEventListener("DOMContentLoaded", function(event) {

    listarArchivos();

    document.getElementById("listaDeArchivos").addEventListener("change", function(){
        editarArchivo();
    });

    document.getElementById("descargar").addEventListener("click", function(){
        descargarArchivo();
    });

    document.getElementById("subirArchivo").addEventListener("click", function(){
        document.getElementById("popup").style.display = "block";
    });

    document.getElementById("popup").addEventListener("click", function(e){
        if(e.target === document.getElementById("popup")){
            document.getElementById("popup").style.display = "none";
        }       
    });

    document.getElementById("nuevoArchivoInput").addEventListener("change", function(){
        var path = (this.value).split("\\");
        document.getElementById("nombreDeArchivo").innerHTML = path[path.length - 1];
    });

    document.getElementById("nuevoArchivo").addEventListener("click", function(){
        subirArchivo();
    });

});