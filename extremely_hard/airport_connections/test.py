'''
You are given a list of airports (three-letter codes like 'JFK'), a list of routes (one-way flights 
from one airport to another like ['JFK', 'SFO']), and a starting airport. Write a function that 
returns the minimum number of airport connections (one-way flights) that need to be added in order 
for someone to be able to reach any airport in the list, starting at the starting airport. Note that 
the connections don't have to be direct; it's okay if an airport can only be reached from the starting 
airport by stopping at other airports first.
'''

import program
import unittest


AIRPORTS = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]

STARTING_AIRPORT = "LGA"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        routes = []
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 17
        )

    def test_case_2(self):
        routes = [["LGA", "DSM"], ["LGA", "ORD"], ["LGA", "EYW"]]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 14
        )

    def test_case_3(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["LGA", "EYW"],
            ["EYW", "JFK"],
            ["EYW", "EWR"],
            ["JFK", "ICN"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 11
        )

    def test_case_4(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["LGA", "EYW"],
            ["EYW", "JFK"],
            ["EYW", "EWR"],
            ["JFK", "ICN"],
            ["LGA", "ICN"],
            ["ICN", "ORD"],
            ["ICN", "EWR"],
            ["JFK", "DSM"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 11
        )

    def test_case_5(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["LGA", "EYW"],
            ["EYW", "JFK"],
            ["EYW", "EWR"],
            ["JFK", "ICN"],
            ["LGA", "ICN"],
            ["ICN", "ORD"],
            ["ICN", "EWR"],
            ["JFK", "DSM"],
            ["ICN", "JFK"],
            ["ORD", "DSM"],
            ["DSM", "LGA"],
            ["JFK", "LGA"],
            ["JFK", "HND"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 10
        )

    def test_case_6(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["LGA", "EYW"],
            ["EYW", "JFK"],
            ["EYW", "EWR"],
            ["JFK", "ICN"],
            ["LGA", "ICN"],
            ["ICN", "ORD"],
            ["ICN", "EWR"],
            ["JFK", "DSM"],
            ["ICN", "JFK"],
            ["ORD", "DSM"],
            ["DSM", "LGA"],
            ["JFK", "LGA"],
            ["JFK", "HND"],
            ["SFO", "SIN"],
            ["SFO", "CDG"],
            ["SFO", "LHR"],
            ["LHR", "DEL"],
            ["DEL", "BGI"],
            ["DEL", "DOH"],
            ["DOH", "SAN"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 3
        )

    def test_case_7(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["EYW", "JFK"],
            ["EYW", "EWR"],
            ["JFK", "ICN"],
            ["LGA", "ICN"],
            ["ICN", "ORD"],
            ["ICN", "EWR"],
            ["JFK", "DSM"],
            ["ICN", "JFK"],
            ["ORD", "DSM"],
            ["DSM", "LGA"],
            ["JFK", "LGA"],
            ["JFK", "HND"],
            ["SFO", "SIN"],
            ["SFO", "CDG"],
            ["SFO", "LHR"],
            ["LHR", "DEL"],
            ["DEL", "BGI"],
            ["DEL", "DOH"],
            ["DOH", "SAN"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 4
        )

    def test_case_8(self):
        routes = [
            ["LGA", "DSM"],
            ["SIN", "BGI"],
            ["SIN", "CDG"],
            ["SIN", "DEL"],
            ["SIN", "DOH"],
            ["SIN", "DSM"],
            ["SIN", "EWR"],
            ["SIN", "EYW"],
            ["SIN", "HND"],
            ["SIN", "ICN"],
            ["SIN", "JFK"],
            ["SIN", "LHR"],
            ["SIN", "ORD"],
            ["SFO", "SIN"],
            ["SFO", "SAN"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 3
        )

    def test_case_9(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["SIN", "BGI"],
            ["SIN", "CDG"],
            ["CDG", "DEL"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["DEL", "EWR"],
            ["HND", "ICN"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["JFK", "SFO"],
            ["EYW", "LHR"],
            ["SFO", "ORD"],
            ["SFO", "LGA"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 6
        )

    def test_case_10(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["SIN", "BGI"],
            ["SIN", "CDG"],
            ["CDG", "DEL"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["DEL", "EWR"],
            ["HND", "ICN"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["JFK", "SFO"],
            ["EYW", "LHR"],
            ["SFO", "ORD"],
            ["SFO", "LGA"],
            ["SFO", "SIN"],
            ["CDG", "EYW"],
            ["LGA", "SAN"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 3
        )

    def test_case_11(self):
        routes = [
            ["LGA", "DSM"],
            ["DSM", "ORD"],
            ["SIN", "BGI"],
            ["SIN", "CDG"],
            ["CDG", "DEL"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["DEL", "EWR"],
            ["HND", "ICN"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["JFK", "SFO"],
            ["EYW", "LHR"],
            ["SFO", "ORD"],
            ["SFO", "LGA"],
            ["SFO", "SIN"],
            ["CDG", "EYW"],
            ["ORD", "HND"],
            ["HND", "SAN"],
            ["LGA", "TLV"],
            ["LGA", "BUD"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 0
        )

    def test_case_12(self):
        routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "DEL"],
            ["DEL", "DOH"],
            ["DOH", "SIN"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SAN", "EYW"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 6
        )

    def test_case_13(self):
        routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "DEL"],
            ["DEL", "DOH"],
            ["DOH", "SIN"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "ORD"],
            ["SAN", "EYW"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 6
        )

    def test_case_14(self):
        routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "DEL"],
            ["DEL", "DOH"],
            ["DOH", "SIN"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "DSM"],
            ["SAN", "EYW"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 5
        )

    def test_case_15(self):
        routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "SIN"],
            ["CDG", "BUD"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["TLV", "DEL"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["HND", "JFK"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "DSM"],
            ["SAN", "EYW"],
        ]
        self.assertTrue(
            program.airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 3
        )


if __name__ == "__main__":
    unittest.main()
