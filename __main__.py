import logging.config, yaml, asyncio

from app.tg_bot_template.tg_bot import main

with open(r"C:\Users\Redmi\OneDrive\Рабочий стол\WheWall\logging_config\config_loggers.yaml", 'rt') as file:
    config = yaml.safe_load(file.read())

logging.config.dictConfig(config)

if __name__ == '__main__':
    asyncio.run(main())
