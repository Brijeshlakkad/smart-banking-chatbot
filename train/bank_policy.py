from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging
from rasa_core.policies.keras_policy import KerasPolicy
logger = logging.getLogger(__name__)

class BankPolicy(KerasPolicy):
    def model_architecture(self, input_shape, output_shape):
        """Build a keras model and return a compiled model."""
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Masking, LSTM, Dense, TimeDistributed, Activation
        model = Sequential()
        if len(output_shape) == 1:
            model.add(Masking(mask_value=-1, input_shape=input_shape))
            model.add(LSTM(self.rnn_size, dropout=0.2))
            model.add(Dense(input_dim=self.rnn_size, units=output_shape[-1]))
        elif len(output_shape) == 2:
            model.add(Masking(mask_value=-1,
                              input_shape=(None, input_shape[1])))
            model.add(LSTM(self.rnn_size, return_sequences=True, dropout=0.2))
            model.add(TimeDistributed(Dense(units=output_shape[-1])))
        else:
            raise ValueError("Cannot construct the model because length of output_shape = {} should be 1 or 2.".format(len(output_shape)))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        logger.debug(model.summary())
        return model
    def train(self, training_trackers, domain, **kwargs):
        if kwargs.get('rnn_size') is not None:
            logger.debug("Parameter `rnn_size` is updated with {}".format(kwargs.get('rnn_size')))
            self.rnn_size = kwargs.get('rnn_size')
        training_data = self.featurize_for_training(training_trackers, domain, **kwargs)
        shuffled_X, shuffled_y = training_data.shuffled_X_y()
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.session = tf.Session()
            with self.session.as_default():
                if self.model is None:
                    self.model = self.model_architecture(shuffled_X.shape[1:],
                                                         shuffled_y.shape[1:])
                validation_split = kwargs.get("validation_split", 0.0)
                logger.info("Fitting model with {} total samples and a validation split of {}".format(training_data.num_examples(), validation_split))
                params = self._get_valid_params(self.model.fit, **kwargs)
                self.model.fit(shuffled_X, shuffled_y, **params)
                self.current_epoch = kwargs.get("epochs", 1)
                logger.info("Done fitting keras policy model")
