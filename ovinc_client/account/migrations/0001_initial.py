# pylint: disable=C0301,C0103

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models

import ovinc_client.account.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("is_deleted", models.BooleanField(db_index=True, default=False, verbose_name="Soft Delete")),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "already in use"},
                        max_length=32,
                        primary_key=True,
                        serialize=False,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("nick_name", models.CharField(blank=True, max_length=32, null=True, verbose_name="Nick Name")),
                (
                    "user_type",
                    models.CharField(
                        choices=[("personal", "Personal"), ("platform", "Platform")],
                        default="personal",
                        max_length=32,
                        verbose_name="User Type",
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")),
                ("is_staff", models.BooleanField(default=False, verbose_name="Is Staff")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "User",
                "ordering": ["username"],
            },
            managers=[
                ("objects", ovinc_client.account.models.UserManager()),
                ("_objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
