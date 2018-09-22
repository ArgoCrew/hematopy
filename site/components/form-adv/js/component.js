/*
  Credits to: [Osvaldas Valutis](www.osvaldas.info)
  Available for use under the MIT License
*/
'use strict';

let _fullpage = {
  originIndex: 0,
};

let fullpage_api = new fullpage('#fullpage', {
  licenseKey: 'xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx',
  autoScrolling: false,
  scrollHorizontally: true,
  controlArrows: false,
  onLeave: function(origin, destination, direction) {
    console.info(origin.index);
    _fullpage.originIndex = origin.index;
  }
});

//methods
fullpage_api.setAllowScrolling(false);

Mousetrap.bind('enter', function() {
  // console.info(_fullpage.originIndex);
  fullpage_api.moveSlideRight();
});

Mousetrap.bind('left', () => { fullpage_api.moveSlideLeft(); });
Mousetrap.bind('right', () => { fullpage_api.moveSlideRight(); });


let inputs = document.querySelectorAll('.input__file');

Array.prototype.forEach.call(inputs, function(input) {
  let label = input.nextElementSibling,
      labelVal = label.innerHTML;

  input.addEventListener('change', function( e ) {
    let fileName = '';
    if( this.files && this.files.length > 1 ){
      fileName = (this.getAttribute( 'data-multiple-caption' ) || '').replace('{count}', this.files.length);
    } else {
      fileName = e.target.value.split( '\\' ).pop();
    }

    if(fileName) {
      label.querySelector( 'span' ).innerHTML = fileName;
    } else {
      label.innerHTML = labelVal;
    }

    fullpage_api.moveSlideRight();
  });

  // Firefox bug fix
  input.addEventListener('focus', () => { input.classList.add('has-focus'); });
  input.addEventListener('blur', () => { input.classList.remove('has-focus'); });
});
