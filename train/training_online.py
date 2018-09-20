from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging
from rasa_core.agent import Agent
from rasa_core.channels.console import CmdlineInput
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
<<<<<<< HEAD

logger = logging.getLogger(__name__)
def run_bank_online(input_channel, interpreter,domain_file="bank_domain.yml",training_data_file='data/stories.md'):
    model_path="models/dialogue/"
    agent = Agent(domain_file,policies=[MemoizationPolicy(max_history=10), KerasPolicy()],interpreter=interpreter)
    agent.train_online(training_data_file,input_channel=input_channel,batch_size=200,epochs=150)
    agent.persist(model_path)
    return agent
=======
from rasa_core.training import online
from rasa_core import utils, train, run
logger = logging.getLogger(__name__)
def train_agent():
    return train.train_dialogue_model(domain_file="bank_domain.yml",
                                      stories_file="data/stories.md",
                                      output_path="models/dialogue",
                                      max_history=10,
                                      kwargs={"batch_size": 50,
                                              "epochs": 200,
                                              "max_training_samples": 300
                                              })


>>>>>>> 5acb14952dd43d910f096c553f1305c6cfb60e53
if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    agent = train_agent()
    online.run_online_learning(agent)
