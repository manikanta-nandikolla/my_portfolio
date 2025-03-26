gsap.from(".hero", { opacity: 0, duration: 1, y: -50 });
gsap.from(".skills", { opacity: 0, duration: 1.5, delay: 0.5, x: -100 });
gsap.from(".projects", { opacity: 0, duration: 1.5, delay: 1, x: 100 });


//Dark Mode Toggle Switch
document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const themeIcon = document.getElementById("themeIcon");
    const body = document.body;

    // Check localStorage for theme preference
    if (localStorage.getItem("theme") === "light") {
        body.classList.add("light-mode");
        themeIcon.classList.replace("fa-moon", "fa-sun");
    }

    darkModeToggle.addEventListener("click", function () {
        if (body.classList.contains("light-mode")) {
            body.classList.remove("light-mode");
            localStorage.setItem("theme", "dark");
            themeIcon.classList.replace("fa-sun", "fa-moon");
        } else {
            body.classList.add("light-mode");
            localStorage.setItem("theme", "light");
            themeIcon.classList.replace("fa-moon", "fa-sun");
        }
    });
});
