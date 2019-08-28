var count = 1;

function add(){
    var tabla = document.getElementById('tabla');
    var tr = document.createElement('tr');
    var lineas = document.getElementById('lineas');
    var valLinea = lineas.options[lineas.selectedIndex].text;
    var idLinea = lineas.options[lineas.selectedIndex].value;
    var linea = document.createElement('input');
    var id_linea = document.createElement('input')
    var eliminar = document.createElement('a');
    var contador = document.getElementById('contador');

    linea.id = "line_" + count.toString();
    linea.name = "line_" + count.toString();
    linea.value = valLinea;
    linea.readOnly = true;

    id_linea.id = "idline_" + count.toString();
    id_linea.name = "idline_" + count.toString();
    id_linea.value = idLinea;
    id_linea.readOnly = true;

    tr.id = "tr_" + count.toString();
    tr.name = "tr_" + count.toString();

    id = count.toString();
    eliminar.id = 'del_' + count.toString();
    eliminar.text = "Eliminar";
    eliminar.href = "javascript:remove("+ id +")";

    contador.value = count;

    tabla.appendChild(tr)
    tr.appendChild(id_linea);
    tr.appendChild(linea);
    tr.appendChild(eliminar);

    count += 1;
}


function remove(id){
    var tabla = document.getElementById('tabla');
    var linea = document.getElementById('line_' + id);
    var id_linea = document.getElementById('idline_' + id);
    var eliminar = document.getElementById('del_' + id);
    var tr = document.getElementById('tr_' + id);

    tr.removeChild(eliminar);
    tr.removeChild(linea);
    tr.removeChild(id_linea);
    tabla.removeChild(tr);

    count -= 1;
}

