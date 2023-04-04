const mainMenuBtn = document.querySelector("#mainMenuBtn");
const mobileMenu = document.querySelector("#mobileMenu");
const closeBtn = document.querySelector("#closeBtn");

mainMenuBtn.addEventListener("click", () => {
  mainMenuBtn.classList.toggle("hidden");
  mobileMenu.classList.toggle("hidden");
});

closeBtn.addEventListener("click", () => {
  mainMenuBtn.classList.toggle("hidden");
  mobileMenu.classList.toggle("hidden");
});
