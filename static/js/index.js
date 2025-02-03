document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript loaded successfully!");

    // Ensure Swiper is properly initialized for your general swiper usage (including partners)
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1, // Default: Show 1 card per view (small screens)
        spaceBetween: 10, // Space between slides
        loop: true, // Enable infinite scrolling
        autoplay: {
            delay: 3000, // Auto-slide every 3 seconds
        },
        breakpoints: {
            768: { // Medium screens and up (tablets)
                slidesPerView: 2,
                spaceBetween: 15,
            },
            1024: { // Large screens (desktops)
                slidesPerView: 3,
                spaceBetween: 20,
            }
        }
    });

    console.log("Swiper initialized successfully!");

    // Carousel Scroll Controls (For non-Swiper elements, if any)
    const carousel = document.getElementById('carousel');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (carousel && prevBtn && nextBtn) {
        console.log("Carousel controls found!");

        // Calculate the width of a single slide dynamically
        const slideWidth = document.querySelector('.w-full')?.clientWidth || 300;

        prevBtn.addEventListener('click', () => {
            carousel.scrollBy({ left: -slideWidth, behavior: 'smooth' });
        });

        nextBtn.addEventListener('click', () => {
            carousel.scrollBy({ left: slideWidth, behavior: 'smooth' });
        });
    } else {
        console.warn("Carousel elements not found! Check HTML structure.");
    }

    // Continuous Typing and Deleting Animation
    function animateText() {
        const text1 = document.getElementById('text1');
        const text2 = document.getElementById('text2');

        function typingEffect() {
            text1.classList.add('typing-effect');
            text2.classList.add('typing-effect');

            setTimeout(() => {
                text1.classList.remove('typing-effect');
                text2.classList.remove('typing-effect');
                text1.classList.add('typing-reverse');
                text2.classList.add('typing-reverse');
            }, 8000); // Wait for typing to finish

            setTimeout(() => {
                text1.classList.remove('typing-reverse');
                text2.classList.remove('typing-reverse');
                typingEffect(); // Restart the animation loop
            }, 16000); // Wait for deleting to finish
        }

        typingEffect(); // Initial call to start typing
    }

    // Call animateText function when page is loaded
    animateText();
});


