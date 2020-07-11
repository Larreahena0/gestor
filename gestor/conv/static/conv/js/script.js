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

function delete1(id, caso,id_c) {
    if(caso == "2"){
        var id = id;
        var caso = "eliminar"
        let url = "{% url 'convocatoria_edit' %}";
        const postData={
            'id': id,
            'caso': caso,
            'id_c': id_c,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
        };
        $.post(url, postData, function(response){
            console.log(response)
        });
    }
    else{
        console.log("Eliminar una columna")
    };
};

$(document).ready(function(){

    $('.Crear').hide();
    $('.Editar').hide();
    $('.Eliminar').hide();
    $('#see').click(function(e){
        e.preventDefault();
        $('h1').html('Convocatorias');
        $('.Mostrar').show();
        $('#textSearch').show();
        $('.Crear').hide();
        $('.Editar').hide();
        $('.Eliminar').hide();
        $('.Convocatorias').hide();
    });
    
    $('#editar').click(function(e){
        e.preventDefault();
        $('h1').html('Editar una convocatoria');
        $('#textSearch').hide();
        $('.Mostrar').hide();
        $('.Crear').hide();
        $('.Eliminar').hide();
        $('.Editar').show();
        $('#estado').val(2)
    });

    $('#add').click(function(e){
        e.preventDefault();
        $('h1').html('Crear una convocatoria');
        $('#textSearch').hide();
        $('.Mostrar').hide();
        $('.Editar').hide();
        $('.Eliminar').hide();
        $('.Crear').show();
        $('#estado').val(0)
    });
    
    $('#delete').click(function(e){
        e.preventDefault();
        $('h1').html('Eliminar una convocatoria');
        $('#textSearch').hide();
        $('.Mostrar').hide();
        $('.Crear').hide();
        $('.Eliminar').show();
        $('.Editar').hide();
        $('#estado').val(1)
    });

    $('.Editar input').click(function(e){
        e.preventDefault();
        window.location.href = "edit/" + $('#conv').val();
    });

    var count = 1;

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
        var contador = $('#contador');
        /*
        formulario.append('<br>');

        formulario.append("<input type='text' name='text_" + count.toString() + "' id='text_" + count.toString() + "' required/>");

        contador.val(count);

        formulario.append("<select id='sel_"+ count.toString() +"' name='sel_"+ count.toString() +"'></select>");

        $("#sel_" + count.toString()).append("<option value='1'>Informativo</option><option value='2'>Opcional</option><option value='3'>Obligatorio</option>");

        formulario.append("<input type='file' name='doc_" + count.toString() + "' id='doc_" + count.toString() + "' required/>");
        formulario.append('<br>');*/
        
        formulario.append('<tr id="tr_'+ count.toString() +'"></tr>')

        var fila = $('#tr_'+count.toString());
        fila.append("<td><input type='text' name='text_" + count.toString() + "' id='text_" + count.toString() + "' placeholder='Descripcion' required/></td>")
        fila.append("<td><select id='sel_"+ count.toString() +"' name='sel_"+ count.toString() +"'></select></td>")
        fila.append('<td><button type="button" onclick=abrir("doc_'+count.toString()+'") id="boton_'+count.toString()+'">Examinar..</button>  <input type="file" name="doc_' + count.toString() + '" id="doc_' + count.toString() + '" style="display:none;" onchange=texto(this,"span_'+count.toString()+'")> <span id="span_'+count.toString()+'">Subir Archivo</span></td>')
        fila.append('<td><a class="config2" title="Eliminar" alt="Eliminar" id="del" href="#"><i class="fas fa-trash-alt"></i></a></td>');
        $("#sel_" + count.toString()).append("<option value='1'>Informativo</option><option value='2'>Opcional</option><option value='3'>Obligatorio</option>");        

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
