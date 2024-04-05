from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.s = RailwayStation("Sofia")

    def test_initialized_correctly(self):
        s = RailwayStation("Sofia")
        self.assertEqual(s.name, "Sofia")
        self.assertEqual(s.arrival_trains, deque())
        self.assertEqual(s.departure_trains, deque())

    def test_less_name_chars_raises(self):
        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("S")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("Sf")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("Sof")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.assertEqual(self.s.arrival_trains, deque())
        self.s.new_arrival_on_board('TEST')
        self.assertEqual(self.s.arrival_trains, deque(["TEST"]))

    def test_train_has_arrived_with_one_train(self):
        train_info = 'some info'

        self.assertEqual(self.s.arrival_trains, deque())
        self.assertEqual(self.s.departure_trains, deque())

        self.s.new_arrival_on_board(train_info)

        result = self.s.train_has_arrived(train_info)

        expected = f"{train_info} is on the platform and will leave in 5 minutes."

        self.assertEqual(result, expected)
        self.assertEqual(len(self.s.departure_trains), 1)
    def test_train_has_arrived_works(self):
        info = "burgas"
        self.assertEqual(self.s.arrival_trains, deque())
        self.assertEqual(self.s.departure_trains, deque())

        self.s.arrival_trains = deque(["sofia", "burgas"])
        result = self.s.train_has_arrived(info)
        self.assertEqual(result, f"There are other trains to arrive before {info}.")

    def test_train_has_left_success(self):
        info = "burgas"
        self.assertEqual(self.s.arrival_trains, deque())
        self.assertEqual(self.s.departure_trains, deque())

        self.s.departure_trains = deque(['burgas', 'sofia'])
        result = self.s.train_has_left(info)
        self.assertTrue(result)
        self.assertEqual(len(self.s.departure_trains), 1)

    def test_train_has_left_fail(self):
        info = "burgas"
        self.assertEqual(self.s.arrival_trains, deque())
        self.assertEqual(self.s.departure_trains, deque())

        self.s.departure_trains = deque(['sofia', 'burgas'])
        result = self.s.train_has_left(info)
        self.assertFalse(result)
        self.assertEqual(len(self.s.departure_trains), 2)


if __name__ == "__main__":
    main()
