# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wavefront-api-client"
VERSION = "2.3.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["certifi>=2017.4.17",
            "python-dateutil>=2.1",
            "six>=1.10",
            "urllib3>=1.21.1"]

setup(
    name=NAME,
    version=VERSION,
    description="Wavefront Public API",
    author="Wavefront",
    author_email="support@wavefront.com",
    url="https://github.com/wavefrontHQ/python-client",
    keywords=["Swagger", "Wavefront Public API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;p&gt;The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.&lt;/p&gt;&lt;p&gt;When you make API calls outside the Wavefront API documentation you must add the header \&quot;Authorization: Bearer &amp;lt;&amp;lt;API-TOKEN&amp;gt;&amp;gt;\&quot; to your HTTP requests.&lt;/p&gt;&lt;p&gt;For legacy versions of the Wavefront API, see the &lt;a href&#x3D;\&quot;/api-docs/ui/deprecated\&quot;&gt;legacy API documentation&lt;/a&gt;.&lt;/p&gt;  # noqa: E501
    """
)
