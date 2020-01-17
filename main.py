from Reinforce import reinforcement_learning
from speech import sentence_transcription
from reward_matrix import dataset
import time
from LED import led_management

state = 0
while True:
    sentence = sentence_transcription()
    t=time.time()
    reinforce_variables = reinforcement_learning(sentence, state)
    print(time.time()-t)
    for i in reinforce_variables[0]:
        print(dataset.iloc[i])
        led_management(dataset.iloc[i]['eyes'])
        print("Paw is {}".format('up' if dataset.iloc[i]['paw'] == 0 else 'down'))
        state = i
    time.sleep(3)