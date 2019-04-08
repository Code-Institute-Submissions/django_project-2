$(document).ready(function(){

});

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
        console.log(str1)
        console.log(str2)
        header.innerHTML = `${str1}${str2}`
      }
  	})
  }
}

changeStatus()
displayIcon()
limitTicketTitle()
