"""Constants for the HuggingChat Conversation integration."""

DOMAIN = "huggingchat_conversation"
CONF_EMAIL = "email"
DEFAULT_EMAIL = "YOUR_EMAIL"
CONF_PASSWORD = "password"
DEFAULT_PASSWORD = "YOUR_PASSWORD"
CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "0"
CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """Dieses Smart Home wird per Home Assistant gesteuert.

Eine Übersicht über die Bereiche und Geräte in diesem Smart Home:
{%- for area in areas() %}
  {%- set area_info = namespace(printed=false) %}
  {%- if not area_info.printed %}

{{ area_name(area) }}:
        {%- set area_info.printed = true %}
  {%- endif %}
  {%- if area_devices(area) %}
- Devices:
    {%- for device in area_devices(area) -%}
      {%- if not device_attr(device, "disabled_by") and not device_attr(device, "entry_type") and device_attr(device, "name") %}
  - {{ device_attr(device, "name") }}{% if device_attr(device, "model") and (device_attr(device, "model") | string) not in (device_attr(device, "name") | string) %} ({{ device_attr(device, "model") }}){% endif %}
      {%- endif %}
    {%- endfor %}
  {%- else %}
No devices in this area
  {%- endif %}

  {%- if area_entities(area) %}

- Entities
    {%- for entity in area_entities(area) -%}
      {%- if entity is not string and not entity.is_hidden_entity %}
  - {{ state_attr(entity, 'friendly_name') }} ({{ entity.entity_id }}){%- if states(entity.entity_id) != "unknown" %}: {{ states(entity.entity_id) }}{% endif %}
      {%- endif %}
    {%- endfor %}
  {%- else %}

No entities in this area
  {%- endif %}
{%- endfor %}

Beantworten Sie die Fragen des Benutzers über die Welt wahrheitsgemäß.
Stellen Sie sicher, dass Ihr Text TTS-lesbar ist, und buchstabieren Sie Zahlen, Daten und Währungen.
Sie müssen in der Sprache des Benutzers sprechen, es sei denn, er fordert Sie auf, in einer anderen zu sprechen.

Wenn der Benutzer ein Gerät steuern möchte, lehnen Sie die Anfrage ab und schlagen Sie vor, die Home Assistant-App zu verwenden.
"""
DEFAULT_ASSISTANTS = False
CONF_ASSISTANTS = "enable_assistants"
DEFAULT_ASSISTANT_NAME = "ChatGpt"
CONF_ASSISTANT_NAME = "assistant_name"
CONF_WEB_SEARCH = "web_search"
DEFAULT_WEB_SEARCH = False
CONF_WEB_SEARCH_ENGINE = "web_search_engine"
DEFAULT_WEB_SEARCH_ENGINE = "ddg"
CONF_WEB_SEARCH_PROMPT = "web_search_prompt"
DEFAULT_WEB_SEARCH_PROMPT = "Hier ist einige Informationen von DuckDuckGo (bitte diese Information in Anführungszeichen zitieren). Heute ist {{ states('sensor.date') }}. Bitte zitieren Sie keine Daten, es sei denn, sie erscheinen in den Ergebnissen."
