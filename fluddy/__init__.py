#!/usr/bin/python3
# -*- coding: utf-8 -*-
# noreorder
__title__ = 'fluddy'
__version__ = '0.0.3'
__author__ = 'Jacob Dent'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2020 Jacob Dent'
__flask_version__ = '1.1.1'
__dot_env_version__ = '0.10.5'
__ascii__ = r"""

  ##    ##               #      #        
  #  #    #               #      #        
  #       #    #   #   ## #   ## #  #   # 
 ####     #    #   #  #  ##  #  ##  #   # 
  #       #    #   #  #   #  #   #  #  ## 
  #       #    #  ##  #  ##  #  ##   ## # 
  #      ###    ## #   ## #   ## #      # 
                                    #   # 
  Version 0.0.3                      ### 

"""
__windows_ascii__ = r"""


@echo off
echo ##    ##               #      #        
echo #  #    #               #      #        
echo #       #    #   #   ## #   ## #  #   # 
echo ###     #    #   #  #  ##  #  ##  #   # 
echo #       #    #   #  #   #  #   #  #  ## 
echo #       #    #  ##  #  ##  #  ##   ## # 
echo #      ###    ## #   ## #   ## #      # 
echo                                    #   # 
echo Version 0.0.3                       ### 


"""


from fluddy.logs import create_logger
from fluddy.bud import initialize_flask_buddy
from fluddy.user_os import SetOS
from fluddy.flask_port import FlaskPort
from fluddy.create import create_flask_app
from fluddy.launcher import initialise_project
from fluddy.cli import main

logger = create_logger()
logger.info('%s v%s', __title__, __version__)
