import unittest
import requests


class MicroserviceTestCase(unittest.TestCase):
    def test_M0_get_data(self):
        response = requests.get('http://127.0.0.1:8080/getData')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')
        # self.assertTrue(len(response.text) > 0)
        # self.assertIsNotNone(response.json())

    def test_M1_post_request(self):
        data = [{"username": "tomst", "ghlink": "filename"}, {"username": "dfgdfg", "dfgdfg": "fghfgh"}]
        response = requests.post("http://127.0.0.1:8081/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), data)

    def test_M2_post_request_with_W(self):
        data = [{"username": "Wario"}, {"username": "fghfgh"}, {"username": "ertert"}]
        response = requests.post("http://127.0.0.1:8082/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["Wario"])

    def test_M2_post_request_with_data_missing_username(self):
        data = [{"username": "Wario"}, {"no_username": "dfgdfg"}, {"username": "ertert"}]
        response = requests.post("http://127.0.0.1:8082/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["Wario"])

    def test_M3_post_request_with_valid_data_D(self):
        data = [{"username": "davor"}, {"username": "dadada"}]
        response = requests.post("http://127.0.0.1:8083/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["davor", "dadada"])

    def test_M3_post_request_with_empty_data(self):
        data = []
        response = requests.post("http://127.0.0.1:8083/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_M3_post_request_with_username_not_starting_with_d(self):
        data = [{"username": "john"}, {"username": "daisy"}]
        response = requests.post("http://127.0.0.1:8083/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["daisy"])

    def test_M4_post_gatherData(self):
        data = [{"username": "davor"}, {"username": "dadada"}]
        response = requests.post("http://127.0.0.1:8084/gatherData", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["davor", "dadada"])


if __name__ == '__main__':
    unittest.main()
