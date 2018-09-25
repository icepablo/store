function delete_function(id)
{
console.log('delete worked')

    $.ajax({
        url:'http://127.0.0.1:8000/my_order/',
        type: "POST",
        data: {id: id},
        success:function(response){},
        complete:function(){},
        error:function (xhr, textStatus, thrownError){}
    });

$('#orders').load('http://127.0.0.1:8000/my_order/ #orders');
}
