from flask import Flask, render_template, request
from .model import model
from .model_input import exp


def create_app():
    APP = Flask(__name__)
    APP.static_folder = 'static'

    @APP.route('/')
    def form():
        '''Homepage with input fields

        :returns: input feilds
        :rtype: html page
        '''
        return render_template('base.html')

    @APP.route('/data/', methods=['POST', 'GET'])
    def root():
        '''Takes user input and produces kickstarter outcome

        :returns: html page with input fields and model results
        :rtype: html page
        '''
        if request.method == 'GET':
            return "/data is accessed directly. Go to '/' to submit form"

        if request.method == 'POST':
            campaign_length = request.form.get('campaign_length')
            percentage_pledged = request.form.get('percentage_pledged')
            backers = request.form.get('num_backers')
            currency = request.form.get('currency')
            category = request.form.get('category')

            user_input = exp(campaign_length, percentage_pledged,
                             backers, currency, category)

        model_display = model(user_input)

        if model_display[0] == 1:
            status = 'success!'
            return render_template('data.html', status=status)
        else:
            status = 'failure...try again!'
            return render_template('data.html', status=status)

    return APP
