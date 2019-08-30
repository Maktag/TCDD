from replib.status import Status
from replib.config import Config


class TestSuit:

    """These are the variable need to initiate the variables"""
    Config.Script_version = "AppTest_11.45.11"
    Config.org_name = "MakTag"
    Config.Project_name = "AppTest"
    Config.User_name = "U@testapp"
    Config.Scripting_team = "QA_team_1"
    Config.Testing_env = "UAT_2"
    Config.Operating_system = "macOS 10.14.3"
    Config.Python_version = "Python3"
    Config.Org_logo_url = "../../maktag_1024.png"

    """This will give you the object to set the status of the test case. Pass the script version."""
    st = Status(Config.Script_version)

    def test_1(self):
    # """This will Initiate the module"""
        self.st.start_module('Login With Facebook')

    # """This will set status pass of the test case id 001,
    #  with the message 'Login is working fine with the FB.',
    # 'T' to save screenshot and 'F' to not save ----- """
        self.st.pass_test('001', 'Login is working fine with the FB.', 'F')

    def test_2(self):
    # """This will end the module"""
        self.st.end_module()

    def test_3(self):
    # """This will Initiate the second module"""
        self.st.start_module('Login With Twitter')
        self.st.pass_test('001', 'Loging with tw is working fine.')
        self.st.pass_test('002', 'Loging with tw is working fine.')

    def test_4(self):
    # """This will end the second module"""
        self.st.end_module()
    # """This will end the report"""
        self.st.report_end()


if __name__ == '__main__':
    ts = TestSuit()
    ts.test_1()
    ts.test_2()
    ts.test_3()
    ts.test_4()
