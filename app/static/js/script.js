document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('.nav-container');
    const hamburger = document.querySelector('.hamburger');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    const menuItems = document.querySelectorAll('.menu-item');
    
    // Hamburger menu toggle
    hamburger.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        this.classList.toggle('active');
        nav.classList.toggle('active');
    });

    // Handle dropdown toggles
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                e.stopPropagation();
                this.parentElement.classList.toggle('active');
            }
        });
    });

    // Handle submenu items
    menuItems.forEach(item => {
        const itemLink = item.querySelector('a');
        const arrow = item.querySelector('.arrow');
        
        // Only prevent default on arrow click, not the entire menu item
        if (arrow) {
            arrow.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    e.stopPropagation();
                    item.classList.toggle('active');
                }
            });
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 768) {
            if (!nav.contains(e.target) && !hamburger.contains(e.target)) {
                nav.classList.remove('active');
                hamburger.classList.remove('active');
                dropdownToggles.forEach(toggle => {
                    toggle.parentElement.classList.remove('active');
                });
                menuItems.forEach(item => {
                    item.classList.remove('active');
                });
            }
        }
    });
});
