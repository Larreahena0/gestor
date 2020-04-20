$(document).ready(function(){

    var count = 1;

	$('#lista').hide();

    $('#sName').hide();
    $('#editar').click(function(e){
        e.preventDefault();
        $('#campos').show();
        $('#lista').hide();
        $('form').removeAttr('novalidate');
        var estado = $('#estado').val();
        if(estado == "0"){
            $('#editar').text("Añadir");
            $('#name').attr("required", "true");
            $('#name').hide();
            $('#sName').show();
            $('input[type="submit"]').val("Editar");
            $('#estado').val("2");
        }
        else {
            $('#editar').text("Editar");
            $('#name').show();
            $('#sName').hide();
            $('input[type="submit"]').val("Enviar");
            $('#estado').val("0");
        }

    });

    $('#delete').click(function(e){
        e.preventDefault();
        $('#editar').text("Añadir");
        $('form').attr("novalidate","true")
        $('#campos').hide();
        $('#estado').val("1");
        $('#lista').show();
        $('#enviar').val("Eliminar");
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

    $('#add').click(function(e){

        e.preventDefault();
        var formulario = $('#campos div');
        var contador = $('#contador');

        formulario.append('<br>');

        formulario.append("<input type='text' name='text_" + count.toString() + "' id='text_" + count.toString() + "' required/>");

        contador.val(count);

        formulario.append("<select id='sel_"+ count.toString() +"' name='sel_"+ count.toString() +"'></select>");

        $("#sel_" + count.toString()).append("<option value='1'>Informativo</option><option value='2'>Opcional</option><option value='3'>Obligatorio</option>");

        formulario.append("<input type='file' name='doc_" + count.toString() + "' id='doc_" + count.toString() + "' required/>");
        formulario.append('<br>');

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
