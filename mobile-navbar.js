class MobileNavbar {
    constructor() {
        this.mobileMenu = document.querySelector('.mobile-menu');
        this.navList = document.querySelector('.nav-lista');
        this.navLinks = document.querySelectorAll('.nav-lista li');
        this.activeClass = 'active';
        this.handleClick = this.handleClick.bind(this);
    }

    animatedLinks() {
        this.navLinks.forEach((link, index) => {
            link.style.animation
                ? (link.style.animation = '')
                : (link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`);
        });
    }

    handleClick() {
        this.navList.classList.toggle(this.activeClass);
        this.mobileMenu.classList.toggle(this.activeClass);
        this.animatedLinks();
    }

    addEventClick() {
        this.mobileMenu.addEventListener('click', this.handleClick);
    }

    init() {
        if (this.mobileMenu) {
            this.addEventClick();
        }
        return this;
    }
}

const mobileNavbar = new MobileNavbar();
mobileNavbar.init();