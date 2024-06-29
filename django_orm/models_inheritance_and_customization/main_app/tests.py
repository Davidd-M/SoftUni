from django.test import TestCase

from django.test import TestCase

from main_app.models import UserProfile, Message


class MessageModelTestCase(TestCase):
    def setUp(self):
        self.user1 = UserProfile.objects.create(username='john_doe', email='john@example.com',
                                                bio='Hello, I am John Doe.')
        self.user2 = UserProfile.objects.create(username='jane_smith', email='jane@example.com',
                                                bio='Hi there, I am Jane Smith.')
        self.user3 = UserProfile.objects.create(username='alice', email='alice@example.com', bio='Hello, I am Alice.')

    def test_zero_reply_to_message(self):
        message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content="Hello, Jane! Could you please tell Alice that tomorrow we are going on vacation?"
        )

        reply_content = 'Hi John, sure! I will forward this message to her!'
        reply_message = message.reply_to_message(reply_content=reply_content)

        # Check if the reply message is created correctly
        self.assertEqual(Message.objects.count(), 2)
        self.assertEqual(reply_message.sender, self.user2)
        self.assertEqual(reply_message.receiver, self.user1)
        self.assertEqual(reply_message.content, reply_content)
