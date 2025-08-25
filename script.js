// script.js
document.getElementById('slide-button').addEventListener('click', function() {
    const newPage = document.getElementById('new-page');
    newPage.classList.add('slide-up');
    setTimeout(() => {
        newPage.classList.add('white-background');
    }, 0);
});

document.querySelectorAll('.button-link').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const loadingScreen = document.getElementById('loading-screen');
        loadingScreen.classList.add('visible');
        setTimeout(() => {
            window.location.href = this.href;
        }, 500);
    });
});
