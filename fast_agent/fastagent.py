import openai as oai

class FastAgent:
    def __init__(self, api_key, base_url="https://open.bigmodel.cn/api/paas/v4/"):
        """
        初始化FastAgent类
        
        参数:
        - api_key: str, OpenAI API密钥，用于认证
        - base_url: str, API基础URL，默认为阿里云通义系列模型的API地址
        """
        # 使用提供的API密钥和基础URL初始化OpenAI客户端
        self.oai_client = oai.OpenAI(api_key=api_key,base_url=base_url)
    
    def chat(self, messages:list, user:str, model="glm-4-flash",**kwargs):
        """
        与指定模型进行聊天
        
        参数:
        - messages: list, 聊天历史，包含之前发送和接收的消息
        - user: str, 用户发送的消息
        - model: str, 使用的模型名称，默认为'glm-4-flash'
        - **kwargs: 额外参数，如温度、最大tokens等
        
        返回:
        - msg: list, 更新后的聊天历史，包括最新的用户和助手消息
        - completion: 对话完成对象，包含模型回复的信息
        """
        # 从messages参数中复制聊天历史，避免直接修改原始数据
        msg = messages.copy()
        # 将用户的新消息添加到聊天历史中
        msg.append({"role": "user", "content": user})
        # 使用OpenAI客户端创建聊天完成请求
        completion = self.oai_client.chat.completions.create(
            model=model,
            messages=msg,
            tools=[],
            **kwargs
        )
        # 将模型的回复添加到聊天历史中
        msg.append({"role": "assistant", "content": completion.choices[0].message.content})
        # 返回更新后的聊天历史和对话完成对象
        return msg,completion
    
    def tool(self,name: str,**kwargs):
        """
        定义一个工具函数，目前未实现具体功能
        
        参数:
        - name: str, 工具的名称
        - **kwargs: 额外参数，根据工具的不同可能需要不同的参数
        """
        pass