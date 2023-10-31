/* globals Chart:false, feather:false */
// Get the width of the screen
var screenWidth = window.innerWidth;

// Set the width of the dashboard to the width of the screen
document.getElementById("dashboard").style.width = screenWidth + "px";

// Add a listener to the window resize event
window.addEventListener("resize", function() {
  // Get the new width of the screen
  var screenWidth = window.innerWidth;

  // Set the width of the dashboard to the new width of the screen
  document.getElementById("dashboard").style.width = screenWidth + "px";
});
(() => {
    'use strict'
  
    feather.replace({ 'aria-hidden': 'true' })
  
    // Graphs
    const ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    const myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          'Domingo',
          'Segunda-feira',
          'Terça-feira',
          'Quarta-feira',
          'Quinta-feira',
          'Sexta-feira',
          'Sábado'
        ],
        datasets: [{
          data: [
            15339,
            21345,
            18483,
            24003,
            23489,
            24092,
            12034
          ],
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#007bff',
          borderWidth: 4,
          pointBackgroundColor: '#007bff'
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        },
        legend: {
          display: false
        }
      }
    })
  })()