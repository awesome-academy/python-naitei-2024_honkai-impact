# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
#This is auto-generated class from django inspectdb, please ignore it

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
#This is auto-generated class from django inspectdb, please ignore it

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
#This is auto-generated class from django inspectdb, please ignore it

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
#This is auto-generated class from django inspectdb, please ignore it

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
#This is auto-generated class from django inspectdb, please ignore it

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
#This is auto-generated class from django inspectdb, please ignore it

class Battlesuit(models.Model):
    valkyrie = models.ForeignKey('Valkyrie', models.DO_NOTHING, db_column='Valkyrie_ID', blank=True, null=True)  # Field name made lowercase.
    battlesuit_id = models.IntegerField(db_column='BattleSuit_ID', primary_key=True)  # Field name made lowercase.
    battlesuit_name = models.CharField(db_column='BattleSuit_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valkyrie_name = models.CharField(db_column='Valkyrie_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weapon_type = models.ForeignKey('WeaponType', models.DO_NOTHING, db_column='Weapon_type_ID', blank=True, null=True)  # Field name made lowercase.
    dmg_type = models.ForeignKey('DmgType', models.DO_NOTHING, db_column='DMG_type_ID', blank=True, null=True)  # Field name made lowercase.
    element = models.ForeignKey('Elements', models.DO_NOTHING, db_column='Element_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'battlesuit'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
#This is auto-generated class from django inspectdb, please ignore it

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
#This is auto-generated class from django inspectdb, please ignore it

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
#This is auto-generated class from django inspectdb, please ignore it

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
#This is auto-generated class from django inspectdb, please ignore it

class DmgType(models.Model):
    dmg_type_id = models.IntegerField(db_column='DMG_type_ID', primary_key=True)  # Field name made lowercase.
    dmg_type_name = models.CharField(db_column='DMG_type_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmg_type'


class Elements(models.Model):
    element_id = models.IntegerField(db_column='Element_ID', primary_key=True)  # Field name made lowercase.
    elements_name = models.CharField(db_column='Elements_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elements'


class Event(models.Model):
    event_id = models.IntegerField(db_column='Event_ID', primary_key=True)  # Field name made lowercase.
    event_name = models.CharField(db_column='Event_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event'


class Eventbattlesuit(models.Model):
    event_character_id = models.IntegerField(db_column='Event_Character_ID', primary_key=True)  # Field name made lowercase.
    event = models.ForeignKey(Event, models.DO_NOTHING, db_column='Event_ID', blank=True, null=True)  # Field name made lowercase.
    battlesuit = models.ForeignKey(Battlesuit, models.DO_NOTHING, db_column='BattleSuit_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventbattlesuit'


class Position(models.Model):
    position_id = models.IntegerField(db_column='Position_ID', primary_key=True)  # Field name made lowercase.
    position_name = models.CharField(db_column='Position_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'position'


class Skill(models.Model):
    battlesuit = models.ForeignKey(Battlesuit, models.DO_NOTHING, db_column='BattleSuit_ID', blank=True, null=True)  # Field name made lowercase.
    skill_id = models.IntegerField(db_column='Skill_ID', primary_key=True)  # Field name made lowercase.
    skill_type = models.ForeignKey('Skilltype', models.DO_NOTHING, db_column='Skill_type_ID', blank=True, null=True)  # Field name made lowercase.
    skill_name = models.CharField(db_column='Skill_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skill'


class Skilltype(models.Model):
    skill_type_id = models.IntegerField(db_column='Skill_type_ID', primary_key=True)  # Field name made lowercase.
    skill_type_name = models.CharField(db_column='Skill_type_name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skilltype'


class Skin(models.Model):
    skin_id = models.IntegerField(db_column='Skin_ID', primary_key=True)  # Field name made lowercase.
    battlesuit = models.ForeignKey(Battlesuit, models.DO_NOTHING, db_column='BattleSuit_ID', blank=True, null=True)  # Field name made lowercase.
    skin_name = models.CharField(db_column='Skin_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skin'


class Stigmata(models.Model):
    stigmata_id = models.IntegerField(db_column='Stigmata_ID', primary_key=True)  # Field name made lowercase.
    set = models.ForeignKey('Stigmataset', models.DO_NOTHING, db_column='Set_ID', blank=True, null=True)  # Field name made lowercase.
    position = models.ForeignKey(Position, models.DO_NOTHING, db_column='Position_ID', blank=True, null=True)  # Field name made lowercase.
    stigmata_name = models.CharField(db_column='Stigmata_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stigmata'


class Stigmatarank(models.Model):
    rank_id = models.IntegerField(db_column='Rank_ID', primary_key=True)  # Field name made lowercase.
    stigmata = models.ForeignKey(Stigmata, models.DO_NOTHING, db_column='Stigmata_ID', blank=True, null=True)  # Field name made lowercase.
    rank_name = models.CharField(db_column='Rank_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    atk = models.IntegerField(db_column='ATK', blank=True, null=True)  # Field name made lowercase.
    def_field = models.IntegerField(db_column='DEF', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    crit = models.IntegerField(db_column='CRIT', blank=True, null=True)  # Field name made lowercase.
    sp = models.IntegerField(db_column='SP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stigmatarank'


class Stigmataset(models.Model):
    set_id = models.IntegerField(db_column='Set_ID', primary_key=True)  # Field name made lowercase.
    set_name = models.CharField(db_column='Set_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    set_eff_name = models.CharField(db_column='Set_Eff_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    two_pieces_eff_name = models.CharField(max_length=255, blank=True, null=True)
    two_pieces_eff = models.CharField(max_length=255, blank=True, null=True)
    three_pieces_eff_name = models.CharField(max_length=255, blank=True, null=True)
    two_piece_eff = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stigmataset'


class SubSkillRankEffect(models.Model):
    subskill_rank_effect_id = models.IntegerField(db_column='SubSkill_Rank_Effect_ID', primary_key=True)  # Field name made lowercase.
    subskil_lid = models.ForeignKey('Subskill', models.DO_NOTHING, db_column='SubSkil_lID', blank=True, null=True)  # Field name made lowercase.
    rank = models.ForeignKey('SuitStats', models.DO_NOTHING, db_column='Rank_ID', blank=True, null=True)  # Field name made lowercase.
    damage = models.IntegerField(db_column='Damage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_skill_rank_effect'


class Subskill(models.Model):
    subskill_id = models.IntegerField(db_column='SubSkill_ID', primary_key=True)  # Field name made lowercase.
    skill = models.ForeignKey(Skill, models.DO_NOTHING, db_column='Skill_ID', blank=True, null=True)  # Field name made lowercase.
    subskill_name = models.CharField(db_column='SubSkill_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    effect = models.CharField(db_column='Effect', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subskill'


class SuitStats(models.Model):
    rank_id = models.IntegerField(db_column='Rank_ID', primary_key=True)  # Field name made lowercase.
    battlesuit = models.ForeignKey(Battlesuit, models.DO_NOTHING, db_column='BattleSuit_ID', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    hp = models.SmallIntegerField(blank=True, null=True)
    sp = models.IntegerField(blank=True, null=True)
    atk = models.SmallIntegerField(blank=True, null=True)
    def_field = models.SmallIntegerField(db_column='def', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    crit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suit_stats'


class TraitValk(models.Model):
    suit = models.ForeignKey(Battlesuit, models.DO_NOTHING, db_column='Suit_Id', blank=True, null=True)  # Field name made lowercase.
    trait = models.ForeignKey('Traits', models.DO_NOTHING, db_column='Trait_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trait_valk'


class Traits(models.Model):
    traits_id = models.IntegerField(db_column='Traits_ID', primary_key=True)  # Field name made lowercase.
    trait_name = models.CharField(db_column='Trait_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traits'


class Valkyrie(models.Model):
    valkyrie_id = models.SmallIntegerField(db_column='Valkyrie_ID', primary_key=True)  # Field name made lowercase.
    valkyrie_name = models.CharField(db_column='Valkyrie_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthday_day = models.IntegerField(db_column='Birthday_day')  # Field name made lowercase.
    birthday_month = models.CharField(db_column='Birthday_month', max_length=255)  # Field name made lowercase.
    cn_va = models.CharField(db_column='CN_VA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jp_va = models.CharField(db_column='JP_VA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'valkyrie'


class WeaponList(models.Model):
    weapon_id = models.IntegerField(db_column='Weapon_ID', primary_key=True)  # Field name made lowercase.
    weapon_type = models.ForeignKey('WeaponType', models.DO_NOTHING, db_column='Weapon_type_ID', blank=True, null=True)  # Field name made lowercase.
    weapon_name = models.CharField(db_column='Weapon_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    base_form = models.ForeignKey('self', models.DO_NOTHING, db_column='base_form_ID', blank=True, null=True)  # Field name made lowercase.
    pri_arm = models.ForeignKey('self', models.DO_NOTHING, db_column='Pri_Arm_ID', related_name='weaponlist_pri_arm_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weapon_list'


class WeaponRanks(models.Model):
    wrank_id = models.IntegerField(db_column='WRank_ID', primary_key=True)  # Field name made lowercase.
    weapon = models.ForeignKey(WeaponList, models.DO_NOTHING, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    crit = models.IntegerField(blank=True, null=True)
    effect_description_1 = models.CharField(max_length=255, blank=True, null=True)
    effect_description_2 = models.CharField(max_length=255, blank=True, null=True)
    effect_description_3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weapon_ranks'


class WeaponType(models.Model):
    weapon_type_id = models.IntegerField(db_column='Weapon_type_ID', primary_key=True)  # Field name made lowercase.
    weapon_type_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weapon_type'


class Weaponeffectcomponents(models.Model):
    id = models.IntegerField(primary_key=True)
    weapon = models.ForeignKey(WeaponList, models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    effect_template = models.ForeignKey('Weaponeffecttemplates', models.DO_NOTHING, blank=True, null=True)
    value_key = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weaponeffectcomponents'


class Weaponeffecttemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    effect_name = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weaponeffecttemplates'
