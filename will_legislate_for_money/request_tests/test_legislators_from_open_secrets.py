from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from public_officials.services import *
import pdb
import vcr

class LegislatorDataTest(TestCase):

    def test_service_gets_organizational_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_organizations'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_org_contributions("N00006134")
            self.assertTrue(legislator_contributions)
            self.assertEqual("Democracy Engine", legislator_contributions[0]['@attributes']['org_name'])

    def test_service_gets_industrial_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_industries'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_ind_contributions("N00006134")
            self.assertTrue(legislator_contributions)
            self.assertEqual("Pharmaceuticals/Health Products", legislator_contributions[0]['@attributes']['industry_name'])

    def test_get_all_legislators_returns_all_legislators(self):
        with vcr.use_cassette('cassettes/get_all_legislators'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_legislators()
            self.assertTrue(legislators)
            self.assertEqual("Luther", legislators[0]["first_name"])