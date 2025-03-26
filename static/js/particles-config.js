// GSAP Animations
gsap.from(".hero", { opacity: 0, duration: 1, y: -50 });
gsap.from(".skills", { opacity: 0, duration: 1.5, delay: 0.5, x: -100 });
gsap.from(".projects", { opacity: 0, duration: 1.5, delay: 1, x: 100 });

// Particles.js Config
particlesJS("particles-js", {
    "particles": {
        "number": { "value": 120, "density": { "enable": true, "value_area": 900 } },
        "color": { "value": "#ffffff" },
        "shape": { "type": "circle" },
        "opacity": { "value": 0.4, "random": true },
        "size": { "value": 2.5, "random": true },
        "move": { "enable": true, "speed": 1.5 }
    },
    "interactivity": {
        "events": {
            "onhover": { "enable": true, "mode": "repulse" },
            "onclick": { "enable": true, "mode": "push" }
        }
    }
});
