# Generated by Django 4.1.3 on 2022-12-06 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='book title')),
                ('author', models.CharField(max_length=255, verbose_name='book author')),
                ('number_of_pages', models.IntegerField(verbose_name='number of pages')),
                ('pub_date', models.DateField(verbose_name=' date published')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='owner first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='owner last name')),
                ('address', models.CharField(max_length=100, verbose_name='owner address')),
                ('phone', models.CharField(max_length=15, verbose_name='phone number')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderBookByAuthor',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookstack.book')),
            ],
            options={
                'ordering': ['author'],
            },
            bases=('bookstack.book',),
        ),
        migrations.CreateModel(
            name='OrderdOwner',
            fields=[
                ('owner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookstack.owner')),
            ],
            options={
                'ordering': ['first_name'],
            },
            bases=('bookstack.owner',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='owner first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='owner last name')),
                ('address', models.CharField(max_length=100, verbose_name='owner address')),
                ('phone', models.CharField(max_length=15, verbose_name='phone number')),
                ('bio', models.TextField(max_length=1000)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookstack.owner', verbose_name='user profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstack.owner', verbose_name='owner of the book'),
        ),
        migrations.CreateModel(
            name='OrderdBook',
            fields=[
            ],
            options={
                'ordering': ['title'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('bookstack.book',),
        ),
    ]
