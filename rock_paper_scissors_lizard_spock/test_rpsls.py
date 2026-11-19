import pytest
from unittest.mock import MagicMock
import rpsls

from rpsls import CHOICES, EXIT_OPTION, SCORE_MAP, get_game_result

# Pure Logic

@pytest.mark.parametrize("player, computer, expected", [
    ("Rock", "Scissors", "You won"),
    ("Rock", "Lizard", "You won"),
    ("Paper", "Spock", "You won"),
    ("Scissors", "Lizard", "You won"),
    ("Lizard", "Paper", "You won"),
    ("Spock", "Rock", "You won"),
    ("Rock", "Paper", "You lost"),
    ("Spock", "Lizard", "You lost"),
])

def test_get_game_result(player, computer, expected):
    assert get_game_result(player, computer) == expected

@pytest.mark.parametrize("hand", CHOICES)
def test_same_hand_is_tie(hand):
    assert get_game_result(hand, hand) == "It's a tie"

def test_score_map_is_complete_and_antisymmetric():
    for a in CHOICES:
        assert set(SCORE_MAP[a]) == set(CHOICES)
        for b in CHOICES:
            assert SCORE_MAP[a][b] == -SCORE_MAP[b][a]

def test_each_hand_beats_exactly_two():
    for a in CHOICES:
        assert sorted(SCORE_MAP[a].values()) == [-1, -1, 0, 1, 1]

# Output
def test_show_hands_prints_both_names(capsys):
     rpsls.show_hands("Rock", "Spock")
     out = capsys.readouterr().out
     assert "You: Rock" in out
     assert "Computer: Spock" in out

# Input / flow (mocked)
def test_play_round_normal(monkeypatch, capsys):
    monkeypatch.setattr(rpsls.random, "choice", MagicMock(return_value="Scissors"))
    monkeypatch.setattr(rpsls, "get_player_choice", MagicMock(return_value="Rock"))
    assert rpsls.play_round() is True
    assert "You won" in capsys.readouterr().out

def test_play_round_exit(monkeypatch):
    monkeypatch.setattr(rpsls, "get_player_choice", MagicMock(return_value=EXIT_OPTION))
    assert rpsls.play_round() is False

def test_main_loops_until_exit(monkeypatch, capsys):
    mock_round = MagicMock(side_effect=[True, True, False])
    monkeypatch.setattr(rpsls, "play_round", mock_round)
    rpsls.main()
    assert mock_round.call_count == 3
    assert "Goodbye" in capsys.readouterr().out