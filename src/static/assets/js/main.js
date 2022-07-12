$(document).ready(function (){
    // Sticky Navbar Style
    $(window).on("scroll", function () {
        if ($(window).scrollTop()) {
            $("nav").addClass("stickyNavStyle");
        } else {
            $("nav").removeClass("stickyNavStyle");
        };
    });
    // Navbar
    $('.bars').on("click", function (e){
        e.preventDefault();
        e.stopPropagation();
        $('.bars').toggleClass('open');
        $('.menu ul').toggleClass('show');
        $('body').toggleClass('y-hidden');
    });
    // Single Swiper
    new Swiper(".singleSwiper",{
        slidesPerView: 1,
        spaceBetween: 25,
        autoplay:{
            delay: 3000,
        },
    });
    // Header Bottom
    new Swiper(".servicesSwiper",{
        spaceBetween: 0,
        loop: false,
        breakpoints:{
            0:{
                slidesPerView: 1.50,
            },
            575:{
                slidesPerView: 2.50,
            },
            767:{
                slidesPerView: 3,
            },
            991:{
                slidesPerView: 2.50,
            },
            1110:{
                slidesPerView: 3,
            },
        }
    });
    // Home Blog
    new Swiper(".blogSwiper",{
        spaceBetween: 30,
        loop: false,
        //centeredSlides: true,
        breakpoints:{
            0:{
                slidesPerView: 1.25,
            },
            575:{
                slidesPerView: 1.75,
            },
            767:{
                slidesPerView: 2.50,
            },
            991:{
                slidesPerView: 4,
            },
        },
        pagination:{
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation:{
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });
    // Popup Close
    $('.popupClose').on("click", function (e){
        e.preventDefault();
        e.stopPropagation();
        $('.popupMain').removeClass('open');
        $('body').removeClass('y-hidden');
        $('body').removeClass('overlay');
    });
    // Project Detail Swiper
    var swiper = new Swiper(".mySwiper",{
        spaceBetween: 10,
        slidesPerView: 4,
        freeMode: true,
        watchSlidesProgress: true,
    });
    var swiper2 = new Swiper(".mySwiper2",{
        spaceBetween: 20,
        thumbs:{
            swiper: swiper,
        },
    });
});
// Home Projects Tabs
function openTabs(evt, tabName){
    var i, tabContent, tabButton;
    tabContent = document.getElementsByClassName("tabContent");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
    tabButton = document.getElementsByClassName("tabButton");
    for (i = 0; i < tabButton.length; i++) {
        tabButton[i].className = tabButton[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "flex";
    evt.currentTarget.className += " active";
}
// Popup Photo
function onClick(element) {
    document.getElementById("img-src").src = element.title;
    $('.popupMain').toggleClass('open');
    $('body').toggleClass('y-hidden');
    $('body').toggleClass('overlay');
}