# Git Commit Visualizer

**Git Commit Visualizer** — это инструмент командной строки на Python для визуализации графа зависимостей коммитов в Git-репозитории с помощью PlantUML. Инструмент генерирует текстовый код PlantUML и изображение, отображающее зависимости коммитов.

## Особенности

- Поддержка русского языка.
- Генерация PlantUML-кода для графа зависимостей коммитов.
- Создание визуализации в виде диаграммы с использованием PlantUML.
- Вывод кода PlantUML в консоль и сохранение его в файл.

## Требования

- Python 3.6 или выше
- [Git](https://git-scm.com/)
- [PlantUML](http://plantuml.com/) и [Java](https://www.java.com/) для генерации диаграмм

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/your-username/git-commit-visualizer.git
   cd git-commit-visualizer
   ```

2. Установите зависимости (если есть).

## Использование

Запустите скрипт `visualizer.py` с параметрами командной строки:

```bash
python visualizer.py --viz_tool_path "/path/to/plantuml.jar" --repo_path "/path/to/git-repo" --output_path "/path/to/output.puml" --date "YYYY-MM-DD"
```

### Аргументы командной строки

- `--viz_tool_path`: Путь к файлу `plantuml.jar`.
- `--repo_path`: Путь к анализируемому Git-репозиторию.
- `--output_path`: Путь для сохранения файла с кодом PlantUML.
- `--date`: Ограничение по дате для коммитов в формате `YYYY-MM-DD`.

### Пример

```bash
python visualizer.py --viz_tool_path "/usr/local/bin/plantuml.jar" --repo_path "/Users/user/my-repo" --output_path "./output.puml" --date "2024-01-01"
```

## Пример вывода

```plaintext
Сгенерированный код PlantUML:
@startuml
rectangle "commit (f4555e7)" as f4555e7
rectangle "Начало работы (2d33b8c)" as 2d33b8c
f4555e7 --> 2d33b8c
...
@enduml
```



После запуска команда также создаст изображение диаграммы по указанному пути `output.puml`.

![Диаграмма зависимостей коммитов](Configuration_managment_practice_2/output/output.png)

## Лицензия

Этот проект лицензирован под лицензией MIT.
