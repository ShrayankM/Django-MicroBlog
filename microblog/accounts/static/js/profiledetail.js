$('.editbutton').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass("btn-outline-primary");
})

$('.editbutton').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass("btn-outline-primary");
})