const header = document.querySelector("header");
const menuIcon = document.querySelector("#menu-icon");
const navigation = document.querySelector("#nav-bar");

if (header && menuIcon && navigation) {
    menuIcon.setAttribute("role", "button");
    menuIcon.setAttribute("tabindex", "0");
    menuIcon.setAttribute("aria-label", "Abrir menu de navegação");
    menuIcon.setAttribute("aria-expanded", "false");
    menuIcon.setAttribute("aria-controls", "nav-bar");
    header.classList.add("menu-ready");

    const setMenuOpen = (isOpen) => {
        header.classList.toggle("menu-open", isOpen);
        menuIcon.setAttribute("aria-expanded", String(isOpen));
        menuIcon.setAttribute("aria-label", `${isOpen ? "Fechar" : "Abrir"} menu de navegação`);
        menuIcon.title = `${isOpen ? "Fechar" : "Abrir"} navegação`;
        menuIcon.textContent = isOpen ? "close" : "menu";
    };

    const toggleMenu = () => {
        const isOpen = menuIcon.getAttribute("aria-expanded") === "true";
        setMenuOpen(!isOpen);
    };

    menuIcon.addEventListener("click", toggleMenu);

    menuIcon.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            toggleMenu();
        }
    });

    navigation.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => setMenuOpen(false));
    });

    document.addEventListener("pointerdown", (event) => {
        if (!header.contains(event.target)) {
            setMenuOpen(false);
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && menuIcon.getAttribute("aria-expanded") === "true") {
            setMenuOpen(false);
            menuIcon.focus();
        }
    });

    const navigationLinks = navigation.querySelectorAll('a[href^="#"]');
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            navigationLinks.forEach((link) => {
                if (link.hash === `#${entry.target.id}`) {
                    link.setAttribute("aria-current", "location");
                } else {
                    link.removeAttribute("aria-current");
                }
            });
        });
    }, { rootMargin: "-100px 0px -65% 0px" });

    document.querySelectorAll("section[id]").forEach((section) => sectionObserver.observe(section));
}
