$(document).ready(function(){

	var contador = 0;
	//Funciones que ocultan las divisiones al iniciar o refrescar la pagina
	if($('#rol').val() != 3){
		$('.lineas').each(function(){
			$(this).hide();
		});
	};
	if($('#rol').val() != 4 && $('#rol').val() != 5){
		$('.estudiante').each(function(){
			$(this).hide();
		});
	};
	if($('#tipo').val() != 1 && $('#tipo').val() != 2){
		$('.pre').each(function(){
			$(this).hide();
		});
		$('.post').each(function(){
			$(this).hide();
		});
	};
	//Con esta funcion se controla el select que despliega los atributos de los estudiantes (nivel, carrera) y los atributos del coordinador de linea (cuantas lineas)
	$('#rol').change(function(){
		if($('#rol').val() == 3){
			$('.lineas').each(function(){
				$(this).show();
			});
			$('.estudiante').each(function(){
				$(this).hide();
			});
		}
		else if($('#rol').val() == 4 || $('#rol').val() == 5){
			$('.lineas').each(function(){
				$(this).hide();
			});
			$('.estudiante').each(function(){
				$(this).show();
			});
		}
		else {
			$('.lineas').each(function(){
				$(this).hide();
			});
			$('.estudiante').each(function(){
				$(this).hide();
			});
		};
	});
	//Con esta funcion se controla el select que despliega las carreras de pregrado o de postgrado dependeiendo del tipo de estudiante
	$('#tipo').change(function(){
		if($('#tipo').val() == 1){
			$('.pre').each(function(){
				$(this).show();
			});
			$('.post').each(function(){
				$(this).hide();
			});
		}
		else if($('#tipo').val() == 2){
			$('.pre').each(function(){
				$(this).hide();
			});
			$('.post').each(function(){
				$(this).show();
			});
		}
		else{
			$('.pre').each(function(){
				$(this).hide();
			});
			$('.post').each(function(){
				$(this).hide();
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
		$('form').submit();
	});

});
