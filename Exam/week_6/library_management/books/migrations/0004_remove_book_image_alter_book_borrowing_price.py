# Generated by Django 4.2.7 on 2023-12-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_post_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowing_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
