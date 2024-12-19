function toggleMenu() {
    const navMenu = document.getElementById('navMenu').querySelector('ul');
    if (navMenu) {
        console.log('Menu trouvé');
        navMenu.classList.toggle('show');
    } else {
        console.error('Menu non trouvé');
    }
}
