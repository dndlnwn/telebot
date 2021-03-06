from di_configuration import DIBot

subject = {1: 'Информатика',
           2: 'Русский'}

count_iteration = 1
count_points = 0


def calculator(message):
    global count_points
    count_points = 0
    bot = DIBot.di_bot()
    calc_msg = bot.send_message(
        message.chat.id,
        'Введите количество баллов по Математике')
    bot.register_next_step_handler(calc_msg, points)


def points(message):
    global count_iteration, count_points
    print('до = {}'.format(count_points))
    count_points += int(message.text)
    print('после = {}'.format(count_points))
    try:
        bot = DIBot.di_bot()
        print(count_iteration)
        calc_msg = bot.send_message(
            message.chat.id,
            'Введите количество баллов по ' + subject[count_iteration])
        count_iteration += 1
        bot.register_next_step_handler(calc_msg, points)
    except:
        count_iteration = 1
        spec_msg(message, count_points)

specialty = {202: '<b>10.05.02 Информационная безопасность телекоммуникационных систем (специалитет)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             189: '<b>09.03.04 Программная инженерия (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             177: '<b>10.03.01 Информационная безопасность (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             173: '<b>09.03.01 Информатика и вычислительная техника (прикладной бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             171: '<b>09.03.02 Информационные системы и технологии (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балл\n\n'
                  '<b>Ссылка на профиль:</b> ',
             170: '<b>27.03.05 Инноватика (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             169: '<b>09.03.01 Информатика и вычислительная техника (академический бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             165: '<b>27.03.04 Управление в технических системах (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             163: '<b>09.03.03 Прикладная информатика (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             156: '<b>11.03.02 Инфокоммуникационные технологии и системы связи (прикладной бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             153: '<b>11.03.02 Инфокоммуникационные технологии и системы связи (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             152: '<b>11.03.01 Радиотехника (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балла\n\n'
                  '<b>Ссылка на профиль:</b> ',
             151: '<b>12.03.03 Фотоника и оптоинформатика (бакалавриат)</b>\n\n'
                  '<b>Проходной балл:</b> {} балл\n\n'
                  '<b>Ссылка на профиль:</b> '}


def spec_msg(message, points):
    bot = DIBot.di_bot()
    bot.send_message(
        message.chat.id,
        '<b>У тебя:</b> {} баллов\n'
        'Ознакомьтесь с доступными направлениям. Для этого можете перейти по ссылке либо воспользоваться командой '
        '/specialties'.format(points), parse_mode = 'HTML')
    if int(points) >= 190:
        for items in specialty:
            bot.send_message(
                message.chat.id,
                specialty[items].format(items),
                parse_mode='HTML',
                disable_web_page_preview=True)
    elif int(points) < 150:
        bot.send_message(
            message.chat.id,
            'К сожалению, твоих баллов не хватает для поступления на бюджет. '
            'Но есть возможность поступить на комерческое обучение. Для ознакомления с специальностями '
            'перейди в раздел с специальностями /specialties')
    elif int(points) < 160:
        for items in specialty:
            if items < 160:
                bot.send_message(
                    message.chat.id,
                    specialty[items].format(items),
                    parse_mode='HTML',
                    disable_web_page_preview=True)
    elif int(points) < 170:
        for items in specialty:
            if items < 170:
                bot.send_message(
                    message.chat.id,
                    specialty[items].format(items),
                    parse_mode='HTML',
                    disable_web_page_preview=True)
    elif int(points) < 180:
        for items in specialty:
            if items < 180:
                bot.send_message(
                    message.chat.id,
                    specialty[items].format(items),
                    parse_mode='HTML',
                    disable_web_page_preview=True)
    elif int(points) < 190:
        for items in specialty:
            if items < 190:
                bot.send_message(
                    message.chat.id,
                    specialty[items].format(items),
                    parse_mode='HTML',
                    disable_web_page_preview=True)
    clear_point()


def clear_point():
    global count_points
    count_points = 1


handlers = {'calculator': calculator}