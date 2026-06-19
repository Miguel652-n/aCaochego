function getApiUrl() {
    const meta = document.querySelector('meta[name="api-url"]');
    if (meta && meta.content && meta.content.trim() !== "") return meta.content.trim();
    if (window.__API_URL__) return window.__API_URL__;
    if (window.location.origin && window.location.origin !== "null") return window.location.origin;
    return "http://127.0.0.1:8000";
}

const API_URL = getApiUrl();

const params = new URLSearchParams(window.location.search);
const animalNome = params.get("animal") || "";

const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const dados = {
        nome: document.getElementById("name").value,
        email: document.getElementById("email").value,
        number: document.getElementById("number").value,
        endereco: document.getElementById("endereco").value,
        cidade: document.getElementById("cidade").value,
        cep: document.getElementById("cep").value,
        estado: document.getElementById("estado").value,
        descricao: document.getElementById("descricao").value,
        animal: animalNome
    };

    try {

        const resposta = await fetch(`${API_URL}/api/colabs`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        if (!resposta.ok) {
            throw new Error(`Erro HTTP: ${resposta.status}`);
        }

        const resultado = await resposta.json();

        console.log(resultado);

        alert("Formulário enviado com sucesso!");

        form.reset();

    } catch (erro) {

        console.error("Erro ao enviar formulário:", erro);

        alert("Erro ao enviar formulário!");

    }

});