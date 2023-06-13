document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("form_insertar").addEventListener("submit", function(event){
        event.preventDefault();
        var data ={
            documento : document.getElementById("documento").value,
            nombre : document.getElementById("nombre").value,
            apellido : document.getElementById("apellido").value,
            correo : document.getElementById("correo").value,
            telefono : document.getElementById("telefono").value,
            direccion : document.getElementById("direccion").value,
            genero : document.getElementById("genero").value,
        };

        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertar",{
            method:"POST",
            body:jsonData,
            headers:{
                "Content-Type":"AppBanco/json"
            }
        })//.then(Response.JSON())
        .then(response => response.json())
        .then(datos =>{
            console.log(datos)
        })
        .catch(console.error())
    });
});