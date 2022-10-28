from setuptools import setup

setup(
    use_scm_version={
        'write_to': 'src/cloud_tasks_deferred_v2/__version__.py',
        'write_to_template': '__version__ = {version!r}\n',
    }
)
