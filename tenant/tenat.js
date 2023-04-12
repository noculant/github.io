// Sample data for tenants
let tenants = [	{name: "John Doe", apartment_number: "101", rate: "$1000"},	{name: "Jane Smith", apartment_number: "102", rate: "$1200"},	{name: "Bob Johnson", apartment_number: "201", rate: "$900"}];

// Function to display all tenants in the table
function displayTenants() {
	let tenantList = document.getElementById("tenant-list");

	// Clear any existing rows
	tenantList.innerHTML = "";

	// Add each tenant to the table
	for (let i = 0; i < tenants.length; i++) {
		let tenant = tenants[i];

		let row = document.createElement("tr");

		let nameCell = document.createElement("td");
		nameCell.textContent = tenant.name;
		row.appendChild(nameCell);

		let apartmentCell = document.createElement("td");
		apartmentCell.textContent = tenant.apartment_number;
		row.appendChild(apartmentCell);

		let rateCell = document.createElement("td");
		rateCell.textContent = tenant.rate;
		row.appendChild(rateCell);

		let actionsCell = document.createElement("td");
		actionsCell.innerHTML = '<button onclick="editTenant(' + i + ')">Edit</button> <button onclick="deleteTenant(' + i + ')">Delete</button>';
		row.appendChild(actionsCell);

		tenantList.appendChild(row);
	}
}

// Function to add a new tenant
function addTenant(event) {
	event.preventDefault();

	let form = document.getElementById("add-tenant-form");

	let name = form.elements["tenant-name"].value;
	let apartmentNumber = form.elements["apartment-number"].value;
	let rate = form.elements["rate"].value;

	let tenant = {name: name, apartment_number: apartmentNumber, rate: rate};
	tenants.push(tenant);

	displayTenants();

	form.reset();
}

// Function to edit an existing tenant
function editTenant(index) {
	let tenant = tenants[index];

	let name = prompt("Enter new name:", tenant.name);
	if (name === null) {
		return; // User clicked cancel
	}

	let apartmentNumber = prompt("Enter new apartment number:", tenant.apartment_number);
	if (apartmentNumber === null) {
		return; // User clicked cancel
	}

	let rate = prompt("Enter new rate:", tenant.rate);
	if (rate === null) {
		return; // User clicked cancel
	}

	tenant.name = name;
	tenant.apartment_number = apartmentNumber;
	tenant.rate = rate;

	displayTenants();
}

// Function to delete an existing tenant
function deleteTenant(index) {
	if (confirm("Are you sure you want to delete this tenant?")) {
		tenants.splice(index, 1);
		displayTenants();
	}
}

// Call the displayTenants function to initially populate the table
displayTenants();

// Add event listener for form submission
let addTenantForm = document.getElementById("add-tenant-form");
addTenantForm.addEventListener("submit", addTenant);
