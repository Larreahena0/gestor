var count = 1;

function add(){
  var formulario = document.getElementById('campos');
  var description = document.createElement('input');
  var input = document.createElement('input')
  var contador = document.getElementById('contador')

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
  formulario.appendChild(input);
  formulario.appendChild(document.createElement('br'))

  count += 1;
}
