import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age
    
    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __str__(self):
        return f"User(nickname={self.nickname}, age={self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, login, password):
        hashed_password = self.hash_password(password)
        for user in self.users:
            if user.nickname == login and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {login} вошел в систему.")
                return
        print("Неправильный логин или пароль.")
    
    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} успешно зарегистрирован.")
    
    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
        self.current_user = None
    
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео с названием '{video.title}' уже существует.")
    
    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        matching_videos = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return matching_videos
    
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        
        video = next((v for v in self.videos if v.title == title), None)
        if video is None:
            print("Видео не найдено.")
            return
        
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        
        print(f"Сейчас воспроизводится видео: {video.title}")
        for second in range(video.time_now, video.duration):
            print(f"Прошло {second + 1} секунд")
            time.sleep(1)
        video.time_now = 0
        print("Конец видео")
    
    @staticmethod
    def hash_password(password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)


# Пример использования:
urtube = UrTube()

# Регистрация пользователей
urtube.register("user1", "password123", 20)
urtube.register("user2", "password456", 16)

# Вход в систему
urtube.log_in("user1", "password123")

# Добавление видео
video1 = Video("Funny Cats", 10)
video2 = Video("Urban the best", 15, adult_mode=True)

urtube.add(video1, video2)

# Поиск видео
print("Видео, содержащие 'Urban':", urtube.get_videos("Urban"))

# Просмотр видео
urtube.watch_video("Funny Cats")
urtube.watch_video("Urban the best")

# Выход из системы
urtube.log_out()

# Попытка просмотра видео без входа в систему
urtube.watch_video("Funny Cats")

# Вход в систему другим пользователем
urtube.log_in("user2", "password456")

# Попытка просмотра видео с возрастным ограничением
urtube.watch_video("Urban the best")


# Общее ТЗ:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

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

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist