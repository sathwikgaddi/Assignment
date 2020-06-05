# main/management/commands/populateUsers.py

import datetime
import random

    
from django.core.management.base import BaseCommand

from django_populate import Faker

from main.models import User
from main.models import Activity_peroid

class Command(BaseCommand):
    help = "Save randomly generated user record values."

    

    def handle(self, *args, **options):
            
            populator = Faker.getPopulator()
            populator.addEntity(User,5)
            populator.addEntity(Activity_peroid,10)
            insertedPks = populator.execute()
            populator.execute()
            self.stdout.write(self.style.SUCCESS('Users records saved successfully.'))
    
    