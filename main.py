from Reinforce import reinforcement_learning
from speech import sentence_transcription
from reward_matrix import dataset

sentence = sentence_transcription()
reinforce_variables = reinforcement_learning(sentence)

for i in reinforce_variables[0]:
    print(dataset.iloc[i])