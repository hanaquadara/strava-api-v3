# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import strava_client
from models.explorer_response import ExplorerResponse  # noqa: E501
from strava_client.rest import ApiException


class TestExplorerResponse(unittest.TestCase):
    """ExplorerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExplorerResponse(self):
        """Test ExplorerResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = strava_client.models.explorer_response.ExplorerResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
