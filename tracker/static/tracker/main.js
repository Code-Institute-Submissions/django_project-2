$(document).ready(function(){

  // const bugChart = document.getElementById('bugChart').getContext('2d')
  // const featChart = document.getElementById('featChart').getContext('2d')
  const endpoint = '/api/charts/data'

  // Bug upvotes Chartt
  $.ajax({
    method: 'GET',
    url: endpoint,
    success: (res) => {
      let data = res.bugs.datasets[0].data
      let labels = res.bugs.labels

      if (bugChart) {
        const bugVotesChart = new Chart(bugChart, {
          type: 'bar',
          data: {
            labels:   labels,
            datasets: [{
              label: 'Bug Upvotes',
              data: data,
              backgroundColor: '#ef7559'
            }]
          },
          options: {
            scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      min: 0,
                      max: 10,
                      stepSize: 2,
                  }
              }]
            }
          }
        })
      }
    },
    error: (error_data) => {
      console.log(error_data)
    },
  })// End Ajax call graph 1


  // Features upvotes Chart
  $.ajax({
    method: 'GET',
    url: endpoint,
    success: (res) => {
      let data = res.features.datasets[0].data
      let labels = res.features.labels

      if (featChart) {
        const featVotesChart = new Chart(featChart, {
          type: 'bar',
          data: {
            labels:   labels,
            datasets: [{
              label: 'Feature Upvotes',
              data: data,
              backgroundColor: '#0a8cb3'
            }]
          },
          options: {
            scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      min: 0,
                      max: 10,
                      stepSize: 2
                  }
              }]
            }
          }
        })
      }
    },
    error: (error_data) => {
      console.log(error_data)
    },
  })// End Ajax call graph 2


})
// End JQuery

const cards = document.querySelectorAll('.card')

// Function to manipulate content of Bootstrap badge
function changeStatus() {
  if (cards) {
    [...cards].forEach(card => {
      let span = card.getElementsByClassName('status')[0]
      let badge = card.getElementsByClassName('badge')[0]
      if (span.innerText == 'TD') {
        span.innerText = 'In Progress'
        badge.classList.add('badge-info')
      }else if (span.innerText == 'RQ') {
        span.innerText = 'Requested'
        badge.classList.add('badge-warning')
      }else if (span.innerText == 'FX') {
        span.innerText = 'Bug Fixed'
        badge.classList.add('badge-success')
      }
  	})
  }
}

// Function to programmatically display bug or feature icon
function displayIcon() {
  if (cards) {
    [...cards].forEach(card => {
      let ticket = card.getElementsByClassName('ticket-title')[0]
      const ticketType = ticket.getElementsByTagName('small')[0]
      const bugIcon = ticket.querySelector('.fa-bug')
      const featureIcon = ticket.querySelector('.fa-users-cog')
      if (ticketType.innerText == 'BG') {
        bugIcon.classList.remove('hide')
      }else if (ticketType.innerText == 'FT') {
        featureIcon.classList.remove('hide')
      }
  	})
  }
}

// Function in list view to change long titles to substring with trailing ...
function limitTicketTitle() {
  if (cards) {
    [...cards].forEach(card => {
      let header = card.getElementsByClassName('ticket-title')[0]
      const titleLength = (header.innerText.length)
      if (titleLength > 30 && header.classList.contains('list')) {
        const str1 = `${header.innerHTML.slice(0, 30)}...`
        const str2 = `${header.innerHTML.slice(titleLength, -1)}`
        header.innerHTML = `${str1}${str2}`
      }
  	})
  }
}

// Function to change singular/plural of 'upvotes' on home page
function upvotes() {
  if (cards) {
    [...cards].forEach(card => {
      if (card.getElementsByClassName('upvotes-total')[0]) {
        const totalUpvotes = parseInt(card.getElementsByClassName('upvotes-total')[0].innerText)
          let element = card.getElementsByClassName('upvotes')[0].innerText
          if (totalUpvotes > 1) {
            element += 's'
            card.getElementsByClassName('upvotes')[0].innerText = element
          }
        }
    	})
    }
  }

changeStatus()
displayIcon()
limitTicketTitle()
upvotes()


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
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



// const featVotesChart = new Chart(featChart, {
//   type: 'bar',
//   data: {
//     labels:   ['Fea 1', 'Fea 2', 'Fea 3', 'Fea 4', 'Fea 5', 'Fea 6'],
//     datasets: [{
//       label: 'Upvotes',
//       data: [45, 88, 34, 67, 24, 78],
//       backgroundColor: '#0a8cb3'
//     }]
//   },
//   options: {}
// })
