# -*- coding: utf-8 -*-

""" IMPORTS """

from Reinforce import reinforcement_learning
from speech import sentence_transcription
from reward_matrix import dataset
import time
from LED import led_management
from sound import sound_management

""" EXECUTION """

with open("record.txt", 'a') as file:
    file.write(input()+"\n")

    state = 0
    count = 0
    while True:
        file.write("Interaction {}\n".format(count))
        t1=time.time()
        sentence = sentence_transcription()
        t2=time.time()
        file.write(str(t2-t1)+"\n")
        reinforce_variables = reinforcement_learning(sentence, state)
        file.write(str(time.time() - t2)+"\n")
        for i in reinforce_variables[0]:
            if dataset.iloc[i]['paw'] == 2:
                print("I give the paw")
            led_management(dataset.iloc[i]['eyes'])
            sound_management(dataset.iloc[i]['voice'])
            state = i
        time.sleep(3)
        file.write("\n")
        count += 1