from pathlib import Path


class DirectoryScanner:
    def __init__(self, root_path):
        """
        Инициализация объекта для сканирования директорий.
        :param root_path: str или Path, корневая директория для сканирования.
        """
        self.root_path = Path(root_path)
        if not self.root_path.exists():
            raise FileNotFoundError(f"Указанный путь '{self.root_path}' не существует.")
        if not self.root_path.is_dir():
            raise NotADirectoryError(f"Указанный путь '{self.root_path}' не является директорией.")

    def scan_directory(self):
        """
        Рекурсивный обход всех папок и подпапок.
        :return: dict, словарь с путями к файлам и папкам.
        """
        contents = {
            "files": [],
            "directories": []
        }

        for path in self.root_path.rglob("*"):  # rglob рекурсивно обходит все поддиректории
            if path.is_file():
                contents["files"].append(path)
            elif path.is_dir():
                contents["directories"].append(path)

        return contents

    def display_contents(self):
        """
        Вывод содержимого папок и подпапок в консоль.
        """
        print(f"Содержимое директории: {self.root_path}")
        contents = self.scan_directory()

        print("\nФайлы:")
        for file_path in contents["files"]:
            print(file_path)

        print("\nПапки:")
        for dir_path in contents["directories"]:
            print(dir_path)


if __name__ == "__main__":
    root_directory = "./example_folder"
    scanner = DirectoryScanner(root_directory)
    scanner.display_contents()
