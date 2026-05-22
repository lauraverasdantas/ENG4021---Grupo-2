document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector("[data-site-nav]");
    if (!nav) {
        return;
    }

    const toggle = nav.querySelector("[data-nav-toggle]");
    const menu = nav.querySelector("[data-nav-menu]");

    const closeMenu = () => {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.setAttribute("aria-label", "Abrir menu");
    };

    const openMenu = () => {
        nav.classList.add("is-open");
        toggle.setAttribute("aria-expanded", "true");
        toggle.setAttribute("aria-label", "Fechar menu");
    };

    toggle.addEventListener("click", () => {
        if (nav.classList.contains("is-open")) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    menu.querySelectorAll("a, button").forEach((item) => {
        item.addEventListener("click", closeMenu);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeMenu();
        }
    });

    window.matchMedia("(min-width: 761px)").addEventListener("change", closeMenu);
});
