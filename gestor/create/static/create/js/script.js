var count = 1;
var flag = true;

esconder();
ocultar();

function verificar(){
    var rol = document.getElementById('rol');
    var n_rol = rol.options[rol.selectedIndex].value;
    if(n_rol == "3"){
        mostrar();
    }else{
        ocultar();
    }
}

function add(){
    var tabla = document.getElementById('tabla');
    var tr = document.createElement('tr');
    var td = document.createElement('td');
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

    td.id = "td_" + count.toString();
    td.name = "td_" + count.toString();

    contador.value = count;

    tabla.appendChild(tr);
    tr.appendChild(td);
    td.appendChild(id_linea);
    var td = document.createElement('td');
    td.id = "td_" + count.toString();
    td.name = "td_" + count.toString();
    tr.appendChild(td);
    td.appendChild(linea);
    count += 1;
    
    esconder();
}


function remove(){
    id = (count-1).toString();
    var tabla = document.getElementById('tabla');
    var linea = document.getElementById('line_' + id);
    var id_linea = document.getElementById('idline_' + id);
    var tr = document.getElementById('tr_' + id);
    var td = document.getElementById('td_' + id);

    tr.removeChild(td)
    tabla.removeChild(tr);

    count -= 1;
    
    esconder();
}

function esconder(){
    if(count <= 1){
        var boton = document.getElementById('eliminar');
        var titulo = document.getElementById('tit_lineas');
        boton.style.display = "none";
        titulo.hidden = true;
    } else {
        var boton = document.getElementById('eliminar');
        var titulo = document.getElementById('tit_lineas');
        titulo.hidden = false;
        boton.style.display = "block";
    }
}

function ocultar(){
    var l_title = document.getElementById('tline');
    var l_select = document.getElementById('lineas');
    var l_salto = document.getElementById('lsalto');
    var l_boton = document.getElementById('lañadir');
    l_title.hidden = true;
    l_select.hidden = true;
    l_salto.hidden = true;
    l_boton.style.display = "none";
}

function mostrar(){
    var l_title = document.getElementById('tline');
    var l_select = document.getElementById('lineas');
    var l_salto = document.getElementById('lsalto');
    var l_boton = document.getElementById('lañadir');
    l_title.hidden = false;
    l_select.hidden = false;
    l_salto.hidden = false;
    l_boton.style.display = "inline-block";
}
