# Generated by Django 4.2.6 on 2023-11-06 19:55

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(blank=True, default='该用户暂未设置签名', max_length=500, null=True)),
                ('User_Type', models.CharField(choices=[('villager', '村庄'), ('young_adult', '年轻人'), ('college_student', '大学生'), ('research_team', '科研团队'), ('business', '企业')], max_length=20)),
                ('Gender_user', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=20)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/%Y/%m', verbose_name='用户头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户资料',
                'verbose_name_plural': '用户资料',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='分类名称')),
                ('desc_category', models.TextField(blank=True, default='', max_length=200, verbose_name='分类描述')),
            ],
            options={
                'verbose_name': '帖子分类',
                'verbose_name_plural': '帖子分类',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='标题')),
                ('desc_topic', models.TextField(blank=True, default='', verbose_name='文章描述')),
                ('content', models.TextField(blank=True, default='', max_length=20000, verbose_name='内容')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remarks', models.PositiveIntegerField(default=0, verbose_name='评论数量')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览数量')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_author', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_demo.category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '论坛帖子',
                'verbose_name_plural': '论坛帖子',
            },
        ),
        migrations.CreateModel(
            name='TopicComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TopicComment_Author', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_demo.topiccomment')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_demo.topic')),
            ],
            options={
                'verbose_name': '帖子评论',
                'verbose_name_plural': '帖子评论',
                'ordering': ('time',),
            },
        ),
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '私信',
                'verbose_name_plural': '私信',
                'ordering': ['-timestamp'],
            },
        ),
    ]
