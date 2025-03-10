
// Event listener for the send button
document.getElementById("send-btn").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        addMessage("user-message", userInput);
        document.getElementById("user-input").value = "";  // Clear input field
        
        // Call Azure OpenAI API and get the response
        const botResponse = await getOpenAiResponse(userInput);
    
        // Display the bot response
        addMessage("bot-message", marked.parse(botResponse || "Sorry, I couldn't process the response."));
        
        
    }
});
function showLoadingSpinner() {
    // const loadingSpinner = document.getElementById("loading-spinner");
    // loadingSpinner.classList.remove("hidden");
    document.getElementById("spinner").style.display = "flex";
    document.getElementById("spinner").style.alignItems = "center";
    document.getElementById("spinner").style.justifyContent = "center";
}

// Function to hide the loading spinner
function hideLoadingSpinner() {
    // const loadingSpinner = document.getElementById("loading-spinner");
    // loadingSpinner.classList.add("hidden");
    document.getElementById("spinner").style.display = "none";
}

// Function to add messages to the chat UI
function addMessage(type, message) {
    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message", type);
    messageContainer.innerHTML = message;
    document.getElementById("chat-box").appendChild(messageContainer);
    document.getElementById("chat-box").scrollTop = document.getElementById("chat-box").scrollHeight;
    hideLoadingSpinner()
}

// Function to get the bot response from Azure OpenAI API
async function getOpenAiResponse(prompt) {
    showLoadingSpinner()
    const requestData = {
        'prompt':prompt
    }

    try {
        // const res = await fetch('https://random-trude-sandeep-projects-f4a7f20e.koyeb.app/',{
        const res = await fetch('https://random-trude-sandeep-projects-f4a7f20e.koyeb.app/',{
            method: "POST",  // Specify the request method
            headers: {
                "Content-Type": "application/json"  // Send JSON data
            },
            body: JSON.stringify(requestData)
        })
        const data = await res.json()
        return data.response
    } catch (error) {
        console.error(error)
    }
}
