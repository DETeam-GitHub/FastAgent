import openai as oai

class FastAgent:
    def __init__(self, api_key, base_url="https://open.bigmodel.cn/api/paas/v4/"):
        self.oai_client = oai.OpenAI(api_key=api_key,base_url=base_url)
    
    def chat(self, messages:list, model="glm-4-flash",**kwargs):
        msg = messages.copy()
        completion = self.oai_client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs
        )
        msg.append({"role": "assistant", "content": completion.choices[0].message.content})
        return completion.choices[0].message.content