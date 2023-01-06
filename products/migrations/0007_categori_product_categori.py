# Generated by Django 4.1.4 on 2022-12-27 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_review_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categori'),
        ),
    ]
