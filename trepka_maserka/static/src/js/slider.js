/** @odoo-module **/

document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.tm-slide');
    if (!slides.length) return;
    let cur = 0;
    setInterval(() => {
        slides[cur].classList.remove('active');
        cur = (cur + 1) % slides.length;
        slides[cur].classList.add('active');
    }, 5000);

    const header = document.querySelector('.tm-header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.classList.toggle('shrink', window.scrollY > 50);
        });
    }
});
