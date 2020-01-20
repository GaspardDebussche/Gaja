# -*- coding: utf-8 -*-

""" IMPORTS """

from Reinforce import reinforcement_learning
from speech import sentence_transcription
from reward_matrix import dataset
import time
from LED import led_management
from sound import sound_management


""" RUNNING CODE """

state = 0

while True:
    sentence = sentence_transcription()
    t=time.time()
    reinforce_variables = reinforcement_learning(sentence, state)
    print(time.time()-t)
    for i in reinforce_variables[0]:
        print(dataset.iloc[i])
        led_management(dataset.iloc[i]['eyes'])
        sound_management(dataset.iloc[i]['voice'])
        print("Paw is {}".format('up' if dataset.iloc[i]['paw'] == 0 else 'down'))
        state = i
    time.sleep(3)