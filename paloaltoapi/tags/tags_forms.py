# pylint: disable=line-too-long
"""XML Form for Tags"""

xml_unregister_tag = {
    "form": "<uid-message><type>update</type><payload><unregister>{}</unregister></payload></uid-message>",
    "item": '<entry ip="{}"><tag><member>{}</member></tag></entry>'
}

xml_register_tag = {
    "form": '<uid-message><type>update</type><payload><register>{}</register></payload></uid-message>',
    "item": '<entry ip="{}" persistent="{}"><tag><member timeout="{}">{}</member></tag></entry>'
}

"""
<uid-message>
  <type>update</type>
  <payload>
    <unregister>
      <entry ip="10.0.0.8">
        <tag>
          <member>DAG-Isolation</member>
        </tag>
      </entry>
    </unregister>
  </payload>
</uid-message>
"""
