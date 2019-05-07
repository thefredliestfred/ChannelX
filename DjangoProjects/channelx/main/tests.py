from django.test import TestCase
from main.models import Channel, Ticket, Messages, ChannelMembers
from django.contrib.auth.models import User
from datetime import date, datetime
from django.contrib.auth import get_user_model
from django.http import HttpRequest


# Create your tests here.
class ChannelTest(TestCase):

    def create_channel(self, room_name='testing', slug='testing'):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')

        channel =  Channel.objects.create(room_name=room_name, start_life=date().today(),
        expire_date=date().today(), start_quiet_hour=datetime.now().time(),
        end_quiet_hour=datetime.now().time(), room_owner=user, slug=room_name)

        self.assertEqual(channel.room_name, 'testing')
        self.assertEqual(channel.slug, 'testing')
        self.assertEqual(channel.room_name, channel.slug)

class UserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='password')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

class SuperUserTest(TestCase):

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class MessageTest(TestCase):

    def test_create_message(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='password')
        
        channel =  Channel.objects.create(room_name='testroom', start_life=date().today(),
        expire_date=date().today(), start_quiet_hour=datetime.now().time(),
        end_quiet_hour=datetime.now().time(), room_owner=user, slug='testroom')

        message = Message.objects.create(room=channel, user=user, date=datetime.now.time, 
        text='this is a message')

        self.assertEqual(message.room, channel)
        self.assertEqual(message.user, user)
        self.assertEqual(message.text, 'this is a message')

class TicketTest(TestCase):

    def test_create_ticket(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='password')

        ticket = Ticket.objects.create(issue='this is an issue', 
        problem_details='allow me to tell you about my woes', date_posted=date().today(), author=user)

        self.assertEqual(ticket.issue, 'this is an issue')
        self.assertEqual(ticket.problem_details, 'allow me to tell you about my woes')

class PageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

class ChannelMembersTest(TestCase):

    def test_channel_members(self):
        member = ChannelMembers.objects.create(channel_id=400, member_id=400)

        self.assertEqual(member.channel_id, 400)
        self.assertEqual(member.member_id, 400)

class QuietHoursTest(TestCase):

    def test_hours(self):
        testnow = (3, 10, 2, 405500)
        test_start = (2, 10, 2, 405500)
        test_end = (4, 10, 2, 405500)

        self.assertTrue(test_start <= testnow < test_end)
