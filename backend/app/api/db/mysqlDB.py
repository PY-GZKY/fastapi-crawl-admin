# -*- coding: utf-8 -*-
from app.api.db.session import SessionLocal
from app.api.logger import logger


class Database(object):

    def __init__(self):
        self.db_ojb = SessionLocal()

    def bulk_save(self, sql_table, item_list):
        try:
            self.db_ojb.bulk_save_objects(item_list)
            self.db_ojb.commit()
            logger.debug("[+] 插入成功 !!! " + "=========  " + sql_table + "   ========")
            return True
        except Exception as e:
            self.db_ojb.rollback()
            logger.error("产生回滚 !!!   回滚信息: ")
            logger.error(e)
            logger.error("[-] Mysql 插入时产生错误")
            return False

    def insert(self, sql_table, item):
        mysql_table_obj = eval(sql_table)
        try:
            core = mysql_table_obj(**item)
            self.db_ojb.add(core)
            self.db_ojb.commit()
            logger.debug("[+] 插入成功 !!! " + "=========  " + sql_table + "   ========")

        except Exception as e:
            self.db_ojb.rollback()
            logger.error("[-] 产生回滚 !!!   回滚信息: ")
            logger.error(e)
            raise Exception("[-] Mysql 插入时产生错误 ...... fail")

    def query(self, sql_table):
        mysql_table_obj = eval(sql_table)
        result = self.db_ojb.query(mysql_table_obj).all()
        return result

    def delete_log(self, sql_table, spiderId):
        try:
            self.db_ojb.query(sql_table).filter(sql_table.spiderId == spiderId).delete(synchronize_session=False)
            self.db_ojb.commit()
            return True
        except:
            self.db_ojb.rollback()
            logger.error("[-] 产生回滚 !!!   回滚信息: ")
            return False

    def delete(self, sql_table):
        try:
            self.db_ojb.query(sql_table).delete(synchronize_session=False)
            self.db_ojb.commit()
            return True
        except:
            self.db_ojb.rollback()
            logger.error("[-] 产生回滚 !!!   回滚信息: ")
            return False

    def __exit__(self):
        self.db_ojb.close()
