// JavaScript for enhanced animations and falling leaves effect

document.addEventListener('DOMContentLoaded', function() {
    // Add hover effects to cards
    addCardHoverEffects();

    // Add button click animations
    addButtonAnimations();
});

function createFallingLeaves() {
    const fallingLeavesContainer = document.createElement('div');
    fallingLeavesContainer.className = 'falling-leaves';
    document.body.appendChild(fallingLeavesContainer);

    // Create multiple leaves
    for (let i = 0; i < 20; i++) {
        const leaf = document.createElement('div');
        leaf.className = 'leaf';
        leaf.style.left = Math.random() * 100 + '%';
        leaf.style.animationDelay = Math.random() * 10 + 's';
        leaf.style.animationDuration = (Math.random() * 5 + 5) + 's';
        fallingLeavesContainer.appendChild(leaf);
    }
}

function addCardHoverEffects() {
    const cards = document.querySelectorAll('.disease-card, .treatment-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
            this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
}

function addButtonAnimations() {
    const buttons = document.querySelectorAll('.stButton button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

// Add loading animation for images
function addImageLoadingEffects() {
    const images = document.querySelectorAll('.stImage img');
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = '0';
            this.style.animation = 'fadeIn 0.5s ease-in-out forwards';
        });
    });
}

// Smooth scrolling for navigation
function addSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
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
}

// Add particle effect on button hover
function addParticleEffect() {
    const buttons = document.querySelectorAll('.stButton button');

    buttons.forEach(button => {
        button.addEventListener('mouseenter', function(e) {
            for (let i = 0; i < 10; i++) {
                createParticle(e.clientX, e.clientY);
            }
        });
    });
}

function createParticle(x, y) {
    const particle = document.createElement('div');
    particle.style.position = 'fixed';
    particle.style.left = x + 'px';
    particle.style.top = y + 'px';
    particle.style.width = '4px';
    particle.style.height = '4px';
    particle.style.background = '#4CAF50';
    particle.style.borderRadius = '50%';
    particle.style.pointerEvents = 'none';
    particle.style.zIndex = '1000';

    document.body.appendChild(particle);

    const angle = Math.random() * Math.PI * 2;
    const velocity = Math.random() * 50 + 20;
    const vx = Math.cos(angle) * velocity;
    const vy = Math.sin(angle) * velocity;

    let posX = x;
    let posY = y;
    let opacity = 1;

    const animate = () => {
        posX += vx * 0.02;
        posY += vy * 0.02;
        opacity -= 0.02;

        particle.style.left = posX + 'px';
        particle.style.top = posY + 'px';
        particle.style.opacity = opacity;

        if (opacity > 0) {
            requestAnimationFrame(animate);
        } else {
            document.body.removeChild(particle);
        }
    };

    requestAnimationFrame(animate);
}

// Initialize all effects
function initEffects() {
    addImageLoadingEffects();
    addSmoothScrolling();
    addParticleEffect();
}

// Call init when Streamlit is ready
if (window.streamlit) {
    window.streamlit.addEventListener('ready', initEffects);
} else {
    // Fallback for when Streamlit isn't loaded yet
    setTimeout(initEffects, 1000);
}
