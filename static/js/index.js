document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript loaded successfully!");

    // Ensure Swiper is properly initialized for your general swiper usage (including partners)
    var swiper = new Swiper('.swiper-container', {
        loop: true,
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


const csrfToken = '{{ csrf_token }}';

function renderEditForm(data) {
    console.log("Rendering Edit Form...");

    const formContainer = document.getElementById('edit-form-container');
    if (!formContainer) {
        console.error("Error: Form container not found!");
        return;
    }

    formContainer.innerHTML = '';  // Clear existing form

    const form = document.createElement('form');
    form.action = `/dashboard/update-person/${data.slug}/`;
    form.method = 'POST';

    // Add CSRF token
    const csrfTokenInput = document.createElement('input');
    csrfTokenInput.type = 'hidden';
    csrfTokenInput.name = 'csrfmiddlewaretoken';
    csrfTokenInput.value = csrfToken;  // Ensure csrfToken is defined
    form.appendChild(csrfTokenInput);

    // Dynamically create form fields
    Object.keys(data).forEach(key => {
        if (key !== 'slug') {  // Ignore slug field
            const fieldDiv = document.createElement('div');
            fieldDiv.classList.add('form-group');

            const label = document.createElement('label');
            label.setAttribute('for', key);
            label.textContent = key.replace('_', ' ').toUpperCase();
            fieldDiv.appendChild(label);

            const input = document.createElement('input');
            input.type = 'text';
            input.name = key;
            input.id = key;
            input.value = data[key] || '';
            fieldDiv.appendChild(input);

            form.appendChild(fieldDiv);
        }
    });

    // Add submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Update Person';
    form.appendChild(submitButton);

    // Append form to container
    formContainer.appendChild(form);

    console.log("Edit Form Rendered Successfully");
}

document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".sidebar nav ul li a");
    const sections = document.querySelectorAll(".content-section");

    // Function to show the selected section and hide others
    function showSection(sectionId) {
        sections.forEach(section => {
            if (section.id === sectionId) {
                section.style.display = "block";
            } else {
                section.style.display = "none";
            }
        });
    }

    // Initially show only the dashboard
    showSection("dashboard");

    // Add click event to each sidebar link
    links.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent the default anchor behavior
            const sectionId = this.getAttribute("data-section");
            showSection(sectionId);

            // Highlight the active link
            links.forEach(l => l.classList.remove("active"));
            this.classList.add("active");
        });
    });
});
