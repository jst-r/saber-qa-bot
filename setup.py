import setuptools

setuptools.setup(
    name='calculator_bot',
    entry_points={
        'console_scripts': [
            'serve_bot = tg_bot.serve:main',
        ],
    }
)