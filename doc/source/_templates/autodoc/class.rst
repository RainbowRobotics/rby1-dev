{# _templates/autodoc/class.rst #}
.. py:class:: {{ fullname }}
   :module: {{ module }}
{% if show_inheritance %}   :show-inheritance:
{% endif %}
{% if bases %}   :bases: {{ bases | join(', ') }}
{% endif %}

{% if docstring %}
{{ docstring }}
{% endif %}

{# 멤버 수집 결과(members)는 conf.py의 autodoc_member_order에 따라 이미 정렬되어 들어옵니다.
   여기서는 'groupwise'로만 재배치하고, 각 그룹 내부 순서는 그대로(bysource) 유지합니다. #}

{# 그룹 분리 #}
{% set mems = members or [] %}
{% set attributes = mems | selectattr("type","in",["attribute","data"]) | list %}
{% set properties = mems | selectattr("type","equalto","property") | list %}
{% set methods = mems | selectattr("type","in",["method","classmethod","staticmethod"]) | list %}
{% set others = mems
    | rejectattr("type","in",["attribute","data","property","method","classmethod","staticmethod"])
    | list %}

{% if attributes %}
Attributes
----------
{% for m in attributes %}
.. autoattribute:: {{ fullname }}.{{ m.name }}
{% endfor %}
{% endif %}

{% if properties %}
Properties
----------
{% for m in properties %}
.. autoattribute:: {{ fullname }}.{{ m.name }}
{% endfor %}
{% endif %}

{% if methods %}
Methods
-------
{% for m in methods %}
.. automethod:: {{ fullname }}.{{ m.name }}
{% endfor %}
{% endif %}

{% if others %}
Others
------
{% for m in others %}
.. auto{{ m.type }}:: {{ fullname }}.{{ m.name }}
{% endfor %}
{% endif %}
