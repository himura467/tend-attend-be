"""v1.0.3

Revision ID: a3a32fc8cd0b
Revises: 45db29753796
Create Date: 2025-03-19 01:15:34.651349

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a3a32fc8cd0b"
down_revision: Union[str, None] = "45db29753796"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_common() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_email_verification_created_at", table_name="email_verification")
    op.drop_index("ix_email_verification_updated_at", table_name="email_verification")
    op.drop_index("ix_user_account_created_at", table_name="user_account")
    op.drop_index("ix_user_account_updated_at", table_name="user_account")
    # ### end Alembic commands ###


def downgrade_common() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "ix_user_account_updated_at", "user_account", ["updated_at"], unique=False
    )
    op.create_index(
        "ix_user_account_created_at", "user_account", ["created_at"], unique=False
    )
    op.create_index(
        "ix_email_verification_updated_at",
        "email_verification",
        ["updated_at"],
        unique=False,
    )
    op.create_index(
        "ix_email_verification_created_at",
        "email_verification",
        ["created_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def upgrade_sequence() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_sequence() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_shard0() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_event_created_at", table_name="event")
    op.drop_index("ix_event_updated_at", table_name="event")
    op.create_index(op.f("ix_event_user_id"), "event", ["user_id"], unique=False)
    op.drop_index("ix_event_attendance_created_at", table_name="event_attendance")
    op.drop_index("ix_event_attendance_updated_at", table_name="event_attendance")
    op.drop_index(
        "ix_event_attendance_action_log_created_at",
        table_name="event_attendance_action_log",
    )
    op.drop_index(
        "ix_event_attendance_action_log_updated_at",
        table_name="event_attendance_action_log",
    )
    op.create_index(
        op.f("ix_event_attendance_action_log_user_id"),
        "event_attendance_action_log",
        ["user_id", "event_id", "start"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade_shard0() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_event_attendance_action_log_user_id"),
        table_name="event_attendance_action_log",
    )
    op.create_index(
        "ix_event_attendance_action_log_updated_at",
        "event_attendance_action_log",
        ["updated_at"],
        unique=False,
    )
    op.create_index(
        "ix_event_attendance_action_log_created_at",
        "event_attendance_action_log",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_event_attendance_updated_at",
        "event_attendance",
        ["updated_at"],
        unique=False,
    )
    op.create_index(
        "ix_event_attendance_created_at",
        "event_attendance",
        ["created_at"],
        unique=False,
    )
    op.drop_index(op.f("ix_event_user_id"), table_name="event")
    op.create_index("ix_event_updated_at", "event", ["updated_at"], unique=False)
    op.create_index("ix_event_created_at", "event", ["created_at"], unique=False)
    # ### end Alembic commands ###


def upgrade_shard1() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_event_created_at", table_name="event")
    op.drop_index("ix_event_updated_at", table_name="event")
    op.create_index(op.f("ix_event_user_id"), "event", ["user_id"], unique=False)
    op.drop_index("ix_event_attendance_created_at", table_name="event_attendance")
    op.drop_index("ix_event_attendance_updated_at", table_name="event_attendance")
    op.drop_index(
        "ix_event_attendance_action_log_created_at",
        table_name="event_attendance_action_log",
    )
    op.drop_index(
        "ix_event_attendance_action_log_updated_at",
        table_name="event_attendance_action_log",
    )
    op.create_index(
        op.f("ix_event_attendance_action_log_user_id"),
        "event_attendance_action_log",
        ["user_id", "event_id", "start"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade_shard1() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_event_attendance_action_log_user_id"),
        table_name="event_attendance_action_log",
    )
    op.create_index(
        "ix_event_attendance_action_log_updated_at",
        "event_attendance_action_log",
        ["updated_at"],
        unique=False,
    )
    op.create_index(
        "ix_event_attendance_action_log_created_at",
        "event_attendance_action_log",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_event_attendance_updated_at",
        "event_attendance",
        ["updated_at"],
        unique=False,
    )
    op.create_index(
        "ix_event_attendance_created_at",
        "event_attendance",
        ["created_at"],
        unique=False,
    )
    op.drop_index(op.f("ix_event_user_id"), table_name="event")
    op.create_index("ix_event_updated_at", "event", ["updated_at"], unique=False)
    op.create_index("ix_event_created_at", "event", ["created_at"], unique=False)
    # ### end Alembic commands ###
