from .enums import Dialects
from .queries import (
    Query,
    QueryBuilder,
)


class MySQLQuery(Query):
    """
    Defines a query class for use with MySQL.
    """

    @classmethod
    def _builder(cls):
        return QueryBuilder(quote_char='`', dialect=Dialects.MYSQL, wrap_union_queries=False)


class VerticaQuery(Query):
    """
    Defines a query class for use with Vertica.
    """

    @classmethod
    def _builder(cls):
        return QueryBuilder(dialect=Dialects.VERTICA)


class OracleQuery(Query):
    """
    Defines a query class for use with Oracle.
    """

    @classmethod
    def _builder(cls):
        return QueryBuilder(dialect=Dialects.ORACLE)


class PostgreSQLQuery(Query):
    """
    Defines a query class for use with PostgreSQL.
    """

    @classmethod
    def _builder(cls):
        return QueryBuilder(dialect=Dialects.POSTGRESQL)


class MSSQLQuery(Query):
    """
    Defines a query class for use with Microsoft SQL Server.
    """

    @classmethod
    def _builder(cls):
        return QueryBuilder(dialect=Dialects.MSSQL)
