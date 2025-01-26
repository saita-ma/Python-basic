import datetime
class GroupLimitReachedException(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name
        with open("Error log.txt", "a+") as error_log:
            error_log.write(f"\n{error_message} // {datetime.datetime.now().strftime("%c")}")