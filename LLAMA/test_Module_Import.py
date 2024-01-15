from unittest import TestCase
from Module_Import import ModuleImport


class TestModuleImport(TestCase):
    def test_import_all_dependencies(self):
        ModuleImport()
