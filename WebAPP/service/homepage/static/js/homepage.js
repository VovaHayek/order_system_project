function search(search_text) {
    $.ajax({
        type: 'GET',
        url: '/',
        dataType: 'json',
        data: {
            'search_text': search_text.value
        },
        success: function(response) {
            console.log(response['html_from_view']);
			$("#restaurants").html(response['html_from_view']);
        }
    })
}