import sqlite3


def sql_query(sql_function):

    def execute_sql(*arguments):
        queries, values = sql_function(*arguments)
        with sqlite3.connect('koworking.db') as conn:
            cursor = conn.cursor()
            for query in queries:
                if values !=None:
                    res = cursor.execute(query, values)
                else:
                    res = cursor.execute(query)
                res = res.fetchone()
                return res
    return execute_sql

@sql_query
def init_db():
    sql: str = '''
CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    to_pay FLOAT,
    time_spent REAL
)
''' 
    return [sql], None

@sql_query
def add_user(user_id:int, to_pay:float, time_spent:float):
    sql: str = '''INSERT INTO users(
        user_id,
        to_pay,
        time_spent
    )
    VALUES(?,?,?)
    '''
    return [sql], [user_id, to_pay, time_spent]

@sql_query
def add_user_data(user_id:int, to_pay:float, time_spent:float):
    sql: str = f'''
    UPDATE users 
    SET to_pay = {to_pay:.2f}
    WHERE user_id = {user_id}
    '''
    sql2: str = f'''
    UPDATE users 
    SET time_spent = {time_spent:.2f}
    WHERE user_id = {user_id}
    '''
    return [sql,sql2], None


@sql_query
def get_user_data(user_id: int) -> tuple:
    sql: str = f'''
    SELECT * FROM users WHERE user_id={user_id}
    '''
    return [sql], None



if __name__ == '__main__':
    init_db()
    add_user(1000000,111,1145)
    add_user_data(1000000,99,111)
    print(get_user_data(1000000))

