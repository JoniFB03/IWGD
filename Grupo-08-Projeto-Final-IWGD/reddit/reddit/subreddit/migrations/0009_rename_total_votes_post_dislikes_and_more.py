# Generated by Django 4.2.6 on 2023-10-12 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("subreddit", "0008_post_upvotes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="total_votes",
            new_name="dislikes",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="upvotes",
            new_name="likes",
        ),
    ]
