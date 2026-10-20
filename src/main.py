"""Запуск приложения"""
from config_parser import parse_args


def print_params(args):
    """Выводит параметры в формате ключ-значение (для 1 Этапа)"""
    print("Параметры запуска:")
    print(f"Имя пакета: {args.package}")
    if args.repo is None:
        print("Репозиторий: (не указан)")
    else:
        print(f"Репозиторий: {args.repo}")
    print(f"Режим работы с тестовым репозиторием: {args.mode}")
    print(f"Версия пакета: {args.version}")
    print(f"Подстрока для фильтрации пакетов: {args.filter}")


def main():
    """Запускает главный цикл"""
    args = parse_args()
    print_params(args)


if __name__ == "__main__":
    main()
