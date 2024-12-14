from zhipuai import ZhipuAI
import json
from .functodict import decorator
# from rich import print


def object_to_dict(obj):
    if hasattr(obj, "__dict__"):
        return {key: object_to_dict(value) for key, value in obj.__dict__.items()}
    elif isinstance(obj, (int, float, str, list, dict, tuple)):
        return obj
    else:
        return str(obj)


class FastAgent:
    def __init__(self, api_key, base_url="https://open.bigmodel.cn/api/paas/v4/"):
        """
        初始化FastAgent类

        参数:
        - api_key: str, API密钥，用于认证
        - base_url: str, API基础URL，默认为智谱的API地址
        """
        # 使用提供的API密钥和基础URL初始化OpenAI客户端
        self.oai_client = ZhipuAI(api_key=api_key)
        self.tools = {}
        self.tool_prompt = []
        self.nt:set = set()

    def chat(self, messages: list, user: str, model="glm-4-flash", **kwargs):
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
        notool=False
        while True:
            # 将用户的新消息添加到聊天历史中
            if messages != "":
                msg.append({"role": "user", "content": user})
            # 使用OpenAI客户端创建聊天完成请求
            if notool:
                completion = self.oai_client.chat.completions.create(
                    model=model, messages=msg
                )
            else:
                completion = self.oai_client.chat.completions.create(
                    model=model, messages=msg, tools=self.tool_prompt
                )

            if completion.choices[0].finish_reason == "stop":
                # 将模型的回复添加到聊天历史中
                msg.append(
                    {"role": "assistant", "content": completion.choices[0].message.content}
                )
                # 返回更新后的聊天历史和对话完成对象
                return msg, completion
            elif completion.choices[0].finish_reason == "tool_calls":

                # 将模型的回复添加到聊天历史中
                # xm = dict(completion.choices[0].message.tool_calls[0])
                # xm["function"] = dict(xm["function"])
                # print(xm)
                # msg.append({"role": "assistant", "tool_calls": xm})
                # print(msg[-1])
                funcall = completion.choices[0].message.tool_calls[0].function

                fkw = json.loads(funcall.arguments)
                x = self.tools[funcall.name](**fkw)
                # print(x)
                msg.append({"role": "tool", "content": x})
                if funcall.name in self.nt:
                    notool = True


    def tool(self,nt:bool = False, **kwargs):
        """
        定义了一个名为tool的函数，该函数是当前类的方法。

        参数：
        - description: str, 对工具的描述。
        - **kwargs: 额外的关键字参数，允许调用者传入任意数量的额外参数。

        返回值：
        - 目前该函数未实现具体功能，仅作为占位符存在。
        """

        # TODO: 在这里实现具体的功能逻辑
        

            
        def at(func):
            if nt:
                self.nt.add(func.__name__)
            x = decorator(func, kwargs)
            self.tools[func.__name__] = func
            self.tool_prompt.append(x)

        return at
