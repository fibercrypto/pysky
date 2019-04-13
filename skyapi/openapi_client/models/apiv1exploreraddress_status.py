# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.25.1
    Contact: skycoin.doe@example.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Apiv1exploreraddressStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'unconfirmed': 'bool',
        'block_seq': 'int',
        'label': 'int',
        'confirmed': 'bool'
    }

    attribute_map = {
        'unconfirmed': 'unconfirmed',
        'block_seq': 'block_seq',
        'label': 'label',
        'confirmed': 'confirmed'
    }

    def __init__(self, unconfirmed=None, block_seq=None, label=None, confirmed=None):  # noqa: E501
        """Apiv1exploreraddressStatus - a model defined in OpenAPI"""  # noqa: E501

        self._unconfirmed = None
        self._block_seq = None
        self._label = None
        self._confirmed = None
        self.discriminator = None

        if unconfirmed is not None:
            self.unconfirmed = unconfirmed
        if block_seq is not None:
            self.block_seq = block_seq
        if label is not None:
            self.label = label
        if confirmed is not None:
            self.confirmed = confirmed

    @property
    def unconfirmed(self):
        """Gets the unconfirmed of this Apiv1exploreraddressStatus.  # noqa: E501


        :return: The unconfirmed of this Apiv1exploreraddressStatus.  # noqa: E501
        :rtype: bool
        """
        return self._unconfirmed

    @unconfirmed.setter
    def unconfirmed(self, unconfirmed):
        """Sets the unconfirmed of this Apiv1exploreraddressStatus.


        :param unconfirmed: The unconfirmed of this Apiv1exploreraddressStatus.  # noqa: E501
        :type: bool
        """

        self._unconfirmed = unconfirmed

    @property
    def block_seq(self):
        """Gets the block_seq of this Apiv1exploreraddressStatus.  # noqa: E501


        :return: The block_seq of this Apiv1exploreraddressStatus.  # noqa: E501
        :rtype: int
        """
        return self._block_seq

    @block_seq.setter
    def block_seq(self, block_seq):
        """Sets the block_seq of this Apiv1exploreraddressStatus.


        :param block_seq: The block_seq of this Apiv1exploreraddressStatus.  # noqa: E501
        :type: int
        """

        self._block_seq = block_seq

    @property
    def label(self):
        """Gets the label of this Apiv1exploreraddressStatus.  # noqa: E501


        :return: The label of this Apiv1exploreraddressStatus.  # noqa: E501
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Apiv1exploreraddressStatus.


        :param label: The label of this Apiv1exploreraddressStatus.  # noqa: E501
        :type: int
        """

        self._label = label

    @property
    def confirmed(self):
        """Gets the confirmed of this Apiv1exploreraddressStatus.  # noqa: E501


        :return: The confirmed of this Apiv1exploreraddressStatus.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this Apiv1exploreraddressStatus.


        :param confirmed: The confirmed of this Apiv1exploreraddressStatus.  # noqa: E501
        :type: bool
        """

        self._confirmed = confirmed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Apiv1exploreraddressStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
