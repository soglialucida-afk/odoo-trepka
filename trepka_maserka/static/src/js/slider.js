// Trepka Maserka — Slider
(function() {
    function initSlider() {
        var slides = document.querySelectorAll('.tm-slide');
        if (!slides.length) return;
        var cur = 0;
        setInterval(function() {
            slides[cur].classList.remove('active');
            cur = (cur + 1) % slides.length;
            slides[cur].classList.add('active');
        }, 5000);
    }

    function initHeader() {
        var header = document.querySelector('.tm-header');
        if (!header) return;
        window.addEventListener('scroll', function() {
            header.classList.toggle('shrink', window.scrollY > 50);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            initSlider();
            initHeader();
        });
    } else {
        initSlider();
        initHeader();
    }
})();