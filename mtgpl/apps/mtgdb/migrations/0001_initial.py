# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='first name')),
                ('last_name', models.CharField(max_length=20, verbose_name='last name')),
                ('mtgjson_id', models.CharField(db_index=True, max_length=100, verbose_name='mtgjson id')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('mana_cost', models.CharField(max_length=100, verbose_name='mana cost')),
                ('cmc', models.PositiveSmallIntegerField(default=0, verbose_name='cmc')),
                ('text', models.TextField(verbose_name='text')),
                ('power', models.CharField(blank=True, db_index=True, max_length=5, verbose_name='power')),
                ('toughness', models.CharField(blank=True, db_index=True, max_length=5, verbose_name='toughness')),
                ('loyalty', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True, verbose_name='loyalty')),
                ('hand_mod', models.SmallIntegerField(blank=True, null=True, verbose_name='hand modifier')),
                ('life_mod', models.SmallIntegerField(blank=True, null=True, verbose_name='life modifier')),
                ('reserved', models.BooleanField(default=False, help_text='Set to true if this card is reserved by Wizards Official Reprint Policy', verbose_name='reserved')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='CardColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('white', 'White'), ('blue', 'Blue'), ('black', 'Black'), ('red', 'Red'), ('green', 'Green')], db_index=True, max_length=5, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='CardSubtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='CardSupertype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='code')),
                ('symbol', models.ImageField(upload_to='', verbose_name='symbol')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='release date')),
                ('mkm_id', models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='mkm id')),
                ('online_only', models.BooleanField(default=False, verbose_name='online only')),
                ('gatherer_code', models.CharField(max_length=10, unique=True, verbose_name='gatherer code')),
                ('mci_code', models.CharField(max_length=10, verbose_name='magiccards.info code')),
                ('exp_type', models.CharField(blank=True, max_length=16, verbose_name='type')),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mtgdb.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Legality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('r', 'Restricted'), ('b', 'Banned'), ('c', 'Conditional'), ('l', 'Legal')], max_length=1, verbose_name='status')),
                ('condition', models.TextField(blank=True, verbose_name='condition')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legality_statuses', to='mtgdb.Card', verbose_name='card')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtgdb.Format', verbose_name='format')),
            ],
        ),
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, db_index=True, max_length=5, verbose_name='number')),
                ('flavor', models.TextField(blank=True, verbose_name='flavor')),
                ('starter', models.BooleanField(default=False, help_text='Set to true if this card was only released as part of a core box set. These are technically part of the core sets and are tournament legal despite not being available in boosters.', verbose_name='starter')),
                ('multiverese_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='multiverse id')),
                ('timeshifted', models.BooleanField(default=False, verbose_name='timeshifted')),
                ('source', models.CharField(blank=True, max_length=128, verbose_name='source')),
                ('border', models.CharField(blank=True, choices=[('b', 'Black'), ('w', 'White'), ('s', 'Silver'), ('g', 'Gold')], max_length=1, verbose_name='border')),
                ('layout', models.CharField(blank=True, max_length=60, verbose_name='layout')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='painted_cards', to='mtgdb.Artist', verbose_name='artist')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtgdb.Card', verbose_name='card')),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtgdb.Expansion', verbose_name='expansion')),
                ('extra_artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='painted_as_extra', to='mtgdb.Artist', verbose_name='extra artist')),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='printing',
            name='rarity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mtgdb.Rarity', verbose_name='rarity'),
        ),
        migrations.AddField(
            model_name='card',
            name='colors',
            field=models.ManyToManyField(to='mtgdb.CardColor', verbose_name='colors'),
        ),
        migrations.AddField(
            model_name='card',
            name='front_side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_sides', to='mtgdb.Card', verbose_name='front side'),
        ),
        migrations.AddField(
            model_name='card',
            name='legality',
            field=models.ManyToManyField(help_text='This field lists all formats that the card *could* be legal in along with its actual legality in that format.', through='mtgdb.Legality', to='mtgdb.Format'),
        ),
        migrations.AddField(
            model_name='card',
            name='subtypes',
            field=models.ManyToManyField(to='mtgdb.CardSubtype', verbose_name='subtypes'),
        ),
        migrations.AddField(
            model_name='card',
            name='supertypes',
            field=models.ManyToManyField(to='mtgdb.CardSupertype', verbose_name='supertypes'),
        ),
        migrations.AddField(
            model_name='card',
            name='types',
            field=models.ManyToManyField(to='mtgdb.CardType', verbose_name='types'),
        ),
    ]