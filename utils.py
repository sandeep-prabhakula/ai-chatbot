from openai import OpenAI
import os


def getOpenAiResponse(prompt):

    response={}
    
    try:
        apiKey = os.getenv("OPENAI_API_KEY")
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
      "content":prompt
    }
  ]
)
        finalResponse=completion.choices[0].message.content


        response['response']=finalResponse
                    
        
    except Exception as e:
        print(e)


    return response