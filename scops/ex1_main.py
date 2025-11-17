import ex1_config as config

print(config.version)   # access global variables as module attributes
print(config.debug)

config.show_info()      # function uses the same global variables inside the module
