from service.sql import find_column_name
import re


def database_transfer(output_db, input_db, tables):
    def tuple_to_str(val):
        datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
        arr = []
        for v in list(val):
            if re.match(datetime_pattern, str(v)):
                arr.append('"' + str(v) + '"')
            else:
                arr.append(str(v))
        return ",".join(arr)

    output_db.connect()
    input_db.connect()
    for table in tables:
        rows_count = output_db.query_one(f'SELECT COUNT(*) FROM {table}')
        print(f"rows_countrows_countrows_countrows_count  {rows_count}")
        if rows_count[0] > 0:
            column_names = find_column_name(output_db, table)
            print(f'!!!!!!!!!!!!!!!!!{column_names}')
            rows = output_db.query_all(f'SELECT * FROM {table}')
            print(f'!!!!!!!!!!!!!!!!!{rows}')
            for row in rows:
                print(f"---------{row}")
                print(f"---------{list(row)}")
                print(
                    f'INSERT INTO {table} ({column_names}) VALUES ({tuple_to_str(row)})')
                input_db.sql(
                    f'INSERT INTO {table} ({column_names}) VALUES ({tuple_to_str(row)})')
                input_db.commit_changes()
