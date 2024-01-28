import psycopg2


def deleting_all(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
        DROP TABLE client_numbers;
        DROP TABLE clients;
        """
        )


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
        CREATE TABLE IF NOT EXISTS clients(
            client_id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) UNIQUE,
            last_name VARCHAR(40),
            email VARCHAR(40) UNIQUE
        )
        """
        )

        cur.execute(
            """
        CREATE TABLE IF NOT EXISTS client_numbers(
            id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES clients(client_id),
            number INT8
        )
        """
        )
        conn.commit()


def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute(
            """
        INSERT INTO clients(first_name, last_name, email) 
        VALUES (%s, %s, %s)
        RETURNING client_id
        """,
            (first_name, last_name, email),
        )
        client_id = cur.fetchone()[0]

    if phones:
        for phone in phones:
            with conn.cursor() as cur:
                cur.execute(
                    """
                INSERT INTO client_numbers(client_id, number) VALUES (%s, %s);
                """,
                    (client_id, phone),
                )

    return client_id


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute(
            """
        INSERT INTO client_numbers(client_id, number) VALUES (%s, %s);
        """,
            (client_id, phone),
        )
    conn.commit()


def change_client(
    conn, client_id, first_name=None, last_name=None, email=None, phones=None
):
    update_fields = []
    params = [client_id]

    if first_name is not None:
        update_fields.append("first_name = %s")
        params.append(first_name)
    if last_name is not None:
        update_fields.append("last_name = %s")
        params.append(last_name)
    if email is not None:
        update_fields.append("email = %s")
        params.append(email)

    if update_fields:
        with conn.cursor() as cur:
            cur.execute(
                """
            UPDATE clients
            SET {}
            WHERE client_id = %s;
            """.format(
                    ", ".join(update_fields)
                ),
                params,
            )

    if phones is not None:
        delete_phone(conn, client_id, None)
        for phone in phones:
            add_phone(conn, client_id, phone)

    conn.commit()


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute(
            """
        DELETE FROM client_numbers
        WHERE client_id = %s AND (number  = %s OR %s IS NULL);
        """,
            (client_id, phone, phone),
        )
    conn.commit()


def delete_client(conn, client_id):
    delete_phone(conn, client_id, None)
    with conn.cursor() as cur:
        cur.execute(
            """
        DELETE FROM clients
        WHERE client_id = %s;
        """,
            (client_id,),
        )
    conn.commit()


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cursor = conn.cursor()

    query = "SELECT c.* FROM clients c WHERE TRUE"
    parameters = []

    if first_name:
        query += " AND c.first_name = %s"
        parameters.append(first_name)

    if last_name:
        query += " AND c.last_name = %s"
        parameters.append(last_name)

    if email:
        query += " AND c.email = %s"
        parameters.append(email)

    if phone:
        query += " AND EXISTS (SELECT 1 FROM phones p WHERE p.client_id = c.client_id AND p.phone_number = %s)"
        parameters.append(phone)

    cursor.execute(query, parameters)
    clients = cursor.fetchall()

    return clients


if __name__ == "__main__":
    with psycopg2.connect(
        database="netology_db", user="postgres", password="Fvbhjirf1997"
    ) as conn:
        deleting_all(conn)
        # Создаем базу данных
        create_db(conn)

        # добавляем клиента
        add_client(
            conn, "Anton", "Antonov", "anton@antonov.ru", ["1234567890", "9876543210"]
        )

        # изменяем информацию о клиенте
        change_client(conn, client_id=1, email="new@client.ru")

        # добавляем новый телефон к уже существующему клиенту
        add_phone(conn, client_id=1, phone="5555555555")

        # ищем клиента
        matching_clients = find_client(conn, first_name="Anton", last_name="Antonov")
        print("Клиенты, соответствующие поиску:")
        for client in matching_clients:
            print(
                f"ID: {client[0]}, Имя: {client[1]}, Фамилия: {client[2]}, электронная почта: {client[3]}"
            )

        # удаляем телефон
        delete_phone(conn, client_id=1, phone="9876543210")

        # удаляем клиента и его телефонные номера
        delete_client(conn, client_id=1)

    conn.close()
