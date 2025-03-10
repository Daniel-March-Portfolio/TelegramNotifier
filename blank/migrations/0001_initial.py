# Generated by Django 5.2b1 on 2025-03-02 22:19

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telegram', '0001_initial'),
        ('template', '0002_alter_template_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blank',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=64, unique=True)),
                ('_chat_id', models.CharField(db_column='chat_id', max_length=64, validators=[django.core.validators.RegexValidator('^\\d+$')])),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegrambot')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.template')),
            ],
        ),
        migrations.CreateModel(
            name='BlankVariable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('_value', models.CharField(db_column='value', max_length=255)),
                ('type', models.CharField(choices=[('string', 'String'), ('integer', 'Integer'), ('float', 'Float'), ('boolean', 'Boolean'), ('uuid', 'UUID')], max_length=16)),
                ('blank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='blank.blank')),
            ],
        ),
        migrations.AddIndex(
            model_name='blank',
            index=models.Index(fields=['tag'], name='blank_blank_tag_9a98f2_idx'),
        ),
        migrations.AddIndex(
            model_name='blankvariable',
            index=models.Index(fields=['blank'], name='blank_blank_blank_i_b4eb32_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='blankvariable',
            unique_together={('blank', 'key')},
        ),
    ]
