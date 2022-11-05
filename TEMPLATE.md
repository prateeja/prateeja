# Example

## Repositories

{% for repo in repositories %}
{{ forloop.index }} ![{{ repo.name }}]({{ repo.url }}) [{{ repo.stargazerCount }}]

{{ repo.description }}
<hr />
{% endfor %}
