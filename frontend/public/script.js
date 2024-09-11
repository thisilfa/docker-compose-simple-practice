// config.js
const apiBaseUrl = window.API_BASE_URL;

const config = {
    apiBaseUrl: apiBaseUrl,
};

// Function to display a message in the responseMessage div
function showMessage(message, isSuccess) {
    const messageDiv = document.getElementById('responseMessage');
    messageDiv.innerText = isSuccess ? `OK: ${message}` : `Error: ${message}`;
    messageDiv.style.color = isSuccess ? 'green' : 'red';
}

// Handle form submission for adding an item
document.getElementById("itemForm").addEventListener("submit", function(event){
    event.preventDefault(); // Prevent form from submitting the normal way

    let formData = new FormData(this);

    fetch(`${config.apiBaseUrl}/add_item`, {
        method: "POST",
        body: formData
    })
    .then(response => response.json().then(data => ({status: response.status, body: data})))
    .then(({status, body}) => {
        const isSuccess = status >= 200 && status < 300;
        showMessage(body.message || body.error, isSuccess);
        document.getElementById("itemForm").reset()
    })
    .catch(error => {
        showMessage("An error occurred while adding the item.", false);
        document.getElementById("itemForm").reset()
    });
});

// Handle form submission for deleting an item
document.getElementById("deleteForm").addEventListener("submit", function(event){
    event.preventDefault(); // Prevent form from submitting the normal way

    let itemId = document.getElementById("item_id").value;

    fetch(`${config.apiBaseUrl}/delete_item/${itemId}`, {
        method: "DELETE",
    })
    .then(response => response.json().then(data => ({status: response.status, body: data})))
    .then(({status, body}) => {
        const isSuccess = status >= 200 && status < 300;
        showMessage(body.message || body.error, isSuccess);
        document.getElementById("deleteForm").reset();
    })
    .catch(error => {
        showMessage("An error occurred while deleting the item.", false);
        document.getElementById("deleteForm").reset();
    });
});