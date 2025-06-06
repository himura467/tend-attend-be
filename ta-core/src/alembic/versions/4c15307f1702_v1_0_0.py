"""v1.0.0

Revision ID: 4c15307f1702
Revises:
Create Date: 2025-02-10 23:35:59.044022

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4c15307f1702"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_common() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "host_account",
        sa.Column(
            "host_name", mysql.VARCHAR(length=64), nullable=False, comment="Host Name"
        ),
        sa.Column(
            "hashed_password",
            mysql.VARCHAR(length=512),
            nullable=False,
            comment="Hashed Password",
        ),
        sa.Column(
            "refresh_token",
            mysql.VARCHAR(length=512),
            nullable=True,
            comment="Refresh Token",
        ),
        sa.Column(
            "email", mysql.VARCHAR(length=64), nullable=False, comment="Email Address"
        ),
        sa.Column(
            "user_id", mysql.BIGINT(unsigned=True), nullable=True, comment="User ID"
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_host_account")),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("host_name"),
        sa.UniqueConstraint("user_id"),
        info={"shard_ids": ("common",)},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_host_account_created_at"), "host_account", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_host_account_updated_at"), "host_account", ["updated_at"], unique=False
    )
    op.create_table(
        "guest_account",
        sa.Column(
            "guest_first_name",
            mysql.VARCHAR(length=64),
            nullable=False,
            comment="Guest First Name",
        ),
        sa.Column(
            "guest_last_name",
            mysql.VARCHAR(length=64),
            nullable=False,
            comment="Guest Last Name",
        ),
        sa.Column(
            "guest_nickname",
            mysql.VARCHAR(length=64),
            nullable=True,
            comment="Guest Nickname",
        ),
        sa.Column(
            "birth_date",
            mysql.DATETIME(timezone=True),
            nullable=False,
            comment="Birth Date",
        ),
        sa.Column(
            "gender", mysql.ENUM("MALE", "FEMALE"), nullable=False, comment="Gender"
        ),
        sa.Column(
            "hashed_password",
            mysql.VARCHAR(length=512),
            nullable=False,
            comment="Hashed Password",
        ),
        sa.Column(
            "refresh_token",
            mysql.VARCHAR(length=512),
            nullable=True,
            comment="Refresh Token",
        ),
        sa.Column(
            "user_id", mysql.BIGINT(unsigned=True), nullable=False, comment="User ID"
        ),
        sa.Column("host_id", mysql.VARCHAR(length=36), nullable=False),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["host_id"],
            ["host_account.id"],
            name=op.f("fk_guest_account_host_id_host_account"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_guest_account")),
        sa.UniqueConstraint(
            "guest_first_name",
            "guest_last_name",
            "guest_nickname",
            "host_id",
            name=op.f("uq_guest_account_guest_first_name"),
        ),
        sa.UniqueConstraint("user_id"),
        info={"shard_ids": ("common",)},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_guest_account_created_at"),
        "guest_account",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_guest_account_updated_at"),
        "guest_account",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "host_verification",
        sa.Column("host_email", mysql.VARCHAR(length=64), nullable=False),
        sa.Column(
            "verification_token",
            mysql.VARCHAR(length=36),
            nullable=False,
            comment="Verification Token",
        ),
        sa.Column(
            "token_expires_at",
            mysql.DATETIME(timezone=True),
            nullable=False,
            comment="Token Expires At",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["host_email"],
            ["host_account.email"],
            name=op.f("fk_host_verification_host_email_host_account"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_host_verification")),
        info={"shard_ids": ("common",)},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_host_verification_created_at"),
        "host_verification",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_host_verification_token_expires_at"),
        "host_verification",
        ["token_expires_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_host_verification_updated_at"),
        "host_verification",
        ["updated_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade_common() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_host_verification_updated_at"), table_name="host_verification"
    )
    op.drop_index(
        op.f("ix_host_verification_token_expires_at"), table_name="host_verification"
    )
    op.drop_index(
        op.f("ix_host_verification_created_at"), table_name="host_verification"
    )
    op.drop_table("host_verification")
    op.drop_index(op.f("ix_guest_account_updated_at"), table_name="guest_account")
    op.drop_index(op.f("ix_guest_account_created_at"), table_name="guest_account")
    op.drop_table("guest_account")
    op.drop_index(op.f("ix_host_account_updated_at"), table_name="host_account")
    op.drop_index(op.f("ix_host_account_created_at"), table_name="host_account")
    op.drop_table("host_account")
    # ### end Alembic commands ###


def upgrade_sequence() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sequence_user_id",
        sa.Column(
            "id", mysql.BIGINT(unsigned=True), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_sequence_user_id")),
        info={"shard_ids": ("sequence",)},
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###


def downgrade_sequence() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sequence_user_id")
    # ### end Alembic commands ###


def upgrade_shard0() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_attendance",
        sa.Column(
            "event_id", mysql.VARCHAR(length=36), nullable=False, comment="Event ID"
        ),
        sa.Column(
            "start", mysql.DATETIME(timezone=True), nullable=False, comment="Start"
        ),
        sa.Column(
            "state",
            mysql.ENUM("PRESENT", "EXCUSED_ABSENCE", "UNEXCUSED_ABSENCE"),
            nullable=False,
            comment="Attendance State",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event_attendance")),
        sa.UniqueConstraint(
            "user_id", "event_id", "start", name=op.f("uq_event_attendance_user_id")
        ),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_event_attendance_created_at"),
        "event_attendance",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_event_attendance_updated_at"),
        "event_attendance",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "event_attendance_action_log",
        sa.Column(
            "event_id", mysql.VARCHAR(length=36), nullable=False, comment="Event ID"
        ),
        sa.Column(
            "start", mysql.DATETIME(timezone=True), nullable=False, comment="Start"
        ),
        sa.Column(
            "action",
            mysql.ENUM("ATTEND", "LEAVE"),
            nullable=False,
            comment="Attendance Action",
        ),
        sa.Column(
            "acted_at",
            mysql.DATETIME(timezone=True),
            nullable=False,
            comment="Acted At",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event_attendance_action_log")),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_event_attendance_action_log_created_at"),
        "event_attendance_action_log",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_event_attendance_action_log_updated_at"),
        "event_attendance_action_log",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "recurrence_rule",
        sa.Column(
            "freq",
            mysql.ENUM(
                "SECONDLY", "MINUTELY", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"
            ),
            nullable=False,
            comment="FREQ",
        ),
        sa.Column("until", mysql.DATETIME(), nullable=True, comment="UNTIL"),
        sa.Column(
            "count", mysql.SMALLINT(unsigned=True), nullable=True, comment="COUNT"
        ),
        sa.Column(
            "interval",
            mysql.SMALLINT(unsigned=True),
            nullable=False,
            comment="INTERVAL",
        ),
        sa.Column("bysecond", mysql.JSON(), nullable=True, comment="BYSECOND"),
        sa.Column("byminute", mysql.JSON(), nullable=True, comment="BYMINUTE"),
        sa.Column("byhour", mysql.JSON(), nullable=True, comment="BYHOUR"),
        sa.Column("byday", mysql.JSON(), nullable=True, comment="BYDAY"),
        sa.Column("bymonthday", mysql.JSON(), nullable=True, comment="BYMONTHDAY"),
        sa.Column("byyearday", mysql.JSON(), nullable=True, comment="BYYEARDAY"),
        sa.Column("byweekno", mysql.JSON(), nullable=True, comment="BYWEEKNO"),
        sa.Column("bymonth", mysql.JSON(), nullable=True, comment="BYMONTH"),
        sa.Column("bysetpos", mysql.JSON(), nullable=True, comment="BYSETPOS"),
        sa.Column(
            "wkst",
            mysql.ENUM("MO", "TU", "WE", "TH", "FR", "SA", "SU"),
            nullable=False,
            comment="WKST",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_recurrence_rule")),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_table(
        "recurrence",
        sa.Column("rrule_id", mysql.VARCHAR(length=36), nullable=False),
        sa.Column("rdate", mysql.JSON(), nullable=False, comment="RDATE"),
        sa.Column("exdate", mysql.JSON(), nullable=False, comment="EXDATE"),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["rrule_id"],
            ["recurrence_rule.id"],
            name=op.f("fk_recurrence_rrule_id_recurrence_rule"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_recurrence")),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_table(
        "event",
        sa.Column(
            "summary", mysql.VARCHAR(length=64), nullable=False, comment="Summary"
        ),
        sa.Column(
            "location", mysql.VARCHAR(length=64), nullable=True, comment="Location"
        ),
        sa.Column(
            "start", mysql.DATETIME(timezone=True), nullable=False, comment="Start"
        ),
        sa.Column("end", mysql.DATETIME(timezone=True), nullable=False, comment="End"),
        sa.Column("is_all_day", sa.BOOLEAN(), nullable=False, comment="Is All Day"),
        sa.Column("recurrence_id", mysql.VARCHAR(length=36), nullable=True),
        sa.Column(
            "timezone", mysql.VARCHAR(length=64), nullable=False, comment="Timezone"
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["recurrence_id"],
            ["recurrence.id"],
            name=op.f("fk_event_recurrence_id_recurrence"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event")),
        sa.UniqueConstraint("summary"),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_index(op.f("ix_event_created_at"), "event", ["created_at"], unique=False)
    op.create_index(op.f("ix_event_updated_at"), "event", ["updated_at"], unique=False)
    # ### end Alembic commands ###


def downgrade_shard0() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_event_updated_at"), table_name="event")
    op.drop_index(op.f("ix_event_created_at"), table_name="event")
    op.drop_table("event")
    op.drop_table("recurrence")
    op.drop_table("recurrence_rule")
    op.drop_index(
        op.f("ix_event_attendance_action_log_updated_at"),
        table_name="event_attendance_action_log",
    )
    op.drop_index(
        op.f("ix_event_attendance_action_log_created_at"),
        table_name="event_attendance_action_log",
    )
    op.drop_table("event_attendance_action_log")
    op.drop_index(op.f("ix_event_attendance_updated_at"), table_name="event_attendance")
    op.drop_index(op.f("ix_event_attendance_created_at"), table_name="event_attendance")
    op.drop_table("event_attendance")
    # ### end Alembic commands ###


def upgrade_shard1() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_attendance",
        sa.Column(
            "event_id", mysql.VARCHAR(length=36), nullable=False, comment="Event ID"
        ),
        sa.Column(
            "start", mysql.DATETIME(timezone=True), nullable=False, comment="Start"
        ),
        sa.Column(
            "state",
            mysql.ENUM("PRESENT", "EXCUSED_ABSENCE", "UNEXCUSED_ABSENCE"),
            nullable=False,
            comment="Attendance State",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event_attendance")),
        sa.UniqueConstraint(
            "user_id", "event_id", "start", name=op.f("uq_event_attendance_user_id")
        ),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_event_attendance_created_at"),
        "event_attendance",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_event_attendance_updated_at"),
        "event_attendance",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "event_attendance_action_log",
        sa.Column(
            "event_id", mysql.VARCHAR(length=36), nullable=False, comment="Event ID"
        ),
        sa.Column(
            "start", mysql.DATETIME(timezone=True), nullable=False, comment="Start"
        ),
        sa.Column(
            "action",
            mysql.ENUM("ATTEND", "LEAVE"),
            nullable=False,
            comment="Attendance Action",
        ),
        sa.Column(
            "acted_at",
            mysql.DATETIME(timezone=True),
            nullable=False,
            comment="Acted At",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event_attendance_action_log")),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_event_attendance_action_log_created_at"),
        "event_attendance_action_log",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_event_attendance_action_log_updated_at"),
        "event_attendance_action_log",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "recurrence_rule",
        sa.Column(
            "freq",
            mysql.ENUM(
                "SECONDLY", "MINUTELY", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"
            ),
            nullable=False,
            comment="FREQ",
        ),
        sa.Column("until", mysql.DATETIME(), nullable=True, comment="UNTIL"),
        sa.Column(
            "count", mysql.SMALLINT(unsigned=True), nullable=True, comment="COUNT"
        ),
        sa.Column(
            "interval",
            mysql.SMALLINT(unsigned=True),
            nullable=False,
            comment="INTERVAL",
        ),
        sa.Column("bysecond", mysql.JSON(), nullable=True, comment="BYSECOND"),
        sa.Column("byminute", mysql.JSON(), nullable=True, comment="BYMINUTE"),
        sa.Column("byhour", mysql.JSON(), nullable=True, comment="BYHOUR"),
        sa.Column("byday", mysql.JSON(), nullable=True, comment="BYDAY"),
        sa.Column("bymonthday", mysql.JSON(), nullable=True, comment="BYMONTHDAY"),
        sa.Column("byyearday", mysql.JSON(), nullable=True, comment="BYYEARDAY"),
        sa.Column("byweekno", mysql.JSON(), nullable=True, comment="BYWEEKNO"),
        sa.Column("bymonth", mysql.JSON(), nullable=True, comment="BYMONTH"),
        sa.Column("bysetpos", mysql.JSON(), nullable=True, comment="BYSETPOS"),
        sa.Column(
            "wkst",
            mysql.ENUM("MO", "TU", "WE", "TH", "FR", "SA", "SU"),
            nullable=False,
            comment="WKST",
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_recurrence_rule")),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_table(
        "recurrence",
        sa.Column("rrule_id", mysql.VARCHAR(length=36), nullable=False),
        sa.Column("rdate", mysql.JSON(), nullable=False, comment="RDATE"),
        sa.Column("exdate", mysql.JSON(), nullable=False, comment="EXDATE"),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["rrule_id"],
            ["recurrence_rule.id"],
            name=op.f("fk_recurrence_rrule_id_recurrence_rule"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_recurrence")),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_table(
        "event",
        sa.Column(
            "summary", mysql.VARCHAR(length=64), nullable=False, comment="Summary"
        ),
        sa.Column(
            "location", mysql.VARCHAR(length=64), nullable=True, comment="Location"
        ),
        sa.Column(
            "start", mysql.DATETIME(timezone=True), nullable=False, comment="Start"
        ),
        sa.Column("end", mysql.DATETIME(timezone=True), nullable=False, comment="End"),
        sa.Column("is_all_day", sa.BOOLEAN(), nullable=False, comment="Is All Day"),
        sa.Column("recurrence_id", mysql.VARCHAR(length=36), nullable=True),
        sa.Column(
            "timezone", mysql.VARCHAR(length=64), nullable=False, comment="Timezone"
        ),
        sa.Column("id", mysql.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("user_id", mysql.BIGINT(unsigned=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["recurrence_id"],
            ["recurrence.id"],
            name=op.f("fk_event_recurrence_id_recurrence"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event")),
        sa.UniqueConstraint("summary"),
        info={"shard_ids": ("shard0", "shard1")},
        mysql_engine="InnoDB",
    )
    op.create_index(op.f("ix_event_created_at"), "event", ["created_at"], unique=False)
    op.create_index(op.f("ix_event_updated_at"), "event", ["updated_at"], unique=False)
    # ### end Alembic commands ###


def downgrade_shard1() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_event_updated_at"), table_name="event")
    op.drop_index(op.f("ix_event_created_at"), table_name="event")
    op.drop_table("event")
    op.drop_table("recurrence")
    op.drop_table("recurrence_rule")
    op.drop_index(
        op.f("ix_event_attendance_action_log_updated_at"),
        table_name="event_attendance_action_log",
    )
    op.drop_index(
        op.f("ix_event_attendance_action_log_created_at"),
        table_name="event_attendance_action_log",
    )
    op.drop_table("event_attendance_action_log")
    op.drop_index(op.f("ix_event_attendance_updated_at"), table_name="event_attendance")
    op.drop_index(op.f("ix_event_attendance_created_at"), table_name="event_attendance")
    op.drop_table("event_attendance")
    # ### end Alembic commands ###
