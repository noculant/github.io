document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("data-form");
    const messageBox = document.createElement("div");
  
    form.addEventListener("submit", async function (event) {
      event.preventDefault();
  
      const formData = new FormData(form);
      const response = await fetch("/", {
        method: "POST",
        body: formData,
      });
      const result = await response.json();
  
      if (result.status === "success") {
        messageBox
  