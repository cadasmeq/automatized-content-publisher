import unittest

from publisher.publish.factory import (
    PostFactory,
)


class ValueObjectTesting(unittest.TestCase):

    def test_post(self):
        msg = "Hola! Este es un nuevo Post!"

        message = Message(msg)
        self.assertEqual(message.msg, msg)


if __name__ == '__main__':
    unittest.main()