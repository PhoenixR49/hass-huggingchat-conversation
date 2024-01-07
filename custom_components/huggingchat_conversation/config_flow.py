"""Config flow for HuggingChat Conversation integration."""
from __future__ import annotations

import logging
import types
from types import MappingProxyType
from typing import Any

from hugchat.login import Login
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.selector import (
    NumberSelector,
    NumberSelectorConfig,
    TemplateSelector,
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)

from .const import (
    CONF_CHAT_MODEL,
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_PROMPT,
    DEFAULT_CHAT_MODEL,
    DEFAULT_EMAIL,
    DEFAULT_PASSWORD,
    DEFAULT_PROMPT,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_EMAIL): TextSelector(
            TextSelectorConfig(type=TextSelectorType.EMAIL, autocomplete="email")
        ),
        vol.Required(CONF_PASSWORD): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.PASSWORD, autocomplete="password"
            )
        ),
    }
)

DEFAULT_OPTIONS = types.MappingProxyType(
    {
        CONF_EMAIL: DEFAULT_EMAIL,
        CONF_PASSWORD: DEFAULT_PASSWORD,
        CONF_CHAT_MODEL: DEFAULT_CHAT_MODEL,
        CONF_PROMPT: DEFAULT_PROMPT,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    # email = data[CONF_EMAIL]
    # passwd = data[CONF_PASSWORD]

    # Log in to huggingface and grant authorization to huggingchat
    sign = Login(data[CONF_EMAIL], data[CONF_PASSWORD])
    await hass.async_add_executor_job(sign.login)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HuggingChat Conversation."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=STEP_USER_DATA_SCHEMA
            )

        errors = {}

        try:
            await validate_input(self.hass, user_input)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "invalid_auth"
        else:
            return self.async_create_entry(title="HuggingChat Conversation", data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

    @staticmethod
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Create the options flow."""
        return OptionsFlow(config_entry)


class OptionsFlow(config_entries.OptionsFlow):
    """HuggingChat config flow options handler."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="HuggingChat Conversation", data=user_input)
        schema = huggingchat_config_option_schema(self.config_entry.options)
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(schema),
        )


def huggingchat_config_option_schema(options: MappingProxyType[str, Any]) -> dict:
    """Return a schema for HuggingChat completion options."""
    if not options:
        options = DEFAULT_OPTIONS
    return {
        vol.Optional(
            CONF_PROMPT,
            description={"suggested_value": options[CONF_PROMPT]},
            default=DEFAULT_PROMPT,
        ): TemplateSelector(),
        vol.Optional(
            CONF_CHAT_MODEL,
            description={"suggested_value": options[CONF_CHAT_MODEL]},
            default=DEFAULT_CHAT_MODEL,
        ): NumberSelector(NumberSelectorConfig(min=0, max=5, step=1)),
    }
