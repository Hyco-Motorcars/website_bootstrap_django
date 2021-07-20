const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.menu-items-main');
    const navLinks = document.querySelectorAll('.menu-items-main li');

    burger.addEventListener('click',()=> {
        //Toggle nav
        nav.classList.toggle('nav-active');

        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            }
            else {
                link.style.animation = 'navLinkFade 1.5s ease'; //forwards ${index / 7 + 2}s';
            }
        });

        //Burger animation
        burger.classList.toggle('toggle');
    });
}


navSlide();
