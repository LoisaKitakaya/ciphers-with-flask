import unittest
from .ciphers import TranspositionCipher, CeaserCipher

class TestCiphers(unittest.TestCase):

    # test data
    def setUp(self) -> None:

        self.text_key = 15

        self.test_string = 'This is a test string'

        self.plaintext_upper = 'THE NEW PASSWORD IS SWORDFISH.'

        self.plaintext_lower = 'the new password is swordfish.'

        self.ceaser_upper_ciphertext = 'iWTCcTlCePhhldgSCXhChldgSUXhWG'

        self.ceaser_lower_ciphertext = '9wtC3t!C5p88!47sCx8C8!47sux8wG'

        self.transposition_lower_ciphertext = 'tdh ei sn esww opradsfsiwsohr.'

        self.transposition_upper_ciphertext = 'TDH EI SN ESWW OPRADSFSIWSOHR.'

    # test if object_instance is an instance of TranspositionCipher
    def test_transposition_object_init(self):

        object_instance = TranspositionCipher(self.test_string)

        self.assertIsInstance(object_instance, TranspositionCipher)

    # test the encryption of upper case text using transposition cipher
    def test_transposition_encrypt_upper(self):

        object_instance = TranspositionCipher(self.plaintext_upper)

        ciphertext = object_instance.encrypt_message(self.text_key)

        self.assertEqual(ciphertext, self.transposition_upper_ciphertext)

    # test the decryption of upper case text using transposition cipher
    def test_transposition_decrypt_upper(self):

        object_instance = TranspositionCipher(self.transposition_upper_ciphertext)

        plaintext = object_instance.decrypt_message(self.text_key)

        self.assertEqual(plaintext, self.plaintext_upper)

    # test the encryption of lower case text using transposition cipher
    def test_transposition_encrypt_lower(self):

        object_instance = TranspositionCipher(self.plaintext_lower)

        ciphertext = object_instance.encrypt_message(self.text_key)

        self.assertEqual(ciphertext, self.transposition_lower_ciphertext)

    # test the decryption of lower case text using transposition cipher
    def test_transposition_decrypt_lower(self):

        object_instance = TranspositionCipher(self.transposition_lower_ciphertext)

        plaintext = object_instance.decrypt_message(self.text_key)

        self.assertEqual(plaintext, self.plaintext_lower)

    # test if object_instance is an instance of CeaserCipher
    def test_ceaser_object_init(self):

        object_instance = CeaserCipher(self.test_string)

        self.assertIsInstance(object_instance, CeaserCipher)

    # test the encryption of upper case text using ceaser cipher
    def test_ceaser_encrypt_upper(self):

        object_instance = CeaserCipher(self.plaintext_upper)

        ciphertext = object_instance.encrypt_message(self.text_key)

        self.assertEqual(ciphertext, self.ceaser_upper_ciphertext)

    # test the decryption of upper case text using ceaser cipher
    def test_ceaser_decrypt_upper(self):

        object_instance = CeaserCipher(self.ceaser_upper_ciphertext)

        plaintext = object_instance.decrypt_message(self.text_key)

        self.assertEqual(plaintext, self.plaintext_upper)

    # test the encryption of lower case text using ceaser cipher
    def test_ceaser_encrypt_lower(self):

        object_instance = CeaserCipher(self.plaintext_lower)

        ciphertext = object_instance.encrypt_message(self.text_key)

        self.assertEqual(ciphertext, self.ceaser_lower_ciphertext)

    # test the decryption of lower case text using ceaser cipher
    def test_ceaser_decrypt_lower(self):

        object_instance = CeaserCipher(self.ceaser_lower_ciphertext)

        plaintext = object_instance.decrypt_message(self.text_key)

        self.assertEqual(plaintext, self.plaintext_lower)

# to be called by __init__.py when running 'python test.py'
def do_tests():

    unittest.main()
    
# to run tests when running 'python test.py'
if __name__ == '__main__':

    unittest.main()