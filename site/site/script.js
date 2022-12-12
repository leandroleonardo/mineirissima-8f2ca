AOS.init();

var nav = document.getElementById('menu');
let items = document.getElementsByClassName('menu-item')

window.addEventListener("scroll", function (event) {

    if (window.pageYOffset > 100) {
        for (i = 0; i < items.length; i++) { items[i].style.color = 'black' }
        //nav.style.background = "#f8f3db";
        nav.style.background = "#ffff";
        nav.style.boxShadow = "1px 0px 4px 0px black"
    }
    else {
        nav.style.background = "transparent";
        nav.style.boxShadow = "";
        for (i = 0; i < items.length; i++) { items[i].style.color = 'white' }
    }
});

function addUser(){
    console.log('entrou!')
}

/* modal */

function openModal(mn) {

    let modal = document.getElementById('dv-modal');

    if (typeof modal == 'undefined' || modal === null)
        return;

    modal.style.display = 'Block';
    document.body.style.overflow = 'hidden';
}

function closeModal(mn) {
    let modal = document.getElementById('dv-modal');

    if (typeof modal == 'undefined' || modal === null)
        return;

    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

/* modal sucesso */

function openModal_sucesso(mn) {

    let modal = document.getElementById('dv-modal-sucesso');

    if (typeof modal == 'undefined' || modal === null)
        return;

    modal.style.display = 'Block';
    document.body.style.overflow = 'hidden';
}

function closeModal_sucesso(mn) {
    let modal = document.getElementById('dv-modal-sucesso');

    if (typeof modal == 'undefined' || modal === null)
        return;

    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}