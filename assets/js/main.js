// Initialize Owl Carousel for hero section
$(document).ready(function() {
    // Hero Slider initialization
    $('.hero-slider').owlCarousel({
        items: 1,
        loop: true,
        margin: 0,
        nav: true,
        dots: true,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        animateOut: 'fadeOut',
        navText: [
            '<i class="fas fa-chevron-left"></i>',
            '<i class="fas fa-chevron-right"></i>'
        ],
        responsive: {
            0: {
                nav: false
            },
            768: {
                nav: true
            }
        }
    });

    // News ticker animation pause on hover
    $('.ticker-wrap').hover(
        function() {
            $(this).find('.ticker').css('animation-play-state', 'paused');
        },
        function() {
            $(this).find('.ticker').css('animation-play-state', 'running');
        }
    );

    // Initialize tooltips
    $('[data-bs-toggle="tooltip"]').tooltip();

    // Smooth scroll for anchor links
    $('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) {
        if (
            location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
            && 
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                event.preventDefault();
                $('html, body').animate({
                    scrollTop: target.offset().top - 100
                }, 1000);
            }
        }
    });

    // Counter animation in statistics section
    $('.counter').each(function() {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 2000,
            easing: 'swing',
            step: function(now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

    // Add shadow to header on scroll
    $(window).scroll(function() {
        if ($(window).scrollTop() > 50) {
            $('.main-header').addClass('scrolled');
        } else {
            $('.main-header').removeClass('scrolled');
        }
    });

    // Mobile menu toggle
    $('.navbar-toggler').click(function() {
        $('.main-nav').toggleClass('mobile-active');
    });

    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}); 