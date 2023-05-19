# Generated by Django 4.2 on 2023-05-16 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCountViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(db_index=True, max_length=150)),
                ('article', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_site.article')),
            ],
        ),
    ]
