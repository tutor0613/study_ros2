from setuptools import setup

package_name = 'basic_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kyp',
    maintainer_email='kyp970115@gmail.com',
    description='ROS2 study - basic package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'basic_pub = basic_pkg.basic_pub:main',
            'basic_sub = basic_pkg.basic_sub:main',
            'argument_pub = basic_pkg.argument_pub:main',
            'calculator = basic_pkg.calculator:main'
        ],
    },
)
