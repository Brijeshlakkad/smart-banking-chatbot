from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging
from rasa_core.training import online
from rasa_core import utils, train, run
from rasa_core.agent import Agent
from rasa_core.channels.console import CmdlineInput
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
logger = logging.getLogger(__name__)
def train_agent():
    return train.train_dialogue_model(domain_file="bank_domain.yml",stories_file="data/stories.md",output_path="models/dialogue",max_history=10,kwargs={"batch_size": 50,"epochs": 200,"max_training_samples": 300 })

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    agent = train_agent()
    online.run_online_learning(agent)
#to train using cmd: $ python -m rasa_core_sdk.endpoint --actions actions & python -m rasa_core.train --online -o models/dialogue -u models/nlu/default/bank_nlu  -d bank_domain.yml -s data/stories.md --endpoints endpoints.yml --batch_size 500 --epochs 200 --history 15 --validation_split 0.2 --nlu_threshold 0.2 --core_threshold 0.2 --fallback_action_name action_fallback
