import random
import json
import torch
#import tkinter
from Brain import NeuralNet
from Neuralnetwork import bag_of_words , tokenize
#import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "trainData.pth"
data = torch.load(FILE)

#model training
input_size = data['input_size']
hideen_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size,hideen_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#------------------------------------
Name = "Jarvis"
from Listen import Listen
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution
from Gui import ImageLabel
def Main():

    sentence = Listen()
    result = str(sentence)

    if sentence == "bye":
        exit()
    
    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution()
                elif "day" in reply:
                    NonInputExecution()
                
                elif "wikipedia" in reply:
                    InputExecution(reply,result)
                
                elif "google" in reply:
                    InputExecution(reply,result)
                
                elif "github" in reply:
                    InputExecution(reply,result)
                
                elif "w3 schools" in reply:
                    InputExecution(reply,result)
                
                elif "songs" in reply:
                    InputExecution(reply,result)
#ImageLabel()           
Main()
