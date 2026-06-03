function criarOngs (nome, cidade, regiao, imagem, pix) {
    return {
        nome,
        cidade,
        regiao,
        imagem,
        pix
    }
}

const ongsData = [
    // MG
    criarOngs("Amparo Pet", "Uberlândia", "MG", "Assets/assetsongs/ampetMG.png", "13966133660"),
    criarOngs("Apa", "Uberlândia", "MG", "Assets/assetsongs/apaMG.png", "13966133660"),
    criarOngs("Bichos Gerais", "Belo Horizonte", "MG", "Assets/assetsongs/bichosgeraisMG.png", "13966133660"),
    criarOngs("Cão Viver", " Contagem", "MG", "Assets/assetsongs/caoviverMG.png", "13966133660"),
    // RJ
    criarOngs("AçãoAnimal", "Rio de Janeiro", "RJ", "Assets/assetsongs/acaoanimalRJ.png", "13966133660"),
    criarOngs("Adote um Bichinho", "Rio de Janeiro", "RJ", "Assets/assetsongs/adotebichRJ.png", "13966133660"),
    criarOngs("Cãodominio", "Resende", "RJ", "Assets/assetsongs/caodominioRJ.webp.png", "13966133660"),
    criarOngs("Distrito Animal", "Rio de Janeiro", "RJ", "Assets/assetsongs/distanimalRJ.jpg", "13966133660"),
    criarOngs("Fazenda Modelo", "Guaratiba", "RJ", "Assets/assetsongs/fazendamodeloRJ.png", "13966133660"),
    criarOngs("Paraíso dos animais", "Guaratiba", "RJ", "Assets/assetsongs/paraisofucinRJ.png", "13966133660"),
    // SP
    criarOngs("Alianima", "São Paulo", "SP", "Assets/assetsongs/alianimaSP.png", "13966133660"),
    criarOngs("Amor Animal", "São Paulo", "SP", "Assets/assetsongs/amoranimalSP.png", "13966133660"),
    criarOngs("Associção Apelos e Patas", "São Paulo", "SP", "Assets/assetsongs/apelosepatasSP.webp.png", "13966133660"),
    criarOngs("Cão Sem Dono", "Campinas", "SP", "Assets/assetsongs/caosemdonoSP.jpg", "13966133660"),
    criarOngs("ONG SOS", "São Caetano do Sul", "SP", "Assets/assetsongs/ongsosSP.jpg", "13966133660"),
    // GO
    criarOngs("Anjos da rua", "Goiânia", "GO", "Assets/assetsongs/anjdaruaGO.jpg", "13966133660"),
    criarOngs("Lar dos animais", "Goiânia", "GO", "Assets/assetsongs/lardosanimGO.png", "13966133660"),
    criarOngs("PROANIMA", "Brasília", "GO", "Assets/assetsongs/proanimaGO.png", "13966133660"),
    criarOngs("SOS animal", "Goiânia", "GO", "Assets/assetsongs/sosanimalGO.png", "13966133660"),
    
]

let quantidadeVisivel = 6;
let listaFiltrada = [...ongsData];

const container = document.querySelector(".ONGs");

function renderOngs() {
    container.innerHTML = "";

    const visiveis = listaFiltrada.slice(0, quantidadeVisivel);

    visiveis.forEach(ong => {
        container.innerHTML += `
            <article class="ONGs-card">

                <h3>${ong.nome}</h3>
                <p>${ong.cidade}-${ong.regiao}</p>

                <div class="img-wrapper">
                    <img src="${ong.imagem}" alt="${ong.nome}">
                </div>

                <div class="pix-box">
                    <p>Chave PIX:</p>
                    <span>${ong.pix}</span>
                </div>

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

function aplicarFiltroOng() {
    const select = document.getElementById("estados");
    const valor = select.value;

    listaFiltrada = ongsData.filter(ong => {
        if (!valor) return true;
        return ong.regiao === valor;
    });

    quantidadeVisivel = 6;
    renderOngs();
}

document.getElementById("verMais").addEventListener("click", () => {
    quantidadeVisivel += 6;
    renderOngs();
});

document.getElementById("estados").addEventListener("change", aplicarFiltroOng);

renderOngs();