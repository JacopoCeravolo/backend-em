# Generated by Django 4.2 on 2024-08-15 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_investor_user_alter_startup_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='company_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='exit_strategy',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='impact_value',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='investor_expertise',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='investor_offering',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='investor_value',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='market',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='sdg',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='team_motives',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='team_values',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='type_of_business',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='type_of_investment',
        ),
        migrations.CreateModel(
            name='InvestorPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_market', models.TextField()),
                ('languages', models.JSONField()),
                ('funding_stage', models.JSONField()),
                ('investment_instrument', models.JSONField()),
                ('exit_strategy', models.JSONField()),
                ('qualities', models.JSONField()),
                ('expertise', models.JSONField()),
                ('team_values', models.TextField()),
                ('impact_level', models.PositiveIntegerField()),
                ('target_group', models.JSONField()),
                ('investor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences_section', to='api.investor')),
            ],
        ),
        migrations.CreateModel(
            name='InvestorPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previously_invested', models.JSONField()),
                ('investor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_section', to='api.investor')),
            ],
        ),
        migrations.AddField(
            model_name='investor',
            name='portfolio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor_porfolio', to='api.investorportfolio'),
        ),
        migrations.AddField(
            model_name='investor',
            name='preferences',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor_preferences', to='api.investorpreferences'),
        ),
    ]
