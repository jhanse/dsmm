$(document).ready(function()    {
    $('.category-name').hover(function() {
        $(this).parent().parent().children().addClass("hover-cat");
    }, function() {
        $(this).parent().parent().children().removeClass("hover-cat");
    });

    $('.news-item').hoverIntent(function() {
        $(this).children().children('.more').animate({opacity: 1}, 500);
    }, function() {
        $(this).children().children('.more').animate({opacity: 0}, 500);
    });

    $(document).ready(function(){
        $('a.nazaj').click(function(){
            if(document.referrer.indexOf(window.location.hostname) != -1){
                parent.history.back();
                return false;
            }
        });
    });

    $('#nav').scrollToFixed({'marginTop': -30});

    $("div.news-item-mini").click(function(){window.location = $(this).attr("url");return false;});
});