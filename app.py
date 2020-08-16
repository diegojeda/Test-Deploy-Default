# App Back End

from werkzeug.utils import cached_property
from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields
import joblib

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Income Prediction API',
    description='Income Prediction API')

ns = api.namespace('Prediction', 
     description='Income Prediction')
   
parser = api.parser()

parser.add_argument(
    'Age', 
    type=int, 
    required=True, 
    help='Age for the person', 
    location='args')

parser.add_argument(
    'workclass', 
    type=int, 
    required=True, 
    help='workclass for the person', 
    location='args')

parser.add_argument(
    'education', 
    type=int, 
    required=True, 
    help='education level for the person', 
    location='args')

parser.add_argument(
    'marital-status', 
    type=int, 
    required=True, 
    help='marital-status for the person', 
    location='args')

parser.add_argument(
    'occupation', 
    type=int, 
    required=True, 
    help='occupation for the person', 
    location='args')

parser.add_argument(
    'relationship', 
    type=int, 
    required=True, 
    help='relationship for the person', 
    location='args')

parser.add_argument(
    'race', 
    type=int, 
    required=True, 
    help='race for the person', 
    location='args')

parser.add_argument(
    'gender', 
    type=int, 
    required=True, 
    help='gender for the person', 
    location='args')

parser.add_argument(
    'capital-gain', 
    type=int, 
    required=True, 
    help='capital-gain for the person', 
    location='args')

parser.add_argument(
    'capital-loss', 
    type=int, 
    required=True, 
    help='capital-loss for the person', 
    location='args')

parser.add_argument(
    'hours-per-week', 
    type=int, 
    required=True, 
    help='hours-per-week working for the person', 
    location='args')

parser.add_argument(
    'native-country', 
    type=int, 
    required=True, 
    help='native-country for the person', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
});