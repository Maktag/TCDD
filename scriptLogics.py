from BizLogicDef import BizLogicDef as bld
from replib.config import Config
from replib.status import Status

input_vars = []


def scenario(bizlogic):
    return bizlogic.replace("Scenario", "").rstrip()


def pre_condition(bizlogic):
    method_name = bizlogic.replace("   Pre_Condition ", "").replace(" ", "_").replace(",", "").replace(".", "_").replace(":", "_").rstrip()
    if method_name in dir(bld):
        getattr(globals()['bld'](), method_name)()
    else:
        print('Implement the method: def', method_name+'(self):')
        definition = open("BizLogicDef.py", "a")
        definition.write("\n\n    def " + method_name+'(self):\n')
        definition.write("        pass")
        definition.close()


def actions(bizlogic, input_d):
    list_of_words = bizlogic.split(" ")
    for word in list_of_words:
        if word.__contains__("$"):
            input_vars.append(word.rstrip())
    method_name = bizlogic.replace("   Action ", "").replace(" ", "_").replace(",", "").replace(".", "_").replace("$", "").replace(
        ":", "_").rstrip()
    if method_name in dir(bld):
        if len(input_vars) > 0 and input_d is not None:
            getattr(globals()['bld'](), method_name)(input_d)
        else:
            getattr(globals()['bld'](), method_name)()
    else:
        if len(input_vars) > 0 and input_d is not None:
            print('Implement the method: def', method_name + '(self, data_list):')
            definition = open("BizLogicDef.py", "a")
            definition.write("\n\n    def " + method_name + '(self, data_list):\n')
            definition.write("        pass")
            definition.close()
        else:
            print('Implement the method: def', method_name + '(self):')
            definition = open("BizLogicDef.py", "a")
            definition.write("\n\n    def " + method_name + '(self):\n')
            definition.write("        pass")
            definition.close()


def input_in_action(bizlogic):
    if bizlogic.__contains__("Input"):
        input_ = bizlogic.replace("   Input ", "").replace(" ", "").rstrip()
        input_values = input_.split(",")
        return input_values


def expected(bizlogic):
    method_name = bizlogic.replace("   Expected ", "").replace(" ", "_").replace(",", "").replace(".", "_").replace(":", "_").rstrip()
    if method_name in dir(bld):
        getattr(globals()['bld'](), method_name)()
        return True
    else:
        print('Implement the method: def', method_name + '(self):')
        definition = open("BizLogicDef.py", "a")
        definition.write("\n\n    def " + method_name + '(self):\n')
        definition.write("        pass")
        definition.close()
        return False


def execute():
    f = open("BizLogic.biz", "r")
    lines = f.readlines()

    """These are the variable need to initiate the variables"""
    Config.Script_version = "AppTest_11.45.12"
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
    st.start_module("Testing")

    for i in range(0, len(lines)):
        line = lines[i]
        if line.__contains__("Scenario"):
            message = line.split(":")[1].rstrip()
            tc_id = line.split(":")[0].rstrip()
        if line.__contains__("Pre_Condition"):
            try:
                pre_condition(line)
            except Exception as ex:
                st.fail_test(tc_id, message + '. Issue is: ' + str(ex), 'F')
        if line.__contains__("Action"):
            try:
                actions(line, input_in_action(lines[i + 1]))
            except Exception as ex:
                st.fail_test(tc_id, message + '. Issue is: ' + str(ex), 'F')
        if line.__contains__("Expected"):
            try:
                if expected(line):
                    st.pass_test(tc_id, message, 'F')
            except Exception as ex:
                st.fail_test(tc_id, message + '. Issue is: ' + str(ex), 'F')

    st.end_module()
    st.report_end()