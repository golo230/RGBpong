// Basic JavaScript to handle smooth scrolling for the "Discover More" button

document.addEventListener('DOMContentLoaded', function () {
    const discoverMoreBtn = document.querySelector('.btn');
    discoverMoreBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const targetId = discoverMoreBtn.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        window.scrollTo({
            top: targetElement.offsetTop,
            behavior: 'smooth'
        });
    });
});
