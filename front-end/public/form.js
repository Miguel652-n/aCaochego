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
const animalId = params.get("animalId") || params.get("animal_id") || "";


const form = document.querySelector("form");

// Validações
function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function validarCEP(cep) {
    const regex = /^\d{5}-?\d{3}$/;
    return regex.test(cep.replace(/\D/g, ''));
}

function validarTelefone(tel) {
    const regex = /^\(?[0-9]{2}\)?[0-9]{4,5}-?[0-9]{4}$/;
    return regex.test(tel.replace(/\D/g, ''));
}

function validarFormulario(dados) {
    const erros = [];

    if (!dados.nome || dados.nome.trim().length < 3) {
        erros.push("Nome deve ter no mínimo 3 caracteres");
    }

    if (!validarEmail(dados.email)) {
        erros.push("Email inválido");
    }

    if (!validarTelefone(dados.number)) {
        erros.push("Telefone inválido (ex: (11) 98765-4321)");
    }

    if (!dados.endereco || dados.endereco.trim().length < 5) {
        erros.push("Endereço deve ter no mínimo 5 caracteres");
    }

    if (!dados.cidade || dados.cidade.trim().length < 2) {
        erros.push("Cidade é obrigatória");
    }

    if (!validarCEP(dados.cep)) {
        erros.push("CEP inválido (formato: 12345-678)");
    }

    if (!dados.estado || dados.estado.length !== 2) {
        erros.push("Estado é obrigatório (ex: SP, RJ)");
    }

    if (!dados.descricao || dados.descricao.trim().length < 10) {
        erros.push("Descrição deve ter no mínimo 10 caracteres");
    }

    return erros;
}

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
        nome: document.getElementById("name").value.trim(),
        email: document.getElementById("email").value.trim(),
        number: document.getElementById("number").value.trim(),
        endereco: document.getElementById("endereco").value.trim(),
        cidade: document.getElementById("cidade").value.trim(),
        cep: document.getElementById("cep").value.trim(),
        estado: document.getElementById("estado").value.trim().toUpperCase(),
        descricao: document.getElementById("descricao").value.trim(),
        animal: animalNome,
        animal_id: animalId ? Number(animalId) : null
    };


    // Validar formulário
    const erros = validarFormulario(dados);
    if (erros.length > 0) {
        alert("Erro ao validar formulário:\n\n" + erros.join("\n"));
        return;
    }

    try {
        const resposta = await fetch(`${API_URL}/api/colabs`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        if (!resposta.ok) {
            const erro = await resposta.json().catch(() => ({}));
            throw new Error(erro.erro || `Erro HTTP ${resposta.status}`);
        }

        const resultado = await resposta.json();
        console.log(resultado);

        alert("Formulário enviado com sucesso! Análise em andamento...");
        form.reset();

    } catch (erro) {
        console.error("Erro ao enviar formulário:", erro);
        alert(`Erro ao enviar formulário: ${erro.message}`);
    }
});