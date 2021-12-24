import pickle


def model(input_data):
    '''Description...

    :param input_data:
    :param type:
    :returns:
    :rtype: list
    '''
    rf = pickle.load(open('model_pickle_lr', 'rb'))
    prob = rf.predict_proba(input_data)[0][1]*100
    return prob
