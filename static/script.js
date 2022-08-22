$(document).ready(function(){

    $('.btn').click(function(){
        $.ajax({
            url: '',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                $("#olx").css("display", "block");
                $.each(response, function(index) {
                    $('.list').append(
                        '<div class="row justify-content" style="margin: 15px;">' +
                        '<button id="'+response[index]?.olx_id+'" data-id="'+response[index]?.olx_id+'" class="btn btn-danger" style="width: 6%;" onClick="onClickHandler(this)">Delete</button>' +
                        '<div class="col col-lg-2 text-center" style="width: 13%; display: block">' +
                        '<input value="'+response[index]?.olx_id+'" type="hidden" name="olx_id" id="olx_id">'+
                        (response[index]?.image != '' ? ('<img src="' + response[index]?.image + '" alt="image" width="150" height="auto" style="margin-right: 20px">') : '<h4 style="display: contents;">#</h4>') +
                        '</div>' +
                        '<div class="col col-lg-2" style="width: 52%; display: block">' +
                        '<h4 style="display: contents;">' +
                        response[index]?.name + 
                        '</h4>' +
                        '</div>' +
                        '<div class="col col-lg-2 text-center" style="width: 15%; display: block">' +
                        '<h4 style="display: contents;">' +
                        response[index]?.price +
                        '</h4>' +
                        '</div>' +
                        '<div class="col col-lg-2 text-center" style="width: 13%; display: block">' +
                        '<h4 style="display: contents;">' +
                        (response[index]?.vendor_name != '' ? (response[index]?.vendor_name) : '#') +
                        '</h4>' +
                        '</div>' +
                        '</div>'
                    )
                })
            }
        })
    })
})