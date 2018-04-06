import io
import json
import random
from snips_nlu import load_resources, SnipsNLUEngine


from src.witness import Witness
from text.generic_text import get_generic_phrase

import pdb

def load_entities(name):
    with open("entities/"+name+".txt") as f:
        entities = map(lambda x: x.strip().split(",")[0], f.readlines())
    return list(entities)

def start():
    load_resources("en")
    with io.open("trained.json") as f:
        engine_dict = json.load(f)
    engine = SnipsNLUEngine.from_dict(engine_dict)
    return engine

def setup():
    people = list()
    rooms = load_entities("room")
    names = load_entities("name")
    murder_room = random.choice(rooms)
    random.shuffle(names)
    pdb.set_trace()
    #killer
    killer = Witness(names[0],True,murder_room,[])
    people.append(killer)
    rooms.remove(murder_room)
    # assign room
    for i in range(1,6):
        w = Witness(names[i],False,random.choice(rooms),[])
        people.append(w)

    # assign people around
    for w in people:
        for h in people:
            if not w.killer and not h.killer:
                if w.room == h.room:
                    if w.name != h.name:
                        w.around.add(h)
    random.shuffle(people)
    return people
    

def main():
    engine = start()
    # setup scene
    people = setup()
    while True:
        print("Select person to talk to:")
        for i,actor in enumerate(people):
            print("%d. %s" % (i,actor.name))
        print("x. To accuss somebody and end the game")
        n = input("> ")
        if n == "x":
            name = input("Who is the murderer?: ")
            if len(list(filter(lambda x: x.name == name and x.killer,people))) > 0:
                print("Congrats! You win")
        try:
            n = int(n)
            actor = people[n]
        except:
            print("Invalid input")
            continue
        loop(engine,actor)

def loop(engine,actor):
    print("Hello detective!")
    while True:
        question = input("> ")
        q = engine.parse(question)
        if q["intent"] != None and q["intent"]["probability"] > 0.7:
            #ASUMIR CORRECTA LA FRASE

            # (usar diccionarios y funciones para simular switch)
            if q["intent"]["intentName"] == "where":
                print(actor.answerPlace())
            if q["intent"]["intentName"] == "who":
                print(actor.answerWho())
            if q["intent"]["intentName"] == "whatsYourName":
                print(actor.answerName())
            if q["intent"]["intentName"] == "workplace":
                print(actor.answerWorkpace())
            if q["intent"]["intentName"] == "bye":
                break
        else:
            print(get_generic_phrase())
            pass


if __name__ == "__main__":
    main()
