function abrir(id) {
    var file = document.getElementById(id);
    file.dispatchEvent(new MouseEvent('click', {
        view: window,
        bubbles: true,
        cancelable: true
    }));
}
function texto(elem, id_text) {
    var texts = document.getElementById(id_text);
    if(elem.files.length != 0) {
        texts.innerText = elem.files[0].name;
    }
}

function delete1(id, caso) {
    window.event.preventDefault();
    if(caso == "1"){
        //Seleccionamos Fila a eliminar de la tabla
        var fila = $('#tr_'+id);
        fila.remove();
    }
    else if(caso == "2"){
        $.confirm({
            boxWidth: '400px',
            useBootstrap: false,
            closeIcon: true,
            title: '¿Está seguro?',
            content: 'El documento no podra ser restaurado',
            typeAnimated: true,
            buttons: {
                somethingElse: {
                    text: 'Seguro',
                    btnClass: 'btn-warning',
                    action: function(){
                        var caso = "eliminar"
                        //Url donde esté, por ende la consulta se hace dependiendo de donde esté el navegador ya sea editando o creando
                        let url = window.location;
                        const postData={
                            'id': id,
                            'caso': caso,
                            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                        };
                        $.post(url, postData, function(response){
                            window.location.reload()
                        });
                    }
                },
                cancel: function () {
                }
            }
        });
    }
    else if(caso == "3"){
        $.confirm({
            boxWidth: '400px',
            useBootstrap: false,
            closeIcon: true,
            title: '¿Está seguro?',
            content: 'La convocatoria no podra ser restaurada',
            typeAnimated: true,
            buttons: {
                somethingElse: {
                    text: 'Seguro',
                    btnClass: 'btn-warning',
                    action: function(){
                        let url = window.location;
                        const postData={
                            'conv': id,
                            'estado': 1,
                            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                        };
                        $.post(url, postData, function(response){
                            window.location.reload()
                        });
                    }
                },
                cancel: function () {
                }
            }
        });
    }
};

$(document).ready(function(){
    var count = 1;
    $('#contador').val(count-1);

    $('.Crear').hide();
    $('#see').click(function(e){
        e.preventDefault();
        $('h1').html('Convocatorias');
        $('.Mostrar').show();
        $('#textSearch').show();
        $('.Crear').hide();
        $('.Convocatorias').hide();
    });
    
    $('#add').click(function(e){
        e.preventDefault();
        $('h1').html('Crear una convocatoria');
        $('#textSearch').hide();
        $('.Mostrar').hide();
        $('.Crear').show();
        $('#estado').val(0)
    });
    
    $('#enviar').click(function(e){
        if($('#estado').val() == 1){
            e.preventDefault();
            $.confirm({
                boxWidth: '400px',
                useBootstrap: false,
                closeIcon: true,
                title: '¿Está seguro?',
                content: 'La convocatoria no podra ser restaurada',
                typeAnimated: true,
                buttons: {
                    somethingElse: {
                        text: 'Seguro',
                        btnClass: 'btn-warning',
                        action: function(){
                            $('form').submit();
                        }
                    },
                    cancel: function () {

                    }
                }
            });
        }
    });

    $("#bparticipar").click(function(e){
        e.preventDefault();
        $("#bparticipar").hide();
        $("#dparticipar").show();
    });

    $('#add_doc').click(function(e){

        e.preventDefault();
        var formulario = $('#tabla');
        
        formulario.append('<tr id="tr_'+ count.toString() +'"></tr>')

        var fila = $('#tr_'+count.toString());
        fila.append("<td><input type='text' name='text_" + count.toString() + "' id='text_" + count.toString() + "' placeholder='Descripcion' required/></td>")
        fila.append("<td><select id='sel_"+ count.toString() +"' name='sel_"+ count.toString() +"'></select></td>")
        fila.append('<td><button type="button" onclick=abrir("doc_'+count.toString()+'") id="boton_'+count.toString()+'">Examinar..</button>  <input type="file" name="doc_' + count.toString() + '" id="doc_' + count.toString() + '" style="display:none;" onchange=texto(this,"span_'+count.toString()+'")> <span id="span_'+count.toString()+'">Subir Archivo</span></td>')
        fila.append('<td><a class="config2" title="Eliminar" alt="Eliminar" id="del" onclick=delete1("'+count.toString()+'","1") href="#"><i class="fas fa-trash-alt"></i></a></td>');
        $("#sel_" + count.toString()).append("<option disabled selected>Seleccione</option><option value='1'>Informativo</option><option value='2'>Opcional</option><option value='3'>Obligatorio</option>");        
        $('#contador').val(count);
        count += 1;
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

});
