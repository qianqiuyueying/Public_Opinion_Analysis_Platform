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

def send_verify_code_to_email(username: str, email: str, code: int) -> None:
    """
    发送验证码
    :param username: 用户名
    :param email: 邮箱地址
    :param code: 验证码
    """
    # 邮件主题
    subject = "【舆情分析平台】邮箱验证码"

    # 邮件正文模板
    content = f"""
尊敬的 {username}，您好！

您正在注册舆情分析平台账号，本次请求的验证码为：

{code}

请在 10 分钟内使用该验证码完成验证。

如非本人操作，请忽略此邮件。

感谢您对舆情分析平台的支持！

舆情分析平台
{now()}
"""

    # 使用 yagmail 发送邮件
    yag = yagmail.SMTP(user="3044481323@qq.com", password="nmosvcwlzswhdcfg", host='smtp.qq.com', encoding='utf-8')
    yag.send(to=email, subject=subject, contents=content)
    yag.close()



import jwt
from config import SECRET_KEY, ALGORITHM
def create_access_token(data: dict):
    """
    生成token
    """
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

from fastapi import Request, HTTPException
async def get_current_user(request: Request):
    """
    当前用户的token并解析
    获得username, id, role
    """
    user = request.state.user
    if not user: 
        raise HTTPException(status_code=401, detail="未登录")
    return user


from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def get_time(timestamp):
    timestamp /= 1000
    dt_utc = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    dt = dt_utc.astimezone(ZoneInfo("Asia/Shanghai"))
    return dt