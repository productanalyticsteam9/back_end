(function ($) {
  "use strict";
  // Auto-scroll
  $('#myCarousel').carousel({
    interval: 5000
  });

  // Control buttons
  $('.next').click(function () {
    $(this).closest('.carousel').carousel('next');
    return false;
  });
  $('.prev').click(function () {
    $(this).closest('.carousel').carousel('prev');
    return false;
  });

  // On carousel scroll
  $("#myCarousel").on("slide.bs.carousel", function (e) {
    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 3;
    var totalItems = $("#myCarousel .carousel-item").length;
    if (idx >= totalItems - (itemsPerSlide - 1)) {
      var it = itemsPerSlide - (totalItems - idx);
      for (var i = 0; i < it; i++) {
        // append slides to end 
        console.log(i)
        if (e.direction == "left") {
          $("#myCarousel .carousel-item").eq(i).appendTo(".carousel-inner");
        } else {
          $("#myCarousel .carousel-item").eq(0).appendTo(".carousel-inner");
        }
      }
    }
  });

  $("#myCarousel1").on("slide.bs.carousel", function (e) {
    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 3;
    var totalItems = $("#myCarousel1 .carousel-item").length;
    if (idx >= totalItems - (itemsPerSlide - 1)) {
      var it = itemsPerSlide - (totalItems - idx);
      for (var i = 0; i < it; i++) {
        // append slides to end 
        if (e.direction == "left") {
          $("#myCarousel1 .carousel-item").eq(i).appendTo(".carousel-inner");
        } else {
          $("#myCarousel1 .carousel-item").eq(0).appendTo(".carousel-inner");
        }
      }
    }
  });
})
(jQuery);