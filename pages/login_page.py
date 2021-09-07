from common.base import Base

class UserLoginPage(Base):
    usr_loc = ("id", "txtUsername")
    pwd_loc = ("id", "txtPassword")
    login_btn_loc = ("linktext", "登 录")
    code_loc = ("class", "switch start")  # 点击扫码登陆
    code1_loc = ("class", "switch quick")  # 点击密码登陆
    foget_pwd_loc = ("linktext", "忘记密码？")  # 忘记密码
    link_loc = ("linktext", "《隐私政策》")   # 隐私链接
    regist_btn_loc = ("id", "J_loginToRegister")  # 立即注册按钮

