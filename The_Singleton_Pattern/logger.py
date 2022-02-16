class Logger:
    class __Logger:
        def __init__(self,name):
            self.name=name

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)    

        def write_log(self,type, msg):
            with open(self.name+".log", "a") as log_file:
                log_file.write("{0}:{1}\n".format(type,msg))

        def info(self,msg):
            self.write_log("[INFO]", msg)

        def error(self,msg):
            self.write_log("[ERROR]", msg)

        def critical(self,msg):
            self.write_log("[CRITICAL]", msg)

        def warn(self, msg):
            self.write_log("[WARN]", msg)

        def debug(self, msg):
            self.write_log("DEBUG",msg)
    instance=None
    def __new__(cls,name):
    
        if not Logger.instance:
            Logger.instance=Logger.__Logger(name)

        return Logger.instance
    def __getattr__(self,name):
        return getattr(self.instance,name)

    def __setattr__(self,name):
        return setattr(self.instance, name)
