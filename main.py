from Reinforce import reinforcement_learning
from speech import sentence_transcription
from reward_matrix import dataset
from time import time

sentence = sentence_transcription()
t=time()
reinforce_variables = reinforcement_learning(sentence)
print(time()-t)
for i in reinforce_variables[0]:
    print(dataset.iloc[i])