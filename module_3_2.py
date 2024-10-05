
def send_email(message, recipient,*,sender = "university.help@gmail.com"):

    if check_email(recipient) and check_email(sender):
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender =="university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')


def check_email(address_em):
    domain_email = [".com", ".ru", ".net"]
    const_ = False
    if address_em.find("@") != -1:
        for dom in domain_email:
            if address_em.endswith(dom):
                const_ = True
                break
    return const_


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', \
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', \
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',\
           sender='urban.teacher@mail.ru')