

var activeBox = false
//bad
function itemClick(){
    activeDesc();

    boxShow();
}

function show(divId) {
    $("." + divId).show();
    console.log('hello')
}
function boxShow() {
    show('descAlignment');
    console.log('hello')
}


function itemClick(){

    console.log('pressed');

    $( document ).ready(function() {

        console.log( "ready!" );
        $('.testContainer').click(function() {

            $('.testContainer').css({
                'border-radius': '0px'
            });
            $('.testContainer:hover').css({
                'animation': 'mymove 0s'
            })
            boxShow()

        });

    });
    activeBox = true;
}

