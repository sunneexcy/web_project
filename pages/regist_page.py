from common.base import Base

class UserRegistPage(Base):
    tel_loc = ("id", "txt_username")  # 输入手机号
    pwd_loc = ("id", "txt_password")  # 输入密码
    pwd_agin_loc = ("id", "txt_password")  # 再次输入密码
    code_loc = ("id", "txt_vcode")  # 输入验证码
    regist_btn_loc = ("linktext", "立即注册")  # 立即注册按钮
    link1_loc = ("linktext", "《当当交易条款》")
    link2_loc = ("linktext", "《当当社区条款》")
    link3_loc = ("linktext", "《当当隐私条款》")

    def input_tel(self, text=""):
        """输入手机号"""
        self.send(self.tel_loc, text)

    def input_pwd(self, text=""):
        """输入密码"""
        self.send(self.pwd_loc, text)

    def input_pwd_again(self, text=""):
        """再次输入密码"""
        self.send(self.pwd_agin_loc, text)

    def regist_click(self):
        """点击注册按钮"""
        self.click(self.regist_btn_loc)

    def link1_click(self):
        """点击链接1"""
        self.click(self.link1_loc)

    def link2_click(self):
        """点击链接2"""
        self.click(self.link2_loc)

    def link3_click(self):
        """点击链接3"""
        self.click(self.link3_loc)




