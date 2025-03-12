from main import *
from time import sleep
import random
# login
login('9157259694','200150109564')
sl(0.5, 1)
# click task page
click_task()
sleep(round(random.uniform(0.5, 1), 2))
# click first task
task=0
goal = 30
def play(brand:str):
    sleep(16)
    click_start_answering()
    sl(0.5, 3)
    click_matching_brand(brand)
    click_submit_answer()
    click_back_to_next()
    print('---------------------------------------------------------')
# inside while loop set task number counter

while True:
    if task == goal:
        break
    click_task_item()
    
    click_play_button()
    des = description_extract()
    brands = ['BVLGARI', 'Bvlgari','Bulgari', 'Gucci', 'Burberry', 'Hermès']
    matched_brand = next((name for name in brands if name in des), None)
    if matched_brand:
        if matched_brand == 'Bulgari' or matched_brand == 'BVLGARI':
            play('BVLGARI')
        elif matched_brand == 'Hermès':
            play('hermes')
        else:
            play(matched_brand)
    else:
        click_watch_later()


    
sleep(10)
close()