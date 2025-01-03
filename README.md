# Проект HTML Splitter

Этот проект предоставляет утилиту для разделения HTML-сообщений на более мелкие фрагменты, сохраняя целостность
HTML-тегов. Поддерживается настройка максимальной длины фрагментов, которая задается через параметры командной строки.

## Особенности

- Разделение больших HTML-сообщений на более мелкие, корректные фрагменты.
- Сохранение структуры HTML-тегов в каждом фрагменте.
- Поддержка настройки размера фрагментов через параметры CLI.

## Требования

- Python 3.8 или выше
- Poetry для управления зависимостями
- pytest для тестирования

## Настройка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/maxoralbay/testjob-splitHtml.git
   cd html-splitter

```

1. Установите зависимости с помощью Poetry:

```bash
poetry install
```

2. Для установки зависимостей для разработки (включая `pytest`) выполните:

```bash
poetry install --dev
```

## Использование

Вы можете запустить HTML Splitter из командной строки, используя команду `split_html`.

### Опции командной строки

- `--file`: Путь к HTML-файлу для разделения (обязательный параметр).

- `--max-length`: Максимальная длина каждого фрагмента (необязательный, по умолчанию 4096).

- `--output`: Путь к выходному файлу для сохранения фрагментов (необязательный, по умолчанию `output_fragments.txt`).

Пример:

```bash
poetry run python main.py --file data/source.html  --max-length 100 --output output_fragments.txt
```

Эта команда разделит файл `input.html` на фрагменты длиной не более 1000 символов и сохранит результат в
`output_fragments.txt`.

## Запуск тестов

В проекте используется `pytest` для тестирования. Вы можете запустить тесты с помощью следующей команды:

```bash
poetry run pytest
```

1. Установку зависимостей.

2. Запуск тестов с использованием `pytest`.

3. Генерацию отчета о покрытии.

4. Загрузку HTML-отчета о покрытии в качестве артефакта.
   Результаты тестов и отчеты о покрытии можно найти на вкладке **Actions**  этого репозитория.

## Работа с пользовательскими HTML-файлами

Чтобы протестировать утилиту с собственным HTML-файлом, поместите его в каталог проекта и укажите с помощью параметра
`--file`. Например, для файла `example.html`:

```bash
poetry run python main.py --file data/source2.html  --max-length 100 --output data/fragments2.txt
```

## Участие в разработке

1. Сделайте fork репозитория.

2. Создайте новую ветку (`git checkout -b feature-name`).

3. Внесите свои изменения.

4. Запустите тесты (`poetry run pytest`).

5. Отправьте pull request.

## Лицензия

Этот проект лицензирован под лицензией MIT 
