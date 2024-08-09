from .models import User, UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


# receiver
@receiver(post_save,sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    if created:
        print("create the user profile ")
        UserProfile.objects.create(user=instance)
        print("User Profile Created")
    else:
        # delete the userprofile get error
        try:
            print("User Is Updated")
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            print("profile was not exist but created")


# post_save.connect(post_save_create_profile_receiver, sender=User)