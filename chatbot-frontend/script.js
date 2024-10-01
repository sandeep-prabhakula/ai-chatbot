
// Event listener for the send button
document.getElementById("send-btn").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value;
    
    if (userInput.trim() !== "") {
        addMessage("user-message", userInput);
        document.getElementById("user-input").value = "";  // Clear input field

        // Call Azure OpenAI API and get the response
        const botResponse = await getOpenAiResponse(userInput);
        console.log(botResponse)
        // Display the bot response
        addMessage("bot-message", botResponse || "Sorry, I couldn't process the response.");
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
    const requestData = {
        'prompt':prompt
    }
    console.log(requestData)
    try {
        // const res = await fetch('https://random-trude-sandeep-projects-f4a7f20e.koyeb.app/',{
        const res = await fetch('http://localhost:8080/',{
            method: "POST",  // Specify the request method
            headers: {
                "Content-Type": "application/json"  // Send JSON data
            },
            body: JSON.stringify(requestData)
        })
        const data = await res.json()
        console.log(data)
        return data.response
    } catch (error) {
        console.error(error)
    }
}
