
const carousel = document.getElementById('carousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

// Calculate the width of a single slide
const slideWidth = document.querySelector('.w-full').clientWidth;

// Scroll by the width of a single slide
prevBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: -slideWidth, behavior: 'smooth' });
});

nextBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: slideWidth, behavior: 'smooth' });
});

