# Generated by Django 3.0.8 on 2020-09-23 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_auto_20200919_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='supporter',
        ),
        migrations.AddField(
            model_name='pledge',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='owner_pledges', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
