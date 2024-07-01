#!/usr/bin/env python3
"""test_utils.py
   This module contains the test cases for the utils module
"""
from parameterized import parameterized
import requests
from typing import Any, Dict, List, Tuple, Union
from unittest import TestCase, main, mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """
        Test the access_nested_map method
        Methods:
            test_access_nested_map - test the access_nested_map method, which
            returns the value of a nested map given a list of keys to traverse
            the map
            test_access_nested_map_exception - test the access_nested_map
            method when a key is not found in the nested map
    """
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: List[str], expected: Union[Dict[str, Any],
                                                                int]) -> None:
        """
            Test the access_nested_map method
            Args:
                nested_map: a nested map
                path: a list of keys to traverse the nested map
                expected: the expected value of the nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a'], KeyError),
        ({'a': 1}, ['a', 'b'], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                                         path: List[str],
                                         expected: Any) -> None:
        """
            Test the access_nested_map method
            Args:
                nested_map: a nested map with no key
                path: a list of keys to traverse the nested map
                expected: the expected exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Test the get_json method
        Methods:
            test_get_json - test the get_json method, which returns the
            payload of a request
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """test_get_json method
            to test that utils.get_json returns the expected result.
            Args:
                test_url: a url
                test_payload: a payload
        """
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        with mock.patch.object(requests, 'get',
                               return_value=mock_response) as mock_method:
            test_response = get_json(test_url)
            self.assertEqual(test_response, test_payload)

        mock_method.assert_called_once()


class TestMemoize(TestCase):
    """
    This class tests the wrapper method memoize from the module utils

    Methods:
    test_memoize: tests the method and checks if it behaves properly
    """
    def test_memoize(self) -> None:
        """
        This method tests memoize wrapper using a mock object to track
        the number of calls and a class to see if memoize does work as
        expected
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, "a_method",
                               return_value=42) as mock_a:
            obj = TestClass()
            obj.a_property
            obj.a_property
            mock_a.assert_called_once()


if __name__ == '__main__':
    main()
