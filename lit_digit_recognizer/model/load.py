from keras.models import model_from_json
import tensorflow as tf
import os
here = os.path.dirname(os.path.abspath(__file__))


def init():
    print(here)
    model_json = os.path.join(here, 'model.json')
    json_file = open(model_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(os.path.join(here, 'model.h5'))
    print("Loaded Model from disk")

    # compile and evaluate loaded model
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # loss,accuracy = model.evaluate(X_test,y_test)
    # print('loss:', loss)
    # print('accuracy:', accuracy)
    graph = tf.get_default_graph()

    return loaded_model, graph
