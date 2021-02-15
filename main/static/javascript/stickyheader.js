function scrollDown() {
    if( window.scrollY > height){
        header.classList.add('sticky-header');
    }
    else{
        header.classList.remove('sticky-header');
    }
}

var header = document.getElementById('menu_nav');
var height = header.offsetTop;

window.addEventListener("scroll", scrollDown);
