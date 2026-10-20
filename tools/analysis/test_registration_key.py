"""Regression vectors, including the original-MSET accepted synthetic identity."""
import unittest
from registration_key import generate, checksum, normalized


class RegistrationKeyTests(unittest.TestCase):
    def test_original_mset_accepted_vector(self):
        self.assertEqual(checksum('MDIR64BITRESEARCH2026'), 64884)
        self.assertEqual(generate('MDIR64BIT RESEARCH', '2026'),
                         '2560-4080-8040-0119')

    def test_spaces_match_original_preprocessing(self):
        self.assertEqual(generate('MDIR64BIT RESEARCH', '20 26'),
                         generate('MDIR64BITRESEARCH', '2026'))

    def test_file_creation_gate_distinguishes_negative_control(self):
        def gate(serial):
            return (sum(map(int, serial.split('-'))) % 9645) % 1000 == 154
        self.assertTrue(gate('2560-4080-8040-0119'))
        self.assertFalse(gate('2560-4080-8040-0001'))

    def test_unsupported_inputs(self):
        for name in [' ', '\n', '\uD55C\uAE00']:
            with self.assertRaises(ValueError):
                generate(name, '2026')
        with self.assertRaises(ValueError):
            generate('A' * 256, '2026')


if __name__ == '__main__':
    unittest.main()
