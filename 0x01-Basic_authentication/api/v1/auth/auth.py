#!/usr/bin/env python3
""" This module Performs Basic Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to a basic authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires authentication """
        if not path or not excluded_paths:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        is_slashed = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not is_slashed:
            tmp_path += '/'

        for exc in excluded_paths:
            exc_len = len(exc)
            if exc_len == 0:
                continue

            if exc[exc_len - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:exc_len - 1]:
                    return False
        return True

    def authorization_header(self, request=None) -> str | None:
        """ Method that handles authorization header """
        if not request:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that checks the current user """
        return None
