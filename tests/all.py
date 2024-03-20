import unittest

import os
import libs.KrakenAPI as KrakenAPI

from dotenv import load_dotenv
load_dotenv()


class TestKraken(unittest.TestCase):
    def test_mpan(self):
        api_key = os.getenv("API_KEY")
        kraken = KrakenAPI.KrakenAPI(api_key)
        result = kraken.get_meter_point(os.getenv("ELEC_MPAN"))
        print(result)
        kraken.close()
        self.assertEqual(result['mpan'], os.getenv("ELEC_MPAN"))

    def test_mpan_usage(self):
        api_key = os.getenv("API_KEY")
        kraken = KrakenAPI.KrakenAPI(api_key)
        result = kraken.get_meter_point_consumption(os.getenv("ELEC_MPAN"),os.getenv("ELEC_SERIAL"))
        print(result)
        kraken.close()
        self.assertGreater(result['count'], 0)

    def test_mpan_usage(self):
        api_key = os.getenv("API_KEY")
        kraken = KrakenAPI.KrakenAPI(api_key)
        result = kraken.get_gas_meter_point_consumption(os.getenv("GAS_MPRN"),os.getenv("GAS_SERIAL"))
        print(result)
        kraken.close()
        self.assertGreater(result['count'], 0)

    def test_products(self):
        api_key = os.getenv("API_KEY")
        kraken = KrakenAPI.KrakenAPI(api_key)
        result = kraken.get_products()
        print(result)
        kraken.close()
        # check count is greater than 0
        self.assertGreater(result['count'], 0)


if __name__ == '__main__':
    unittest.main()