import copy
import random

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



test=validate_input_num("enter a number of tests: ")
max_balls=test*2
max_balls_copy1=max_balls
max_balls_copy2=max_balls
random_dict={}
random_color=[]
while test>0:
    while max_balls_copy2>0:
        if len(colors_list)>1: 
            random_color.append(colors_list.pop(random.randint(0,(len(colors_list)-1))))
            #print(f'max balls copy2: {max_balls_copy2}')
        for element in random_color:
            try:
                if (random_dict[element]):
                    skip=None
            except:
                if len(colors_list)>1:
                    random_dict[element]=random.randint(0,max_balls_copy2)
                else:
                    random_dict[element]=max_balls_copy2
                if sum(random_dict.values())>max_balls:
                    colors_list.append(element)
                    del random_dict[element]
                else:
                    max_balls_copy2-=random_dict[element]
                    #print(f'max balls copy2 {max_balls_copy2}\n len de color_list: {len(colors_list)}')
                if len(colors_list)==1:
                    random_color.append(colors_list.pop(0))
        for element in random_color:
            if random_dict[element]==0:
                del random_dict[element]
    print(f'The random dict is:\n{random_dict}')
    test-=1

