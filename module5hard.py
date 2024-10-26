import hashlib
import time

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def __int__(self):
        return f'{self.age}'

class Video:
    """
    Класс видео, содержащий атрибуты: название, продолжительность, время остановки, ограничение по возрасту
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    """
    Класс основной, содержит атрибуты: список пользователей, список видеороликов,
    текущего пользователя (проверка на существование и возраста)
    """
    def __init__(self):
        self.users =  [] #(список пользователей User),
        self.videos = [] #(список видеороликов Video),
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = nickname
                return

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def add(self, *files):
        for film in files:
            vid_s = False
            for video in self.videos:
                if film.title.lower() == video.title.lower():
                    vid_s =True
            if not vid_s:
                self.videos.append(film)

    def get_videos(self, title_video):
        files_ = []
        for video in self.videos:
            if title_video.lower() in video.title.lower():
                files_.append(video.title)
        return  files_

    def watch_video(self, film):
        if self.current_user:
            for video in self.videos:
                if self.current_user.age < 18:
                    print(f"Вам '{self.current_user.nickname}' нет 18 лет, пожалуйста покиньте страницу")
                    return
                if film in video.title:
                    for i in range(1, video.duration+1):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print(f'Конец видео - "{film}"')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 15, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
