# Generated by Django 2.2.7 on 2019-11-26 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('adult', models.BooleanField(null=True)),
                ('backdrop_path', models.CharField(max_length=140, null=True)),
                ('budget', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=140, null=True)),
                ('release_date', models.DateField()),
                ('revenue', models.IntegerField()),
                ('runtime', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=40)),
                ('tagline', models.TextField(null=True)),
                ('title', models.CharField(max_length=30)),
                ('video', models.BooleanField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genres', models.ManyToManyField(blank=True, related_name='genre_movies', to='movies.Genre')),
                ('like_user', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=10)),
                ('profile_path', models.CharField(max_length=140, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('key', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('file_path', models.CharField(max_length=140, primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(blank=True, to='movies.People'),
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('credit_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('character', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.People')),
            ],
        ),
    ]
