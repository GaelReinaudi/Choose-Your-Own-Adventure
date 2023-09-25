from cyoa_game.adventure import Adventure
import cyoa_game.config as config
import pytest
import pytest_check as check


@pytest.mark.asyncio
async def test_end_first_chapter():
    adventure = Adventure(config.OpenAIKeyManager.get_api_key())
    text = await adventure.start()
    check.is_true(
        text.strip().endswith(adventure.end_of_first_part),
        "The text should end with the end of the first part.",
    )


if __name__ == '__main__':
    pytest.main([__file__])
