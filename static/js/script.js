document.addEventListener("DOMContentLoaded", function () { // Sets up event listener that exectures once content is loaded
    const form = document.getElementById("data-form"); // Selects data-form ID element
    const messageBox = document.createElement("div"); // This line creates a new div element
  
    form.addEventListener("submit", async function (event) { // Sets up event listener for submit
      event.preventDefault(); // Prevents the default form from reloading the page
  
      const formData = new FormData(form); // Creates a formData object to sent to server
      const response = await fetch("/", { // Sends a asynchronous request to the server using fetch function
        method: "POST", // Sets up HTTP request method to post
        body: formData, // Sets the request body to formData
      });
      const result = await response.json(); // Reads the response from the server as JSON
  
      if (result.status === "success") { // Checks whether server response was a success
        messageBox
  