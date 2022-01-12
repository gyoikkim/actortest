# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class ActortestError(Exception):
    """A custom core Actortest exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(ActortestError, self).__init__(message)


class ActortestNotImplemented(ActortestError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(ActortestNotImplemented, self).__init__(message)


class ActortestAPIError(ActortestError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Actortest API'
        else:
            message = 'Http response error from Actortest API. {0}'.format(message)

        super(ActortestAPIError, self).__init__(message)


class ActortestApiAuthError(ActortestAPIError):
    """A custom exception for API authentication errors"""
    pass


class ActortestMissingDependency(ActortestError):
    """A custom exception for missing dependencies."""
    pass


class ActortestWarning(Warning):
    """Base warning for Actortest."""


class ActortestUserWarning(UserWarning, ActortestWarning):
    """The primary warning class."""
    pass


class ActortestSkippedTestWarning(ActortestUserWarning):
    """A warning for when a test is skipped."""
    pass


class ActortestDeprecationWarning(ActortestUserWarning):
    """A warning for deprecated features."""
    pass
