# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wavefront-api-client"
VERSION = "2.119.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Wavefront REST API",
    author_email="chitimba@wavefront.com",
    url="https://github.com/wavefrontHQ/python-client",
    keywords=["Swagger", "Wavefront REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;p&gt;The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.&lt;/p&gt;&lt;p&gt;When you make REST API calls outside the Wavefront REST API documentation you must add the header \&quot;Authorization: Bearer &amp;lt;&amp;lt;API-TOKEN&amp;gt;&amp;gt;\&quot; to your HTTP requests.&lt;/p&gt;  # noqa: E501
    """
)
