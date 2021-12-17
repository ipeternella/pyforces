import unittest

from parameterized import parameterized

from challenges.realm.hackerrank.encryption import encryption


class EncryptionTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("feed the dog", "fto ehg ee dd"),
            ("have a nice day", "hae and via ecy"),
        ]
    )
    def test_should_cipher_string(self, s, expected_cipher):
        # act
        cipher = encryption(s)

        # assert
        self.assertEqual(cipher, expected_cipher)
