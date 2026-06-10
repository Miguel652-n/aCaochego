function criarPet(nome, especie, genero, idade, regiao, ong, cidade, imagem) {
  return {
    nome,
    especie,
    genero,
    idade,
    regiao,
    ong,
    cidade,
    imagem
  };
}

const petsData = [
    // cachorros
    criarPet("Ben", "cachorro", "macho", "Idoso", "MG", "Amparo pet", "Uberlândia", "Assets/Doguinhos/Machos/Ben_I.png"),
    criarPet("Babi", "cachorro", "femea", "Filhote", "MG", "Cão Viver", "Contagem", "Assets/Doguinhos/Femeas/Babi_F.png"),
    criarPet("Beto", "cachorro", "macho", "Idoso", "MG", "Amparo pet", "Uberlândia", "Assets/Doguinhos/Machos/Beto_I.png"),
    criarPet("Bebel", "cachorro", "femea", "Adulto", "RJ", "Ação animal", "Rio de Janeiro", "Assets/Doguinhos/Femeas/Bebel_A.png"),
    criarPet("Bob", "cachorro", "macho", "Adulto", "RJ", "Distrito Animal", "Rio de Janeiro", "Assets/Doguinhos/Machos/Bob_A.png"),
    criarPet("Bella", "cachorro", "femea", "Adulto", "MG", "Apa", "Uberlândia", "Assets/Doguinhos/Femeas/Bella_A.png"),
    criarPet("Caos", "cachorro", "macho", "Adulto", "RJ", "Cãodominio", "Resende", "Assets/Doguinhos/Machos/Caos_A.png"),
    criarPet("Collie", "cachorro", "femea", "Filhote", "RJ", "Cãodominio", "Resende", "Assets/Doguinhos/Femeas/Collie_F.png"),
    criarPet("Chocolate", "cachorro", "macho", "Adulto", "RJ", "Adote um Bichinho", "Itaguaí", "Assets/Doguinhos/Machos/Chocolate_A.png"),
    criarPet("Jade", "cachorro", "femea", "Filhote", "RJ", "Adote um Bichinho", "Itaguaí", "Assets/Doguinhos/Femeas/Jade_F.png"),
    criarPet("Cirius", "cachorro", "macho", "Filhote", "SP", "Alianima", "Bela vista", "Assets/Doguinhos/Machos/Cirius_F.png"),
    criarPet("Lindinha", "cachorro", "femea", "Filhote", "SP", "Amor animal", "Marília", "Assets/Doguinhos/Femeas/Lindinha_F.png"),
    criarPet("Dante", "cachorro", "macho", "Adulto", "SP", "Amor animal", "Marília", "Assets/Doguinhos/Machos/Dante_A.png"),
    criarPet("Luna", "cachorro", "femea", "Filhote", "MG", "Apa", "Uberlândia", "Assets/Doguinhos/Femeas/Luna_F.png"),
    criarPet("Fred", "cachorro", "macho", "Filhote", "RJ", "Adote um Bichinho", "Itaguaí", "Assets/Doguinhos/Machos/Fred_F.png"),
    criarPet("Malu", "cachorro", "femea", "Filhote", "SP", "Alianima", "Bela vista", "Assets/Doguinhos/Femeas/Malu_F.png"),
    criarPet("Hamlet", "cachorro", "macho", "Filhote", "SP", "Alianima", "Bela vista", "Assets/Doguinhos/Machos/Hamelet_F.png"),
    criarPet("Mel", "cachorro", "femea", "Adulto", "GO", "Anjos da rua", "Goiânia", "Assets/Doguinhos/Femeas/Mel_A.png"),
    criarPet("Kratus", "cachorro", "macho", "Adulto", "Go", "Anjos da rua", "Goiânia", "Assets/Doguinhos/Machos/Kratus_A.png"),
    criarPet("Panqueca", "cachorro", "femea", "Adulto", "RJ", "Fazenda Modelo", "Guaratiba", "Assets/Doguinhos/Femeas/Panqueca_A.png"),
    criarPet("Nacho", "cachorro", "macho", "Adulto", "GO", "Lar dos animais", "Goiânia", "Assets/Doguinhos/Machos/Nacho_A.png"),
    criarPet("Tamires", "cachorro", "femea", "Adulto", "GO", "Anjos da rua", "Goiânia", "Assets/Doguinhos/Femeas/Tamires_A.png"),
    criarPet("Thor", "cachorro", "macho", "Adulto", "GO", "Anjos da rua", "Goiânia", "Assets/Doguinhos/Machos/Thor_A.png"),
    criarPet("Zoe", "cachorro", "femea", "Filhote", "RJ", "Cãodominio", "Resende", "Assets/Doguinhos/Femeas/Zoe_F.png"),
    criarPet("Zeus", "cachorro", "macho", "Filhote", "SP", "Amor animal", "Marília", "Assets/Doguinhos/Machos/Zeus_F.png"),
    criarPet("Paçoca", "cachorro", "femea", "Adulto", "SP", "Amor Animal", "Marília", "Assets/Doguinhos/Femeas/Paçoca_A.png"),
    // gatos  
    criarPet("Cookie", "gato", "macho", "Filhote", "RJ", "Cãodominio", "Resende", "Assets/Miaus/Machos/Cookie_F.png"),
    criarPet("Café", "gato", "femea", "Adulto", "RJ", "Cãodominio", "Resende", "Assets/Miaus/Femeas/Cafe_A.png"),
    criarPet("Coxinha", "gato", "macho", "Idoso", "MG", "Apa", "Uberlândia", "Assets/Miaus/Machos/Coxinha_I.png"),
    criarPet("Faisca", "gato", "femea", "Adulto", "SP", "Amor animal", "Marília", "Assets/Miaus/Femeas/Faisca_A.png"),
    criarPet("Felix", "gato", "macho", "Filhote", "SP", "Alianima", "Bela vista", "Assets/Miaus/Machos/Felix_F.png"),
    criarPet("Flora", "gato", "femea", "Adulto", "MG", "Bichos Gerais", "Belo Horizonte", "Assets/Miaus/Femeas/Flora_A.png"),
    criarPet("Garfield", "gato", "macho", "Adulto", "RJ", "Fazenda Modelo", "Guaratiba", "Assets/Miaus/Machos/Garfield_A.png"),
    criarPet("Kitty", "gato", "femea", "Adulto", "Rj", "Fazenda modelo", "Guaratiba", "Assets/Miaus/Femeas/Kitty_A.png"),
    criarPet("Gatito", "gato", "macho", "Filhote", "RJ", "Cãodominio", "Resende", "Assets/Miaus/Machos/Gatito_F.png"),
    criarPet("Luz", "gato", "femea", "Adulto", "SP", "Ong SOS", "São Caetano do Sul", "Assets/Miaus/Femeas/Luz_A.png"),
    criarPet("Mingau", "gato", "macho", "Filhote", "MG", "Apa", "Uberlândia", "Assets/Miaus/Machos/Mingau_F.png"),
    criarPet("Maya", "gato", "femea", "Adulto", "MG", "Bichos gerais", "Belo Horizonte", "Assets/Miaus/Femeas/Maya_A.png"),
    criarPet("Nico", "gato", "macho", "Adulto", "GO", "Anjos da rua", "Goiânia", "Assets/Miaus/Machos/Nico_A.png"),
    criarPet("Moon", "gato", "femea", "Adulto", "Sp", "Ong SOS", "São Caetano do Sul", "Assets/Miaus/Femeas/Moon_A.png"),
    criarPet("Ozzy", "gato", "macho", "Filhote", "SP", "Alianima", "Bela vista", "Assets/Miaus/Machos/Ozzy_F.png"),
    criarPet("Pixie", "gato", "femea", "Adulto", "SP", "Amor animal", "Marília", "Assets/Miaus/Femeas/Pixie_A.png"),
    criarPet("Zoe", "gato", "femea", "Adulto", "GO", "Lar dos animais", "Goinia", "Assets/Miaus/Femeas/Zoe_A.png"),
    
];

let quantidadeVisivel = 6;
let listaFiltrada = [...petsData];

const container = document.querySelector(".adotar");

function renderPets() {

    container.innerHTML = "";

    const visiveis = listaFiltrada.slice(0, quantidadeVisivel);

    visiveis.forEach(pet => {
        container.innerHTML += `
            <article class="adotar-card">
                
                <h3>${pet.ong}</h3>
                <p>${pet.cidade} - ${pet.regiao}</p>

                <div class="img-wrapper">
                    <img src="${pet.imagem}" alt="${pet.nome}">
                </div>

                <p>${pet.nome}</p>

                <button><a href="formulario.html?animal=${pet.nome}">Adotar</a></button>
            </article>
        `;
    });

    const botao = document.getElementById("verMais");
    if (quantidadeVisivel >= listaFiltrada.length) {
        botao.style.display = "none";
    } else {
        botao.style.display = "block";
    }
}

function aplicarFiltro() {
    const especie = document.querySelector('input[name="especie"]:checked')?.value;
    const genero = document.querySelector('input[name="genero"]:checked')?.value;
    const idadesSelecionadas = document.querySelectorAll('input[name="idade"]:checked');
    const regiao = document.querySelector(".estados").value;

    const idades = Array.from(idadesSelecionadas).map(i => i.value);

    listaFiltrada = petsData.filter(pet => {
        if (especie && pet.especie !== especie) return false;
        if (genero && pet.genero !== genero) return false;
        if (idades.length > 0 && !idades.map(i => i.toLowerCase()).includes(pet.idade.toLowerCase())) return false;
        if (regiao && pet.regiao !== regiao) return false;

        return true;
    });

    quantidadeVisivel = 6;
    renderPets();
}

document.getElementById("verMais").addEventListener("click", () => {
    quantidadeVisivel += 6;
    renderPets();
});

document.querySelector("form").addEventListener("change", aplicarFiltro);

renderPets();

// ========================================================================================================= //

function renderPets() {

    const container = document.querySelector(".adotar");

    container.innerHTML = "";

    const visiveis = listaFiltrada.slice(0, quantidadeVisivel);

    visiveis.forEach(pet => {

        container.innerHTML += `

            <article class="adotar-card">
                
                <h3>${pet.ong}</h3>
                <p>${pet.cidade} - ${pet.regiao}</p>

                <div class="img-wrapper">
                    <img src="${pet.imagem}" alt="${pet.nome}">
                </div>

                <p>${pet.nome}</p>

                <button><a href="formulario.html?animal=${pet.nome}">Adotar</a></button>

            </article>

        `;
    });
}

const API_URL = "http://127.0.0.1:8000";

async function enviarAnimaisParaBackend() {
    for (const pet of petsData) {
        try {
            console.log("Enviando:", pet.nome);

            const resposta = await fetch(`${API_URL}/animais`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(pet)
            });

            if (!resposta.ok) {
                const erro = await resposta.text();

                console.error("FALHOU:");
                console.error("Nome:", pet.nome);
                console.error("Animal:", pet);
                console.error("Resposta:", erro);

                continue;
            }

            const data = await resposta.json();
            console.log("Sucesso:", pet.nome);

        } catch (erro) {
            console.error("EXCEÇÃO:");
            console.error("Nome:", pet.nome);
            console.error("Animal:", pet);
            console.error(erro);
        }
    }
}