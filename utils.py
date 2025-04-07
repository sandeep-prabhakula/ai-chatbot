from openai import AzureOpenAI



def getOpenAiResponse(prompt):

    response={}
    
    try:
        client = OpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key="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",
                )

        completion = client.chat.completions.create(
                        extra_body={},
                        model="deepseek/deepseek-r1-distill-llama-70b:free",
                        messages=[
                                {
                                    "role": "user",
                                    "content":prompt
                                }
                            ]
                    )
        finalResponse=airesponse.choices[0].message.content


        response['response']=finalResponse
                    
        
    except Exception as e:
        print("Exception : "+str(e))


    return response