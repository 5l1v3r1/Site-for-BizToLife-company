$(document).ready(function(){




    $('#contact-form').validate({
     rules: {
      user_name: {
         required: true,
         minlength: 4
      },
      user_email: {
         required: true,
         email:true
      },
      user_subject: {
         required: false,
      },
      user_message: {
         required: true,
      },
     },
     messages: {
      user_name: {
         required: "Come on, you have a name don't you?",
         minlength: "Your name must consist of at least 2 characters"
      },
      user_email: {
         required: "Please put your email address",
      },
      user_message: {
         required: "Put some messages here?",
         minlength: "Your name must consist of at least 2 characters"
      },

     },
     submitHandler: function(form) {
      $(form).ajaxSubmit({
         type:"POST",
         data: $(form).serialize(),
         url:"sendmail.php",
         success: function() {
            $('#contact-form #success').fadeIn();
         },
         error: function() {

            $('#contact-form #error').fadeIn();
         }
      });
   }});



	// Mix It Up Activation
	var portfolio_item = $('.portfolio-contant-active');
	if (portfolio_item.length) {
		var mixer = mixitup(portfolio_item);
	};


	$(".portfolio-single-slider").slick({
		infinite: true,
		arrows:false,
		autoplay: true,
  		autoplaySpeed: 2000

	});

	$(".clients-logo").slick({
		infinite: true,
		arrows:false,
		autoplay: true,
  		autoplaySpeed: 2000
	});

	$(".testimonial-slider").slick({
		slidesToShow:1,
		infinite: true,
		arrows:false,
		autoplay: true,
  		autoplaySpeed: 2000
	});


	// CountDown JS
	$('.count-down').syotimer({
    year: year,
    month: month,
    day: day,
    hour: hour,
    minute: minute,
    lang: 'rus'
 });

	// Init Magnific Popup
	$('.portfolio-popup').magnificPopup({
  		delegate: 'a',
  		type: 'image',
  		gallery:{
			enabled:true
		},
  		mainClass: 'mfp-with-zoom',
  		navigateByImgClick: true,
  		arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',
  		tPrev: 'Previous (Left arrow key)',
  		tNext: 'Next (Right arrow key)',
  		tCounter: '<span class="mfp-counter">%curr% of %total%</span>',
		zoom: {
		    enabled: true,
		    duration: 300,
		    easing: 'ease-in-out',
		    opener: function(openerElement) {
		      return openerElement.is('img') ? openerElement : openerElement.find('img');
		    }
		  }
});






var map;
function initialize() {
	var mapOptions = {
		zoom: 13,
		center: new google.maps.LatLng(58.020683,  56.293872),
		styles: style_array_here
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}

var google_map_canvas = $('#map-canvas');

if(google_map_canvas.length) {
	google.maps.event.addDomListener(window, 'load', initialize);
}






	// Counter

	// $('.counter').counterUp({
 //        delay: 10,
 //        time: 1000
 //    });


});
