from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
logger = logging.getLogger(__name__)
def run_bank_online(input_channel, interpreter,domain_file="bank_domain.yml",training_data_file='data/stories.md'):
    model_path="models/dialogue/"
    fallback = FallbackPolicy(fallback_action_name="action_fallback", core_threshold=0.2, nlu_threshold=0.2)
    agent = Agent(domain_file,policies=[MemoizationPolicy(max_history=10), KerasPolicy(), fallback],interpreter=interpreter)
    agent.train_online(training_data_file,input_channel=input_channel,batch_size=200,epochs=194)
    agent.persist(model_path)
    return agent
if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('models/nlu/default/bank_nlu')
    run_bank_online(ConsoleInputChannel(), interpreter=nlu_interpreter)
