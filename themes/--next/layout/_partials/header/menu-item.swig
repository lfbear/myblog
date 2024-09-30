{% macro render(name, itemName, value) %}

  {%- set itemURL = value.split('||')[0] | trim %}
  {%- if not itemURL.startsWith('http') %}
    {%- set itemURL = itemURL | replace('//', '/') %}
  {%- endif %}
  <li class="menu-item menu-item-{{ itemName | replace(' ', '-') }}">

    {%- set menuIcon = '' %}
    {%- if theme.menu_settings.icons %}
      {%- set menuIcon = '<i class="fa fa-fw fa-' + value.split('||')[1] | trim + '"></i>' %}
    {%- endif %}
    {%- if name=='language'%}
      {%- if page.lang=='en'%}
        {%- set itemURL= '/' %}
        {%- set menuText= '简体中文' %}
      {%- endif%}
      {%- if page.lang=='zh-CN'%}
        {%- set itemURL='/en' %}
        {%- set menuText= 'English' %}
      {%- endif%}
    {%- else %}
      {%- set menuText = __('menu.' + name) | replace('menu.', '') %}
    {%- endif %}
    {%- set menuBadge = '' %}
    {%- if theme.menu_settings.badges %}
      {%- set badges = {
        archives  : site.posts.length,
        categories: site.categories.length,
        tags      : site.tags.length
        }
      %}
      {%- for menu, count in badges %}
        {%- if name == menu %}
          {%- set menuBadge = '<span class="badge">' + count + '</span>' %}
        {%- endif %}
      {%- endfor %}
    {%- endif %}

    {% if page.lang !=='zh-CN' %}
        {%- set itemURL= page.lang + itemURL%}
    {%- endif%}

    {{ next_url(itemURL, menuIcon + menuText + menuBadge, {rel: 'section'}) }}



  </li>

{% endmacro %}
