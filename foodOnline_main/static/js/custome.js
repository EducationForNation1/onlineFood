$(document).ready(function (){
    $('.add_to_cart').on('click', function (e){
        e.preventDefault();
        food_id = $(this).attr('data-id');
        url = $(this).attr('data-url');
        data={
            food_id:food_id,
        }
        $.ajax({
            type:'GET',
            url:url,
            data:data,
            success:function (response){
                console.log(response)
            }
        })
    })

    // Place the cart item quantity on load
    $('.item-qty').each(function (){
        let the_id = $(this).attr('id');
        let qty = $(this).attr('data-qty');

        $('#'+the_id).html(qty); 
        

    });
})