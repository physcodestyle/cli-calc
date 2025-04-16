# Приложение super_calc

## Архитектура

### Функциональные требования

1. Поддержка вычислений разных типов и различной степени сложности.
2. Удобный консольный интерфейс для работы в интерактивном режиме.
3. Вывод результатов вычислений в различных форматах.
4. Ввод данных разных типов (числа, таблицы, внешние API).
5. Возможность использовать пользовательские алгоритмы (сценарии) для сложных вычислений.
6. Возможность использования команд для формирования сценариев с помощью языка bash.

### Технические требования

1. Поддержка операционных систем Windows, Linux, macOS, Android, iOS, iPadOS с помощью терминала на базе Unix-подобных ОС.
2. Полная поддержка клавиатуры для работы с приложением.
3. Полная поддержка мыши для работы с приложением.
4. Поддержка тем оформления для интерактивного режима.

### Как устроено приложение

Основой (ядром) приложения является **окружение для вычислений**, с помощью которого можно реализовать расчёты для любой модели предметной области.

Модель предметной области состоит из:

- объектов (данные),
- отношений между объектами,
- функция(-и) обработки данных (объектов и отношений между ними).

Окружение обеспечивает бизнес-логику работы приложения, которая позволяет осуществить вычисления и выдать результат. В рамках бизнес-логики возможны:

- предобработка вводимых данных,
- вычисления,
- постобработка результатов вычислений.

Таким образом, бизнес-логика приложения основана на взаимодействии с тремя группами модулей:

- модули для ввода данных (предобработка),
- модули для вычислений (модели предметных областей),
- модули для вывода данных (постобработка).
