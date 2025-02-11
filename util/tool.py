import bcrypt
from datetime import datetime

class PasswordManager:
    """
    密码管理器，用于对密码进行加密和验证
    """
    @staticmethod
    def hash_password(password: str) -> bytes:
        """
        使用 bcrypt 加密密码
        :param password: 原始密码（字符串）
        :return: 加密后的密码（字节串）
        """
        # 将密码转换为字节串
        password_bytes = password.encode('utf-8')
        # 生成盐（salt），盐是随机生成的，用于增加密码的安全性
        salt = bcrypt.gensalt()
        # 使用盐对密码进行加密
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password

    @staticmethod
    def check_password(hashed_password: bytes, password: str) -> bool:
        """
        验证密码是否正确
        :param hashed_password: 加密后的密码（字节串）
        :param password: 用户输入的原始密码（字符串）
        :return: 如果密码正确返回 True，否则返回 False
        """
        # 将用户输入的密码转换为字节串
        password_bytes = password.encode('utf-8')
        # 使用 bcrypt 比较用户输入的密码和存储的加密密码
        return bcrypt.checkpw(password_bytes, hashed_password)
    
def now() -> str:
    """
    获取当前时间的字符串表示
    :return: 当前时间的字符串，格式为 'YYYY-MM-DD HH:MM:SS'
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


import yagmail
from random import randint
def send_verify_code(email: str, code: int) -> None:
    """
    发送验证码
    :param email: 邮箱地址
    :param code: 验证码
    """
    yag = yagmail.SMTP(user="3044481323@qq.com", password="nmosvcwlzswhdcfg", host='smtp.qq.com', encoding='utf-8')
    content = f"您的验证码是：{code}"
    yag.send(email, '舆情分析平台注册', content)
    yag.close()