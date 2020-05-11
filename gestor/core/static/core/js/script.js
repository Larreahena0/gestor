$(document).ready(function(){

    $('#add').hide();

    $('#see').click(function(e){
        e.preventDefault();
        $('h1').html('Semilleros');
        alert('ver');
    });
    
    $('#editar').click(function(e){
        e.preventDefault();
        $('h1').html('Editar semillero');
        $('.add').hide();
        $('.edit').show();
        $('.delete').hide();
        $(this).hide();
        $('#add').show();
    });

    $('#add').click(function(e){
        e.preventDefault();
        $('h1').html('Añadir semillero');
        $('.add').show();
        $('.edit').hide();
        $('.delete').hide();
        $(this).hide();
        $('#editar').show();
    });

    $('.edit input').click(function(e){
        e.preventDefault();
        window.location.href = "edit/" + $('#lista').val();
    });
    
    $('#delete').click(function(e){
        e.preventDefault();
        $('h1').html('Eliminar semillero');
        $('.add').hide();
        $('.edit').hide();
        $('.delete').show();
    });

});