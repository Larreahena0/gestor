function delete1(id) {
    window.event.preventDefault();
    $.confirm({
        boxWidth: '400px',
        useBootstrap: false,
        closeIcon: true,
        title: '¿Está seguro?',
        content: 'El semillero no podra ser restaurado',
        typeAnimated: true,
        buttons: {
            somethingElse: {
                text: 'Seguro',
                btnClass: 'btn-warning',
                action: function(){
                    let url = window.location;
                    const postData={
                        'id': id,
                        'caso':"eliminar",
                        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                    };
                    $.post(url, postData, function(response){
                        $.alert({
                            boxWidth: '400px',
                            useBootstrap: false,
                            closeIcon: true,
                            title: 'Exito',
                            content: 'Se ha eliminado el semillero exitosamente',
                            typeAnimated: true,
                            buttons: {
                                ok: {
                                    btnClass: 'btn-warning',
                                    action: function(){
                                        window.location.reload();
                                    }
                                }

                            }
                        });
                    });
                }
            },
            cancelar: function () {
            }
        }
    });
};

$(document).ready(function(){

    $('.add').hide();
    $('.see').show();
    //$('#coordinador').val("");

    $('#see').click(function(e){
        e.preventDefault();
        $('h1').html('Semilleros');
        $('.see').show();
        $('#textSearch').show();
        $('.add').hide();
    });

    $('#register_2').click(function(){
		$('#campos').hide();
		$('.add').show();
		$('#new_coord').hide();
	});


    $('#add').click(function(e){
        e.preventDefault();
        $('h1').html('Añadir semillero');
        $('.add').show();
        $('.see').hide();
        $('#campos').hide();
        $('#new_coord').hide();
        $('#coord').show();
        $('#textSearch').hide();
    });

    $('.edit input').click(function(e){
        e.preventDefault();
        window.location.href = "edit/" + $('#lista').val();
    });

    $('#textSearch').keyup(function(e){
		e.preventDefault();
		texto = $(this).val().toLowerCase();
		var contador = 0;
		$.each($('#tableConv .info'),function(){
			if($(this).text().toLowerCase().indexOf(texto) === -1){
				$(this).hide();
			}
			else {
				$(this).show();
				contador++;
			}
		});
	});
    
    $("#cedula").keypress(function (e) {
        if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           //No se permite escribir un ASCII distinto a los numeros
           return false;
       }
    });
    $('#consult').click(function(e){
        var cc = $('#cedula').val();
        if(cc==""){
            $.alert({
                boxWidth: '400px',
                useBootstrap: false,
                closeIcon: true,
                title: 'Cedula vacia',
                content: 'Porfavor digite el numero de cedula del coordinador.',
                typeAnimated: true,
                buttons: {
                    Ok: {
                        btnClass: 'btn-warning',
                    }
                }
            });
        }
        else{
            let url = window.location;
            const postData={
                'cc': cc,
                'caso': 'verificar',
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            };
            $.post(url, postData, function(response){
                var lista = response.split(",")
                var response = lista[0]
                var nombre = lista[1]
                if(response == "1"){
                    var title='Coordinador existente';
                    var content='¿Desea asignar a '+ nombre +' al semillero como coordinador?';
                }
                else if(response == "2"){
                    var title='Integrante existente';
                    var content='El usuario '+ nombre +' es integrante de otro semillero pero no tiene perfil como  coordinador ¿Desea crearlo?';
                }
                else if(response == "3"){
                    var title='No existe el usuario';
                    var content='El usuario ingresado no existe en la aplicacion ¿Desea registrarlo?';
                }
                $.confirm({
                    boxWidth: '400px',
                    useBootstrap: false,
                    closeIcon: true,
                    title: title,
                    content: content,
                    typeAnimated: true,
                    buttons: {
                        somethingElse: {
                            text: 'Si',
                            btnClass: 'btn-warning',
                            action: function(){
                                if(response=="1"){
                                    $('#coordinador').val(cc);
                                    $('#coord').hide();
                                    $('#campos').show();
                                    $('#coord1').html("Nombre: "+nombre);
                                    $('#coord3').html("Documento: "+cc);
                                    $('#estado').val(response);
                                }
                                else if(response=="2"){
                                    $('#new_integr').hide();
                                    $('#new_coord').show();
                                    $('#coord').hide();
                                    $('#coordinador').val(cc);
                                    $('#coord3').html("Documento: "+cc);
                                    $('#estado').val(response);
                                }
                                else if(response=="3"){
                                    $('#new_coord').show();
                                    $('#coord').hide();
                                    $('#estado').val(response);
                                    $('#coord2').html(cc);
                                    $('#coord3').html("Documento: "+cc);
                                    $('#coordinador').val(cc);
                                }
                            }
                        },
                        No: function () {
                        }
                    }
                });
            });
        }
    });
    $('#register11').click(function(e){
        e.preventDefault();
        $('#caso').val($('#estado').val());
        $('form').submit();
    }); 

    $('#register1').click(function(e){
        e.preventDefault();
        var estado = $('#estado').val();
        let url = window.location;
        var cc = $('#coordinador').val()
        if(estado=="1"){
            var joined = $('#joined').val()
            var id_group = $('#id_group').val()
            var name = $('#name_s').val()
            var description = $('#description').val()
            var mail = $('#mail').val()
            var postData={
                'cc': cc,
                'joined': joined,
                'id_group': id_group,
                'name': name,
                'description':description,
                'mail': mail,
                'caso': estado,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            };
            $.post(url, postData, function(response){
                $.alert({
                    boxWidth: '400px',
                    useBootstrap: false,
                    closeIcon: true,
                    title: "Edicion exitosa",
                    content: "Se ha editado exitosamente el semillero.",
                    typeAnimated: true,
                    buttons: {
                        ok: {
                            btnClass: 'btn-warning',
                            action: function(){
                                window.location.reload();
                            }
                        }
                    }
                });
            });    
        }
    });

    $('#enviar').click(function(e){
        e.preventDefault();
        $.confirm({
            boxWidth: '400px',
            useBootstrap: false,
            closeIcon: true,
            title: "¿Esta seguro?",
            content: "Esta seguro de los cambios realizados",
            typeAnimated: true,
            buttons: {
                somethingElse: {
                    text: 'Si',
                    btnClass: 'btn-warning',
                    action: function(){
                        $('form').submit();
                    }
                },
                No: function () {
                }
            }
        });
    });
    $('#register').click(function(e){
        e.preventDefault();
        var estado = $('#estado').val();
        let url = window.location;
        var user = $('#username').val();
        var group = "Coordinador";
        var password = $('#password').val();
        var rpassword = $('#rpassword').val();
        var cc = $('#coordinador').val()
        if(estado=="2"){
            var postData={
                'cc': cc,
                'user': user,
                'group': group,
                'password': password,
                'rpassword': rpassword,
                'caso': estado,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            };
        }    
        else if(estado=="3"){
            var name = $('#name').val();
            var lastname = $('#lastname').val();
            var email = $('#email').val();
            var phone = $('#phone').val();
            var adicional = $('#adicional').val();
            var postData={
                'cc': cc,
                'user': user,
                'group': group,
                'password': password,
                'rpassword': rpassword,
                'name':name,
                'lastname':lastname,
                'email':email,
                'phone':phone,
                'adicional':adicional,
                'caso': estado,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            };
        }
        $.post(url, postData, function(response){
            var lista = response.split(",")
            var response = lista[0]
            var nombre = lista[1]
            if(response=="1"){
                var title="Nombre de usuario invalido";
                var content="El nombre de usuario no puede tener espacios";
            }
            else if(response=="2"){
                var title='Registro exitoso';
                var content='El usuario fue registrado con exito.';
                $('#new_coord').hide();
                $('#campos').show();
                $('#estado').val("1");
                $('#coord1').html("Nombre: "+nombre);
            }    
            else if(response=="3"){
                var title="Contraseñas no coinciden";
                var content="Las contraseñas deben ser iguales";
            }
            else if(response=="4"){
                var title="Nombre de usuario en uso";
                var content="Porfavor digite otro nombre de usuario.";
            }
            $.alert({
                boxWidth: '400px',
                useBootstrap: false,
                closeIcon: true,
                title: title,
                content: content,
                typeAnimated: true,
                buttons: {
                    ok: {
                        btnClass: 'btn-warning',
                    }
                }
            });
        });  
    });
});