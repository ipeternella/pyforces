import unittest

from challenges.realm.hackerrank.fraudulent_activity_notifications import activityNotifications


class FraudulentActivityTests(unittest.TestCase):
    def test_should_compute_notifications(self):
        # arrange
        d = 5
        expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

        # act
        notifications = activityNotifications(expenditure, d)

        # assert
        self.assertEqual(notifications, 2)

    def test_should_compute_notifications_smaller(self):
        # arrange
        d = 2
        expenditure = [2, 3, 4, 2, 6]

        # act
        notifications = activityNotifications(expenditure, d)

        # assert
        self.assertEqual(notifications, 1)
