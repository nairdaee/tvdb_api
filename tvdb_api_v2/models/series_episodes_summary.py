# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions. The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.   How to use this API documentation ----------------   You may browse the API routes without authentication, but if you wish to send requests to the API and see response data, then you must authenticate. 1. Obtain a JWT token by `POST`ing  to the `/login` route in the `Authentication` section with your API key and credentials. 1. Paste the JWT token from the response into the \"JWT Token\" field at the top of the page and click the 'Add Token' button.   You will now be able to use the remaining routes to send requests to the API and get a response.   Language Selection ----------------   Language selection is done via the `Accept-Language` header. At the moment, you may only pass one language abbreviation in the header at a time. Valid language abbreviations can be found at the `/languages` route..   Authentication ----------------   Authentication to use the API is similar to the How-to section above. Users must `POST` to the `/login` route with their API key and credentials in the following format in order to obtain a JWT token.  `{\"apikey\":\"APIKEY\",\"username\":\"USERNAME\",\"userkey\":\"USERKEY\"}`  Note that the username and key are ONLY required for the `/user` routes. The user's key is labled `Account Identifier` in the account section of the main site. The token is then used in all subsequent requests by providing it in the `Authorization` header. The header will look like: `Authorization: Bearer <yourJWTtoken>`. Currently, the token expires after 24 hours. You can `GET` the `/refresh_token` route to extend that expiration date.   Versioning ----------------   You may request a different version of the API by including an `Accept` header in your request with the following format: `Accept:application/vnd.thetvdb.v$VERSION`. This documentation automatically uses the version seen at the top and bottom of the page.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SeriesEpisodesSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, aired_episodes=None, aired_seasons=None, dvd_episodes=None, dvd_seasons=None):
        """
        SeriesEpisodesSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aired_episodes': 'str',
            'aired_seasons': 'list[str]',
            'dvd_episodes': 'str',
            'dvd_seasons': 'list[str]'
        }

        self.attribute_map = {
            'aired_episodes': 'airedEpisodes',
            'aired_seasons': 'airedSeasons',
            'dvd_episodes': 'dvdEpisodes',
            'dvd_seasons': 'dvdSeasons'
        }

        self._aired_episodes = aired_episodes
        self._aired_seasons = aired_seasons
        self._dvd_episodes = dvd_episodes
        self._dvd_seasons = dvd_seasons

    @property
    def aired_episodes(self):
        """
        Gets the aired_episodes of this SeriesEpisodesSummary.
        Number of all aired episodes for this series

        :return: The aired_episodes of this SeriesEpisodesSummary.
        :rtype: str
        """
        return self._aired_episodes

    @aired_episodes.setter
    def aired_episodes(self, aired_episodes):
        """
        Sets the aired_episodes of this SeriesEpisodesSummary.
        Number of all aired episodes for this series

        :param aired_episodes: The aired_episodes of this SeriesEpisodesSummary.
        :type: str
        """

        self._aired_episodes = aired_episodes

    @property
    def aired_seasons(self):
        """
        Gets the aired_seasons of this SeriesEpisodesSummary.

        :return: The aired_seasons of this SeriesEpisodesSummary.
        :rtype: list[str]
        """
        return self._aired_seasons

    @aired_seasons.setter
    def aired_seasons(self, aired_seasons):
        """
        Sets the aired_seasons of this SeriesEpisodesSummary.

        :param aired_seasons: The aired_seasons of this SeriesEpisodesSummary.
        :type: list[str]
        """

        self._aired_seasons = aired_seasons

    @property
    def dvd_episodes(self):
        """
        Gets the dvd_episodes of this SeriesEpisodesSummary.
        Number of all dvd episodes for this series

        :return: The dvd_episodes of this SeriesEpisodesSummary.
        :rtype: str
        """
        return self._dvd_episodes

    @dvd_episodes.setter
    def dvd_episodes(self, dvd_episodes):
        """
        Sets the dvd_episodes of this SeriesEpisodesSummary.
        Number of all dvd episodes for this series

        :param dvd_episodes: The dvd_episodes of this SeriesEpisodesSummary.
        :type: str
        """

        self._dvd_episodes = dvd_episodes

    @property
    def dvd_seasons(self):
        """
        Gets the dvd_seasons of this SeriesEpisodesSummary.

        :return: The dvd_seasons of this SeriesEpisodesSummary.
        :rtype: list[str]
        """
        return self._dvd_seasons

    @dvd_seasons.setter
    def dvd_seasons(self, dvd_seasons):
        """
        Sets the dvd_seasons of this SeriesEpisodesSummary.

        :param dvd_seasons: The dvd_seasons of this SeriesEpisodesSummary.
        :type: list[str]
        """

        self._dvd_seasons = dvd_seasons

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SeriesEpisodesSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
