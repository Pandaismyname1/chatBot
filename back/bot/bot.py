import aiml
import hashlib
import pickle
import base64
import os
from pprint import pprint
import sys
import pronto
import re


def saveSession(k, name):
    file = open('..\\sessions\\'+name+'.ses', 'wb')
    pickle.dump(k._sessions[name], file)
    file.close()
    print('Saved session for: '+name)


def loadSession(k, name):
    file = open('..\\sessions\\'+name+'.ses', 'rb')
    session = pickle.load(file)
    file.close()
    k._sessions[name] = session
    return session


def auth(k, name):
    initialName = name
    k.setPredicate('name', name, name)
    if(os.path.isfile('..\\sessions\\'+name+'.ses')):
        loadSession(k, name)
    else:
        saveSession(k, name)


def loadBot(k, path):
    if path[:-4] == '.brn':
        k.loadBrain(path)
    else:
        from botGenerator import generateBot
        generateBot(path, '..\\brains\\' + os.path.basename(path) + '.brn')
        k.loadBrain('..\\brains\\' + os.path.basename(path) + '.brn')


if __name__ == '__main__':
    import owlready2

    onto = owlready2.get_ontology("..\\ontologies\\example.owl")
    onto.load()

    print(onto)
    # ont = pronto.Ontology('..\\ontologies\\istorie.owl')
    # ont = pronto.Ontology('https://protege.stanford.edu/ontologies/pizza/pizza.owl')

    # print(ont)
    # question = (input())

    # match = re.findall('what ([a-zA-Z\_]+) ([A-Za-z]+)?', question)
    
    # print(match)
    # obj = ont[match[0][1]]
    # relation = match[0][0]
    # response = obj.relations[pronto.Relationship(relation)].name[0]
    # print('A ' + match[0][1] + ' ' + relation + ' ' + response)

    # match = re.findall('what are the relations of ([A-Za-z]+)?', question)
    
    # print(match)
    # obj = ont[match[0]]
    # print(obj.other['comment'][0])
    # for relation in obj.relations:
    #     wth = obj.relations[relation].name[0]
    #     print(match[0] + ' ' + relation.obo_name + ' '+ wth)
    # pprint(obj)


    # path = sys.argv[1]

    # k = aiml.Kernel()
    # loadBot(k,path)
    # initialName = ''
    # while True:
    #     response = input("> ")
    #     name = k.getPredicate('name',initialName)
    #     if response == "quit":
    #         exit()
    #     elif response == "save":
    #         k.saveBrain("..\\bot_brain.brn")
    #         saveSession(k,name)
    #     else:
    #         print(k.respond(response,name))
    #         name = k.getPredicate('name',name)
    #         if(name!=initialName):
    #             auth(k, name)
