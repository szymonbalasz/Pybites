import configparser
import re


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        #print(self.config)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        #print (len(self.config.sections()))
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
          (= "envlist" attribute of [tox] section)"""
        envs = self.config["tox"]["envlist"]
        #result = re.split("[^a-zA-Z0-9]", envs)
        result = re.split(r'\n| ,|,', envs)
        #print ([string for string in result if string != ""])
        result = (([string.strip() for string in result if string != ""]))
        print(list(dict.fromkeys(result)))
        return ((list(dict.fromkeys(result))))

    # @property
    # def environments(self):
    #     """Return a list of environments
    #       (= "envlist" attribute of [tox] section)"""
    #     enviroment = sorted([i.lstrip() for i in re.split(r'\n| ,|,', self.config['tox']['envlist']) if i])
    #     return enviroment

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        result = []
        #print("HELLO?")
        #print (len(self.config.sections()))
        for section in self.config.sections():
            #print(self.config.options(section))
            for part in self.config[section]:
                if part == "basepython":
                    #print(self.config[section][part])
                    basepy = self.config[section][part]

                    if basepy not in result:
                        result.append(basepy)
        #print(result)
        #print("\n")
        return result
