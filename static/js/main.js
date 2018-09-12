function increment_function(id)
{
console.log('+')

    $.ajax({
        url:'http://127.0.0.1:8000/home/',
        type: "POST",
        data: {id: id, sign: 'plus'},
        success:function(response){},
        complete:function(){},
        error:function (xhr, textStatus, thrownError){}
    });

$('#products_query').load('http://127.0.0.1:8000/home/ #products_query');
}

function decrement_function(id)
{
    $.ajax({
        url:'http://127.0.0.1:8000/home/',
        type: "POST",
        data: {id: id, sign: 'minus'},
        success:function(response){},
        complete:function(){},
        error:function (xhr, textStatus, thrownError){}
    });

$('#products_query').load('http://127.0.0.1:8000/home/ #products_query');
console.log('-')

}


