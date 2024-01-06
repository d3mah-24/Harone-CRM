(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
      if ($("#spinner").length > 0) {
        $("#spinner").removeClass("show");
      }
    }, 1);
  };
  spinner();

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

  // Sidebar Toggler
  $(".sidebar-toggler").click(function () {
    $(".sidebar, .content").toggleClass("open");
    return false;
  });

  // Progress Bar
  $(".pg-bar").waypoint(
    function () {
      $(".progress .progress-bar").each(function () {
        $(this).css("width", $(this).attr("aria-valuenow") + "%");
      });
    },
    { offset: "80%" }
  );

  // Calender
  $("#calender").datetimepicker({
    inline: true,
    format: "L",
  });

  // Testimonials carousel
  $(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    items: 1,
    dots: true,
    loop: true,
    nav: false,
  });

  // Chart Global Color
  Chart.defaults.color = "#6C7293";
  Chart.defaults.borderColor = "#000000";

  // Worldwide Sales Chart

  const domain = window.location.origin;
  const url = `${domain}/CRM/company/reportdata`;

  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };

  fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      var a = response.json();
      console.log("Response:");
    })
    .catch((error) => {
      alert(88);
      console.error("Error:", error);
    });

  var ctx1 = $("#worldwide-sales").get(0).getContext("2d");

  var myChart1 = new Chart(ctx1, {
    type: "bar",
    data: {
      labels: ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
      datasets: [
        {
          label: "USA",
          data: [15, 30, 55, 65, 60, 80, 95],
          backgroundColor: "rgba(235, 22, 22, .7)",
        },
        {
          label: "UK",
          data: [8, 35, 40, 60, 70, 55, 75],
          backgroundColor: "rgba(235, 22, 22, .5)",
        },
        {
          label: "AU",
          data: [12, 25, 45, 55, 65, 70, 60],
          backgroundColor: "rgba(235, 22, 22, .3)",
        },
      ],
    },
    options: {
      responsive: true,
    },
  });
  // Doughnut Chart
  var ctx6 = $("#doughnut-chart").get(0).getContext("2d");
  var myChart6 = new Chart(ctx6, {
    type: "doughnut",
    data: {
      labels: ["Italy", "France", "Spain", "USA", "Argentina"],
      datasets: [
        {
          backgroundColor: [
            "rgba(235, 22, 22, .7)",
            "rgba(235, 22, 22, .6)",
            "rgba(235, 22, 22, .5)",
            "rgba(235, 22, 22, .4)",
            "rgba(235, 22, 22, .3)",
          ],
          data: [55, 49, 44, 24, 15],
        },
      ],
    },
    options: {
      responsive: true,
    },
  });
})(jQuery);
