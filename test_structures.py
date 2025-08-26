import unittest
import random
from queues import Queue
from stack import is_valid_parentheses

class TestQueueLab(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.customers = [f"Customer #{i}" for i in range(1, 21)]
        for customer in self.customers:
            self.queue.enqueue(customer)
        print(f"\n[Setup] Queue initialized with customers: {self.queue.items}")

    def test_enqueue_count(self):
        print("\n[Test] Enqueue count...")
        self.assertEqual(len(self.queue.items), 20)
        print("[Pass] Queue contains 20 customers")

    def test_peek(self):
        print("\n[Test] Peek...")
        front = self.queue.peek()
        print(f"[Peeked] Customer at front: {front}")
        self.assertEqual(front, "Customer #1")
        print("[Pass] Peek returns the correct customer")

    def test_select_and_announce_winner(self):
        print("\n[Test] Select and announce winner...")
        winner = self.queue.select_and_announce_winner()
        print(f"[Winner Selected] {winner}")
        self.assertIsInstance(winner, str)
        self.assertTrue(winner.startswith("Customer #"))
        self.assertNotIn(winner, self.queue.items)
        print(f"[Queue State] Remaining: {self.queue.items}")
        print("[Pass] Winner selected and queue dequeued properly")

class TestStackLab(unittest.TestCase):
    def test_valid(self):
        print("\n[Test] Valid parentheses strings...")
        cases = ["()", "{[()]}", "([]{})"]
        for s in cases:
            print(f"[Check] Testing: {s}")
            result = is_valid_parentheses(s)
            print(f"[Stack Check] Final result for {s}: {result}")
            self.assertTrue(result)
            print(f"[Pass] {s} is valid")

    def test_invalid(self):
        print("\n[Test] Invalid parentheses strings...")
        cases = ["(", "([)]", "(()"]
        for s in cases:
            print(f"[Check] Testing: {s}")
            result = is_valid_parentheses(s)
            print(f"[Stack Check] Final result for {s}: {result}")
            self.assertFalse(result)
            print(f"[Pass] {s} is invalid")

if __name__ == "__main__":
    unittest.main()
