const btnDiv = document.getElementById('addbtn');
const hiddenWrapper = document.getElementById('hidden-wrapper');
const eventWrapper = document.getElementById('event-wrapper');
// Add a click event listener to the trigger div
btnDiv.addEventListener('click', function () {
    // Toggle the display style of the target div
    hiddenWrapper.style.display = 'flex';
    eventWrapper.style.display = 'none';
});