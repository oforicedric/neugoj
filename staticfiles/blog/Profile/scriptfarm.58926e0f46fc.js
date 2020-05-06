function showChart(user_activity, all_activity) {
  var ctx = document.getElementById("myChart");
  ctx.width = 100;
  ctx.height = 100;
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: graph_labels,
      datasets: [
        {
          data: user_activity,
          label: "My Study Activity",
          borderColor: "#3e95cd",
          fill: false
        },
        {
          data: all_activity,
          label: "Average Neugo User Activity",
          borderColor: "#8e5ea2",
          fill: false
        },
      ]
    },
    options: {
      maintainAspectRatio: false,
      responsive: true,
    }
  });

};
/*
// Our labels along the x-axis
var years = [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050];
// For drawing the lines
var africa = [86,114,106,106,107,111,133,221,783,2478];
var asia = [282,350,411,502,635,809,947,1402,3700,5267];
var europe = [168,170,178,190,203,276,408,547,675,734];
var latinAmerica = [40,20,10,16,24,38,74,167,508,784];
var northAmerica = [6,3,2,2,7,26,82,172,312,433];

var ctx = document.getElementById("myChart");
ctx.width = 100;
ctx.height =100;
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      { 
        data: africa,
        label: "Africa",
        borderColor: "#3e95cd",
        fill: false
      },
      { 
        data: asia,
        label: "Asia",
        borderColor: "#8e5ea2",
        fill: false
      },
      { 
        data: europe,
        label: "Europe",
        borderColor: "#3cba9f",
        fill: false
      },
      { 
        data: latinAmerica,
        label: "Latin America",
        borderColor: "#e8c3b9",
        fill: false
      },
      { 
        data: northAmerica,
        label: "North America",
        borderColor: "#c45850",
        fill: false
      }
    ]
  },
  options: {
              maintainAspectRatio:false,
              responsive:true,
            }
});
*/
// slider

var swiper = new Swiper('.blog-slider', {
 // spaceBetween: 30,
  effect: 'fade',
  loop: true,
  mousewheel: {
    invert: false,
  },
  // autoHeight: true,
  pagination: {
    el: '.blog-slider__pagination',
    clickable: true,
  }
});

//end of slider