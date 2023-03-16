import json
import markdown


class User:
    user_score = {'user_ie': 0, 'user_sn': 0, 'user_tf': 0, 'user_jp': 0}  # это баллы
    user_types = {}  # это буквы min для EI, SN, TF и JP
    user_nnnn = ''
    user_full = ''

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return [self.name, [item for item in self.user_score.values()], self.user_nnnn]


if __name__ == '__main__':
    print('Привет! Это Тест 8. Инструкция к тесту: Этот вопросник предназначен для определения типичных способов \n'
          'поведения и личностных характеристик. Он состоит из 70 утверждений (вопросов), каждое из которых имеет \n'
          'два варианта ответа. Вам необходимо выбрать ОДИН. Все ответы равноценны, среди них нет "правильных" \n'
          'или "неправильных"! Поэтому не нужно "угадывать" ответ. Выберите ответ, который свойствен вашему \n'
          'поведению в большинстве жизненных ситуаций. Работайте последовательно, не пропуская вопросов. \n'
          'Отвечайте правдиво, если вы хотите узнать что-то о себе, а не о какой-то мифической личности.\n')

    user_name = input('Введите ваше имя:').strip()
    user_email = input('Введите ваш email:').strip()

    user = User(user_name, user_email)  # Инициализация пользователя

    print('Начнём? Ответьте на 70 вопросов, обычно это занимает 3-5 минут.')
    print('Что-бы не было ошибок при вводе и для корректного отображения, пожалуйста, вводите только «a» \n'
          'или «b».')

    with open('questions.txt', encoding='utf-8') as file:  # Считывание файла с вопросами построчно
        for i, line in enumerate(file):
            print(line.strip())
            answer = input('Введите ответ "а" или "b": ').strip()
            # while answer != 'a' and answer != 'b':  # Проверка на правильность ввода
            #     answer = input('Неверный ввод. Пожалуйста, введите "a" или "b": ')

            if answer == 'a':
                match i % 7:  # В зависимости от строки с вопросом, наращиваем определенный параметр
                    case 0:
                        user.user_score['user_ie'] += 1
                    case 1 | 2:
                        user.user_score['user_sn'] += 1
                    case 3 | 4:
                        user.user_score['user_tf'] += 1
                    case 5 | 6:
                        user.user_score['user_jp'] += 1

    # Определяем тип личности, в зависимости от набранных баллов
    user.user_types = {'user_i': 'E' if user.user_score['user_ie'] > 5 else 'I',
                       'user_n': 'S' if user.user_score['user_sn'] > 10 else 'N',
                       'user_f': 'T' if user.user_score['user_tf'] > 10 else 'F',
                       'user_p': 'J' if user.user_score['user_jp'] > 10 else 'P'}

    for value in user.user_types.values():  # Из полученного типа личности устанавливаем буквенную аббревиатуру
        user.user_nnnn += value

    with open('result_types.json', encoding='utf-8') as file:  # Считываем JSON файл с расшифровкой аббревиатуры
        data = json.load(file)

    user.user_full = data[user.user_nnnn]  # Устанавливаем пользователю полученную расшифровку

    print(f'\nБуквенный код оценки: {user.user_nnnn},  Вашей оценкой является балл: {user.user_score["user_ie"]} '
          f'{user.user_score["user_sn"]} {user.user_score["user_tf"]} {user.user_score["user_jp"]}\n')
    print('Результат тестирования: ' + user.user_full)

    print('Помните, что темпераменты и типы - это возможности, а не способности и что существует корреляция. \n'
          'Когда кто-то имеет предпочтение к чему-либо, он склонен много заниматься этим и поэтому развивает свои \n'
          'способности в этом виде деятельности. Тогда вероятно, что предыдущий параграф верен,\n'
          'хотя исключения всегда найдутся. Так что NF может иметь в себе достаточно SР, чтобы быть \n'
          'превосходным в стратегии и лучшим в логистике, чем можно было бы ожидать \n'
          '(хотя логистика бы должна была быть его наименее квалифицированной ролью).\n')

    print('Спасибо! Тестирование закончилось.')

    with open(f'{user.name}_ESTF.md', 'w', encoding='utf-8') as f:
        f.write(str(user.__str__()))


