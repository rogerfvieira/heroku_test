import pickle


def model(input_data):
    '''Description...

    :param input_data:
    :param type:
    :returns:
    :rtype: list
    '''
    rf = pickle.load(open('model_pickle_lr', 'rb'))
#   pred = rf.predict(input_data)
    prob=rf.predict_proba(input_input)[0][1]
    return prob
