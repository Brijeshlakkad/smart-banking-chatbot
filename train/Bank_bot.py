from __future__ import absolute_import

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
logger = logging.getLogger(__name__)


class BankAPI(object):
    def search(self, info):
        return "Got You!"


def train_dialogue(domain_file="bank_domain.yml",model_path="models/dialogue/",training_data_file="data/stories.md"):
    from rasa_core.policies.fallback import FallbackPolicy
    fallback = FallbackPolicy(fallback_action_name="action_fallback", core_threshold=0.2, nlu_threshold=0.2)
    agent = Agent(domain_file,policies=[MemoizationPolicy(max_history=15),KerasPolicy(),fallback])
    training_data = agent.load_data(training_data_file)
    agent.train(training_data,batch_size=200,epochs=150,validation_split=0.2)
    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer
    training_data = load_data('data/training_data.json')
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',fixed_model_name="bank_nlu")
    return model_directory

def run_nlu():
    from rasa_nlu import config
    from rasa_nlu.model import Interpreter
    interpreter = Interpreter.load("models/nlu/default/bank_nlu",config.load('config.yml'))
    while True:
        inp=raw_input()
        if inp=="quit":
            break
        print(interpreter.parse(u"'"+inp+"'"))

def run_bank_bot(serve_forever=True):
    from rasa_core.agent import Agent
    from rasa_core.interpreter import RasaNLUInterpreter
    from rasa_core.channels.console import CmdlineInput
    interpreter = RasaNLUInterpreter('models/nlu/default/bank_nlu')
    agent = Agent.load('models/dialogue', interpreter = interpreter)
    if serve_forever:
		agent.handle_channels([CmdlineInput()])
    return agent

def run_bank_bot_for_web():
    from rasa_core.agent import Agent
    from rasa_core.interpreter import RasaNLUInterpreter
    from rasa_core.channels.console import CmdlineInput
    interpreter = RasaNLUInterpreter('models/nlu/default/bank_nlu')
    agent = Agent.load('models/dialogue', interpreter = interpreter)
    channel = BotServerInputChannel(agent)
    agent.handle_channels([channel])
# $ python -m rasa_core.train -d bank_domain.yml -s data/stories.md -o models/dialogue --batch_size 500 --epochs 200 --history 15 --validation_split 0.2 --nlu_threshold 0.2 --core_threshold 0.2 --fallback_action_name action_fallback

# $ python -m rasa_core.run --enable_api  -d models/dialogue -u models/nlu/default/bank_nlu --endpoints endpoints.yml

# $ python -m rasa_core.server -d models/dialogue -u models/nlu/default/bank_nlu --endpoints endpoints.yml

# chatroom connector
# $ python -m rasa_utils.bot  -d models/dialogue -u models/nlu/default/bank_nlu --endpoints endpoints.yml --enable_api

# run fb connector
# $ python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/bank_nlu --port 5002 --credentials credentials.yml --endpoints endpoints.yml
# $ python -m rasa_nlu.evaluate --data data/stories.json --config config.yml --mode crossvalidation
if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    parser = argparse.ArgumentParser(description='starts the bot')
    parser.add_argument('task',choices=["train-nlu", "train-dialogue", "run"],help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task=="run":
        run_bank_bot()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or 'run' to use the script.")
        exit(1)
