
$('.postbtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass( "btn-outline-warning");
})

$('.postbtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass("btn-outline-warning");
})

$('.viewbtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass( "btn-outline-primary");
})

$('.viewbtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass( "btn-outline-primary");
})

$('.logoutbtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass( "btn-outline-danger");
})

$('.logoutbtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass( "btn-outline-danger");
})

$('.loginbtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass( "btn-outline-success");
})

$('.loginbtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass( "btn-outline-success");
})

$('.registerbtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass( "btn-outline-info");
})

$('.registerbtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass( "btn-outline-info");
})

$('.profilebtn').mouseover(function() {
    $(this).removeClass("btn-light")
    $(this).addClass("btn-outline-dark");
})

$('.profilebtn').mouseout(function() {
    $(this).addClass("btn-light")
    $(this).removeClass("btn-outline-dark");
})



