import numpy as np


def exp(campaign_length, percentage_pledged, backers, currency, category):
    '''
    '''

    list_currencies = ['AUD', 'CAD', 'CHF', 'DKK', 'EUR', 'GBP', 'HKD',
                       'JPY', 'MXN', 'NOK', 'NZD', 'SEK', 'SGD', 'USD']
    list_categories = ['Art', 'Comics', 'Crafts', 'Dance', 'Design',
                       'Fashion', 'Film & Video', 'Food', 'Games',
                       'Journalism', 'Music', 'Photography',
                       'Publishing', 'Technology', 'Theater']

    def currency_category_select(user_input, list_input):
        ''' Gets the user_input and list of options and picks an option,
            sets the selected option as 1 and all other options as zero

        :param user_input: user input for currency and category
        :type user_input: str
        :param list_input: list of currencies or categories
        :type list_input: str
        :returns: a list of 1's and 0's based on input
        :rtype: list
        '''
        for x in range(len(list_input)):
            if list_input[x] == user_input:
                list_input[x] = 1
            else:
                list_input[x] = 0

        return list_input

    input_currency = currency_category_select(currency,
                                              list_currencies)
    input_category = currency_category_select(category,
                                              list_categories)

    model_input = np.array([campaign_length,
                           percentage_pledged,
                           backers])

    model_input = np.append(model_input,
                            input_currency)

    model_input = np.append(model_input,
                            input_category).reshape(1, -1)
    return model_input
