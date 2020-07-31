function delete1(id) {
    window.event.preventDefault();
	$.confirm({
		boxWidth: '400px',
		useBootstrap: false,
		closeIcon: true,
		title: '¿Está seguro?',
		content: 'El integrante no podra ser restaurado',
		typeAnimated: true,
		buttons: {
			somethingElse: {
				text: 'Seguro',
				btnClass: 'btn-warning',
				action: function(){
					var caso = "eliminar"
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
};


$(document).ready(function(){
	$('#crear').hide();
	$('#campos').hide();
	$('#nuevo').hide();
	$('#documento').hide();
	
	//Funcion util para editar los campos de un usuario
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

	$('#editar').click(function(){
		$('#ver').hide();
		$('#textSearch').hide();
		$('#crear').show();
	});

	$('#see').click(function(){
		$('#ver').show();
		$('#textSearch').show();
		$('#crear').hide();
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
                content: 'Porfavor digite el numero de cedula del integrante.',
                typeAnimated: true,
                buttons: {
                    ok: {
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
                console.log(response)
                if(response == "1"){
                    var title='Integrante existente';
                    var content='¿Desea asignar este integrante al semillero?';
                }
                else if(response == "2"){
                    var title='No existe el integrante';
                    var content='El integrante ingresado no existe en la aplicacion ¿Desea registrarlo?';
				}
				else if(response == "3"){
                    var title='Integrante registrado';
                    var content='El integrante ingresado ya forma parte del semillero';
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
								if(response=="1" || response=="2"){
									$('#document').val(cc);
									$('#inte').hide();
									$('#campos').show();
									$('#documento').show();
									$('#inte2').html(cc);
									if(response=="1"){
										$('#caso').val("viejo");
									}
									else if(response=="2"){
										$('#nuevo').show();
										$('#caso').val("nuevo");
									}
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

	$('#textSearch').keyup(function(e){
		e.preventDefault();
		texto = $(this).val().toLowerCase();
		var cont = 0;
		$.each($('#tableConv .info'),function(){
			if($(this).text().toLowerCase().indexOf(texto) === -1){
				$(this).hide();
			}
			else {
				$(this).show();
				cont++;
			}
		});
	});
});
