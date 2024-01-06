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
      return response.json(); // Parse the JSON data from the response
    })
    .then((res) => {
      const data = res.Sum_tot;
      console.log("Specific Value:", data);
      var dataset = [];
      var values = [];
      var keys = [];
      for (const key in data) {
        if (Object.hasOwnProperty.call(data, key)) {
          const element = {
            label: key,
            data: [parseInt(data[key])],
            backgroundColor: `rgba(${Math.floor(
              Math.random() * (255 - 120) + 120
            )}, 22, ${Math.floor(Math.random() * (255 - 20) + 20)} )`,
          };

          dataset.push(element);
          values.push(parseInt(data[key]));
          keys.push(key);
          // console.log(element, key);
        }
      }
      console.log(dataset);
      var ctx1 = $("#worldwide-sales").get(0).getContext("2d");
      var myChart1 = new Chart(ctx1, {
        type: "bar",
        data: {
          labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
          datasets: dataset,
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
          labels: keys,
          datasets: [
            {
              backgroundColor: [
                "rgba(123, 55, 22, .7)",
                "rgba(43, 2, 3, .6)",
                "rgba(235, 233, 22, .5)",
                "rgba(36, 22, 22, .4)",
                "rgba(22, 56, 22, .3)",
              ],
              data: values,
            },
          ],
        },
        options: {
          responsive: true,
        },
      });
    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch
      console.error("Error:", error);
    });
})(jQuery);
