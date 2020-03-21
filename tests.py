import unittest
import keygen
import chaos
import transform
import numpy as np

class Test_keygen(unittest.TestCase):

    def test_sum_frequencies(self):
        matrix = np.array([
            [6, 2, 0.39, 4, 1.235],
            [4, 7.85, 0.12, 3, 9],
            [3, 2, 9, 7, 4]
        ])
        actual = keygen.sum_frequencies(matrix)
        expected = 62.595
        self.assertAlmostEqual(expected, actual, delta=0.00001)

    def test_control_param(self):
        actual = keygen.control_parameter(9.85, 3, 0.75)
        expected = 0.4625
        self.assertAlmostEqual(first=expected, second=actual, delta=0.00001)

    def test_iterations(self):
        actual = keygen.iterations(21.5)
        expected = (21.5 % 3.1) + 2
        self.assertAlmostEqual(expected, actual, delta=0.00001)

    def test_initial_state(self):
        T = 0.4625
        x0 = 0.75
        i = 3
        actual = keygen.initial_state(T, x0, i)
        expected = (T + x0 * i) % 1
        self.assertAlmostEqual(expected, actual, delta=0.000001)

    def test_initial_state_r(self):
        T = 0.4625
        r = 1.13
        i = 3
        actual = keygen.initial_state_r(T, r, i)
        expected = (T * i * r) % 0.09 + 1.11
        self.assertAlmostEqual(expected, actual, delta=0.000001)

    def test_get_fractional(self):
        number = 5.8125
        actual = keygen.get_fractional(number)
        self.assertEqual(0.8125, actual)

    def test_fractional_to_binary(self):
        actual = keygen.fractional_to_binary(0.8125, 8)
        expected = np.array([1, 1, 0, 1, 0, 0, 0, 0])
        self.assertTrue(np.array_equal(expected, actual))

    def test_key_partition(self):
        x0 = 0.1
        x_binary = keygen.fractional_to_binary(keygen.get_fractional(x0), 52)
        actual = keygen.sum_and_divide(x_binary, 2^52)

    def test_initial_states(self):
        x0 = 22.6666
        T = 3
        R = 3
        actual = keygen.initial_states(T, x0, R)
        expected = np.array([0.6666, 0.3332, 0.9998])
        self.assertTrue(np.allclose(expected, actual))

    def test_initial_states_r(self):
        r = 22.6666
        T = 3
        R = 3
        actual = keygen.initial_states_r(T, r, R)
        expected = np.array([1.1598, 1.1196, 1.1694])
        self.assertTrue(np.allclose(expected, actual))


    def test_key_from_partitions(self):
        x0 = np.empty([52], dtype=np.uint8)
        x0[5] = 21
        y0 = np.empty([52], dtype=np.uint8)
        y0[27] = 3
        r = np.empty([52], dtype=np.uint8)
        r[34] = 9
        T = np.empty([52], dtype=np.uint8)
        T[2] = 64
        R = np.empty([48], dtype=np.uint8)
        R[8] = 50
        expected = np.concatenate((x0, y0, r, T, R), axis=0)
        actual = keygen.key_from_partitions(x0, y0, r, T, R)
        self.assertTrue(np.array_equal(expected, actual))

    def test_log_map_sequences(self):
        x0 = .65
        y0 = .75
        r = 1.12
        m = 3
        n = 3
        expected = np.array([
            [0.8281, 0.4557376, 1.0444467],
            [0.6195, 0.9198765, 0.19540909]
        ])
        actual = chaos.log_map_sequences(r, x0, y0, 3)
        self.assertTrue(np.allclose(expected, actual))

    def test_sequence_to_int(self):
        seq = np.array([.5, 1.3, 33, 34])
        max = 33
        expected = np.array([0, 1, 33, 0])
        actual = chaos.sequence_to_int(seq, max)
        self.assertTrue(np.array_equal(expected, actual))

    def test_swap_rows(self):
        matrix = np.array([
            [1, 1],
            [2, 2],
            [3, 3]
        ])
        destinations = np.array([2, 0, 1])
        expected = np.array([
            [2, 2],
            [1, 1],
            [3, 3]
        ])
        actual = transform.swap_rows(matrix, destinations)
        self.assertTrue(np.array_equal(expected, actual))

    def test_swap_columns(self):
        matrix = np.array([
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ])
        expected = np.array([
            [2, 3, 1],
            [2, 3, 1],
            [2, 3, 1]
        ])
        destinations = np.array([1, 2])
        actual = transform.swap_columns(matrix, destinations)
        self.assertTrue(np.array_equal(expected, actual))

if __name__ == "__main__":
    unittest.main()
