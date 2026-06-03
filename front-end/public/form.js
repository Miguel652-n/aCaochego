const API_URL = "http://127.0.0.1:8000";

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
        descricao: document.getElementById("descricao").value
    };

    try {

        const resposta = await fetch(`${API_URL}/colabs`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();

        console.log(resultado);

        alert("Formulário enviado com sucesso!");

        form.reset();

    } catch (erro) {

        console.error("Erro ao enviar formulário:", erro);

        alert("Erro ao enviar formulário!");

    }

});