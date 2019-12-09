var count = 1;

function add(){
    var formulario = document.getElementById('campos');
    var description = document.createElement('input');
    var input = document.createElement('input');
    var contador = document.getElementById('contador');
    var tipo = document.createElement('select');
    
    array = [
        "Informativo",
        "Opcional",
        "Obligatorio"
    ];

    tipo.id = "sel_" + count.toString();
    tipo.name = "sel_" + count.toString();

    description.type = 'text';
    description.id = "text_" + count.toString();
    description.name = "text_" + count.toString();
    description.required = true;

    input.type = 'file';
    input.accept = 'application/pdf';
    input.id = "doc_" + count.toString();
    input.name = "doc_" + count.toString();
    input.required = true;

    contador.value = count;

    formulario.appendChild(description);
    formulario.appendChild(tipo);
    
    for(var i = 1; i <= array.length; i++){
        var option = document.createElement('option');
        option.value = i.toString();
        option.text = array[i-1];
        tipo.appendChild(option);
    }

    formulario.appendChild(input);
    formulario.appendChild(document.createElement('br'))

    count += 1;
}

function participate(){
    var boton = document.getElementById("participar");
    boton.style.display = "none";
    var tabla = document.getElementById("dparticipar");
    tabla.style.display = "inline-block";

}