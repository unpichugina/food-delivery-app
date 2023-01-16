$('.addCart').click(function () {

    const data = {
        'product_id': $(this).data('product-id'),
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
    };
    console.log(data);
    $.post('/cart/add/', data, function () {

    });// $(".alert").alert('close');
});
