$(document).ready(function(){

    $('.btn').click(function(){
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function (response) {
                $.each(response, function(index) {
                    $('.list').append(
                        '<input "id="" type="hidden" value="">'+
                        '<div><h3>' + response[index]?.name + '</h3><h3>' + response[index]?.price + '</h3>' +
                        (response[index]?.image != '' ? ('<img src="' + response[index]?.image + '" alt="image" width="250" height="auto"><br>') : response[index]?.image) +
                        (response[index]?.vendor_name != '' ? ('<h3>' + response[index]?.vendor_name + '</h3><br>') : response[index]?.vendor_name)  +
                        '<button class="btn btn-danger" onClick="onClickHandler()">Delete</button><br><br></div>'
                    )
                })
            }
        })
    })
})