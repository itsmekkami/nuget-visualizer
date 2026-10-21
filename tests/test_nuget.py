"""Тесты разбора параметров (Этап 1)"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from config_parser import parse_args


class TestConfigParser(unittest.TestCase):
    """Проверки корректности разбора CLI-аргументов"""
    def test_full_args(self):
        """Все параметры заданы явно"""
        test_args = [
            "-p", "Newtonsoft.Json",
            "-r", "./local_repo",
            "-m", "local",
            "-v", "13.0.1",
            "-f", "Json"
        ]
        result = parse_args(test_args)

        self.assertEqual(result.package, "Newtonsoft.Json")
        self.assertEqual(result.repo, "./local_repo")
        self.assertEqual(result.mode, "local")
        self.assertEqual(result.version, "13.0.1")
        self.assertEqual(result.filter, "Json")

    def test_default_args(self):
        """Задан только обязательный параметр, остальные по умолчанию"""
        test_args = ["-p", "TestPackage"]
        result = parse_args(test_args)
        self.assertEqual(result.package, "TestPackage")
        self.assertIsNone(result.repo)
        self.assertEqual(result.mode, "remote")
        self.assertEqual(result.version, "latest")
        self.assertEqual(result.filter, "")

    def test_long_flags(self):
        """Проверка длинных флагов (--package, --mode и т.д.)"""
        test_args = [
            "--package", "LongFlags",
            "--mode", "local"
        ]
        result = parse_args(test_args)
        self.assertEqual(result.package, "LongFlags")
        self.assertEqual(result.mode, "local")

    def test_missing_required_arg(self):
        """Отсутствие обязательного аргумента вызывает SystemExit"""
        test_args = ["-m", "local"]
        with self.assertRaises(SystemExit):
            parse_args(test_args)

    def test_invalid_mode_choice(self):
        """Недопустимый режим вызывает SystemExit"""
        test_args = ["-p", "Test", "-m", "invalid_mode"]
        with self.assertRaises(SystemExit):
            parse_args(test_args)

    def test_invalid_version_format(self):
        """Неверный формат версии вызывает SystemExit"""
        test_args = ["-p", "Test", "-v", "not_a_version"]
        with self.assertRaises(SystemExit):
            parse_args(test_args)

    def test_valid_version_formats(self):
        """Правильные форматы версий принимаются"""
        for version in ["1.0", "1.2.3", "13.0.3-beta"]:
            test_args = ["-p", "Test", "-v", version]
            result = parse_args(test_args)
            self.assertEqual(result.version, version)


if __name__ == "__main__":
    unittest.main()
