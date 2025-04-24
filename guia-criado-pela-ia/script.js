const searchBar = document.getElementById('searchBar');
const sections = document.querySelectorAll('.section');

searchBar.addEventListener('input', () => {
  const query = searchBar.value.toLowerCase();

  sections.forEach(section => {
    const keywords = section.getAttribute('data-keywords');
    if (keywords.includes(query) || query === '') {
      section.classList.remove('hidden');
    } else {
      section.classList.add('hidden');
    }
  });
});

function abrirModal(tipo) {
  const imagemModal = document.getElementById("imagemModal");
  const modal = document.getElementById("modal");

  const imagens = {
    Gelo: "img/gelo.png",
    Fogo: "img/fogo.png",
    Terra: "img/terra.png",
    Buff: "img/buff.png",
    Passiva: "img/passivas.png",
    Dainn: "img/dain.png",
  };

  imagemModal.src = imagens[tipo];
  modal.style.display = "block";
}

function fecharImagem() {
  document.getElementById("modal").style.display = "none";
}
