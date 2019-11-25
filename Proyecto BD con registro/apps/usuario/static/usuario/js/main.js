$(document).ready(function(){
    $("#formulario").validate({
        errorClass: "is-invalid",
        rules:{
            usuario:{
                required:true

            },
            pass:{
                
                required:true
                
            },

        },
        messages:{
            usuario:{
                required:"¡El usuario es requerido!"
            },
            pass:{
                required:"¡La contraseña es requerida!"
            },
            
        }
       
    })
})

$(document).ready(function(){
    $("#registro").validate({
        errorClass: "is-invalid",
        rules:{
            usuarior:{
                required:true

            },
            passr:{
                
                required:true
                
            },
            mailr:{
                required:true
            },

        },
        messages:{
            usuarior:{
                required:"¡El usuario es requerido!"
            },
            passr:{
                required:"¡La contraseña es requerida!"
            },
            mailr:{
                required:"¡El correo es requerido!"
            }
            
        }
       
    })
})

$("#registro").submit(function(){
    if($("#registro").valid()){
        console.log("valido")
    }else{
        console.log("no valido")
    }
    return false
})
