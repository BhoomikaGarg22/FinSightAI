from backend.db import get_connection


def save_chat(user_id, question, answer):
    """
    Save a chat conversation.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats (
            user_id,
            question,
            answer
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            question,
            answer,
        ),
    )

    conn.commit()
    conn.close()


def get_chat_history(user_id):
    """
    Get all chats for a user.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM chats
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,),
    )

    chats = cursor.fetchall()

    conn.close()

    return chats


def delete_chat(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM chats
        WHERE id = ?
        """,
        (chat_id,),
    )

    conn.commit()
    conn.close()


def clear_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM chats
        WHERE user_id = ?
        """,
        (user_id,),
    )

    conn.commit()
    conn.close()