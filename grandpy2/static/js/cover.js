$(function() {

    var $list, $inputText, $map, $quote;
    $list = $('ul');
    $inputText = $("#inputText");
    $map = $("#map");
    $quote = $("#quote")



    $inputText.keypress(function(e) {
        if(e.which == 13) {

            var text = $('input:text').val();


            $map.empty();
            $map.append('<div class="map_display"><iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBN18OElCDJ6nPJvc_d-FLMZXdKVjpyTj0&q='+text+'"></iframe></div>') ;
            $list.append('<li>' + text + '</li>');

            $quote.append('{{ quote('+text+') }}');

            $('input:text').val('');

        };
    });


});

