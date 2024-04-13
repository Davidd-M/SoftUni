window.addEventListener("load", solve);

function solve() {
    // Selecting the elements
    const nameInput = document.getElementById("name");
    const phoneInput = document.getElementById("phone");
    const categorySelect = document.getElementById("category");
    const addButton = document.getElementById("add-btn");
    const checkList = document.getElementById("check-list");
    const contactList = document.getElementById("contact-list");

    // Function to create a new contact item
    function createContactItem(name, phone, category, isSaved) {
        // Create list item
        const listItem = document.createElement("li");

        // Create article element
        const article = document.createElement("article");

        // Add name, phone, and category as paragraphs inside the article
        const nameParagraph = document.createElement("p");
        nameParagraph.textContent = `name:${name}`;
        article.appendChild(nameParagraph);

        const phoneParagraph = document.createElement("p");
        phoneParagraph.textContent = `phone:${phone}`;
        article.appendChild(phoneParagraph);

        const categoryParagraph = document.createElement("p");
        categoryParagraph.textContent = `category:${category}`;
        article.appendChild(categoryParagraph);

        // Append article to list item
        listItem.appendChild(article);

        if (!isSaved) {
            // Create div for buttons
            const buttonsDiv = document.createElement("div");
            buttonsDiv.classList.add("buttons");

            // Create edit button
            const editButton = document.createElement("button");
            editButton.textContent = "Edit";
            editButton.classList.add("edit-btn");
            buttonsDiv.appendChild(editButton);

            // Create save button
            const saveButton = document.createElement("button");
            saveButton.textContent = "Save";
            saveButton.classList.add("save-btn");
            buttonsDiv.appendChild(saveButton);

            // Append buttonsDiv to listItem
            listItem.appendChild(buttonsDiv);
        } else {
            // Create delete button
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "Delete";
            deleteButton.classList.add("del-btn");
            listItem.appendChild(deleteButton);
        }

        return listItem;
    }

    // Adding event listener to the Add button
    addButton.addEventListener("click", function() {
        // Get the values from the input fields
        const name = nameInput.value.trim();
        const phone = phoneInput.value.trim();
        const category = categorySelect.value;

        // Check if any of the input fields are empty
        if (name === "" || phone === "" || category === "") {
            // If any of them are empty, do nothing
            return;
        }

        // Create a new contact item
        const contactItem = createContactItem(name, phone, category, false);

        // Append the contact item to the check-list
        checkList.appendChild(contactItem);

        // Clear the input fields after adding the contact
        nameInput.value = "";
        phoneInput.value = "";
        categorySelect.value = "";
    });

    // Adding event listener to the check-list
    checkList.addEventListener("click", function(event) {
        const target = event.target;
        // Check if the clicked element is a save button
        if (target.classList.contains("save-btn")) {
            let listItem = target;
            while (listItem && listItem.nodeName !== "LI") {
                listItem = listItem.parentNode;
            }

            // Remove the save button
            const buttonsDiv = listItem.querySelector(".buttons");
            buttonsDiv.removeChild(target);

            // Remove the edit button
            const editButton = buttonsDiv.querySelector(".edit-btn");
            editButton.remove();

            // Create delete button
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "Delete";
            deleteButton.classList.add("del-btn");
            listItem.appendChild(deleteButton);

            // Remove edit and save buttons from the contact item
            const savedButtonsDiv = listItem.querySelector(".buttons");
            savedButtonsDiv.remove();

            // Create a new contact item with the same information
            const article = listItem.querySelector("article");
            const name = article.querySelector("p:nth-child(1)").textContent.split(":")[1];
            const phone = article.querySelector("p:nth-child(2)").textContent.split(":")[1];
            const category = article.querySelector("p:nth-child(3)").textContent.split(":")[1];
            const savedContactItem = createContactItem(name, phone, category, true);

            // Append the new contact item to the contact-list
            contactList.appendChild(savedContactItem);

            // Remove the contact from the check-list
            listItem.remove();
        }

        // Check if the clicked element is an edit button
        if (target.classList.contains("edit-btn")) {
            let listItem = target;
            while (listItem && listItem.nodeName !== "LI") {
                listItem = listItem.parentNode;
            }
            // Get the article element containing contact information
            const article = listItem.querySelector("article");
            // Get the contact information
            const name = article.querySelector("p:nth-child(1)").textContent.split(":")[1];
            const phone = article.querySelector("p:nth-child(2)").textContent.split(":")[1];
            const category = article.querySelector("p:nth-child(3)").textContent.split(":")[1];

            // Populate the input fields with the contact information
            nameInput.value = name;
            phoneInput.value = phone;
            categorySelect.value = category;

            // Remove the contact from the check-list
            listItem.remove();
        }
    });

    // Adding event listener to the contact-list for delete button
    contactList.addEventListener("click", function(event) {
        const target = event.target;
        // Check if the clicked element is a delete button
        if (target.classList.contains("del-btn")) {
            // Get the parent li element and remove it from the contact-list
            let listItem = target;
            while (listItem && listItem.nodeName !== "LI") {
                listItem = listItem.parentNode;
            }
            listItem.remove();
        }
    });
}
