from backend.db import get_connection


def add_stock(user_id, symbol, company):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if already exists
    cursor.execute(
        """
        SELECT id
        FROM watchlist
        WHERE user_id=? AND symbol=?
        """,
        (user_id, symbol.upper()),
    )

    if cursor.fetchone():
        conn.close()
        return False, "Stock already in watchlist."

    cursor.execute(
        """
        INSERT INTO watchlist(user_id, symbol, company)
        VALUES(?,?,?)
        """,
        (
            user_id,
            symbol.upper(),
            company,
        ),
    )

    conn.commit()
    conn.close()

    return True, "Added successfully."


def get_watchlist(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM watchlist
        WHERE user_id=?
        ORDER BY created_at DESC
        """,
        (user_id,),
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def remove_stock(stock_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE
        FROM watchlist
        WHERE id=?
        """,
        (stock_id,),
    )

    conn.commit()
    conn.close()