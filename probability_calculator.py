import copy
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num):
    if num > len(self.contents):
      return self.contents
    draws = []

    sample = random.sample(self.contents, num)
    for x in sample:
      draws.append(x)
      self.contents.remove(x)
    return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  succesfull_draw = 0
  
  drawed = []
  global j
  for j in range(num_experiments):
    global expected_balls_copy 
    expected_balls_copy= copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    drawed = hat_copy.draw(num_balls_drawn)

    drawedDict = {}
    for x in drawed:
      if x not in drawedDict:
        drawedDict[x] = 1
      else:
        drawedDict[x] += 1

    allMatch = True
    for key in expected_balls.keys():
      if drawed.count(key) < expected_balls[key]:
        allMatch = False
        break
    if allMatch:
      succesfull_draw += 1
  probability_=succesfull_draw / num_experiments
  return probability_

print("This progran calculates the probability of getting a certain combination of color balls")
print("from a box full of ball of 5 diferent colors")

colors_list=["Red",'Green','Blue',"Black","Pink"]

def validate_color(input_description=": "):  
    while True:
        print(f"Yuo can choose fron thesse colors: \n{colors_list}")
        color=(input(input_description)).lower().title()
        if color in colors_list:
            break
        else:
           print("==Invalid color==")
    return color

def validate_input_num(input_description=": "): 
    while True:
        try:
            num=int(input(input_description))
        except:
            print('===Invalid Input===')
            continue
        if type(num)==int:
            break
    return num

def validate_option(message="",max_option=1):
  while True:
    option_=input(message)
    try: 
      if int(option_)<=max_option and int(option_)>0:
        break
    except:
      print("===Input a valid option===")
  return option_

max_balls=validate_input_num("Enter how many balls are in the box: ")
#max_balls=45
max_balls_copy1=max_balls
max_balls_copy2=max_balls
colors_list_copy_1=colors_list
colors_list_copy_2=colors_list

'''
colors_list_sample=[]
colors_dict={}
while max_balls_copy1>0:
   color=validate_color('Enter a color for the balls: ')
   colors_list_sample.append(color)
   #if color in colors_list_sample:
   try:
      if (colors_dict[color]):
        option=validate_option(f"Do you want to overdrive the amoun of {color} balls?\n1 for Yes\n2 for No\n: ",2)
      if option=='1':
        max_balls_copy1+=colors_dict[color]
        colors_dict[color]=validate_input_num(f'Enter the NEW amount of {color} balls: ')
        print(f'overwrited color\n{colors_dict}')
        if (max_balls_copy1-colors_dict[color])>=0:
          max_balls_copy1-=colors_dict[color]
          print(f'{max_balls_copy1} balls left to chosse')
        else:
          del colors_dict[color]
          print('This number excedes the amount of balls in the box')
          print('==Select a diferent lower number==')
      if option=='2':
        skip=None
   except:
        colors_dict[color]=validate_input_num(f'Enter the amount of {color} balls: ')
        if (max_balls_copy1-colors_dict[color])>=0:
          max_balls_copy1-=colors_dict[color]
          print(f'{max_balls_copy1} balls left to chosse')
        else:
          del colors_dict[color]
          colors_list_sample.remove(color)
          print('This number excedes the amount of balls in the box')
          print('==Select a diferent lower number==')

print(f'user dict: \n {colors_dict}')
'''
#lest create a box of colored balls randomly 
random_dict={}
random_color=[]
while max_balls_copy2>0:
  if len(colors_list_copy_2)>1:
    random_color.append(colors_list_copy_2.pop(random.randint(0,(len(colors_list_copy_2)-1))))
    #print(f'max balls copy2: {max_balls_copy2}')
  for element in random_color:
    try:
      if (random_dict[element]):
        skip=None
    except:
      if len(colors_list)>1:
        random_dict[element]=random.randint(0,max_balls_copy2)
        max_balls_copy2-=random_dict.get(element)
      else:
        random_dict[element]=max_balls_copy2
        if sum(random_dict.values())>max_balls:
          colors_list_copy_2.append(element)
          del random_dict[element]
        else:
          max_balls_copy2-=random_dict[element]
          #print(f'max balls copy2 {max_balls_copy2}\n len de color_list: {len(colors_list_copy_2)}')
        if len(colors_list_copy_2)==1:
          random_color.append(colors_list_copy_2.pop(0))
  for element in random_color:
    if random_dict.get(element)==0:
      del random_dict[element]

print(random_dict)

#colors_list=["Red",'Green','Blue',"Black","Pink"]

try:
   red=random_dict["Red"]
except:
   red=0
try:
   green=random_dict['Green']
except:
   green=0
try:
   blue=random_dict['Blue']
except:
   blue=0
try:
   black=random_dict["Black"]
except:
   black=0
try:
   pink=random_dict["Pink"]
except:
   pink=0

print(f'red={red} green={green} blue={blue} black={black} pink={pink}')

box=Hat(Red=red,Green=green,Blue=blue,Black=black,Pink=pink)
#print(f'this is the box: {box}') ===========passed===========

while True:
  num_balls_to_drawn=validate_input_num(f'Enter how many balls you want to drwa from the box of {max_balls}: ')
  draw=box.draw(num_balls_to_drawn)
  if max_balls >= num_balls_to_drawn:
    break
  else:
    print(f"The number of balls to draw must be less or equal to the amount of balls in the box ({max_balls})")
experiments=validate_input_num('Enter how many experiments you wish to do: ')
#{"Red": 2,"Green": 3}
'''
probability = prob_calculator.experiment(hat=hat,
                                             expected_balls={
                                                 "yellow": 2,
                                                 "blue": 3,
                                                 "test": 1
                                             },
                                             num_balls_drawn=20,
                                             num_experiments=10000)
'''
probability=experiment(hat=box,expected_balls=random_dict,num_balls_drawn=num_balls_to_drawn,num_experiments=experiments)
print(probability)
