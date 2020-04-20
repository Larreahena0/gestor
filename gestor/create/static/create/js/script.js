$(document).ready(function(){

	var contador = 0;
	
	if($('#rol').val() != 3){
		$('.lineas').each(function(){
			$(this).hide();
		});
	}

	$('#rol').change(function(){
		if($('#rol').val() != 3){
			$('.lineas').each(function(){
				$(this).hide();
			});
		}
		else {
			$('.lineas').each(function(){
				$(this).show();
			});
		}
	});

	$('#lañadir').click(function(){

		var flag = false;

		$('#tabla .classLine input').each(function(){
			if($(this).val().indexOf($('#lineas').val()) === -1){

			} else {
				flag = true;
			}
		});
		if(!flag){
			$('#tabla').append(`<tr id='tr_` + contador.toString() + `'>
									<td class='classLine' id='td_` + contador.toString() + `'>
										<input id='idline_` + contador.toString() + `' name='idline_` + contador.toString() + `' type='text' value='`+ $('#lineas').val() + `' readOnly>
								 	</td>
									<td>
										<input id='line_` + contador.toString() + `' name='line_` + contador.toString() + `' type='text' value='`+ $('#lineas option:selected').text() +`' readOnly>
									</td>
								</tr>`);
			contador++;
		} else {
			$.confirm({
                boxWidth: '400px',
                useBootstrap: false,
                closeIcon: true,
                title: 'Línea ya añadida',
                content: 'No es posible añadir la misma línea dos veces.',
                typeAnimated: true,
                buttons: {
					ok: {
						btnClass: 'btn-warning',
                    }
                }
            });
		}
	});

	$('#eliminar').click(function(){
		if($('#tabla tbody tr').length != 1){
			$('#tabla tr:last-child').remove();
			contador--;
		}
	});

	$('#enviar').click(function(e){
		e.preventDefault();
		$('#contador').val(contador-1);
		//$('form').submit();
	});

});
