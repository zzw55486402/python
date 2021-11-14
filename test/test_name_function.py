# 单元测试包 unittest
import unittest
from name_function import get_formatted_name

# 创建测试类并且定义测试方法（可以定义多个测试方法）
class NameTestCase(unittest.TestCase):
    # 测试get_formatted_name方法
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        # 判断得到的结果和预期是否符合
        self.assertEqual(formatted_name, "Janis Joplin")
    def test_first_mid_last_name(self):
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

# 执行测试函数
unittest.main()