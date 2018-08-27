from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
import numpy as np
import spacy
import json
import spacy
from rasa_nlu.converters import load_data
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
warnings.filterwarnings(action='ignore', message="UndefinedMetricWarning")
def train_nlu(data, config, model_dir):
    trainer =Trainer(RasaNLUConfig(config))
    training_data = load_data(data)
    trainer.train(training_data)
    model_directory=trainer.persist(model_dir, fixed_model_name="bank_nlu")
def run_nlu():
    interpreter = Interpreter.load("models/nlu/default/bank_nlu", RasaNLUConfig('config_spacy.json'))
    while True:
        inp=raw_input()
        if inp=="quit":
            break
        print(interpreter.parse(u"'"+inp+"'"))
if __name__ == '__main__':
    #train_nlu("data/training_data.json","config_spacy.json","models/nlu")
    run_nlu()
