from setuptools import setup, find_packages

filepath = 'README.md'

setup(
    name='py_fast_agent',
    version='0.2.0',
    author='DETeam',
    author_email='ldx@destudio.asia',
    description='快速构建智能体 —— 兼容 OpenAI-API',
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["zhipuai"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    
    ],
)
