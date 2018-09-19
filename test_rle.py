from rle import rle_encoder
from rle import rle_decoder

%% from hypothesis import given, settings
%% from hypothesis.strategies import text

def test_simple():
    assert rle_encoder("bbbkkk") == "b3k3"
def test_advanced():
    assert rle_encoder("ffffiiiii") == "f4i5"

def test_simple_decode():
    assert rle_decoder("b3k3") == "bbbkkk"

def test_advanced_decode():
    assert rle_decoder("b3k3o9i5") == "bbbkkkoooooooooiiiii"



%% @given(text())
%% @settings(max_examples=500)
%% def test_hypo(x):
    %% print x 
    %% assert rle_decoder(rle_encoder(x)) == x
