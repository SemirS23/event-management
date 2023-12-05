const btnDiv = document.getElementById('addbtn');
const hiddenWrapper = document.getElementById('hidden-wrapper');
const venueWrapper = document.getElementById('venue-wrapper');
// Add a click event listener to the trigger div
btnDiv.addEventListener('click', function () {
    // Toggle the display style of the target div
    hiddenWrapper.style.display = 'flex';
    venueWrapper.style.display = 'none';
});


const inputQuantity = document.getElementById('quantity')
const priceTag = document.getElementById('price');
inputQuantity.addEventListener('input', function () {
    var event = document.getElementById('event').value;
    console.log(event);
    fetch('/eticket/get_ticket_price/' + event + '/', {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        var price = inputQuantity.value * data
        priceTag.innerText = "$" + price
    })
    .catch(error => console.error('Error fetching data:', error));
    
});