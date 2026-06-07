"""
Utils.py - 工具函数模块
功能：提供通用的辅助函数
"""


# 2026-06-07 更新
def find_key_by_value(d: dict, val, default=None):
    for k, v in d.items():
        if v == val:
            return k
    return default
