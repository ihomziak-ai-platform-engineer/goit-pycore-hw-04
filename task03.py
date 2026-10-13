
import sys
from pathlib import Path
from colorama import Fore, Style, init


def print_directory_tree(directory: Path, prefix: str = ""):
    try:
        items = sorted(
            directory.iterdir(),
            key=lambda item: (not item.is_dir(), item.name.lower())
        )

    except (PermissionError, OSError) as error:
        print(f"{prefix}{Fore.RED}Помилка доступу: {error}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1

        branch = "└── " if is_last else "├── "

        if item.is_dir():
            print(
                f"{prefix}{branch}"
                f"{Fore.BLUE}{item.name}/{Style.RESET_ALL}"
            )

            if not item.is_symlink():
                new_prefix = prefix + ("    " if is_last else "│   ")
                print_directory_tree(item, new_prefix)

        else:
            print(
                f"{prefix}{branch}"
                f"{Fore.GREEN}{item.name}{Style.RESET_ALL}"
            )


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Використання: python task03.py <шлях_до_директорії>")
        sys.exit(1)

    path = Path(sys.argv[1]).expanduser()

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує: {path}")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: шлях не є директорією: {path}")
        sys.exit(1)

    print(f"{Fore.BLUE}{path.name}/")
    print_directory_tree(path)


if __name__ == "__main__":
    main()
