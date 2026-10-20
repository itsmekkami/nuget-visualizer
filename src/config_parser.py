"""Разбор параметров командной строки"""
import argparse


def create_parser():
    """Создает и настраивает парсер"""
    parser = argparse.ArgumentParser(
        description="Инструмент визуализации графа зависимостей"
        )
    parser.add_argument(
        "-p", "--package",
        required=True,
        help="Имя анализируемого пакета"
    )
    parser.add_argument(
        "-r", "--repo",
        default=None,
        help="URL-адрес репозитория или путь к тестовому репозиторию"
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["local", "remote"],
        default="remote",
        help="Режим работы с тестовым репозиторием"
    )
    parser.add_argument(
        "-v", "--version",
        default="latest",
        help="Версия пакета"
    )
    parser.add_argument(
        "-f", "--filter",
        default="",
        help="Подстрока для фильтрации пакетов"
    )
    return parser


def parse_args(args_list: list = None):
    """Разбирает переданные аргументы"""
    parser = create_parser()
    return parser.parse_args(args_list)
