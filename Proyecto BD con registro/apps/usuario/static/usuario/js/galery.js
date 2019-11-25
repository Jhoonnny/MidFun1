$(document).ready(function() {


    var userFeed = new Instafeed({
        get: 'user',
        userId: '20325080818',
        limit: 12,
        resolution: 'standard_resolution',
        accessToken: '20325080818.1677ed0.5a580703d0a34562b09ea9197a4c536b',
        sortBy: 'most-recent',
        template: '<div class="col-lg-3 instaimg"><a href="{{image}}" title="{{caption}}" target="_blank"><img src="{{image}}" alt="{{caption}}" class="img-fluid"/></a></div>',
    });


    userFeed.run();

    
  /*una galeria para todos los elementos */
    $('.gallery').magnificPopup({
        type: 'image',
        delegate: 'a',
        gallery: {
            enabled: true
        }
    });


});