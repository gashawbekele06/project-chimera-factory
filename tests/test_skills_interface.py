# tests/test_skills_interface.py

import pytest
from skills.fetch_trends import fetch_trends
from skills.generate_multimodal_content import generate_multimodal_content
from skills.publish_content import publish_content


def test_fetch_trends_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        fetch_trends({"niche": "test", "platforms": ["twitter"]})


def test_generate_multimodal_content_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        generate_multimodal_content({
            "topic": "test",
            "goal": "test",
            "persona_voice": ["witty"],
            "tier": "daily",
            "character_reference_id": "test123"
        })


def test_publish_content_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        publish_content({
            "platform": "twitter",
            "caption": "test caption",
            "media_urls": [],
            "disclosure_level": "automated"
        })


def test_fetch_trends_accepts_correct_parameters():
    # Confirms interface accepts optional params
    with pytest.raises(NotImplementedError):
        fetch_trends({
            "niche": "crypto",
            "platforms": ["twitter"],
            "time_window_hours": 12,
            "max_results": 10
        })
