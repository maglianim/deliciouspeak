from flask_testing import TestCase

from api.main import create_app
from api.biz.core.DbService import DbService

class BaseTest(TestCase):

    db_Service = DbService();

    def create_app(self):
        # pass in test configuration
        return create_app().app

    def setUp(self):
        self.db_Service.create_all()

    def tearDown(self):
        self.db_Service.drop_all()
