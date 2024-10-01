
// Event listener for the send button
document.getElementById("send-btn").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value;
    
    if (userInput.trim() !== "") {
        addMessage("user-message", userInput);
        document.getElementById("user-input").value = "";  // Clear input field

        // Call Azure OpenAI API and get the response
        const botResponse = await getOpenAiResponse(userInput);
        
        // Display the bot response
        addMessage("bot-message", botResponse.response || "Sorry, I couldn't process the response.");
    }
});

// Function to add messages to the chat UI
function addMessage(type, message) {
    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message", type);
    messageContainer.textContent = message;
    document.getElementById("chat-box").appendChild(messageContainer);
    document.getElementById("chat-box").scrollTop = document.getElementById("chat-box").scrollHeight;
}

// Function to get the bot response from Azure OpenAI API
async function getOpenAiResponse(prompt) {
    try {
        const res = await fetch('https://random-trude-sandeep-projects-f4a7f20e.koyeb.app/',{
            method:'POST',
            body:JSON.stringify({
                'prompt':prompt
            })
        })
        const data = await res.json()
        return data.response
    } catch (error) {
        console.error(error)
    }
}
