const balance = document.getElementById('balance')

fetch('/eticket/get_balance/', {
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }
})
.then(response => response.json())
.then(data => {
    balance.innerText = "Balance:  $" + data
})
.catch(error => console.error('Error fetching data:', error));