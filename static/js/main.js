document.addEventListener('DOMContentLoaded', function() {
    // 繝｡繝九Η繝ｼ繝医げ繝ｫ讖溯・
    const menuToggle = document.querySelector('.menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            console.log('Menu toggled');
        });
    }
    
    // 繧ｹ繝繝ｼ繧ｺ繧ｹ繧ｯ繝ｭ繝ｼ繝ｫ
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // 繧ｹ繧ｯ繝ｭ繝ｼ繝ｫ繧｢繝九Γ繝ｼ繧ｷ繝ｧ繝ｳ
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // 繧｢繝九Γ繝ｼ繧ｷ繝ｧ繝ｳ蟇ｾ雎｡隕∫ｴ縺ｮ逶｣隕・
    document.querySelectorAll('.service-card, .recruit-section, .access-section').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s, transform 0.6s';
        observer.observe(el);
    });
});
