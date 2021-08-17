'''
Imagine that you want to schedule a meeting of a certain duration with a coworker. You have access to 
your calendar and your coworker's calendar (both of which contain your respective meetings for the 
day, in the form of [startTime, endTime]), as well as both of your daily bounds (i.e., the earliest 
and latest times at which you're available for meetings every day, in the form of 
[earliestTime, latestTime]). Write a function that takes in your calendar, your daily bounds, your 
coworker's calendar, your coworker's daily bounds, and the duration of the meeting that you want to 
schedule, and that returns a list of all the time blocks (in the form of [startTime, endTime]) 
during which you could schedule the meeting. Note that times will be given and should be returned 
in military time (example times: '8:30', '9:01', '23:56').
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:00", "20:00"]
        calendar2 = [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"],
        ]
        dailyBounds2 = ["10:00", "18:30"]
        meetingDuration = 30
        expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_2(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:00", "20:00"]
        calendar2 = [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"],
        ]
        dailyBounds2 = ["10:00", "18:30"]
        meetingDuration = 45
        expected = [["15:00", "16:00"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_3(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["8:00", "20:00"]
        calendar2 = [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"],
        ]
        dailyBounds2 = ["7:00", "18:30"]
        meetingDuration = 45
        expected = [["8:00", "9:00"], ["15:00", "16:00"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_4(self):
        calendar1 = [
            ["8:00", "10:30"],
            ["11:30", "13:00"],
            ["14:00", "16:00"],
            ["16:00", "18:00"],
        ]
        dailyBounds1 = ["8:00", "18:00"]
        calendar2 = [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"],
        ]
        dailyBounds2 = ["7:00", "18:30"]
        meetingDuration = 15
        expected = []
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_5(self):
        calendar1 = [
            ["10:00", "10:30"],
            ["10:45", "11:15"],
            ["11:30", "13:00"],
            ["14:15", "16:00"],
            ["16:00", "18:00"],
        ]
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = [
            ["10:00", "11:00"],
            ["12:30", "13:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"],
        ]
        dailyBounds2 = ["9:00", "18:30"]
        meetingDuration = 15
        expected = [
            ["9:30", "10:00"],
            ["11:15", "11:30"],
            ["13:30", "14:15"],
            ["18:00", "18:30"],
        ]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_6(self):
        calendar1 = [
            ["10:00", "10:30"],
            ["10:45", "11:15"],
            ["11:30", "13:00"],
            ["14:15", "16:00"],
            ["16:00", "18:00"],
        ]
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = [["10:00", "11:00"], ["10:30", "20:30"]]
        dailyBounds2 = ["9:00", "22:30"]
        meetingDuration = 60
        expected = []
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_7(self):
        calendar1 = [
            ["10:00", "10:30"],
            ["10:45", "11:15"],
            ["11:30", "13:00"],
            ["14:15", "16:00"],
            ["16:00", "18:00"],
        ]
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = [["10:00", "11:00"], ["10:30", "16:30"]]
        dailyBounds2 = ["9:00", "22:30"]
        meetingDuration = 60
        expected = [["18:00", "20:00"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_8(self):
        calendar1 = []
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = []
        dailyBounds2 = ["9:00", "16:30"]
        meetingDuration = 60
        expected = [["9:30", "16:30"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_9(self):
        calendar1 = []
        dailyBounds1 = ["9:00", "16:30"]
        calendar2 = []
        dailyBounds2 = ["9:30", "20:00"]
        meetingDuration = 60
        expected = [["9:30", "16:30"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_10(self):
        calendar1 = []
        dailyBounds1 = ["9:30", "16:30"]
        calendar2 = []
        dailyBounds2 = ["9:30", "16:30"]
        meetingDuration = 60
        expected = [["9:30", "16:30"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)

    def test_case_11(self):
        calendar1 = [
            ["7:00", "7:45"],
            ["8:15", "8:30"],
            ["9:00", "10:30"],
            ["12:00", "14:00"],
            ["14:00", "15:00"],
            ["15:15", "15:30"],
            ["16:30", "18:30"],
            ["20:00", "21:00"],
        ]
        dailyBounds1 = ["6:30", "22:00"]
        calendar2 = [
            ["9:00", "10:00"],
            ["11:15", "11:30"],
            ["11:45", "17:00"],
            ["17:30", "19:00"],
            ["20:00", "22:15"],
        ]
        dailyBounds2 = ["8:00", "22:30"]
        meetingDuration = 30
        expected = [["8:30", "9:00"], ["10:30", "11:15"], ["19:00", "20:00"]]
        result = program.calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
