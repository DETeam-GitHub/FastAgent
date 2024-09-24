"""
内省工具
"""

import inspect
from typing import Any, Dict, Optional

def get_function_info(func: callable) -> Dict[str, Any]:
    """
    获取给定函数的所有参数及其类型，并获取函数的返回值类型和函数名称。
    
    参数:
    func (callable): 要检查的函数。
    
    返回:
    dict: 包含函数名称、参数名称、类型和返回值类型的字典。
    """
    # 获取函数签名
    signature = inspect.signature(func)
    
    # 解析参数和类型注解
    parameters = {}
    for name, param in signature.parameters.items():
        # 获取参数类型注解
        annotation = param.annotation
        if annotation is inspect.Parameter.empty:
            annotation = None
        parameters[name] = {
            'default': param.default,
            'annotation': annotation
        }
    
    # 获取返回值类型注解
    return_annotation = signature.return_annotation
    if return_annotation is inspect.Signature.empty:
        return_annotation = None
    
    # 获取函数名称
    function_name = func.__name__
    
    # 构建最终结果
    result = {
        'function_name': function_name,
        'parameters': parameters,
        'return_type': return_annotation
    }
    
    return result
