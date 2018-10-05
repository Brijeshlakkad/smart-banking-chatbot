from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import pickle
import warnings
import typing

from typing import Optional, Any, List, Text, Dict, Callable

import numpy as np
from sklearn.base import clone
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle as sklearn_shuffle

from rasa_core.policies.policy import Policy
from rasa_core.featurizers import TrackerFeaturizer, MaxHistoryTrackerFeaturizer
logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    import sklearn
    from rasa_core.domain import Domain
    from rasa_core.trackers import DialogueStateTracker


class SklearnPolicy(Policy):
    def train(self, training_trackers, domain,  **kwargs):
        training_data = self.featurize_for_training(training_trackers, domain, **kwargs)
        X, y = self._extract_training_data(training_data)
        model = self.model_architecture(**kwargs)
        score = None
        self.label_encoder = clone(self.label_encoder).fit(y)
        Xt, yt = self._preprocess_data(X, y)

        if self.cv is None:
            model = clone(model).fit(Xt, yt)
        else:
            param_grid = self.param_grid or {}
            model, score = self._search_and_score(
                model, Xt, yt, param_grid)

        self.model = model
        logger.info("Done fitting sklearn policy model")
        if score is not None:
            logger.info("Cross validation score: {:.5f}".format(score))
