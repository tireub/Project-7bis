 var $list, $inputText, $map, $quote;
    $list = $('ul');
    $inputText = $("#inputText");
    $map = $("#map");
    $quote = $("#quote")


$(function() {

    $inputText.keypress(function(e) {
        if(e.which == 13) {

            var text = $('input:text').val();


            $map.empty();
            $map.append('<div class="map_display"><iframe width="400" height="300" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBN18OElCDJ6nPJvc_d-FLMZXdKVjpyTj0&q='+text+'"></iframe></div>') ;
            $list.append('<li>' + text + '</li>');
            extractAdress(text)
            postData(text);


            $('input:text').val('');

        };
    });
});


function postData(input) {
    $.ajax({
        type: "GET",
        url: ("/quote"),
        data: { location: input },
        success: function(response) {

            $list.append('<li>Pour ton information, ' + response + '</li>');

            }
    });
}

function extractAdress(input) {
    $.ajax({
        type: "GET",
        url: ("/geoloc"),
        data: { location: input },
        success: function(response){
            $list.append('<li>Ce que tu cherches a pour adresse : ' + response + '.</li>');
            }
        });
}

