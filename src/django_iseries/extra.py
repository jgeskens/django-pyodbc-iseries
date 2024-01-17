from django.db.models import Exists as DjangoExists


class Exists(DjangoExists):
    template = "%(subquery)s"

    def select_format(self, compiler, sql, params):
        print(params)
        sql = f'''(
            SELECT 1 FROM SYSIBM.SYSDUMMY1 WHERE EXISTS({sql})
            UNION
            SELECT 0 FROM SYSIBM.SYSDUMMY1 WHERE NOT EXISTS({sql})
        )'''
        return sql, list(params) * 2
