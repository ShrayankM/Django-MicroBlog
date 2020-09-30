$('.editbutton').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass("btn-outline-primary");
})

$('.editbutton').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass("btn-outline-primary");
})


$('.deletebtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass("btn-outline-danger");
})


$('.deletebtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass("btn-outline-danger");
})

$('.updatebtn').mouseover(function() {
    $(this).removeClass("btn-light");
    $(this).addClass("btn-outline-warning");
})


$('.updatebtn').mouseout(function() {
    $(this).addClass("btn-light");
    $(this).removeClass("btn-outline-warning");
})