"""
Define a new function using the @qgsfunction decorator.

The function accept the following parameters

:param [any]: Define any parameters you want to pass to your function before
              the following arguments.
:param feature: The current feature
:param parent: The QgsExpression object
:param context: If there is an argument called ``context`` found at the last
                position, this variable will contain a ``QgsExpressionContext``
                object, that gives access to various additional information like
                expression variables. E.g. ``context.variable('layer_id')``
:returns: The result of the expression.


The @qgsfunction decorator accepts the following arguments:

:param args: Defines the number of arguments. With ``args='auto'`` the number
             arguments will automatically be extracted from the signature.
:param group: The name of the group under which this expression function will
              be listed.
:param usesgeometry: Set this to False if your function does not access
                     feature.geometry(). Defaults to True.
:param referenced_columns: An array of attribute names that are required to run
                           this function. Defaults to
                           [QgsFeatureRequest.ALL_ATTRIBUTES].
"""

from qgis.core import *
from qgis.gui import *
import hashlib
import os

@qgsfunction(args='auto', group='Custom')
def my_md5sum(value1, feature, parent, context):
    """
    Calculates the sum of the two parameters value1 and value2.
    <h2>Example usage:</h2>
    <ul>
      <li>my_sum(5, 8) -> 13</li>
      <li>my_sum("field1", "field2") -> 42</li>
    </ul>
    """
    print(value1)
    print(context.variable('project_home'))
    
    project_home = context.variable('project_home')
    relative_filename = value1
    fullpath = os.path.join(project_home, relative_filename)
    print(fullpath)
 
    
    
    filehash = hashlib.md5()
    return 'Hallo Stefan'
