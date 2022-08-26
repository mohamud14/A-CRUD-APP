from unicodedata import name
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

from main import app, db


class TestBase(LiveServerTestCase):
    TEST_PORT = 5050  # test port, doesn't need to be open

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            LIVESERVER_PORT=self.TEST_PORT,
            DEBUG=True,
            TESTING=True
        )
        return app

    def setUp(self):
        from schema import Teams, Players
        db.create_all()  # create schema before we try to get the page

        test_team = Teams(team_name="Test",team_id=1)
        db.session.add(test_team)
        test_player = Players(player_name="Test Player",player_id=10, plays_for=1)
        db.session.add(test_player)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestIndex(TestBase):

    def test_index_route(self):
        response = app.test_client().get('/')

        assert response.status_code == 200

########################## ADD MORE TESTS ##################################
