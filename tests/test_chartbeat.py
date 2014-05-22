import unittest

from chartbeatpy import Chartbeat


class ChartbeatTest(unittest.TestCase):
    def setUp(self):
        self.beat = Chartbeat("317a25eccba186e0f6b558f45214c0e7", "avc.com")
        self.keys = [
            Chartbeat.READ, Chartbeat.WRITE, Chartbeat.IDLE
        ]

    def test_histogram(self):
        data = self.beat.histogram(keys=self.keys, breaks=[1, 5, 10])
        for key in self.keys:
            self.assertTrue(key in data)

    def test_path_summary(self):
        data = self.beat.path_summary(keys=self.keys, types=["n", "n", "s"])
        for path in data:
            for key in self.keys:
                self.assertTrue(key in data[path])

    def test_quickstats(self):
        data = self.beat.quickstats()
        self.assertTrue("visit" in data)

    def test_api_version(self):
        altbeat = Chartbeat("317a25eccba186e0f6b558f45214c0e7", "avc.com", api_version='3')
        data = altbeat.quickstats()
        self.assertTrue("visit" in data)

    def test_geo(self):
        data = self.beat.geo()
        self.assertTrue("lat_lngs" in data)

    def test_summary(self):
        data = self.beat.summary(keys=["read", "write", "idle"])
        self.assertTrue("read" in data)
        self.assertTrue("write" in data)
        self.assertTrue("idle" in data)

    def test_recent(self):
        data = self.beat.recent()
        self.assertIsInstance(data, list)

    def test_referrers(self):
        data = self.beat.referrers()
        self.assertTrue("referrers" in data)

    def test_top_pages(self):
        data = self.beat.top_pages()
        self.assertIsInstance(data, list)

    def test_engage_series(self):
        data = self.beat.engage_series()
        self.assertTrue("data" in data)

    def test_engage_stats(self):
        data = self.beat.engage_stats()
        self.assertTrue("data" in data)

    def test_social_series(self):
        data = self.beat.social_series()
        self.assertTrue("data" in data)

    def test_social_stats(self):
        data = self.beat.social_stats()
        self.assertTrue("data" in data)

    def test_traffic_series(self):
        data = self.beat.traffic_series()
        self.assertTrue("data" in data)

    def test_traffice_stats(self):
        data = self.beat.traffic_stats()
        self.assertTrue("data" in data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
