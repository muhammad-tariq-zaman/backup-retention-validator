import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import validate

def row(b, age):
    return {"backup": b, "age_days": str(age)}

class TestRetention(unittest.TestCase):
    def test_purge_due(self):
        self.assertEqual(validate([row("B1", 45)], 30)[0][2], "PURGE DUE")
    def test_kept(self):
        self.assertEqual(validate([row("B1", 10)], 30)[0][2], "KEPT")
    def test_boundary_kept(self):
        self.assertEqual(validate([row("B1", 30)], 30)[0][2], "KEPT")
    def test_oldest_first(self):
        r = validate([row("A", 5), row("B", 60)], 30)
        self.assertEqual(r[0][0], "B")
