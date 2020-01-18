from Reinforce import reinforcement_learning
from speech import sentence_transcription
from reward_matrix import dataset
import time
from LED import led_management
from sound import sound_management

file = open("record.txt", 'a')
file.write(input())

state = 0
count = 0
while True:
    file.write("Interaction {}".format(count))
    t1=time.time()
    sentence = sentence_transcription()
    t2=time.time()
    file.write(t2-t1)
    reinforce_variables = reinforcement_learning(sentence, state)
    file.write(time.time() - t2)
    for i in reinforce_variables[0]:
        print(dataset.iloc[i])
        led_management(dataset.iloc[i]['eyes'])
        sound_management(dataset.iloc[i]['voice'])
        print("Paw is {}".format('up' if dataset.iloc[i]['paw'] == 0 else 'down'))
        state = i
    time.sleep(3)
    file.write("\n")