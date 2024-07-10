# Generated by Django 5.0.6 on 2024-07-06 03:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetails",
            fields=[
                ("is_created", models.DateTimeField(auto_now_add=True)),
                ("is_updated", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("user_name", models.CharField(db_index=True, max_length=30)),
                (
                    "mobile_number",
                    models.CharField(
                        db_index=True,
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message='Mobile number must be in the format: "+91XXXXXXXXXX", where X is a digit and the number starts with 6, 7, 8, or 9.',
                                regex="^\\+91[6-9]\\d{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "email_id",
                    models.EmailField(
                        db_index=True,
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.EmailValidator(
                                message="Invalid email format"
                            )
                        ],
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Password must contain at least 8 characters, including at least one digit, one lowercase letter, and one uppercase letter.",
                                regex="^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$",
                            )
                        ],
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        validators=[
                            django.core.validators.RegexValidator(
                                message='Date of birth must be in the format: "YYYY-MM-DD".',
                                regex="^\\d{4}-\\d{2}-\\d{2}$",
                            )
                        ]
                    ),
                ),
                ("is_mobile_verified", models.BooleanField(default=False)),
                ("is_email_verified", models.BooleanField(default=False)),
                ("last_login", models.DateTimeField(auto_now_add=True)),
                ("unsuccessfull_attempts", models.IntegerField(default=0)),
                ("is_blocked", models.BooleanField(default=False)),
                ("block_expiration", models.DateTimeField(blank=True, null=True)),
                ("recaptcha_attempts", models.IntegerField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]