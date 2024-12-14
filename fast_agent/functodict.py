"""
内省工具
"""

import inspect

def decorator(func,kwargs):
    # 获取函数签名
    sig = inspect.signature(func)
    
    # 获取函数文档字符串
    doc = func.__doc__
    
    # 生成参数描述
    parameters = {
        "type": "object",
        "properties": {},
        "required": [],
    }
    
    for param_name, param in sig.parameters.items():
        if param_name in kwargs:
            description = kwargs[param_name]
            param_type = param.annotation
            
            # 根据参数类型生成描述
            if param_type == int:
                param_type_str = "int"
            elif param_type == str:
                param_type_str = "string"
            elif param_type == float:
                param_type_str = "float"
            elif param_type == bool:
                param_type_str = "bool"
            elif param_type == list:
                param_type_str = "list"
            elif param_type == dict:
                param_type_str = "dict"
            else:
                param_type_str = "any"
            
            parameters["properties"][param_name] = {
                "type": param_type_str,
                "description": description,
            }
            if param.default == inspect.Parameter.empty:
                parameters["required"].append(param_name)
    
    # 生成函数描述
    function_description = {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": doc.strip(),
            "parameters": parameters,
        },
    }
    
    
    return function_description
