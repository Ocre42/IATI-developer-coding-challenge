from ..main import get_total_budget_value, valid_year, check_start_year
import os
import pytest

def test_get_total_budget_value():
	fpath = os.path.join(os.path.dirname(__file__),"sample_data_fully_valid_10_rows.csv")
	result = get_total_budget_value(fpath, 2018)
	assert result == float(500)

def test_get_total_budget_wrong_path():
	with pytest.raises(Exception):
		get_total_budget_value("wrongpath.csv", 2018)

def test_valid_year_correct():
	assert True == valid_year(1990)

def test_valid_year_incorrect():
	assert False == valid_year(200)

def test_check_start_year_correct():
	assert True == check_start_year("2018-02-01",2018)

def test_check_start_year_incorrect():
	assert False == check_start_year("2017-02-01",2018)

