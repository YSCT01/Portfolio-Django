var menuicon = document.getElementById("menumob");
var menumovil = document.getElementById("menumobil");
var close = document.getElementById("closemenu");
var listamen = document.getElementById("listamobil");

menuicon.addEventListener('click', function (){
        menumovil.classList.remove('hide');
        menumovil.classList.add("active");
});

close.addEventListener("click", function (){
    listamen.classList.add("hide");
    listamen.addEventListener("animationend", function (){
        if(listamen.classList.contains("hide")) {
            menumovil.classList.remove("active");
            listamen.classList.remove("hide");
        }
})
})



