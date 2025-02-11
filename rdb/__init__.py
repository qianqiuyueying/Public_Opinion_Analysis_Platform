import redis

# 配置
redis_config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
}

# 创建 Redis 连接
redis_client = redis.StrictRedis(**redis_config)

def store_verify_code(email: str, code: int) -> None:
    """
    往redis中存储验证码
    :param email: 邮箱地址
    :param code: 验证码
    """
    # 生成 key
    key = f"verify_code:{email}"
    # 存储验证码
    redis_client.set(key, code)
    # 设置过期时间为 5 分钟
    redis_client.expire(key, 300)

def get_verify_code(email: str) -> int:
    """
    从redis中取验证码
    :param email: 邮箱地址
    :return: 验证码
    """
    # 生成 key
    key = f"verify_code:{email}"
    # 获取验证码
    code = redis_client.get(key)
    # 返回验证码
    return int(code) if code else None