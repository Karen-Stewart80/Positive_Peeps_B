import unittest
from main import create_app, db
from models.Profiles import Profiles
from models.Users import Users

class TestProfiles(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_profiles_index(self):
        response= self.client.get("/profiles/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)



    def test_profiles_create(self):
        response = self.client.post("/auth/register",                   
        json = {                                                        
            "email": "test1@test.com",
            "password": "123456"

        })
        response = self.client.post("/auth/login",                      
        json = {              
            "email": "test1@test.com",
            "password": "123456"
        })                    
        data = response.get_json()                                      
        headers_data= {                                                 
            'Authorization': f"Bearer {data['token']}"
        }
        data = {                                                       
            "username" : "test_username", 
            "fname" : "test", 
            "lname" : "test",
            "account_active": "True",
            "github": "True",
            "back_end": "True",
            "full_stack": "True",
            "front_end": "True"
        }
       
        response = self.client.post("/profiles/",                       
        json = data,                                                    
        headers = headers_data)  

        self.assertEqual(response.status_code, 200)

        self.assertIsInstance(data, dict)
        self.assertTrue(bool("userid" in data.keys()))

        profiles = Profiles.query.get(data["userid"])
        self.assertIsNotNone(profiles)

    def test_profiles_delete(self):
         response = self.client.post("/auth/register",                   
        json = {                                                        
            "email": "test1@test.com",
            "password": "123456"

        })
        response = self.client.post("/auth/login",                      
        json = {              
            "email": "test1@test.com",
            "password": "123456"
        })                    
        data = response.get_json()                                      
        headers_data= {                                                 
            'Authorization': f"Bearer {data['token']}"
        }
        data = {                                                       
            "username" : "test_username", 
            "fname" : "test", 
            "lname" : "test",
            "account_active": "True",
            "github": "True",
            "back_end": "True",
            "full_stack": "True",
            "front_end": "True"
        }

        profile = Profiles.query.filter_by(username=test_username).first()

        #profiles = Profiles.query.first()

        response = self.client.delete(f"/profiles/{profiles.userid}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        profiles = Profiles.query.get(profiles.userid)
        self.assertIsNone(profiles)