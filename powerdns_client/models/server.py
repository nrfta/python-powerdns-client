# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Server(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'id': 'str',
        'daemon_type': 'str',
        'version': 'str',
        'url': 'str',
        'config_url': 'str',
        'zones_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'daemon_type': 'daemon_type',
        'version': 'version',
        'url': 'url',
        'config_url': 'config_url',
        'zones_url': 'zones_url'
    }

    def __init__(self, type=None, id=None, daemon_type=None, version=None, url=None, config_url=None, zones_url=None):  # noqa: E501
        """Server - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._daemon_type = None
        self._version = None
        self._url = None
        self._config_url = None
        self._zones_url = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if daemon_type is not None:
            self.daemon_type = daemon_type
        if version is not None:
            self.version = version
        if url is not None:
            self.url = url
        if config_url is not None:
            self.config_url = config_url
        if zones_url is not None:
            self.zones_url = zones_url

    @property
    def type(self):
        """Gets the type of this Server.  # noqa: E501

        Set to “Server”  # noqa: E501

        :return: The type of this Server.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Server.

        Set to “Server”  # noqa: E501

        :param type: The type of this Server.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this Server.  # noqa: E501

        The id of the server, “localhost”  # noqa: E501

        :return: The id of this Server.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Server.

        The id of the server, “localhost”  # noqa: E501

        :param id: The id of this Server.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def daemon_type(self):
        """Gets the daemon_type of this Server.  # noqa: E501

        “recursor” for the PowerDNS Recursor and “authoritative” for the Authoritative Server  # noqa: E501

        :return: The daemon_type of this Server.  # noqa: E501
        :rtype: str
        """
        return self._daemon_type

    @daemon_type.setter
    def daemon_type(self, daemon_type):
        """Sets the daemon_type of this Server.

        “recursor” for the PowerDNS Recursor and “authoritative” for the Authoritative Server  # noqa: E501

        :param daemon_type: The daemon_type of this Server.  # noqa: E501
        :type: str
        """

        self._daemon_type = daemon_type

    @property
    def version(self):
        """Gets the version of this Server.  # noqa: E501

        The version of the server software  # noqa: E501

        :return: The version of this Server.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Server.

        The version of the server software  # noqa: E501

        :param version: The version of this Server.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def url(self):
        """Gets the url of this Server.  # noqa: E501

        The API endpoint for this server  # noqa: E501

        :return: The url of this Server.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Server.

        The API endpoint for this server  # noqa: E501

        :param url: The url of this Server.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def config_url(self):
        """Gets the config_url of this Server.  # noqa: E501

        The API endpoint for this server’s configuration  # noqa: E501

        :return: The config_url of this Server.  # noqa: E501
        :rtype: str
        """
        return self._config_url

    @config_url.setter
    def config_url(self, config_url):
        """Sets the config_url of this Server.

        The API endpoint for this server’s configuration  # noqa: E501

        :param config_url: The config_url of this Server.  # noqa: E501
        :type: str
        """

        self._config_url = config_url

    @property
    def zones_url(self):
        """Gets the zones_url of this Server.  # noqa: E501

        The API endpoint for this server’s zones  # noqa: E501

        :return: The zones_url of this Server.  # noqa: E501
        :rtype: str
        """
        return self._zones_url

    @zones_url.setter
    def zones_url(self, zones_url):
        """Sets the zones_url of this Server.

        The API endpoint for this server’s zones  # noqa: E501

        :param zones_url: The zones_url of this Server.  # noqa: E501
        :type: str
        """

        self._zones_url = zones_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Server, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Server):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
