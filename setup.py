from setuptools import setup

package_name = 'study_ros2'

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
    description='ROS2 study package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'basic_pub = study_ros2.basic_pub:main',
            'basic_sub = study_ros2.basic_sub:main'
        ],
    },
)
