// script.js
document.getElementById('slide-button').addEventListener('click', function() {
    const newPage = document.getElementById('new-page');

    // Add slide-up class to trigger animation
    newPage.classList.add('slide-up');

    // Use a timeout to change the background color after the animation duration
    setTimeout(() => {
        newPage.classList.add('white-background'); // Change background color to white
    }, 0); // Match this duration with your CSS transition duration
});
document.querySelectorAll('.button-link').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior

        // Show the loading screen
        const loadingScreen = document.getElementById('loading-screen');
        loadingScreen.classList.add('visible'); // Add visible class to show it

        // Simulate a delay (e.g., for an AJAX request or form submission)
        setTimeout(() => {
            // Redirect to the login or signup page
            window.location.href = this.href; // Use the href of the clicked link
        }, 500); // Delay for 0.5 seconds
    });
});
