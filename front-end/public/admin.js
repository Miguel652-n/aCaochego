const API_URL = "https://acaochego-production.up.railway.app";

  // credenciais simples (altere aqui)
  const USUARIO = "admin";
  const SENHA   = "acaochego2025";

  let todosColabs = [];

  function fazerLogin() {
    const u = document.getElementById("usuario").value;
    const s = document.getElementById("senha").value;
    if (u === USUARIO && s === SENHA) {
      document.getElementById("tela-login").style.display = "none";
      document.getElementById("tela-admin").style.display = "block";
      carregarColabs();
    } else {
      document.getElementById("erro-login").style.display = "block";
    }
  }

  document.addEventListener("keydown", e => {
    if (e.key === "Enter" && document.getElementById("tela-login").style.display !== "none") {
      fazerLogin();
    }
  });

  function sair() {
    document.getElementById("tela-login").style.display = "flex";
    document.getElementById("tela-admin").style.display = "none";
    document.getElementById("usuario").value = "";
    document.getElementById("senha").value = "";
  }

  async function carregarColabs() {
    const tbody = document.getElementById("tabela-body");
    tbody.innerHTML = `<tr><td colspan="7"><div class="estado"><i class="bi bi-hourglass-split"></i>Carregando...</div></td></tr>`;

    try {
      const res = await fetch(`${API_URL}/colabs`);
      todosColabs = await res.json();

      atualizarResumo();
      atualizarFiltroAnimal();
      filtrar();

      const agora = new Date().toLocaleTimeString("pt-br");
      document.getElementById("ultimo-update").textContent = `Atualizado às ${agora}`;

    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="7"><div class="estado"><i class="bi bi-wifi-off"></i>Erro ao conectar com a API</div></td></tr>`;
    }
  }

  function atualizarResumo() {
    const comAnimal = todosColabs.filter(c => c.animal && c.animal.trim() !== "").length;
    document.getElementById("total-colabs").textContent    = todosColabs.length;
    document.getElementById("total-com-animal").textContent = comAnimal;
    document.getElementById("total-sem-animal").textContent = todosColabs.length - comAnimal;
  }

  function atualizarFiltroAnimal() {
    const sel = document.getElementById("filtro-animal");
    const atual = sel.value;
    const animais = [...new Set(todosColabs.map(c => c.animal).filter(Boolean))].sort();
    sel.innerHTML = `<option value="">Todos os animais</option>`;
    animais.forEach(a => {
      const op = document.createElement("option");
      op.value = a;
      op.textContent = a;
      if (a === atual) op.selected = true;
      sel.appendChild(op);
    });
  }

  function filtrar() {
    const busca  = document.getElementById("busca").value.toLowerCase();
    const animal = document.getElementById("filtro-animal").value;

    const resultado = todosColabs.filter(c => {
      const matchBusca  = !busca  || c.nome.toLowerCase().includes(busca) || c.email.toLowerCase().includes(busca);
      const matchAnimal = !animal || c.animal === animal;
      return matchBusca && matchAnimal;
    });

    renderTabela(resultado);
    document.getElementById("rodape").textContent =
      `Mostrando ${resultado.length} de ${todosColabs.length} cadastros`;
  }

  function renderTabela(lista) {
    const tbody = document.getElementById("tabela-body");

    if (lista.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7"><div class="estado"><i class="bi bi-search"></i>Nenhum resultado encontrado</div></td></tr>`;
      return;
    }

    tbody.innerHTML = lista.map((c, i) => `
      <tr>
        <td style="color:#bbb;font-size:13px;">${c.id}</td>
        <td class="nome-col" style="cursor:pointer;" onclick="abrirModal(${c.id})">${c.nome}</td>
        <td>${c.email}</td>
        <td>${c.number || "—"}</td>
        <td>${c.cidade || "—"} / ${c.estado || "—"}</td>
        <td>${c.animal ? `<span class="tag-animal">${c.animal}</span>` : `<span class="tag-sem">não informado</span>`}</td>
        <td>
          <button class="btn-deletar" onclick="deletar(${c.id}, event)" title="Remover">
            <i class="bi bi-trash3"></i>
          </button>
        </td>
      </tr>
    `).join("");
  }

  function abrirModal(id) {
    const c = todosColabs.find(x => x.id === id);
    if (!c) return;

    document.getElementById("modal-nome").textContent = c.nome;
    document.getElementById("modal-conteudo").innerHTML = `
      <div class="modal-linha"><span class="modal-label">Email</span><span class="modal-valor">${c.email}</span></div>
      <div class="modal-linha"><span class="modal-label">Contato</span><span class="modal-valor">${c.number || "—"}</span></div>
      <div class="modal-linha"><span class="modal-label">Endereço</span><span class="modal-valor">${c.endereco || "—"}</span></div>
      <div class="modal-linha"><span class="modal-label">Cidade / Estado</span><span class="modal-valor">${c.cidade || "—"} / ${c.estado || "—"}</span></div>
      <div class="modal-linha"><span class="modal-label">CEP</span><span class="modal-valor">${c.cep || "—"}</span></div>
      <div class="modal-linha"><span class="modal-label">Animal desejado</span><span class="modal-valor">${c.animal || "Não informado"}</span></div>
      <div class="modal-linha"><span class="modal-label">Descrição</span><span class="modal-valor">${c.descricao || "—"}</span></div>
    `;

    document.getElementById("overlay").classList.add("ativo");
  }

  function fecharModal(e) {
    if (e.target === document.getElementById("overlay")) {
      document.getElementById("overlay").classList.remove("ativo");
    }
  }

  async function deletar(id, e) {
    e.stopPropagation();
    if (!confirm("Remover este cadastro?")) return;

    try {
      await fetch(`${API_URL}/colabs/${id}`, { method: "DELETE" });
      todosColabs = todosColabs.filter(c => c.id !== id);
      atualizarResumo();
      atualizarFiltroAnimal();
      filtrar();
    } catch (err) {
      alert("Erro ao deletar.");
    }
  }