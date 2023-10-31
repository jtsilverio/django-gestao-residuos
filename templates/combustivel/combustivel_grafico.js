var ctx = document.getElementById("myChart").getContext("2d");

var data = {
  labels: ["Red", "Blue", "Yellow", "Green", "Purple"],
  datasets: [{
    data: [12, 19, 3, 5, 2],
    backgroundColor: ["#FF0000", "#0000FF", "#FFFF00", "#008000", "#800080"]
  }]
};

var myChart = new Chart(ctx, {
  type: 'bar',
  data: data,
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});