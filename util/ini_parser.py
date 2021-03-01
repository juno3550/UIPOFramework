import configparser


class IniParser:

    # 初始化打开指定ini文件并指定编码
    def __init__(self, file_path, section):
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path, encoding="utf-8")
        self.section = section

    # 获取所有分组名称
    def get_sections(self):
        return self.cf.sections()

    # 获取指定分组的所有键
    def get_options(self):
        return self.cf.options(self.section)

    # 获取指定分组的键值对
    def get_items(self):
        return self.cf.items(self.section)

    # 获取指定分组的指定键的值
    def get_value(self, key):
        return self.cf.get(self.section, key)
