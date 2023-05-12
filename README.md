# PA03
Programming Assignment 03 of COSI 103A
Group by Yuxuan Xiong and Zone Zhang
Transaction stores financial transactions with the fields.
Tracker offers the user the several options and makes calls to the Transaction class to update the database.
Also contains a suite of tests for the app.




The script of running pylint is:

yuxuanxiong@YuxuanXiong:/mnt/c/Users/79181/OneDrive/Documents/GitHub/PA03$ pylint tracker.py
************* Module tracker
tracker.py:25:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:29:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:30:0: R0912: Too many branches (15/12) (too-many-branches)

-----------------------------------
Your code has been rated at 9.51/10


yuxuanxiong@YuxuanXiong:/mnt/c/Users/79181/OneDrive/Documents/GitHub/PA03$ pylint transaction.py

------------------------------------
Your code has been rated at 10.00/10




The script of running pytest is:

Here is the script running the program:
yuxuanxiong@YuxuanXiong:/mnt/c/Users/79181/OneDrive/Documents/GitHub/PA03$ python3 tracker.py
menu:
            0. quit 
            1. show transactions (enter show)
            2. add transaction (enter add, date fomat: YYYY-MM-DD)
            3. delete transaction (enter delete)
            4. summarize transactions by date (enter date)
            5. summarize transactions by month (enter month)
            6. summarize transactions by year (enter year)
            7. summarize transactions by category (enter category)
            8. print this menu (enter print)

command> quit


yuxuanxiong@YuxuanXiong:/mnt/c/Users/79181/OneDrive/Documents/GitHub/PA03$ python3 tracker.py
menu:
            0. quit
            1. show transactions (enter show)
            2. add transaction (enter add, date fomat: YYYY-MM-DD)
            3. delete transaction (enter delete)
            4. summarize transactions by date (enter date)
            5. summarize transactions by month (enter month)
            6. summarize transactions by year (enter year)
            7. summarize transactions by category (enter category)
            8. print this menu (enter print)

command> show


item #     amount     cateory         date            description
----------------------------------------------------------------------
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
4          12         orange          2021/08/26      this is an orange
----------------------------------------------------------------------



command> add 15 beef 2022/03/28 this is meat 
----------------------------------------------------------------------



command> show


item #     amount     cateory         date            description
----------------------------------------------------------------------
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
4          12         orange          2021/08/26      this is an orange
5          15         beef            2022/03/28      this is meat
----------------------------------------------------------------------



command> print
menu:
            0. quit
            1. show transactions (enter show)
            2. add transaction (enter add, date fomat: YYYY-MM-DD)
            3. delete transaction (enter delete)
            4. summarize transactions by date (enter date)
            5. summarize transactions by month (enter month)
            6. summarize transactions by year (enter year)
            7. summarize transactions by category (enter category)
            8. print this menu (enter print)

----------------------------------------------------------------------



command> date


item #     amount     cateory         date            description
----------------------------------------------------------------------
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
4          12         orange          2021/08/26      this is an orange
5          15         beef            2022/03/28      this is meat
----------------------------------------------------------------------



command> month


item #     amount     cateory         date            description
----------------------------------------------------------------------
5          15         beef            2022/03/28      this is meat
4          12         orange          2021/08/26      this is an orange
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
----------------------------------------------------------------------



command> year


item #     amount     cateory         date            description
----------------------------------------------------------------------
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
4          12         orange          2021/08/26      this is an orange
5          15         beef            2022/03/28      this is meat
----------------------------------------------------------------------



command> add 9 pork 2009/03/26 this is meat

command> year


item #     amount     cateory         date            description
----------------------------------------------------------------------
6          9          pork            2009/03/26      this is meat
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
4          12         orange          2021/08/26      this is an orange
5          15         beef            2022/03/28      this is meat
----------------------------------------------------------------------



command> category


item #     amount     cateory         date            description
----------------------------------------------------------------------
1          10         apple           2021/09/26      this is apple
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
5          15         beef            2022/03/28      this is meat
4          12         orange          2021/08/26      this is an orange
6          9          pork            2009/03/26      this is meat
----------------------------------------------------------------------

command> delete 1
----------------------------------------------------------------------



command> show


item #     amount     cateory         date            description
----------------------------------------------------------------------
2          10         apple           2021/09/26      this is apple
3          10         apple           2021/09/26      this is apple
4          12         orange          2021/08/26      this is an orange
5          15         beef            2022/03/28      this is meat
6          9          pork            2009/03/26      this is meat
----------------------------------------------------------------------



command>


