# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions. The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.   How to use this API documentation ----------------   You may browse the API routes without authentication, but if you wish to send requests to the API and see response data, then you must authenticate. 1. Obtain a JWT token by `POST`ing  to the `/login` route in the `Authentication` section with your API key and credentials. 1. Paste the JWT token from the response into the \"JWT Token\" field at the top of the page and click the 'Add Token' button.   You will now be able to use the remaining routes to send requests to the API and get a response.   Language Selection ----------------   Language selection is done via the `Accept-Language` header. At the moment, you may only pass one language abbreviation in the header at a time. Valid language abbreviations can be found at the `/languages` route..   Authentication ----------------   Authentication to use the API is similar to the How-to section above. Users must `POST` to the `/login` route with their API key and credentials in the following format in order to obtain a JWT token.  `{\"apikey\":\"APIKEY\",\"username\":\"USERNAME\",\"userkey\":\"USERKEY\"}`  Note that the username and key are ONLY required for the `/user` routes. The user's key is labled `Account Identifier` in the account section of the main site. The token is then used in all subsequent requests by providing it in the `Authorization` header. The header will look like: `Authorization: Bearer <yourJWTtoken>`. Currently, the token expires after 24 hours. You can `GET` the `/refresh_token` route to extend that expiration date.   Versioning ----------------   You may request a different version of the API by including an `Accept` header in your request with the following format: `Accept:application/vnd.thetvdb.v$VERSION`. This documentation automatically uses the version seen at the top and bottom of the page.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.auth import Auth
from .models.basic_episode import BasicEpisode
from .models.conflict import Conflict
from .models.episode import Episode
from .models.episode_data_query_params import EpisodeDataQueryParams
from .models.episode_record_data import EpisodeRecordData
from .models.filter_keys import FilterKeys
from .models.json_errors import JSONErrors
from .models.language import Language
from .models.language_data import LanguageData
from .models.links import Links
from .models.not_authorized import NotAuthorized
from .models.not_found import NotFound
from .models.series import Series
from .models.series_actors import SeriesActors
from .models.series_actors_data import SeriesActorsData
from .models.series_data import SeriesData
from .models.series_episodes import SeriesEpisodes
from .models.series_episodes_query import SeriesEpisodesQuery
from .models.series_episodes_query_params import SeriesEpisodesQueryParams
from .models.series_episodes_summary import SeriesEpisodesSummary
from .models.series_image_query_result import SeriesImageQueryResult
from .models.series_image_query_result_ratings_info import SeriesImageQueryResultRatingsInfo
from .models.series_image_query_results import SeriesImageQueryResults
from .models.series_images_count import SeriesImagesCount
from .models.series_images_counts import SeriesImagesCounts
from .models.series_images_query_param import SeriesImagesQueryParam
from .models.series_images_query_params import SeriesImagesQueryParams
from .models.series_search_data import SeriesSearchData
from .models.token import Token
from .models.update import Update
from .models.update_data import UpdateData
from .models.update_data_query_params import UpdateDataQueryParams
from .models.user import User
from .models.user_data import UserData
from .models.user_favorites import UserFavorites
from .models.user_favorites_data import UserFavoritesData
from .models.user_ratings import UserRatings
from .models.user_ratings_data import UserRatingsData
from .models.user_ratings_data_no_links import UserRatingsDataNoLinks
from .models.user_ratings_data_no_links_empty_array import UserRatingsDataNoLinksEmptyArray
from .models.user_ratings_query_params import UserRatingsQueryParams

# import apis into sdk package
from .apis.authentication_api import AuthenticationApi
from .apis.episodes_api import EpisodesApi
from .apis.languages_api import LanguagesApi
from .apis.search_api import SearchApi
from .apis.series_api import SeriesApi
from .apis.updates_api import UpdatesApi
from .apis.users_api import UsersApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
