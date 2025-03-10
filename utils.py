from openai import OpenAI



def getOpenAiResponse(prompt):

    response={}
    
    try:
        client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

        completion = client.chat.completions.create(
  extra_body={},
  model="qwen/qwen2.5-vl-72b-instruct:free",
#   model="deepseek/deepseek-r1-distill-llama-70b:free",
  messages=[
    {
      "role": "user",
      "content":"what is chain of thought prompting"
    }
  ]
)
        finalResponse=completion.choices[0].message.content


        response['response']=finalResponse
                    
        
    except Exception as e:
        print(e)


    return response