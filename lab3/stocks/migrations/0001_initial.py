# Generated by Django 4.2.4 on 2023-10-15 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_create', models.DateField()),
                ('date_of_form', models.DateField()),
                ('date_of_finish', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.BinaryField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.status')),
            ],
        ),
        migrations.CreateModel(
            name='ExpApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.application')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.expertise')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.user'),
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.status'),
        ),
    ]
