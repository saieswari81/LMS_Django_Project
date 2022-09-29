
class AppRouter:

    def db_for_read(self, model, **hints):
        """
        SET DB Connection for Apps
        """
        if model._meta.app_label == 'lms':
            return 'LOANS'

        return None 

    def db_for_write(self, model, **hints):
        """
        SET DB Connection for Apps
        """
        if model._meta.app_label == 'lms':
            return 'LOANS'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        SET DB Connection for Apps
        """
        if obj1._meta.app_label == 'lms' or \
           obj2._meta.app_label == 'lms':
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        SET DB Connection for Apps
        """
        if app_label == 'lms':
            return 'LOANS'

        return None
