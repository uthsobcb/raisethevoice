# Generated by Django 5.1 on 2024-08-16 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('feed', '0002_vote_delete_likepost'), ('feed', '0003_post_downvote_count_post_upvote_count_and_more'), ('feed', '0004_remove_comment_total_likes_remove_post_total_likes'), ('feed', '0005_alter_vote_type')]

    dependencies = [
        ('feed', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('up', 'Up'), ('down', 'Down')], max_length=10)),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='feed.post')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.AddField(
            model_name='post',
            name='downvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='feed.post'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'post')},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='total_likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='total_likes',
        ),
        migrations.AlterField(
            model_name='vote',
            name='type',
            field=models.IntegerField(choices=[(1, 'Upvote'), (-1, 'Downvote')], default=None, null=True),
        ),
    ]
