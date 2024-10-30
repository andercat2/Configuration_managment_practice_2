import subprocess
import argparse
from datetime import datetime

def get_commit_dependencies(repo_path):
    # Команда для получения хеша и сообщения коммита
    command = ["git", "-C", repo_path, "log", "--pretty=%H %P %s"]
    print("Выполняем команду:", " ".join(command))  # Временный вывод для проверки
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", shell=True)
    print("Вывод команды:", result.stdout)  # Временный вывод для отладки
    
    commits = result.stdout.strip().split("\n")
    
    dependencies = {}
    commit_messages = {}
    for commit in commits:
        if not commit.strip():
            continue
        parts = commit.split(maxsplit=2)
        hash_value = parts[0]
        parent_hashes = parts[1:-1]
        message = parts[-1] if len(parts) > 2 else "Без сообщения"
        dependencies[hash_value] = parent_hashes
        commit_messages[hash_value] = message
    return dependencies, commit_messages

def generate_plantuml_code(dependencies, commit_messages):
    # Генерация PlantUML кода с использованием rectangle для простых прямоугольников
    plantuml_code = ["@startuml"]
    added_nodes = set()  # Набор для отслеживания добавленных узлов
    
    for commit, parents in dependencies.items():
        commit_label = f"{commit_messages.get(commit, 'Без сообщения')} ({commit[:7]})"
        if commit not in added_nodes:
            plantuml_code.append(f'rectangle "{commit_label}" as {commit[:7]}')  # Создаем узел как простой прямоугольник
            added_nodes.add(commit)
        
        for parent in parents:
            if parent not in commit_messages:
                # Пропускаем родителя, если его нет в словаре сообщений коммитов
                print(f"Предупреждение: Родительский коммит {parent} не найден в сообщениях коммитов")
                continue
            
            parent_label = f"{commit_messages[parent]} ({parent[:7]})"
            if parent not in added_nodes:
                plantuml_code.append(f'rectangle "{parent_label}" as {parent[:7]}')  # Создаем родительский узел как прямоугольник
                added_nodes.add(parent)
            
            # Создаем связь между узлами
            plantuml_code.append(f'{parent[:7]} --> {commit[:7]}')
    
    plantuml_code.append("@enduml")
    return "\n".join(plantuml_code)

def save_to_file(output_path, content):
    # Сохранение PlantUML кода в файл с кодировкой UTF-8
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

def visualize_with_plantuml(viz_tool_path, output_path):
    # Вызов PlantUML для генерации изображения
    command = ["java", "-jar", viz_tool_path, output_path]
    subprocess.run(command)
    print(f"Визуализация создана с помощью PlantUML по пути {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Визуализатор графа зависимостей")
    parser.add_argument("--viz_tool_path", required=True, help="Путь к программе для визуализации графов (plantuml.jar)")
    parser.add_argument("--repo_path", required=True, help="Путь к анализируемому репозиторию")
    parser.add_argument("--output_path", required=True, help="Путь к файлу-результату")
    parser.add_argument("--date", required=True, help="Дата коммитов в формате ГГГГ-ММ-ДД")
    args = parser.parse_args()

    # Получаем зависимости коммитов
    dependencies, commit_messages = get_commit_dependencies(args.repo_path)
    
    # Генерируем код PlantUML
    plantuml_code = generate_plantuml_code(dependencies, commit_messages)
    
    # Выводим PlantUML код в консоль
    print("Сгенерированный код PlantUML:")
    print(plantuml_code)
    
    # Сохраняем PlantUML код в файл
    save_to_file(args.output_path, plantuml_code)
    print(f"Код PlantUML сохранен в {args.output_path}")

    # Визуализируем результат с помощью PlantUML
    visualize_with_plantuml(args.viz_tool_path, args.output_path)

if __name__ == "__main__":
    main()
