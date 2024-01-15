import subprocess
import sys


class ModuleImport:
    def __init__(self):
        self.install_dependencies()

    def install_dependencies(self):
        self.import_wonderwords()
        self.import_googletrans()
        self.import_pygame()
        self.import_gtts()
        self.import_json()
        self.import_goslate()
        self.import_pydictionary()

    def import_gtts(self):
        try:
            import gtts
        except ImportError:
            print("gtts is not installed, trying to install...")
            self.install_package('gtts')

    def import_wonderwords(self):
        # 检查 wonderwords 是否已安装
        try:
            import wonderwords
        except ImportError:
            print("wonderwords is not installed, trying to install...")
            self.install_package('wonderwords')

    def import_pygame(self):
        try:
            import pygame
        except ImportError:
            print("pygame is not installed, trying to install...")
            self.install_package('pygame')

    def import_googletrans(self):
        # 检查 googletrans 是否已安装
        try:
            from googletrans import Translator
        except ImportError:
            print("googletrans is not installed, trying to install...")
            self.install_package('googletrans==4.0.0-rc1')  # 特定版本，因为之后的版本可能不再支持免费翻译

    def import_json(self):
        try:
            import json
        except ImportError:
            print("json is not installed, trying to install...")
            self.install_package('json')

    def import_goslate(self):
        try:
            import goslate
        except ImportError:
            print("goslate is not installed, trying to install...")
            self.install_package('git+https://github.com/yeahwhat-mc/goslate#egg=goslate')

    def import_pydictionary(self):
        try:
            import PyDictionary
        except ImportError:
            print("PyDictionary is not installed, trying to install...")
            self.install_package('PyDictionary')

    @staticmethod
    def install_package(package):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])