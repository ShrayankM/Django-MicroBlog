# Generated by Django 3.1.1 on 2020-09-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
