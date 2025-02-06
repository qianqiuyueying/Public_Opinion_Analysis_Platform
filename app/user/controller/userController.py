from __init__ import user_router

@user_router.post("/login")
def login():
    """
    登录接口
    """
    ...

@user_router.post("/register")
def register():
    """
    注册接口
    """
    ...

@user_router.get("/info")
def info():
    """
    获取用户信息
    """
    ...

@user_router.get("/list")
def user_list():
    """
    获取用户列表
    """
    ...

@user_router.get("/logout")
def logout():
    """
    退出登录
    """
    ...