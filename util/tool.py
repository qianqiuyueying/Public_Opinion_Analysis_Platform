import bcrypt
from datetime import datetime

class PasswordManager:
    """
    密码管理器，用于对密码进行加密和验证
    """
    @staticmethod
    def hash_password(password: str) -> str:
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
        return str(hashed_password, 'utf-8')

    @staticmethod
    def check_password(hashed_password: str, password: str) -> bool:
        """
        验证密码是否正确
        :param hashed_password: 加密后的密码（字节串）
        :param password: 用户输入的原始密码（字符串）
        :return: 如果密码正确返回 True，否则返回 False
        """
        # 将用户输入的密码转换为字节串
        password_bytes = password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        print(password_bytes, hashed_password_bytes)
        # 使用 bcrypt 比较用户输入的密码和存储的加密密码
        return bcrypt.checkpw(password_bytes, hashed_password_bytes)
    
def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


import yagmail
from random import randint
def send_verify_code(email: str) -> None:
    """
    发送验证码
    :param email: 邮箱地址
    :param code: 验证码
    """
    code = randint(1000, 9999)
    msg = MIMEText(f'您的验证码是：{code}', 'plain', 'utf-8')
    msg['Subject'] = '舆情分析平台注册验证码'
    msg['From'] = 'qianqiuyueying@outlook.com'
    msg['To'] = email
    msg.attach(msg)