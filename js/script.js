document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll('.timeline-item');
    
    function checkVisibility() {
        const scrollPosition = window.scrollY + window.innerHeight;
        
        items.forEach(item => {
            const itemTop = item.getBoundingClientRect().top + window.scrollY;
            if (scrollPosition > itemTop + 150) {
                item.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkVisibility);
    checkVisibility(); // Chama a função ao carregar a página
});
