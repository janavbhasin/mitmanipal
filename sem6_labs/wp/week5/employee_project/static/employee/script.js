// Optional: Handle any front-end validations if required
document.querySelector('form').addEventListener('submit', function(event) {
    const dateOfJoining = document.getElementById('date_of_joining').value;
    
    if (!dateOfJoining) {
        alert('Please select a date of joining');
        event.preventDefault();
    }
});
