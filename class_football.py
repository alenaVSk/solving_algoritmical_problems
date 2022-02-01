''' Создайте класс SoccerPlayr, у которого есть:
конструктор __init__, принимающий 2 аргумента: name, surname.Также во время 
инициализации необходимо создать 2 атрибута экземпляра:
goals и assists - общее количество голов и передач игрока, изначально оба 
значения должны быть 0;
метод score, который принимает количество голов, забитых игроком, по умолчанию 
данное значение равно единице. Метод должен увеличить общее количество забитых 
голов игрока на переданное значение;
метод make_assist, который принимает количество передач, сделанных игроком за 
матч, по умолчанию данное значение равно единице. Метод должен увеличить общее 
количество сделанных передач игроком на переданное значение;
метод statistics, который выводит на экран статистику игрока в виде:
<Фамилия> <Имя> - голы: <goals>, предачи: <assists>                                                                                
'''
class SoccerPlayr:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0
    def score(self, goals = 1):
        self.goals += goals
    def make_assist(self, assists = 1):
        self.assists += assists
    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, пердачи: {self.assists}')

leo = SoccerPlayr('Leo', 'Messi')
leo.goals = 500
leo.assists = 600
leo.score()
leo.make_assist()
leo.statistics()

alex = SoccerPlayr('Alex', 'Kokorin')
alex.goals = 400
alex.assists = 500
alex.score()
alex.make_assist()
alex.statistics()

