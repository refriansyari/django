import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        # create fake data for that entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create new user entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating databse.. please wait!")
    populate(20)
    print("Populating complete!")
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

# import django
# django.setup()

# import random
# from first_app.models import AccessRecord, Webpage, Topic
# from faker import Faker

# fakegen = Faker()
# topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t


# def populate(N=5):
#     for entry in range(N):
#         # get topic for the entry
#         top = add_topic()

#         # create fake data for that entry
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()

#         # Create new webpage entry
#         webpg = Webpage.objects.get_or_create(
#             topic=top, url=fake_url, name=fake_name)[0]

#         # Create a fake access record for that webpage
#         acc_rec = AccessRecord.objects.get_or_create(
#             name=webpg, date=fake_date)[0]


# if __name__ == '__main__':
#     print("Populating script!")
#     populate(20)
#     print("Populating complete!")
