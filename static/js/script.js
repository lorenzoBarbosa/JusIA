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

const overlay = document.getElementById("overlay");
const botaoFechar = document.getElementById("fechar-overlay");
const botaoAceitar = document.getElementById("aceitar-lead");
const botaoRecusar = document.getElementById("recusar-lead");
const campoHorario = document.getElementById("data-hora-consulta");

let botaoQueAbriu = null;  
let leadAtual = null;      

if (overlay && botaoFechar && botaoAceitar && botaoRecusar && campoHorario) {
    function abrirOverlay(card, botao) {
        botaoQueAbriu = botao;
        leadAtual = card;

        document.getElementById("overlay-nome").textContent = card.dataset.nome || "";
        document.getElementById("overlay-telefone").textContent = card.dataset.telefone || "";
        document.getElementById("overlay-assunto").textContent = card.dataset.assunto || "";
        document.getElementById("overlay-recebida").textContent = card.dataset.recebida || "";
        document.getElementById("overlay-urgencia").textContent = card.dataset.urgencia || "";
        document.getElementById("overlay-processo-andamento").textContent = card.dataset.processoAndamento || "";
        document.getElementById("overlay-cidade-estado").textContent = card.dataset.cidadeEstado || "";
        document.getElementById("overlay-email").textContent = card.dataset.email || "";
        document.getElementById("overlay-disponibilidade").textContent = card.dataset.disponibilidade || "";
        document.getElementById("overlay-status").textContent = card.dataset.status || "";
        document.getElementById("overlay-resumo").textContent = card.dataset.resumo || "";

        campoHorario.value = "";
        const agora = new Date();
        agora.setMinutes(agora.getMinutes() - agora.getTimezoneOffset());
        campoHorario.min = agora.toISOString().slice(0, 16);

        overlay.classList.add("active");
        overlay.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
        botaoFechar.focus();
    }

    function fecharOverlay() {
        overlay.classList.remove("active");
        overlay.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";
        if (botaoQueAbriu) botaoQueAbriu.focus();
    }

    async function enviarDecisao(decisao) {
        if (!leadAtual) return;

        if (decisao === "aceita" && !campoHorario.value) {
            alert("Informe o horário proposto para a consultoria.");
            campoHorario.focus();
            return;
        }

        try {
            const resposta = await fetch(`/leads/${leadAtual.dataset.id}/decidir`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    decisao: decisao,
                    data_hora_consulta: decisao === "aceita" ? campoHorario.value : null
                })
            });

            if (!resposta.ok) throw new Error("Erro " + resposta.status);

            leadAtual.remove();
            leadAtual = null;
            fecharOverlay();
        } catch (erro) {
            console.error(erro);
            alert("Não foi possível enviar a decisão.");
        }
    }

    document.addEventListener("click", (e) => {
        const botao = e.target.closest(".abrir-lead");
        if (!botao) return;
        const card = botao.closest(".lead-card");
        if (card) abrirOverlay(card, botao);
    });


    botaoFechar.addEventListener("click", fecharOverlay);

    overlay.addEventListener("click", (e) => {
        if (e.target === overlay) fecharOverlay();
    });

    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && overlay.classList.contains("active")) {
            fecharOverlay();
        }
    });

    botaoAceitar.addEventListener("click", () => enviarDecisao("aceita"));
    botaoRecusar.addEventListener("click", () => enviarDecisao("recusada"));
}
