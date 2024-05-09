# Home Assistant HuggingChat Conversation

Conversation support for Home Assistant using HuggingChat.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

[![Community forum](https://img.shields.io/badge/community-forum-green?link=https%3A%2F%2Fcommunity.home-assistant.io%2Ft%2Fhuggingchat-integration%2F668518&style=for-the-badge)](https://community.home-assistant.io/t/huggingchat-integration/668518)
[![GitHub License](https://img.shields.io/github/license/PhoenixR49/hass-huggingchat-conversation?style=for-the-badge)](https://github.com/PhoenixR49/hass-huggingchat-conversation?tab=GPL-3.0-1-ov-file#readme)
[![GitHub Release](https://img.shields.io/github/v/release/PhoenixR49/hass-huggingchat-conversation?style=for-the-badge)](https://github.com/PhoenixR49/hass-huggingchat-conversation/releases)
[![installations](https://img.shields.io/endpoint?url=https://ha-analytics.vaskivskyi.com/badges/huggingchat_conversation/total.json&style=for-the-badge&color=blue)](https://github.com/Vaskivskyi/ha-analytics)

## Installation

- Install HuggingChat Conversation:
  - With [HACS](https://hacs.xyz) (recommended).

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=PhoenixR49&repository=hass-huggingchat-conversation&category=Integration)

    OR
    - Select Frontend.
    - Open the menu at the top right and use the Customised repositories option to add the card's repository.
    - Add the address of the repository with the category `Integration`, and press ADD. The card repository appears in the list.
    - The card for this new repository will be displayed. Click on INSTALL.
    - Restart Home Assistant
  - Manual
    - Clone the repository

      - ```bash
        git clone https://github.com/PhoenixR49/hass-huggingchat-conversation
        ```

    - Add the contents of the custom_component folder to the following path in your Home Assistant configuration: `/config/custom_components`.
    - Restart Home Assistant

## Star History

<a href="https://star-history.com/#PhoenixR49/hass-huggingchat-conversation&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PhoenixR49/hass-huggingchat-conversation&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PhoenixR49/hass-huggingchat-conversation&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PhoenixR49/hass-huggingchat-conversation&type=Date" />
  </picture>
</a>

## Credits

Many thanks to [Soulter](https://github.com/Soulter) for its [HuggingChat Python API](https://github.com/Soulter/hugging-chat-api) and to [deedy5](https://github.com/deedy5) for its [DuckDuckGo API](https://github.com/deedy5/duckduckgo_search).

Integration built with the [OpenAI Conversation](https://github.com/home-assistant/core/blob/dev/homeassistant/components/openai_conversation) by [Paulus Schoutsen](https://github.com/balloob) and the [OpenAI Custom Conversation](https://github.com/drndos/hass-openai-custom-conversation) by [Filip Bednárik](https://github.com/drndos/).
