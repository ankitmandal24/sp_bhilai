///// Section-1 CSS-Slider /////
  // Auto Switching Images for CSS-Slider
  function bannerSwitcher() {
    next = $('.sec-1-input').filter(':checked').next('.sec-1-input');
    if (next.length) next.prop('checked', true);
    else $('.sec-1-input').first().prop('checked', true);
  }

const right = document.getElementById('right');
const left = document.getElementById('left');
const carouse = document.querySelector('.carouse');

let counter = 650;
right.addEventListener('click',()=>{
    if(counter === 1950){
        counter = 0;
    }
    carouse.style.transform = `translateX(-${counter}px)`;
    counter = counter + 650;
});

var counterBack;
left.addEventListener('click', ()=>{
    if(counter === 650){
        counterBack = -1300;
        counter = 1950;
    }
    else if(counter === 1300){
        counterBack = 0;
        counter = 650;
    }else if(counter === 1950){
        counterBack = -650;
        counter = 1300;
    }
    carouse.style.transform = `translateX(${counterBack}px)`;
});

///// Anchor Smooth Scroll /////
//   $('.main-menu a, .learn-more-button a').click(function(e){

//     e.preventDefault();

//     var target = $(this).attr('href');

//     $('html, body').animate({scrollTop: $(target).offset().top}, 1000);
//     return false;
//   });
