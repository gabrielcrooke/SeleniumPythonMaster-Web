cd .\src\test

python -m pytest test_003.py --alluredir ..\allure-results
python -m pytest test_007.py --alluredir ..\allure-results
python -m pytest test005.py --alluredir ..\allure-results
python -m pytest test017.py --alluredir ..\allure-results

pause