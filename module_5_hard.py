class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password =  hash(password)
        self.age = age

    def __eq__(self,other):
        return self.nickname == other.nickname

    def __str__(self):
        return f"{self.nickname}"

class Video:

    def __init__(self,title,duration,adult_mode=False):
        self.title = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self,other):
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return f"Video(title='{self.title}',duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users =[]
        self.videos =[]
        self.current_user = None

    def log_in(self,nickname,password):

        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"Пользователь {'nickname'}'вошёл в систему.")
                return True
        print("Ошибка входа: неверный логин или пароль.")
        return False

    def register(self, nickname, password, age ):
        new_user =  User(nickname, password, age)
        if new_user in self.users:
            print(f"Пользователь {'nickmame'} уже существует.")
        else:
            self.users.append(new_user)
            self.current_user =new_user

    def log_out(self):


        if 'self.current_user':
            print(f"Пользователь {'self.current_user.nickmame'} вышел из системы.")
            self.current_user = None



    def  add(self, videos):
        for video in videos:
            if 'video' not in self.videos:
                self.videos.append('video')

    def get_videos(self,search_term):
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term.lower in video.title.lower()]

    def watch_video(self,title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет,пожалуста поктньте страницу")
                    return
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    video.time_now = 0
                    return

ur = UrTube()
v1 = Video('Лучший язык програмирования 2024 года', 200)
v2 = Video('Для чего девушкам парень програмист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))









ur.watch_video('Для чего девушкам парень програмист?')
ur.register('vasy_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJC1b9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень програмист?')

ur.register('vasy_pupkin', 'lolkekcheburek', 55)

print(ur.current_user)
ur.watch_video('Лучший язык програмирования 2024 года!')






