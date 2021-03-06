# Generated by Django 2.0.1 on 2018-01-31 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probId', models.CharField(max_length=30, verbose_name='Problem id for identification')),
                ('title', models.CharField(default='TODO', max_length=30, verbose_name='Problem Title will be crawlled later')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProblemInSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setName', models.CharField(max_length=200, unique=True, verbose_name='name of ProblemSet')),
                ('author', models.CharField(default='Unknown', max_length=30, verbose_name='author of this ProblemSet')),
                ('hasProblem', models.ManyToManyField(through='problem.ProblemInSet', to='problem.Problem')),
                ('setCreator', models.ForeignKey(default='root', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_AC', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
                ('realUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='probleminset',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.ProblemSet'),
        ),
        migrations.AddField(
            model_name='problem',
            name='RelProblem',
            field=models.ManyToManyField(through='problem.ProblemStatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problem',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.OnlineJudge'),
        ),
    ]
