/*Obtener variable de tabs a clickear*/
var tabexp= document.getElementById('exptab');
var tabcono = document.getElementById('conotab');
/*Obtener variable de contenedores de información*/
var conocont = document.getElementById('conoinfo')
var expcont = document.getElementById('expinfo')



function changeTab(cshow, chide, tabact, taboff){
        /*Cambio de clases*/
        cshow.classList.remove("hidentab");
        tabact.classList.add("active");
        taboff.classList.remove("active");
        chide.classList.add("hidentab");
        console.log("click");
}

window.addEventListener('load', function (){
    changeTab(conocont, expcont, tabcono, tabexp);
})