function valida_envia() {
    //validar el nombre
    if (document.valida.nombre.value.length == 0) {
        alert("Tiene que escribir su nombre completo.")
        document.valida.nombre.focus()
        return 0;
        }
    //validar el motivo de la consulta
    if (document.valida.motivo.selectedIndex== 0) {
         alert("Debe seleccionar un curso.")
         document.valida.motivo.focus()
        return 0;
        }
        //validar el mensaje
    if (document.valida.mensaje.value.length == 0) {
        alert("Recuerde escribir su mensaje.")
         document.valida.mensaje.focus()
        return 0;
        }

    alert("Muchas gracias por enviar el formulario.");
    document.valida_envia.submit();}

    //validar el correo
    function pruebaemail (email){
        re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
        if(!re.exec(email)){
            alert('email no valido');
            return 0;
        } }