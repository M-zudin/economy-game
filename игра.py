import random
game_rules={'duration':None,'start_money':None,'game_mode':None,'percent':None,'return_amount':None}
begins=['Nano','Micro','Sam','Pana','Go']
ends=['soft','hard','sung','sonic','hypersonic','ogle']
players_list=[]
visible_players_list=[]
obligations=[]
stocks=[]
try:
    game_rules['duration']=int(input('Введите кол-во ходов (больше 1)\n'))
    if game_rules['duration']<=1:
        raise ValueError
except ValueError:
    game_rules['duration']=5
    print('Некорректное значение, установлено на 5')
try:
    game_rules['start_money']=int(input('Введите стартовое кол-во денег (от 100)\n'))
    if game_data['rules']['start_money']<100:
        raise ValueError
except ValueError:
    game_rules['start_money']=100
    print('Некорректное значение, установлено на 100')
game_rules['game_mode']=input('Введите общий режим игры\n0 - фиксированные кол-ва и проценты от начального\n1- проценты каждый ход и проценты от текущего\n')
if game_rules['game_mode']=='0':
    game_rules['game_mode']=0
if game_rules['game_mode']=='1':
    game_rules['game_mode']=1
else:
    game_rules['game_mode']=0
    print('Некорректное значение, установлено на 0')
if game_rules['game_mode']==0:
    try:
        game_rules['return_amount']=int(input(f'''Введите кол-во денег для возврата(от {round(game_rules['start_money']+game_rules['start_money']/10)})\n'''))
        if game_rules['return_amount']<game_rules['start_money']+game_rules['start_money']/10:
            raise ValueError
    except ValueError:
        game_rules['return_amount']=round(game_rules['start_money']+game_rules['start_money']/10)
        print(f'''Некорректное значение, установлено на {game_rules['return_amount']}''')
else:
    try:
        game_rules['percent']=int(input('Введите процент каждый ход(от 5)\n'))
        if game_rules['percent']<5
            raise ValueError
    except ValueError:
        game_rules['percent']=5
        print('Некорректное значение, установлено на 5}')
class player():
    def __init__(self):
        self.money=game_rules['start_money']
        self.obligations=[]
        self.stocks=[]
        self.visible_obligations=[]
        self.visible_stocks=[]
        self.name=input('Введите имя\n')
        visible_players_list.append(self.name)
        if game_rules['game_mode']==0:
            self.debt=game_rule['return_amount']
    def pay_debt(amount,self):
        self.debt-=amount
        self.money-=amount
    def update(self):
        if game_rules['game_mode']==1:
            self.debt+=self.debt+self.debt*game_rules['percent']/100
class obligation():
    def __init__(self):
        self.cost=random.randint(20,70)
        self.first_cost=self.cost
        self.percent=0
        self.name=name
        self.visible_name='Облигация '+name
        self.owner=None
        self.start_turn=turn
    def buy(buyer,self):
        exec(f'{buyer}.visible_obligations.append(self.visible_name)')
        exec(f'{buyer}.obligations.append(self.name)')
        exec(f'{buyer}.money-=self.cost')
        self.owner=buyer
    def sell(self):
        exec(f'{buyer}.visible_obligations.remove(self.visible_name)')
        exec(f'{buyer}.obligations.remove(self.name)')
        exec(f'{buyer}.money+=self.cost')
        obligations.remove(self.visible_name)
    def update(self):
        if game_rules['game_mode']==0:
            self.cost-=self.first_cost/10
            exec(f'{self.owner}.money+=self.first_cost*self.percent/100
        else:
            exec(f'{self.owner}.money+=self.cost*self.percent/100')
            self.cost-=self.cost/game_rules['percent']
class stock():
    def __init__(self):
        self.cost=5
        self.first_cost=self.cost
        self.trend=random.randint(-2,2) #будем использовать?
        self.name=name 
        self.visible_name='Акция '+name
        self.owner=None
        self.start_turn=turn
    def buy(buyer,self):
        exec(f'{buyer}.visible_stocks.append(self.visible_name)')
        exec(f'{buyer}.stocks.append(self.name)')
        exec(f'{buyer}.money-=self.cost')
        self.owner=buyer
    def sell(self):
        exec(f'{buyer}.visible_stocks.remove(self.visible_name)')
        exec(f'{buyer}.stocks.remove(self.name)')
        exec(f'{buyer}.money+=self.cost')
        stocks.remove(self.visible_name)
    def update(self):
        self.cost=random.randint(round(self.first_cost/2.5),round(self.first_cost*2.5))
def create_obligs(amount):
    for x in range(0,amount):
        while True:
            name=begins[random.randint(0,4)]+ends[random.randint(0,4)]
            if name not in obligations:
                break
        obligations.append(name)
        exec(f'{name}=obligation()')
def create_stocks(amount):
    for x in range(0,amount):
        while True:
            name=begins[random.randint(0,4)]+ends[random.randint(0,4)]
            if name not in stocks:
                break
        stocks.append(name)
        exec(f'{name}=stock()')
