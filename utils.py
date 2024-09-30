from openai import AzureOpenAI



def getOpenAiResponse(prompt):

    response={}
    
    try:
        client = AzureOpenAI(
            api_key="ee0b7f3478a547debc73164b67414934",
            api_version="2024-05-01-preview",
            azure_endpoint = "https://azureopenaiinstance.openai.azure.com"
            )
        
        airesponse = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                { "role": "system", "content": "You are a helpful assistant." },
                { "role": "user", "content":  prompt} 
            ],

        )
        finalResponse=airesponse.choices[0].message.content


        response['response']=finalResponse
                    
        
    except Exception as e:
        print(e)


    return response