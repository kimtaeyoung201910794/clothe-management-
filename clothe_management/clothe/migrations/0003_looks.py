# Generated by Django 4.1 on 2022-08-16 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothe', '0002_alter_clothe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='looks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ACC1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ACC1', to='clothe.clothe')),
                ('ACC2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ACC2', to='clothe.clothe')),
                ('bottom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bottom', to='clothe.clothe')),
                ('shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='clothe.clothe')),
                ('top', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top', to='clothe.clothe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
